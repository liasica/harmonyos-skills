---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-6003
title: ArkData
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:12+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d76bdbfb8eb87d0e777c0f1187aa047ad1a676c395afe44a47c323bd0f4a5a4b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API跨平台权限变更 | 类名：Preferences；  API声明：on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void;  差异内容：NA | 类名：Preferences；  API声明：on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void;  差异内容：crossplatform | api/@ohos.data.preferences.d.ts |
| API跨平台权限变更 | 类名：Preferences；  API声明：off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void;  差异内容：NA | 类名：Preferences；  API声明：off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void;  差异内容：crossplatform | api/@ohos.data.preferences.d.ts |
| API跨平台权限变更 | 类名：StoreConfig；  API声明：isReadOnly?: boolean;  差异内容：NA | 类名：StoreConfig；  API声明：isReadOnly?: boolean;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：StoreConfig；  API声明：cryptoParam?: CryptoParam;  差异内容：NA | 类名：StoreConfig；  API声明：cryptoParam?: CryptoParam;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：StoreConfig；  API声明：persist?: boolean;  差异内容：NA | 类名：StoreConfig；  API声明：persist?: boolean;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：interface CryptoParam  差异内容：NA | 类名：relationalStore；  API声明：interface CryptoParam  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：CryptoParam；  API声明：encryptionKey: Uint8Array;  差异内容：NA | 类名：CryptoParam；  API声明：encryptionKey: Uint8Array;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：CryptoParam；  API声明：iterationCount?: number;  差异内容：NA | 类名：CryptoParam；  API声明：iterationCount?: number;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：CryptoParam；  API声明：encryptionAlgo?: EncryptionAlgo;  差异内容：NA | 类名：CryptoParam；  API声明：encryptionAlgo?: EncryptionAlgo;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：CryptoParam；  API声明：hmacAlgo?: HmacAlgo;  差异内容：NA | 类名：CryptoParam；  API声明：hmacAlgo?: HmacAlgo;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：CryptoParam；  API声明：kdfAlgo?: KdfAlgo;  差异内容：NA | 类名：CryptoParam；  API声明：kdfAlgo?: KdfAlgo;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：CryptoParam；  API声明：cryptoPageSize?: number;  差异内容：NA | 类名：CryptoParam；  API声明：cryptoPageSize?: number;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：enum EncryptionAlgo  差异内容：NA | 类名：relationalStore；  API声明：enum EncryptionAlgo  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：EncryptionAlgo；  API声明：AES\_256\_GCM = 0  差异内容：NA | 类名：EncryptionAlgo；  API声明：AES\_256\_GCM = 0  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：EncryptionAlgo；  API声明：AES\_256\_CBC  差异内容：NA | 类名：EncryptionAlgo；  API声明：AES\_256\_CBC  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：enum HmacAlgo  差异内容：NA | 类名：relationalStore；  API声明：enum HmacAlgo  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：HmacAlgo；  API声明：SHA1 = 0  差异内容：NA | 类名：HmacAlgo；  API声明：SHA1 = 0  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：HmacAlgo；  API声明：SHA256  差异内容：NA | 类名：HmacAlgo；  API声明：SHA256  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：HmacAlgo；  API声明：SHA512  差异内容：NA | 类名：HmacAlgo；  API声明：SHA512  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：enum KdfAlgo  差异内容：NA | 类名：relationalStore；  API声明：enum KdfAlgo  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：KdfAlgo；  API声明：KDF\_SHA1 = 0  差异内容：NA | 类名：KdfAlgo；  API声明：KDF\_SHA1 = 0  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：KdfAlgo；  API声明：KDF\_SHA256  差异内容：NA | 类名：KdfAlgo；  API声明：KDF\_SHA256  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：KdfAlgo；  API声明：KDF\_SHA512  差异内容：NA | 类名：KdfAlgo；  API声明：KDF\_SHA512  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：interface SqlExecutionInfo  差异内容：NA | 类名：relationalStore；  API声明：interface SqlExecutionInfo  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：SqlExecutionInfo；  API声明：sql: Array<string>;  差异内容：NA | 类名：SqlExecutionInfo；  API声明：sql: Array<string>;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：SqlExecutionInfo；  API声明：totalTime: number;  差异内容：NA | 类名：SqlExecutionInfo；  API声明：totalTime: number;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：SqlExecutionInfo；  API声明：waitTime: number;  差异内容：NA | 类名：SqlExecutionInfo；  API声明：waitTime: number;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：SqlExecutionInfo；  API声明：prepareTime: number;  差异内容：NA | 类名：SqlExecutionInfo；  API声明：prepareTime: number;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：SqlExecutionInfo；  API声明：executeTime: number;  差异内容：NA | 类名：SqlExecutionInfo；  API声明：executeTime: number;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：enum Field  差异内容：NA | 类名：relationalStore；  API声明：enum Field  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：CURSOR\_FIELD = '#\_cursor'  差异内容：NA | 类名：Field；  API声明：CURSOR\_FIELD = '#\_cursor'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：ORIGIN\_FIELD = '#\_origin'  差异内容：NA | 类名：Field；  API声明：ORIGIN\_FIELD = '#\_origin'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：DELETED\_FLAG\_FIELD = '#\_deleted\_flag'  差异内容：NA | 类名：Field；  API声明：DELETED\_FLAG\_FIELD = '#\_deleted\_flag'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：DATA\_STATUS\_FIELD = '#\_data\_status'  差异内容：NA | 类名：Field；  API声明：DATA\_STATUS\_FIELD = '#\_data\_status'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：OWNER\_FIELD = '#\_cloud\_owner'  差异内容：NA | 类名：Field；  API声明：OWNER\_FIELD = '#\_cloud\_owner'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：PRIVILEGE\_FIELD = '#\_cloud\_privilege'  差异内容：NA | 类名：Field；  API声明：PRIVILEGE\_FIELD = '#\_cloud\_privilege'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Field；  API声明：SHARING\_RESOURCE\_FIELD = '#\_sharing\_resource\_field'  差异内容：NA | 类名：Field；  API声明：SHARING\_RESOURCE\_FIELD = '#\_sharing\_resource\_field'  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：enum TransactionType  差异内容：NA | 类名：relationalStore；  API声明：enum TransactionType  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：TransactionType；  API声明：DEFERRED  差异内容：NA | 类名：TransactionType；  API声明：DEFERRED  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：TransactionType；  API声明：IMMEDIATE  差异内容：NA | 类名：TransactionType；  API声明：IMMEDIATE  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：TransactionType；  API声明：EXCLUSIVE  差异内容：NA | 类名：TransactionType；  API声明：EXCLUSIVE  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：relationalStore；  API声明：interface TransactionOptions  差异内容：NA | 类名：relationalStore；  API声明：interface TransactionOptions  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：TransactionOptions；  API声明：transactionType?: TransactionType;  差异内容：NA | 类名：TransactionOptions；  API声明：transactionType?: TransactionType;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：RdbPredicates；  API声明：notContains(field: string, value: string): RdbPredicates;  差异内容：NA | 类名：RdbPredicates；  API声明：notContains(field: string, value: string): RdbPredicates;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：RdbPredicates；  API声明：notLike(field: string, value: string): RdbPredicates;  差异内容：NA | 类名：RdbPredicates；  API声明：notLike(field: string, value: string): RdbPredicates;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：ResultSet；  API声明：getValue(columnIndex: number): ValueType;  差异内容：NA | 类名：ResultSet；  API声明：getValue(columnIndex: number): ValueType;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：RdbStore；  API声明：on(event: 'statistics', observer: Callback<SqlExecutionInfo>): void;  差异内容：NA | 类名：RdbStore；  API声明：on(event: 'statistics', observer: Callback<SqlExecutionInfo>): void;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：RdbStore；  API声明：off(event: 'statistics', observer?: Callback<SqlExecutionInfo>): void;  差异内容：NA | 类名：RdbStore；  API声明：off(event: 'statistics', observer?: Callback<SqlExecutionInfo>): void;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：RdbStore；  API声明：close(): Promise<void>;  差异内容：NA | 类名：RdbStore；  API声明：close(): Promise<void>;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：Transaction；  API声明：execute(sql: string, args?: Array<ValueType>): Promise<ValueType>;  差异内容：NA | 类名：Transaction；  API声明：execute(sql: string, args?: Array<ValueType>): Promise<ValueType>;  差异内容：crossplatform | api/@ohos.data.relationalStore.d.ts |
| API跨平台权限变更 | 类名：uniformTypeDescriptor；  API声明：class TypeDescriptor  差异内容：NA | 类名：uniformTypeDescriptor；  API声明：class TypeDescriptor  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly typeId: string;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly typeId: string;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly belongingToTypes: Array<string>;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly belongingToTypes: Array<string>;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly description: string;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly description: string;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly referenceURL: string;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly referenceURL: string;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly iconFile: string;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly iconFile: string;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly filenameExtensions: Array<string>;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly filenameExtensions: Array<string>;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：readonly mimeTypes: Array<string>;  差异内容：NA | 类名：TypeDescriptor；  API声明：readonly mimeTypes: Array<string>;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：belongsTo(type: string): boolean;  差异内容：NA | 类名：TypeDescriptor；  API声明：belongsTo(type: string): boolean;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：isLowerLevelType(type: string): boolean;  差异内容：NA | 类名：TypeDescriptor；  API声明：isLowerLevelType(type: string): boolean;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：isHigherLevelType(type: string): boolean;  差异内容：NA | 类名：TypeDescriptor；  API声明：isHigherLevelType(type: string): boolean;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：TypeDescriptor；  API声明：equals(typeDescriptor: TypeDescriptor): boolean;  差异内容：NA | 类名：TypeDescriptor；  API声明：equals(typeDescriptor: TypeDescriptor): boolean;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：uniformTypeDescriptor；  API声明：function getTypeDescriptor(typeId: string): TypeDescriptor;  差异内容：NA | 类名：uniformTypeDescriptor；  API声明：function getTypeDescriptor(typeId: string): TypeDescriptor;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string;  差异内容：NA | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string;  差异内容：NA | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypeByMIMEType(mimeType: string, belongsTo?: string): string;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string>;  差异内容：NA | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string>;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| API跨平台权限变更 | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypesByMIMEType(mimeType: string, belongsTo?: string): Array<string>;  差异内容：NA | 类名：uniformTypeDescriptor；  API声明：function getUniformDataTypesByMIMEType(mimeType: string, belongsTo?: string): Array<string>;  差异内容：crossplatform | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace dataShare  差异内容：declare namespace dataShare | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：enum ChangeType  差异内容：enum ChangeType | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ChangeType；  API声明：INSERT = 0  差异内容：INSERT = 0 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ChangeType；  API声明：DELETE  差异内容：DELETE | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ChangeType；  API声明：UPDATE  差异内容：UPDATE | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：function createDataProxyHandle(): Promise<DataProxyHandle>;  差异内容：function createDataProxyHandle(): Promise<DataProxyHandle>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：interface ProxyData  差异内容：interface ProxyData | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData；  API声明：value?: ValueType;  差异内容：value?: ValueType; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData；  API声明：allowList?: string[];  差异内容：allowList?: string[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：interface DataProxyChangeInfo  差异内容：interface DataProxyChangeInfo | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyChangeInfo；  API声明：type: ChangeType;  差异内容：type: ChangeType; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyChangeInfo；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyChangeInfo；  API声明：value: ValueType;  差异内容：value: ValueType; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：enum DataProxyErrorCode  差异内容：enum DataProxyErrorCode | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyErrorCode；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyErrorCode；  API声明：URI\_NOT\_EXIST = 1  差异内容：URI\_NOT\_EXIST = 1 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyErrorCode；  API声明：NO\_PERMISSION = 2  差异内容：NO\_PERMISSION = 2 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyErrorCode；  API声明：OVER\_LIMIT = 3  差异内容：OVER\_LIMIT = 3 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：interface DataProxyResult  差异内容：interface DataProxyResult | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyResult；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyResult；  API声明：result: DataProxyErrorCode;  差异内容：result: DataProxyErrorCode; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：interface DataProxyGetResult  差异内容：interface DataProxyGetResult | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyGetResult；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyGetResult；  API声明：result: DataProxyErrorCode;  差异内容：result: DataProxyErrorCode; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyGetResult；  API声明：value: ValueType | undefined;  差异内容：value: ValueType | undefined; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyGetResult；  API声明：allowList: string[] | undefined;  差异内容：allowList: string[] | undefined; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：enum DataProxyType  差异内容：enum DataProxyType | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyType；  API声明：SHARED\_CONFIG = 0  差异内容：SHARED\_CONFIG = 0 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：interface DataProxyConfig  差异内容：interface DataProxyConfig | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyConfig；  API声明：type: DataProxyType;  差异内容：type: DataProxyType; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：dataShare；  API声明：interface DataProxyHandle  差异内容：interface DataProxyHandle | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：on(event: 'dataChange', uris: string[], config: DataProxyConfig, callback: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[];  差异内容：on(event: 'dataChange', uris: string[], config: DataProxyConfig, callback: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：off(event: 'dataChange', uris: string[], config: DataProxyConfig, callback?: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[];  差异内容：off(event: 'dataChange', uris: string[], config: DataProxyConfig, callback?: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>;  差异内容：publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>;  差异内容：delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>;  差异内容：get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：distributedDataObject；  API声明：type ProgressObserver = (sessionId: string, progress: number) => void;  差异内容：type ProgressObserver = (sessionId: string, progress: number) => void; | api/@ohos.data.distributedDataObject.d.ts |
| 删除API | 类名：ResultSet；  API声明：getValueForFlutter(columnIndex: number): ValueType;  差异内容：getValueForFlutter(columnIndex: number): ValueType; | NA | api/@ohos.data.relationalStore.d.ts |
| 删除API | 类名：ResultSet；  API声明：getRowForFlutter(): ValuesBucket;  差异内容：getRowForFlutter(): ValuesBucket; | NA | api/@ohos.data.relationalStore.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.data.dataShare.d.ts  差异内容：ArkData | api/@ohos.data.dataShare.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：setLocale(locale: string): Promise<void>;  差异内容：setLocale(locale: string): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DataObject；  API声明：on(type: 'progressChanged', callback: ProgressObserver): void;  差异内容：on(type: 'progressChanged', callback: ProgressObserver): void; | api/@ohos.data.distributedDataObject.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DataObject；  API声明：off(type: 'progressChanged', callback?: ProgressObserver): void;  差异内容：off(type: 'progressChanged', callback?: ProgressObserver): void; | api/@ohos.data.distributedDataObject.d.ts |
