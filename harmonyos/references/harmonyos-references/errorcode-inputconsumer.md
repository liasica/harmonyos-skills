---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputconsumer
title: 全局快捷键管理错误码
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > 错误码 > 全局快捷键管理错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:10:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:834133763a296cf8b14a279ade9d9dd1ce554023a89e27ada0e91ed32dce7776
---

说明

* 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 4200002 快捷键被系统注册

PhonePC/2in1TabletTVWearable

**错误信息**

The hotkey has been used by the system.

**错误描述**

快捷键已经被系统应用注册，会产生此错误码。

**可能原因**

1. 快捷键已经被系统应用注册。

**处理步骤**

1. 可以通过[getAllSystemHotkeys](js-apis-inputconsumer.md#inputconsumergetallsystemhotkeys)接口查询所有的系统快捷键。

## 4200003 快捷键已经被三方注册

PhonePC/2in1TabletTVWearable

**错误信息**

The hotkey has been subscribed to by another.

**错误描述**

快捷键被其他三方应用注册，会产生此错误码。

**可能原因**

1. 快捷键已经被其他三方应用注册。

**处理步骤**

1. 在cmd命令窗口执行(hidumper -s 3101 -a -s)查询已经被注册的快捷键，注册未被三方占用的快捷键。

## 3800001 多模输入服务内部错误

PhoneTV

**错误信息**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**错误描述**

多模输入服务内部错误。

**可能原因**

内存分配失败，线程繁忙，服务异常退出等非预期错误。

**处理步骤**

建议稍后重试。
