---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbmanager-oh-usbmanager-usbconfig
title: OH_UsbManager_UsbConfig
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > OH_UsbManager_UsbConfig
category: harmonyos-references
scraped_at: 2026-11-12T09:55:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:87bb37b88af7802ca1508f2fef4cc1bad27131b5bbdca23d980ceac36a09d75e
---

```c
typedef struct OH_UsbManager_UsbConfig {...} OH_UsbManager_UsbConfig
```

## 概述

定义USB配置。一个[OH\_UsbManager\_UsbDevice](capi-usbmanager-oh-usbmanager-usbdevice.md)可以包含多个

**OH\_UsbManager\_UsbConfig**实例。

**起始版本：** 26.0.1

**相关模块：** [UsbManager](capi-usbmanager.md)

**所在头文件：** [ohusb\_manager.h](capi-ohusb-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t id | USB配置的唯一标识。  **起始版本：** 26.0.1 |
| uint8\_t attributes | 配置属性。  **起始版本：** 26.0.1 |
| uint8\_t maxPower | 最大功耗，单位：mA。  **起始版本：** 26.0.1 |
| const char \*name | 配置名称，可以为空。  **起始版本：** 26.0.1 |
| bool isRemoteWakeup | 是否支持远程唤醒。true表示支持远程唤醒；false表示不支持。  **起始版本：** 26.0.1 |
| bool isSelfPowered | 是否支持独立供电。true表示支持独立供电；false表示不支持。  **起始版本：** 26.0.1 |
| [OH\_UsbManager\_UsbInterface](capi-usbmanager-oh-usbmanager-usbinterface.md) \*interfaces | 支持的接口属性。  **起始版本：** 26.0.1 |
| uint32\_t interfaceCount | 配置中的接口数量。  **起始版本：** 26.0.1 |
