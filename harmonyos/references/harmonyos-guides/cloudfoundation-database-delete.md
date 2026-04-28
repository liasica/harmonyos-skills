---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-delete
title: 删除数据
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 删除数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4897c5c692f24f8a6df840e4971c0190706405a372f085cedf71163124468fc4
---

开发者可以通过[delete()](../harmonyos-references/cloudfoundation-clouddatabase.md#delete)删除单个对象或者一组对象。删除数据时，云数据库会根据传入对象主键删除相应的数据，不会比对该对象其它属性与存储的数据是否一致。删除一组对象时，删除操作是原子性的，即对象列表中的对象要么全部删除成功，要么全部删除失败。

说明

* 删除一组对象时，该组中的对象必须属于同一个对象类型，否则会导致删除失败。
* 调用删除数据方法，有两种返回方式，返回一个Promise对象或者在参数中传入一个callback对象返回，本文以Promise为例详细说明。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[初始化数据库访问](cloudfoundation-database-initialize.md)。

## 删除数据

**代码示例：**

将对象删除，如果删除成功，返回删除对象的个数；执行失败，抛出异常。

```
1. // 假设图书遗失，图书管理员需要将遗失的书籍从BookInfo表中删除
2. async delete() {
3. try {
4. let book = new BookInfo();
5. book.id = 3;
6. let deleteNum = await databaseZone.delete(book);
7. hilog.info(0x0000, 'testTag', `Succeeded in deleting data, result: ${JSON.stringify(deleteNum)}`);
8. } catch (err) {
9. hilog.error(0x0000, 'testTag', `Failed to delete data, code: ${err.code}, message: ${err.message}`);
10. }
11. }
```
