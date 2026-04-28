---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablerelationalstore
title: @ohos.data.sendableRelationalStore (共享关系型数据库)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.sendableRelationalStore (共享关系型数据库)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:19+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:74ecd0d8049b129f23c5cf4b9d0097cc70a339630ee217a74a4dd24eb857246a
---

该模块针对关系型数据库（Relational Database，RDB）提供了sendable支持。支持从查询结果集中获取sendable类型ValuesBucket用于并发实例间传递。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 使用场景

PhonePC/2in1TabletTVWearable

在使用[taskpool](../harmonyos-guides/taskpool-introduction.md)进行多线程计算时，因为对跨线程传递的数据类型限制，关系型数据库常规的ValuesBucket、Asset、Assets数据存储容器不能直接用于跨线程传递。

本模块提供了相应的类型转换工具函数，以便在常规数据存储容器和支持跨线程传递的数据存储容器之间进行类型转换，用于跨线程传递。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendableRelationalStore } from '@kit.ArkData';
```

## sendableRelationalStore.toSendableValuesBucket

PhonePC/2in1TabletTVWearable

toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket

将不能用于跨线程传递的键值对数据，转换为可用于跨线程传递的键值对数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| valuesBucket | [NonSendableBucket](js-apis-data-sendablerelationalstore.md#nonsendablebucket) | 是 | 不可跨线程传递的ValuesBucket数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ValuesBucket](js-apis-data-sendablerelationalstore.md#valuesbucket) | 可用于跨线程传递的ValuesBucket数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**示例：**

```
1. const asset1: sendableRelationalStore.NonSendableAsset = {
2. name: 'hangman',
3. uri: '//path/example',
4. path: '//path/example',
5. createTime: 'createTime1',
6. modifyTime: 'modifyTime1',
7. size: 'size1'
8. };
9. const asset2: sendableRelationalStore.NonSendableAsset = {
10. name: 'hangman',
11. uri: '//path/example',
12. path: '//path/example',
13. createTime: 'createTime1',
14. modifyTime: 'modifyTime1',
15. size: 'size1'
16. };
17. const u8 = new Uint8Array([1, 2, 3]);
18. const valuesBucket: sendableRelationalStore.NonSendableBucket = {
19. age: 18,
20. name: "hangman",
21. salary: 100.5,
22. passed: true,
23. data1: asset1,
24. blobType: u8,
25. bigValue: BigInt("15822401018187971961171"),
26. data2: [asset1, asset2]
27. };

29. const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);
```

## sendableRelationalStore.fromSendableValuesBucket

PhonePC/2in1TabletTVWearable

fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket

将可用于跨线程传递的键值对数据，转换为不能用于跨线程传递的键值对数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| valuesBucket | [ValuesBucket](js-apis-data-sendablerelationalstore.md#valuesbucket) | 是 | 可用于跨线程传递的ValuesBucket数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [NonSendableBucket](js-apis-data-sendablerelationalstore.md#nonsendablebucket) | 不可跨线程传递的ValuesBucket数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**示例：**

```
1. const asset1: sendableRelationalStore.NonSendableAsset = {
2. name: 'hangman',
3. uri: '//path/example',
4. path: '//path/example',
5. createTime: 'createTime1',
6. modifyTime: 'modifyTime1',
7. size: 'size1'
8. };
9. const asset2: sendableRelationalStore.NonSendableAsset = {
10. name: 'hangman',
11. uri: '//path/example',
12. path: '//path/example',
13. createTime: 'createTime1',
14. modifyTime: 'modifyTime1',
15. size: 'size1'
16. };
17. const u8 = new Uint8Array([1, 2, 3]);

