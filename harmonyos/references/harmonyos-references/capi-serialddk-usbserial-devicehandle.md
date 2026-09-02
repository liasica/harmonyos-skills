---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-devicehandle
title: UsbSerial_Device
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbSerial_Device
category: harmonyos-references
scraped_at: 2026-09-02T14:52:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf1effdef8511fa9b3ebe1b7018cd3222074548bf4dc9d449a0c2e7961167b42
---

```c
typedef struct UsbSerial_Device UsbSerial_Device
```

## 概述

USB串口设备数据结构（不透明），用于表示USB串口设备。开发者应通过[OH\_UsbSerial\_Open](capi-usb-serial-api-h.md#oh_usbserial_open)接口函数获取此结构体实例。

**起始版本：** 18

**相关模块：** [USBSerialDDK](capi-serialddk.md)

**所在头文件：** [usb\_serial\_types.h](capi-usb-serial-types-h.md)
