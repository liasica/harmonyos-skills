---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-event-filter
title: 使用WindowManager管理多模输入事件 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 其他开发场景 > 使用WindowManager管理多模输入事件 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1414c3b731ca69824e1e30f737f412f1088cc567e89afe51917d899db6d5ccd8
---

## 场景介绍

[WindowManager](../harmonyos-references/capi-windowmanager.md)提供应用窗口的管理能力，可以用于管理多模输入事件。

当前支持使用WindowManager进行多模输入事件的过滤，还可以将多模触摸事件注入目标窗口，具体开发步骤可见下文。

## 过滤多模输入事件

使用WindowManager模块提供的能力去拦截按键事件，让按键事件不往应用内部组件分发。

### 在CMake脚本中链接动态库

```txt
target_link_libraries(entry PUBLIC libnative_window_manager.so libohinput.so)
```

### 接口使用说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeWindowManager\_RegisterKeyEventFilter(int32\_t windowId, OH\_NativeWindowManager\_KeyEventFilter keyEventFilter) | 为指定的窗口注册过滤回调函数keyEventFilter。 |
| OH\_NativeWindowManager\_UnregisterKeyEventFilter(int32\_t windowId) | 取消指定窗口上的过滤回调函数。 |

* 应用窗口创建后，使用窗口ID绑定按键事件过滤函数。
* 应用窗口需要收到按键事件时，才触发按键事件的拦截。
* 当回调函数返回true表示拦截，false表示不拦截。
* 同一个窗口ID注册的回调函数只允许一个，最后注册的回调函数会覆盖之前注册过的回调函数。如需过滤多个按键的组合场景，建议在一个回调函数里面处理。

### 示例代码

以下示例代码中介绍了如何注册过滤函数和取消过滤函数，以过滤ESC退出按键和数字按键为例。

```
#include "napi/native_api.h"
#include "window_manager/oh_window_comm.h"
#include "window_manager/oh_window_event_filter.h"
#include "multimodalinput/oh_input_manager.h"
#include "multimodalinput/oh_key_code.h"

// 设置过滤函数
static bool filterFunc(Input_KeyEvent *event)
{
    auto keyCode = OH_Input_GetKeyEventKeyCode(event);
    auto action = OH_Input_GetKeyEventAction(event);
    
    // 过滤escape和数字键的按下
    return (keyCode >= Input_KeyCode::KEYCODE_0 && keyCode <= Input_KeyCode::KEYCODE_9
         && action == Input_KeyEventAction::KEY_ACTION_DOWN) || (keyCode == Input_KeyCode::KEYCODE_ESCAPE);
}

static napi_value registerFilter(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    
    int32_t windowId;
    napi_get_value_int32(env, args[0], &windowId);
    
    // 向windowId对应的窗口注册filterFunc的过滤函数
    auto res = OH_NativeWindowManager_RegisterKeyEventFilter(windowId, filterFunc);
    
    napi_value errCode;
    napi_create_int32(env, res, &errCode);
    return errCode;
}

static napi_value clearFilter(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t windowId;
    napi_get_value_int32(env, args[0], &windowId);

    auto res = OH_NativeWindowManager_UnregisterKeyEventFilter(windowId);
    napi_value errCode;
    napi_create_int32(env, res, &errCode);
    return errCode;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"registerFilter", nullptr, registerFilter, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"clearFilter", nullptr, clearFilter, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```

## 将多模触摸事件注入给目标窗口

使用WindowManager模块提供的能力为指定窗口注入触摸事件，仅支持同进程窗口。此操作不会触发窗口焦点、层级变化或拖拽，事件会直接发送给ArkUI。

### 在CMake脚本中链接动态库

```txt
target_link_libraries(entry PUBLIC libnative_window_manager.so libohinput.so)
```

### 接口使用说明

| 接口名 | 描述 |
| --- | --- |
| OH\_WindowManager\_InjectTouchEvent(int32\_t windowId, Input\_TouchEvent\* touchEvent, int32\_t windowX, int32\_t windowY) | 为指定的窗口注入触摸事件。 |

