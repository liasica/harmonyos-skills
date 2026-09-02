---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk
title: UsbDdk
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 模块 > UsbDdk
category: harmonyos-references
scraped_at: 2026-09-02T14:52:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8a6d627fe5269fe6b89bfc39524772757f12e7243cf6ba70fb28bc360b33c8e
---

## 概述

提供USB DDK接口，包括主机侧打开和关闭接口、管道同步异步读写通信、控制传输、中断传输等，适用于需要与USB设备进行底层交互和数据通信的场景，帮助开发者实现高效的USB设备驱动开发。

**系统能力：** SystemCapability.Driver.USB.Extension

**起始版本：** 10

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [usb\_ddk\_api.h](capi-usb-ddk-api-h.md) | 声明用于主机侧访问设备的USB DDK接口，提供USB设备管理、配置和数据传输等功能，帮助开发者实现与USB设备的底层交互和数据通信。 |
| [usb\_ddk\_types.h](capi-usb-ddk-types-h.md) | 提供USB DDK中的枚举类型与结构体定义，包括USB设备描述、控制传输、请求管道等核心数据结构，帮助开发者便捷地进行驱动开发。 |
