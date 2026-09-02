---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk
title: HidDdk
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 模块 > HidDdk
category: harmonyos-references
scraped_at: 2026-09-02T14:52:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bbaaba6d5715c1f8a4da57d4c927ba95ed479f5128fdb213f5767d8bd26592d2
---

## 概述

提供HID DDK接口，包括创建设备、发送事件、销毁设备等功能，用于HID设备的驱动开发。

**系统能力：** SystemCapability.Driver.HID.Extension

**起始版本：** 11

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [hid\_ddk\_api.h](capi-hid-ddk-api-h.md) | 声明主机侧访问输入设备的HID DDK（Driver Development Kit，驱动开发工具包）接口。该模块提供了创建、打开、读写HID设备的能力，支持设备管理和事件注入，支持两种使用模式：一是虚拟HID设备的创建与事件注入，适用于模拟键盘、鼠标、触摸屏输入等场景；二是真实HID设备的访问与通信，支持打开、读写设备报告以及获取设备信息，适用于与HID设备进行数据交互的场景。 |
| [hid\_ddk\_types.h](capi-hid-ddk-types-h.md) | 提供HID DDK中的枚举变量与结构体定义，支持开发者在驱动开发中定义和操作HID设备，适用于与鼠标、键盘、触摸屏等输入设备交互的场景，提供了设备特性、事件类型、键值编码、坐标轴等完整定义，帮助开发者快速实现HID设备的驱动开发。 |
