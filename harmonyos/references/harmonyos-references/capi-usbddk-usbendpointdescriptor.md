---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbendpointdescriptor
title: UsbEndpointDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbEndpointDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5d46cfda0f15747ee2570f2354e80ea1d9b53aa10186e65f3d6bbf3ea6cbc5dd
---

```c
typedef struct UsbEndpointDescriptor {...} __attribute__((packed)) UsbEndpointDescriptor
```

## 概述

标准端点描述符，对应USB协议中Standard Endpoint Descriptor。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t bLength | 该描述符的大小，单位：Byte。 |
| uint8\_t bDescriptorType | 描述符类型。 |
| uint8\_t bEndpointAddress | 端点地址，包含端点编号以及端点方向。 |
| uint8\_t bmAttributes | 端点属性，包括传输类型、同步类型和使用类型。 |
| uint16\_t wMaxPacketSize | 该端点所能承载的最大包的大小，单位：Byte。 |
| uint8\_t bInterval | 数据传输时轮询端点的时间间隔。 |
| uint8\_t bRefresh | 用于音频类设备，同步反馈的速率。 |
| uint8\_t bSynchAddress | 用于音频类设备，同步端点的地址。 |
