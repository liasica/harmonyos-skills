---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-metadatabinding
title: 记忆链接错误码
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > 错误码 > 记忆链接错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:10:56+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:426d1ed62a555a9a2da7e4f68c64deb86ee4ba870b04044c0dcac4bd2a5bbf0b
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

## 32100001 文件创建失败

PhoneTablet

**错误信息**

Internal handling failed.

**错误描述**

当调用记忆链接模块接口时，若服务异常，会报此错误码。

**可能原因**

服务状态异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试，返回原始图片文件。

## 32100004 订阅失败

PhoneTablet

**错误信息**

Subscription failed. Possible causes: 1. Abnormal system capability; 2. IPC exception; 3. Algorithm loading exception.

**错误描述**

当调用metadataBinding模块on接口时，若订阅失败，会报此错误码。

**可能原因**

订阅异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试。

## 32100005 取消订阅失败

PhoneTablet

**错误信息**

Unsubscription failed. Possible causes: 1. Abnormal system capability; 2. IPC exception.

**错误描述**

当调用metadataBinding模块off接口时，若取消订阅失败，会报此错误码。

**可能原因**

取消订阅异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试。
