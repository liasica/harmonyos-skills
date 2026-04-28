---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-hdc
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ff2909cfe6f770ab2ed0a6cba2db4b42b0a8207606026889069e838ea4bdbdac
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global；  API声明： export interface GetStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core | 类名：global；  API声明： export interface GetStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core.Lite | api/@system.storage.d.ts |
| syscap变更 | 类名：global；  API声明： export interface SetStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core | 类名：global；  API声明： export interface SetStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core.Lite | api/@system.storage.d.ts |
| syscap变更 | 类名：global；  API声明： export interface ClearStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core | 类名：global；  API声明： export interface ClearStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core.Lite | api/@system.storage.d.ts |
| syscap变更 | 类名：global；  API声明： export interface DeleteStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core | 类名：global；  API声明： export interface DeleteStorageOptions  差异内容：SystemCapability.DistributedDataManager.Preferences.Core.Lite | api/@system.storage.d.ts |
| syscap变更 | 类名：global；  API声明： export default class Storage  差异内容：SystemCapability.DistributedDataManager.Preferences.Core | 类名：global；  API声明： export default class Storage  差异内容：SystemCapability.DistributedDataManager.Preferences.Core.Lite | api/@system.storage.d.ts |
| 错误码变更 | 类名：DataObject；  API声明：setSessionId(sessionId: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(sessionId: string, callback: AsyncCallback<void>): void;  差异内容：15400001,201,401 | api/@ohos.data.distributedDataObject.d.ts |
| 错误码变更 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：15400001,201,401 | api/@ohos.data.distributedDataObject.d.ts |
| 错误码变更 | 类名：DataObject；  API声明：setSessionId(sessionId?: string): Promise<void>;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(sessionId?: string): Promise<void>;  差异内容：15400001,201,401 | api/@ohos.data.distributedDataObject.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：clear(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Preferences；  API声明：clear(callback: AsyncCallback<void>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：clear(): Promise<void>;  差异内容：NA | 类名：Preferences；  API声明：clear(): Promise<void>;  差异内容：15500000 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：flush(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Preferences；  API声明：flush(callback: AsyncCallback<void>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：flush(): Promise<void>;  差异内容：NA | 类名：Preferences；  API声明：flush(): Promise<void>;  差异内容：15500000 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：put(key: string, value: Uint8Array | string | number | boolean): Promise<void>;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：put(key: string, value: Uint8Array | string | number | boolean): Promise<void>;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：putBatch(entries: Entry[], callback: AsyncCallback<void>): void;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：putBatch(entries: Entry[], callback: AsyncCallback<void>): void;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：putBatch(entries: Entry[]): Promise<void>;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：putBatch(entries: Entry[]): Promise<void>;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：delete(key: string, callback: AsyncCallback<void>): void;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：delete(key: string, callback: AsyncCallback<void>): void;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：delete(key: string): Promise<void>;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：delete(key: string): Promise<void>;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：deleteBatch(keys: string[], callback: AsyncCallback<void>): void;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：deleteBatch(keys: string[], callback: AsyncCallback<void>): void;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：deleteBatch(keys: string[]): Promise<void>;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：deleteBatch(keys: string[]): Promise<void>;  差异内容：14800047,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：getResultSet(keyPrefix: string): Promise<KVStoreResultSet>;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：getResultSet(keyPrefix: string): Promise<KVStoreResultSet>;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：getResultSet(query: Query): Promise<KVStoreResultSet>;  差异内容：15100003,15100005,401 | 类名：SingleKVStore；  API声明：getResultSet(query: Query): Promise<KVStoreResultSet>;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：startTransaction(callback: AsyncCallback<void>): void;  差异内容：15100005 | 类名：SingleKVStore；  API声明：startTransaction(callback: AsyncCallback<void>): void;  差异内容：14800047,15100005 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：SingleKVStore；  API声明：startTransaction(): Promise<void>;  差异内容：15100005 | 类名：SingleKVStore；  API声明：startTransaction(): Promise<void>;  差异内容：14800047,15100005 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(keyPrefix: string): Promise<KVStoreResultSet>;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(keyPrefix: string): Promise<KVStoreResultSet>;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(query: Query): Promise<KVStoreResultSet>;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(query: Query): Promise<KVStoreResultSet>;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>;  差异内容：15100003,15100005,401 | 类名：DeviceKVStore；  API声明：getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>;  差异内容：15100001,15100003,15100005,401 | api/@ohos.data.distributedKVStore.d.ts |
| 错误码变更 | 类名：preferences；  API声明：function getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>): void;  差异内容：401 | 类名：preferences；  API声明：function getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：preferences；  API声明：function getPreferences(context: Context, name: string): Promise<Preferences>;  差异内容：401 | 类名：preferences；  API声明：function getPreferences(context: Context, name: string): Promise<Preferences>;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：preferences；  API声明：function deletePreferences(context: Context, name: string, callback: AsyncCallback<void>): void;  差异内容：15500010,401 | 类名：preferences；  API声明：function deletePreferences(context: Context, name: string, callback: AsyncCallback<void>): void;  差异内容：15500000,15500010,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：preferences；  API声明：function deletePreferences(context: Context, name: string): Promise<void>;  差异内容：15500010,401 | 类名：preferences；  API声明：function deletePreferences(context: Context, name: string): Promise<void>;  差异内容：15500000,15500010,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：preferences；  API声明：function removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void;  差异内容：401 | 类名：preferences；  API声明：function removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：preferences；  API声明：function removePreferencesFromCache(context: Context, name: string): Promise<void>;  差异内容：401 | 类名：preferences；  API声明：function removePreferencesFromCache(context: Context, name: string): Promise<void>;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void;  差异内容：401 | 类名：Preferences；  API声明：get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：get(key: string, defValue: ValueType): Promise<ValueType>;  差异内容：401 | 类名：Preferences；  API声明：get(key: string, defValue: ValueType): Promise<ValueType>;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：getAll(callback: AsyncCallback<Object>): void;  差异内容：401 | 类名：Preferences；  API声明：getAll(callback: AsyncCallback<Object>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：has(key: string, callback: AsyncCallback<boolean>): void;  差异内容：401 | 类名：Preferences；  API声明：has(key: string, callback: AsyncCallback<boolean>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：has(key: string): Promise<boolean>;  差异内容：401 | 类名：Preferences；  API声明：has(key: string): Promise<boolean>;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：put(key: string, value: ValueType, callback: AsyncCallback<void>): void;  差异内容：401 | 类名：Preferences；  API声明：put(key: string, value: ValueType, callback: AsyncCallback<void>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：put(key: string, value: ValueType): Promise<void>;  差异内容：401 | 类名：Preferences；  API声明：put(key: string, value: ValueType): Promise<void>;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：delete(key: string, callback: AsyncCallback<void>): void;  差异内容：401 | 类名：Preferences；  API声明：delete(key: string, callback: AsyncCallback<void>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：delete(key: string): Promise<void>;  差异内容：401 | 类名：Preferences；  API声明：delete(key: string): Promise<void>;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：on(type: 'change', callback: Callback<{  key: string;  }>): void;  差异内容：401 | 类名：Preferences；  API声明：on(type: 'change', callback: Callback<string>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：off(type: 'change', callback?: Callback<{  key: string;  }>): void;  差异内容：401 | 类名：Preferences；  API声明：off(type: 'change', callback?: Callback<string>): void;  差异内容：15500000,401 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：relationalStore；  API声明：function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void;  差异内容：14800010,401 | 类名：relationalStore；  API声明：function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void;  差异内容：14800000,14800010,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：relationalStore；  API声明：function deleteRdbStore(context: Context, name: string): Promise<void>;  差异内容：14800010,401 | 类名：relationalStore；  API声明：function deleteRdbStore(context: Context, name: string): Promise<void>;  差异内容：14800000,14800010,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void;  差异内容：401 | 类名：RdbStore；  API声明：insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：insert(table: string, values: ValuesBucket): Promise<number>;  差异内容：401 | 类名：RdbStore；  API声明：insert(table: string, values: ValuesBucket): Promise<number>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void;  差异内容：401 | 类名：RdbStore；  API声明：batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>;  差异内容：401 | 类名：RdbStore；  API声明：batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void;  差异内容：401 | 类名：RdbStore；  API声明：update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>;  差异内容：401 | 类名：RdbStore；  API声明：update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void;  差异内容：401 | 类名：RdbStore；  API声明：delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：delete(predicates: RdbPredicates): Promise<number>;  差异内容：401 | 类名：RdbStore；  API声明：delete(predicates: RdbPredicates): Promise<number>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;  差异内容：401 | 类名：RdbStore；  API声明：query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;  差异内容：14800000,14800014,14800015,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;  差异内容：401 | 类名：RdbStore；  API声明：query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;  差异内容：14800000,14800014,14800015,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void;  差异内容：401 | 类名：RdbStore；  API声明：querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void;  差异内容：14800000,14800014,14800015,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>;  差异内容：401 | 类名：RdbStore；  API声明：querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>;  差异内容：14800000,14800014,14800015,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void;  差异内容：401 | 类名：RdbStore；  API声明：executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>;  差异内容：401 | 类名：RdbStore；  API声明：executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：beginTransaction(): void;  差异内容：401 | 类名：RdbStore；  API声明：beginTransaction(): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,14800047,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：commit(): void;  差异内容：401 | 类名：RdbStore；  API声明：commit(): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：rollBack(): void;  差异内容：401 | 类名：RdbStore；  API声明：rollBack(): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：backup(destName: string, callback: AsyncCallback<void>): void;  差异内容：401 | 类名：RdbStore；  API声明：backup(destName: string, callback: AsyncCallback<void>): void;  差异内容：14800000,14800010,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：backup(destName: string): Promise<void>;  差异内容：401 | 类名：RdbStore；  API声明：backup(destName: string): Promise<void>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：restore(srcName: string, callback: AsyncCallback<void>): void;  差异内容：401 | 类名：RdbStore；  API声明：restore(srcName: string, callback: AsyncCallback<void>): void;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：restore(srcName: string): Promise<void>;  差异内容：401 | 类名：RdbStore；  API声明：restore(srcName: string): Promise<void>;  差异内容：14800000,14800011,14800014,14800015,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void;  差异内容：401,801 | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>): Promise<void>;  差异内容：401,801 | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>): Promise<void>;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void;  差异内容：401,801 | 类名：RdbStore；  API声明：obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：obtainDistributedTableName(device: string, table: string): Promise<string>;  差异内容：401,801 | 类名：RdbStore；  API声明：obtainDistributedTableName(device: string, table: string): Promise<string>;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[  string,  number  ]>>): void;  差异内容：401,801 | 类名：RdbStore；  API声明：sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[  string,  number  ]>>): void;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[  string,  number  ]>>;  差异内容：401,801 | 类名：RdbStore；  API声明：sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[  string,  number  ]>>;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;  差异内容：401,801 | 类名：RdbStore；  API声明：remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>;  差异内容：401,801 | 类名：RdbStore；  API声明：remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>;  差异内容：14800000,14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;  差异内容：401,801 | 类名：RdbStore；  API声明：on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;  差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore；  API声明：off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;  差异内容：401,801 | 类名：RdbStore；  API声明：off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;  差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：goToFirstRow(): boolean;  差异内容：14800012 | 类名：ResultSet；  API声明：goToFirstRow(): boolean;  差异内容：14800000,14800011,14800012,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：goToLastRow(): boolean;  差异内容：14800012 | 类名：ResultSet；  API声明：goToLastRow(): boolean;  差异内容：14800000,14800011,14800012,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：goToNextRow(): boolean;  差异内容：14800012 | 类名：ResultSet；  API声明：goToNextRow(): boolean;  差异内容：14800000,14800011,14800012,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：goToPreviousRow(): boolean;  差异内容：14800012 | 类名：ResultSet；  API声明：goToPreviousRow(): boolean;  差异内容：14800000,14800011,14800012,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：close(): void;  差异内容：14800012 | 类名：ResultSet；  API声明：close(): void;  差异内容：14800000,14800012 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：DataObject；  API声明：revokeSave(): Promise<RevokeSaveSuccessResponse>;  差异内容：401,801 | 类名：DataObject；  API声明：revokeSave(): Promise<RevokeSaveSuccessResponse>;  差异内容：801 | api/@ohos.data.distributedDataObject.d.ts |
| 错误码变更 | 类名：Preferences；  API声明：getAll(): Promise<Object>;  差异内容：401 | 类名：Preferences；  API声明：getAll(): Promise<Object>;  差异内容：15500000 | api/@ohos.data.preferences.d.ts |
| 错误码变更 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void;  差异内容：14800010,14800011,401 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void;  差异内容：14800000,14800010,14800011,14800017,14800021,14800022,14800023,14800027,14800028,14800029,14800030,14801001,14801002,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>;  差异内容：14800010,14800011,401 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>;  差异内容：14800000,14800010,14800011,14800017,14800021,14800027,14800028,14800029,14800030,14801001,14801002,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：getColumnIndex(columnName: string): number;  差异内容：14800013,401 | 类名：ResultSet；  API声明：getColumnIndex(columnName: string): number;  差异内容：14800000,14800011,14800013,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：getColumnName(columnIndex: number): string;  差异内容：14800013,401 | 类名：ResultSet；  API声明：getColumnName(columnIndex: number): string;  差异内容：14800000,14800011,14800013,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：goTo(offset: number): boolean;  差异内容：14800012,401 | 类名：ResultSet；  API声明：goTo(offset: number): boolean;  差异内容：14800000,14800011,14800012,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：goToRow(position: number): boolean;  差异内容：14800012,401 | 类名：ResultSet；  API声明：goToRow(position: number): boolean;  差异内容：14800000,14800011,14800012,14800014,14800019,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：getBlob(columnIndex: number): Uint8Array;  差异内容：14800013,401 | 类名：ResultSet；  API声明：getBlob(columnIndex: number): Uint8Array;  差异内容：14800000,14800011,14800012,14800013,14800014,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：getString(columnIndex: number): string;  差异内容：14800013,401 | 类名：ResultSet；  API声明：getString(columnIndex: number): string;  差异内容：14800000,14800011,14800012,14800013,14800014,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：getLong(columnIndex: number): number;  差异内容：14800013,401 | 类名：ResultSet；  API声明：getLong(columnIndex: number): number;  差异内容：14800000,14800011,14800012,14800013,14800014,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：getDouble(columnIndex: number): number;  差异内容：14800013,401 | 类名：ResultSet；  API声明：getDouble(columnIndex: number): number;  差异内容：14800000,14800011,14800012,14800013,14800014,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：ResultSet；  API声明：isColumnNull(columnIndex: number): boolean;  差异内容：14800013,401 | 类名：ResultSet；  API声明：isColumnNull(columnIndex: number): boolean;  差异内容：14800000,14800011,14800012,14800013,14800014,14800021,14800022,14800023,14800024,14800025,14800026,14800027,14800028,14800029,14800030,14800031,14800032,14800033,14800034,401 | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DataObject；  API声明：setSessionId(sessionId: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(sessionId: string, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.data.distributedDataObject.d.ts |
| 权限变更 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.data.distributedDataObject.d.ts |
| 权限变更 | 类名：DataObject；  API声明：setSessionId(sessionId?: string): Promise<void>;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(sessionId?: string): Promise<void>;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.data.distributedDataObject.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_REMOTE = 0  差异内容：NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_REMOTE = 0  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.data.rdb.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_REMOTE = 0  差异内容：NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_REMOTE = 0  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SingleKVStore；  API声明：sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC occurs: {@code INVALID\_ARGUMENT}, {@code SERVER\_UNAVAILABLE}, {@code IPC\_ERROR}, and {@code DB\_ERROR}. | 类名：SingleKVStore；  API声明：sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | api/@ohos.data.distributedData.d.ts |
| 函数变更 | 类名：DistributedObject；  API声明：on(type: 'change', callback: Callback<{  sessionId: string;  fields: Array<string>;  }>): void;  差异内容：callback: Callback<{  sessionId: string;  fields: Array<string>;  }> | 类名：DistributedObject；  API声明：on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void;  差异内容：callback: (sessionId: string, fields: Array<string>) => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DistributedObject；  API声明：off(type: 'change', callback?: Callback<{  sessionId: string;  fields: Array<string>;  }>): void;  差异内容：callback?: Callback<{  sessionId: string;  fields: Array<string>;  }> | 类名：DistributedObject；  API声明：off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void;  差异内容：callback?: (sessionId: string, fields: Array<string>) => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DistributedObject；  API声明：on(type: 'status', callback: Callback<{  sessionId: string;  networkId: string;  status: 'online' | 'offline';  }>): void;  差异内容：callback: Callback<{  sessionId: string;  networkId: string;  status: 'online' | 'offline';  }> | 类名：DistributedObject；  API声明：on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;  差异内容：callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DistributedObject；  API声明：off(type: 'status', callback?: Callback<{  sessionId: string;  deviceId: string;  status: 'online' | 'offline';  }>): void;  差异内容：callback?: Callback<{  sessionId: string;  deviceId: string;  status: 'online' | 'offline';  }> | 类名：DistributedObject；  API声明：off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;  差异内容：callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DataObject；  API声明：on(type: 'change', callback: Callback<{  sessionId: string;  fields: Array<string>;  }>): void;  差异内容：callback: Callback<{  sessionId: string;  fields: Array<string>;  }> | 类名：DataObject；  API声明：on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void;  差异内容：callback: (sessionId: string, fields: Array<string>) => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DataObject；  API声明：off(type: 'change', callback?: Callback<{  sessionId: string;  fields: Array<string>;  }>): void;  差异内容：callback?: Callback<{  sessionId: string;  fields: Array<string>;  }> | 类名：DataObject；  API声明：off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void;  差异内容：callback?: (sessionId: string, fields: Array<string>) => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DataObject；  API声明：on(type: 'status', callback: Callback<{  sessionId: string;  networkId: string;  status: 'online' | 'offline';  }>): void;  差异内容：callback: Callback<{  sessionId: string;  networkId: string;  status: 'online' | 'offline';  }> | 类名：DataObject；  API声明：on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;  差异内容：callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：DataObject；  API声明：off(type: 'status', callback?: Callback<{  sessionId: string;  deviceId: string;  status: 'online' | 'offline';  }>): void;  差异内容：callback?: Callback<{  sessionId: string;  deviceId: string;  status: 'online' | 'offline';  }> | 类名：DataObject；  API声明：off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;  差异内容：callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void | api/@ohos.data.distributedDataObject.d.ts |
| 函数变更 | 类名：Preferences；  API声明：on(type: 'change', callback: Callback<{  key: string;  }>): void;  差异内容：callback: Callback<{  key: string;  }> | 类名：Preferences；  API声明：on(type: 'change', callback: Callback<string>): void;  差异内容：callback: Callback<string> | api/@ohos.data.preferences.d.ts |
| 函数变更 | 类名：Preferences；  API声明：off(type: 'change', callback?: Callback<{  key: string;  }>): void;  差异内容：callback?: Callback<{  key: string;  }> | 类名：Preferences；  API声明：off(type: 'change', callback?: Callback<string>): void;  差异内容：callback?: Callback<string> | api/@ohos.data.preferences.d.ts |
| 属性变更 | 类名：KVManagerConfig；  API声明：context: Context;  差异内容：Context | 类名：KVManagerConfig；  API声明：context: BaseContext;  差异内容：BaseContext | api/@ohos.data.distributedKVStore.d.ts |
| 自定义类型变更 | 类名：relationalStore；  API声明：type ValuesBucket = {  [key: string]: ValueType | Uint8Array | null;  };  差异内容：{  [key: string]: ValueType | Uint8Array | null;  } | 类名：relationalStore；  API声明：type ValuesBucket = Record<string, ValueType>;  差异内容：Record<string, ValueType> | api/@ohos.data.relationalStore.d.ts |
| 自定义类型变更 | 类名：preferences；  API声明：type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean>;  差异内容：number | string | boolean | Array<number> | Array<string> | Array<boolean> | 类名：preferences；  API声明：type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint;  差异内容：number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint | api/@ohos.data.preferences.d.ts |
| 自定义类型变更 | 类名：relationalStore；  API声明：type ValueType = number | string | boolean | Uint8Array;  差异内容：number | string | boolean | Uint8Array | 类名：relationalStore；  API声明：type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets | Float32Array | bigint;  差异内容：null | number | string | boolean | Uint8Array | Asset | Assets | Float32Array | bigint | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：distributedDataObject；  API声明： interface BindInfo  差异内容： interface BindInfo | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：BindInfo；  API声明：storeName: string;  差异内容：storeName: string; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：BindInfo；  API声明：tableName: string;  差异内容：tableName: string; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：BindInfo；  API声明：primaryKey: commonType.ValuesBucket;  差异内容：primaryKey: commonType.ValuesBucket; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：BindInfo；  API声明：field: string;  差异内容：field: string; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：BindInfo；  API声明：assetName: string;  差异内容：assetName: string; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：DataObject；  API声明：bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void;  差异内容：bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：DataObject；  API声明：bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>;  差异内容：bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function getPreferences(context: Context, options: Options, callback: AsyncCallback<Preferences>): void;  差异内容：function getPreferences(context: Context, options: Options, callback: AsyncCallback<Preferences>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function getPreferences(context: Context, options: Options): Promise<Preferences>;  差异内容：function getPreferences(context: Context, options: Options): Promise<Preferences>; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void;  差异内容：function deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function deletePreferences(context: Context, options: Options): Promise<void>;  差异内容：function deletePreferences(context: Context, options: Options): Promise<void>; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void;  差异内容：function removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function removePreferencesFromCache(context: Context, options: Options): Promise<void>;  差异内容：function removePreferencesFromCache(context: Context, options: Options): Promise<void>; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明： interface Options  差异内容： interface Options | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Options；  API声明：name: string;  差异内容：name: string; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Options；  API声明：dataGroupId?: string | null | undefined;  差异内容：dataGroupId?: string | null | undefined; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function getPreferencesSync(context: Context, options: Options): Preferences;  差异内容：function getPreferencesSync(context: Context, options: Options): Preferences; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function removePreferencesFromCacheSync(context: Context, name: string): void;  差异内容：function removePreferencesFromCacheSync(context: Context, name: string): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function removePreferencesFromCacheSync(context: Context, options: Options): void;  差异内容：function removePreferencesFromCacheSync(context: Context, options: Options): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：getSync(key: string, defValue: ValueType): ValueType;  差异内容：getSync(key: string, defValue: ValueType): ValueType; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：getAllSync(): Object;  差异内容：getAllSync(): Object; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：hasSync(key: string): boolean;  差异内容：hasSync(key: string): boolean; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：putSync(key: string, value: ValueType): void;  差异内容：putSync(key: string, value: ValueType): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：deleteSync(key: string): void;  差异内容：deleteSync(key: string): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：clearSync(): void;  差异内容：clearSync(): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：on(type: 'multiProcessChange', callback: Callback<string>): void;  差异内容：on(type: 'multiProcessChange', callback: Callback<string>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void;  差异内容：on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：off(type: 'multiProcessChange', callback?: Callback<string>): void;  差异内容：off(type: 'multiProcessChange', callback?: Callback<string>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void;  差异内容：off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void;  差异内容：function deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function deleteRdbStore(context: Context, config: StoreConfig): Promise<void>;  差异内容：function deleteRdbStore(context: Context, config: StoreConfig): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>): void;  差异内容：insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<number>;  差异内容：insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution, callback: AsyncCallback<number>): void;  差异内容：update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution, callback: AsyncCallback<number>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<number>;  差异内容：update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void;  差异内容：query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：querySql(sql: string, callback: AsyncCallback<ResultSet>): void;  差异内容：querySql(sql: string, callback: AsyncCallback<ResultSet>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：executeSql(sql: string, callback: AsyncCallback<void>): void;  差异内容：executeSql(sql: string, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：commit(txId: number): Promise<void>;  差异内容：commit(txId: number): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void;  差异内容：setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>, type: DistributedType, config: DistributedConfig, callback: AsyncCallback<void>): void;  差异内容：setDistributedTables(tables: Array<string>, type: DistributedType, config: DistributedConfig, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>;  差异内容：setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void;  差异内容：on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：off(event: 'dataChange', type: SubscribeType, observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void;  差异内容：off(event: 'dataChange', type: SubscribeType, observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum AssetStatus  差异内容： enum AssetStatus | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_NORMAL  差异内容：ASSET\_NORMAL | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_INSERT  差异内容：ASSET\_INSERT | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_UPDATE  差异内容：ASSET\_UPDATE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_DELETE  差异内容：ASSET\_DELETE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_ABNORMAL  差异内容：ASSET\_ABNORMAL | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_DOWNLOADING  差异内容：ASSET\_DOWNLOADING | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface Asset  差异内容： interface Asset | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：name: string;  差异内容：name: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：path: string;  差异内容：path: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：createTime: string;  差异内容：createTime: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：modifyTime: string;  差异内容：modifyTime: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：size: string;  差异内容：size: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Asset；  API声明：status?: AssetStatus;  差异内容：status?: AssetStatus; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：type Assets = Asset[];  差异内容：type Assets = Asset[]; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：type PRIKeyType = number | string;  差异内容：type PRIKeyType = number | string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：type UTCTime = Date;  差异内容：type UTCTime = Date; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：type ModifyTime = Map<PRIKeyType, UTCTime>;  差异内容：type ModifyTime = Map<PRIKeyType, UTCTime>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig；  API声明：dataGroupId?: string;  差异内容：dataGroupId?: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig；  API声明：customDir?: string;  差异内容：customDir?: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig；  API声明：autoCleanDirtyData?: boolean;  差异内容：autoCleanDirtyData?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig；  API声明：allowRebuild?: boolean;  差异内容：allowRebuild?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum Progress  差异内容： enum Progress | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Progress；  API声明：SYNC\_BEGIN  差异内容：SYNC\_BEGIN | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Progress；  API声明：SYNC\_IN\_PROGRESS  差异内容：SYNC\_IN\_PROGRESS | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Progress；  API声明：SYNC\_FINISH  差异内容：SYNC\_FINISH | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface Statistic  差异内容： interface Statistic | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Statistic；  API声明：total: number;  差异内容：total: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Statistic；  API声明：successful: number;  差异内容：successful: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Statistic；  API声明：failed: number;  差异内容：failed: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Statistic；  API声明：remained: number;  差异内容：remained: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface TableDetails  差异内容： interface TableDetails | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：TableDetails；  API声明：upload: Statistic;  差异内容：upload: Statistic; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：TableDetails；  API声明：download: Statistic;  差异内容：download: Statistic; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum ProgressCode  差异内容： enum ProgressCode | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：SUCCESS  差异内容：SUCCESS | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：UNKNOWN\_ERROR  差异内容：UNKNOWN\_ERROR | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：NETWORK\_ERROR  差异内容：NETWORK\_ERROR | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：CLOUD\_DISABLED  差异内容：CLOUD\_DISABLED | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：LOCKED\_BY\_OTHERS  差异内容：LOCKED\_BY\_OTHERS | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：RECORD\_LIMIT\_EXCEEDED  差异内容：RECORD\_LIMIT\_EXCEEDED | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：NO\_SPACE\_FOR\_ASSET  差异内容：NO\_SPACE\_FOR\_ASSET | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode；  API声明：BLOCKED\_BY\_NETWORK\_STRATEGY  差异内容：BLOCKED\_BY\_NETWORK\_STRATEGY | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface ProgressDetails  差异内容： interface ProgressDetails | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressDetails；  API声明：schedule: Progress;  差异内容：schedule: Progress; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressDetails；  API声明：code: ProgressCode;  差异内容：code: ProgressCode; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressDetails；  API声明：details: Record<string, TableDetails>;  差异内容：details: Record<string, TableDetails>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncMode；  API声明：SYNC\_MODE\_TIME\_FIRST  差异内容：SYNC\_MODE\_TIME\_FIRST | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncMode；  API声明：SYNC\_MODE\_NATIVE\_FIRST  差异内容：SYNC\_MODE\_NATIVE\_FIRST | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncMode；  API声明：SYNC\_MODE\_CLOUD\_FIRST  差异内容：SYNC\_MODE\_CLOUD\_FIRST | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD  差异内容：SUBSCRIBE\_TYPE\_CLOUD | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD\_DETAILS  差异内容：SUBSCRIBE\_TYPE\_CLOUD\_DETAILS | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_LOCAL\_DETAILS  差异内容：SUBSCRIBE\_TYPE\_LOCAL\_DETAILS | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum ChangeType  差异内容： enum ChangeType | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeType；  API声明：DATA\_CHANGE  差异内容：DATA\_CHANGE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeType；  API声明：ASSET\_CHANGE  差异内容：ASSET\_CHANGE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface ChangeInfo  差异内容： interface ChangeInfo | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeInfo；  API声明：table: string;  差异内容：table: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeInfo；  API声明：type: ChangeType;  差异内容：type: ChangeType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeInfo；  API声明：inserted: Array<string> | Array<number>;  差异内容：inserted: Array<string> | Array<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeInfo；  API声明：updated: Array<string> | Array<number>;  差异内容：updated: Array<string> | Array<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ChangeInfo；  API声明：deleted: Array<string> | Array<number>;  差异内容：deleted: Array<string> | Array<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum DistributedType  差异内容： enum DistributedType | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedType；  API声明：DISTRIBUTED\_DEVICE  差异内容：DISTRIBUTED\_DEVICE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedType；  API声明：DISTRIBUTED\_CLOUD  差异内容：DISTRIBUTED\_CLOUD | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface DistributedConfig  差异内容： interface DistributedConfig | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig；  API声明：autoSync: boolean;  差异内容：autoSync: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum ConflictResolution  差异内容： enum ConflictResolution | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ConflictResolution；  API声明：ON\_CONFLICT\_NONE = 0  差异内容：ON\_CONFLICT\_NONE = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ConflictResolution；  API声明：ON\_CONFLICT\_ROLLBACK = 1  差异内容：ON\_CONFLICT\_ROLLBACK = 1 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ConflictResolution；  API声明：ON\_CONFLICT\_ABORT = 2  差异内容：ON\_CONFLICT\_ABORT = 2 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ConflictResolution；  API声明：ON\_CONFLICT\_FAIL = 3  差异内容：ON\_CONFLICT\_FAIL = 3 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ConflictResolution；  API声明：ON\_CONFLICT\_IGNORE = 4  差异内容：ON\_CONFLICT\_IGNORE = 4 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ConflictResolution；  API声明：ON\_CONFLICT\_REPLACE = 5  差异内容：ON\_CONFLICT\_REPLACE = 5 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum Origin  差异内容： enum Origin | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Origin；  API声明：LOCAL  差异内容：LOCAL | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Origin；  API声明：CLOUD  差异内容：CLOUD | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Origin；  API声明：REMOTE  差异内容：REMOTE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum Field  差异内容： enum Field | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Field；  API声明：CURSOR\_FIELD = '#\_cursor'  差异内容：CURSOR\_FIELD = '#\_cursor' | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Field；  API声明：ORIGIN\_FIELD = '#\_origin'  差异内容：ORIGIN\_FIELD = '#\_origin' | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Field；  API声明：DELETED\_FLAG\_FIELD = '#\_deleted\_flag'  差异内容：DELETED\_FLAG\_FIELD = '#\_deleted\_flag' | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Field；  API声明：OWNER\_FIELD = '#\_cloud\_owner'  差异内容：OWNER\_FIELD = '#\_cloud\_owner' | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Field；  API声明：PRIVILEGE\_FIELD = '#\_cloud\_privilege'  差异内容：PRIVILEGE\_FIELD = '#\_cloud\_privilege' | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Field；  API声明：SHARING\_RESOURCE\_FIELD = '#\_sharing\_resource\_field'  差异内容：SHARING\_RESOURCE\_FIELD = '#\_sharing\_resource\_field' | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum RebuildType  差异内容： enum RebuildType | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RebuildType；  API声明：NONE  差异内容：NONE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RebuildType；  API声明：REBUILT  差异内容：REBUILT | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbPredicates；  API声明：notContains(field: string, value: string): RdbPredicates;  差异内容：notContains(field: string, value: string): RdbPredicates; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbPredicates；  API声明：notLike(field: string, value: string): RdbPredicates;  差异内容：notLike(field: string, value: string): RdbPredicates; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getAsset(columnIndex: number): Asset;  差异内容：getAsset(columnIndex: number): Asset; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getAssets(columnIndex: number): Assets;  差异内容：getAssets(columnIndex: number): Assets; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getValue(columnIndex: number): ValueType;  差异内容：getValue(columnIndex: number): ValueType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getRow(): ValuesBucket;  差异内容：getRow(): ValuesBucket; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：version: number;  差异内容：version: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：rebuilt: RebuildType;  差异内容：rebuilt: RebuildType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): number;  差异内容：insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：batchInsertSync(table: string, values: Array<ValuesBucket>): number;  差异内容：batchInsertSync(table: string, values: Array<ValuesBucket>): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number;  差异内容：updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：deleteSync(predicates: RdbPredicates): number;  差异内容：deleteSync(predicates: RdbPredicates): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet;  差异内容：querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet;  差异内容：querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>;  差异内容：getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[], callback: AsyncCallback<ModifyTime>): void;  差异内容：getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[], callback: AsyncCallback<ModifyTime>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void;  差异内容：cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cleanDirtyData(table: string, callback: AsyncCallback<void>): void;  差异内容：cleanDirtyData(table: string, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cleanDirtyData(table: string, cursor?: number): Promise<void>;  差异内容：cleanDirtyData(table: string, cursor?: number): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：execute(sql: string, args?: Array<ValueType>): Promise<ValueType>;  差异内容：execute(sql: string, args?: Array<ValueType>): Promise<ValueType>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>;  差异内容：execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：executeSync(sql: string, args?: Array<ValueType>): ValueType;  差异内容：executeSync(sql: string, args?: Array<ValueType>): ValueType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：beginTrans(): Promise<number>;  差异内容：beginTrans(): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：rollback(txId: number): Promise<void>;  差异内容：rollback(txId: number): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>;  差异内容：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;  差异内容：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>;  差异内容：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：on(event: string, interProcess: boolean, observer: Callback<void>): void;  差异内容：on(event: string, interProcess: boolean, observer: Callback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void;  差异内容：on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：off(event: string, interProcess: boolean, observer?: Callback<void>): void;  差异内容：off(event: string, interProcess: boolean, observer?: Callback<void>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void;  差异内容：off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：emit(event: string): void;  差异内容：emit(event: string): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：close(): Promise<void>;  差异内容：close(): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：attach(fullPath: string, attachName: string, waitTime?: number): Promise<number>;  差异内容：attach(fullPath: string, attachName: string, waitTime?: number): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number): Promise<number>;  差异内容：attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：detach(attachName: string, waitTime?: number): Promise<number>;  差异内容：detach(attachName: string, waitTime?: number): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：lockRow(predicates: RdbPredicates): Promise<void>;  差异内容：lockRow(predicates: RdbPredicates): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：unlockRow(predicates: RdbPredicates): Promise<void>;  差异内容：unlockRow(predicates: RdbPredicates): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;  差异内容：queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace cloudData  差异内容： declare namespace cloudData | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData；  API声明： enum StrategyType  差异内容： enum StrategyType | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：StrategyType；  API声明：NETWORK  差异内容：NETWORK | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData；  API声明： enum NetWorkStrategy  差异内容： enum NetWorkStrategy | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：NetWorkStrategy；  API声明：WIFI = 1  差异内容：WIFI = 1 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：NetWorkStrategy；  API声明：CELLULAR = 2  差异内容：CELLULAR = 2 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData；  API声明：function setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>;  差异内容：function setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace cloudExtension  差异内容： declare namespace cloudExtension | api/@ohos.data.cloudExtension.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace commonType  差异内容： declare namespace commonType | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：commonType；  API声明： enum AssetStatus  差异内容： enum AssetStatus | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_NORMAL  差异内容：ASSET\_NORMAL | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_INSERT  差异内容：ASSET\_INSERT | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_UPDATE  差异内容：ASSET\_UPDATE | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_DELETE  差异内容：ASSET\_DELETE | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_ABNORMAL  差异内容：ASSET\_ABNORMAL | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：AssetStatus；  API声明：ASSET\_DOWNLOADING  差异内容：ASSET\_DOWNLOADING | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：commonType；  API声明： interface Asset  差异内容： interface Asset | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：name: string | undefined;  差异内容：name: string | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：uri: string | undefined;  差异内容：uri: string | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：path: string | undefined;  差异内容：path: string | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：createTime: string | undefined;  差异内容：createTime: string | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：modifyTime: string | undefined;  差异内容：modifyTime: string | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：size: string | undefined;  差异内容：size: string | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：Asset；  API声明：status?: AssetStatus | undefined;  差异内容：status?: AssetStatus | undefined; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：commonType；  API声明：type Assets = Array<Asset>;  差异内容：type Assets = Array<Asset>; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：commonType；  API声明：type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets;  差异内容：type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：commonType；  API声明：type ValuesBucket = Record<string, ValueType>;  差异内容：type ValuesBucket = Record<string, ValueType>; | api/@ohos.data.commonType.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace dataSharePredicates  差异内容： declare namespace dataSharePredicates | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：dataSharePredicates；  API声明： class DataSharePredicates  差异内容： class DataSharePredicates | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：equalTo(field: string, value: ValueType): DataSharePredicates;  差异内容：equalTo(field: string, value: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：and(): DataSharePredicates;  差异内容：and(): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：orderByAsc(field: string): DataSharePredicates;  差异内容：orderByAsc(field: string): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：orderByDesc(field: string): DataSharePredicates;  差异内容：orderByDesc(field: string): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：limit(total: number, offset: number): DataSharePredicates;  差异内容：limit(total: number, offset: number): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：in(field: string, value: Array<ValueType>): DataSharePredicates;  差异内容：in(field: string, value: Array<ValueType>): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace sendablePreferences  差异内容： declare namespace sendablePreferences | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：const MAX\_KEY\_LENGTH: number;  差异内容：const MAX\_KEY\_LENGTH: number; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：const MAX\_VALUE\_LENGTH: number;  差异内容：const MAX\_VALUE\_LENGTH: number; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明： interface Options  差异内容： interface Options | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Options；  API声明：name: string;  差异内容：name: string; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Options；  API声明：dataGroupId?: string | null;  差异内容：dataGroupId?: string | null; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：function getPreferences(context: Context, options: Options): Promise<Preferences>;  差异内容：function getPreferences(context: Context, options: Options): Promise<Preferences>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：function getPreferencesSync(context: Context, options: Options): Preferences;  差异内容：function getPreferencesSync(context: Context, options: Options): Preferences; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：function deletePreferences(context: Context, options: Options): Promise<void>;  差异内容：function deletePreferences(context: Context, options: Options): Promise<void>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：function removePreferencesFromCache(context: Context, options: Options): Promise<void>;  差异内容：function removePreferencesFromCache(context: Context, options: Options): Promise<void>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明：function removePreferencesFromCacheSync(context: Context, options: Options): void;  差异内容：function removePreferencesFromCacheSync(context: Context, options: Options): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：sendablePreferences；  API声明： interface Preferences  差异内容： interface Preferences | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：get(key: string, defValue: lang.ISendable): Promise<lang.ISendable>;  差异内容：get(key: string, defValue: lang.ISendable): Promise<lang.ISendable>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：getSync(key: string, defValue: lang.ISendable): lang.ISendable;  差异内容：getSync(key: string, defValue: lang.ISendable): lang.ISendable; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：getAll(): Promise<lang.ISendable>;  差异内容：getAll(): Promise<lang.ISendable>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：getAllSync(): lang.ISendable;  差异内容：getAllSync(): lang.ISendable; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：has(key: string): Promise<boolean>;  差异内容：has(key: string): Promise<boolean>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：hasSync(key: string): boolean;  差异内容：hasSync(key: string): boolean; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：put(key: string, value: lang.ISendable): Promise<void>;  差异内容：put(key: string, value: lang.ISendable): Promise<void>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：putSync(key: string, value: lang.ISendable): void;  差异内容：putSync(key: string, value: lang.ISendable): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：delete(key: string): Promise<void>;  差异内容：delete(key: string): Promise<void>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：deleteSync(key: string): void;  差异内容：deleteSync(key: string): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：clear(): Promise<void>;  差异内容：clear(): Promise<void>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：clearSync(): void;  差异内容：clearSync(): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：flush(): Promise<void>;  差异内容：flush(): Promise<void>; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：on(type: 'change', callback: Callback<string>): void;  差异内容：on(type: 'change', callback: Callback<string>): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：on(type: 'multiProcessChange', callback: Callback<string>): void;  差异内容：on(type: 'multiProcessChange', callback: Callback<string>): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：on(type: 'dataChange', keys: Array<string>, callback: Callback<lang.ISendable>): void;  差异内容：on(type: 'dataChange', keys: Array<string>, callback: Callback<lang.ISendable>): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：off(type: 'change', callback?: Callback<string>): void;  差异内容：off(type: 'change', callback?: Callback<string>): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：off(type: 'multiProcessChange', callback?: Callback<string>): void;  差异内容：off(type: 'multiProcessChange', callback?: Callback<string>): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：Preferences；  API声明：off(type: 'dataChange', keys: Array<string>, callback?: Callback<lang.ISendable>): void;  差异内容：off(type: 'dataChange', keys: Array<string>, callback?: Callback<lang.ISendable>): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：global；  API声明： declare namespace unifiedDataChannel  差异内容： declare namespace unifiedDataChannel | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： enum ShareOptions  差异内容： enum ShareOptions | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ShareOptions；  API声明：IN\_APP  差异内容：IN\_APP | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ShareOptions；  API声明：CROSS\_APP  差异内容：CROSS\_APP | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：type GetDelayData = (type: string) => UnifiedData;  差异内容：type GetDelayData = (type: string) => UnifiedData; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：type ValueType = number | string | image.PixelMap | Want | ArrayBuffer;  差异内容：type ValueType = number | string | image.PixelMap | Want | ArrayBuffer; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class UnifiedDataProperties  差异内容： class UnifiedDataProperties | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties；  API声明：extras?: Record<string, object>;  差异内容：extras?: Record<string, object>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties；  API声明：tag?: string;  差异内容：tag?: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties；  API声明：readonly timestamp?: Date;  差异内容：readonly timestamp?: Date; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties；  API声明：shareOptions?: ShareOptions;  差异内容：shareOptions?: ShareOptions; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties；  API声明：getDelayData?: GetDelayData;  差异内容：getDelayData?: GetDelayData; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class UnifiedData  差异内容： class UnifiedData | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedData；  API声明：addRecord(record: UnifiedRecord): void;  差异内容：addRecord(record: UnifiedRecord): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedData；  API声明：getRecords(): Array<UnifiedRecord>;  差异内容：getRecords(): Array<UnifiedRecord>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedData；  API声明：hasType(type: string): boolean;  差异内容：hasType(type: string): boolean; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedData；  API声明：getTypes(): Array<string>;  差异内容：getTypes(): Array<string>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedData；  API声明：properties: UnifiedDataProperties;  差异内容：properties: UnifiedDataProperties; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Summary  差异内容： class Summary | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Summary；  API声明：summary: Record<string, number>;  差异内容：summary: Record<string, number>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Summary；  API声明：totalSize: number;  差异内容：totalSize: number; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class UnifiedRecord  差异内容： class UnifiedRecord | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedRecord；  API声明：getType(): string;  差异内容：getType(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedRecord；  API声明：getValue(): ValueType;  差异内容：getValue(): ValueType; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Text  差异内容： class Text | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Text；  API声明：details?: Record<string, string>;  差异内容：details?: Record<string, string>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class PlainText  差异内容： class PlainText | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：textContent: string;  差异内容：textContent: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：abstract?: string;  差异内容：abstract?: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Hyperlink  差异内容： class Hyperlink | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：url: string;  差异内容：url: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class HTML  差异内容： class HTML | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：HTML；  API声明：htmlContent: string;  差异内容：htmlContent: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：HTML；  API声明：plainContent?: string;  差异内容：plainContent?: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class File  差异内容： class File | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：File；  API声明：details?: Record<string, string>;  差异内容：details?: Record<string, string>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：File；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Image  差异内容： class Image | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Image；  API声明：imageUri: string;  差异内容：imageUri: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Video  差异内容： class Video | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Video；  API声明：videoUri: string;  差异内容：videoUri: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Audio  差异内容： class Audio | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Audio；  API声明：audioUri: string;  差异内容：audioUri: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class Folder  差异内容： class Folder | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Folder；  API声明：folderUri: string;  差异内容：folderUri: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class SystemDefinedRecord  差异内容： class SystemDefinedRecord | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedRecord；  API声明：details?: Record<string, number | string | Uint8Array>;  差异内容：details?: Record<string, number | string | Uint8Array>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class SystemDefinedForm  差异内容： class SystemDefinedForm | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：formId: number;  差异内容：formId: number; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：formName: string;  差异内容：formName: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：module: string;  差异内容：module: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class SystemDefinedAppItem  差异内容： class SystemDefinedAppItem | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：appId: string;  差异内容：appId: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：appName: string;  差异内容：appName: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：appIconId: string;  差异内容：appIconId: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：appLabelId: string;  差异内容：appLabelId: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class SystemDefinedPixelMap  差异内容： class SystemDefinedPixelMap | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedPixelMap；  API声明：rawData: Uint8Array;  差异内容：rawData: Uint8Array; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： class ApplicationDefinedRecord  差异内容： class ApplicationDefinedRecord | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ApplicationDefinedRecord；  API声明：applicationDefinedType: string;  差异内容：applicationDefinedType: string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ApplicationDefinedRecord；  API声明：rawData: Uint8Array;  差异内容：rawData: Uint8Array; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明： enum Intention  差异内容： enum Intention | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Intention；  API声明：DATA\_HUB = 'DataHub'  差异内容：DATA\_HUB = 'DataHub' | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：type Options = {  /\*\*  \* Indicates the target Intention  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @since 10  \*/  /\*\*  \* Indicates the target Intention  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @atomicservice  \* @since 11  \*/  intention?: Intention;  /\*\*  \* Indicates the unique identifier of target UnifiedData  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @since 10  \*/  /\*\*  \* Indicates the unique identifier of target UnifiedData  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @atomicservice  \* @since 11  \*/  key?: string;  };  差异内容：type Options = {  /\*\*  \* Indicates the target Intention  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @since 10  \*/  /\*\*  \* Indicates the target Intention  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @atomicservice  \* @since 11  \*/  intention?: Intention;  /\*\*  \* Indicates the unique identifier of target UnifiedData  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @since 10  \*/  /\*\*  \* Indicates the unique identifier of target UnifiedData  \*  \* @syscap SystemCapability.DistributedDataManager.UDMF.Core  \* @atomicservice  \* @since 11  \*/  key?: string;  }; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void;  差异内容：function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function insertData(options: Options, data: UnifiedData): Promise<string>;  差异内容：function insertData(options: Options, data: UnifiedData): Promise<string>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void;  差异内容：function updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function updateData(options: Options, data: UnifiedData): Promise<void>;  差异内容：function updateData(options: Options, data: UnifiedData): Promise<void>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void;  差异内容：function queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function queryData(options: Options): Promise<Array<UnifiedData>>;  差异内容：function queryData(options: Options): Promise<Array<UnifiedData>>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void;  差异内容：function deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function deleteData(options: Options): Promise<Array<UnifiedData>>;  差异内容：function deleteData(options: Options): Promise<Array<UnifiedData>>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace uniformDataStruct  差异内容： declare namespace uniformDataStruct | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface PlainText  差异内容： interface PlainText | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：uniformDataType: 'general.plain-text';  差异内容：uniformDataType: 'general.plain-text'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：textContent: string;  差异内容：textContent: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：abstract?: string;  差异内容：abstract?: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：details?: Record<string, string>;  差异内容：details?: Record<string, string>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface Hyperlink  差异内容： interface Hyperlink | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：uniformDataType: 'general.hyperlink';  差异内容：uniformDataType: 'general.hyperlink'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：url: string;  差异内容：url: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：details?: Record<string, string>;  差异内容：details?: Record<string, string>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface HTML  差异内容： interface HTML | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：HTML；  API声明：uniformDataType: 'general.html';  差异内容：uniformDataType: 'general.html'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：HTML；  API声明：htmlContent: string;  差异内容：htmlContent: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：HTML；  API声明：plainContent?: string;  差异内容：plainContent?: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：HTML；  API声明：details?: Record<string, string>;  差异内容：details?: Record<string, string>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface OpenHarmonyAppItem  差异内容： interface OpenHarmonyAppItem | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：uniformDataType: 'openharmony.app-item';  差异内容：uniformDataType: 'openharmony.app-item'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：appId: string;  差异内容：appId: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：appName: string;  差异内容：appName: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：appIconId: string;  差异内容：appIconId: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：appLabelId: string;  差异内容：appLabelId: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：OpenHarmonyAppItem；  API声明：details?: Record<string, number | string | Uint8Array>;  差异内容：details?: Record<string, number | string | Uint8Array>; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace uniformTypeDescriptor  差异内容： declare namespace uniformTypeDescriptor | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：uniformTypeDescriptor；  API声明： enum UniformDataType  差异内容： enum UniformDataType | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ENTITY = 'general.entity'  差异内容：ENTITY = 'general.entity' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OBJECT = 'general.object'  差异内容：OBJECT = 'general.object' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：COMPOSITE\_OBJECT = 'general.composite-object'  差异内容：COMPOSITE\_OBJECT = 'general.composite-object' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TEXT = 'general.text'  差异内容：TEXT = 'general.text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PLAIN\_TEXT = 'general.plain-text'  差异内容：PLAIN\_TEXT = 'general.plain-text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：HTML = 'general.html'  差异内容：HTML = 'general.html' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：HYPERLINK = 'general.hyperlink'  差异内容：HYPERLINK = 'general.hyperlink' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：XML = 'general.xml'  差异内容：XML = 'general.xml' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SMIL = 'com.real.smil'  差异内容：SMIL = 'com.real.smil' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SOURCE\_CODE = 'general.source-code'  差异内容：SOURCE\_CODE = 'general.source-code' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SCRIPT = 'general.script'  差异内容：SCRIPT = 'general.script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SHELL\_SCRIPT = 'general.shell-script'  差异内容：SHELL\_SCRIPT = 'general.shell-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：CSH\_SCRIPT = 'general.csh-script'  差异内容：CSH\_SCRIPT = 'general.csh-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PERL\_SCRIPT = 'general.perl-script'  差异内容：PERL\_SCRIPT = 'general.perl-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PHP\_SCRIPT = 'general.php-script'  差异内容：PHP\_SCRIPT = 'general.php-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PYTHON\_SCRIPT = 'general.python-script'  差异内容：PYTHON\_SCRIPT = 'general.python-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：RUBY\_SCRIPT = 'general.ruby-script'  差异内容：RUBY\_SCRIPT = 'general.ruby-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TYPE\_SCRIPT = 'general.type-script'  差异内容：TYPE\_SCRIPT = 'general.type-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：JAVA\_SCRIPT = 'general.java-script'  差异内容：JAVA\_SCRIPT = 'general.java-script' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：C\_HEADER = 'general.c-header'  差异内容：C\_HEADER = 'general.c-header' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：C\_SOURCE = 'general.c-source'  差异内容：C\_SOURCE = 'general.c-source' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：C\_PLUS\_PLUS\_HEADER = 'general.c-plus-plus-header'  差异内容：C\_PLUS\_PLUS\_HEADER = 'general.c-plus-plus-header' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：C\_PLUS\_PLUS\_SOURCE = 'general.c-plus-plus-source'  差异内容：C\_PLUS\_PLUS\_SOURCE = 'general.c-plus-plus-source' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：JAVA\_SOURCE = 'general.java-source'  差异内容：JAVA\_SOURCE = 'general.java-source' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MARKDOWN = 'general.markdown'  差异内容：MARKDOWN = 'general.markdown' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：EBOOK = 'general.ebook'  差异内容：EBOOK = 'general.ebook' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：EPUB = 'general.epub'  差异内容：EPUB = 'general.epub' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AZW = 'com.amazon.azw'  差异内容：AZW = 'com.amazon.azw' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AZW3 = 'com.amazon.azw3'  差异内容：AZW3 = 'com.amazon.azw3' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：KFX = 'com.amazon.kfx'  差异内容：KFX = 'com.amazon.kfx' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MOBI = 'com.amazon.mobi'  差异内容：MOBI = 'com.amazon.mobi' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MEDIA = 'general.media'  差异内容：MEDIA = 'general.media' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：IMAGE = 'general.image'  差异内容：IMAGE = 'general.image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：JPEG = 'general.jpeg'  差异内容：JPEG = 'general.jpeg' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PNG = 'general.png'  差异内容：PNG = 'general.png' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：RAW\_IMAGE = 'general.raw-image'  差异内容：RAW\_IMAGE = 'general.raw-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TIFF = 'general.tiff'  差异内容：TIFF = 'general.tiff' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：BMP = 'com.microsoft.bmp'  差异内容：BMP = 'com.microsoft.bmp' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ICO = 'com.microsoft.ico'  差异内容：ICO = 'com.microsoft.ico' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PHOTOSHOP\_IMAGE = 'com.adobe.photoshop-image'  差异内容：PHOTOSHOP\_IMAGE = 'com.adobe.photoshop-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AI\_IMAGE = 'com.adobe.illustrator.ai-image'  差异内容：AI\_IMAGE = 'com.adobe.illustrator.ai-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FAX = 'general.fax'  差异内容：FAX = 'general.fax' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：JFX\_FAX = 'com.j2.jfx-fax'  差异内容：JFX\_FAX = 'com.j2.jfx-fax' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：EFX\_FAX = 'com.js.efx-fax'  差异内容：EFX\_FAX = 'com.js.efx-fax' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：XBITMAP\_IMAGE = 'general.xbitmap-image'  差异内容：XBITMAP\_IMAGE = 'general.xbitmap-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TGA\_IMAGE = 'com.truevision.tga-image'  差异内容：TGA\_IMAGE = 'com.truevision.tga-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SGI\_IMAGE = 'com.sgi.sgi-image'  差异内容：SGI\_IMAGE = 'com.sgi.sgi-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENEXR\_IMAGE = 'com.ilm.openexr-image'  差异内容：OPENEXR\_IMAGE = 'com.ilm.openexr-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FLASHPIX\_IMAGE = 'com.kodak.flashpix.image'  差异内容：FLASHPIX\_IMAGE = 'com.kodak.flashpix.image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WORD\_DOC = 'com.microsoft.word.doc'  差异内容：WORD\_DOC = 'com.microsoft.word.doc' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：EXCEL = 'com.microsoft.excel.xls'  差异内容：EXCEL = 'com.microsoft.excel.xls' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PPT = 'com.microsoft.powerpoint.ppt'  差异内容：PPT = 'com.microsoft.powerpoint.ppt' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PDF = 'com.adobe.pdf'  差异内容：PDF = 'com.adobe.pdf' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：POSTSCRIPT = 'com.adobe.postscript'  差异内容：POSTSCRIPT = 'com.adobe.postscript' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ENCAPSULATED\_POSTSCRIPT = 'com.adobe.encapsulated-postscript'  差异内容：ENCAPSULATED\_POSTSCRIPT = 'com.adobe.encapsulated-postscript' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：VIDEO = 'general.video'  差异内容：VIDEO = 'general.video' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AVI = 'general.avi'  差异内容：AVI = 'general.avi' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MPEG = 'general.mpeg'  差异内容：MPEG = 'general.mpeg' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MPEG4 = 'general.mpeg-4'  差异内容：MPEG4 = 'general.mpeg-4' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：VIDEO\_3GPP = 'general.3gpp'  差异内容：VIDEO\_3GPP = 'general.3gpp' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：VIDEO\_3GPP2 = 'general.3gpp2'  差异内容：VIDEO\_3GPP2 = 'general.3gpp2' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WM = 'com.microsoft.windows-media-wm'  差异内容：WINDOWS\_MEDIA\_WM = 'com.microsoft.windows-media-wm' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WMV = 'com.microsoft.windows-media-wmv'  差异内容：WINDOWS\_MEDIA\_WMV = 'com.microsoft.windows-media-wmv' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WMP = 'com.microsoft.windows-media-wmp'  差异内容：WINDOWS\_MEDIA\_WMP = 'com.microsoft.windows-media-wmp' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WVX = 'com.microsoft.windows-media-wvx'  差异内容：WINDOWS\_MEDIA\_WVX = 'com.microsoft.windows-media-wvx' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WMX = 'com.microsoft.windows-media-wmx'  差异内容：WINDOWS\_MEDIA\_WMX = 'com.microsoft.windows-media-wmx' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：REALMEDIA = 'com.real.realmedia'  差异内容：REALMEDIA = 'com.real.realmedia' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AUDIO = 'general.audio'  差异内容：AUDIO = 'general.audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AAC = 'general.aac'  差异内容：AAC = 'general.aac' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AIFF = 'general.aiff'  差异内容：AIFF = 'general.aiff' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ALAC = 'general.alac'  差异内容：ALAC = 'general.alac' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FLAC = 'general.flac'  差异内容：FLAC = 'general.flac' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MP3 = 'general.mp3'  差异内容：MP3 = 'general.mp3' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OGG = 'general.ogg'  差异内容：OGG = 'general.ogg' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PCM = 'general.pcm'  差异内容：PCM = 'general.pcm' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WMA = 'com.microsoft.windows-media-wma'  差异内容：WINDOWS\_MEDIA\_WMA = 'com.microsoft.windows-media-wma' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WAVEFORM\_AUDIO = 'com.microsoft.waveform-audio'  差异内容：WAVEFORM\_AUDIO = 'com.microsoft.waveform-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WINDOWS\_MEDIA\_WAX = 'com.microsoft.windows-media-wax'  差异内容：WINDOWS\_MEDIA\_WAX = 'com.microsoft.windows-media-wax' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AU\_AUDIO = 'general.au-audio'  差异内容：AU\_AUDIO = 'general.au-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：AIFC\_AUDIO = 'general.aifc-audio'  差异内容：AIFC\_AUDIO = 'general.aifc-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SD2\_AUDIO = 'com.digidesign.sd2-audio'  差异内容：SD2\_AUDIO = 'com.digidesign.sd2-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：REALAUDIO = 'com.real.realaudio'  差异内容：REALAUDIO = 'com.real.realaudio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FILE = 'general.file'  差异内容：FILE = 'general.file' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：DIRECTORY = 'general.directory'  差异内容：DIRECTORY = 'general.directory' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FOLDER = 'general.folder'  差异内容：FOLDER = 'general.folder' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SYMLINK = 'general.symlink'  差异内容：SYMLINK = 'general.symlink' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ARCHIVE = 'general.archive'  差异内容：ARCHIVE = 'general.archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：BZ2\_ARCHIVE = 'general.bz2-archive'  差异内容：BZ2\_ARCHIVE = 'general.bz2-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：DISK\_IMAGE = 'general.disk-image'  差异内容：DISK\_IMAGE = 'general.disk-image' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TAR\_ARCHIVE = 'general.tar-archive'  差异内容：TAR\_ARCHIVE = 'general.tar-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ZIP\_ARCHIVE = 'general.zip-archive'  差异内容：ZIP\_ARCHIVE = 'general.zip-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：JAVA\_ARCHIVE = 'com.sun.java-archive'  差异内容：JAVA\_ARCHIVE = 'com.sun.java-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：GNU\_TAR\_ARCHIVE = 'org.gnu.gnu-tar-archive'  差异内容：GNU\_TAR\_ARCHIVE = 'org.gnu.gnu-tar-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：GNU\_ZIP\_ARCHIVE = 'org.gnu.gnu-zip-archive'  差异内容：GNU\_ZIP\_ARCHIVE = 'org.gnu.gnu-zip-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：GNU\_ZIP\_TAR\_ARCHIVE = 'org.gnu.gnu-zip-tar-archive'  差异内容：GNU\_ZIP\_TAR\_ARCHIVE = 'org.gnu.gnu-zip-tar-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENXML = 'org.openxmlformats.openxml'  差异内容：OPENXML = 'org.openxmlformats.openxml' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：WORDPROCESSINGML\_DOCUMENT = 'org.openxmlformats.wordprocessingml.document'  差异内容：WORDPROCESSINGML\_DOCUMENT = 'org.openxmlformats.wordprocessingml.document' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SPREADSHEETML\_SHEET = 'org.openxmlformats.spreadsheetml.sheet'  差异内容：SPREADSHEETML\_SHEET = 'org.openxmlformats.spreadsheetml.sheet' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PRESENTATIONML\_PRESENTATION = 'org.openxmlformats.presentationml.presentation'  差异内容：PRESENTATIONML\_PRESENTATION = 'org.openxmlformats.presentationml.presentation' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENDOCUMENT = 'org.oasis.opendocument'  差异内容：OPENDOCUMENT = 'org.oasis.opendocument' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENDOCUMENT\_TEXT = 'org.oasis.opendocument.text'  差异内容：OPENDOCUMENT\_TEXT = 'org.oasis.opendocument.text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENDOCUMENT\_SPREADSHEET = 'org.oasis.opendocument.spreadsheet'  差异内容：OPENDOCUMENT\_SPREADSHEET = 'org.oasis.opendocument.spreadsheet' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENDOCUMENT\_PRESENTATION = 'org.oasis.opendocument.presentation'  差异内容：OPENDOCUMENT\_PRESENTATION = 'org.oasis.opendocument.presentation' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENDOCUMENT\_GRAPHICS = 'org.oasis.opendocument.graphics'  差异内容：OPENDOCUMENT\_GRAPHICS = 'org.oasis.opendocument.graphics' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENDOCUMENT\_FORMULA = 'org.oasis.opendocument.formula'  差异内容：OPENDOCUMENT\_FORMULA = 'org.oasis.opendocument.formula' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：STUFFIT\_ARCHIVE = 'com.allume.stuffit-archive'  差异内容：STUFFIT\_ARCHIVE = 'com.allume.stuffit-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：CALENDAR = 'general.calendar'  差异内容：CALENDAR = 'general.calendar' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：VCS = 'general.vcs'  差异内容：VCS = 'general.vcs' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：ICS = 'general.ics'  差异内容：ICS = 'general.ics' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：CONTACT = 'general.contact'  差异内容：CONTACT = 'general.contact' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：DATABASE = 'general.database'  差异内容：DATABASE = 'general.database' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：MESSAGE = 'general.message'  差异内容：MESSAGE = 'general.message' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：EXECUTABLE = 'general.executable'  差异内容：EXECUTABLE = 'general.executable' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：PORTABLE\_EXECUTABLE = 'com.microsoft.portable-executable'  差异内容：PORTABLE\_EXECUTABLE = 'com.microsoft.portable-executable' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：SUN\_JAVA\_CLASS = 'com.sun.java-class'  差异内容：SUN\_JAVA\_CLASS = 'com.sun.java-class' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：VCARD = 'general.vcard'  差异内容：VCARD = 'general.vcard' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：NAVIGATION = 'general.navigation'  差异内容：NAVIGATION = 'general.navigation' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：LOCATION = 'general.location'  差异内容：LOCATION = 'general.location' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：FONT = 'general.font'  差异内容：FONT = 'general.font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TRUETYPE\_FONT = 'general.truetype-font'  差异内容：TRUETYPE\_FONT = 'general.truetype-font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：TRUETYPE\_COLLECTION\_FONT = 'general.truetype-collection-font'  差异内容：TRUETYPE\_COLLECTION\_FONT = 'general.truetype-collection-font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENTYPE\_FONT = 'general.opentype-font'  差异内容：OPENTYPE\_FONT = 'general.opentype-font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：POSTSCRIPT\_FONT = 'com.adobe.postscript-font'  差异内容：POSTSCRIPT\_FONT = 'com.adobe.postscript-font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：POSTSCRIPT\_PFB\_FONT = 'com.adobe.postscript-pfb-font'  差异内容：POSTSCRIPT\_PFB\_FONT = 'com.adobe.postscript-pfb-font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：POSTSCRIPT\_PFA\_FONT = 'com.adobe.postscript-pfa-font'  差异内容：POSTSCRIPT\_PFA\_FONT = 'com.adobe.postscript-pfa-font' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_FORM = 'openharmony.form'  差异内容：OPENHARMONY\_FORM = 'openharmony.form' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_APP\_ITEM = 'openharmony.app-item'  差异内容：OPENHARMONY\_APP\_ITEM = 'openharmony.app-item' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_PIXEL\_MAP = 'openharmony.pixel-map'  差异内容：OPENHARMONY\_PIXEL\_MAP = 'openharmony.pixel-map' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_ATOMIC\_SERVICE = 'openharmony.atomic-service'  差异内容：OPENHARMONY\_ATOMIC\_SERVICE = 'openharmony.atomic-service' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_PACKAGE = 'openharmony.package'  差异内容：OPENHARMONY\_PACKAGE = 'openharmony.package' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_HAP = 'openharmony.hap'  差异内容：OPENHARMONY\_HAP = 'openharmony.hap' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_HDOC = 'openharmony.hdoc'  差异内容：OPENHARMONY\_HDOC = 'openharmony.hdoc' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_HINOTE = 'openharmony.hinote'  差异内容：OPENHARMONY\_HINOTE = 'openharmony.hinote' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_STYLED\_STRING = 'openharmony.styled-string'  差异内容：OPENHARMONY\_STYLED\_STRING = 'openharmony.styled-string' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType；  API声明：OPENHARMONY\_WANT = 'openharmony.want'  差异内容：OPENHARMONY\_WANT = 'openharmony.want' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：uniformTypeDescriptor；  API声明： class TypeDescriptor  差异内容： class TypeDescriptor | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly typeId: string;  差异内容：readonly typeId: string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly belongingToTypes: Array<string>;  差异内容：readonly belongingToTypes: Array<string>; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly description: string;  差异内容：readonly description: string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly referenceURL: string;  差异内容：readonly referenceURL: string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly iconFile: string;  差异内容：readonly iconFile: string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly filenameExtensions: Array<string>;  差异内容：readonly filenameExtensions: Array<string>; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：readonly mimeTypes: Array<string>;  差异内容：readonly mimeTypes: Array<string>; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：belongsTo(type: string): boolean;  差异内容：belongsTo(type: string): boolean; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：isLowerLevelType(type: string): boolean;  差异内容：isLowerLevelType(type: string): boolean; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：isHigherLevelType(type: string): boolean;  差异内容：isHigherLevelType(type: string): boolean; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：equals(typeDescriptor: TypeDescriptor): boolean;  差异内容：equals(typeDescriptor: TypeDescriptor): boolean; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：uniformTypeDescriptor；  API声明：function getTypeDescriptor(typeId: string): TypeDescriptor;  差异内容：function getTypeDescriptor(typeId: string): TypeDescriptor; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string;  差异内容：function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string;  差异内容：function getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明：export type ValueType = number | string | boolean;  差异内容：export type ValueType = number | string | boolean; | api/@ohos.data.ValuesBucket.d.ts |
| 新增API | NA | 类名：global；  API声明：export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;  差异内容：export type ValuesBucket = Record<string, ValueType | Uint8Array | null>; | api/@ohos.data.ValuesBucket.d.ts |
