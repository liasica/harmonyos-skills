---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hiretrieval
title: 应用灰度错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > 应用灰度错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa6f9e5c2375735115496f3aa75a60e305dce60453488c88a70aa3a86eeb2df7
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 36000001

**错误信息**

Initialization error. Possibly caused by invoking this function before invoking init function.

**错误描述**

应用灰度初始化异常。

**可能原因**

没有完成应用灰度的初始化。

**处理步骤**

在调用该接口之前，先调用[hiRetrieval.init()](js-apis-hiretrieval.md#hiretrievalinit)接口完成应用灰度的初始化。

## 36000002

**错误信息**

Multi-instance applications not supported error. Possibly caused by invoking this function in a multi-instance application.

**错误描述**

多实例应用调用[hiRetrieval.init()](js-apis-hiretrieval.md#hiretrievalinit)接口异常（当前仅init()接口会抛出此错误码）。

**可能原因**

当前版本暂不支持多实例应用调用应用灰度的能力。

**处理步骤**

请确认当前应用是否为[多实例应用](../harmonyos-guides/multiinstance.md)。若为多实例应用，请避免调用HiRetrieval相关接口。
