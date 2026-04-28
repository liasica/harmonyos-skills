---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pushkit-b123sp18
title: Push Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Push Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:695dd33ee692c746e6e569607a83a31e31131015761a2e1e0a1837c2f865c407
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：pushService；  API声明：export function receiveMessage(pushType: 'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY', ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void;  差异内容：pushType: 'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY' | 类名：pushService；  API声明：export function receiveMessage(pushType: PushType, ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void;  差异内容：pushType: PushType | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService；  API声明：export type PushType = 'DEFAULT' | 'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY';  差异内容：export type PushType = 'DEFAULT' | 'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY'; | api/@hms.core.push.pushService.d.ts |