* 构造事件参数，向目标窗口ID注入事件。
* 仅支持注入同进程窗口。注入不会触发窗口焦点、层级变化或拖拽，事件直接发送给ArkUI。
* 接口需要在指定窗口加载UI后调用。
* 完成窗口和多模触摸事件校验，确保事件参数正确，再将事件发送给ArkUI。具体参数说明如下：

  | 参数名 | 描述 |
  | --- | --- |
  | windowId | 目标窗口ID，仅支持同进程的窗口，否则返回错误码1300002。窗口需完成UI加载，否则返回错误码1300003。 |
  | touchEvent | 多模触摸事件，具体可见[Input\_TouchEvent](../harmonyos-references/capi-input-input-touchevent.md)，事件定义在oh\_input\_manager.h中。调用[OH\_Input\_CreateTouchEvent](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_createtouchevent)接口创建touchEvent对象，使用完后调用[OH\_Input\_DestroyTouchEvent](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁该对象。具体参数说明见下表。 |
  | windowX | 注入事件相对于注入窗口的落点横坐标。参数应为大于等于0的整数，否则返回错误码1300003。 |
  | windowY | 注入事件相对于注入窗口的落点纵坐标。参数应为大于等于0的整数，否则返回错误码1300003。 |

  其中，touchEvent多模触摸事件具体参数说明如下：

  | 参数名 | 方法 | 描述 |
  | --- | --- | --- |
  | action | [OH\_Input\_SetTouchEventAction](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventaction) | 表示事件行为，默认值为0。  当前只支持0-3的行为，分别表示为：  - 0：cancel，表示取消事件。  - 1：down，表示按下事件。  - 2：move，表示移动事件。  - 3：up，表示抬起事件。  - 其他行为会返回错误码1300003。 |
  | id | [OH\_Input\_SetTouchEventFingerId](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventfingerid) | 表示手指ID，默认值为0。  应为大于等于0的整数，否则返回错误码1300003。 |
  | displayX | [OH\_Input\_SetTouchEventDisplayX](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventdisplayx) | 表示事件落点相对于屏幕的横坐标，默认值为0。  参数应为非负整数，否则返回错误码1300003。建议与windowX保持对应关系，即使不一致也不会返回错误码，仅校验入参合法范围。转换方法推荐使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法获取windowRect属性，通过displayX减去windowRect中窗口左上角横坐标计算对应的windowX。 |
  | displayY | [OH\_Input\_SetTouchEventDisplayY](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventdisplayy) | 表示事件落点相对于屏幕的纵坐标，默认值为0。  参数应为非负整数，否则返回错误码1300003。建议与windowY保持对应关系，即使不一致也不会返回错误码，仅校验入参合法范围。转换方法推荐使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法获取windowRect属性，通过displayY减去windowRect中窗口左上角纵坐标计算对应的windowY。 |
  | actionTime | [OH\_Input\_SetTouchEventActionTime](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventactiontime) | 表示时间戳，默认值为-1。参数应为非负整数，否则返回错误码1300003。 |
  | windowId | [OH\_Input\_SetTouchEventWindowId](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventwindowid) | 表示事件注入窗口ID，默认值为-1。若参数不为默认值且不等于[OH\_WindowManager\_InjectTouchEvent](../harmonyos-references/capi-oh-window-h.md#oh_windowmanager_injecttouchevent)接口参数windowId，将校验传入参数错误。 |
  | displayId | [OH\_Input\_SetTouchEventDisplayId](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_settoucheventdisplayid) | 表示事件注入屏幕ID，默认值为-1。无限制，但是应该尽量保证与[OH\_WindowManager\_InjectTouchEvent](../harmonyos-references/capi-oh-window-h.md#oh_windowmanager_injecttouchevent)接口参数windowId有相互对应关系，推荐使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法获取displayId属性。 |

### 示例代码

以下示例代码介绍了如何将多模触摸事件注入目标窗口，以单次事件注入为例。

```
#include "napi/native_api.h"
#include "window_manager/oh_window.h"
#include "multimodalinput/oh_input_manager.h"

const int32_t ARGS_TWO = 2;
const int32_t ARGS_THREE = 3;
const int32_t ARGS_FOUR = 4;
const int32_t ARGS_FIVE = 5;
const int32_t ARGS_SIX = 6;
const int32_t ARGS_SEVEN = 7;
const int32_t ARGS_EIGHT = 8;
const int32_t ARGS_NINE = 9;
const int32_t ARGS_TEN = 10;

static napi_value injectEvent(napi_env env, napi_callback_info info)
{
    size_t argc = ARGS_TEN;
    napi_value args[ARGS_TEN] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t windowId;
    napi_get_value_int32(env, args[0], &windowId);

    int32_t displayId;
    napi_get_value_int32(env, args[1], &displayId);

    int32_t windowX;
    napi_get_value_int32(env, args[ARGS_TWO], &windowX);

    int32_t windowY;
    napi_get_value_int32(env, args[ARGS_THREE], &windowY);

    int32_t action;
    napi_get_value_int32(env, args[ARGS_FOUR], &action);

    int32_t fingerId;
    napi_get_value_int32(env, args[ARGS_FIVE], &fingerId);

    int32_t displayX;
    napi_get_value_int32(env, args[ARGS_SIX], &displayX);

    int32_t displayY;
    napi_get_value_int32(env, args[ARGS_SEVEN], &displayY);

    int32_t actionTime;
    napi_get_value_int32(env, args[ARGS_EIGHT], &actionTime);

    int32_t TE_WindowId;
    napi_get_value_int32(env, args[ARGS_NINE], &TE_WindowId);
    
    // 构造多模事件touchEvent
    Input_TouchEvent* touchEvent = OH_Input_CreateTouchEvent();
    OH_Input_SetTouchEventAction(touchEvent, action);
    OH_Input_SetTouchEventFingerId(touchEvent, fingerId);
    OH_Input_SetTouchEventDisplayX(touchEvent, displayX);
    OH_Input_SetTouchEventDisplayY(touchEvent, displayY);
    OH_Input_SetTouchEventActionTime(touchEvent, actionTime);
    OH_Input_SetTouchEventWindowId(touchEvent, TE_WindowId);
    OH_Input_SetTouchEventDisplayId(touchEvent, displayId);

    // 向windowId对应的窗口注入多模触摸事件
    auto res = OH_WindowManager_InjectTouchEvent(windowId, touchEvent, windowX, windowY);

    // 使用完touchEvent后销毁对象
    OH_Input_DestroyTouchEvent(&touchEvent);
    
    napi_value errCode;
    napi_create_int32(env, res, &errCode);
    return errCode;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"injectEvent", nullptr, injectEvent, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```
