---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-certmanager
title: 证书管理错误码
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 错误码 > 证书管理错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:07:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:25fe1525ec4775852fed670fc796e837b62274f0f59a3b91dcfc3e0ff98859ac
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 17500001 内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error.

**可能原因**

调用API时发生内部错误。

**处理步骤**

检查内部运行情况是否正常。

## 17500002 证书不存在

PhonePC/2in1TabletTVWearable

**错误信息**

The certificate does not exist.

**可能原因**

证书管理过程中发现证书不存在。

**处理步骤**

检查证书是否存在。

## 17500003 证书或凭据无效

PhonePC/2in1TabletTVWearable

**错误信息**

The keystore is in an invalid format or the keystore password is incorrect.

**可能原因**

输入不是有效的证书或凭据。

**处理步骤**

检查证书或凭据的有效性。

## 17500004 证书或凭据数量达到上限

PhonePC/2in1TabletTVWearable

**错误信息**

The number of certificates or credentials reaches the maximum allowed.

**可能原因**

已安装的证书或凭据数量达到最大值。

**处理步骤**

清理过期的证书或凭据。

## 17500005 应用未经用户授权

PhonePC/2in1TabletTVWearable

**错误信息**

The application is not authorized by the user.

**可能原因**

用户没有将输入的凭据授权给当前应用使用。

**处理步骤**

检查输入的凭据是否正确或当前应用申请授权。

## 17500007 设备进入坚盾守护模式

PhonePC/2in1TabletTVWearable

**错误信息**

The device enters advanced security mode.

**可能原因**

用户已开启坚盾守护模式。

**处理步骤**

需要在应用界面提醒用户关闭坚盾守护模式。

## 17500009 不支持指定的证书存储路径

PhonePC/2in1TabletTVWearable

**错误信息**

The device does not support the specified certificate store path.

**可能原因**

设备不支持指定的证书存储路径。

**处理步骤**

检查输入的证书类型是否正确。

## 17500010 访问USB证书凭据失败

PhonePC/2in1TabletTVWearable

**错误信息**

The USB key service access failed.

**可能原因**

USB硬件驱动服务发生异常。

**处理步骤**

检查USB是否正常连接或USB驱动是否正常工作。

## 17500011 入参校验失败

PhonePC/2in1TabletTVWearable

**错误信息**

The input parameters validation failed.

**可能原因**

参数格式异常或参数范围无效。

**处理步骤**

检查接口入参格式或范围。
