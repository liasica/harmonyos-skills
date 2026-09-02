---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventproperties
title: Hid_EventProperties
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_EventProperties
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:173da40989f4c13e16c8e8f08a1ba2dc8f1b9e2d3559344367cba0574b756c1d
---

```c
typedef struct Hid_EventProperties {...} Hid_EventProperties
```

## 概述

设备事件属性，包括事件类型、键值、绝对坐标、相对坐标等各类事件属性编码及取值范围。用于HID设备的属性配置，适用于需要精细化管理输入事件的场景。使用结构体前，需根据HID设备规范初始化所有成员变量。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| struct [Hid\_EventTypeArray](capi-hidddk-hid-eventtypearray.md) hidEventTypes | 事件类型属性编码数组，包含设备支持的事件类型集合，用于配置HID设备可触发的事件。 |
| struct [Hid\_KeyCodeArray](capi-hidddk-hid-keycodearray.md) hidKeys | 键值属性编码数组，包含设备支持的按键编码集合，用于配置HID设备支持的按键功能。 |
| struct [Hid\_AbsAxesArray](capi-hidddk-hid-absaxesarray.md) hidAbs | 绝对坐标属性编码数组，用于配置绝对坐标输入（如触摸屏、手柄摇杆）。 |
| struct [Hid\_RelAxesArray](capi-hidddk-hid-relaxesarray.md) hidRelBits | 相对坐标属性编码数组，用于配置相对坐标输入（如鼠标移动）。 |
| struct [Hid\_MscEventArray](capi-hidddk-hid-msceventarray.md) hidMiscellaneous | 其他特殊事件属性编码数组，用于配置特殊输入事件（如扫描、手势）。 |
| int32\_t hidAbsMax[64] | 绝对坐标属性最大值。数组元素按索引对应各坐标轴，必须不小于对应坐标轴的最小值。 |
| int32\_t hidAbsMin[64] | 绝对坐标属性最小值。数组元素按索引对应各坐标轴，必须不大于对应坐标轴的最大值。 |
| int32\_t hidAbsFuzz[64] | 绝对坐标属性模糊值。数组元素按索引对应各坐标轴，用于定义输入事件的模糊容差，建议不超过坐标范围。 |
| int32\_t hidAbsFlat[64] | 绝对坐标属性平坦值。数组元素按索引对应各坐标轴，用于定义输入事件死区的平坦范围（此范围内的值不触发事件上报），建议不超过模糊值。 |
