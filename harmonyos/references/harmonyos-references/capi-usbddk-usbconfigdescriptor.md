---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbconfigdescriptor
title: UsbConfigDescriptor
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbConfigDescriptor
category: harmonyos-references
scraped_at: 2026-04-28T08:10:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7db32df5ffd6da3b36b5263343601db21afbede7aba5b9a55dfd77a6337a6b2b
---

```
1. typedef struct UsbConfigDescriptor {...} __attribute__((packed)) UsbConfigDescriptor
```

## 概述

PC/2in1

标准配置描述符，对应USB协议中Standard Configuration Descriptor。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint8\_t bLength | 该描述符的大小，单位为字节。 |
| uint8\_t bDescriptorType | 描述符类型。 |
| uint16\_t wTotalLength | 该配置描述符的总长度，包含配置、接口、端点和特定于类或供应商的描述符。 |
| uint8\_t bNumInterfaces | 该配置所支持的接口数量。 |
| uint8\_t bConfigurationValue | 设置配置所需要的参数，用来选择当前配置。 |
| uint8\_t iConfiguration | 描述该配置的字符串描述符的索引。 |
| uint8\_t bmAttributes | 配置属性，包含供电模式，远程唤醒等配置。 |
| uint8\_t bMaxPower | 总线供电的USB设备的最大功耗，以2mA为单位。 |
