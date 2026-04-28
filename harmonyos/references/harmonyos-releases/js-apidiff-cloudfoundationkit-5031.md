---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cloudfoundationkit-5031
title: Cloud Foundation Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > Cloud Foundation Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:40+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:445f3a8729b5ce127ec12dd44186995dfad7b10dba3354c6017da787953bce68
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace cloudResPrefetch  差异内容： declare namespace cloudResPrefetch | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明：function registerPrefetchTask(options: PrefetchOptions): void;  差异内容：function registerPrefetchTask(options: PrefetchOptions): void; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明：function getPrefetchResult(mode: PrefetchMode): Promise<PrefetchResult>;  差异内容：function getPrefetchResult(mode: PrefetchMode): Promise<PrefetchResult>; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>): void;  差异内容：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>): void; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明： interface PrefetchOptions  差异内容： interface PrefetchOptions | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchOptions；  API声明：token?: string;  差异内容：token?: string; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchOptions；  API声明：params?: string | Object;  差异内容：params?: string | Object; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明： enum PrefetchMode  差异内容： enum PrefetchMode | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchMode；  API声明：INSTALL\_PREFETCH = 1  差异内容：INSTALL\_PREFETCH = 1 | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchMode；  API声明：PERIODIC\_PREFETCH = 2  差异内容：PERIODIC\_PREFETCH = 2 | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明： interface PrefetchResult  差异内容： interface PrefetchResult | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchResult；  API声明：result: string | Object;  差异内容：result: string | Object; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchResult；  API声明：timestamp: Date;  差异内容：timestamp: Date; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchResult；  API声明：token: string;  差异内容：token: string; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
