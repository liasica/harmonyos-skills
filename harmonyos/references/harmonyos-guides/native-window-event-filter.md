---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-event-filter
title: 使用WindowManager管理多模输入事件（C/C++）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 使用WindowManager管理多模输入事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8ad38e55de4cffdfe0fb7c702be666c9ec50fd74cc8aa7022fca991d65556cbc
---

## 场景介绍

[WindowManager](../harmonyos-references/capi-windowmanager.md)提供应用窗口的管理能力，可以用于管理多模输入事件。

当前支持使用WindowManager进行多模输入事件的过滤，还可以将多模触摸事件注入目标窗口，具体开发步骤可见下文。

## 过滤多模输入事件

使用WindowManager模块提供的能力去拦截按键事件，让按键事件不往应用内部组件分发。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(entry PUBLIC libnative_window_manager.so libohinput.so)
```

### 添加头文件

```
1. #include "multimodalinput/oh_input_manager.h"
2. #include "multimodalinput/oh_key_code.h"
3. #include "window_manager/oh_window_comm.h"
4. #include "window_manager/oh_window_event_filter.h"
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
1. #include "napi/native_api.h"
2. #include "window_manager/oh_window_comm.h"
3. #include "window_manager/oh_window_event_filter.h"
4. #include "multimodalinput/oh_input_manager.h"
5. #include "multimodalinput/oh_key_code.h"

7. // 设置过滤函数
8. static bool filterFunc(Input_KeyEvent *event) {
9. auto keyCode = OH_Input_GetKeyEventKeyCode(event);
10. auto action = OH_Input_GetKeyEventAction(event);
11. // case1: 过滤escape
12. // return keyCode == Input_KeyCode::KEYCODE_ESCAPE;

14. // case2: 过滤数字键的按下，抬起不过滤
15. // return keyCode >= Input_KeyCode::KEYCODE_0 && keyCode <= Input_KeyCode::KEYCODE_9
16. //  && action == Input_KeyEventAction::KEY_ACTION_DOWN;

18. // 过滤escape和数字键的按下(case1 || case2)
19. return (keyCode >= Input_KeyCode::KEYCODE_0 && keyCode <= Input_KeyCode::KEYCODE_9
20. && action == Input_KeyEventAction::KEY_ACTION_DOWN) || (keyCode == Input_KeyCode::KEYCODE_ESCAPE);
21. }

23. static napi_value registerFilter(napi_env env, napi_callback_info info) {
24. size_t argc = 1;
25. napi_value args[1] = {nullptr};
26. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

28. int32_t windowId;
29. napi_get_value_int32(env, args[0], &windowId);

31. // 向windowId对应的窗口注册filterFunc的过滤函数
32. auto res = OH_NativeWindowManager_RegisterKeyEventFilter(windowId, filterFunc);

34. napi_value errCode;
35. napi_create_int32(env, res, &errCode);
36. return errCode;
37. }

39. static napi_value clearFilter(napi_env env, napi_callback_info info) {
40. size_t argc = 1;
41. napi_value args[1] = {nullptr};
42. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

44. int32_t windowId;
45. napi_get_value_int32(env, args[0], &windowId);

47. auto res = OH_NativeWindowManager_UnregisterKeyEventFilter(windowId);
48. napi_value errCode;
49. napi_create_int32(env, res, &errCode);
50. return errCode;

52. }

54. EXTERN_C_START
55. static napi_value Init(napi_env env, napi_value exports) {
56. napi_property_descriptor desc[] = {
57. {"registerFilter", nullptr, registerFilter, nullptr, nullptr, nullptr, napi_default, nullptr},
58. {"clearFilter", nullptr, clearFilter, nullptr, nullptr, nullptr, napi_default, nullptr}};
59. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
60. return exports;
61. }
62. EXTERN_C_END
```

## 将多模触摸事件注入给目标窗口

使用WindowManager模块提供的能力为指定窗口注入触摸事件，仅支持同进程窗口。此操作不会触发窗口焦点、层级变化或拖拽，事件会直接发送给ArkUI。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(entry PUBLIC libnative_window_manager.so libohinput.so)
```

### 添加头文件

```
1. #include "multimodalinput/oh_input_manager.h"
2. #include "window_manager/oh_window.h"
3. #include "napi/native_api.h"
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
1. #include "napi/native_api.h"
2. #include "window_manager/oh_window.h"
3. #include "multimodalinput/oh_input_manager.h"

5. static napi_value injectEvent(napi_env env, napi_callback_info info) {
6. size_t argc = 10;
7. napi_value args[10] = {nullptr};
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

10. int32_t windowId;
11. napi_get_value_int32(env, args[0], &windowId);

13. int32_t displayId;
14. napi_get_value_int32(env, args[1], &displayId);

16. int32_t windowX;
17. napi_get_value_int32(env, args[2], &windowX);

19. int32_t windowY;
20. napi_get_value_int32(env, args[3], &windowY);

22. int32_t action;
23. napi_get_value_int32(env, args[4], &action);

25. int32_t fingerId;
26. napi_get_value_int32(env, args[5], &fingerId);

28. int32_t displayX;
29. napi_get_value_int32(env, args[6], &displayX);

31. int32_t displayY;
32. napi_get_value_int32(env, args[7], &displayY);

34. int32_t actionTime;
35. napi_get_value_int32(env, args[8], &actionTime);

37. int32_t TE_WindowId;
38. napi_get_value_int32(env, args[9], &TE_WindowId);

40. // 构造多模事件touchEvent
41. Input_TouchEvent* touchEvent = OH_Input_CreateTouchEvent();
42. OH_Input_SetTouchEventAction(touchEvent, action);
43. OH_Input_SetTouchEventFingerId(touchEvent, fingerId);
44. OH_Input_SetTouchEventDisplayX(touchEvent, displayX);
45. OH_Input_SetTouchEventDisplayY(touchEvent, displayY);
46. OH_Input_SetTouchEventActionTime(touchEvent, actionTime);
47. OH_Input_SetTouchEventWindowId(touchEvent, TE_WindowId);
48. OH_Input_SetTouchEventDisplayId(touchEvent, displayId);

50. // 向windowId对应的窗口注入多模触摸事件
51. auto res = OH_WindowManager_InjectTouchEvent(windowId, touchEvent, windowX, windowY);

53. // 使用完touchEvent后销毁对象
54. OH_Input_DestroyTouchEvent(&touchEvent);

56. napi_value errCode;
57. napi_create_int32(env, res, &errCode);
58. return errCode;
59. }

61. EXTERN_C_START
62. static napi_value Init(napi_env env, napi_value exports) {
63. napi_property_descriptor desc[] = {
64. {"injectEvent", nullptr, injectEvent, nullptr, nullptr, nullptr, napi_default, nullptr}};
65. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
66. return exports;
67. }
68. EXTERN_C_END
```
