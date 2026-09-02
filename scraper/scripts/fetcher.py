"""阶段 2：调 documentPortal/getDocumentById 拉正文 HTML，交给 converter 转 Markdown"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Optional

import httpx

from scripts.converter import ExtractedDoc, convert_api_html


@dataclass
class FetchResult:
    url: str
    success: bool
    doc: Optional[ExtractedDoc] = None
    error: Optional[str] = None


async def fetch_document(client: httpx.AsyncClient, api_base: str, meta: dict, settings: dict) -> FetchResult:
    """meta 来自 discover：url / object_id / category / title / breadcrumb

    网络错误、5xx、429 按 retries 重试；其余 4xx 与接口 code != 0 视为确定性失败不重试
    """
    url = meta["url"]
    payload = {"objectId": meta["object_id"], "version": "", "catalogName": meta["category"], "language": "cn"}
    last_err: Optional[Exception] = None
    for attempt in range(settings.get("retries", 2) + 1):
        try:
            resp = await client.post(api_base + "getDocumentById", json=payload)
            if resp.status_code == 429 or resp.status_code >= 500:
                raise httpx.HTTPStatusError(f"http {resp.status_code}", request=resp.request, response=resp)
            if resp.status_code >= 400:
                return FetchResult(url=url, success=False, error=f"http {resp.status_code}")
            data = resp.json()
        except (httpx.HTTPError, ValueError) as e:
            last_err = e
            await asyncio.sleep(0.5 * (attempt + 1))
            continue
        if data.get("code") != 0 or not data.get("value"):
            return FetchResult(url=url, success=False,
                               error=f"api code={data.get('code')} {data.get('message', '')}".rstrip())
        value = data["value"]
        html = (value.get("content") or {}).get("content") or ""
        if not html:
            return FetchResult(url=url, success=False, error="api returned empty content")
        updated = (value.get("displayUpdateTime") or value.get("updatedDate") or "")[:10] or None
        doc = convert_api_html(
            html,
            title=value.get("title") or meta["title"],
            breadcrumb=meta.get("breadcrumb", ""),
            doc_updated_at=updated,
            base_url=url,
        )
        return FetchResult(url=url, success=True, doc=doc)
    return FetchResult(url=url, success=False, error=f"request: {last_err}")
