---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent
title: OH_NativeXComponent_MouseEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent_MouseEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:401caff83a19288bc33cd99eb21ebdac42fcbd4af2bdb7150da36fdc059832d2
---

```c
typedef struct {...} OH_NativeXComponent_MouseEvent
```

## 概述

鼠标事件。用于在XComponent的鼠标事件回调中传递鼠标事件信息，包含触点相对于组件和屏幕的坐标、事件时间戳、鼠标动作及按键信息。

**起始版本：** 9

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float x | 鼠标触点相对于当前组件左上角的x轴坐标。单位：vp。 |
| float y | 鼠标触点相对于当前组件左上角的y轴坐标。单位：vp。 |
| float screenX | 鼠标触点相对于XComponent所在应用屏幕左上角的x轴坐标。单位：vp。 |
| float screenY | 鼠标触点相对于XComponent所在应用屏幕左上角的y轴坐标。单位：vp。 |
| int64\_t timestamp | 当前鼠标事件的时间戳。触发事件时距离系统启动的时间间隔，单位：ns。 |
| [OH\_NativeXComponent\_MouseEventAction](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventaction) action | 当前鼠标事件动作。取值参考OH\_NativeXComponent\_MouseEventAction，包括按下、释放、移动等动作类型。 |
| [OH\_NativeXComponent\_MouseEventButton](capi-native-interface-xcomponent-h.md#oh_nativexcomponent_mouseeventbutton) button | 触发当前鼠标事件的按键。取值参考OH\_NativeXComponent\_MouseEventButton，包括左键、右键、中键、后退键、前进键等按键类型。 |
