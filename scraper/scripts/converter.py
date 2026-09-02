"""HTML → Markdown 提取与转换"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup, Tag
from markdownify import markdownify

from scripts.paths import strip_signed_params


class ExtractionError(Exception):
    """选择器全部失配，无法从 HTML 抽出正文"""


@dataclass
class ExtractedDoc:
    title: str
    breadcrumb: str
    doc_updated_at: Optional[str]
    markdown: str


_UPDATED_RE = re.compile(r"(\d{4}[-/.]\d{1,2}[-/.]\d{1,2})")


def _first_match(soup: BeautifulSoup, candidates: list[str]) -> Optional[Tag]:
    for sel in candidates:
        node = soup.select_one(sel)
        if node is not None:
            return node
    return None


_UPDATED_HINT_RE = re.compile(r"更新时间[:：]\s*(\d{4}[-/.]\d{1,2}[-/.]\d{1,2})")


def _extract_updated_at(soup: BeautifulSoup, candidates: list[str]) -> Optional[str]:
    node = _first_match(soup, candidates)
    if node is not None:
        m = _UPDATED_RE.search(node.get_text(" ", strip=True))
        if m:
            return m.group(1).replace("/", "-").replace(".", "-")
    # 兜底：全文 grep `更新时间: YYYY-MM-DD`（华为站点未给「更新时间」独立 class）
    text = soup.get_text(" ", strip=True)
    m = _UPDATED_HINT_RE.search(text)
    if m:
        return m.group(1).replace("/", "-").replace(".", "-")
    return None


def _extract_breadcrumb(soup: BeautifulSoup, candidates: list[str]) -> str:
    node = _first_match(soup, candidates)
    if node is None:
        return ""
    parts = [t.strip() for t in node.stripped_strings if t.strip() and t.strip() not in {"/", ">"}]
    return " > ".join(parts)


def extract_and_convert(html: str, selectors: dict, *, base_url: str = "") -> ExtractedDoc:
    soup = BeautifulSoup(html, "lxml")

    title_node = _first_match(soup, selectors.get("title_candidates", []))
    body_node = _first_match(soup, selectors.get("body_candidates", []))
    if title_node is None or body_node is None:
        raise ExtractionError(
            f"selectors failed: title={title_node is not None}, body={body_node is not None}"
        )

    title = title_node.get_text(strip=True)
    breadcrumb = _extract_breadcrumb(soup, selectors.get("breadcrumb_candidates", []))
    doc_updated_at = _extract_updated_at(soup, selectors.get("updated_at_candidates", []))

    body_copy = BeautifulSoup(str(body_node), "lxml")
    for sel in selectors.get("updated_at_candidates", []):
        for n in body_copy.select(sel):
            n.decompose()
    for sel in selectors.get("breadcrumb_candidates", []):
        for n in body_copy.select(sel):
            n.decompose()

    # 把所有 <a href> 转绝对 URL，便于后续按绝对 URL 改写为本仓库相对链接
    if base_url:
        from urllib.parse import urljoin
        for a in body_copy.find_all("a", href=True):
            try:
                a["href"] = urljoin(base_url, a["href"])
            except Exception:
                pass
    # 图片等资源链接带按分钟变化的 CDN 签名参数（HW-CC-Date / HW-CC-Sign 等），
    # 不剥掉的话同一页面每次抓取 hash 都不同，无法判断内容是否真的更新
    for tag, attr in (("a", "href"), ("img", "src")):
        for node in body_copy.find_all(tag, **{attr: True}):
            node[attr] = strip_signed_params(node[attr])

    md = markdownify(str(body_copy), heading_style="ATX", code_language_callback=_code_lang)
    md = _post_process(md)
    return ExtractedDoc(title=title, breadcrumb=breadcrumb,
                        doc_updated_at=doc_updated_at, markdown=md)


_LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^\s)]+)\)")


def rewrite_internal_links(
    markdown: str,
    *,
    from_md_path,
    references_root,
    allow_prefixes: list,
    url_normalizer,
    url_to_relative,
) -> str:
    """把 markdown 中所有指向白名单内的 http(s) 链接改写为相对路径

    - url_normalizer: callable(url) -> normalized_url（用 paths.normalize_url）
    - url_to_relative: callable(url, from_md_path, references_root, allow_prefixes) -> str | None
    """
    from urllib.parse import urlparse

    def repl(m: "re.Match[str]") -> str:
        text, url = m.group(1), m.group(2)
        try:
            fragment = urlparse(url).fragment
            normalized = url_normalizer(url)
            if fragment:
                normalized = f"{normalized}#{fragment}"
            rel = url_to_relative(normalized, from_md_path, references_root, allow_prefixes)
        except Exception:
            return m.group(0)
        if rel is None:
            return m.group(0)
        return f"[{text}]({rel})"
    return _LINK_RE.sub(repl, markdown)


def _code_lang(tag: Tag) -> str:
    code = tag.find("code") if tag.name == "pre" else tag
    if code is None:
        return ""
    classes = code.get("class") or []
    for c in classes:
        if c.startswith("language-"):
            return c[len("language-"):]
    return ""


_UI_NOISE_LINES = {
    "收起", "展开", "自动换行", "复制", "深色代码主题",
    "返回顶部", "查看反馈", "上一篇", "下一篇",
}


def _post_process(md: str) -> str:
    # 移除孤立的 UI 控件文字（华为站代码块周边 toolbar）
    cleaned: list[str] = []
    for line in md.splitlines():
        stripped = line.strip()
        if stripped in _UI_NOISE_LINES:
            continue
        cleaned.append(line)
    md = "\n".join(cleaned)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md


# YAML 纯标量不能以这些指示符开头
_YAML_INDICATORS = set("-?:,[]{}#&*!|>'\"%@`")


def yaml_scalar(value: str) -> str:
    """能作为 YAML 纯标量原样输出就原样输出，否则用 JSON 双引号形式（JSON 字符串是合法的 YAML 双引号标量）

    标题里常见 `xxx: yyy`、以 `@ohos.` 开头等写法，直接输出会让 frontmatter 不是合法 YAML
    """
    if (value and value[0] not in _YAML_INDICATORS and ": " not in value and " #" not in value
            and not value.endswith(":") and value == value.strip()):
        return value
    return json.dumps(value, ensure_ascii=False)


def read_frontmatter(path: Path) -> dict[str, str]:
    """读取 .md 顶部 frontmatter 为 dict，值保持原样（不做 YAML 反转义）

    只认 `key: value` 单行，够用于取 url / content_hash；文件不存在或没有 frontmatter 返回空 dict
    """
    try:
        with path.open(encoding="utf-8") as f:
            if f.readline().rstrip("\n") != "---":
                return {}
            out: dict[str, str] = {}
            for line in f:
                line = line.rstrip("\n")
                if line == "---":
                    return out
                key, sep, value = line.partition(": ")
                if sep:
                    out[key] = value
            return {}
    except OSError:
        return {}


def render_with_frontmatter(
    *,
    markdown: str,
    url: str,
    title: str,
    breadcrumb: str,
    category: str,
    scraped_at: str,
    doc_updated_at: Optional[str],
    content_hash: str,
) -> str:
    lines = ["---"]
    lines.append(f"url: {url}")
    lines.append(f"title: {yaml_scalar(title)}")
    if breadcrumb:
        lines.append(f"breadcrumb: {yaml_scalar(breadcrumb)}")
    lines.append(f"category: {category}")
    lines.append(f"scraped_at: {scraped_at}")
    lines.append(f"doc_updated_at: {doc_updated_at or ''}")
    lines.append(f"content_hash: {content_hash}")
    lines.append("---")
    lines.append("")
    lines.append(markdown.strip())
    lines.append("")
    return "\n".join(lines)


def compute_content_hash(markdown: str) -> str:
    """对 Markdown 正文做规范化后 sha256；忽略空白差异"""
    normalized = re.sub(r"\s+", " ", markdown).strip()
    return "sha256:" + hashlib.sha256(normalized.encode("utf-8")).hexdigest()
