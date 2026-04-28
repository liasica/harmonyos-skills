---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usb-devicearray
title: Usb_DeviceArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Usb_DeviceArray
category: harmonyos-references
scraped_at: 2026-04-28T08:10:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea7a552b816a62d0fbdf37b0a422b1916bff238d2168458372eb102b182c9a65
---

```
1. typedef struct Usb_DeviceArray {...} Usb_DeviceArray
```

## 概述

PC/2in1

设备ID清单，用于存放OH\_Usb\_GetDevices接口获取到的设备ID列表和设备数量。

**起始版本：** 18

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint64\_t\* deviceIds | 开发者申请好的设备ID数组首地址，申请的数组大小建议一般不超过128，以避免过度占用内存。 |
| uint32\_t num | 实际返回的设备数量，根据数量遍历deviceIds获得设备ID。当该值为0时，表示不存在USB设备。 |
