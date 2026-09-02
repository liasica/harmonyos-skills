---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-query
title: 查询数据
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 查询数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:16e7ad5fb6cb1e3e1932a357c30ba4032628095de7f7f5133b47cb47510e04a3
---

云数据库通过[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法查询对象，并提供了丰富的谓词查询，比如[equalTo()](../harmonyos-references/cloudfoundation-clouddatabase.md#equalto)、[notEqualTo()](../harmonyos-references/cloudfoundation-clouddatabase.md#notequalto)、[in()](../harmonyos-references/cloudfoundation-clouddatabase.md#in)等。通过单个或者多个链式过滤条件，开发者可以从存储区查询到满足特定条件的对象，也可以通过排序谓词对查询结果排序，或者通过限定查询返回数量谓词限定查询结果返回的数量。详细的查询条件请参见[DatabaseQuery](../harmonyos-references/cloudfoundation-clouddatabase.md#databasequeryt-extends-databaseobject)。

应用会直接从云侧存储区服务器查询数据，本地不会缓存数据。

**说明** 

* 每次的查询操作仅支持查询一个对象类型下的数据。
* 调用查询数据方法，有两种返回方式，返回一个Promise对象或者在参数中传入一个callback对象返回，下面以Promise为例详细说明。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[初始化数据库访问](cloudfoundation-database-initialize.md)。

## 简单查询

开发者可以在无查询条件时，获取一个对象类型中所有的对象；也可以指定单个查询条件，来获取满足该条件的对象。

1. 导入相关模块。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';
   import { BookInfo } from '../model/BookInfo';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 查询对象类型BookInfo的所有数据。

   ```typescript
   let condition = new cloudDatabase.DatabaseQuery(BookInfo);
   databaseZone.query(condition).then((resultArray: BookInfo[]) => {
     resultArray.forEach((value) => {
       hilog.info(0x0000, 'cloudDb',
         `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
     });
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
   });
   ```

## 按条件查询

开发者可以通过多个链式过滤条件，来获取满足条件的对象。多个链式条件之间默认用“与”运算。

1. 导入相关模块。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';
   import { BookInfo } from '../model/BookInfo';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 按条件查询数据。

   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍名称为“Jane Eyre”的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);

     condition.equalTo('bookName', 'Jane Eyre');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍名称不为“Jane Eyre”的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.notEqualTo('bookName', 'Jane Eyre');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍名称以“Jane”开始的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.beginsWith('bookName', 'Jane');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍名称以“Eyre”结束的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.endsWith('bookName', 'Eyre');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍名称中包含“d”的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.contains('bookName', 'd');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格大于82的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.greaterThan('price', 82.0);
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格小于82的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.lessThan('price', 82.0);
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格大于或等于82的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.greaterThanOrEqualTo('price', 82.0);
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格小于或等于82的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.lessThanOrEqualTo('price', 82.0);
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍名称被包含在['demo', 'Jane Eyre']中的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.in('bookName', ['demo', 'Jane Eyre']);
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格为空的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.isNull('price');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格不为空的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.isNotNull('price');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格在10到50之间的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.beginGroup()
       .greaterThan('price', 10.0)
       .lessThan('price', 50.0)
       .endGroup();
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询按照价格升序排列的书籍。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.orderByAsc('price');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询价格不超过50且按照价格降序排列的书籍。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.lessThan('price', 50.0).orderByDesc('price');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格小于50或者书籍名称等于“demo”的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.lessThan('price', 50.0).or().equalTo('bookName', 'demo');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询书籍价格大于40并且书籍名称中包含“j”的数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.greaterThan('price', 40.0).and().contains('bookName', 'j');
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```
   * 构造查询条件，并调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法，查询价格不超过50且按照价格降序排列的书籍，最多展示两条数据。

     ```typescript
     let condition = new cloudDatabase.DatabaseQuery(BookInfo);
     condition.lessThan('price', 50.0).orderByDesc('price').limit(2, 0);
     databaseZone.query(condition).then((resultArray: BookInfo[]) => {
       resultArray.forEach((value) => {
         hilog.info(0x0000, 'cloudDb',
           `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
       });
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
     });
     ```

## 对查询结果进行算术计算

1. 导入相关模块。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';
   import { BookInfo } from '../model/BookInfo';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 开发者可以通过[calculateQuery()](../harmonyos-references/cloudfoundation-clouddatabase.md#calculatequery)对查询结果对象中的某个字段进行算术计算并返回计算的结果。

   ```typescript
   let condition = new cloudDatabase.DatabaseQuery(BookInfo);
   condition.lessThan('price', 50.0);
   databaseZone.calculateQuery(condition, 'price', cloudDatabase.QueryCalculate.AVERAGE).then((num: number) => {
     hilog.info(0x0000, 'cloudDb', `Succeeded in querying: QueryCalculate.AVERAGE price  = ${num}`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
   });
   ```

## 随机查询

从6.0.1(21)版本开始，新增支持随机查询功能。

1. 导入相关模块。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';
   import { BookInfo } from '../model/BookInfo';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 开发者可以通过[orderByRandom()](../harmonyos-references/cloudfoundation-clouddatabase.md#orderbyrandom)按随机顺序展示查询结果集中的对象。

   该方法适用于推荐随机内容、播放随机音视频等场景。

   ```typescript
   let condition = new cloudDatabase.DatabaseQuery(BookInfo);
   condition.orderByRandom().limit(10);
   databaseZone.query(condition).then((resultArray: BookInfo[]) => {
     resultArray.forEach((value) => {
       hilog.info(0x0000, 'cloudDb',
         `Succeeded in querying: bookName = ${value.bookName}    price: ${value.price?.toString()}`);
     });
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'cloudDb', `Failed to query, code: ${err.code}, message: ${err.message}`);
   });
   ```
