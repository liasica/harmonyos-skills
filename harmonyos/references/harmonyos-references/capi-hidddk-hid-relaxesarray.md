---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-relaxesarray
title: Hid_RelAxesArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_RelAxesArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d0faf6b503a0f97fdcf9496cbc24b1cde3bb07764b931db072113107be4ce33
---

```c
typedef struct Hid_RelAxesArray {...} Hid_RelAxesArray
```

## 概述

相对坐标属性编码数组，用于存储HID设备支持的相对坐标属性信息。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Hid\_RelAxes](capi-hid-ddk-types-h.md#hid_relaxes)\* hidRelAxes | 相对坐标属性编码数组的指针，指向调用方预先分配的数组（不允许为空指针），数组大小不小于length。 |
| uint16\_t length | 数组的有效长度，不超过hidRelAxes数组的实际长度。 |
