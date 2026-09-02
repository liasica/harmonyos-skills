---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataprotectionkit-7001
title: Data Protection Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Data Protection Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:98f6ced2f9649a4eafaa21b4aa95f4f7e418ead14efc4c1813eeac922d62c571
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE[since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 权限变更 | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE[since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 权限变更 | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE[since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：CustomProperty；  API声明：options?: DlpFileQueryOptions;  差异内容：options?: DlpFileQueryOptions; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function queryOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<Array<string>>;  差异内容：function queryOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<Array<string>>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>;  差异内容：function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export interface DlpFileQueryOptions  差异内容：export interface DlpFileQueryOptions | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpFileQueryOptions；  API声明：classificationLabel?: string;  差异内容：classificationLabel?: string; | api/@ohos.dlpPermission.d.ts |
