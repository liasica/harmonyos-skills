"""主入口：两阶段同步

阶段 1（discover）：访问 5 个根 URL，递归点开 .layout-left 全部折叠节点，抽出全部 a[href]
阶段 2（fetch）：并发渲染所有发现的 URL，抽正文转 Markdown，按 hash 增量写盘
"""
from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml
from playwright.async_api import async_playwright

from scripts.converter import (
    compute_content_hash,
    render_with_frontmatter,
    rewrite_internal_links,
)
from scripts.discover import discover_from_root
from scripts.fetcher import fetch_page
from scripts.manifest import Manifest
from scripts.paths import (
    normalize_url,
    url_to_local_path,
    url_to_reference_relative,
)


SCRAPER_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SCRAPER_ROOT.parent
DATA_DIR = SCRAPER_ROOT / "data"
DOCS_DIR = REPO_ROOT / "harmonyos" / "references"
LOGS_DIR = DATA_DIR / "logs"
MANIFEST_PATH = DATA_DIR / "manifest.json"
DISCOVERY_CACHE_PATH = DATA_DIR / "discovery.json"
SYNC_STATE_PATH = DATA_DIR / "sync_state.json"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).isoformat(timespec="seconds")


def _load_discovery_cache(today_start: str, args: argparse.Namespace) -> dict | None:
    """同日内的 discovery 缓存可复用；--force 或 --root（部分同步）时不复用"""
    if args.force or args.root:
        return None
    if not DISCOVERY_CACHE_PATH.exists():
        return None
    try:
        import json
        d = json.loads(DISCOVERY_CACHE_PATH.read_text(encoding="utf-8"))
        if d.get("date") != today_start[:10]:
            return None
        return {url: meta for url, meta in d.get("urls", {}).items()}
    except Exception:
        return None


def _write_indexes(manifest: Manifest, log: logging.Logger) -> None:
    """生成 harmonyos/references/INDEX.md（全量）+ 各 category 的 INDEX.md

    清单文件每行一个相对路径（参考 linhay/harmony-next.skills 格式），按字母序排列。
    用作 AI 助手的"先在 INDEX 命中路径，再 Read 对应 .md"导航入口。
    """
    from collections import defaultdict
    by_category: dict[str, list[tuple[str, str]]] = defaultdict(list)
    all_paths: list[str] = []
    for url, entry in manifest.entries.items():
        if entry.status in ("error", "stale") or not entry.local_path:
            continue
        # local_path 是相对 REPO_ROOT 的路径，例如 harmonyos/references/<cat>/x.md
        # 在 references 内的相对路径才是 INDEX 要列的内容
        try:
            in_refs = Path(entry.local_path).relative_to(Path("harmonyos/references"))
        except ValueError:
            continue
        rel = str(in_refs)
        all_paths.append(rel)
        by_category[entry.category].append((rel, entry.title))

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    # 全局清单
    all_paths.sort()
    (DOCS_DIR / "INDEX.md").write_text("\n".join(all_paths) + "\n", encoding="utf-8")
    log.info("INDEX.md written: %d paths", len(all_paths))

    # 各 category 清单（带标题）
    for cat, items in by_category.items():
        items.sort(key=lambda x: x[0])
        cat_dir = DOCS_DIR / cat
        if not cat_dir.exists():
            continue
        lines = [f"# {cat}", "", f"共 {len(items)} 篇文档。", ""]
        for rel, title in items:
            # 在 category INDEX 中链接是相对 category 目录
            try:
                in_cat = Path(rel).relative_to(cat)
            except ValueError:
                in_cat = Path(rel)
            lines.append(f"- [{title}]({in_cat})")
        (cat_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("category INDEX.md written for %d categories", len(by_category))


def _update_readme_stats(manifest: Manifest, log: logging.Logger) -> None:
    """回填 README.md 中的 LAST_SYNC 与各 category 计数 placeholder"""
    from collections import Counter
    counter: Counter = Counter()
    for entry in manifest.entries.values():
        if entry.status in ("error", "stale") or not entry.local_path:
            continue
        counter[entry.category] += 1

    readme_path = REPO_ROOT / "README.md"
    if not readme_path.exists():
        log.warning("README.md not found at %s, skipping stats update", readme_path)
        return

    text = readme_path.read_text(encoding="utf-8")
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    total = sum(counter.values())
    replacements = {
        "<!-- LAST_SYNC -->": today,
        "<!-- COUNT_RELEASES -->": str(counter.get("harmonyos-releases", 0)),
        "<!-- COUNT_GUIDES -->": str(counter.get("harmonyos-guides", 0)),
        "<!-- COUNT_REFERENCES -->": str(counter.get("harmonyos-references", 0)),
        "<!-- COUNT_BESTPRACTICES -->": str(counter.get("best-practices", 0)),
        "<!-- COUNT_FAQS -->": str(counter.get("harmonyos-faqs", 0)),
        "<!-- COUNT_TOTAL -->": str(total),
    }
    # 同时支持二次更新：把已替换的具体值再次替换回 placeholder 不可行，
    # 改用 regex 直接定位 "更新日期" 和表格行，针对最后已知值做替换
    import re
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    # 第二次同步：替换已存在的具体值。匹配 "最后一次完整同步：**YYYY-MM-DD**"
    text = re.sub(
        r"最后一次完整同步：\*\*\d{4}-\d{2}-\d{2}\*\*",
        f"最后一次完整同步：**{today}**",
        text,
    )
    # 替换表格里"| <分类> ... | <数字> |"中的数字
    for category_label, count in (
        ("版本说明 (`harmonyos-releases`)", counter.get("harmonyos-releases", 0)),
        ("指南 (`harmonyos-guides`)", counter.get("harmonyos-guides", 0)),
        ("API 参考 (`harmonyos-references`)", counter.get("harmonyos-references", 0)),
        ("最佳实践 (`best-practices`)", counter.get("best-practices", 0)),
        ("FAQ (`harmonyos-faqs`)", counter.get("harmonyos-faqs", 0)),
    ):
        text = re.sub(
            rf"(\| {re.escape(category_label)} \| )\d+( \|)",
            rf"\g<1>{count}\g<2>",
            text,
        )
    text = re.sub(
        r"(\| \*\*合计\*\* \| \*\*)\d+(\*\* \|)",
        rf"\g<1>{total}\g<2>",
        text,
    )

    readme_path.write_text(text, encoding="utf-8")
    log.info("README stats updated: total=%d, by_category=%s", total, dict(counter))


def _save_discovery_cache(discovered: dict[str, dict], today_start: str) -> None:
    import json
    DISCOVERY_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"date": today_start[:10], "saved_at": now_iso(),
               "count": len(discovered), "urls": discovered}
    tmp = DISCOVERY_CACHE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(DISCOVERY_CACHE_PATH)


