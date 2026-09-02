---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk
title: USBSerialDDK
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 模块 > USBSerialDDK
category: harmonyos-references
scraped_at: 2026-09-02T14:52:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:475fe1ba5b878f74635c4c9a0f8181a4a0e9d11c6fea540a357909393b068378
---

## 概述

提供USB Serial DDK（USB串口驱动开发工具包）接口，包括枚举类型和USB Serial DDK API使用的数据结构。串口通信常见于工业用途及一些老旧设备，如：发卡机、身份证读卡器等。开发者通过使用USB Serial DDK，可以开发USB串口外设扩展驱动。

**系统能力：** SystemCapability.Driver.UsbSerial.Extension

**起始版本：** 18

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [usb\_serial\_api.h](capi-usb-serial-api-h.md) | 声明用于主机侧通过USB接口访问串口设备的USB Serial DDK接口，提供串口读写操作和参数配置的能力，适用于工业控制、嵌入式设备通信等需要通过USB访问串口设备的场景。 |
| [usb\_serial\_types.h](capi-usb-serial-types-h.md) | 提供USB Serial DDK中的枚举类型与结构体的定义，用于USB串口驱动开发，简化串口设备参数配置、返回码处理和流量控制等操作，提升驱动开发效率。 |
