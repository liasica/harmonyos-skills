---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-certmanagerdialog
title: 证书管理对话框错误码
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 错误码 > 证书管理对话框错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:07:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:855684093038e3a9eea5a0f5a3ec3eba19861bb35a9b010e1dafdbbf887a7b8a
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 29700001 内部错误

PhonePC/2in1Tablet

**错误信息**

Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error.

**可能原因**

调用API时发生内部错误。

**处理步骤**

检查内部运行情况是否正常。

## 29700002 操作取消

PhonePC/2in1Tablet

**错误信息**

The user cancels the installation operation.

**可能原因**

调用API时用户取消操作。

**处理步骤**

无需处理。

## 29700003 证书安装失败错误

PhonePC/2in1Tablet

**错误信息**

The user install certificate failed in the certificate manager dialog, such as the certificate is in an invalid format.

**可能原因**

调用API安装证书时失败，可能是由于证书格式错误。

**处理步骤**

检查证书格式，数据等是否正常。

## 29700004 设备类型不支持

PhonePC/2in1Tablet

**错误信息**

The API is not supported on this device.

**可能原因**

调用API时当前设备非PC设备。

**处理步骤**

更换PC设备调用此API。

## 29700005 操作不符合设备安全策略

PhonePC/2in1Tablet

**错误信息**

The operation does not comply with the device security policy, such as the device does not allow users to manage the ca certificate of the global user.

**可能原因**

调用API时当前设备非企业设备。

**处理步骤**

更换企业设备调用此API。

## 29700006 入参校验失败

PhonePC/2in1Tablet

**错误信息**

The input parameters validation failed.

**可能原因**

参数格式异常或参数范围无效。

**处理步骤**

检查接口入参格式或范围。

## 29700007 无可用授权证书

PhonePC/2in1Tablet

**错误信息**

No Available certificate for authorization

**可能原因**

没有可用的授权证书。

**处理步骤**

安装有效证书凭据。
