---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkendpointdescriptor
title: UsbDdkEndpointDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkEndpointDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fa847e6f84488bb9c67e955487360f2fd16790e9bbe3532429b537e56bc24bdc
---

```c
typedef struct UsbDdkEndpointDescriptor {...} UsbDdkEndpointDescriptor
```

## 概述

端点描述符，包含标准端点描述符和未做解析的描述符信息。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [struct UsbEndpointDescriptor](capi-usbddk-usbendpointdescriptor.md) endpointDescriptor | 标准端点描述符。 |
| const uint8\_t\* extra | 未做解析的描述符指针，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |
