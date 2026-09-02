---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterface
title: UsbDdkInterface
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbDdkInterface
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c21b563731e69083fd0acc9fc23c6ba30c917e249d34fabeead14126907d5102
---

```c
typedef struct UsbDdkInterface {...} UsbDdkInterface
```

## 概述

USB接口，是特定接口下备用设置的集合。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t numAltsetting | USB接口的备用设置数量。 |
| [struct UsbDdkInterfaceDescriptor](capi-usbddk-usbddkinterfacedescriptor.md)\* altsetting | USB接口的备用设置数组的指针，数组的长度由numAltsetting指定。 |
