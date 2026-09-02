---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hilog
title: HiLog
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 模块 > HiLog
category: harmonyos-references
scraped_at: 2026-09-02T14:52:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7e7f838b40578b5cdd3438890904e322593528f65f885ca278ba35e058387aa
---

## 概述

HiLog模块是HarmonyOS提供的C/C++日志记录模块，用于在应用运行过程中输出结构化日志信息。开发者可以通过使用这些接口实现日志相关功能，输出日志时可以指定日志类型、所属业务领域、日志TAG标识、日志级别等。

使用场景： 开发者在应用开发过程中需要记录运行日志用于问题定位、流程追踪和行为分析时使用本模块接口。通过DEBUG级别日志记录调试日志，跟踪业务流程和运行状态；通过INFO级别日志记录非正常情况下的业务关键节点信息，比如无网络信号或登录失败；在出现异常或错误时，通过WARN、ERROR、FATAL级别日志记录故障信息，快速定位问题根因。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 8

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [log.h](capi-log-h.md) | HiLog模块日志接口定义，通过这些接口实现日志打印相关功能。用户输出日志时，先定义日志所属业务领域、日志TAG，然后按照日志类型、日志级别选择对应API，指定参数隐私标识输出日志内容。  业务领域：指定日志所对应的业务领域，用户自定义，用于标识业务的子系统、模块。16进制整数，范围0x0~0xFFFF，超出范围时日志接口不会输出日志内容。  日志TAG：字符串常量，用于标识调用所在的类或者业务。TAG最多支持31字节，超限将被截断，不建议使用中文以避免乱码和对齐问题。  日志级别：DEBUG、INFO、WARN、ERROR、FATAL。各级别说明可查阅[log.h](capi-log-h.md)。  参数格式：类printf的%方式，包括格式字符串（包括参数类型标识）和变参。  隐私参数标识：在格式字符串每个参数中%符号后类型前可选择性地增加{public}、{private}标识。每个参数未指定隐私标识时，缺省为隐私。 |
