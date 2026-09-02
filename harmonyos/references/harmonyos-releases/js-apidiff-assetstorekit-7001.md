---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-assetstorekit-7001
title: Asset Store Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Asset Store Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:5867b4353340d8cc417231c66e93b36dd58ad1a7a018d6f23ee82b57d9148494
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：asset；  API声明：function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>;  差异内容：function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset；  API声明：function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>;  差异内容：function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset；  API声明：function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>;  差异内容：function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset；  API声明：interface BatchErrInfo  差异内容：interface BatchErrInfo | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchErrInfo；  API声明：index: number;  差异内容：index: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchErrInfo；  API声明：errCode: number;  差异内容：errCode: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchErrInfo；  API声明：message: string;  差异内容：message: string; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset；  API声明：interface BatchResult  差异内容：interface BatchResult | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchResult；  API声明：failedCount: number;  差异内容：failedCount: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchResult；  API声明：failedErrorInfos: Array<BatchErrInfo>;  差异内容：failedErrorInfos: Array<BatchErrInfo>; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：INCONSISTENT\_ATTRIBUTE = 24000019  差异内容：INCONSISTENT\_ATTRIBUTE = 24000019 | api/@ohos.security.asset.d.ts |
