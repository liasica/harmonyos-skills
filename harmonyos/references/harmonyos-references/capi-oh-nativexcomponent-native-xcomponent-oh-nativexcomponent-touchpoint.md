---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-touchpoint
title: OH_NativeXComponent_TouchPoint
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_TouchPoint
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0b219b30d44106e297bf299ec190ae67fbc60d18dc4624e01b946eb363d1592e
---

```c
typedef struct {...} OH_NativeXComponent_TouchPoint
```

## 概述

触摸事件中触摸点的信息。该结构体由系统在触摸事件回调中填充，开发者可通过回调获取各触摸点的状态数据（包括相对于应用窗口和组件的坐标、触摸类型、接触面积、压力大小、时间戳以及按下状态等信息）。适用于需要精确获取和处理多点触控信息的场景。

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
| [OH\_NativeXComponent\_TouchEventType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_toucheventtype) type | 触摸事件的类型，用于区分按压、抬起、移动等不同触摸动作，具体取值见OH\_NativeXComponent\_TouchEventType。 |
| double size | 指垫和屏幕之间的接触面积。取值范围为[0.0, 1.0]，值越大表示接触面积越大（归一化值）。 |
| float force | 当前触摸事件的压力，取值范围为[0, 1]，其中0表示无压力，1表示设备可识别的最大压力（具体取值范围依设备能力而定）。 |
| int64\_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| bool isPressed | 当前点是否被按下，按下时为true，离开时为false。 |
