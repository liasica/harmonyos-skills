---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-event-filter-h
title: oh_window_event_filter.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_window_event_filter.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f00fb3be52301e8859d8d9426dbc7bf4ec875c8d4d12852014ff6fac15b57274
---

## 概述

PhonePC/2in1TabletTVWearable

定义窗口管理按键事件过滤的接口，当多模输入的事件经过窗口时，可以通过过滤接口拦截事件不让事件往下分发。

**引用文件：** <window\_manager/oh\_window\_event\_filter.h>

**库：** libnative\_window\_manager.so

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**相关模块：** [WindowManager](capi-windowmanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef bool (\*OH\_NativeWindowManager\_KeyEventFilter)(Input\_KeyEvent\* keyEvent)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_keyeventfilter) | OH\_NativeWindowManager\_KeyEventFilter | 定义多模按键的过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterKeyEventFilter(int32\_t windowId,OH\_NativeWindowManager\_KeyEventFilter keyEventFilter)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_registerkeyeventfilter) | - | 注册按键事件的过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterKeyEventFilter(int32\_t windowId)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_unregisterkeyeventfilter) | - | 取消注册窗口的按键事件过滤函数。 |
| [typedef bool (\*OH\_NativeWindowManager\_MouseEventFilter)(Input\_MouseEvent\* mouseEvent)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_mouseeventfilter) | OH\_NativeWindowManager\_MouseEventFilter | 定义多模鼠标事件的过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterMouseEventFilter(int32\_t windowId,OH\_NativeWindowManager\_MouseEventFilter mouseEventFilter)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_registermouseeventfilter) | - | 注册鼠标事件的过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterMouseEventFilter(int32\_t windowId)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_unregistermouseeventfilter) | - | 取消注册窗口的鼠标事件过滤函数。 |
| [typedef bool (\*OH\_NativeWindowManager\_TouchEventFilter)(Input\_TouchEvent\* touchEvent)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_toucheventfilter) | OH\_NativeWindowManager\_TouchEventFilter | 定义多模触摸事件的过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_RegisterTouchEventFilter(int32\_t windowId,OH\_NativeWindowManager\_TouchEventFilter touchEventFilter)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_registertoucheventfilter) | - | 注册触摸事件的过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_UnregisterTouchEventFilter(int32\_t windowId)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_unregistertoucheventfilter) | - | 取消注册窗口的触摸事件过滤函数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeWindowManager\_KeyEventFilter()

PhonePC/2in1TabletTVWearable

```
1. typedef bool (*OH_NativeWindowManager_KeyEventFilter)(Input_KeyEvent* keyEvent)
```

**描述**

定义多模按键的过滤函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 多模按键事件，具体可见[Input\_KeyEvent](capi-input-input-keyevent.md)，事件定义在oh\_input\_manager中。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回是否过滤该事件。返回true窗口不再往下分发，返回false表示不拦截。 |

### OH\_NativeWindowManager\_RegisterKeyEventFilter()

PhonePC/2in1TabletTVWearable

```
1. WindowManager_ErrorCode OH_NativeWindowManager_RegisterKeyEventFilter(int32_t windowId,OH_NativeWindowManager_KeyEventFilter keyEventFilter)
```

**描述**

注册按键事件的过滤函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要过滤按键事件的窗口ID。 |
| [OH\_NativeWindowManager\_KeyEventFilter](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_keyeventfilter) keyEventFilter | 多模按键的过滤函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### OH\_NativeWindowManager\_UnregisterKeyEventFilter()

PhonePC/2in1TabletTVWearable

```
1. WindowManager_ErrorCode OH_NativeWindowManager_UnregisterKeyEventFilter(int32_t windowId)
```

**描述**

取消注册窗口的按键事件过滤函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要取消过滤按键事件的窗口ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### OH\_NativeWindowManager\_MouseEventFilter()

PhonePC/2in1TabletTVWearable

```
1. typedef bool (*OH_NativeWindowManager_MouseEventFilter)(Input_MouseEvent* mouseEvent)
```

**描述**

定义多模鼠标事件的过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 多模鼠标事件，具体可见[Input\_MouseEvent](capi-input-input-mouseevent.md)，事件定义在oh\_input\_manager中。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回是否过滤该事件。true表示过滤该事件，不会继续往下分发；false表示不过滤不拦截此事件，将会继续分发。 |

### OH\_NativeWindowManager\_RegisterMouseEventFilter()

PhonePC/2in1TabletTVWearable

```
1. WindowManager_ErrorCode OH_NativeWindowManager_RegisterMouseEventFilter(int32_t windowId,OH_NativeWindowManager_MouseEventFilter mouseEventFilter)
```

**描述**

注册鼠标事件的过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要过滤鼠标事件的窗口ID。 |
| [OH\_NativeWindowManager\_MouseEventFilter](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_mouseeventfilter) mouseEventFilter | 多模鼠标事件的过滤函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### OH\_NativeWindowManager\_UnregisterMouseEventFilter()

PhonePC/2in1TabletTVWearable

```
1. WindowManager_ErrorCode OH_NativeWindowManager_UnregisterMouseEventFilter(int32_t windowId)
```

**描述**

取消注册窗口的鼠标事件过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要取消过滤鼠标事件的窗口ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### OH\_NativeWindowManager\_TouchEventFilter()

PhonePC/2in1TabletTVWearable

```
1. typedef bool (*OH_NativeWindowManager_TouchEventFilter)(Input_TouchEvent* touchEvent)
```

**描述**

定义多模触摸事件的过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 多模触摸事件，具体可见[Input\_TouchEvent](capi-input-input-touchevent.md)，事件定义在oh\_input\_manager中。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回是否过滤该事件。true表示过滤该事件，不会继续往下分发；false表示不过滤不拦截此事件，将会继续分发。 |

### OH\_NativeWindowManager\_RegisterTouchEventFilter()

PhonePC/2in1TabletTVWearable

```
1. WindowManager_ErrorCode OH_NativeWindowManager_RegisterTouchEventFilter(int32_t windowId,OH_NativeWindowManager_TouchEventFilter touchEventFilter)
```

**描述**

注册触摸事件的过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要过滤触摸事件的窗口ID。 |
| [OH\_NativeWindowManager\_TouchEventFilter](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_toucheventfilter) touchEventFilter | 多模触摸事件的过滤函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### OH\_NativeWindowManager\_UnregisterTouchEventFilter()

PhonePC/2in1TabletTVWearable

```
1. WindowManager_ErrorCode OH_NativeWindowManager_UnregisterTouchEventFilter(int32_t windowId)
```

**描述**

取消注册窗口的触摸事件过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要取消过滤触摸事件的窗口ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |
