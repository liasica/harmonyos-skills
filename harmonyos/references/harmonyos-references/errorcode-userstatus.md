---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-userstatus
title: 用户状态感知错误码
breadcrumb: API参考 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > 错误码 > 用户状态感知错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:10:56+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:b9802bd49bc2fa89ab674bb79e9aafd55ea871342359671f57189c5272118429
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

## 33900001 服务异常

PhonePC/2in1Tablet

**错误信息**

Service exception. Possible causes:

1. System error, such as a null pointer and container-related exception.

2. Node-API invocation exception, such as invalid Node-API status.

**错误描述**

当调用userStatus模块on、off接口时，若服务异常，会报此错误码。

**可能原因**

服务状态异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试，期间可优先尝试获取器件列表方式进一步获取设备可用性。

## 33900002 订阅失败

PhonePC/2in1Tablet

**错误信息**

Subscription failed. Possible causes:

1. Callback registration failed.

2. Failed to bind the native object to the JS wrapper.

3. Node-API invocation exception, such as invalid Node-API status.

4. IPC request exception.

**错误描述**

当调用userStatus模块on接口时，若订阅失败，会报此错误码。

**可能原因**

订阅异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试。

## 33900003 取消订阅失败

PhonePC/2in1Tablet

**错误信息**

Unsubscription failed. Possible causes:

1. Callback failure.

2. Node-API invocation exception, such as invalid Node-API status.

3. IPC request exception.

**错误描述**

当调用userStatus模块off接口时，若取消订阅失败，会报此错误码。

**可能原因**

取消订阅异常。

**处理步骤**

1. 定时重试操作，如间隔1s或者按照指数增长间隔重试。
2. 连续重试3次不可用则停止尝试。
