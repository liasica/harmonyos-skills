# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp>=2,<3",
#     "httpx>=0.27",
#     "markdownify>=0.13",
# ]
# ///
"""HarmonyOS 文档 MCP 服务（stdio）

把 harmonyos/references 离线库与华为文档在线接口暴露为 MCP 工具，供任意 MCP 客户端调用：

- list_categories：五个分类及篇数
- search_docs：按标题 / 路径检索 INDEX，或用 rg / grep 全文检索
- read_doc：按相对路径（或华为文档 URL）读取一篇文档，支持分页
- coding_rules：ArkTS / ArkUI 编码强制规则
- fetch_online：调华为 documentPortal 接口拉最新正文（本地没有或怀疑过旧时兜底）

运行：uv run mcp/server.py（依赖由 PEP 723 内联元数据声明，uv 自动准备隔离环境）
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

import httpx
from markdownify import markdownify
from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

REPO_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = REPO_ROOT / "harmonyos" / "references"
INDEX_PATH = REFERENCES / "INDEX.md"
RULES_PATH = REPO_ROOT / "harmonyos" / "rules" / "arkts-coding-rules.md"

DOC_URL_PREFIX = "https://developer.huawei.com/consumer/cn/doc/"
DOC_API = "https://developer.huawei.com/consumer/cn/documentPortal/getDocumentById"

CATEGORY_NAMES = {
    "harmonyos-releases": "版本说明",
    "harmonyos-guides": "指南",
    "harmonyos-references": "API 参考",
    "best-practices": "最佳实践",
    "harmonyos-faqs": "FAQ",
    "harmonyos-roadmap": "变更预告",
}

_INDEX_LINE_RE = re.compile(r"^- \[(.*)\]\(([^)\s]+)\)$")

mcp = MCPServer(
    "harmonyos-docs",
    instructions=(
        "HarmonyOS NEXT 官方文档离线镜像（版本说明 / 指南 / API 参考 / 最佳实践 / FAQ）。"
        "先用 search_docs 找到文档路径，再用 read_doc 读正文；"
        "写 ArkTS / ArkUI 代码前先读 coding_rules；"
        "本地没有命中或怀疑过旧时用 fetch_online 拉线上最新内容。"
        "回答时引用文档的 url 字段作为出处。"
    ),
)


class _Index:
    """INDEX.md 的内存副本，按文件 mtime 自动重载"""

    def __init__(self) -> None:
        self._mtime = -1.0
        self.entries: list[dict[str, str]] = []
        self.by_path: dict[str, dict[str, str]] = {}
        # 文件名（即华为文档的 objectId）-> 条目
        self.by_stem: dict[str, dict[str, str]] = {}

    def load(self) -> "_Index":
        try:
            mtime = INDEX_PATH.stat().st_mtime
        except FileNotFoundError:
            raise ToolError(f"索引不存在：{INDEX_PATH}，请先完成一次文档同步")
        if mtime == self._mtime:
            return self
        entries: list[dict[str, str]] = []
        with INDEX_PATH.open(encoding="utf-8") as f:
            for line in f:
                m = _INDEX_LINE_RE.match(line.rstrip("\n"))
                if not m:
                    continue
                title, path = m.group(1), m.group(2)
                entries.append({"title": title, "path": path, "category": path.split("/", 1)[0]})
        self.entries = entries
        self.by_path = {e["path"]: e for e in entries}
        self.by_stem = {Path(e["path"]).stem: e for e in entries}
        self._mtime = mtime
        return self


_index = _Index()


def _read_frontmatter(path: Path) -> dict[str, str]:
    """读 .md 顶部 frontmatter（只认 `key: value` 单行，值保持原样）"""
    out: dict[str, str] = {}
    try:
        with path.open(encoding="utf-8") as f:
            if f.readline().rstrip("\n") != "---":
                return out
            for line in f:
                line = line.rstrip("\n")
                if line == "---":
                    break
                key, sep, value = line.partition(": ")
                if sep:
                    out[key] = value.strip('"')
    except OSError:
        pass
    return out


def _resolve_doc_path(path: str) -> Path:
    """把用户给的路径 / URL 解析为 references 内的绝对路径，拒绝越界"""
    p = path.strip()
    if p.startswith(DOC_URL_PREFIX):
        # https://developer.huawei.com/consumer/cn/doc/<cat>/<id>?query -> <cat>/<id>.md
        rest = p[len(DOC_URL_PREFIX):].split("?", 1)[0].split("#", 1)[0].rstrip("/")
        p = rest + ".md"
    for prefix in ("harmonyos/references/", "references/"):
        if p.startswith(prefix):
            p = p[len(prefix):]
    target = (REFERENCES / p).resolve()
    if REFERENCES.resolve() not in target.parents:
        raise ToolError(f"路径越界：{path}")
    if not target.is_file():
        raise ToolError(f"文档不存在：{path}（用 search_docs 查找正确路径）")
    return target


def _check_category(category: str | None) -> str | None:
    if category and category not in CATEGORY_NAMES:
        raise ToolError(f"未知分类 {category!r}，可选：{', '.join(CATEGORY_NAMES)}")
    return category


def _entry_with_url(entry: dict[str, str]) -> dict[str, str]:
    fm = _read_frontmatter(REFERENCES / entry["path"])
    return {**entry, "url": fm.get("url", ""), "doc_updated_at": fm.get("doc_updated_at", "")}


def _fulltext_files(query: str, root: Path, limit: int) -> list[str]:
    """用 rg（没有则 grep）做不区分大小写的短语全文检索，返回相对 references 的路径"""
    if shutil.which("rg"):
        cmd = ["rg", "--files-with-matches", "--ignore-case", "--fixed-strings",
               "--glob", "*.md", "--glob", "!INDEX.md", "--max-count", "1", "--", query, str(root)]
    else:
        cmd = ["grep", "-rliF", "--include=*.md", "--exclude=INDEX.md", "--", query, str(root)]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if proc.returncode not in (0, 1):
        raise ToolError(f"全文检索失败：{proc.stderr.strip() or proc.returncode}")
    paths = sorted(str(Path(line).relative_to(REFERENCES)) for line in proc.stdout.splitlines() if line)
    return paths[:limit]


@mcp.tool()
def list_categories() -> list[dict[str, Any]]:
    """列出文档分类（category 标识、中文名、篇数），search_docs / fulltext 的 category 参数取这里的标识"""
    idx = _index.load()
    counts: dict[str, int] = {c: 0 for c in CATEGORY_NAMES}
    for e in idx.entries:
        counts[e["category"]] = counts.get(e["category"], 0) + 1
    return [{"category": c, "name": CATEGORY_NAMES.get(c, c), "count": n} for c, n in counts.items()]


@mcp.tool()
def search_docs(query: str, category: str | None = None, limit: int = 20,
                fulltext: bool = False) -> list[dict[str, str]]:
    """检索 HarmonyOS 文档，返回 title / path / category / url，path 直接传给 read_doc

    默认按标题与路径匹配：query 按空白拆成多个关键词，全部命中才算匹配，不区分大小写。
    fulltext=true 时改为在正文里做短语全文检索（较慢，query 作为一个整体匹配），标题检索没命中时再用。
    category 可限定分类（见 list_categories）。
    """
    _check_category(category)
    q = query.strip()
    if not q:
        raise ToolError("query 不能为空")
    limit = max(1, min(limit, 100))
    idx = _index.load()

    if fulltext:
        root = REFERENCES / category if category else REFERENCES
        hits = [idx.by_path[p] for p in _fulltext_files(q, root, limit) if p in idx.by_path]
        return [_entry_with_url(e) for e in hits]

    terms = [t.lower() for t in q.split()]
    scored: list[tuple[int, int, dict[str, str]]] = []
    for e in idx.entries:
        if category and e["category"] != category:
            continue
        title = e["title"].lower()
        path = e["path"].lower()
        if not all(t in title or t in path for t in terms):
            continue
        in_title = sum(1 for t in terms if t in title)
        # 命中标题的关键词越多越靠前，其次标题越短越靠前（更可能是主题页而非细节页）
        scored.append((-in_title, len(title), e))
    scored.sort(key=lambda x: (x[0], x[1]))
    return [_entry_with_url(e) for _, _, e in scored[:limit]]


@mcp.tool()
def read_doc(path: str, offset: int = 0, max_chars: int = 30000) -> dict[str, Any]:
    """读取一篇文档的正文（Markdown）与元信息

    path 为 search_docs 返回的相对路径（如 harmonyos-guides/application-dev-guide.md），也接受华为文档 URL。
    正文超过 max_chars 时截断，返回 next_offset，用它作为 offset 再次调用读取后续内容。
    """
    target = _resolve_doc_path(path)
    text = target.read_text(encoding="utf-8")
    fm = _read_frontmatter(target)
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            body = text[end + len("\n---\n"):]
    body = body.strip("\n")
    offset = max(0, offset)
    max_chars = max(1000, min(max_chars, 200000))
    chunk = body[offset: offset + max_chars]
    next_offset = offset + max_chars if offset + max_chars < len(body) else None
    return {
        "path": str(target.relative_to(REFERENCES)),
        "url": fm.get("url", ""),
        "title": fm.get("title", ""),
        "breadcrumb": fm.get("breadcrumb", ""),
        "doc_updated_at": fm.get("doc_updated_at", ""),
        "total_chars": len(body),
        "offset": offset,
        "next_offset": next_offset,
        "content": chunk,
    }


@mcp.tool()
def coding_rules() -> str:
    """HarmonyOS 官方 ArkTS / ArkUI / API 使用强制规则，为用户写或改 ArkTS 代码前先读"""
    try:
        return RULES_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ToolError(f"规则文件不存在：{RULES_PATH}")


@mcp.tool()
def fetch_online(url_or_object_id: str) -> dict[str, str]:
    """从华为开发者站在线拉取一篇文档的最新正文（转为 Markdown）

    参数可以是完整文档 URL，也可以只给 URL 最后一段 objectId（如 application-dev-guide）。
    本地库没有命中、或本地 doc_updated_at 明显过旧时使用；结果不写入本地库。
    """
    raw = url_or_object_id.strip()
    object_id = raw.rsplit("/", 1)[-1].split("?", 1)[0].split("#", 1)[0]
    if not object_id:
        raise ToolError("无法从输入中解析 objectId")
    try:
        resp = httpx.post(DOC_API, json={"objectId": object_id, "language": "cn"}, timeout=30.0,
                          headers={"Content-Type": "application/json"})
        resp.raise_for_status()
        data = resp.json()
    except httpx.HTTPError as e:
        raise ToolError(f"请求华为文档接口失败：{e}")
    if data.get("code") != 0 or not data.get("value"):
        raise ToolError(f"华为文档接口返回异常：code={data.get('code')} message={data.get('message', '')}")
    value = data["value"]
    html = (value.get("content") or {}).get("content", "")
    md = markdownify(html, heading_style="ATX").strip() if html else ""
    # 只给 objectId 时从本地索引反查原 URL；本地也没有就留空
    url = raw if raw.startswith(DOC_URL_PREFIX) else ""
    local_path = ""
    local = _index.load().by_stem.get(object_id) if INDEX_PATH.exists() else None
    if local:
        local_path = local["path"]
        url = url or _read_frontmatter(REFERENCES / local_path).get("url", "")
    return {"object_id": object_id, "title": value.get("title", ""), "url": url,
            "local_path": local_path, "markdown": md}


if __name__ == "__main__":
    mcp.run()
