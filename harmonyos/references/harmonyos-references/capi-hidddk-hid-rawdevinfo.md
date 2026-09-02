---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-rawdevinfo
title: Hid_RawDevInfo
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_RawDevInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8ea94ffa19838af44401afbf35d46ea6a0d649a6357f120a905832850f5ea588
---

```c
typedef struct Hid_RawDevInfo {...} Hid_RawDevInfo
```

## 概述

HID原始设备信息，包含总线类型、供应商ID、产品ID等关键标识信息。开发者可以通过此结构体识别和区分不同的HID设备，通常用于设备识别、设备匹配、设备过滤等场景。

**起始版本：** 18

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t busType | 总线类型，用于标识HID设备的物理连接方式。 |
| uint16\_t vendor | 供应商ID。 |
| uint16\_t product | 产品ID。 |
