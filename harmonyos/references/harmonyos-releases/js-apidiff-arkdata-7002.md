---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-7002
title: ArkData
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > ArkData
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8c1d2497f351d194f4965f03a34bea3e36dde885d1072ef7650a6c2ca68e86e1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：201 | api/@ohos.data.distributedDataObject.d.ts |
| 删除错误码 | 类名：RdbStore；  API声明：stopCloudSync(): Promise<void>;  差异内容：14800000 | 类名：RdbStore；  API声明：stopCloudSync(): Promise<void>;  差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：DataObject；  API声明：setSessionId(callback: AsyncCallback<void>): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 9 - 19] | api/@ohos.data.distributedDataObject.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD = 1  差异内容：NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD = 1  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD\_DETAILS = 2  差异内容：NA | 类名：SubscribeType；  API声明：SUBSCRIBE\_TYPE\_CLOUD\_DETAILS = 2  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType；  API声明：DATA\_CHANGE = 0  差异内容：NA | 类名：ChangeType；  API声明：DATA\_CHANGE = 0  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType；  API声明：ASSET\_CHANGE = 1  差异内容：NA | 类名：ChangeType；  API声明：ASSET\_CHANGE = 1  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DistributedType；  API声明：DISTRIBUTED\_CLOUD = 1  差异内容：NA | 类名：DistributedType；  API声明：DISTRIBUTED\_CLOUD = 1  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>;  差异内容：queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;  差异内容：queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProxyData；  API声明：isMultiValues?: boolean;  差异内容：isMultiValues?: boolean; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData；  API声明：values?: Record<number, ValueType>;  差异内容：values?: Record<number, ValueType>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData；  API声明：trustProviders?: string[];  差异内容：trustProviders?: string[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyChangeInfo；  API声明：values?: ValueType[];  差异内容：values?: ValueType[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise<void>;  差异内容：putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise<void>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：removeValue(uri: string, key: number, config: DataProxyConfig): Promise<void>;  差异内容：removeValue(uri: string, key: number, config: DataProxyConfig): Promise<void>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle；  API声明：getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>;  差异内容：getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：interface CloudModelInfo  差异内容：interface CloudModelInfo | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：CloudModelInfo；  API声明：modelType: string;  差异内容：modelType: string; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：CloudModelInfo；  API声明：modelVersionCode?: string;  差异内容：modelVersionCode?: string; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：enum NetworkPolicy  差异内容：enum NetworkPolicy | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：NetworkPolicy；  API声明：WIFI\_ONLY = 0  差异内容：WIFI\_ONLY = 0 | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：NetworkPolicy；  API声明：WIFI\_AND\_CELLULAR = 1  差异内容：WIFI\_AND\_CELLULAR = 1 | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig；  API声明：modelInfo?: CloudModelInfo;  差异内容：modelInfo?: CloudModelInfo; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig；  API声明：networkPolicy?: NetworkPolicy;  差异内容：networkPolicy?: NetworkPolicy; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence；  API声明：function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>;  差异内容：function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>; | api/@ohos.data.intelligence.d.ts |
