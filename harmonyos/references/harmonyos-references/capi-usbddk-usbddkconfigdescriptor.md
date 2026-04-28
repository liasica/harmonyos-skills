---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkconfigdescriptor
title: UsbDdkConfigDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkConfigDescriptor
category: harmonyos-references
scraped_at: 2026-04-28T08:10:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b9349c7b1a4908bad48a40d078108372e0ecffb66e8eadc4284e1759991020ce
---

```
1. typedef struct UsbDdkConfigDescriptor {...} UsbDdkConfigDescriptor
```

## 概述

PC/2in1

配置描述符。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| struct UsbConfigDescriptor configDescriptor | 标准配置描述符。 |
| struct UsbDdkInterface\* interface | 该配置所包含的接口。 |
| const uint8\_t\* extra | 未做解析的描述符，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |
