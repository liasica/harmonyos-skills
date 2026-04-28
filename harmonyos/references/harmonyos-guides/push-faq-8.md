---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-8
title: 场景化消息中的请求URL版本问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 场景化消息中的请求URL版本问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:726e8513a110e433f3134d0cd0b07b922360be622698b7b6c075d1089d64bfdf
---

场景化消息[请求体结构](../harmonyos-references/push-scenariozed-api-request-struct.md)中，请求URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

**请使用V3版本**的请求URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）进行消息推送。
