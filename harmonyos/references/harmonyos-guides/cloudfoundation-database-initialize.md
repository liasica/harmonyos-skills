---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-initialize
title: 初始化数据库访问
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 初始化数据库访问
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a56bd51085d283caa112354ec46a0cb1f9fdb18b50c70b6d7c573a589452bf47
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[引入对象类型文件](cloudfoundation-database-add-file.md)。

## 操作步骤

1. 设置云数据库配置项。

   在“entry/src/main/module.json5”文件中添加网络权限。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.INTERNET"
   4. }
   5. ]
   ```
2. （可选）如果存在需要登录应用才能操作数据库的场景（如新增或删除数据），您需要执行如下操作：

   1. [通过AuthProvider获取用户凭据](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)。
   2. 调用[cloudCommon.init()](../harmonyos-references/cloudfoundation-cloudcommon.md#cloudcommoninit)方法进行初始化时，传入获取的凭据。
3. 在业务代码中，使用AGC开发平台上创建的存储区“QuickStartDemo”类初始化DatabaseZone。

   ```
   1. import { cloudDatabase } from '@kit.CloudFoundationKit';

   3. let databaseZone = cloudDatabase.zone('QuickStartDemo');
   ```

   说明

   * cloudDatabase.zone方法接收的入参为“存储区名称”，即cloudDBZoneName，请参见[新增存储区](cloudfoundation-database-add-zone.md)章节。
   * 存储区最多创建4个，超过4个会导致云数据库访问失败。
4. 如果需要使用数据库查询方法，可以使用类（此处以BookInfo为例）初始化DatabaseQuery。

   ```
   1. import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的相对路径

   3. let condition = new cloudDatabase.DatabaseQuery(BookInfo);
   ```

   说明

   后续“databaseZone”、“condition”都需要在每个查询中独立使用，可以参考此章节创建，下文代码中不再重复创建的操作。
