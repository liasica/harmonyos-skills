---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-assetstorekit-6001
title: Asset Store Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Asset Store Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:36+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f285978a6d09ce69dbb8a921c269486cf87647c2eaa652ed3e40f3a192f01181
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：asset；  API声明：function querySyncResult(query: AssetMap): Promise<SyncResult>;  差异内容：function querySyncResult(query: AssetMap): Promise<SyncResult>; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset；  API声明：interface SyncResult  差异内容：interface SyncResult | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：SyncResult；  API声明：readonly resultCode: number;  差异内容：readonly resultCode: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：SyncResult；  API声明：readonly totalCount?: number;  差异内容：readonly totalCount?: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：SyncResult；  API声明：readonly failedCount?: number;  差异内容：readonly failedCount?: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：ErrorCode；  API声明：PARAM\_VERIFICATION\_FAILED = 24000018  差异内容：PARAM\_VERIFICATION\_FAILED = 24000018 | api/@ohos.security.asset.d.ts |
