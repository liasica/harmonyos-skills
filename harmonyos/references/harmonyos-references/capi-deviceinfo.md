---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-deviceinfo
title: DeviceInfo
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 模块 > DeviceInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:52:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d369d5871f27862622f19ab869caf38f4fb53cf36a922dbcc5763615d3ece1d2
---

## 概述

提供查询终端设备信息的API。该模块提供了获取设备类型、制造商、品牌、型号、版本信息等设备基础信息的能力，适用于需要根据设备特性进行适配、统计设备信息或进行设备管理的场景。这些API通过读取系统属性获取设备信息，返回值为指向常量字符串的指针。该指针指向系统内部存储的数据，调用者无需释放内存。

**起始版本：** 10

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [deviceinfo.h](capi-deviceinfo-h.md) | 该模块提供了获取设备类型、制造商、品牌、型号、版本信息等设备基础信息的能力，适用于需要根据设备特性进行适配、统计设备信息或进行设备管理的场景。这些API通过读取系统属性获取设备信息，返回值为指向常量字符串的指针。该指针指向系统内部存储的数据，调用者无需释放内存。 |
