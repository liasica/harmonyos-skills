---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbmanager-oh-usbmanager-usbinterface
title: OH_UsbManager_UsbInterface
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > OH_UsbManager_UsbInterface
category: harmonyos-references
scraped_at: 2026-11-12T09:55:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:857dd1bf67212f5ade4e677439ecf2e2613eb03a403025779d06e448bce9919c
---

```c
typedef struct OH_UsbManager_UsbInterface {...} OH_UsbManager_UsbInterface
```

## 概述

定义USB接口。一个[OH\_UsbManager\_UsbConfig](capi-usbmanager-oh-usbmanager-usbconfig.md)可以包含多个OH\_UsbManager\_UsbInterface实例，每个实例提供特定功能。

**起始版本：** 26.0.1

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb\_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t id | USB接口的唯一标识。  **起始版本：** 26.0.1 |
| uint8\_t protocol | 接口协议。  **起始版本：** 26.0.1 |
| uint8\_t clazz | 接口类。  **起始版本：** 26.0.1 |
| uint8\_t subClass | 接口子类。  **起始版本：** 26.0.1 |
| uint8\_t alternateSetting | 此USB接口的交替设置编号，由USB接口描述符定义。值0表示默认的交替设置。  **起始版本：** 26.0.1 |
| const char \*name | 接口名称。  **起始版本：** 26.0.1 |
| [OH\_UsbManager\_UsbEndpoint](capi-usbmanager-oh-usbmanager-usbendpoint.md) \*endpoints | 属于该USB接口的端点。  **起始版本：** 26.0.1 |
| uint32\_t endpointCount | 接口中的端点数量。  **起始版本：** 26.0.1 |
