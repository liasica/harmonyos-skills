---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-literesultset
title: Class (LiteResultSet)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Class (LiteResultSet)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fd5ed7fc75301aa7b4e6c54e0129c38fb86dbae840f71105b48169b656671efe
---

提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

LiteResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

下列API示例中，都需先使用[queryWithoutRowCount](arkts-apis-data-relationalstore-rdbstore.md#querywithoutrowcount23)、[querySqlWithoutRowCount](arkts-apis-data-relationalstore-rdbstore.md#querysqlwithoutrowcount23)等query类方法中任一方法获取到LiteResultSet实例，再通过此实例调用对应方法。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本class首批接口从API version 23开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { relationalStore } from '@kit.ArkData';
```

## getColumnNames23+

PhonePC/2in1TabletTVWearable

getColumnNames(): Array<string>

获取结果集中所有列的名称。

列名以字符串数组的形式返回，数组中字符串的顺序与结果集中列的顺序一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回结果集中所有列的名称。支持获取包含重名列的列名。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getColumnNamesExample(store : relationalStore.RdbStore){
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. // 联表查询EMPLOYEE1和EMPLOYEE2，并获取重名的列名。store为获取到的RdbStore实例。
5. resultSet = await store.querySqlWithoutRowCount("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
6. if (resultSet != undefined) {
7. const names = resultSet.getColumnNames();
8. }
9. } catch (err) {
10. console.error(`Failed to get column names: code:${err.code}, message:${err.message}`);
11. }
12. }
```

## getColumnIndex23+

PhonePC/2in1TabletTVWearable

getColumnIndex(columnName: string): number

根据指定的列名获取列索引。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnName | string | 是 | 表示结果集中指定列的名称。当结果集中包含重名列时，返回值会不符合预期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定列的索引。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getColumnIndexExample(store : relationalStore.RdbStore){
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. const idIndex = resultSet.getColumnIndex("ID");
7. const nameIndex = resultSet.getColumnIndex("NAME");
8. const ageIndex = resultSet.getColumnIndex("AGE");
9. const salaryIndex = resultSet.getColumnIndex("SALARY");
10. }
11. } catch (err) {
12. console.error(`failed, code is ${err.code}, message is ${err.message}`);
13. }
14. }
```

## getColumnName23+

PhonePC/2in1TabletTVWearable

getColumnName(columnIndex: number): string

根据指定的列索引获取列名。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 表示结果集中指定列的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定列的名称。当结果集中包含重名列时，返回值会不符合预期。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getColumnNameExample(store : relationalStore.RdbStore){
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. const id = resultSet.getColumnName(0);
7. const name = resultSet.getColumnName(1);
8. const age = resultSet.getColumnName(2);
9. const salary = resultSet.getColumnName(3);
10. }
11. } catch (err) {
12. console.error(`failed, code is ${err.code}, message is ${err.message}`);
13. }
14. }
```

## getColumnType23+

PhonePC/2in1TabletTVWearable

getColumnType(columnIdentifier: number | string): Promise<ColumnType>

根据指定的列索引或列名称获取列数据类型，使用Promise异步回调。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIdentifier | number | string | 是 | 表示结果集中指定列的索引或名称，索引从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColumnType](arkts-apis-data-relationalstore-e.md#columntype18)> | Promise对象。返回指定列的数据类型。当结果集中包含重名列时，通过列名获取的结果会不符合预期。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getColumnTypeExample(store : relationalStore.RdbStore){
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. // 方式一：通过列名获取列数据类型
8. let idType = await resultSet.getColumnType("ID");
9. let nameType = await resultSet.getColumnType("NAME");
10. let ageType = await resultSet.getColumnType("AGE");
11. let salaryType = await resultSet.getColumnType("SALARY");
12. let codesType = await resultSet.getColumnType("CODES");
13. // 方式二：通过列索引获取列数据类型
14. let identityType = await resultSet.getColumnType(5);
15. let assetDataType = await resultSet.getColumnType(6);
16. let assetsDataType = await resultSet.getColumnType(7);
17. let floatArrayType = await resultSet.getColumnType(8);
18. }
19. } catch (err) {
20. console.error(`failed, code is ${err.code}, message is ${err.message}`);
21. }
22. }
```

## getColumnTypeSync23+

PhonePC/2in1TabletTVWearable

getColumnTypeSync(columnIdentifier: number | string): ColumnType

根据指定的列索引或列名称获取列数据类型。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIdentifier | number | string | 是 | 表示结果集中指定列的索引或名称，索引从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColumnType](arkts-apis-data-relationalstore-e.md#columntype18) | 返回指定列的数据类型。当结果集中包含重名列时，通过列名获取的结果会不符合预期。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getColumnTypeSyncExample(store : relationalStore.RdbStore){
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. // 方式一：通过列名获取列数据类型
8. let idType = resultSet.getColumnTypeSync("ID");
9. let nameType = resultSet.getColumnTypeSync("NAME");
10. let ageType = resultSet.getColumnTypeSync("AGE");
11. let salaryType = resultSet.getColumnTypeSync("SALARY");
12. let codesType = resultSet.getColumnTypeSync("CODES");
13. // 方式二：通过列索引获取列数据类型
14. let identityType = resultSet.getColumnTypeSync(5);
15. let assetDataType = resultSet.getColumnTypeSync(6);
16. let assetsDataType = resultSet.getColumnTypeSync(7);
17. let floatArrayType = resultSet.getColumnTypeSync(8);
18. }
19. } catch (err) {
20. console.error(`failed, code is ${err.code}, message is ${err.message}`);
21. }
22. }
```

