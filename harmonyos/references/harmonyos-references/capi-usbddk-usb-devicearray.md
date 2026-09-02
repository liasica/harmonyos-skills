---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usb-devicearray
title: Usb_DeviceArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Usb_DeviceArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a882e599f033764fd8279c636ab328c608f7fa25b94d4e3d4102fc7f86c55e0f
---

```c
typedef struct Usb_DeviceArray {...} Usb_DeviceArray
```

## 概述

设备ID数组，用于存放[OH\_Usb\_GetDevices](capi-usb-ddk-api-h.md#oh_usb_getdevices)接口获取到的设备ID列表和设备数量。开发者申请设备ID数组，使用完结构体后需释放申请的内存，否则会造成资源泄漏。

**起始版本：** 18

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t\* deviceIds | 开发者申请好的设备ID数组首地址，申请的数组大小建议不超过128，以避免过度占用内存。 |
| uint32\_t num | 实际返回的设备数量，根据数量遍历deviceIds获得设备ID。当该值为0时，表示不存在USB设备。 |
