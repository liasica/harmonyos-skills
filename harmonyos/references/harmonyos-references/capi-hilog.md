---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hilog
title: HiLog
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 模块 > HiLog
category: harmonyos-references
scraped_at: 2026-04-28T08:11:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9705cc9b92ab93db91f437965fe1d192b48e800165c26db1fed2f5f6b500c3ba
---

## 概述

PhonePC/2in1TabletTVWearable

HiLog模块实现日志打印功能。开发者可以通过使用这些接口实现日志相关功能，输出日志时可以指定日志类型、所属业务领域、日志TAG标识、日志级别等。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 8

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [log.h](capi-log-h.md) | HiLog模块日志接口定义，通过这些接口实现日志打印相关功能。用户输出日志时，先定义日志所属业务领域、日志TAG，然后按照类型、级别选择对应API，指定参数隐私标识输出日志内容。  业务领域：指定日志所对应的业务领域，用户自定义使用，用于标识业务的子系统、模块。16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。  日志TAG：字符串常量，用于标识调用所在的类或者业务。  日志级别：DEBUG、INFO、WARN、ERROR、FATAL。  参数格式：类printf的%方式，包括格式字符串（包括参数类型标识）和变参。  隐私参数标识：在格式字符串每个参数中%符号后类型前增加{public}、{private}标识。注意：每个参数未指定隐私标识时，缺省为隐私。 |
