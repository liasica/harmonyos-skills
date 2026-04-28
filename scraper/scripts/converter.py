"""HTML → Markdown 提取与转换"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Optional

from bs4 import BeautifulSoup, Tag
from markdownify import markdownify


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
    # 兜底：全文 grep "更新时间: YYYY-MM-DD"（华为站点未给"更新时间"独立 class）
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
    lines.append(f"title: {title}")
    if breadcrumb:
        lines.append(f"breadcrumb: {breadcrumb}")
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
