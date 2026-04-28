---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-resultset
title: resultSet (结果集)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > data/rdb > resultSet (结果集)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b271958e044ad2f6690f6f0818940843958e63f455d4bba0348506d0eeee6312
---

结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.relationalStore#ResultSet](arkts-apis-data-relationalstore-resultset.md)。

## ResultSet

PhonePC/2in1TabletTVWearable

提供通过查询数据库生成的数据库结果集的访问方法。

### 使用说明

需要通过[RdbStore.query()](js-apis-data-rdb.md#query)获取resultSet对象。

```
1. import dataRdb from '@ohos.data.rdb';
2. let predicates = new dataRdb.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("AGE", 18);
4. let promise = rdbStore.query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
5. promise.then((resultSet) => {
6. console.log(TAG + "resultSet columnNames:" + resultSet.columnNames);
7. console.log(TAG + "resultSet columnCount:" + resultSet.columnCount);
8. });
```

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| columnNames | Array<string> | 是 | 否 | 获取结果集中所有列的名称。 |
| columnCount | number | 是 | 否 | 获取结果集中的列数。 |
| rowCount | number | 是 | 否 | 获取结果集中的行数。 |
| rowIndex | number | 是 | 否 | 获取结果集当前行的索引。 |
| isAtFirstRow | boolean | 是 | 否 | 检查结果集是否位于第一行。 |
| isAtLastRow | boolean | 是 | 否 | 检查结果集是否位于最后一行。 |
| isEnded | boolean | 是 | 否 | 检查结果集是否位于最后一行之后。 |
| isStarted | boolean | 是 | 否 | 检查指针是否移动过。 |
| isClosed | boolean | 是 | 否 | 检查当前结果集是否关闭。 |

### getColumnIndex

PhonePC/2in1TabletTVWearable

getColumnIndex(columnName: string): number

根据指定的列名获取列索引。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnName | string | 是 | 表示结果集中指定列的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定列的索引。 |

**示例：**

```
1. const success = resultSet.goToFirstRow();
2. if (success) {
3. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
4. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
5. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
6. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
7. }
```

### getColumnName

PhonePC/2in1TabletTVWearable

getColumnName(columnIndex: number): string

根据指定的列索引获取列名。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 表示结果集中指定列的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定列的名称。 |

**示例：**

```
1. const id = resultSet.getColumnName(0);
2. const name = resultSet.getColumnName(1);
3. const age = resultSet.getColumnName(2);
```

### goTo

PhonePC/2in1TabletTVWearable

goTo(offset:number): boolean

向前或向后移至结果集的指定行，相对于其当前位置偏移。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 表示相对于当前位置的偏移量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**示例：**

```
1. let predicatesgoto = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promisequerygoto = rdbStore.query(predicatesgoto, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promisequerygoto.then((resultSet) => {
4. resultSet.goTo(1);
5. resultSet.close();
6. }).catch((err) => {
7. console.log('query failed');
8. });
```

### goToRow

PhonePC/2in1TabletTVWearable

goToRow(position: number): boolean

转到结果集的指定行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | number | 是 | 表示要移动到的指定位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**示例：**

```
1. let predicatesgotorow = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promisequerygotorow = rdbStore.query(predicatesgotorow, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promisequerygotorow.then((resultSet) => {
4. resultSet.goToRow(5);
5. resultSet.close();
6. }).catch((err) => {
7. console.log('query failed');
8. });
```

### goToFirstRow

PhonePC/2in1TabletTVWearable

goToFirstRow(): boolean

转到结果集的第一行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**示例：**

```
1. let predicatesgoFirst = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promisequerygoFirst = rdbStore.query(predicatesgoFirst, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promisequerygoFirst.then((resultSet) => {
4. resultSet.goToFirstRow();
5. resultSet.close();
6. }).catch((err) => {
7. console.log('query failed');
8. });
```

### goToLastRow

PhonePC/2in1TabletTVWearable

goToLastRow(): boolean

转到结果集的最后一行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**示例：**

```
1. let predicatesgoLast = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promisequerygoLast = rdbStore.query(predicatesgoLast, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promisequerygoLast.then((resultSet) => {
4. resultSet.goToLastRow();
5. resultSet.close();
6. }).catch((err) => {
7. console.log('query failed');
8. });
```

### goToNextRow

PhonePC/2in1TabletTVWearable

goToNextRow(): boolean

转到结果集的下一行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**示例：**

```
1. let predicatesgoNext = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promisequerygoNext = rdbStore.query(predicatesgoNext, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promisequerygoNext.then((resultSet) => {
4. resultSet.goToNextRow();
5. resultSet.close();
6. }).catch((err) => {
7. console.log('query failed');
8. });
```

### goToPreviousRow

PhonePC/2in1TabletTVWearable

goToPreviousRow(): boolean

转到结果集的上一行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**示例：**

```
1. let predicatesgoPrev = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promisequerygoPrev = rdbStore.query(predicatesgoPrev, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promisequerygoPrev.then((resultSet) => {
4. resultSet.goToPreviousRow();
5. resultSet.close();
6. }).catch((err) => {
7. console.log('query failed');
8. });
```

### getBlob

PhonePC/2in1TabletTVWearable

getBlob(columnIndex: number): Uint8Array

以字节数组的形式获取当前行中指定列的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 以字节数组的形式返回指定列的值。 |

**示例：**

```
1. const codes = resultSet.getBlob(resultSet.getColumnIndex("CODES"));
```

### getString

PhonePC/2in1TabletTVWearable

getString(columnIndex: number): string

以字符串形式获取当前行中指定列的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串形式返回指定列的值。 |

**示例：**

```
1. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
```

### getLong

PhonePC/2in1TabletTVWearable

getLong(columnIndex: number): number

以Long形式获取当前行中指定列的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 以Long形式返回指定列的值。  该接口支持的数据范围是：Number.MIN\_SAFE\_INTEGER ~ Number.MAX\_SAFE\_INTEGER，若超出该范围，建议使用[getDouble](js-apis-data-resultset.md#getdouble)。 |

**示例：**

```
1. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
```

### getDouble

PhonePC/2in1TabletTVWearable

getDouble(columnIndex: number): number

以double形式获取当前行中指定列的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 以double形式返回指定列的值。 |

**示例：**

```
1. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
```

### isColumnNull

PhonePC/2in1TabletTVWearable

isColumnNull(columnIndex: number): boolean

检查当前行中指定列的值是否为null。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | number | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前行中指定列的值为null，则返回true，否则返回false。 |

**示例：**

```
1. const isColumnNull = resultSet.isColumnNull(resultSet.getColumnIndex("CODES"));
```

### close

PhonePC/2in1TabletTVWearable

close(): void

关闭结果集。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

```
1. let predicatesClose = new dataRdb.RdbPredicates("EMPLOYEE");
2. let promiseClose = rdbStore.query(predicatesClose, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
3. promiseClose.then((resultSet) => {
4. resultSet.close();
5. }).catch((err) => {
6. console.log('resultset close failed');
7. });
```
