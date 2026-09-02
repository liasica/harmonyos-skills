---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-cloudfoundation
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Cloud Foundation Kit（云开发服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44267582ec53b65bab86e6926c0af6627226feecee9c092a9a91fa5121927eb0
---

**说明** 

以下仅介绍本模块特有错误码。若返回通用错误码，请参考[通用错误码](errorcode-universal.md)处理。

## 1008210001 云函数网络连接错误

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

**错误信息**

Client internal error.

**错误描述**

云函数客户端内部错误。

**可能原因**

1. 真机场景下，如错误信息中包含“create http task error”，可能是签名方式错误，或者网络问题导致签名验证失败。
2. 模拟器场景下，如错误信息中包含“create http task error”，可能是未注册模拟器调试凭据。
3. 系统内部错误。

**处理步骤**

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](../harmonyos-guides/ide-signing-auto.md#section6333421192714)和[手动签名](../harmonyos-guides/ide-signing-manual.md)两种方式。
2. 请检查设备网络连接情况。
3. 请参考[使用模拟器调试](../harmonyos-guides/cloudfoundation-emulator.md)进行排查。
4. 若以上排查结果均无异常，请稍后重试。

## 1008211001 云函数服务器侧错误

**错误信息**

Server error.

**错误描述**

云函数服务器侧出现错误。

**可能原因**

云函数服务器出现异常，或认证失败。

**处理步骤**

请结合错误信息，参考[云函数服务器侧错误码](../AppGallery-connect-References/errorcode-nodejs-0000001733038624.md)进行排查。

## 1008220001 云存储网络连接错误

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

**错误信息**

Client internal error.

**错误描述**

云存储客户端内部错误。

**可能原因**

1. 真机场景下，如错误信息中包含“create http task error”，可能是签名方式错误，或者网络问题导致签名验证失败。
2. 模拟器场景下，如错误信息中包含“create http task error”，可能是未注册模拟器调试凭据。
3. 系统内部错误。

**处理步骤**

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](../harmonyos-guides/ide-signing-auto.md#section6333421192714)和[手动签名](../harmonyos-guides/ide-signing-manual.md)两种方式。
2. 请检查设备网络连接情况。
3. 请参考[使用模拟器调试](../harmonyos-guides/cloudfoundation-emulator.md)进行排查。
4. 若以上排查结果均无异常，请稍后重试。

## 1008221001 云存储服务器侧错误

**错误信息**

Server error.

**错误描述**

云存储服务器侧错误。

**可能原因**

云存储客户端请求的服务器侧文件不存在，服务器侧安全规则配置不正确，或认证失败等。

**处理步骤**

1. 请参考[云存储模块常见问题](../harmonyos-guides/cloudfoundation-faq-1.md)进行排查。
2. 请结合错误信息，参考[云存储服务器侧错误码](../AppGallery-connect-References/0000001057683679-0000001056723660.md)进行排查。

## 1008230001 云数据库网络连接错误

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

**错误信息**

Client internal error.

**错误描述**

云数据库客户端内部错误。

**可能原因**

1. 真机场景下，如错误信息中包含“create http task error”，可能是签名方式错误，或者网络问题导致签名验证失败。
2. 模拟器场景下，如错误信息中包含“create http task error”，可能是未注册模拟器调试凭据。
3. 系统内部错误。

**处理步骤**

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](../harmonyos-guides/ide-signing-auto.md#section6333421192714)和[手动签名](../harmonyos-guides/ide-signing-manual.md)两种方式。
2. 请检查设备网络连接情况。
3. 请参考[使用模拟器调试](../harmonyos-guides/cloudfoundation-emulator.md)进行排查。
4. 若以上排查结果均无异常，请稍后重试。

## 1008230002 云数据库schema配置错误

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

**错误信息**

Natural object error.

**错误描述**

云数据库代码对象错误。

**可能原因**

查询代码中传入的存储对象名称和实际是否相符。

**处理步骤**

检查传入存储对象名称参数和实际存储对象名称是否一致。

## 1008231001 云数据库服务器侧错误

**错误信息**

Server error.

**错误描述**

云数据库服务器侧出现错误。

**可能原因**

云数据库服务器出现异常，或认证失败。

**处理步骤**

请结合错误信息，参考[云数据库服务器侧错误码](../AppGallery-connect-Guides/agc-clouddb-error-code-0000001117436042.md)进行排查。

## 1008240009 预加载客户端内部错误

**错误信息**

Client internal error.

**错误描述**

预加载客户端内部错误。

**可能原因**

1. 如错误信息中包含“preload not support”，可能是设备类型不支持预加载。
2. 如错误信息中包含“preload no data”，可能是预加载无缓存数据。
3. 如错误信息中包含“preload failed”，可能是系统内部错误。

**处理步骤**

1. 请检查设备类型。当前预加载模块仅支持Phone、Tablet、PC/2in1设备。
2. 请参考[预加载模块常见问题](../harmonyos-guides/cloudfoundation-faq-5.md)进行排查。
3. 若以上排查结果均无异常，请稍后重试。
