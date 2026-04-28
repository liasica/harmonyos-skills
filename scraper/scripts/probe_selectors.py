"""首次运行前的选择器探测：打开一个根 URL，打印各候选选择器命中情况"""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

import yaml
from playwright.async_api import async_playwright


SCRAPER_ROOT = Path(__file__).resolve().parents[1]


async def probe(url: str, headed: bool) -> None:
    selectors = yaml.safe_load((SCRAPER_ROOT / "config" / "selectors.yaml").read_text())
    settings = yaml.safe_load((SCRAPER_ROOT / "config" / "whitelist.yaml").read_text())["settings"]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headed)
        ctx = await browser.new_context(user_agent=settings["user_agent"])
        page = await ctx.new_page()
        await page.goto(url, timeout=settings["page_timeout_ms"])
        await page.wait_for_timeout(3000)

        print(f"\n=== probing {url} ===\n")
        for group_name in ("sidebar", "article"):
            print(f"-- {group_name} --")
            group = selectors[group_name]
            for key, value in group.items():
                if not isinstance(value, list):
                    continue
                for sel in value:
                    try:
                        n = len(await page.query_selector_all(sel))
                    except Exception as e:
                        n = f"ERR:{e}"
                    print(f"  {key:25s} {sel:60s} -> {n}")
            print()
        if not headed:
            await browser.close()
        else:
            print("浏览器已打开（headed），手动检查后 Ctrl+C 退出")
            await asyncio.sleep(600)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("--headed", action="store_true")
    args = p.parse_args()
    asyncio.run(probe(args.url, args.headed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
