---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-axis-type-h
title: oh_axis_type.h
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 头文件 > oh_axis_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7d267e0c369be9884dd314f69618366c1116f390d3121fcfefab94ed2ec3455e
---

## 概述

PhonePC/2in1TabletTVWearable

输入设备的轴事件结构和枚举。

**引用文件：** <multimodalinput/oh\_axis\_type.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**相关模块：** [input](capi-input.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputEvent\_AxisType](capi-oh-axis-type-h.md#inputevent_axistype) | InputEvent\_AxisType | 输入设备的轴类型。 |
| [InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype) | InputEvent\_AxisEventType | 输入设备的轴事件类型。 |
| [InputEvent\_AxisAction](capi-oh-axis-type-h.md#inputevent_axisaction) | InputEvent\_AxisAction | 轴事件动作。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### InputEvent\_AxisType

PhonePC/2in1TabletTVWearable

```
1. enum InputEvent_AxisType
```

**描述**

输入设备的轴类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AXIS\_TYPE\_UNKNOWN | 未知轴类型，通常作为初始值。 |
| AXIS\_TYPE\_SCROLL\_VERTICAL | 垂直滚动轴，当您滚动鼠标滚轮或在触控板上进行单指或双指滑动时，垂直滚动轴的状态改变。 |
| AXIS\_TYPE\_SCROLL\_HORIZONTAL | 水平滚动轴，当您滚动鼠标滚轮或在触控板上进行双指滑动时，水平滚动轴的状态发生变化。 |
| AXIS\_TYPE\_PINCH | 捏合轴，用于描述触控板上的双指捏合手势。 |
| AXIS\_TYPE\_ROTATE | 旋转轴，用于描述触控板上的双指旋转手势。 |

### InputEvent\_AxisEventType

PhonePC/2in1TabletTVWearable

```
1. enum InputEvent_AxisEventType
```

**描述**

输入设备的轴事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AXIS\_EVENT\_TYPE\_PINCH = 1 | 双指捏合事件，包含AXIS\_TYPE\_PINCH和AXIS\_TYPE\_ROTATE两种轴类型。  **起始版本：** 12。 |
| AXIS\_EVENT\_TYPE\_SCROLL = 2 | 滚轴事件，包含AXIS\_TYPE\_SCROLL\_VERTICAL和AXIS\_TYPE\_SCROLL\_HORIZONTAL两种轴类型，其中鼠标滚轮事件仅包含AXIS\_TYPE\_SCROLL\_VERTICAL一种轴类型。  **起始版本：** 12。 |

### InputEvent\_AxisAction

PhonePC/2in1TabletTVWearable

```
1. enum InputEvent_AxisAction
```

**描述**

轴事件动作。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AXIS\_ACTION\_CANCEL = 0 | 取消轴输入事件。 |
| AXIS\_ACTION\_BEGIN | 开始轴输入事件。 |
| AXIS\_ACTION\_UPDATE | 轴输入事件中。 |
| AXIS\_ACTION\_END | 结束轴输入事件。 |
