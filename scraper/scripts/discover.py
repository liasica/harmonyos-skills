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


async def _expand_tree_fully(page, expandable_selectors: list[str], link_selector: str,
                             max_rounds: int = 12) -> None:
    """循环点击所有折叠节点直到收敛或达上限

    收敛判据同时看折叠节点数与链接数：只看节点数时，展开一层恰好又出现同样多的子节点就会误判收敛
    """
    last_key: tuple[int, int] | None = None
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
        n_links = await page.evaluate("(sel) => document.querySelectorAll(sel).length", link_selector)
        key = (len(handles), n_links)
        if key == last_key:
            break
        last_key = key
        for h in handles:
            try:
                await h.click(timeout=300)
            except Exception:
                pass
        await page.wait_for_timeout(700)


async def discover_from_root(
    root_url: str,
    selectors: dict,
    allow_prefixes: list[str],
    settings: dict,
    *,
    browser_context,
) -> list[dict]:
    """打开 root_url，递归点开所有侧边栏折叠节点，抽出全部 a[href]"""
    link_selector = selectors["link_candidates"][0]
    page = await browser_context.new_page()
    try:
        await page.goto(root_url, timeout=settings["page_timeout_ms"])
        # 侧边栏树比正文晚渲染，ready_selector 会先被正文满足；必须等到树里真的出现链接再展开，
        # 否则空树被当成"没有子节点"，整个根抽出 0 条链接
        try:
            await page.wait_for_selector(link_selector, timeout=settings["page_timeout_ms"])
        except Exception:
            pass
        await page.wait_for_timeout(settings.get("extra_wait_ms", 800))
        await _expand_tree_fully(page, selectors.get("expandable_node", []), link_selector)
        html = await page.content()
        return extract_links_from_html(html, root_url, selectors, allow_prefixes)
    finally:
        await page.close()
