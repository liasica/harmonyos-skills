---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-cloudfoundation
title: ArkTS错误码
breadcrumb: API参考 > 应用服务 > Cloud Foundation Kit（云开发服务） > ArkTS API > ArkTS错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:32+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c73a4a8f4aa1dc111770497da0a39bd2613f097989ca2fe4123ce13c66ceaf43
---

说明

以下仅介绍本模块特有错误码。若返回通用错误码，请参考[通用错误码](errorcode-universal.md)处理。若错误信息中返回了其他错误码，请参考下述链接处理：

* [云函数](../AppGallery-connect-References/errorcode-nodejs-0000001733038624.md)
* [云存储](../AppGallery-connect-References/0000001057683679-0000001056723660.md)
* [云数据库](../AppGallery-connect-Guides/agc-clouddb-error-code-0000001117436042.md)

## 1008210001 云函数网络连接错误

PhonePC/2in1TabletTVWearable

**错误信息**

Network connection error.

**错误描述**

云函数网络连接错误。

**可能原因**

1. 网络连接配置了代理服务器。
2. 当前设备无网络。

**处理步骤**

检查设备网络连接情况。

## 1008210009 云函数客户端内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

Client internal error.

**错误描述**

云函数客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

## 1008211001 云函数服务器侧错误

PhonePC/2in1TabletTVWearable

**错误信息**

Server error.

**错误描述**

云函数服务器侧出现错误。

**可能原因**

云函数服务器出现异常，或认证失败。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

## 1008220001 云存储网络连接错误

PhonePC/2in1TabletTVWearable

**错误信息**

Network connection error.

**错误描述**

云存储网络连接错误。

**可能原因**

1. 网络连接配置了代理服务器。
2. 当前设备无网络。

**处理步骤**

检查设备网络连接情况。

## 1008220009 云存储客户端内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

Client internal error.

**错误描述**

云存储客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

## 1008221001 云存储云侧执行错误

PhonePC/2in1TabletTVWearable

**错误信息**

Server error.

**错误描述**

云存储云侧执行错误。

**可能原因**

云存储客户端请求的云侧文件不存在，云侧安全规则配置不正确，或认证失败等。

**处理步骤**

根据错误信息，检查云侧资源以及请求是否正确。

## 1008230001 云数据库网络连接错误

PhonePC/2in1TabletTVWearable

**错误信息**

Network connection error.

**错误描述**

云数据库网络连接错误。

**可能原因**

1. 网络连接配置了代理服务器。
2. 当前设备无网络。

**处理步骤**

检查设备网络连接情况。

## 1008230009 云数据库客户端内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

Client internal error.

**错误描述**

云数据库客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

## 1008230002 云数据库schema配置错误

PhonePC/2in1TabletTVWearable

**错误信息**

Schema config error.

**错误描述**

云数据库schema.json文件配置错误。

**可能原因**

1. schema.json文件不存在或者路径错误。
2. schema.json文件中的存储对象和代码中创建的存储对象不一致，可能是云侧存储对象发生了变更，但schema.json文件未重新导出。
3. schema.json文件同时存在于AppScope目录和entry目录中。当开发者在entry目录下的schema.json文件中更新了存储对象，在编译构建过程中，这些更新会被AppScope目录下的 schema.json文件覆盖。详细信息请参见[资源分类](../harmonyos-guides/resource-categories-and-access.md#资源分类)。

**处理步骤**

1. 将schema.json文件下载后放在rawfile目录下。
2. 参见[引入对象类型文件](../harmonyos-guides/cloudfoundation-database-add-file.md)，确保schema.json文件中对象和代码中创建的存储对象一致。
3. 将entry目录下的schema.json文件移动到AppScope目录下进行维护。

## 1008230003 云数据库代码对象错误

PhonePC/2in1TabletTVWearable

**错误信息**

Natural object error.

**错误描述**

云数据库代码对象错误。

**可能原因**

查询代码中传入的存储对象名称和实际是否相符。

**处理步骤**

检查传入存储对象名称参数和实际存储对象名称是否一致。

## 1008231001 云数据库服务器侧错误

PhonePC/2in1TabletTVWearable

**错误信息**

Server error.

**错误描述**

云数据库服务器侧出现错误。

**可能原因**

云数据库服务器出现异常，或认证失败。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。

## 1008240009 预加载客户端内部错误

PhonePC/2in1Tablet

**错误信息**

Client internal error.

**错误描述**

预加载客户端内部错误。

**可能原因**

客户端内部错误。

**处理步骤**

请通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101723605535783370&keyWord=Cloud Foundation Kit&channel=ICS0000)联系技术支持人员定位问题。
