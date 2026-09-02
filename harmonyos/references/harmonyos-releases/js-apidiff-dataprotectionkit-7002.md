---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataprotectionkit-7002
title: Data Protection Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Data Protection Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:704702a6fda0f3233a5c4d3a3fcc491cfe159200477020cfa84a93d9eadbe85c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE[since 26.0.0] | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE [since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 权限变更 | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE[since 26.0.0] | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE [since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 权限变更 | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE[since 26.0.0] | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE or ohos.permission.ACCESS\_DLP\_SERVICE [since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>;  差异内容：function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function getControlledAppLists(): Promise<Array<string>>;  差异内容：function getControlledAppLists(): Promise<Array<string>>; | api/@ohos.dlpPermission.d.ts |
