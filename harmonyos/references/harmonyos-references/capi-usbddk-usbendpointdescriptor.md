---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbendpointdescriptor
title: UsbEndpointDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbEndpointDescriptor
category: harmonyos-references
scraped_at: 2026-04-28T08:10:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f073db681215aa829c3b54c12e1db44de49e5341d553c141cbf6468ece6c3657
---

```
1. typedef struct UsbEndpointDescriptor {...} __attribute__((packed)) UsbEndpointDescriptor
```

## 概述

PC/2in1

标准端点描述符，对应USB协议中Standard Endpoint Descriptor。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t bLength | 该描述符的大小，单位为字节。 |
| uint8\_t bDescriptorType | 描述符类型。 |
| uint8\_t bEndpointAddress | 端点地址，包含端点编号以及端点方向。 |
| uint8\_t bmAttributes | 端点属性，包括传输类型、同步类型、使用类型。 |
| uint16\_t wMaxPacketSize | 该端点所能承载的最大包的大小。 |
| uint8\_t bInterval | 数据传输轮询端点的时间间隔。 |
| uint8\_t bRefresh | 用于音频类设备，同步反馈的速率。 |
| uint8\_t bSynchAddress | 用于音频类设备，同步端点的地址。 |
