---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbmanager-oh-usbmanager-usbpipe
title: OH_UsbManager_UsbPipe
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > OH_UsbManager_UsbPipe
category: harmonyos-references
scraped_at: 2026-11-12T09:55:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9e1eac7d3da0fccb43c4e521c91c92e20f8da193927d9c46a7db9ff1a2d3cb7e
---

```c
typedef struct OH_UsbManager_UsbPipe {...} OH_UsbManager_UsbPipe
```

## 概述

定义用于与已打开设备通信的USB设备管道。

**起始版本：** 26.0.1

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb\_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t busNum | 所连接设备的总线编号。  **起始版本：** 26.0.1 |
| uint8\_t devAddress | 所连接设备的设备地址。  **起始版本：** 26.0.1 |
