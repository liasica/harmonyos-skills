---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-file
title: 引入对象类型文件
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 引入对象类型文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58a2567e489f6fa6ce48c9f43e44592f7b52e6e74e8d8f826a4e43e960731def
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[新增对象类型](cloudfoundation-database-add-object.md)。
* 已[新增存储区](cloudfoundation-database-add-zone.md)。

## 操作步骤

1. 将对象类型中导出的json格式文件命名为schema.json，拷贝到DevEco Studio项目的“AppScope/resources/rawfile”或者“entry/src/main/resources/rawfile”目录下。在编译构建过程中，AppScope目录下的资源文件会合入到模块的资源文件中，详细信息请参见[资源分类](resource-categories-and-access.md#资源分类)。
2. 按照AGC控制台上创建的对象类型“BookInfo”在代码工程中创建BookInfo.ets文件，文件内容参考以下代码。

   说明

   在AGC控制台创建的字段类型与ArkTS数据类型的匹配关系如下：

   * String、Text对应string。
   * Boolean对应boolean。
   * Byte、ByteArray对应Uint8Array。
   * Short、Integer、Long、Float、Double、IntAutoIncrement、LongAutoIncrement对应number。
   * Date对应Date。

   ```
   1. import { cloudDatabase } from '@kit.CloudFoundationKit';

   3. class BookInfo extends cloudDatabase.DatabaseObject{
   4. public naturalbase_ClassName(): string {
   5. return "BookInfo";
   6. }
   7. public id: number | undefined;
   8. public bookName: string | undefined;
   9. public author: string | undefined;
   10. public price: number | undefined;
   11. public borrowerId: number | undefined;
   12. public borrowerName: string | undefined;
   13. public borrowerTime: Date | undefined;
   14. }

   16. export { BookInfo };
   ```
