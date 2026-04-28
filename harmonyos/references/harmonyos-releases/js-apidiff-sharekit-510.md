---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-510
title: Share Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Share Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3279ee44757d84ac60f7840d69d37c9cab9da2b4e60f657989b8badddee9c882
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：systemShare；  API声明：enum ShareAbilityName  差异内容：enum ShareAbilityName | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：COPY\_TO\_PASTEBOARD = 'SystemShare\_CopyToPasteboard'  差异内容：COPY\_TO\_PASTEBOARD = 'SystemShare\_CopyToPasteboard' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：SAVE\_TO\_MEDIA\_ASSET = 'SystemShare\_SaveToMediaAsset'  差异内容：SAVE\_TO\_MEDIA\_ASSET = 'SystemShare\_SaveToMediaAsset' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：SAVE\_AS\_FILE = 'SystemShare\_SaveAsFile'  差异内容：SAVE\_AS\_FILE = 'SystemShare\_SaveAsFile' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：PRINT = 'SystemShare\_Print'  差异内容：PRINT = 'SystemShare\_Print' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：SAVE\_TO\_SUPERHUB = 'SystemShare\_Superhub'  差异内容：SAVE\_TO\_SUPERHUB = 'SystemShare\_Superhub' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：COLLECTION = 'SystemShare\_Collection'  差异内容：COLLECTION = 'SystemShare\_Collection' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：HARMONYSHARE = 'SystemShare\_HarmonyShare'  差异内容：HARMONYSHARE = 'SystemShare\_HarmonyShare' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName；  API声明：ENCRYPT = 'SystemShare\_Encrypt'  差异内容：ENCRYPT = 'SystemShare\_Encrypt' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：systemShare；  API声明：interface ShareAbilityInfo  差异内容：interface ShareAbilityInfo | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityInfo；  API声明：name: string;  差异内容：name: string; | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：systemShare；  API声明：interface ShareOperationResult  差异内容：interface ShareOperationResult | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareOperationResult；  API声明：targetAbilityInfo: ShareAbilityInfo;  差异内容：targetAbilityInfo: ShareAbilityInfo; | api/@hms.collaboration.systemShare.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ShareController；  API声明：on(type: 'shareCompleted', callback: Callback<ShareOperationResult>): void;  差异内容：on(type: 'shareCompleted', callback: Callback<ShareOperationResult>): void; | api/@hms.collaboration.systemShare.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ShareController；  API声明：off(type: 'shareCompleted', callback?: Callback<ShareOperationResult>): void;  差异内容：off(type: 'shareCompleted', callback?: Callback<ShareOperationResult>): void; | api/@hms.collaboration.systemShare.d.ts |
