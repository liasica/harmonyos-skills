---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-510
title: ArkData
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4819d5adf8d22b6ad8baa5dc6cecb01a8e1fab043bc1daa15d0b7229cecf677b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：preferences；  API声明：enum StorageType  差异内容：enum StorageType | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：StorageType；  API声明：XML = 0  差异内容：XML = 0 | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：StorageType；  API声明：GSKV  差异内容：GSKV | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：preferences；  API声明：function isStorageTypeSupported(type: StorageType): boolean;  差异内容：function isStorageTypeSupported(type: StorageType): boolean; | api/@ohos.data.preferences.d.ts |
| 新增API | NA | 类名：Tokenizer；  API声明：CUSTOM\_TOKENIZER  差异内容：CUSTOM\_TOKENIZER | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：enum ColumnType  差异内容：enum ColumnType | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：NULL  差异内容：NULL | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：INTEGER  差异内容：INTEGER | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：REAL  差异内容：REAL | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：TEXT  差异内容：TEXT | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：BLOB  差异内容：BLOB | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：ASSET  差异内容：ASSET | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：ASSETS  差异内容：ASSETS | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：FLOAT\_VECTOR  差异内容：FLOAT\_VECTOR | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ColumnType；  API声明：UNLIMITED\_INT  差异内容：UNLIMITED\_INT | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function isVectorSupported(): boolean;  差异内容：function isVectorSupported(): boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：function isTokenizerSupported(tokenizer: Tokenizer): boolean;  差异内容：function isTokenizerSupported(tokenizer: Tokenizer): boolean; | api/@ohos.data.relationalStore.d.ts |
| 起始版本有变化 | 类名：Intention；  API声明：DRAG = 'Drag'  差异内容：12 | 类名：Intention；  API声明：DRAG = 'Drag'  差异内容：14 | api/@ohos.data.unifiedDataChannel.d.ts |
| 起始版本有变化 | 类名：unifiedDataChannel；  API声明：function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void;  差异内容：12 | 类名：unifiedDataChannel；  API声明：function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void;  差异内容：14 | api/@ohos.data.unifiedDataChannel.d.ts |
| 起始版本有变化 | 类名：unifiedDataChannel；  API声明：function removeAppShareOptions(intention: Intention): void;  差异内容：12 | 类名：unifiedDataChannel；  API声明：function removeAppShareOptions(intention: Intention): void;  差异内容：14 | api/@ohos.data.unifiedDataChannel.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResultSet；  API声明：getColumnType(columnIdentifier: number | string): Promise<ColumnType>;  差异内容：getColumnType(columnIdentifier: number | string): Promise<ColumnType>; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResultSet；  API声明：getColumnTypeSync(columnIdentifier: number | string): ColumnType;  差异内容：getColumnTypeSync(columnIdentifier: number | string): ColumnType; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ResultSet；  API声明：getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>;  差异内容：getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>;  差异内容：batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RdbStore；  API声明：batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number;  差异内容：batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Transaction；  API声明：batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>;  差异内容：batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Transaction；  API声明：batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number;  差异内容：batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Options；  API声明：storageType?: StorageType | null | undefined;  差异内容：storageType?: StorageType | null | undefined; | api/@ohos.data.preferences.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：StoreConfig；  API声明：rootDir?: string;  差异内容：rootDir?: string; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：StoreConfig；  API声明：vector?: boolean;  差异内容：vector?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：StoreConfig；  API声明：persist?: boolean;  差异内容：persist?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DistributedConfig；  API声明：asyncDownloadAsset?: boolean;  差异内容：asyncDownloadAsset?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DistributedConfig；  API声明：enableCloud?: boolean;  差异内容：enableCloud?: boolean; | api/@ohos.data.relationalStore.d.ts |
