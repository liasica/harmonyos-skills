"""主入口：两阶段同步（全部走华为 documentPortal 接口，不需要浏览器）

阶段 1（discover）：每个根调一次 getCatalogTree，展平目录树得到文档清单与面包屑
阶段 2（fetch）：并发调 getDocumentById 拉正文 HTML，转 Markdown，按 hash 增量写盘

退出码：0 成功；1 discover 失败或本次抓取错误率过高（结果不可信，CI 据此不提交）；2 参数错误
"""
from __future__ import annotations

import argparse
import asyncio
import logging
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

import httpx
import yaml

from scripts.converter import (
    compute_content_hash,
    read_frontmatter,
    render_with_frontmatter,
    rewrite_internal_links,
    yaml_scalar,
)
from scripts.discover import fetch_catalog_tree, flatten_tree
from scripts.fetcher import FetchResult, fetch_document
from scripts.manifest import EntryStatus, Manifest
from scripts.paths import (
    DOC_URL_PREFIX,
    normalize_url,
    split_doc_url,
    url_to_local_path,
    url_to_reference_relative,
)


SCRAPER_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SCRAPER_ROOT.parent
DATA_DIR = SCRAPER_ROOT / "data"
DOCS_DIR = REPO_ROOT / "harmonyos" / "references"
LOGS_DIR = DATA_DIR / "logs"
MANIFEST_PATH = DATA_DIR / "manifest.json"

TZ_CN = timezone(timedelta(hours=8))
# 每完成多少页 flush 一次 manifest（中断恢复用）
FLUSH_EVERY = 50
# 本次抓取的错误占比超过该值即视为站点或接口出了问题，退出码置 1
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


def _collect_docs(manifest: Manifest) -> dict[str, list[tuple[str, str]]]:
    """按分类收集可进入 INDEX 的文档，每条为 (相对 references/ 的路径, 标题)

    - stale（本次全量未再发现）的条目排除
    - error 条目若磁盘上仍有上次成功的副本则保留，一次瞬时抓取失败不应把文档从索引里抹掉
    - 同一文件若被多条记录指向，按路径去重
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


def _frontmatter_matches(local_path: Path, url: str, doc) -> bool:
    """正文没变时也要核对 frontmatter：url 写法、标题、面包屑、更新时间任一变化都应重写文件"""
    fm = read_frontmatter(local_path)
    expected = {
        "url": url,
        "title": yaml_scalar(doc.title),
        "breadcrumb": yaml_scalar(doc.breadcrumb) if doc.breadcrumb else None,
        "doc_updated_at": doc.doc_updated_at or "",
    }
    return all(fm.get(k) == v for k, v in expected.items() if v is not None)


async def run(args: argparse.Namespace) -> int:
    started = time.monotonic()
    log = setup_logging()
    whitelist = load_yaml(SCRAPER_ROOT / "config" / "whitelist.yaml")
    settings = whitelist["settings"]
    allow_prefixes = settings["url_allow_prefixes"]
    api_base = settings["api_base"]

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

    roots = whitelist["roots"]
    if args.root:
        roots = [r for r in roots if r["category"] == args.root]

    limits = httpx.Limits(max_connections=settings["concurrency"],
                          max_keepalive_connections=settings["concurrency"])
    async with httpx.AsyncClient(timeout=settings["request_timeout_s"], limits=limits,
                                 headers={"User-Agent": settings["user_agent"]}) as client:
        # === Phase 1: discover（各根并行，每根一次 getCatalogTree）===
        async def discover_one(root: dict) -> tuple[dict, list[dict]]:
            category, object_id = split_doc_url(root["url"])
            log.info("discovering: %s", root["url"])
            try:
                tree_title, tree = await fetch_catalog_tree(client, api_base, category, object_id)
            except Exception as e:
                log.error("discover failed for %s: %s", root["url"], e)
                return root, []
            docs = flatten_tree(tree, tree_title or root["name"])
            # 根文档自身若不在树里也要收录
            if docs and not any(d["object_id"] == object_id for d in docs):
                docs.insert(0, {"object_id": object_id, "title": root["name"],
                                "breadcrumb": tree_title or root["name"]})
            log.info("  -> %s: %d docs", category, len(docs))
            return root, docs

        results = await asyncio.gather(*(discover_one(r) for r in roots))
        # 任一根失败或树里没有文档就整体放弃：带着残缺清单做全量会把该分类全部误标 stale
        failed = [root["category"] for root, docs in results if not docs]
        if failed:
            log.error("discover failed for %s, abort without touching manifest / INDEX", failed)
            return 1

        discovered: dict[str, dict] = {}
        for root, docs in results:
            category = root["category"]
            for d in docs:
                url = f"{DOC_URL_PREFIX}{category}/{d['object_id']}"
                if url in discovered:
                    continue
                discovered[url] = {"url": url, "object_id": d["object_id"], "category": category,
                                   "title": d["title"], "breadcrumb": d["breadcrumb"]}
        log.info("phase 1 done: %d docs across %d roots (%.1fs)",
                 len(discovered), len(roots), time.monotonic() - started)

        if args.dry_run:
            for url in list(discovered)[:50]:
                log.info("[dry-run] %s", url)
            log.info("[dry-run] total %d docs", len(discovered))
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
        done = 0

        async def worker(meta: dict) -> None:
            nonlocal done
            async with sem:
                result = await fetch_document(client, api_base, meta, settings)
            seen.add(meta["url"])
            _persist(manifest, result, meta, log, allow_prefixes)
            done += 1
            if done % FLUSH_EVERY == 0:
                manifest.save()
                log.info("progress: %d/%d (manifest flushed)", done, len(targets))

        # 全部任务一起交给信号量调度，避免按批 gather 时每批都要等最慢的一页
        await asyncio.gather(*(worker(m) for m in targets))

    # 仅在全量模式下做 stale 标记
    is_full_sync = not args.root and not args.limit
    if is_full_sync:
        manifest.mark_stale_except(seen=seen)
        dropped = manifest.drop_shadowed_stale()
        if dropped:
            log.info("dropped %d stale entries shadowed by live ones (old url variants)", dropped)
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
    log.info("done in %.1fs. stats=%s", time.monotonic() - started, manifest._stats())

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
    if previous_hash == content_hash and local_path.exists() and _frontmatter_matches(local_path, result.url, doc):
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
    parser.add_argument("--limit", type=int, default=None, help="只处理前 N 个文档（调试用）")
    parser.add_argument("--root", type=str, default=None, help="只处理指定 category 的根")
    parser.add_argument("--dry-run", action="store_true", help="只跑 discover，列出文档 URL 不抓取")
    parser.add_argument("--force", action="store_true", help="忽略本日 last_checked_at，强制重抓")
    args = parser.parse_args()
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
