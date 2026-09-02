---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-7002
title: Multimodal Awareness Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Multimodal Awareness Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0a9632e21560feb579562cab363b213ab90c9f834c21463a3f334e667333fe61
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE | 类名：motion；  API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE [since 20] | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE | 类名：motion；  API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE [since 20] | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE | 类名：motion；  API声明：function getRecentOperatingHandStatus(): OperatingHandStatus;  差异内容：ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE [since 20] | api/@ohos.multimodalAwareness.motion.d.ts |
