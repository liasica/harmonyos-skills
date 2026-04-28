---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-6101
title: ArkData
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > ArkData
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95bed77849beda4eaad3b054c7e787cca9a7410f2ac253853b2835cb53868b2d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：ValueType；  API声明：FLOAT  差异内容：NA | 类名：ValueType；  API声明：FLOAT  差异内容：stagemodelonly | api/@ohos.data.distributedKVStore.d.ts |
| 新增错误码 | 类名：SingleKVStore；  API声明：getResultSize(query: Query, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：SingleKVStore；  API声明：getResultSize(query: Query, callback: AsyncCallback<number>): void;  差异内容：15100004 | api/@ohos.data.distributedKVStore.d.ts |
| 新增错误码 | 类名：SingleKVStore；  API声明：getResultSize(query: Query): Promise<number>;  差异内容：NA | 类名：SingleKVStore；  API声明：getResultSize(query: Query): Promise<number>;  差异内容：15100004 | api/@ohos.data.distributedKVStore.d.ts |
| 新增错误码 | 类名：DeviceKVStore；  API声明：getResultSize(query: Query, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：DeviceKVStore；  API声明：getResultSize(query: Query, callback: AsyncCallback<number>): void;  差异内容：15100004 | api/@ohos.data.distributedKVStore.d.ts |
| 新增错误码 | 类名：DeviceKVStore；  API声明：getResultSize(query: Query): Promise<number>;  差异内容：NA | 类名：DeviceKVStore；  API声明：getResultSize(query: Query): Promise<number>;  差异内容：15100004 | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：Schema；  API声明：get root(): FieldNode;  差异内容：get root(): FieldNode; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：Schema；  API声明：get indexes(): Array<string>;  差异内容：get indexes(): Array<string>; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：Schema；  API声明：get mode(): number;  差异内容：get mode(): number; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：Schema；  API声明：get skip(): number;  差异内容：get skip(): number; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：FieldNode；  API声明：get nullable(): boolean;  差异内容：get nullable(): boolean; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：FieldNode；  API声明：get type(): number;  差异内容：get type(): number; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：UnifiedData；  API声明：get properties(): UnifiedDataProperties;  差异内容：get properties(): UnifiedDataProperties; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Summary；  API声明：get summary(): Record<string, number>;  差异内容：get summary(): Record<string, number>; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Summary；  API声明：get totalSize(): number;  差异内容：get totalSize(): number; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：PlainText；  API声明：get textContent(): string;  差异内容：get textContent(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Hyperlink；  API声明：get url(): string;  差异内容：get url(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：HTML；  API声明：get htmlContent(): string;  差异内容：get htmlContent(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：File；  API声明：get uri(): string;  差异内容：get uri(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Image；  API声明：get imageUri(): string;  差异内容：get imageUri(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Video；  API声明：get videoUri(): string;  差异内容：get videoUri(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Audio；  API声明：get audioUri(): string;  差异内容：get audioUri(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：Folder；  API声明：get folderUri(): string;  差异内容：get folderUri(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：get formId(): number;  差异内容：get formId(): number; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：get formName(): string;  差异内容：get formName(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：get bundleName(): string;  差异内容：get bundleName(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：get abilityName(): string;  差异内容：get abilityName(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedForm；  API声明：get module(): string;  差异内容：get module(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：get appId(): string;  差异内容：get appId(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：get appName(): string;  差异内容：get appName(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：get appIconId(): string;  差异内容：get appIconId(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：get appLabelId(): string;  差异内容：get appLabelId(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：get bundleName(): string;  差异内容：get bundleName(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedAppItem；  API声明：get abilityName(): string;  差异内容：get abilityName(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：SystemDefinedPixelMap；  API声明：get rawData(): Uint8Array;  差异内容：get rawData(): Uint8Array; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ApplicationDefinedRecord；  API声明：get applicationDefinedType(): string;  差异内容：get applicationDefinedType(): string; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：ApplicationDefinedRecord；  API声明：get rawData(): Uint8Array;  差异内容：get rawData(): Uint8Array; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get typeId(): string;  差异内容：get typeId(): string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get belongingToTypes(): Array<string>;  差异内容：get belongingToTypes(): Array<string>; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get description(): string;  差异内容：get description(): string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get referenceURL(): string;  差异内容：get referenceURL(): string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get iconFile(): string;  差异内容：get iconFile(): string; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get filenameExtensions(): Array<string>;  差异内容：get filenameExtensions(): Array<string>; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：TypeDescriptor；  API声明：get mimeTypes(): Array<string>;  差异内容：get mimeTypes(): Array<string>; | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：notEqualTo(field: string, value: ValueType): DataSharePredicates;  差异内容：notEqualTo(field: string, value: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：beginWrap(): DataSharePredicates;  差异内容：beginWrap(): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：endWrap(): DataSharePredicates;  差异内容：endWrap(): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：or(): DataSharePredicates;  差异内容：or(): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：like(field: string, value: string): DataSharePredicates;  差异内容：like(field: string, value: string): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：between(field: string, low: ValueType, high: ValueType): DataSharePredicates;  差异内容：between(field: string, low: ValueType, high: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates;  差异内容：notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：greaterThan(field: string, value: ValueType): DataSharePredicates;  差异内容：greaterThan(field: string, value: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：lessThan(field: string, value: ValueType): DataSharePredicates;  差异内容：lessThan(field: string, value: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates;  差异内容：greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates;  差异内容：lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：DataSharePredicates；  API声明：notIn(field: string, value: Array<ValueType>): DataSharePredicates;  差异内容：notIn(field: string, value: Array<ValueType>): DataSharePredicates; | api/@ohos.data.dataSharePredicates.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：type RowData = Array<ValueType>;  差异内容：type RowData = Array<ValueType>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：type RowsData = Array<RowData>;  差异内容：type RowsData = Array<RowData>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：enum DistributedTableType  差异内容：enum DistributedTableType | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedTableType；  API声明：DEVICE\_COLLABORATION = 0  差异内容：DEVICE\_COLLABORATION = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedTableType；  API声明：SINGLE\_VERSION = 1  差异内容：SINGLE\_VERSION = 1 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig；  API声明：tableType?: DistributedTableType;  差异内容：tableType?: DistributedTableType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：interface ReturningConfig  差异内容：interface ReturningConfig | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ReturningConfig；  API声明：columns: Array<string>;  差异内容：columns: Array<string>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ReturningConfig；  API声明：maxReturningCount?: number;  差异内容：maxReturningCount?: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：interface Result  差异内容：interface Result | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Result；  API声明：readonly changed: number;  差异内容：readonly changed: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Result；  API声明：readonly resultSet: LiteResultSet;  差异内容：readonly resultSet: LiteResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getColumnNames(): Array<string>;  差异内容：getColumnNames(): Array<string>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getCurrentRowData(): RowData;  差异内容：getCurrentRowData(): RowData; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet；  API声明：getRowsData(maxCount: number, position?: number): Promise<RowsData>;  差异内容：getRowsData(maxCount: number, position?: number): Promise<RowsData>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore；  API声明：class LiteResultSet  差异内容：class LiteResultSet | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getColumnNames(): Array<string>;  差异内容：getColumnNames(): Array<string>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getColumnIndex(columnName: string): number;  差异内容：getColumnIndex(columnName: string): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getColumnName(columnIndex: number): string;  差异内容：getColumnName(columnIndex: number): string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getColumnType(columnIdentifier: number | string): Promise<ColumnType>;  差异内容：getColumnType(columnIdentifier: number | string): Promise<ColumnType>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getColumnTypeSync(columnIdentifier: number | string): ColumnType;  差异内容：getColumnTypeSync(columnIdentifier: number | string): ColumnType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：goToNextRow(): boolean;  差异内容：goToNextRow(): boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getBlob(columnIndex: number): Uint8Array;  差异内容：getBlob(columnIndex: number): Uint8Array; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getString(columnIndex: number): string;  差异内容：getString(columnIndex: number): string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getLong(columnIndex: number): number;  差异内容：getLong(columnIndex: number): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getDouble(columnIndex: number): number;  差异内容：getDouble(columnIndex: number): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getAsset(columnIndex: number): Asset;  差异内容：getAsset(columnIndex: number): Asset; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getAssets(columnIndex: number): Assets;  差异内容：getAssets(columnIndex: number): Assets; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getValue(columnIndex: number): ValueType;  差异内容：getValue(columnIndex: number): ValueType; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getRow(): ValuesBucket;  差异内容：getRow(): ValuesBucket; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>;  差异内容：getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getCurrentRowData(): RowData;  差异内容：getCurrentRowData(): RowData; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：getRowsData(maxCount: number, position?: number): Promise<RowsData>;  差异内容：getRowsData(maxCount: number, position?: number): Promise<RowsData>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：isColumnNull(columnIndex: number): boolean;  差异内容：isColumnNull(columnIndex: number): boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：LiteResultSet；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;  差异内容：batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result;  差异内容：batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;  差异内容：updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result;  差异内容：updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>;  差异内容：deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result;  差异内容：deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>;  差异内容：queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet;  差异内容：queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>;  差异内容：querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore；  API声明：querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet;  差异内容：querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;  差异内容：batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result;  差异内容：batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;  差异内容：updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result;  差异内容：updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>;  差异内容：deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result;  差异内容：deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>;  差异内容：queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet;  差异内容：queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>;  差异内容：querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：Transaction；  API声明：querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet;  差异内容：querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet; | api/@ohos.data.relationalStore.d.ts |
| 删除API | 类名：Schema；  API声明：root: FieldNode;  差异内容：root: FieldNode; | NA | api/@ohos.data.distributedKVStore.d.ts |
| 删除API | 类名：Schema；  API声明：indexes: Array<string>;  差异内容：indexes: Array<string>; | NA | api/@ohos.data.distributedKVStore.d.ts |
| 删除API | 类名：Schema；  API声明：mode: number;  差异内容：mode: number; | NA | api/@ohos.data.distributedKVStore.d.ts |
| 删除API | 类名：Schema；  API声明：skip: number;  差异内容：skip: number; | NA | api/@ohos.data.distributedKVStore.d.ts |
| 删除API | 类名：FieldNode；  API声明：nullable: boolean;  差异内容：nullable: boolean; | NA | api/@ohos.data.distributedKVStore.d.ts |
| 删除API | 类名：FieldNode；  API声明：type: number;  差异内容：type: number; | NA | api/@ohos.data.distributedKVStore.d.ts |
| 删除API | 类名：UnifiedData；  API声明：properties: UnifiedDataProperties;  差异内容：properties: UnifiedDataProperties; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Summary；  API声明：summary: Record<string, number>;  差异内容：summary: Record<string, number>; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Summary；  API声明：totalSize: number;  差异内容：totalSize: number; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：PlainText；  API声明：textContent: string;  差异内容：textContent: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Hyperlink；  API声明：url: string;  差异内容：url: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：HTML；  API声明：htmlContent: string;  差异内容：htmlContent: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：File；  API声明：uri: string;  差异内容：uri: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Image；  API声明：imageUri: string;  差异内容：imageUri: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Video；  API声明：videoUri: string;  差异内容：videoUri: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Audio；  API声明：audioUri: string;  差异内容：audioUri: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：Folder；  API声明：folderUri: string;  差异内容：folderUri: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedForm；  API声明：formId: number;  差异内容：formId: number; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedForm；  API声明：formName: string;  差异内容：formName: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedForm；  API声明：bundleName: string;  差异内容：bundleName: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedForm；  API声明：abilityName: string;  差异内容：abilityName: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedForm；  API声明：module: string;  差异内容：module: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedAppItem；  API声明：appId: string;  差异内容：appId: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedAppItem；  API声明：appName: string;  差异内容：appName: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedAppItem；  API声明：appIconId: string;  差异内容：appIconId: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedAppItem；  API声明：appLabelId: string;  差异内容：appLabelId: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedAppItem；  API声明：bundleName: string;  差异内容：bundleName: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedAppItem；  API声明：abilityName: string;  差异内容：abilityName: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：SystemDefinedPixelMap；  API声明：rawData: Uint8Array;  差异内容：rawData: Uint8Array; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：ApplicationDefinedRecord；  API声明：applicationDefinedType: string;  差异内容：applicationDefinedType: string; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：ApplicationDefinedRecord；  API声明：rawData: Uint8Array;  差异内容：rawData: Uint8Array; | NA | api/@ohos.data.unifiedDataChannel.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：typeId: string;  差异内容：typeId: string; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：belongingToTypes: Array<string>;  差异内容：belongingToTypes: Array<string>; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：description: string;  差异内容：description: string; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：referenceURL: string;  差异内容：referenceURL: string; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：iconFile: string;  差异内容：iconFile: string; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：filenameExtensions: Array<string>;  差异内容：filenameExtensions: Array<string>; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 删除API | 类名：TypeDescriptor；  API声明：mimeTypes: Array<string>;  差异内容：mimeTypes: Array<string>; | NA | api/@ohos.data.uniformTypeDescriptor.d.ts |