def setup_logging() -> logging.Logger:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"sync-{datetime.now().strftime('%Y-%m-%d')}.log"
    fmt = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return logging.getLogger("sync")


async def run(args: argparse.Namespace) -> int:
    log = setup_logging()
    whitelist = load_yaml(SCRAPER_ROOT / "config" / "whitelist.yaml")
    selectors = load_yaml(SCRAPER_ROOT / "config" / "selectors.yaml")
    settings = whitelist["settings"]
    allow_prefixes = settings["url_allow_prefixes"]

    manifest = Manifest.load(MANIFEST_PATH)
    sync_started_at = now_iso()
    today_start = datetime.now(timezone(timedelta(hours=8))).replace(
        hour=0, minute=0, second=0, microsecond=0
    ).isoformat(timespec="seconds")

    roots = whitelist["roots"]
    if args.root:
        roots = [r for r in roots if r["category"] == args.root]

    # category 推断：URL 必须落在 5 个根的二级路径前缀内，否则视为越界
    category_prefixes: list[tuple[str, str]] = []
    for r in whitelist["roots"]:
        seg = r["url"].split("/consumer/cn/doc/", 1)[1].split("/", 1)[0]
        category_prefixes.append((f"https://developer.huawei.com/consumer/cn/doc/{seg}", r["category"]))

    def infer_category(url: str) -> str:
        for prefix, cat in category_prefixes:
            if url == prefix or url.startswith(prefix + "/") or url.startswith(prefix + "?"):
                return cat
        return "unknown"

    # === 断点续传：尝试加载 discovery 缓存 ===
    discovered: dict[str, dict] = {}
    cache = _load_discovery_cache(today_start, args)
    if cache is not None:
        discovered = cache
        log.info("phase 1 skipped (cache): %d urls from %s", len(discovered), DISCOVERY_CACHE_PATH)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=settings["user_agent"])

        if not discovered:
            # === Phase 1: discover (5 个根并行) ===
            async def discover_one(root: dict) -> tuple[dict, list[dict]]:
                log.info("discovering: %s", root["url"])
                try:
                    links = await discover_from_root(
                        root["url"], selectors["sidebar"], allow_prefixes, settings,
                        browser_context=context,
                    )
                except Exception as e:
                    log.error("discover failed for %s: %s", root["url"], e)
                    return root, []
                log.info("  → %s: %d links", root["category"], len(links))
                return root, links

            results = await asyncio.gather(*(discover_one(r) for r in roots))
            for root, links in results:
                discovered.setdefault(root["url"], {
                    "url": root["url"], "title": root["name"], "category": root["category"],
                })
                for l in links:
                    cat = infer_category(l["url"])
                    if cat == "unknown":
                        continue
                    if l["url"] in discovered:
                        continue
                    discovered[l["url"]] = {"url": l["url"], "title": l["title"], "category": cat}

            log.info("phase 1 done: %d unique URLs", len(discovered))
            _save_discovery_cache(discovered, today_start)

        if args.dry_run:
            for url in list(discovered)[:50]:
                log.info("[dry-run] %s", url)
            log.info("[dry-run] total %d urls", len(discovered))
            await context.close()
            await browser.close()
            return 0

        # === Phase 2: fetch（断点续传：本日已 check 过且非 force 跳过）===
        all_targets = list(discovered.values())
        if args.limit:
            all_targets = all_targets[: args.limit]

        skipped: list[dict] = []
        targets: list[dict] = []
        for meta in all_targets:
            entry = manifest.entries.get(meta["url"])
            if entry and entry.last_checked_at >= today_start and not args.force:
                skipped.append(meta)
            else:
                targets.append(meta)

        log.info("phase 2: %d to fetch, %d already done today (skipped), concurrency=%d",
                 len(targets), len(skipped), settings["concurrency"])

        sem = asyncio.Semaphore(settings["concurrency"])
        seen: set[str] = {m["url"] for m in skipped}

        async def worker(meta: dict):
            async with sem:
                result = await fetch_page(meta["url"], selectors, settings, browser_context=context)
            seen.add(meta["url"])
            _persist(manifest, result, meta, log, allow_prefixes)

        # 分批处理：每批结束 flush manifest（中断恢复用）
        batch_size = 50
        for i in range(0, len(targets), batch_size):
            batch = targets[i : i + batch_size]
            await asyncio.gather(*(worker(m) for m in batch))
            manifest.save()
            log.info("progress: %d/%d (manifest flushed)",
                     min(i + batch_size, len(targets)), len(targets))

        await context.close()
        await browser.close()

    # 仅在全量模式下做 stale 标记
    is_full_sync = not args.root and not args.limit
    if is_full_sync:
        manifest.mark_stale_except(seen=seen)
        manifest.last_full_sync_at = now_iso()
    manifest.save()

    # 生成 INDEX.md
    _write_indexes(manifest, log)
    # 回填 README 统计数据
    if is_full_sync:
        _update_readme_stats(manifest, log)
    log.info("manifest saved: %s", MANIFEST_PATH)
    log.info("done. stats=%s", manifest._stats())
    return 0


