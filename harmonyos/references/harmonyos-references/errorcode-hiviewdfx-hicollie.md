---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hicollie
title: HiCollie错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > HiCollie错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2b7012fe378d1e8a778aa8d4978be63b9c98529d30100316257739b51216a210
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 29800001 系统服务获取失败

**错误信息**

Wrong thread context. The function cannot be called from main thread.

**错误描述**

在错误的线程中调用接口。

**可能原因**

该接口服务无法从主线程调用。

**处理步骤**

在非主线程调用该接口服务。

## 29800002 远程调用失败

**错误信息**

Remote call failed.

**错误描述**

当前接口请求远程服务失败。

**可能原因**

服务未启动或崩溃。

**处理步骤**

建议重试。

## 29800003 无效的timer名称

**错误信息**

Invalid timer name.

**错误描述**

timer name是无效的。

**可能原因**

传入的字符指针name为nullptr或name指向空字符串。

**处理步骤**

检查传入的name参数，确保其为非空字符指针，且指向非空字符串。

## 29800004 无效的timeout值

**错误信息**

Invalid timeout value.

**错误描述**

timeout值是无效的。

**可能原因**

传入的timeout的值为0。

**处理步骤**

检查传入的timeout，确保其大于0。

## 29800005 错误的进程上下文

**错误信息**

Wrong process context.

**错误描述**

进程上下文错误。

**可能原因**

接入函数执行时长检测定时器的进程是appspawn或nativespawn进程。

**处理步骤**

请勿在appspawn和nativespawn进程中接入hicollie检测。

## 29800006 错误的timer id参数

**错误信息**

Wrong timer id output param.

**错误描述**

错误的timer id值参数。

**可能原因**

* 传入的整型指针id为nullptr；
* 接入函数执行时长检测机制的进程中hicollie插件同时存在任务数达到最大值128。

**处理步骤**

* 检查传入的id参数，确保其为非空整型指针；
* 如果达到最大值限制，请减少该进程中hicollie检测机制的在其他地方的调用后重试。