## goToNextRow23+

PhonePC/2in1TabletTVWearable

goToNextRow(): boolean

移动结果集到下一行。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集到下一行，返回true；否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |

**示例：**

```
1. async function goToNextRowExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. }
8. } catch (err) {
9. console.error(`failed, code is ${err.code}, message is ${err.message}`);
10. }
11. }
```

## getValue23+

PhonePC/2in1TabletTVWearable

getValue(columnIndex: number): ValueType

获取当前行中指定列的值。

如果值类型为INTEGER，值大于Number.MAX\_SAFE\_INTEGER或小于Number.MIN\_SAFE\_INTEGER时，如果不希望丢失精度，建议使用[getString](arkts-apis-data-relationalstore-literesultset.md#getstring23)接口获取。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 允许返回的数据字段类型。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. async function getValueExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const name = resultSet.getValue(resultSet.getColumnIndex("NAME"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getBlob23+

PhonePC/2in1TabletTVWearable

getBlob(columnIndex: number): Uint8Array

以字节数组的形式获取当前行中指定列的值。

如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成字节数组类型返回指定值，如果该列内容为空时，会返回空字节数组。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 以字节数组的形式返回指定列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800041 | Type conversion failed. |

**示例：**

```
1. async function getBlobExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const name = resultSet.getBlob(resultSet.getColumnIndex("CODES"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getString23+

PhonePC/2in1TabletTVWearable

getString(columnIndex: number): string

以字符串形式获取当前行中指定列的值。

如果当前列中的值为INTEGER、DOUBLE、TEXT、BLOB类型，会以字符串形式返回指定值；如果该列内容为空，则会返回空字符串""。

如果当前列中的值为DOUBLE类型，可能存在精度的丢失，建议使用[getDouble](arkts-apis-data-relationalstore-literesultset.md#getdouble23)接口获取。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串形式返回指定列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800041 | Type conversion failed. |

**示例：**

```
1. async function getStringExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getLong23+

PhonePC/2in1TabletTVWearable

getLong(columnIndex: number): number

以Long形式获取当前行中指定列的值。

如果当前列的数据类型为INTEGER、DOUBLE、TEXT会转成Long类型返回指定值，非数字的TEXT、BLOB类型会返回0。如果该列内容为空时，会返回0。

如果当前列的数据类型为INTEGER，值大于Number.MAX\_SAFE\_INTEGER 或小于Number.MIN\_SAFE\_INTEGER时，如果不希望丢失精度，建议使用[getString](arkts-apis-data-relationalstore-literesultset.md#getstring23)接口获取。

如果当前列的数据类型为DOUBLE时，如果不希望丢失精度，建议使用[getDouble](arkts-apis-data-relationalstore-literesultset.md#getdouble23)接口获取。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 以Long形式返回指定列的值。  该接口支持的精度范围是：Number.MIN\_SAFE\_INTEGER ~ Number.MAX\_SAFE\_INTEGER，若超出该范围，建议对于DOUBLE类型的值使用[getDouble](arkts-apis-data-relationalstore-literesultset.md#getdouble23)，对于INTEGER类型的值使用[getString](arkts-apis-data-relationalstore-literesultset.md#getstring23)。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800041 | Type conversion failed. |

**示例：**

```
1. async function getLongExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getDouble23+

PhonePC/2in1TabletTVWearable

getDouble(columnIndex: number): number

以double形式获取当前行中指定列的值。

如果当前列的数据类型为INTEGER、DOUBLE、TEXT会转成double类型返回指定值，非数字的TEXT、BLOB类型会返回0.0。如果该列内容为空时，会返回0.0。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 以double形式返回指定列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800041 | Type conversion failed. |

**示例：**

```
1. async function getDoubleExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getAsset23+

PhonePC/2in1TabletTVWearable

getAsset(columnIndex: number): Asset

以[Asset](arkts-apis-data-relationalstore-i.md#asset10)形式获取当前行中指定列的值。

如果当前列的数据类型为Asset类型，会以Asset类型返回指定值；如果当前列中的值为null时，会返回null；如果当前列的数据类型非Asset类型，则返回14800041。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Asset](arkts-apis-data-relationalstore-i.md#asset10) | 以Asset形式返回指定列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800041 | Type conversion failed. |

**示例：**

```
1. async function getAssetExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const doc = resultSet.getAsset(resultSet.getColumnIndex("DOC"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getAssets23+

PhonePC/2in1TabletTVWearable

getAssets(columnIndex: number): Assets

以[Assets](arkts-apis-data-relationalstore-t.md#assets10)形式获取当前行中指定列的值。

如果当前列的数据类型为Assets类型，会以Assets类型返回指定值；如果当前列中的值为null时，会返回null；如果当前列的数据类型非Assets类型，则返回14800041。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Assets](arkts-apis-data-relationalstore-t.md#assets10) | 以Assets形式返回指定列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800041 | Type conversion failed. |

**示例：**

```
1. async function getAssetsExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const name = resultSet.getAssets(resultSet.getColumnIndex("DOCS"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## getRow23+

PhonePC/2in1TabletTVWearable

getRow(): ValuesBucket

获取当前行的数据。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 返回指定行的值。当结果集中包含重名列时，返回值会不符合预期，建议使用[getCurrentRowData](arkts-apis-data-relationalstore-literesultset.md#getcurrentrowdata23)接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getRowExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const rowData = resultSet.getRow();
8. console.info(`rowData: ${JSON.stringify(rowData)}`);
9. }
10. } catch (err) {
11. console.error(`failed, code is ${err.code}, message is ${err.message}`);
12. }
13. }
```

## getCurrentRowData23+

PhonePC/2in1TabletTVWearable

getCurrentRowData(): RowData

获取当前行所有列的值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RowData](arkts-apis-data-relationalstore-t.md#rowdata23) | 返回当前行所有列的值。支持获取包含重名列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function getCurrentRowDataExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. // 联表查询EMPLOYEE1和EMPLOYEE2，并获取当前行包含重名列名的值。store为获取到的RdbStore实例。
5. resultSet = await store.querySqlWithoutRowCount("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
6. if (resultSet != undefined) {
7. resultSet.goToNextRow();
8. const rowData = resultSet.getCurrentRowData();
9. console.info(`rowData: ${JSON.stringify(rowData)}`);
10. }
11. } catch (err) {
12. console.error(`Failed to get row data: code:${err.code}, message:${err.message}`);
13. }
14. }
```

## getRows23+

PhonePC/2in1TabletTVWearable

getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>

从结果集中获取指定数量的数据，使用Promise异步回调。禁止与[LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)的其他接口并发调用，否则获取的数据可能非预期。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxCount | number | 是 | 正整数，指定要从结果集中获取数据的条数。 |
| position | number | 否 | 非负整数，指定从结果集中获取数据的起始位置，不填则从结果集的当前行（默认首次获取数据时为当前结果集的第一行）开始获取数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)>> | 返回maxCount条数据，剩余数据不足maxCount条则返回剩余数据，返回空数组时代表已经遍历到结果集的末尾。当结果集中包含重名列时，返回值会不符合预期，建议使用[getRowsData](arkts-apis-data-relationalstore-literesultset.md#getrowsdata23)接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |

**示例：**

```
1. async function getRowsExample(store : relationalStore.RdbStore) {
2. // 以查到100条数据为例
3. try {
4. let resultSet: relationalStore.LiteResultSet | undefined;
5. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
6. // 示例1：仅指定maxCount
7. if (resultSet != undefined) {
8. let rows: Array<relationalStore.ValuesBucket>;
9. let maxCount: number = 50;
10. // 从结果集的当前行（默认首次获取数据时为当前结果集的第一行，后续为上次获取数据结束位置的下一行）开始获取数据
11. // getRows会自动移动结果集当前行到上次getRows获取结束位置的下一行，goToNextRow等接口移动
12. while ((rows = await resultSet.getRows(maxCount)).length != 0) {
13. console.info(JSON.stringify(rows[0]));
14. }
15. }

17. // 示例2：指定maxCount和起始的position
18. if (resultSet != undefined) {
19. let rows: Array<relationalStore.ValuesBucket>;
20. let maxCount: number = 50;
21. let position: number = 50;
22. while ((rows = await resultSet.getRows(maxCount, position)).length != 0) {
23. console.info(JSON.stringify(rows[0]));
24. position += rows.length;
25. }
26. }
27. } catch (err) {
28. console.error(`failed, code is ${err.code}, message is ${err.message}`);
29. }
30. }
```

## getRowsData23+

PhonePC/2in1TabletTVWearable

getRowsData(maxCount: number, position?: number): Promise<RowsData>

从指定位置position开始，最多获取maxCount行数据。使用Promise异步回调。禁止与[LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)的其他接口并发调用，否则获取的数据可能非预期。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxCount | number | 是 | 正整数，指定从结果集中获取数据的条数。不为正整数则参数非法，抛出错误码14800001。 |
| position | number | 否 | 非负整数，指定从结果集中获取数据的起始位置，不填则从结果集的当前行（默认首次获取数据时为当前结果集的第一行）开始获取数据。不为非负整数则参数非法，抛出错误码14800001。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RowsData](arkts-apis-data-relationalstore-t.md#rowsdata23)> | 返回maxCount条数据，剩余数据不足maxCount条则返回剩余数据，返回空数组时代表已经遍历到结果集的末尾。支持获取包含重名列的值。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |

**示例：**

```
1. async function getRowsDataExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. // 联表查询EMPLOYEE1和EMPLOYEE2，并获取多行包含重名列名的值。store为获取到的RdbStore实例。
5. resultSet = await store.querySqlWithoutRowCount("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
6. // 以查到50条数据为例
7. // 示例1：仅指定maxCount
8. if (resultSet != undefined) {
9. let rowsData: relationalStore.RowsData;
10. // 从结果集的当前行（默认首次获取数据时为当前结果集的第一行，后续为上次获取数据结束位置的下一行）开始获取数据
11. // getRowsData会自动移动结果集当前行到上次getRowsData获取结束位置的下一行，无需使用goToNextRow接口移动
12. let maxCount: number = 50;
13. let rowCount: number = 0;
14. while ((rowsData = await resultSet.getRowsData(maxCount)).length != 0) {
15. rowsData.forEach((rowData, index) => {
16. // 第rowCount + index + 1行的查询结果
17. console.info(`${rowCount + index + 1}：${rowData}`);
18. });
19. rowCount += rowsData.length;
20. }
21. }

23. // 示例2：指定maxCount和起始的position
24. if (resultSet != undefined) {
25. let rowsData: relationalStore.RowsData;
26. let maxCount: number = 50;
27. let position: number = 50;
28. while ((rowsData = await resultSet.getRowsData(maxCount, position)).length != 0) {
29. rowsData.forEach((rowData, index) => {
30. // 第position + index + 1行的查询结果
31. console.info(`${position + index + 1}：${rowData}`);
32. });
33. position += rowsData.length;
34. }
35. }
36. } catch (err) {
37. console.error(`Failed to get rows data: code:${err.code}, message:${err.message}`);
38. }
39. }
```

## isColumnNull23+

PhonePC/2in1TabletTVWearable

isColumnNull(columnIndex: number): boolean

检查当前行中指定列的值是否为null。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前行中指定列的值为null，则返回true；否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. async function isColumnNullExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.goToNextRow();
7. const name = resultSet.isColumnNull(resultSet.getColumnIndex("NAME"));
8. }
9. } catch (err) {
10. console.error(`failed, code is ${err.code}, message is ${err.message}`);
11. }
12. }
```

## close23+

PhonePC/2in1TabletTVWearable

close(): void

关闭结果集，若不关闭可能会引起fd泄露和内存泄露。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

```
1. async function closeExample(store : relationalStore.RdbStore) {
2. try {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. resultSet.close();
7. }
8. } catch (err) {
9. console.error(`failed, code is ${err.code}, message is ${err.message}`);
10. }
11. }
```
