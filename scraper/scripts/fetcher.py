"""单页面渲染 + 抽取，调用 converter 完成 Markdown 转换"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Optional

from scripts.converter import (
    ExtractedDoc,
    ExtractionError,
    extract_and_convert,
)


@dataclass
class FetchResult:
    url: str
    success: bool
    doc: Optional[ExtractedDoc] = None
    error: Optional[str] = None
    raw_html: Optional[str] = None


async def fetch_page(
    url: str,
    selectors: dict,
    settings: dict,
    *,
    browser_context,
) -> FetchResult:
    article_selectors = selectors["article"]
    page = await browser_context.new_page()
    try:
        last_err: Optional[Exception] = None
        for attempt in range(settings.get("retries", 2) + 1):
            try:
                await page.goto(url, timeout=settings["page_timeout_ms"])
                ready = article_selectors.get("ready_selector")
                if ready:
                    await page.wait_for_selector(ready, timeout=settings["page_timeout_ms"])
                await page.wait_for_timeout(settings.get("extra_wait_ms", 800))
                html = await page.content()
                doc = extract_and_convert(html, article_selectors, base_url=url)
                return FetchResult(url=url, success=True, doc=doc, raw_html=html)
            except ExtractionError as e:
                return FetchResult(url=url, success=False, error=f"extract: {e}", raw_html=None)
            except Exception as e:
                last_err = e
                await asyncio.sleep(0.5 * (attempt + 1))
        return FetchResult(url=url, success=False, error=f"render: {last_err}")
    finally:
        await page.close()
