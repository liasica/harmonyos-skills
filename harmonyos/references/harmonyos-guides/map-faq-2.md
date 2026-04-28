---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-2
title: siteId参数如何获取
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > siteId参数如何获取
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5bb1b78e3846b60f15d47b34e32c53e882aa006504f6fd9c636f322c798fcd5d
---

siteId有多种获取方式，这里提供其中的3种作为参考：

1. 可通过[on('poiClick')](../harmonyos-references/map-map-mapeventmanager.md#onpoiclick)方法获取。
2. 可通过[位置搜索](map-site-search.md)相关接口（关键字搜索、周边搜索、地点详情、自动补全、正地理编码）的返回结果中获取。
3. 可通过[chooseLocation](../harmonyos-references/map-scenemap.md#chooselocation)接口的返回结果中获取。
