"""从根 URL 渲染侧边栏并抽取所有目录链接"""
from __future__ import annotations

from urllib.parse import urljoin

from bs4 import BeautifulSoup

from scripts.paths import normalize_url


def extract_links_from_html(
    html: str,
    base_url: str,
    selectors: dict,
    allow_prefixes: list[str],
) -> list[dict]:
    """从渲染后的 HTML 抽链接（纯函数，易测）"""
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[dict] = []
    for sel in selectors.get("link_candidates", []):
        for a in soup.select(sel):
            href = a.get("href") or ""
            if not href or href.startswith("#"):
                continue
            absolute = urljoin(base_url, href)
            if not any(absolute.startswith(p) for p in allow_prefixes):
                continue
            normalized = normalize_url(absolute)
            if normalized in seen:
                continue
            seen.add(normalized)
            title = a.get_text(strip=True) or normalized
            out.append({"url": normalized, "title": title})
    return out


async def _expand_tree_fully(page, expandable_selectors: list[str], max_rounds: int = 12) -> int:
    """循环点击所有折叠节点直到收敛或达上限。返回最终展开的 a[href] 数量"""
    last_total = -1
    for _ in range(max_rounds):
        # 收集所有折叠节点
        handles = []
        for sel in expandable_selectors:
            try:
                handles.extend(await page.query_selector_all(sel))
            except Exception:
                pass
        if not handles:
            break
        if len(handles) == last_total:
            break
        last_total = len(handles)
        for h in handles:
            try:
                await h.click(timeout=300)
            except Exception:
                pass
        await page.wait_for_timeout(700)
    return await page.evaluate("() => document.querySelectorAll('.layout-left a[href]').length")


async def discover_from_root(
    root_url: str,
    selectors: dict,
    allow_prefixes: list[str],
    settings: dict,
    *,
    browser_context,
) -> list[dict]:
    """打开 root_url，递归点开所有侧边栏折叠节点，抽出全部 a[href]"""
    page = await browser_context.new_page()
    try:
        await page.goto(root_url, timeout=settings["page_timeout_ms"])
        ready = selectors.get("ready_selector")
        if ready:
            try:
                await page.wait_for_selector(ready, timeout=settings["page_timeout_ms"])
            except Exception:
                pass
        await page.wait_for_timeout(settings.get("extra_wait_ms", 800))
        await _expand_tree_fully(page, selectors.get("expandable_node", []))
        html = await page.content()
        return extract_links_from_html(html, root_url, selectors, allow_prefixes)
    finally:
        await page.close()
