---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-7001
title: ArkData
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:7f91387cf26fa7b4b3a912248d4e3a711c279286077cd47126d2e28f1f376410
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：cloudData；  API声明：enum AutoSyncTriggerMode  差异内容：enum AutoSyncTriggerMode | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode；  API声明：ACCOUNT\_LOGIN = 0  差异内容：ACCOUNT\_LOGIN = 0 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode；  API声明：CLOUD\_SWITCH\_ON = 1  差异内容：CLOUD\_SWITCH\_ON = 1 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode；  API声明：NETWORK\_RECOVER = 2  差异内容：NETWORK\_RECOVER = 2 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode；  API声明：CLOUD\_DATA\_CHANGE = 3  差异内容：CLOUD\_DATA\_CHANGE = 3 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode；  API声明：USER\_CHANGE = 4  差异内容：USER\_CHANGE = 4 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData；  API声明：interface AutoSyncTriggerInfo  差异内容：interface AutoSyncTriggerInfo | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerInfo；  API声明：mode: AutoSyncTriggerMode;  差异内容：mode: AutoSyncTriggerMode; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData；  API声明：function onAutoSyncTrigger(observer: Callback<AutoSyncTriggerInfo>): void;  差异内容：function onAutoSyncTrigger(observer: Callback<AutoSyncTriggerInfo>): void; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData；  API声明：function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void;  差异内容：function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：enum DataProxyMaxValueLength  差异内容：enum DataProxyMaxValueLength | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyMaxValueLength；  API声明：MAX\_LENGTH\_4K = 4096  差异内容：MAX\_LENGTH\_4K = 4096 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyMaxValueLength；  API声明：MAX\_LENGTH\_100K = 102400  差异内容：MAX\_LENGTH\_100K = 102400 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyConfig；  API声明：maxValueLength?: DataProxyMaxValueLength;  差异内容：maxValueLength?: DataProxyMaxValueLength; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>;  差异内容：deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：SingleKVStore；  API声明：rekey(): Promise<void>;  差异内容：rekey(): Promise<void>; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_TO\_DOWNLOAD  差异内容：ASSET\_TO\_DOWNLOAD | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：STOP\_CLOUD\_SYNC = 8  差异内容：STOP\_CLOUD\_SYNC = 8 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressDetails；  API声明：message?: string;  差异内容：message?: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：enum AssetConflictPolicy  差异内容：enum AssetConflictPolicy | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetConflictPolicy；  API声明：CONFLICT\_POLICY\_DEFAULT = 0  差异内容：CONFLICT\_POLICY\_DEFAULT = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetConflictPolicy；  API声明：CONFLICT\_POLICY\_TIME\_FIRST = 1  差异内容：CONFLICT\_POLICY\_TIME\_FIRST = 1 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetConflictPolicy；  API声明：CONFLICT\_POLICY\_TEMP\_PATH = 2  差异内容：CONFLICT\_POLICY\_TEMP\_PATH = 2 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig；  API声明：assetConflictPolicy?: AssetConflictPolicy;  差异内容：assetConflictPolicy?: AssetConflictPolicy; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig；  API声明：assetTempPath?: string;  差异内容：assetTempPath?: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig；  API声明：assetDownloadOnDemand?: boolean;  差异内容：assetDownloadOnDemand?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig；  API声明：autoSyncSwitch?: boolean;  差异内容：autoSyncSwitch?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：interface CloudSyncConfig  差异内容：interface CloudSyncConfig | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CloudSyncConfig；  API声明：mode: SyncMode;  差异内容：mode: SyncMode; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CloudSyncConfig；  API声明：enablePredicate?: boolean;  差异内容：enablePredicate?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CloudSyncConfig；  API声明：predicate?: RdbPredicates;  差异内容：predicate?: RdbPredicates; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：enum SyncResultCode  差异内容：enum SyncResultCode | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：FAIL = 1  差异内容：FAIL = 1 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：OFFLINE = 2  差异内容：OFFLINE = 2 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：INVALID\_ARGS = 3  差异内容：INVALID\_ARGS = 3 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：DISTRIBUTED\_TABLE\_NOT\_SET = 4  差异内容：DISTRIBUTED\_TABLE\_NOT\_SET = 4 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：TABLE\_FIELD\_MISMATCH = 5  差异内容：TABLE\_FIELD\_MISMATCH = 5 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：DISTRIBUTED\_SCHEMA\_MISMATCH = 6  差异内容：DISTRIBUTED\_SCHEMA\_MISMATCH = 6 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：BUSY = 7  差异内容：BUSY = 7 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：CORRUPTED = 8  差异内容：CORRUPTED = 8 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：TIMEOUT = 9  差异内容：TIMEOUT = 9 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：SCHEMA\_CHANGED = 10  差异内容：SCHEMA\_CHANGED = 10 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode；  API声明：CONSTRAINT\_VIOLATION = 11  差异内容：CONSTRAINT\_VIOLATION = 11 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：interface SyncResult  差异内容：interface SyncResult | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResult；  API声明：readonly device: string;  差异内容：readonly device: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResult；  API声明：readonly code: SyncResultCode;  差异内容：readonly code: SyncResultCode; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResult；  API声明：readonly message: string;  差异内容：readonly message: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>;  差异内容：syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>;  差异内容：cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：stopCloudSync(): Promise<void>;  差异内容：stopCloudSync(): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：export const enum UriPermission  差异内容：export const enum UriPermission | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission；  API声明：READ = 1  差异内容：READ = 1 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission；  API声明：WRITE = 2  差异内容：WRITE = 2 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission；  API声明：PERSIST = 3  差异内容：PERSIST = 3 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties；  API声明：uriAuthorizationPolicies?: Array<UriPermission>;  差异内容：uriAuthorizationPolicies?: Array<UriPermission>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：HTML；  API声明：uriAuthorizationPolicies?: Array<number>;  差异内容：uriAuthorizationPolicies?: Array<number>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：FileUri；  API声明：uriAuthorizationPolicies?: Array<number>;  差异内容：uriAuthorizationPolicies?: Array<number>; | api/@ohos.data.uniformDataStruct.d.ts |
