---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-5032
title: Multimodal Awareness Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Multimodal Awareness Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3ae909a6a4a13f35157e11ba7b2bf6eb86199b87bf37e82168e4bc7bdf8950b4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace motion  差异内容： declare namespace motion | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion；  API声明： export enum OperatingHandStatus  差异内容： export enum OperatingHandStatus | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：OperatingHandStatus；  API声明：UNKNOWN\_STATUS = 0  差异内容：UNKNOWN\_STATUS = 0 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：OperatingHandStatus；  API声明：LEFT\_HAND\_OPERATED = 1  差异内容：LEFT\_HAND\_OPERATED = 1 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：OperatingHandStatus；  API声明：RIGHT\_HAND\_OPERATED = 2  差异内容：RIGHT\_HAND\_OPERATED = 2 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void; | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void; | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：function getRecentOperatingHandStatus(): OperatingHandStatus; | api/@ohos.multimodalAwareness.motion.d.ts |
| kit变更 | NA | MultimodalAwarenessKit | api/@ohos.multimodalAwareness.motion.d.ts |
