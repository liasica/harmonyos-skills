---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usb-nonroothubarray
title: Usb_NonRootHubArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Usb_NonRootHubArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf3055ec1d08a2bfde8eeda1e33175db7706edf76884e9da4af94d3f2aa99869
---

```c
typedef struct Usb_NonRootHubArray {...} Usb_NonRootHubArray
```

## 概述

非根集线器数组，用于存放[OH\_Usb\_GetNonRootHubs](capi-usb-ddk-api-h.md#oh_usb_getnonroothubs)接口获取到的非根集线器设备ID数组和数量。开发者申请非根集线器ID数组，使用完结构体后需释放申请的内存，否则会造成资源泄漏。

**起始版本：** 26.0.0

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t\* nonRootHubIds | 开发者申请好的非根集线器设备ID数组首地址，申请的数组大小建议不超过128，以避免过度占用内存。非根USB集线器设备ID由总线号左移32位加上设备地址构造而成。 |
| uint32\_t num | 实际返回的非根集线器数量，根据数量遍历nonRootHubIds获得非根集线器设备ID。当该值为0时，表示不存在非根集线器设备。 |
