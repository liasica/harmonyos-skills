---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/t-native-xcomponent-oh-nativexcomponent-mouseevent
title: OH_NativeXComponent_MouseEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_MouseEvent
category: harmonyos-references
scraped_at: 2026-04-28T08:04:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5579fdd5b59fefeab0b4e144b3635f7d8fe20028d786d88941192f258e47525d
---

```
1. typedef struct {...} OH_NativeXComponent_MouseEvent
```

## 概述

PhonePC/2in1TabletTVWearable

鼠标事件。

**起始版本：** 9

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| float x | 点击触点相对于当前组件左上角的x轴坐标。单位：vp。 |
| float y | 点击触点相对于当前组件左上角的y轴坐标。单位：vp。 |
| float screenX | 点击触点相对于XComponent所在应用屏幕左上角的x轴坐标。单位：vp。 |
| float screenY | 点击触点相对于XComponent所在应用屏幕左上角的y轴坐标。单位：vp。 |
| int64\_t timestamp | 当前鼠标事件的时间戳。触发事件时距离系统启动的时间间隔，单位纳秒。 |
| [OH\_NativeXComponent\_MouseEventAction](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventaction) action | 当前鼠标事件动作。 |
| [OH\_NativeXComponent\_MouseEventButton](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventbutton) button | 鼠标事件按键。 |
