---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-upsert
title: 写入数据
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 写入数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0cae7daa91ca3a86307ee1e236efa8f8feffbbb72120690c0f0da76ad04f570f
---

开发者可以通过[upsert()](../harmonyos-references/cloudfoundation-clouddatabase.md#upsert)将一个或者一组对象写入到当前存储区中。在写入对象时，如果在存储区已经存在主键相同的对象，则更新已有的对象；如果不存在，则写入一个新的对象。写入的数据可以来自于新建对象，或者从存储区查询出来的对象。

**说明** 

* 写入一组对象时，数据的写入操作是原子性的，即对象列表中的对象要么全部成功写入，要么全部失败。
* 写入一组对象时，该组中的对象必须属于同一个对象类型，否则会导致写入失败。
* 写入一组对象时，数据总大小不能超过2MB，否则会导致写入失败。
* 写入一组对象时，数据总条数不能超过1000条，否则会导致写入失败。
* 写入一组对象时，“String”类型的数据最大长度为200个字符，“Text”类型的数据最大长度为100000000个字符。
* 调用写入数据方法，有两种返回方式，返回一个Promise对象或者在参数中传入一个callback对象返回，下面以Promise为例详细说明。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[初始化数据库访问](cloudfoundation-database-initialize.md)。

## 写入数据

Promise对象中封装了写入操作执行的结果，通过该Promise对象可以异步侦听执行结果：如果执行成功，可以获取写入的对象数量；如果执行失败，可以获取错误信息。

1. 导入相关模块。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';
   import { BookInfo } from '../model/BookInfo';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 将BookInfo对象写入至存储区中，写入成功后，返回写入的数量；写入失败，抛出异常。

   ```typescript
   let book = new BookInfo();
   book.id = 11;
   book.bookName = 'Jane Eyre'
   book.price = 100.0;
   book.borrowerTime = new Date();
   databaseZone.upsert(book).then((record: number) => {
     hilog.info(0x0000, 'cloudDb', `Succeeded in upserting: ${record}`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'cloudDb', `Failed to upsert, code: ${err.code}, message: ${err.message}`);
   });
   ```
