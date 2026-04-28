---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b035
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4ceff290093a9601ab826f125e289b2469e09d4c8459570f5c635cc560308487
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：14800014,202,401,801 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>;  差异内容：14800014,202,401,801 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>;  差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：14800014,202,401,801 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>;  差异内容：14800014,202,401,801 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>;  差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD\_DETAILS  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD\_DETAILS  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType；  API声明：DATA\_CHANGE  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：ChangeType；  API声明：DATA\_CHANGE  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType；  API声明：ASSET\_CHANGE  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：ChangeType；  API声明：ASSET\_CHANGE  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DistributedType；  API声明：DISTRIBUTED\_CLOUD  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：DistributedType；  API声明：DISTRIBUTED\_CLOUD  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>;  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>;  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig；  API声明：pluginLibs?: Array<string>;  差异内容：pluginLibs?: Array<string>; | api/@ohos.data.relationalStore.d.ts |