def _persist(manifest: Manifest, result, meta: dict, log: logging.Logger,
             allow_prefixes: list[str]) -> None:
    now = now_iso()
    if not result.success:
        log.warning("fetch failed: %s (%s)", result.url, result.error)
        manifest.upsert(
            url=result.url,
            title=meta.get("title", result.url),
            category=meta["category"],
            local_path="",
            content_hash="",
            doc_updated_at=None,
            now=now,
            error=result.error,
        )
        return

    doc = result.doc
    local_path = url_to_local_path(result.url, DOCS_DIR)

    # 把 markdown 中指向白名单内的 http(s) 链接改写为相对路径
    md = rewrite_internal_links(
        doc.markdown,
        from_md_path=local_path,
        references_root=DOCS_DIR,
        allow_prefixes=allow_prefixes,
        url_normalizer=normalize_url,
        url_to_relative=url_to_reference_relative,
    )
    content_hash = compute_content_hash(md)

    existing = manifest.entries.get(result.url)
    if existing and existing.content_hash == content_hash and local_path.exists():
        manifest.upsert(
            url=result.url, title=doc.title, category=meta["category"],
            local_path=str(local_path.relative_to(REPO_ROOT)),
            content_hash=content_hash, doc_updated_at=doc.doc_updated_at,
            now=now,
        )
        return

    rendered = render_with_frontmatter(
        markdown=md,
        url=result.url,
        title=doc.title,
        breadcrumb=doc.breadcrumb,
        category=meta["category"],
        scraped_at=now,
        doc_updated_at=doc.doc_updated_at,
        content_hash=content_hash,
    )
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text(rendered, encoding="utf-8")
    log.info("wrote: %s (%d bytes)", local_path, len(rendered))
    manifest.upsert(
        url=result.url, title=doc.title, category=meta["category"],
        local_path=str(local_path.relative_to(REPO_ROOT)),
        content_hash=content_hash, doc_updated_at=doc.doc_updated_at,
        now=now,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="HarmonyOS docs sync")
    parser.add_argument("--limit", type=int, default=None, help="只处理前 N 个 URL（调试用）")
    parser.add_argument("--root", type=str, default=None, help="只处理指定 category 的根")
    parser.add_argument("--dry-run", action="store_true", help="只跑 discover，列出 URL 不渲染")
    parser.add_argument("--force", action="store_true",
                        help="忽略 discovery 缓存与本日 last_checked_at，强制重抓")
    args = parser.parse_args()
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
