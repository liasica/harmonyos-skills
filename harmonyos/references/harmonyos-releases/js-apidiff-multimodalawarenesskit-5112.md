---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-5112
title: Multimodal Awareness Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Release引入的API > Multimodal Awareness Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:22cc1f98aba85ab9ed7a42aae69855e7645f2c7478476b5cd9e6f28f0ac185d6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global；  API声明：declare namespace motion  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：global；  API声明：declare namespace motion  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion；  API声明：export enum OperatingHandStatus  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion；  API声明：export enum OperatingHandStatus  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：OperatingHandStatus；  API声明：UNKNOWN\_STATUS = 0  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：OperatingHandStatus；  API声明：UNKNOWN\_STATUS = 0  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：OperatingHandStatus；  API声明：LEFT\_HAND\_OPERATED = 1  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：OperatingHandStatus；  API声明：LEFT\_HAND\_OPERATED = 1  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：OperatingHandStatus；  API声明：RIGHT\_HAND\_OPERATED = 2  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：OperatingHandStatus；  API声明：RIGHT\_HAND\_OPERATED = 2  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
