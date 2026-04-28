---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-6001
title: ArkData
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:34+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4b3347d9ae06faf89dfc994c368288f20f6759a8464066ecbc4aff34411c907b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：201 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.data.distributedDataObject.d.ts |
| 权限变更 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum FormType  差异内容：declare enum FormType | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：FormType；  API声明：TYPE\_BIG = 0  差异内容：TYPE\_BIG = 0 | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：FormType；  API声明：TYPE\_MID = 1  差异内容：TYPE\_MID = 1 | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：FormType；  API声明：TYPE\_SMALL = 2  差异内容：TYPE\_SMALL = 2 | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：global；  API声明：declare struct ContentFormCard  差异内容：declare struct ContentFormCard | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：ContentFormCard；  API声明：contentFormData: uniformDataStruct.ContentForm;  差异内容：contentFormData: uniformDataStruct.ContentForm; | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：ContentFormCard；  API声明：@Prop  formType: FormType;  差异内容：@Prop  formType: FormType; | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：ContentFormCard；  API声明：@Prop  formWidth?: number;  差异内容：@Prop  formWidth?: number; | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：ContentFormCard；  API声明：@Prop  formHeight?: number;  差异内容：@Prop  formHeight?: number; | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：ContentFormCard；  API声明：handleOnClick?: Function;  差异内容：handleOnClick?: Function; | api/@ohos.data.UdmfComponents.d.ets |
| 新增API | NA | 类名：distributedDataObject；  API声明：type DataObserver = (sessionId: string, fields: Array<string>) => void;  差异内容：type DataObserver = (sessionId: string, fields: Array<string>) => void; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：distributedDataObject；  API声明：type StatusObserver = (sessionId: string, networkId: string, status: string) => void;  差异内容：type StatusObserver = (sessionId: string, networkId: string, status: string) => void; | api/@ohos.data.distributedDataObject.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：interface ExceptionMessage  差异内容：interface ExceptionMessage | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ExceptionMessage；  API声明：code: number;  差异内容：code: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ExceptionMessage；  API声明：message: string;  差异内容：message: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ExceptionMessage；  API声明：sql: string;  差异内容：sql: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：interface SqlInfo  差异内容：interface SqlInfo | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlInfo；  API声明：sql: string;  差异内容：sql: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlInfo；  API声明：args: Array<ValueType>;  差异内容：args: Array<ValueType>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo;  差异内容：function getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function getUpdateSqlInfo(predicates: RdbPredicates, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo;  差异内容：function getUpdateSqlInfo(predicates: RdbPredicates, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function getDeleteSqlInfo(predicates: RdbPredicates): SqlInfo;  差异内容：function getDeleteSqlInfo(predicates: RdbPredicates): SqlInfo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>): SqlInfo;  差异内容：function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>): SqlInfo; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：sendableRelationalStore；  API声明：type NonSendableValues = Array<relationalStore.ValueType>;  差异内容：type NonSendableValues = Array<relationalStore.ValueType>; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore；  API声明：function fromSendableValues(values: collections.Array<ValueType>): NonSendableValues;  差异内容：function fromSendableValues(values: collections.Array<ValueType>): NonSendableValues; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore；  API声明：function toSendableValues(values: NonSendableValues): collections.Array<ValueType>;  差异内容：function toSendableValues(values: NonSendableValues): collections.Array<ValueType>; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Intention；  API声明：SYSTEM\_SHARE = 'SystemShare'  差异内容：SYSTEM\_SHARE = 'SystemShare' | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Intention；  API声明：PICKER = 'Picker'  差异内容：PICKER = 'Picker' | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Intention；  API声明：MENU = 'Menu'  差异内容：MENU = 'Menu' | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.data.UdmfComponents.d.ets  差异内容：ArkData | api/@ohos.data.UdmfComponents.d.ets |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace dataSharePredicates  差异内容：NA | 类名：global；  API声明：declare namespace dataSharePredicates  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：dataSharePredicates；  API声明：class DataSharePredicates  差异内容：NA | 类名：dataSharePredicates；  API声明：class DataSharePredicates  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSharePredicates；  API声明：equalTo(field: string, value: ValueType): DataSharePredicates;  差异内容：NA | 类名：DataSharePredicates；  API声明：equalTo(field: string, value: ValueType): DataSharePredicates;  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSharePredicates；  API声明：and(): DataSharePredicates;  差异内容：NA | 类名：DataSharePredicates；  API声明：and(): DataSharePredicates;  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSharePredicates；  API声明：orderByAsc(field: string): DataSharePredicates;  差异内容：NA | 类名：DataSharePredicates；  API声明：orderByAsc(field: string): DataSharePredicates;  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSharePredicates；  API声明：orderByDesc(field: string): DataSharePredicates;  差异内容：NA | 类名：DataSharePredicates；  API声明：orderByDesc(field: string): DataSharePredicates;  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSharePredicates；  API声明：limit(total: number, offset: number): DataSharePredicates;  差异内容：NA | 类名：DataSharePredicates；  API声明：limit(total: number, offset: number): DataSharePredicates;  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSharePredicates；  API声明：in(field: string, value: Array<ValueType>): DataSharePredicates;  差异内容：NA | 类名：DataSharePredicates；  API声明：in(field: string, value: Array<ValueType>): DataSharePredicates;  差异内容：atomicservice | api/@ohos.data.dataSharePredicates.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：export type ValueType = number | string | boolean;  差异内容：NA | 类名：global；  API声明：export type ValueType = number | string | boolean;  差异内容：atomicservice | api/@ohos.data.ValuesBucket.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbPredicates；  API声明：having(conditions: string, args?: Array<ValueType>): RdbPredicates;  差异内容：having(conditions: string, args?: Array<ValueType>): RdbPredicates; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DataObject；  API声明：setAsset(assetKey: string, uri: string): Promise<void>;  差异内容：setAsset(assetKey: string, uri: string): Promise<void>; | api/@ohos.data.distributedDataObject.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DataObject；  API声明：setAssets(assetsKey: string, uris: Array<string>): Promise<void>;  差异内容：setAssets(assetsKey: string, uris: Array<string>): Promise<void>; | api/@ohos.data.distributedDataObject.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void;  差异内容：on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void;  差异内容：on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void;  差异内容：off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void;  差异内容：off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：rekey(cryptoParam?: CryptoParam): Promise<void>;  差异内容：rekey(cryptoParam?: CryptoParam): Promise<void>; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：StoreConfig；  API声明：enableSemanticIndex?: boolean;  差异内容：enableSemanticIndex?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：DataObject；  API声明：on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void;  差异内容：on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void; | 类名：DataObject；  API声明：on(type: 'change', callback: DataObserver): void;  差异内容：on(type: 'change', callback: DataObserver): void; | api/@ohos.data.distributedDataObject.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：DataObject；  API声明：off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void;  差异内容：off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void; | 类名：DataObject；  API声明：off(type: 'change', callback?: DataObserver): void;  差异内容：off(type: 'change', callback?: DataObserver): void; | api/@ohos.data.distributedDataObject.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：DataObject；  API声明：on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;  差异内容：on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void; | 类名：DataObject；  API声明：on(type: 'status', callback: StatusObserver): void;  差异内容：on(type: 'status', callback: StatusObserver): void; | api/@ohos.data.distributedDataObject.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：DataObject；  API声明：off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;  差异内容：off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void; | 类名：DataObject；  API声明：off(type: 'status', callback?: StatusObserver): void;  差异内容：off(type: 'status', callback?: StatusObserver): void; | api/@ohos.data.distributedDataObject.d.ts |
