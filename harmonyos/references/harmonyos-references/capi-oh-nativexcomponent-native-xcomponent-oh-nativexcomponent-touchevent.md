---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-touchevent
title: OH_NativeXComponent_TouchEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_TouchEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d1802137891fd2bfe7d86c0628d096cc0c09700d4d4f47db1b798f124b10891
---

```c
typedef struct {...} OH_NativeXComponent_TouchEvent
```

## 概述

触摸事件。当用户在XComponent组件上进行触摸操作时，通过该结构体可获取触摸点的坐标、触摸类型、接触面积、压力、时间戳等信息，适用于需要在Native层处理XComponent触摸交互的场景。

**起始版本：** 8

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t id | 手指的唯一标识符。 |
| float screenX | 触摸点相对于XComponent所在应用窗口左上角的x坐标，单位：px。 |
| float screenY | 触摸点相对于XComponent所在应用窗口左上角的y坐标，单位：px。 |
| float x | 触摸点相对于XComponent组件左边缘的x坐标，单位：px。 |
| float y | 触摸点相对于XComponent组件上边缘的y坐标，单位：px。 |
| [OH\_NativeXComponent\_TouchEventType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_toucheventtype) type | 触摸事件的类型。 |
| double size | 触摸区域的归一化大小，表示指垫与屏幕接触面积的相对比例，取值范围为0.0~1.0，值越大表示接触面积越大。 |
| float force | 当前触摸事件的压力，归一化值，取值范围为0.0~1.0，0表示无压力，1表示设备可识别的最大压力。 |
| int64\_t deviceId | 产生当前触摸事件的设备的ID。 |
| int64\_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| [OH\_NativeXComponent\_TouchPoint](capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-touchpoint.md) touchPoints[OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER] | 当前触摸点的数组，数组中有效元素的个数为numPoints。OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER的介绍请参考[宏定义](capi-native-interface-xcomponent-h.md#宏定义)。 |
| uint32\_t numPoints | 当前触摸点的数量，取值范围为[1, OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER]。值为1时为单指触摸，大于1时为多指触摸。 |
