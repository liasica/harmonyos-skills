---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkendpointdescriptor
title: UsbDdkEndpointDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkEndpointDescriptor
category: harmonyos-references
scraped_at: 2026-04-29T14:01:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b00fc6c93ff91874b7569adc2f0682ee7067ea00aa4b7714e266fd4b8f3166c3
---

```
1. typedef struct UsbDdkEndpointDescriptor {...} UsbDdkEndpointDescriptor
```

## 概述

PC/2in1

端点描述符。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [struct UsbEndpointDescriptor](capi-usbddk-usbendpointdescriptor.md) endpointDescriptor | 标准端点描述符。 |
| const uint8\_t\* extra | 未做解析的描述符，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |
