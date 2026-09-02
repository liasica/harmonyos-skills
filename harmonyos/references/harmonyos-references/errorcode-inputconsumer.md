---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputconsumer
title: 全局快捷键管理错误码
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > 错误码 > 全局快捷键管理错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fc7f39aa6820828d6a5aad0d365135f6fa3afb46884730e7470f5db2325f1cf9
---

**说明** 

* 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 4200002 快捷键被系统注册

**错误信息**

The hotkey has been used by the system.

**错误描述**

快捷键已经被系统应用注册，会产生此错误码。

**可能原因**

快捷键已经被系统应用注册。

**处理步骤**

可以通过[getAllSystemHotkeys](js-apis-inputconsumer.md#inputconsumergetallsystemhotkeys)接口查询所有的系统快捷键。

## 4200003 快捷键已经被其他应用注册

**错误信息**

The hotkey has been subscribed to by another.

**错误描述**

快捷键被其他应用注册，会产生此错误码。

**可能原因**

快捷键已经被其他应用注册。

**处理步骤**

在cmd命令窗口执行(hidumper -s 3101 -a -s)查询已经被注册的快捷键，注册未被其他应用占用的快捷键。

## 3800001 多模输入服务内部错误

**错误信息**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**错误描述**

多模输入服务内部错误。

**可能原因**

内存分配失败，线程繁忙，服务运行异常等非预期错误。

**处理步骤**

建议稍后重试。
