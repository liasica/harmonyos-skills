---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-absaxesarray
title: Hid_AbsAxesArray
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_AbsAxesArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5240cca8d880e220856797a20e6aa087b922105721cd04ab9b7ef331e3012a4a
---

```c
typedef struct Hid_AbsAxesArray {...} Hid_AbsAxesArray
```

## 概述

绝对坐标属性数组，用于存储HID设备的多个绝对坐标轴的属性信息，支持描述如触摸屏、游戏摇杆等输入设备的坐标特征，适用于需要精确读取和处理多维输入数据的驱动开发场景，例如在手柄、触摸板等输入设备中记录轴位数据。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Hid\_AbsAxes](capi-hid-ddk-types-h.md#hid_absaxes)\* hidAbsAxes | 指向绝对坐标属性编码数组首元素的指针。需与length配合使用，指针需有效且不为 NULL。 |
| uint16\_t length | 数组的有效长度，表示hidAbsAxes指针指向的有效元素个数。取值范围：[0, 65535]。 |
