"""主入口：两阶段同步

阶段 1（discover）：访问 5 个根 URL，递归点开 .layout-left 全部折叠节点，抽出全部 a[href]
阶段 2（fetch）：并发渲染所有发现的 URL，抽正文转 Markdown，按 hash 增量写盘

退出码：0 成功；1 discover 失败或本次抓取错误率过高（结果不可信，CI 据此不提交）；2 参数错误
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml
from playwright.async_api import async_playwright

from scripts.converter import (
    compute_content_hash,
    read_frontmatter,
    render_with_frontmatter,
    rewrite_internal_links,
)
from scripts.discover import discover_from_root
from scripts.fetcher import FetchResult, fetch_page
from scripts.manifest import EntryStatus, Manifest
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

TZ_CN = timezone(timedelta(hours=8))
# 每完成多少页 flush 一次 manifest（中断恢复用）
FLUSH_EVERY = 50
# 本次抓取的错误占比超过该值即视为站点或选择器出了问题，退出码置 1
MAX_ERROR_RATIO = 0.2

_CATEGORY_DISPLAY = {
    "harmonyos-releases": "版本说明",
    "harmonyos-guides": "指南",
    "harmonyos-references": "API 参考",
    "best-practices": "最佳实践",
    "harmonyos-faqs": "FAQ",
    "harmonyos-roadmap": "变更预告",
}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(TZ_CN).isoformat(timespec="seconds")


def _load_discovery_cache(today: str, args: argparse.Namespace) -> dict | None:
    """同日内的 discovery 缓存可复用；--force 或 --root（部分同步）时不复用"""
    if args.force or args.root:
        return None
    if not DISCOVERY_CACHE_PATH.exists():
        return None
    try:
        d = json.loads(DISCOVERY_CACHE_PATH.read_text(encoding="utf-8"))
        if d.get("date") != today:
            return None
        return dict(d.get("urls", {}))
    except Exception:
        return None


def _save_discovery_cache(discovered: dict[str, dict], today: str) -> None:
    DISCOVERY_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"date": today, "saved_at": now_iso(),
               "count": len(discovered), "urls": discovered}
    tmp = DISCOVERY_CACHE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(DISCOVERY_CACHE_PATH)


def _collect_docs(manifest: Manifest) -> dict[str, list[tuple[str, str]]]:
    """按分类收集可进入 INDEX 的文档，每条为 (相对 references/ 的路径, 标题)

    - stale（本次全量未再发现）的条目排除
    - error 条目若磁盘上仍有上次成功的副本则保留，一次瞬时抓取失败不应把文档从索引里抹掉
    - 同一文档可能被带 / 不带 query 的两个 URL 各记一条，按路径去重
    """
    by_category: dict[str, list[tuple[str, str]]] = defaultdict(list)
    seen_paths: set[str] = set()
    for entry in manifest.entries.values():
        if entry.status == EntryStatus.STALE or not entry.local_path:
            continue
        if not (REPO_ROOT / entry.local_path).exists():
            continue
        try:
            rel = str(Path(entry.local_path).relative_to(Path("harmonyos/references")))
        except ValueError:
            continue
        if rel in seen_paths:
            continue
        seen_paths.add(rel)
        by_category[entry.category].append((rel, entry.title))
    for items in by_category.values():
        items.sort(key=lambda x: x[0])
    return by_category


def _write_indexes(docs: dict[str, list[tuple[str, str]]], log: logging.Logger) -> None:
    """生成 harmonyos/references/INDEX.md（全量，按分类分组）+ 各 category 的 INDEX.md

    全量 INDEX 按分类分组，每条 `- [title](relative/path.md)`，便于 AI 用 grep 命中后 Read。
    """
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    total = sum(len(v) for v in docs.values())

    # 全量 INDEX（按分类分组，每条带标题）
    lines = ["# HarmonyOS 文档全量索引", "",
             f"共 {total} 篇文档。先在本文件 grep 关键词获取相对路径，再 Read 对应 `.md`。", ""]
    for cat, display in _CATEGORY_DISPLAY.items():
        items = docs.get(cat, [])
        if not items:
            continue
        lines.append(f"## {display}（`{cat}`）— {len(items)} 篇")
        lines.append("")
        for rel, title in items:
            lines.append(f"- [{title}]({rel})")
        lines.append("")
    (DOCS_DIR / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    log.info("INDEX.md written: %d entries across %d categories", total, len(docs))

    # 各 category INDEX（带标题）
    for cat, items in docs.items():
        cat_dir = DOCS_DIR / cat
        if not cat_dir.exists():
            continue
        display = _CATEGORY_DISPLAY.get(cat, cat)
        cat_lines = [f"# {display}（{cat}）", "", f"共 {len(items)} 篇文档。", ""]
        for rel, title in items:
            try:
                in_cat = Path(rel).relative_to(cat)
            except ValueError:
                in_cat = Path(rel)
            cat_lines.append(f"- [{title}]({in_cat})")
        (cat_dir / "INDEX.md").write_text("\n".join(cat_lines) + "\n", encoding="utf-8")
    log.info("category INDEX.md written for %d categories", len(docs))


def _update_readme_stats(docs: dict[str, list[tuple[str, str]]], log: logging.Logger) -> None:
    """回填 README.md 中「最后一次完整同步」日期与文档统计表的各分类计数（与 INDEX 口径一致）"""
    readme_path = REPO_ROOT / "README.md"
    if not readme_path.exists():
        log.warning("README.md not found at %s, skipping stats update", readme_path)
        return

    text = readme_path.read_text(encoding="utf-8")
    today = datetime.now(TZ_CN).strftime("%Y-%m-%d")
    counts = {cat: len(items) for cat, items in docs.items()}
    total = sum(counts.values())
    # 替换 `最后一次完整同步：**YYYY-MM-DD**` 中的日期
    text = re.sub(
        r"最后一次完整同步：\*\*\d{4}-\d{2}-\d{2}\*\*",
        f"最后一次完整同步：**{today}**",
        text,
    )
    # 替换表格里 `| <分类> (`<cat>`) | <数字> |` 中的数字
    for cat, display in _CATEGORY_DISPLAY.items():
        label = f"{display} (`{cat}`)"
        text = re.sub(
            rf"(\| {re.escape(label)} \| )\d+( \|)",
            rf"\g<1>{counts.get(cat, 0)}\g<2>",
            text,
        )
    text = re.sub(
        r"(\| \*\*合计\*\* \| \*\*)\d+(\*\* \|)",
        rf"\g<1>{total}\g<2>",
        text,
    )

    readme_path.write_text(text, encoding="utf-8")
    log.info("README stats updated: total=%d, by_category=%s", total, counts)


def setup_logging() -> logging.Logger:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"sync-{datetime.now(TZ_CN).strftime('%Y-%m-%d')}.log"
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


def _hash_on_disk(local_path: Path) -> str:
    """读磁盘副本 frontmatter 里的 content_hash；文件不存在返回空串"""
    return read_frontmatter(local_path).get("content_hash", "")


async def run(args: argparse.Namespace) -> int:
    log = setup_logging()
    whitelist = load_yaml(SCRAPER_ROOT / "config" / "whitelist.yaml")
    selectors = load_yaml(SCRAPER_ROOT / "config" / "selectors.yaml")
    settings = whitelist["settings"]
    allow_prefixes = settings["url_allow_prefixes"]

    categories = [r["category"] for r in whitelist["roots"]]
    if args.root and args.root not in categories:
        log.error("unknown --root %r, expected one of: %s", args.root, ", ".join(categories))
        return 2

    manifest = Manifest.load(MANIFEST_PATH)
    # manifest 为空说明是全新环境（如 CI），此时部分同步（--root / --limit）得到的清单不完整，不能拿来重写 INDEX
    had_manifest = bool(manifest.entries)
    today_start = datetime.now(TZ_CN).replace(
        hour=0, minute=0, second=0, microsecond=0
    ).isoformat(timespec="seconds")
    today = today_start[:10]

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
    cache = _load_discovery_cache(today, args)
    if cache is not None:
        discovered = cache
        log.info("phase 1 skipped (cache): %d urls from %s", len(discovered), DISCOVERY_CACHE_PATH)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=settings["user_agent"])
        try:
            if not discovered:
                # === Phase 1: discover（各根并行）===
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
                    log.info("  -> %s: %d links", root["category"], len(links))
                    return root, links

                results = await asyncio.gather(*(discover_one(r) for r in roots))
                # 任一根失败或抽不到链接就整体放弃：带着残缺结果做全量会把该分类全部误标 stale
                failed = [root["category"] for root, links in results if not links]
                if failed:
                    log.error("discover failed for %s, abort without touching manifest / INDEX", failed)
                    return 1
                for root, links in results:
                    discovered.setdefault(root["url"], {
                        "url": root["url"], "title": root["name"], "category": root["category"],
                    })
                    for l in links:
                        cat = infer_category(l["url"])
                        if cat == "unknown" or l["url"] in discovered:
                            continue
                        discovered[l["url"]] = {"url": l["url"], "title": l["title"], "category": cat}

                log.info("phase 1 done: %d unique URLs", len(discovered))
                # 只缓存全量 discover 的结果；--root 的部分结果若写入缓存，会被下一次全量误当作完整清单
                if not args.root:
                    _save_discovery_cache(discovered, today)

            if args.dry_run:
                for url in list(discovered)[:50]:
                    log.info("[dry-run] %s", url)
                log.info("[dry-run] total %d urls", len(discovered))
                return 0

            # === Phase 2: fetch（断点续传：本日已 check 过且非 force 跳过）===
            all_targets = list(discovered.values())
            if args.limit:
                all_targets = all_targets[: args.limit]

            skipped: list[dict] = []
            targets: list[dict] = []
            claimed_paths: set[Path] = set()
            duplicates = 0
            for meta in all_targets:
                # 同一文档带 / 不带 query 会映射到同一个 .md，只抓先发现的那个，避免两个变体交替改写
                local_path = url_to_local_path(meta["url"], DOCS_DIR)
                if local_path in claimed_paths:
                    duplicates += 1
                    continue
                claimed_paths.add(local_path)
                entry = manifest.entries.get(meta["url"])
                if entry and entry.last_checked_at >= today_start and not args.force:
                    skipped.append(meta)
                else:
                    targets.append(meta)

            log.info("phase 2: %d to fetch, %d already done today (skipped), %d duplicate urls dropped, concurrency=%d",
                     len(targets), len(skipped), duplicates, settings["concurrency"])

            sem = asyncio.Semaphore(settings["concurrency"])
            seen: set[str] = {m["url"] for m in skipped}
            done = 0

            async def worker(meta: dict) -> None:
                nonlocal done
                async with sem:
                    result = await fetch_page(meta["url"], selectors, settings, browser_context=context)
                seen.add(meta["url"])
                _persist(manifest, result, meta, log, allow_prefixes)
                done += 1
                if done % FLUSH_EVERY == 0:
                    manifest.save()
                    log.info("progress: %d/%d (manifest flushed)", done, len(targets))

            # 全部任务一起交给信号量调度，避免按批 gather 时每批都要等最慢的一页
            await asyncio.gather(*(worker(m) for m in targets))
        finally:
            await context.close()
            await browser.close()

    # 仅在全量模式下做 stale 标记
    is_full_sync = not args.root and not args.limit
    if is_full_sync:
        manifest.mark_stale_except(seen=seen)
        manifest.last_full_sync_at = now_iso()
    manifest.save()

    docs = _collect_docs(manifest)
    if is_full_sync or had_manifest:
        _write_indexes(docs, log)
    else:
        log.warning("partial sync on an empty manifest, INDEX.md left untouched")
    if is_full_sync:
        _update_readme_stats(docs, log)
    log.info("manifest saved: %s", MANIFEST_PATH)
    log.info("done. stats=%s", manifest._stats())

    errors = sum(1 for m in targets if manifest.entries[m["url"]].status == EntryStatus.ERROR)
    if targets and errors / len(targets) > MAX_ERROR_RATIO:
        log.error("%d/%d fetches failed this run, exceeds %.0f%%, treat as failure",
                  errors, len(targets), MAX_ERROR_RATIO * 100)
        return 1
    return 0


def _persist(manifest: Manifest, result: FetchResult, meta: dict, log: logging.Logger,
             allow_prefixes: list[str]) -> None:
    now = now_iso()
    local_path = url_to_local_path(result.url, DOCS_DIR)
    rel_path = str(local_path.relative_to(REPO_ROOT))
    existing = manifest.entries.get(result.url)

    if not result.success:
        log.warning("fetch failed: %s (%s)", result.url, result.error)
        # 磁盘上若还有上次成功的副本，保留其路径与 hash，INDEX 不因一次瞬时失败而丢文档
        has_copy = local_path.exists()
        manifest.upsert(
            url=result.url,
            title=existing.title if existing else meta.get("title", result.url),
            category=meta["category"],
            local_path=rel_path if has_copy else "",
            content_hash=(existing.content_hash if existing else _hash_on_disk(local_path)) if has_copy else "",
            doc_updated_at=existing.doc_updated_at if existing else None,
            now=now,
            error=result.error,
        )
        return

    doc = result.doc

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

    # manifest 里没有记录（如 CI 的全新环境）时退回读磁盘副本 frontmatter 里的 hash，避免整库重写
    previous_hash = existing.content_hash if existing and existing.content_hash else _hash_on_disk(local_path)
    if previous_hash == content_hash and local_path.exists():
        manifest.upsert(
            url=result.url, title=doc.title, category=meta["category"],
            local_path=rel_path, content_hash=content_hash,
            doc_updated_at=doc.doc_updated_at, now=now,
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
        local_path=rel_path, content_hash=content_hash,
        doc_updated_at=doc.doc_updated_at, now=now,
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
