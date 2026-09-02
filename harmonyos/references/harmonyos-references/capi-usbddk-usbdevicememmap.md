---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbdevicememmap
title: UsbDeviceMemMap
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDeviceMemMap
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ffe59594d1b042ae42150178f6bc330ea0cb43427505460ef16e15e230bbfced
---

```c
typedef struct UsbDeviceMemMap {...} UsbDeviceMemMap
```

## 概述

设备内存映射，通过[OH\_Usb\_CreateDeviceMemMap](capi-usb-ddk-api-h.md#oh_usb_createdevicememmap)创建，使用映射后的缓冲区可提升数据传输性能。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* const address | 映射后的缓冲区地址。 |
| const size\_t size | 缓冲区大小（单位：Byte），必须大于 0。 |
| uint32\_t offset | 所使用的缓冲区的偏移量，默认为0，表示没有偏移。偏移从缓冲区地址address开始计算，offset和bufferLength之和必须小于等于缓冲区大小size。 |
| uint32\_t bufferLength | 所使用的缓冲区的长度，默认等于缓冲区大小 size，表示使用全部的缓冲区。offset和bufferLength之和必须小于等于缓冲区大小size。 |
| uint32\_t transferedLength | 实际传输的数据长度（单位：Byte）。 |
