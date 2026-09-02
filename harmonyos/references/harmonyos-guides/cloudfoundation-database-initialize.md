---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-initialize
title: 初始化数据库访问
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 初始化数据库访问
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:21570ea636badd292fbdf7a701ee4b45c0939d510a0474e60f058a90dcc33729
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[引入对象类型文件](cloudfoundation-database-add-file.md)。

## 操作步骤

1. 设置云数据库配置项。

   在“entry/src/main/module.json5”文件中添加网络权限。

   ```typescript
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     }
   ]
   ```
2. （可选）如果存在需要登录应用才能操作数据库的场景（如新增或删除数据），您需要执行如下操作：

   1. [通过AuthProvider获取用户凭据](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)。
   2. 调用[init()](../harmonyos-references/cloudfoundation-cloudcommon.md#init)方法进行初始化时，传入获取的凭据。
3. 导入相关模块。

   ```typescript
   import { cloudDatabase } from '@kit.CloudFoundationKit';
   import { BookInfo } from '../model/BookInfo';
   ```
4. 在业务代码中，使用AGC开发平台上创建的存储区“QuickStartDemo”初始化DatabaseZone。

   ```typescript
   let databaseZone = cloudDatabase.zone('QuickStartDemo');
   ```

   **说明** 

   * 后续“databaseZone”都需要在每个查询中独立使用，可以参考此章节创建，下文代码中不再重复创建的操作。
   * cloudDatabase.zone方法接收的入参为“存储区名称”，即cloudDBZoneName，请参见[新增存储区](cloudfoundation-database-add-zone.md)章节。
   * 存储区最多创建4个，超过4个会导致云数据库访问失败。
5. 如果需要使用数据库查询方法，可以使用类（此处以BookInfo为例）初始化DatabaseQuery。

   ```typescript
   let condition = new cloudDatabase.DatabaseQuery(BookInfo);
   ```
