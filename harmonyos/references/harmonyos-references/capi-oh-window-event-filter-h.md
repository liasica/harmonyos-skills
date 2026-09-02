---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-event-filter-h
title: oh_window_event_filter.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_window_event_filter.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f9f4f9e678a36d9bc0af101fdcd441c94b477d400746e17897124520a7a4167a
---

## 概述

定义窗口管理事件过滤的接口。当多模输入的事件经过窗口时，可通过过滤接口拦截事件，阻止事件向下分发。

**引用文件：** <window\_manager/oh\_window\_event\_filter.h>

**库：** libnative\_window\_manager.so

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**相关模块：** [WindowManager](capi-windowmanager.md)

## 汇总

### 函数

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
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_GetKeyEventFilter(int32\_t windowId, OH\_NativeWindowManager\_KeyEventFilter\* outKeyEventFilter)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_getkeyeventfilter) | - | 获取指定窗口注册的多模按键事件过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_GetMouseEventFilter(int32\_t windowId, OH\_NativeWindowManager\_MouseEventFilter\* outMouseEventFilter)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_getmouseeventfilter) | - | 获取指定窗口注册的多模鼠标事件过滤函数。 |
| [WindowManager\_ErrorCode OH\_NativeWindowManager\_GetTouchEventFilter(int32\_t windowId, OH\_NativeWindowManager\_TouchEventFilter\* outTouchEventFilter)](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_gettoucheventfilter) | - | 获取指定窗口注册的多模触摸事件过滤函数。 |

## 函数说明

### OH\_NativeWindowManager\_KeyEventFilter()

```c
typedef bool (*OH_NativeWindowManager_KeyEventFilter)(Input_KeyEvent* keyEvent)
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

```c
WindowManager_ErrorCode OH_NativeWindowManager_RegisterKeyEventFilter(int32_t windowId,OH_NativeWindowManager_KeyEventFilter keyEventFilter)
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
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVAILD\_WINDOW\_ID，表示参数windowId无效。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数keyEventFilter无效。  返回SERVICE\_ERROR，表示窗口管理服务异常。 |

### OH\_NativeWindowManager\_UnregisterKeyEventFilter()

```c
WindowManager_ErrorCode OH_NativeWindowManager_UnregisterKeyEventFilter(int32_t windowId)
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
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVAILD\_WINDOW\_ID，表示参数windowId无效。  返回SERVICE\_ERROR，表示窗口管理服务异常。 |

### OH\_NativeWindowManager\_MouseEventFilter()

```c
typedef bool (*OH_NativeWindowManager_MouseEventFilter)(Input_MouseEvent* mouseEvent)
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

```c
WindowManager_ErrorCode OH_NativeWindowManager_RegisterMouseEventFilter(int32_t windowId,OH_NativeWindowManager_MouseEventFilter mouseEventFilter)
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
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVAILD\_WINDOW\_ID，表示参数windowId无效。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数mouseEventFilter无效。  返回SERVICE\_ERROR，表示窗口管理服务异常。 |

### OH\_NativeWindowManager\_UnregisterMouseEventFilter()

```c
WindowManager_ErrorCode OH_NativeWindowManager_UnregisterMouseEventFilter(int32_t windowId)
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
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVAILD\_WINDOW\_ID，表示参数windowId无效。  返回SERVICE\_ERROR，表示窗口管理服务异常。 |

### OH\_NativeWindowManager\_TouchEventFilter()

```c
typedef bool (*OH_NativeWindowManager_TouchEventFilter)(Input_TouchEvent* touchEvent)
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

```c
WindowManager_ErrorCode OH_NativeWindowManager_RegisterTouchEventFilter(int32_t windowId,OH_NativeWindowManager_TouchEventFilter touchEventFilter)
```

**描述**

注册触摸事件的过滤函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 需要过滤触摸事件的窗口ID。 |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVAILD\_WINDOW\_ID，表示参数windowId无效。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数touchEventFilter无效。  返回SERVICE\_ERROR，表示窗口管理服务异常。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 返回窗口管理接口的通用状态码，具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### OH\_NativeWindowManager\_UnregisterTouchEventFilter()

```c
WindowManager_ErrorCode OH_NativeWindowManager_UnregisterTouchEventFilter(int32_t windowId)
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
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVAILD\_WINDOW\_ID，表示参数windowId无效。  返回SERVICE\_ERROR，表示窗口管理服务异常。 |

### OH\_NativeWindowManager\_GetKeyEventFilter()

```c
WindowManager_ErrorCode OH_NativeWindowManager_GetKeyEventFilter(int32_t windowId, OH_NativeWindowManager_KeyEventFilter* outKeyEventFilter)
```

**描述**

获取指定窗口注册的多模按键事件过滤函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 窗口ID。 |
| [OH\_NativeWindowManager\_KeyEventFilter](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_keyeventfilter)\* outKeyEventFilter | 返回已注册的多模按键事件过滤函数指针。如果窗口没有注册过滤器，\*outKeyEventFilter将返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVALID\_WINDOW\_ID，表示入参windowId无效。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示入参outKeyEventFilter为NULL。 |

### OH\_NativeWindowManager\_GetMouseEventFilter()

```c
WindowManager_ErrorCode OH_NativeWindowManager_GetMouseEventFilter(int32_t windowId, OH_NativeWindowManager_MouseEventFilter* outMouseEventFilter)
```

**描述**

获取指定窗口注册的多模鼠标事件过滤函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 窗口ID。 |
| [OH\_NativeWindowManager\_MouseEventFilter](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_mouseeventfilter)\* outMouseEventFilter | 返回已注册的多模鼠标事件过滤函数指针。如果窗口没有注册过滤器，\*outMouseEventFilter将返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVALID\_WINDOW\_ID，表示入参windowId无效。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示入参outMouseEventFilter为NULL。 |

### OH\_NativeWindowManager\_GetTouchEventFilter()

```c
WindowManager_ErrorCode OH_NativeWindowManager_GetTouchEventFilter(int32_t windowId, OH_NativeWindowManager_TouchEventFilter* outTouchEventFilter)
```

**描述**

获取指定窗口注册的多模触摸事件过滤函数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 窗口ID。 |
| [OH\_NativeWindowManager\_TouchEventFilter](capi-oh-window-event-filter-h.md#oh_nativewindowmanager_toucheventfilter)\* outTouchEventFilter | 返回已注册的多模触摸事件过滤函数指针。如果窗口没有注册过滤器，\*outTouchEventFilter将返回NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | 函数返回的执行结果。  返回OK，表示接口调用成功。  返回INVALID\_WINDOW\_ID，表示入参windowId无效。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示入参outTouchEventFilter为NULL。 |
