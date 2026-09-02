---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie
title: HiCollie
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 模块 > HiCollie
category: harmonyos-references
scraped_at: 2026-09-02T14:52:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:84a91d9098a3e5e541ecb6fb0ee5e1acf21ee0129e0150024caa4c4e13c6ed5e
---

## 概述

提供检测业务线程卡死、卡顿，以及上报卡死事件的能力。本模块函数支持以下功能：

（1）注册应用业务线程卡死的周期性检测任务；

（2）注册应用业务线程卡顿检测的回调函数；

（3）上报应用业务线程卡死事件。

使用场景：应用卡顿问题定位、线程健康状态监控、开发调试阶段的卡死问题诊断、卡顿数据采集与分析。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiCollie

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [hicollie.h](capi-hicollie-h.md) | HiCollie模块提供检测业务线程卡死、卡顿，以及上报卡死事件的能力。 |
