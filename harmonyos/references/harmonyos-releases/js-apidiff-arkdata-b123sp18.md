---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b123sp18
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ffbfcb71e19183bbf16c0a682149a1313346b44e990867df78e68ca8552e00be
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void;  差异内容：14800000,14800010,14800011,14800017,14800021,14800022,14800023,14800027,14800028,14800029,14800030,14801001,14801002,401 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void;  差异内容：14800000,14800010,14800011,14800017,14800020,14800021,14800022,14800023,14800027,14800028,14800029,14800030,14801001,14801002,401 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>;  差异内容：14800000,14800010,14800011,14800017,14800021,14800027,14800028,14800029,14800030,14801001,14801002,401 | 类名：relationalStore；  API声明：function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>;  差异内容：14800000,14800010,14800011,14800017,14800020,14800021,14800022,14800023,14800027,14800028,14800029,14800030,14801001,14801002,401 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig；  API声明：cryptoParam?: CryptoParam;  差异内容：cryptoParam?: CryptoParam; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface CryptoParam  差异内容： interface CryptoParam | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CryptoParam；  API声明：encryptionKey: Uint8Array;  差异内容：encryptionKey: Uint8Array; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CryptoParam；  API声明：iterationCount?: number;  差异内容：iterationCount?: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CryptoParam；  API声明：encryptionAlgo?: EncryptionAlgo;  差异内容：encryptionAlgo?: EncryptionAlgo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CryptoParam；  API声明：hmacAlgo?: HmacAlgo;  差异内容：hmacAlgo?: HmacAlgo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CryptoParam；  API声明：kdfAlgo?: KdfAlgo;  差异内容：kdfAlgo?: KdfAlgo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CryptoParam；  API声明：cryptoPageSize?: number;  差异内容：cryptoPageSize?: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum EncryptionAlgo  差异内容： enum EncryptionAlgo | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：EncryptionAlgo；  API声明：AES\_256\_GCM = 0  差异内容：AES\_256\_GCM = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：EncryptionAlgo；  API声明：AES\_256\_CBC  差异内容：AES\_256\_CBC | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum HmacAlgo  差异内容： enum HmacAlgo | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：HmacAlgo；  API声明：SHA1 = 0  差异内容：SHA1 = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：HmacAlgo；  API声明：SHA256  差异内容：SHA256 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：HmacAlgo；  API声明：SHA512  差异内容：SHA512 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum KdfAlgo  差异内容： enum KdfAlgo | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：KdfAlgo；  API声明：KDF\_SHA1 = 0  差异内容：KDF\_SHA1 = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：KdfAlgo；  API声明：KDF\_SHA256  差异内容：KDF\_SHA256 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：KdfAlgo；  API声明：KDF\_SHA512  差异内容：KDF\_SHA512 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： enum TransactionType  差异内容： enum TransactionType | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：TransactionType；  API声明：DEFERRED  差异内容：DEFERRED | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：TransactionType；  API声明：IMMEDIATE  差异内容：IMMEDIATE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：TransactionType；  API声明：EXCLUSIVE  差异内容：EXCLUSIVE | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface TransactionOptions  差异内容： interface TransactionOptions | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：TransactionOptions；  API声明：transactionType?: TransactionType;  差异内容：transactionType?: TransactionType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：createTransaction(options?: TransactionOptions): Promise<Transaction>;  差异内容：createTransaction(options?: TransactionOptions): Promise<Transaction>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明： interface Transaction  差异内容： interface Transaction | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：commit(): Promise<void>;  差异内容：commit(): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：rollback(): Promise<void>;  差异内容：rollback(): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>;  差异内容：insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number;  差异内容：insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>;  差异内容：batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：batchInsertSync(table: string, values: Array<ValuesBucket>): number;  差异内容：batchInsertSync(table: string, values: Array<ValuesBucket>): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>;  差异内容：update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number;  差异内容：updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：delete(predicates: RdbPredicates): Promise<number>;  差异内容：delete(predicates: RdbPredicates): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：deleteSync(predicates: RdbPredicates): number;  差异内容：deleteSync(predicates: RdbPredicates): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;  差异内容：query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet;  差异内容：querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>;  差异内容：querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：querySqlSync(sql: string, args?: Array<ValueType>): ResultSet;  差异内容：querySqlSync(sql: string, args?: Array<ValueType>): ResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：execute(sql: string, args?: Array<ValueType>): Promise<ValueType>;  差异内容：execute(sql: string, args?: Array<ValueType>): Promise<ValueType>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：executeSync(sql: string, args?: Array<ValueType>): ValueType;  差异内容：executeSync(sql: string, args?: Array<ValueType>): ValueType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Intention；  API声明：DRAG = 'Drag'  差异内容：DRAG = 'Drag' | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void;  差异内容：function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：unifiedDataChannel；  API声明：function removeAppShareOptions(intention: Intention): void;  差异内容：function removeAppShareOptions(intention: Intention): void; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：flushSync(): void;  差异内容：flushSync(): void; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Preferences；  API声明：flushSync(): void;  差异内容：flushSync(): void; | api/@ohos.data.sendablePreferences.d.ets |
| 新增API | NA | 类名：uniformDataStruct；  API声明： interface ContentForm  差异内容： interface ContentForm | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：readonly uniformDataType: 'general.content-form';  差异内容：readonly uniformDataType: 'general.content-form'; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：thumbData?: Uint8Array;  差异内容：thumbData?: Uint8Array; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：title: string;  差异内容：title: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：appIcon?: Uint8Array;  差异内容：appIcon?: Uint8Array; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：appName?: string;  差异内容：appName?: string; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：ContentForm；  API声明：linkUri?: string;  差异内容：linkUri?: string; | api/@ohos.data.uniformDataStruct.d.ts |
