---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-device
title: Hid_Device
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_Device
category: harmonyos-references
scraped_at: 2026-04-28T08:10:45+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:f4c586804bffbc0a358fb8173639b5e1e466fc1cfd892278513be4c304b11cc7
---

```
1. typedef struct Hid_Device {...} Hid_Device
```

## 概述

PC/2in1

设备基本信息。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| const char\* deviceName | 设备名称 |
| uint16\_t vendorId | 厂商ID |
| uint16\_t productId | 产品ID |
| uint16\_t version | 版本号 |
| uint16\_t bustype | 总线类型 |
| Hid\_DeviceProp\* properties | 由[Hid\_DeviceProp](capi-hid-ddk-types-h.md#hid_deviceprop)表示的设备特性 |
| uint16\_t propLength | 设备特性数量 |
