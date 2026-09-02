"""阶段 1：调 documentPortal/getCatalogTree 拿整棵目录树，展平成文档清单"""
from __future__ import annotations

import httpx


def flatten_tree(nodes: list[dict], root_title: str) -> list[dict]:
    """把目录树展平为 [{object_id, title, breadcrumb}]，保持树的顺序，同一文档只保留首次出现

    节点字段：nodeName（标题）、relateDocument（文档 objectId，纯目录节点没有）、children
    面包屑为「根标题 > 各级目录 > 本节点」
    """
    out: list[dict] = []
    seen: set[str] = set()

    def walk(items: list[dict], path: tuple[str, ...]) -> None:
        for node in items:
            name = (node.get("nodeName") or "").strip()
            crumb = path + (name,) if name else path
            object_id = (node.get("relateDocument") or "").strip()
            if object_id and object_id not in seen:
                seen.add(object_id)
                out.append({"object_id": object_id, "title": name or object_id, "breadcrumb": " > ".join(crumb)})
            walk(node.get("children") or [], crumb)

    walk(nodes, (root_title,) if root_title else ())
    return out


async def fetch_catalog_tree(client: httpx.AsyncClient, api_base: str, category: str,
                             object_id: str) -> tuple[str, list[dict]]:
    """返回 (目录树标题, 顶层节点列表)；接口报错抛异常"""
    resp = await client.post(api_base + "getCatalogTree",
                             json={"language": "cn", "catalogName": category, "objectId": object_id})
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0 or not data.get("value"):
        raise RuntimeError(f"getCatalogTree code={data.get('code')} message={data.get('message', '')}")
    value = data["value"]
    return value.get("title") or "", value.get("catalogTreeList") or []
