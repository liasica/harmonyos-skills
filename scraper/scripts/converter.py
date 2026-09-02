"""接口返回的 HTML -> Markdown 转换，以及 frontmatter 的渲染与读取"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
from markdownify import markdownify

from scripts.paths import strip_signed_params


@dataclass
class ExtractedDoc:
    title: str
    breadcrumb: str
    doc_updated_at: Optional[str]
    markdown: str


_HEADING_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6"]
_LANG_CLASS_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+#.-]{0,20}$")
# 标题文本开头的 [hK] 是站点标注的显示层级：不带标记的 h4 渲染为顶层章节，带 [h2] 的 h4 渲染为再低一级
_LEVEL_MARK_RE = re.compile(r"^\s*\[h([1-6])\]\s*")
# 提示框开头的图标图片（note_3.0-zh-cn.png 之类），页面上显示为「说明」等文字
_NOTE_ICON_RE = re.compile(r"/(note|caution|notice|warning|danger|tip)_[^/]*\.(?:png|gif|svg)$", re.I)
_NOTE_LABELS = {"note": "说明", "caution": "注意", "notice": "须知", "warning": "警告", "danger": "危险", "tip": "提示"}


def convert_api_html(html: str, *, title: str, breadcrumb: str, doc_updated_at: Optional[str],
                     base_url: str) -> ExtractedDoc:
    """把 getDocumentById 返回的正文 HTML 转为 Markdown

    - 开头的 h1 就是标题，标题已进 frontmatter，不重复输出；title 为空时用它兜底
    - 标题文本开头的 [hK] 标记表示比原标签再低 K-1 级，去掉标记并按此调整层级
    - 接口原文顶层章节是 h4（页面渲染为 h2），把标题层级整体上移到从 h2 开始
    - 提示框的图标图片换成「说明」「注意」等文字标签
    - 链接转绝对 URL 并剥掉 CDN 签名参数；没有 href 的空锚点删除
    """
    soup = BeautifulSoup(html, "lxml")
    body = soup.body or soup

    h1 = body.find("h1")
    if h1 is not None:
        if not title.strip():
            title = h1.get_text(strip=True)
        h1.decompose()

    for h in body.find_all(_HEADING_TAGS[1:]):
        first = h.find(string=True)
        m = _LEVEL_MARK_RE.match(first) if first else None
        if m:
            first.replace_with(first[m.end():])
            h.name = f"h{min(6, int(h.name[1]) + int(m.group(1)) - 1)}"

    headings = body.find_all(_HEADING_TAGS[1:])
    levels = [int(h.name[1]) for h in headings]
    if levels:
        shift = min(levels) - 2
        if shift > 0:
            for h in headings:
                h.name = f"h{int(h.name[1]) - shift}"

    # 视频 / 音频没有 Markdown 形式，转成带文字的链接（src 在自身或第一个 <source> 上）
    for media in body.find_all(["video", "audio"]):
        src = media.get("src") or next((s.get("src") for s in media.find_all("source") if s.get("src")), None)
        if src:
            link = soup.new_tag("a", href=src)
            link.string = "视频" if media.name == "video" else "音频"
            media.replace_with(link)
        else:
            media.decompose()

    for a in body.find_all("a"):
        href = a.get("href")
        if href:
            a["href"] = strip_signed_params(urljoin(base_url, href))
        elif not a.get_text(strip=True):
            a.decompose()
    for img in body.find_all("img", src=True):
        src = strip_signed_params(urljoin(base_url, img["src"]))
        m = _NOTE_ICON_RE.search(src)
        if m:
            # 先剥掉签名参数再判断，真实 src 带 ?HW-CC-... 后缀
            label = soup.new_tag("strong")
            label.string = _NOTE_LABELS[m.group(1).lower()]
            img.replace_with(label)
        else:
            img["src"] = src
    # 其余带 src 的元素（source / iframe 等）同样处理
    for el in body.find_all(src=True):
        if el.name != "img":
            el["src"] = strip_signed_params(urljoin(base_url, el["src"]))

    md = markdownify(str(body), heading_style="ATX", code_language_callback=_code_lang)
    md = _post_process(md)
    return ExtractedDoc(title=title.strip(), breadcrumb=breadcrumb,
                        doc_updated_at=doc_updated_at or None, markdown=md)


def _code_lang(tag: Tag) -> str:
    """从 <pre class="TypeScript"> 或 <code class="language-ts"> 取代码语言"""
    candidates = [tag]
    if tag.name == "pre":
        code = tag.find("code")
        if code is not None:
            candidates.append(code)
    for el in candidates:
        classes = el.get("class") or []
        for c in classes:
            if c.startswith("language-"):
                return c[len("language-"):]
        for c in classes:
            if _LANG_CLASS_RE.match(c):
                return c.lower()
    return ""


_URL_RE = re.compile(r"https?://[^\s)\]\"'<>]+")


def _post_process(md: str) -> str:
    # 兜底：正文文本里直接出现的签名 URL 也剥掉参数
    if "HW-CC-" in md:
        md = _URL_RE.sub(lambda m: strip_signed_params(m.group(0)), md)
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


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
