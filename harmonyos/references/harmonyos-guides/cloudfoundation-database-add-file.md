---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-file
title: 引入对象类型文件
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 引入对象类型文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:b482eb7f41f2597b61cfe2d7d5f7ec4d4eb3ff4b0685f9a4e114b712dc94b8f6
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[新增对象类型](cloudfoundation-database-add-object.md)。
* 已[新增存储区](cloudfoundation-database-add-zone.md)。

## 操作步骤

1. 将对象类型中导出的json格式文件命名为schema.json，拷贝到DevEco Studio项目的“AppScope/resources/rawfile”或者“entry/src/main/resources/rawfile”目录下。在编译构建过程中，AppScope目录下的资源文件会合入到模块的资源文件中，详细信息请参见[资源分类](resource-categories-and-access.md#资源分类)。
2. 按照AGC控制台上创建的对象类型“BookInfo”在代码工程“entry/src/main/ets/model”目录下创建BookInfo.ets文件，文件内容参考以下代码。

   **说明** 

   在AGC控制台创建的字段类型与ArkTS数据类型的匹配关系如下：

   * String、Text对应string。
   * Boolean对应boolean。
   * Byte、ByteArray对应Uint8Array。
   * Short、Integer、Long、Float、Double、IntAutoIncrement、LongAutoIncrement对应number。
   * Date对应Date。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';

   class BookInfo extends cloudDatabase.DatabaseObject {
     public naturalbase_ClassName(): string {
       return 'BookInfo';
     }

     public id: number | undefined;
     public bookName: string | undefined;
     public author: string | undefined;
     public price: number | undefined;
     public borrowerId: number | undefined;
     public borrowerName: string | undefined;
     public borrowerTime: Date | undefined;
   }

   export { BookInfo };
   ```