19. const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket({
20. age: 18,
21. name: "hangman",
22. salary: 100.5,
23. passed: true,
24. data1: asset1,
25. blobType: u8,
26. bigValue: BigInt("15822401018187971961171"),
27. data2: [asset1, asset2]
28. });
29. const nonSendableBucket = sendableRelationalStore.fromSendableValuesBucket(sendableValuesBucket);
```

## sendableRelationalStore.toSendableAsset

PhonePC/2in1TabletTVWearable

toSendableAsset(asset: NonSendableAsset): Asset

将不可跨线程传递的附件数据，转换为可跨线程传递的附件数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | [NonSendableAsset](js-apis-data-sendablerelationalstore.md#nonsendableasset) | 是 | 不可跨线程传递的Asset数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [Asset](js-apis-data-sendablerelationalstore.md#asset) | 可跨线程传递的Asset数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**示例：**

```
1. const asset1: sendableRelationalStore.NonSendableAsset = {
2. name: 'hangman',
3. uri: '//path/example',
4. path: '//path/example',
5. createTime: 'createTime1',
6. modifyTime: 'modifyTime1',
7. size: 'size1'
8. };
9. const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
```

## sendableRelationalStore.fromSendableAsset

PhonePC/2in1TabletTVWearable

fromSendableAsset(asset: Asset): NonSendableAsset

将可跨线程传递的附件数据，转换为不可跨线程传递的附件数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | [Asset](js-apis-data-sendablerelationalstore.md#asset) | 是 | 可跨线程传递的Asset数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [NonSendableAsset](js-apis-data-sendablerelationalstore.md#nonsendableasset) | 不可跨线程传递的Asset数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |

**示例：**

```
1. const asset1: sendableRelationalStore.NonSendableAsset = {
2. name: 'hangman',
3. uri: '//path/example',
4. path: '//path/example',
5. createTime: 'createTime1',
6. modifyTime: 'modifyTime1',
7. size: 'size1'
8. };
9. const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
10. const normalAsset = sendableRelationalStore.fromSendableAsset(sendableAsset);
```

## sendableRelationalStore.fromSendableValues20+

PhonePC/2in1TabletTVWearable

fromSendableValues(values: collections.Array<ValueType>): NonSendableValues

将可跨线程传递的数组数据，转换为不可跨线程传递的数组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | collections.Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 是 | 可跨线程传递的数组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [NonSendableValues](js-apis-data-sendablerelationalstore.md#nonsendablevalues20) | 不可跨线程传递的数组数据。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800000 | Inner error. |

**示例：**

```
1. import { sendableRelationalStore } from '@kit.ArkData';
2. import { collections } from '@kit.ArkTS';
3. const array = new collections.Array<sendableRelationalStore.ValueType>();
4. array.push("a");
5. array.push("b");
6. array.push(1);
7. array.push(2);
8. const values = sendableRelationalStore.fromSendableValues(array);
```

## sendableRelationalStore.toSendableValues20+

PhonePC/2in1TabletTVWearable

toSendableValues(values: NonSendableValues): collections.Array<ValueType>

将不可跨线程传递的数组数据，转换为可跨线程传递的数组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [NonSendableValues](js-apis-data-sendablerelationalstore.md#nonsendablevalues20) | 是 | 不可跨线程传递的数组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| collections.Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 可跨线程传递的数组数据。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800000 | Inner error. |

**示例：**

```
1. import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
2. const array: relationalStore.ValueType[] = [];
3. array.push(1);
4. array.push(2);
5. array.push("aaaaaa")
6. const values = sendableRelationalStore.toSendableValues(array);
```

## Asset

PhonePC/2in1TabletTVWearable

记录资产附件（文件、图片、视频等类型文件）的相关信息。用于支持资产数据跨线程传递，继承自[lang.ISendable](js-apis-arkts-lang.md#langisendable)。资产类型的相关接口暂不支持Datashare。使用[sendableRelationalStore.toSendableAsset](js-apis-data-sendablerelationalstore.md#sendablerelationalstoretosendableasset)方法创建。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 资产的名称。 |
| uri | string | 否 | 否 | 资产的uri，在系统里的绝对路径。 |
| path | string | 否 | 否 | 资产在应用沙箱里的路径。 |
| createTime | string | 否 | 否 | 资产被创建出来的时间。 |
| modifyTime | string | 否 | 否 | 资产最后一次被修改的时间。 |
| size | string | 否 | 否 | 资产占用空间的大小。 |
| status | number | 否 | 是 | 资产的状态，取值与[relationalStore.AssetStatus](arkts-apis-data-relationalstore-e.md#assetstatus10)枚举值保持一致，默认值为relationalStore.AssetStatus.ASSET\_NORMAL。 |

## Assets

PhonePC/2in1TabletTVWearable

type Assets = collections.Array<Asset>

表示[Asset](js-apis-data-sendablerelationalstore.md#asset)类型数据的集合。用于支持Asset数据集合跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| [collections.Array](arkts-apis-arkts-collections-array.md)<[Asset](js-apis-data-sendablerelationalstore.md#asset)> | 用于并发场景的Asset附件数据集合。 |

## ValueType

PhonePC/2in1TabletTVWearable

type ValueType = null | number | string | boolean | collections.Uint8Array | Asset | Assets | collections.Float32Array | bigint

用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| null | 表示值类型为空。 |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |
| [collections.Uint8Array](arkts-apis-arkts-collections-uint8array.md) | 表示值类型为Uint8类型的数组。 |
| [Asset](js-apis-data-sendablerelationalstore.md#asset) | 表示值类型为附件Asset。  当字段类型是Asset时，在创建表的sql语句中，类型应当为：ASSET。 |
| [Assets](js-apis-data-sendablerelationalstore.md#assets) | 表示值类型为附件数据集合Assets。  当字段类型是Assets时，在创建表的sql语句中，类型应当为：ASSETS。 |
| [collections.Float32Array](arkts-apis-arkts-collections-float32array.md) | 表示值类型为浮点数组。  当字段类型是collections.Float32Array时，在创建表的sql语句中，类型应当为：floatvector(128)。 |
| bigint | 表示值类型为任意长度的整数。  当字段类型是bigint时，在创建表的sql语句中，类型应当为：UNLIMITED INT，详见[通过关系型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-rdb-store.md)。  **说明：**  bigint类型字段不能比较大小，不适用以下谓词操作：between、notBetween、greaterThan、lessThan、greaterThanOrEqualTo、lessThanOrEqualTo、orderByAsc、orderByDesc。  bigint类型字段的数据写入时，需通过BigInt()方法或在数据尾部添加'n'的方式明确为bigint类型，如'let data = BigInt(1234)'或'let data = 1234n'。  bigint字段如果写入number类型的数据，则查询该数据的返回类型为number，而非bigint。 |

## ValuesBucket

PhonePC/2in1TabletTVWearable

type ValuesBucket = collections.Map<string, ValueType>

表示[ValueType](js-apis-data-sendablerelationalstore.md#valuetype)数据的键值对存储，用于支持ValueType数据跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| [collections.Map](arkts-apis-arkts-collections-map.md)<string, [ValueType](js-apis-data-sendablerelationalstore.md#valuetype)> | 并发场景的键值对数据存储，其中，键的类型为string，值的类型为ValueType。 |

## NonSendableBucket

PhonePC/2in1TabletTVWearable

type NonSendableBucket = relationalStore.ValuesBucket

用于存储键值对的类型。不支持跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| [relationalStore.ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 非并发场景的键值对数据存储。 |

## NonSendableValues20+

PhonePC/2in1TabletTVWearable

type NonSendableValues = Array<relationalStore.ValueType>

表示[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)数据数组存储。不支持跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| Array<[relationalStore.ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 非并发场景的数组数据存储，值的类型为ValueType。 |

## NonSendableAsset

PhonePC/2in1TabletTVWearable

type NonSendableAsset = relationalStore.Asset

记录资产附件（文件、图片、视频等类型文件）的相关信息。不支持跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| [relationalStore.Asset](arkts-apis-data-relationalstore-i.md#asset10) | 非并发场景的资产附件数据存储。 |

## 跨线程传递使用示例

PhonePC/2in1TabletTVWearable

调用taskpool执行数据插入时，主线程调用toSendableValuesBucket方法将数据转为跨线程传递类型，传入taskpool处理。

调用taskpool执行数据查询时，调用ResultSet的getSendableRow方法，获取可跨线程传递的数据行返回主线程，主线程中调用fromSendableValuesBucket方法，转为常规ValuesBucket执行后续处理。

```
1. // Index.ets
2. import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
3. import { taskpool } from '@kit.ArkTS';

