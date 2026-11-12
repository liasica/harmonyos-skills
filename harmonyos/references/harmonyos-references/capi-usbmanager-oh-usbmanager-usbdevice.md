---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbmanager-oh-usbmanager-usbdevice
title: OH_UsbManager_UsbDevice
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > OH_UsbManager_UsbDevice
category: harmonyos-references
scraped_at: 2026-11-12T09:55:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5929a6ab33392cf6d03cf38b7ac7c5ba77a3f9cd6db8e25c6cde15af2afdb395
---

```c
typedef struct OH_UsbManager_UsbDevice {...} OH_UsbManager_UsbDevice
```

## 概述

定义USB设备的扁平化表示。

**起始版本：** 26.0.1

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb\_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t busNum | USB设备的总线编号。  **起始版本：** 26.0.1 |
| uint8\_t devAddress | 设备在总线上的地址。  **起始版本：** 26.0.1 |
| const char \*name | 设备名称，格式为<总线编号>-<设备地址>。  **起始版本：** 26.0.1 |
| const char \*manufacturerName | 制造商名称。  **起始版本：** 26.0.1 |
| const char \*productName | 产品名称。  **起始版本：** 26.0.1 |
| const char \*version | 设备版本。  **起始版本：** 26.0.1 |
| uint16\_t vendorId | 厂商ID。  **起始版本：** 26.0.1 |
| uint16\_t productId | 产品ID。  **起始版本：** 26.0.1 |
| uint8\_t clazz | 设备类。  **起始版本：** 26.0.1 |
| uint8\_t subClass | 设备子类。  **起始版本：** 26.0.1 |
| uint8\_t protocol | 设备协议。  **起始版本：** 26.0.1 |
| [OH\_UsbManager\_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md) \*configs | 设备配置描述符信息。  **起始版本：** 26.0.1 |
| uint32\_t configCount | 设备中的配置数量。  **起始版本：** 26.0.1 |
