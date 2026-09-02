---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-historicalpoint
title: OH_NativeXComponent_HistoricalPoint
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_HistoricalPoint
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:039c54470ce1611c9bc46d26a5a9b1f8bf313155c82543a02a5d33d00c91ddd3
---

```c
typedef struct {...} OH_NativeXComponent_HistoricalPoint
```

## 概述

历史触摸点。在触摸事件处理中，系统会记录触摸轨迹中的历史触摸点信息，用于还原高速滑动等场景下的完整触摸轨迹。每个历史触摸点包含该时刻触摸点的坐标、类型、压力、时间戳等信息。该结构体用于记录触摸事件过程中的历史触摸点信息，包括触摸点的坐标、压力、时间戳、倾斜角度等属性，适用于需要分析触摸轨迹、手势识别等场景。

**起始版本：** 10

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
| [OH\_NativeXComponent\_TouchEventType](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_toucheventtype) type | 触摸事件的触摸类型。 |
| double size | 触摸工具与屏幕之间的接触面积。该值为归一化的接触面积，取值范围：0.0~1.0。 |
| float force | 当前触摸事件的压力。取值范围[0, 1]。取值范围：0.0~1.0，0.0表示无压力，1.0表示最大压力。 |
| int64\_t timeStamp | 当前触摸事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| float titlX | 平面X-Y上的投影与当前触摸事件的Z轴之间的角度，单位：弧度。 |
| float titlY | 平面Y-Z上的投影与当前触摸事件的Z轴之间的角度，单位：弧度。 |
| [OH\_NativeXComponent\_TouchEvent\_SourceTool](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_touchevent_sourcetool) sourceTool | 当前触摸事件的源工具。 |