5. @Concurrent
6. async function insert(context: Context, dataItem: sendableRelationalStore.ValuesBucket) {
7. const CONFIG: relationalStore.StoreConfig = {
8. name: "Store.db",
9. securityLevel: relationalStore.SecurityLevel.S3,
10. };

12. let store = await relationalStore.getRdbStore(context, CONFIG);
13. console.info(`Get store successfully!`);

15. const CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS test (" +
16. "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
17. "name TEXT NOT NULL, " +
18. "age INTEGER, " +
19. "salary REAL, " +
20. "blobType BLOB)";
21. await store.executeSql(CREATE_TABLE_SQL);
22. console.info(`Create table test successfully!`);

24. // 数据插入
25. const rowId = await store.insertSync("test", dataItem);
26. await store.close();
27. return rowId;
28. }

30. @Concurrent
31. async function queryByName(context: Context, name: string) {
32. const CONFIG: relationalStore.StoreConfig = {
33. name: "Store.db",
34. securityLevel: relationalStore.SecurityLevel.S3,
35. };

37. let store = await relationalStore.getRdbStore(context, CONFIG);
38. console.info(`Get store successfully!`);

40. const predicates = new relationalStore.RdbPredicates("test");
41. predicates.equalTo("name", name);

43. const resultSet = await store.query(predicates);
44. if (resultSet.rowCount > 0 && resultSet.goToFirstRow()) {
45. // 获取可用于跨线程传递的ValuesBucket返回查询结果
46. return resultSet.getSendableRow();
47. }
48. return null;
49. }

52. @Entry
53. @Component
54. struct Index {
55. @State message: string = 'Hello World';

57. build() {
58. RelativeContainer() {
59. Text(this.message)
60. .id('HelloWorld')
61. .fontSize(50)
62. .fontWeight(FontWeight.Bold)
63. .alignRules({
64. center: { anchor: '__container__', align: VerticalAlign.Center },
65. middle: { anchor: '__container__', align: HorizontalAlign.Center }
66. })
67. .onClick(async () => {
68. let context: Context = this.getUIContext().getHostContext() as Context;

70. const item: relationalStore.ValuesBucket = {
71. name: "zhangsan",
72. age: 20,
73. salary: 5000
74. }
75. // 调用toSendableValuesBucket转换数据，用于跨线程传递。
76. const sendableItem = sendableRelationalStore.toSendableValuesBucket(item);
77. const insertRowId = await taskpool.execute(insert, context, sendableItem) as number;
78. console.info(`Insert data success, row id is: ${insertRowId}`);

80. const rowData = await taskpool.execute(queryByName, context, "zhangsan");
81. if (rowData) {
82. const row =
83. sendableRelationalStore.fromSendableValuesBucket(rowData as sendableRelationalStore.ValuesBucket);
84. console.info(`Query success, name is ${row['name']}, age is ${row['age']}.`);
85. } else {
86. console.error(`Query failed.`)
87. }
88. })
89. }
90. .height('100%')
91. .width('100%')
92. }
93. }
```
