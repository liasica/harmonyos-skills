---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-error-code
title: ArkTS API错误码
breadcrumb: API参考 > AI > Agent Framework Kit（智能体框架服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:18:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94aa790534ac5517b98fb58462f94572c24e4144dcbf4f756c154844a6b93013
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1022400010 参数错误

PhoneTablet

**错误信息**

Parameter error.

**错误描述**

输入参数错误。

**可能原因**

输入参数的取值超出支持的范围，或规格。

**处理步骤**

检查输入参数是否符合要求，确保无误后再次尝试。

## 1022400011 隐私协议未授权

PhoneTablet

**错误信息**

Privacy agreement not accepted.

**错误描述**

隐私未经授权。

**可能原因**

未同意小艺隐私协议。

**处理步骤**

重新点击Agent按钮，打开小艺页面时同意隐私协议。

## 1022400012 未登录华为账户

PhoneTablet

**错误信息**

HUAWEI ID not signed in.

**错误描述**

未登录华为账号。

**可能原因**

未登录华为账号。

**处理步骤**

重新登录设备上的华为账号。

## 1022400013 网络错误

PhoneTablet

**错误信息**

Internet error.

**错误描述**

网络异常。

**可能原因**

设备未连接至网络或处于弱网环境。

**处理步骤**

连接网络后，重新尝试。

## 1022400014 内部错误

PhoneTablet

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

内部连接失败，当前小艺版本不支持。

**处理步骤**

建议到应用市场下载最新版的小艺app。
