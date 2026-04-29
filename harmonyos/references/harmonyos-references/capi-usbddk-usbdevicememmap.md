---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbdevicememmap
title: UsbDeviceMemMap
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDeviceMemMap
category: harmonyos-references
scraped_at: 2026-04-29T14:01:32+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8d0238f829e7feb5a13214cff6ed8a84760552bdef49886651e3eb599716056f
---

```
1. typedef struct UsbDeviceMemMap {...} UsbDeviceMemMap
```

## 概述

PC/2in1

设备内存映射，通过[OH\_Usb\_CreateDeviceMemMap](capi-usb-ddk-api-h.md#oh_usb_createdevicememmap)创建设备内存映射，使用内存映射后的缓冲区，可提升数据传输性能。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* const address | 映射后的缓冲区地址。 |
| const size\_t size | 缓冲区大小。 |
| uint32\_t offset | 所使用的缓冲区的偏移量，默认为0，表示没有偏移，从映射后的缓冲区地址address开始。 |
| uint32\_t bufferLength | 所使用的缓冲区的长度，默认等于缓冲区大小 size，表示使用全部的缓冲区。 |
| uint32\_t transferedLength | 实际传输的数据的长度。 |
