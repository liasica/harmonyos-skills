---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk
title: USBSerialDDK
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 模块 > USBSerialDDK
category: harmonyos-references
scraped_at: 2026-04-28T08:10:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4db37d4601673f930b4cbb4b8a0e6e50f0a314e655cdb26e99d39d526569e95f
---

## 概述

PC/2in1

提供USB Serial DDK接口，包括枚举类型和USB Serial DDK API使用的数据结构。工业用途及一些老旧设备会使用到串口通信，如：发卡机、身份证读卡器等。通过构建USB Serial DDK，支持外设扩展驱动基于USB Serial DDK开发非标外设扩展驱动。

**系统能力：** SystemCapability.Driver.UsbSerial.Extension

**起始版本：** 18

## 文件汇总

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [usb\_serial\_api.h](capi-usb-serial-api-h.md) | 声明用于主机侧访问串口设备的USB Serial DDK接口。 |
| [usb\_serial\_types.h](capi-usb-serial-types-h.md) | 提供USB Serial DDK中的枚举变量、结构体定义与宏定义。 |
