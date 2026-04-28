"""URL 与本地存储路径之间的双向映射"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse


_TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"}
# 注意：华为站点的 ?istab=1&m=1 看似 UI 参数，但 SPA 路由依赖它判断"哪个 tab"，
# 删掉就会重定向到 404。所以这里不剥离它们。同一文档若被带/不带 query 各访问一次，
# url_to_local_path 仍按 path 段映射到同一 .md，第二次访问会触发 unchanged 路径。


def normalize_url(url: str) -> str:
    """规范化 URL：剥离 fragment、tracking 参数、尾斜杠"""
    parsed = urlparse(url)
    query_pairs = [(k, v) for k, v in parse_qsl(parsed.query) if k not in _TRACKING_PARAMS]
    query_pairs.sort()
    new_query = urlencode(query_pairs)
    path = parsed.path
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return urlunparse((parsed.scheme, parsed.netloc, path, "", new_query, ""))


_DOC_PREFIX = "/consumer/cn/doc/"


def url_to_local_path(url: str, root: Path) -> Path:
    """把 URL 映射为本地 Markdown 路径，剥离 /consumer/cn/doc/ 前缀

    规则：
      - 移除 `/consumer/cn/doc/` 前缀
      - 路径段直接复用
      - 以 / 结尾 → 该目录下 index.md
      - 否则 → <最后一段>.md
    """
    parsed = urlparse(url)
    raw_path = parsed.path
    if raw_path.startswith(_DOC_PREFIX):
        raw_path = raw_path[len(_DOC_PREFIX):]
    if raw_path.endswith("/"):
        return root / raw_path.lstrip("/") / "index.md"
    rel = raw_path.lstrip("/")
    return root / f"{rel}.md"


def is_in_whitelist(url: str, allow_prefixes: list[str]) -> bool:
    """判断 URL 是否落在白名单前缀内"""
    return any(url.startswith(p) for p in allow_prefixes)


def url_to_reference_relative(url: str, from_md_path: Path, references_root: Path,
                              allow_prefixes: list[str]) -> str | None:
    """把白名单内的 URL 转为指向本仓库的相对路径

    返回 None 表示该 URL 不在白名单内（链接应保留原样）
    """
    import os
    from urllib.parse import urlparse
    if not is_in_whitelist(url, allow_prefixes):
        return None
    parsed = urlparse(url)
    target = url_to_local_path(url, references_root)
    rel = os.path.relpath(str(target), start=str(from_md_path.parent))
    if parsed.fragment:
        rel = f"{rel}#{parsed.fragment}"
    return rel
