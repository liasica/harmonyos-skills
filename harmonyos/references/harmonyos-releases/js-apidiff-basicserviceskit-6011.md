---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6011
title: Basic Services Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:57+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0d277d4966f525c4a2adb95f4058d094acdc8ef559c46a9badf98e1dfaeea61b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：deviceInfo；  API声明：const chipType: string;  差异内容：const chipType: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const bootCount: number;  差异内容：const bootCount: number; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：power；  API声明：export enum PowerKeyFilteringStrategy  差异内容：export enum PowerKeyFilteringStrategy | api/@ohos.power.d.ts |
| 新增API | NA | 类名：PowerKeyFilteringStrategy；  API声明：DISABLE\_LONG\_PRESS\_FILTERING = 0  差异内容：DISABLE\_LONG\_PRESS\_FILTERING = 0 | api/@ohos.power.d.ts |
| 新增API | NA | 类名：PowerKeyFilteringStrategy；  API声明：LONG\_PRESS\_FILTERING\_ONCE = 1  差异内容：LONG\_PRESS\_FILTERING\_ONCE = 1 | api/@ohos.power.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：enum SslType  差异内容：enum SslType | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：SslType；  API声明：TLS = 'TLS'  差异内容：TLS = 'TLS' | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：SslType；  API声明：TLCP = 'TLCP'  差异内容：TLCP = 'TLCP' | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：agent；  API声明：const VISIBILITY\_COMPLETION: 1;  差异内容：const VISIBILITY\_COMPLETION: 1; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent；  API声明：const VISIBILITY\_PROGRESS: 2;  差异内容：const VISIBILITY\_PROGRESS: 2; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：systemDateTime；  API声明：function getAutoTimeStatus(): boolean;  差异内容：function getAutoTimeStatus(): boolean; | api/@ohos.systemDateTime.d.ts |
| 新增API | NA | 类名：zlib；  API声明：export enum PathSeparatorStrategy  差异内容：export enum PathSeparatorStrategy | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：PathSeparatorStrategy；  API声明：PATH\_SEPARATOR\_STRATEGY\_DEFAULT = 0  差异内容：PATH\_SEPARATOR\_STRATEGY\_DEFAULT = 0 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：PathSeparatorStrategy；  API声明：PATH\_SEPARATOR\_STRATEGY\_REPLACE\_BACKSLASH = 1  差异内容：PATH\_SEPARATOR\_STRATEGY\_REPLACE\_BACKSLASH = 1 | api/@ohos.zlib.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CacheDownloadOptions；  API声明：sslType?: SslType;  差异内容：sslType?: SslType; | api/@ohos.request.cacheDownload.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CacheDownloadOptions；  API声明：caPath?: string;  差异内容：caPath?: string; | api/@ohos.request.cacheDownload.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Notification；  API声明：visibility?: number;  差异内容：visibility?: number; | api/@ohos.request.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Options；  API声明：pathSeparatorStrategy?: PathSeparatorStrategy;  差异内容：pathSeparatorStrategy?: PathSeparatorStrategy; | api/@ohos.zlib.d.ts |
