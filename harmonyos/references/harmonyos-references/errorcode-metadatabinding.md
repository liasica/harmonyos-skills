---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-metadatabinding
title: 记忆链接错误码
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > 错误码 > 记忆链接错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ebc658f3d75840ffcc38552d85436a87ffb15cd822c39e22fd1158a172601763
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

## 32100001 文件创建失败

**错误信息**

Internal handling failed.

**错误描述**

当调用记忆链接模块接口时，若文件创建失败，会报此错误码。

**可能原因**

服务状态异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试，返回原始图片文件。

## 32100004 订阅失败

**错误信息**

Subscription Failed. Possible causes: 1. Abnormal system capability. 2. IPC communication abnormality. 3. Algorithm loading exception.

**错误描述**

当调用metadataBinding模块on接口时，若订阅失败，会报此错误码。

**可能原因**

订阅异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试。

## 32100005 取消订阅失败

**错误信息**

Unsubscription Failed. Possible causes: 1. Abnormal system capability. 2. IPC communication abnormality.

**错误描述**

当调用metadataBinding模块off接口时，若取消订阅失败，会报此错误码。

**可能原因**

取消订阅异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试。
