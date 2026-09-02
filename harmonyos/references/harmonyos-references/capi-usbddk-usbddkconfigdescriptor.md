---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkconfigdescriptor
title: UsbDdkConfigDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkConfigDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fde02c1becee59b202a640b73dfc6f57dcc15763c7707b75b8d14181339958e7
---

```c
typedef struct UsbDdkConfigDescriptor {...} UsbDdkConfigDescriptor
```

## 概述

配置描述符，包含标准配置描述符和接口描述符等信息。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [struct UsbConfigDescriptor](capi-usbddk-usbconfigdescriptor.md) configDescriptor | 标准配置描述符。 |
| [struct UsbDdkInterface](capi-usbddk-usbddkinterface.md)\* interface | 该配置所包含的接口。 |
| const uint8\_t\* extra | 未做解析的描述符指针，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |
