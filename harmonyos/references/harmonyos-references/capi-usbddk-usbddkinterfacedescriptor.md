---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterfacedescriptor
title: UsbDdkInterfaceDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkInterfaceDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:27a236885472f48c5ee5f58722e06bddaf66b9e8e522227932cc6ef51609d788
---

```c
typedef struct UsbDdkInterfaceDescriptor {...} UsbDdkInterfaceDescriptor
```

## 概述

接口描述符，包含标准接口描述符和端点描述符等信息。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [struct UsbInterfaceDescriptor](capi-usbddk-usbinterfacedescriptor.md) interfaceDescriptor | 标准接口描述符。 |
| [struct UsbDdkEndpointDescriptor](capi-usbddk-usbddkendpointdescriptor.md)\* endPoint | 该接口所包含的端点描述符，可为空指针表示无端点（不包含控制端点0）。 |
| const uint8\_t\* extra | 未做解析的描述符指针，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |
