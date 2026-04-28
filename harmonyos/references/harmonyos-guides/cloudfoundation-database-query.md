---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-query
title: 查询数据
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 查询数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f611a6f4db2f95c89176b10a3405dd816e92913107720f9a473fbcbe80bf5316
---

云数据库通过[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法查询对象，并提供了丰富的谓词查询，比如[equalTo()](../harmonyos-references/cloudfoundation-clouddatabase.md#equalto)、[notEqualTo()](../harmonyos-references/cloudfoundation-clouddatabase.md#notequalto)、[in()](../harmonyos-references/cloudfoundation-clouddatabase.md#in)等。通过单个或者多个链式过滤条件，开发者可以从存储区查询到满足特定条件的对象，也可以通过排序谓词对查询结果排序，或者通过限定查询返回数量谓词限定查询结果返回的数量。详细的查询条件请参见[DatabaseQuery](../harmonyos-references/cloudfoundation-clouddatabase.md#databasequery)。

应用会直接从云侧存储区服务器查询数据，本地不会缓存数据。

说明

* 每次的查询操作仅支持查询一个对象类型下的数据。
* 调用查询数据方法，有两种返回方式，返回一个Promise对象或者在参数中传入一个callback对象返回，下面以Promise为例详细说明。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[初始化数据库访问](cloudfoundation-database-initialize.md)。

## 简单查询

开发者可以在无查询条件时，获取一个对象类型中所有的对象；也可以指定单个查询条件，来获取满足该条件的对象。

* 查询对象类型BookInfo的所有数据。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. async queryAll() {
  4. try {
  5. let resultArray = await databaseZone.query(condition);
  6. hilog.info(0x0000, 'testTag', `Succeeded in querying data, result: ${JSON.stringify(resultArray)}`);
  7. } catch (err) {
  8. hilog.error(0x0000, 'testTag', `Failed to query data, code: ${err.code}, message: ${err.message}`);
  9. }
  10. }
  ```

  说明

  后续hilog都需要从@kit.PerformanceAnalysisKit中引入，将不在示例代码中呈现。
* 通过异步侦听的方式查询“bookName”参数对应的书籍。

  ```
  1. async queryBook(bookName: string): Promise<BookInfo> {
  2. try {
  3. condition.equalTo('bookName', bookName);
  4. let resultArray = await databaseZone.query(condition);
  5. let bookInfo = resultArray[0];
  6. hilog.info(0x0000, 'testTag', `Succeeded in querying data, result: ${JSON.stringify(resultArray)}`);
  7. return Promise.resolve(bookInfo);
  8. } catch (err) {
  9. hilog.error(0x0000, 'testTag', `Failed to query data, code: ${err.code}, message: ${err.message}`);
  10. return Promise.reject(err);
  11. }
  12. }
  ```

## 复合查询

开发者可以通过多个链式过滤条件，来获取满足条件的对象。多个链式条件之间默认用“与”运算。

* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询“bookName”包含“数据库”，“price”大于20.0并且小于50.0的书籍。

  ```
  1. condition.contains('bookName', '数据库')
  2. .greaterThan('price', 20.0)
  3. .and()
  4. .lessThan('price', 50.0);
  5. let resultArray = await databaseZone.query(condition);
  ```
* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询“bookName”包含“数据库”，“price”在小于20.0或者大于50.0区间的书籍。

  ```
  1. condition.contains('bookName', '数据库')
  2. .lessThan('price', 20.0)
  3. .or()
  4. .greaterThan('price', 50.0);
  5. let resultArray = await databaseZone.query(condition);
  ```
* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询“bookName”包含“史记”，“author”是“司马迁”，“price”大于60.0的书籍。

  ```
  1. condition.contains('bookName', '史记')
  2. .equalTo('author', '司马迁')
  3. .greaterThan('price', 60.0);
  4. let resultArray = await databaseZone.query(condition);
  ```
* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询“bookName”包含“自传”，并且“author”是“齐白石”，或者“author”是“司马迁”，并且“price”大于60.0的书籍。

  ```
  1. condition.contains('bookName', '自传')
  2. .beginGroup()
  3. .equalTo('author', '齐白石')
  4. .or()
  5. .equalTo('author', '司马迁')
  6. .endGroup()
  7. .greaterThan('price', 60.0);
  8. let resultArray = await databaseZone.query(condition);
  ```
* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询“bookName”包含“数据库”，并且“borrowerTime”在特定时间段内的书籍。其中，针对Date类型构造greaterThan()、greaterThanOrEqualTo()、lessThan()、lessThanOrEqualTo()、equalTo()、notEqualTo()查询条件时，需要调用getTime()方法将Date类型转换成number类型。

  ```
  1. let begin = (new Date("2025-12-29T08:00:00.000+08:00")).getTime();
  2. let end = (new Date("2025-12-31T08:00:00.000+08:00")).getTime();
  3. condition.contains('bookName', '数据库')
  4. .greaterThan('borrowerTime', begin)
  5. .and()
  6. .lessThan('borrowerTime', end);
  7. let resultArray = await databaseZone.query(condition);
  ```

## 数据排序

开发者可以通过[orderByAsc()](../harmonyos-references/cloudfoundation-clouddatabase.md#orderbyasc)或者[orderByDesc()](../harmonyos-references/cloudfoundation-clouddatabase.md#orderbydesc)实现对查询结果集中的对象按某个字段进行升序或者降序排列，排序谓词需要在其它查询谓词之后且在限定数据查询数量谓词之前。

```
1. condition.lessThan('price', 50.0)
2. .orderByDesc('price');
3. let resultArray = await databaseZone.query(condition);
```

## 随机查询

从6.0.1(21)版本开始，新增支持随机查询功能。

开发者可以通过[orderByRandom()](../harmonyos-references/cloudfoundation-clouddatabase.md#orderbyrandom)按随机顺序展示查询结果集中的对象。

该方法适用于推荐随机内容、播放随机音视频等场景。

```
1. condition.orderByRandom()
2. .limit(10);
3. let resultArray = await databaseZone.query(condition);
```

## 限定数据查询返回数量

在查询数据时，开发者可以通过[limit()](../harmonyos-references/cloudfoundation-clouddatabase.md#limit)限定查询返回数据的起始位置和数量，实现数据的分页。例如与排序查询谓词组合使用，可以实现获取top-N条数据。

对查询结果中的对象限定查询返回数量时，限定数据查询返回数量谓词在所有其他谓词查询之后。

* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询所有价格小于50.0的书籍，并且只显示最开始10条记录。

  ```
  1. condition.lessThan('price', 50.0)
  2. .limit(10);
  3. let resultArray = await databaseZone.query(condition);
  ```
* 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询所有价格小于50.0的书籍，并将查询结果按照降序排序，只显示价格排序从第6条开始的10条记录。

  ```
  1. condition.lessThan('price', 50.0)
  2. .orderByDesc('price')
  3. .limit(10, 6);
  4. let resultArray = await databaseZone.query(condition);
  ```

## 对查询结果进行算术计算

在查询数据时，可以通过[calculateQuery()](../harmonyos-references/cloudfoundation-clouddatabase.md#calculatequery)对查询结果对象中的某个字段进行算术计算并返回计算的结果。

构造查询条件，并调用[calculateQuery()](../harmonyos-references/cloudfoundation-clouddatabase.md#calculatequery)方法，查询所有价格小于50.0的书籍，并且计算所有书籍价格的平均值。

```
1. async calculateQuery() {
2. try {
3. condition.lessThan('price', 50.0);
4. let resultNum = await databaseZone.calculateQuery(condition, 'price', cloudDatabase.QueryCalculate.AVERAGE);
5. hilog.info(0x0000, 'testTag', `Succeeded in calculating queried data, result: ${JSON.stringify(resultNum)}`);
6. } catch (err) {
7. hilog.error(0x0000, 'testTag', `Failed to calculate queried data, code: ${err.code}, message: ${err.message}`);
8. }
9. }
```
