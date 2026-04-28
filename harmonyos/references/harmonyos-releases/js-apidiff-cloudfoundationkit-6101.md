---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cloudfoundationkit-6101
title: Cloud Foundation Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Cloud Foundation Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b6228d09ac570b57d364017c9a463edf8ae8f89e0533350d50ebe588546bac6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：cloudResPrefetch；  API声明：function getPrefetchResult(mode: PrefetchMode): Promise<PrefetchResult>;  差异内容：NA | 类名：cloudResPrefetch；  API声明：function getPrefetchResult(mode: PrefetchMode, params?: PrefetchParams): Promise<PrefetchResult>;  差异内容：params?: PrefetchParams | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 函数变更 | 类名：cloudResPrefetch；  API声明：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>): void;  差异内容：NA | 类名：cloudResPrefetch；  API声明：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>, params?: PrefetchParams): void;  差异内容：params?: PrefetchParams | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchMode；  API声明：LINK\_PREFETCH = 3  差异内容：LINK\_PREFETCH = 3 | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch；  API声明：interface PrefetchParams  差异内容：interface PrefetchParams | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchParams；  API声明：link?: string;  差异内容：link?: string; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
