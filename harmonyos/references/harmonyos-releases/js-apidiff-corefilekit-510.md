---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-510
title: Core File Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:23a41d9e02efbd22c635185a1389a58548db859f40472a419db0643cb86b0a54
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：PhotoViewMIMETypes；  API声明：IMAGE\_TYPE = 'image/\*'  差异内容：NA | 类名：PhotoViewMIMETypes；  API声明：IMAGE\_TYPE = 'image/\*'  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewMIMETypes；  API声明：VIDEO\_TYPE = 'video/\*'  差异内容：NA | 类名：PhotoViewMIMETypes；  API声明：VIDEO\_TYPE = 'video/\*'  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewMIMETypes；  API声明：IMAGE\_VIDEO\_TYPE = '/'  差异内容：NA | 类名：PhotoViewMIMETypes；  API声明：IMAGE\_VIDEO\_TYPE = '/'  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectOptions；  API声明：MIMEType?: PhotoViewMIMETypes;  差异内容：NA | 类名：PhotoSelectOptions；  API声明：MIMEType?: PhotoViewMIMETypes;  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectOptions；  API声明：maxSelectNumber?: number;  差异内容：NA | 类名：PhotoSelectOptions；  API声明：maxSelectNumber?: number;  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectResult；  API声明：photoUris: Array<string>;  差异内容：NA | 类名：PhotoSelectResult；  API声明：photoUris: Array<string>;  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectResult；  API声明：isOriginalPhoto: boolean;  差异内容：NA | 类名：PhotoSelectResult；  API声明：isOriginalPhoto: boolean;  差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSaveOptions；  API声明：newFileNames?: Array<string>;  差异内容：NA | 类名：PhotoSaveOptions；  API声明：newFileNames?: Array<string>;  差异内容：18 | api/@ohos.file.picker.d.ts |
| 起始版本有变化 | 类名：storageStatistics；  API声明：function getTotalSize(callback: AsyncCallback<number>): void;  差异内容：9 | 类名：storageStatistics；  API声明：function getTotalSize(callback: AsyncCallback<number>): void;  差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics；  API声明：function getTotalSize(): Promise<number>;  差异内容：9 | 类名：storageStatistics；  API声明：function getTotalSize(): Promise<number>;  差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics；  API声明：function getTotalSizeSync(): number;  差异内容：10 | 类名：storageStatistics；  API声明：function getTotalSizeSync(): number;  差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics；  API声明：function getFreeSize(callback: AsyncCallback<number>): void;  差异内容：9 | 类名：storageStatistics；  API声明：function getFreeSize(callback: AsyncCallback<number>): void;  差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics；  API声明：function getFreeSize(): Promise<number>;  差异内容：9 | 类名：storageStatistics；  API声明：function getFreeSize(): Promise<number>;  差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics；  API声明：function getFreeSizeSync(): number;  差异内容：10 | 类名：storageStatistics；  API声明：function getFreeSizeSync(): number;  差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
