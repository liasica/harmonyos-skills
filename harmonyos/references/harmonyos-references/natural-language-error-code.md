---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-error-code
title: ArkTS API错误码
breadcrumb: API参考 > AI > Natural Language Kit（自然语言理解服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:18:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d96d6f232bf4fb2bd66d82ca58bca60743ae2aa9e65957eef3cdc0a6f32da543
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 200 运行超时

PhonePC/2in1Tablet

**错误信息**

Run timed out, please try again later.

**错误描述**

运行超时，请重试。

**可能原因**

当前存在大量的请求，无法及时处理。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

## 1011200001 运行失败

PhonePC/2in1Tablet

**错误信息**

Failed to run, please try again.

**错误描述**

运行失败，请重试。

**可能原因**

输入不符合要求，或服务存在异常。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

## 1011200002 服务异常

PhonePC/2in1Tablet

**错误信息**

The service is abnormal.

**错误描述**

服务异常时，系统会产生此错误码。

**可能原因**

服务异常。

**处理步骤**

系统异常，建议重启设备重试。
