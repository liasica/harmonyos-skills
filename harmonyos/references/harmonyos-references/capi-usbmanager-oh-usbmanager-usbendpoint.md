---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbmanager-oh-usbmanager-usbendpoint
title: OH_UsbManager_UsbEndpoint
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > OH_UsbManager_UsbEndpoint
category: harmonyos-references
scraped_at: 2026-11-12T09:55:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:379cfbe6369dbffcecdd723444d4dc2b402350c6bed43be0a15687568f3a57d0
---

```c
typedef struct OH_UsbManager_UsbEndpoint {...} OH_UsbManager_UsbEndpoint
```

## 概述

定义用于发送或接收数据的USB端点。端点从[OH\_UsbManager\_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md)获取。

**起始版本：** 26.0.1

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb\_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t address | 端点地址。  **起始版本：** 26.0.1 |
| uint8\_t attributes | 端点属性。  **起始版本：** 26.0.1 |
| uint8\_t interval | 端点数据传输间隔。对于中断端点，单位为毫秒。对于等时端点，单位取决于设备速度。  **起始版本：** 26.0.1 |
| uint16\_t maxPacketSize | 端点上数据包的最大大小，单位：字节。  **起始版本：** 26.0.1 |
| [OH\_UsbManager\_RequestDirection](capi-ohusb-manager-h.md#oh_usbmanager_requestdirection) direction | 端点方向。  **起始版本：** 26.0.1 |
| uint8\_t number | 端点号。  **起始版本：** 26.0.1 |
| uint8\_t type | 端点类型。  **起始版本：** 26.0.1 |
| uint8\_t interfaceId | 端点所属接口的唯一标识。  **起始版本：** 26.0.1 |
