---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-h
title: oh_window.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_window.h
category: harmonyos-references
scraped_at: 2026-04-29T13:54:20+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e877d6e6e0185aaafa9e95daa8f8fc88627371dfd4d218da1cd74201fa4044aa
---

## 概述

PhonePC/2in1TabletTVWearable

定义窗口管理的相关接口，主要用于设置和获取指定窗口的属性，以及设置指定窗口的状态栏样式、导航栏样式。

**引用文件：** <window\_manager/oh\_window.h>

**库：** libnative\_window\_manager.so

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 15

**相关模块：** [WindowManager](capi-windowmanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [int32\_t OH\_WindowManager\_SetWindowStatusBarEnabled(int32\_t windowId, bool enabled, bool enableAnimation)](capi-oh-window-h.md#oh_windowmanager_setwindowstatusbarenabled) | - | 设置主窗口是否显示状态栏。 |
| [int32\_t OH\_WindowManager\_SetWindowStatusBarColor(int32\_t windowId, int32\_t color)](capi-oh-window-h.md#oh_windowmanager_setwindowstatusbarcolor) | - | 设置主窗口的状态栏内容颜色。 |
| [int32\_t OH\_WindowManager\_SetWindowNavigationBarEnabled(int32\_t windowId, bool enabled, bool enableAnimation)](capi-oh-window-h.md#oh_windowmanager_setwindownavigationbarenabled) | - | 设置主窗口是否显示导航栏。 |
| [int32\_t OH\_WindowManager\_GetWindowAvoidArea(int32\_t windowId, WindowManager\_AvoidAreaType type, WindowManager\_AvoidArea\* avoidArea)](capi-oh-window-h.md#oh_windowmanager_getwindowavoidarea) | - | 获取指定窗口的避让区域。 |
| [int32\_t OH\_WindowManager\_IsWindowShown(int32\_t windowId, bool\* isShow)](capi-oh-window-h.md#oh_windowmanager_iswindowshown) | - | 判断指定窗口是否显示。 |
| [int32\_t OH\_WindowManager\_ShowWindow(int32\_t windowId)](capi-oh-window-h.md#oh_windowmanager_showwindow) | - | 显示指定窗口。 |
| [int32\_t OH\_WindowManager\_SetWindowTouchable(int32\_t windowId, bool isTouchable)](capi-oh-window-h.md#oh_windowmanager_setwindowtouchable) | - | 设置指定窗口是否可触。 |
| [int32\_t OH\_WindowManager\_SetWindowFocusable(int32\_t windowId, bool isFocusable)](capi-oh-window-h.md#oh_windowmanager_setwindowfocusable) | - | 设置指定窗口是否可获焦。 |
| [int32\_t OH\_WindowManager\_SetWindowBackgroundColor(int32\_t windowId, const char\* color)](capi-oh-window-h.md#oh_windowmanager_setwindowbackgroundcolor) | - | 设置指定窗口背景颜色。 |
| [int32\_t OH\_WindowManager\_SetWindowBrightness(int32\_t windowId, float brightness)](capi-oh-window-h.md#oh_windowmanager_setwindowbrightness) | - | 设置指定窗口的屏幕亮度。 |
| [int32\_t OH\_WindowManager\_SetWindowKeepScreenOn(int32\_t windowId, bool isKeepScreenOn)](capi-oh-window-h.md#oh_windowmanager_setwindowkeepscreenon) | - | 设置指定窗口是否开启屏幕常亮。 |
| [int32\_t OH\_WindowManager\_SetWindowPrivacyMode(int32\_t windowId, bool isPrivacy)](capi-oh-window-h.md#oh_windowmanager_setwindowprivacymode) | - | 设置指定窗口是否开启隐私模式。 |
| [int32\_t OH\_WindowManager\_GetWindowProperties(int32\_t windowId, WindowManager\_WindowProperties\* windowProperties)](capi-oh-window-h.md#oh_windowmanager_getwindowproperties) | - | 获取指定窗口属性。 |
| [int32\_t OH\_WindowManager\_Snapshot(int32\_t windowId, OH\_PixelmapNative\* pixelMap)](capi-oh-window-h.md#oh_windowmanager_snapshot) | - | 获取指定窗口截图。 |
| [int32\_t OH\_WindowManager\_GetAllWindowLayoutInfoList(int64\_t displayId,WindowManager\_Rect\*\* windowLayoutInfoList, size\_t\* windowLayoutInfoSize)](capi-oh-window-h.md#oh_windowmanager_getallwindowlayoutinfolist) | - | 获取指定屏幕上可见的窗口布局信息数组，按当前窗口层级排列，层级最高的对应数组下标为0。 |
| [void OH\_WindowManager\_ReleaseAllWindowLayoutInfoList(WindowManager\_Rect\* windowLayoutInfoList)](capi-oh-window-h.md#oh_windowmanager_releaseallwindowlayoutinfolist) | - | 释放窗口布局信息数组占用的内存。 |
| [int32\_t OH\_WindowManager\_InjectTouchEvent(int32\_t windowId, Input\_TouchEvent\* touchEvent, int32\_t windowX, int32\_t windowY)](capi-oh-window-h.md#oh_windowmanager_injecttouchevent) | - | 将多模触摸事件注入给目标窗口，仅支持注入同进程窗口，且该注入不会触发窗口焦点和层级变化，不会触发窗口拖拽，事件会直接发送给ArkUI。该接口需要在指定窗口加载UI之后调用。 |
| [int32\_t OH\_WindowManager\_GetAllMainWindowInfo(WindowManager\_MainWindowInfo\*\* infoList, size\_t\* mainWindowInfoSize)](capi-oh-window-h.md#oh_windowmanager_getallmainwindowinfo) | - | 获取全部主窗信息。 |
| [void OH\_WindowManager\_ReleaseAllMainWindowInfo(WindowManager\_MainWindowInfo\* infoList)](capi-oh-window-h.md#oh_windowmanager_releaseallmainwindowinfo) | - | 释放主窗口信息列表的内存。 |
| [typedef void (\*OH\_WindowManager\_WindowSnapshotCallback)(const OH\_PixelmapNative\*\* snapshotPixelMapList, size\_t snapshotListSize)](capi-oh-window-h.md#oh_windowmanager_windowsnapshotcallback) | OH\_WindowManager\_WindowSnapshotCallback | 接收主窗口截图列表的回调接口。 |
| [int32\_t OH\_WindowManager\_GetMainWindowSnapshot(int32\_t\* windowIdList, size\_t windowIdListSize, WindowManager\_WindowSnapshotConfig config, OH\_WindowManager\_WindowSnapshotCallback callback)](capi-oh-window-h.md#oh_windowmanager_getmainwindowsnapshot) | - | 获取一个或多个指定windowId的主窗口截图。 |
| [void OH\_WindowManager\_ReleaseMainWindowSnapshot(const OH\_PixelmapNative\* snapshotPixelMapList)](capi-oh-window-h.md#oh_windowmanager_releasemainwindowsnapshot) | - | 释放主窗口截图列表的内存。 |
| [int32\_t OH\_WindowManager\_LockCursor(int32\_t windowId, bool isCursorFollowMovement)](capi-oh-window-h.md#oh_windowmanager_lockcursor) | - | 锁定鼠标光标，控制鼠标光标不超过指定窗口区域，同时可控制光标是否跟随鼠标移动。仅支持获焦窗口调用，失焦之后会自动取消锁定。 |
| [int32\_t OH\_WindowManager\_UnlockCursor(int32\_t windowId)](capi-oh-window-h.md#oh_windowmanager_unlockcursor) | - | 清除窗口设置的鼠标光标指定的模式。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_WindowManager\_SetWindowStatusBarEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowStatusBarEnabled(int32_t windowId, bool enabled, bool enableAnimation)
```

**描述**

设置主窗口是否显示状态栏。

调用生效后返回并不表示状态栏的显示或隐藏已完成。主窗口在非全屏/最大化模式（智慧多窗悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 主窗口id。传入非主窗口id时调用无效。不存在对应窗口id时接口返回错误码WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL。 |
| bool enabled | 设置状态栏是否显示。true表示设置状态栏显示，false表示设置状态栏隐藏。 |
| bool enableAnimation | 设置是否开启状态栏的显隐动画。true表示开启状态栏的显隐动画，false表示关闭状态栏的显隐动画。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持功能。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowStatusBarColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowStatusBarColor(int32_t windowId, int32_t color)
```

**描述**

设置主窗口的状态栏内容颜色。

调用生效后返回并不表示状态栏的颜色更新已完成。主窗口在非全屏/最大化模式（智慧多窗悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 主窗口id。传入非主窗口id时调用无效。不存在对应窗口id时接口返回错误码WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL。 |
| int32\_t color | 要设置的颜色值，格式为ARGB。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持功能。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowNavigationBarEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowNavigationBarEnabled(int32_t windowId, bool enabled, bool enableAnimation)
```

**描述**

设置主窗口是否显示导航栏。HarmonyOS各设备不支持此能力。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 主窗口id。传入非主窗口id时调用无效。不存在对应窗口id时接口返回错误码WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL。 |
| bool enabled | 设置导航栏是否显示。true表示设置导航栏显示，false表示设置导航栏隐藏。 |
| bool enableAnimation | 设置是否开启导航栏的显隐动画。true表示开启导航栏的显隐动画，false表示关闭导航栏的显隐动画。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持功能。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_GetWindowAvoidArea()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_GetWindowAvoidArea(int32_t windowId, WindowManager_AvoidAreaType type, WindowManager_AvoidArea* avoidArea)
```

**描述**

获取指定窗口的避让区域。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| [WindowManager\_AvoidAreaType](capi-oh-window-comm-h.md#windowmanager_avoidareatype) type | 避让区域的类型。 |
| [WindowManager\_AvoidArea](capi-windowmanager-avoidarea.md)\* avoidArea | 返回指向指定窗口的避让区域的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功，返回指向对应窗口id的避让区域的指针。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_IsWindowShown()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_IsWindowShown(int32_t windowId, bool* isShow)
```

**描述**

判断指定窗口是否显示。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| bool\* isShow | 返回指定窗口是否显示的结果。true表示指定窗口显示，false表示指定窗口不显示，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。 |

### OH\_WindowManager\_ShowWindow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_ShowWindow(int32_t windowId)
```

**描述**

显示指定窗口。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowTouchable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowTouchable(int32_t windowId, bool isTouchable)
```

**描述**

设置指定窗口是否可触。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| bool isTouchable | 窗口是否可触。true表示窗口可触，false表示窗口不可触。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowFocusable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowFocusable(int32_t windowId, bool isFocusable)
```

**描述**

设置指定窗口是否可获焦。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| bool isFocusable | 窗口是否可获焦。true表示窗口可获焦，false表示窗口不可获焦。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowBackgroundColor(int32_t windowId, const char* color)
```

**描述**

设置指定窗口背景颜色。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| const char\* color | 设置窗口的背景色。该参数为字符串类型，格式为十六进制RGB或ARGB颜色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。 |

### OH\_WindowManager\_SetWindowBrightness()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowBrightness(int32_t windowId, float brightness)
```

**描述**

指定主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。

窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。

当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。

当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议窗口退至后台时调用此接口，否则可能引发时序问题。

**设备行为差异：**

* 针对TV设备：当前接口不生效也不报错。
* 针对非2in1设备（不包含TV设备）：
  + 在HarmonyOS 6.1.0之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。
  + 从HarmonyOS 6.1.0开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。
* 针对2in1设备：
  + 在HarmonyOS 5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。
  + 从HarmonyOS 5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| float brightness | 指定的屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowKeepScreenOn()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowKeepScreenOn(int32_t windowId, bool isKeepScreenOn)
```

**描述**

设置指定窗口是否开启屏幕常亮。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| bool isKeepScreenOn | 指定窗口是否开启屏幕常亮。true表示开启屏幕常亮，false表示关闭屏幕常亮。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_SetWindowPrivacyMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_SetWindowPrivacyMode(int32_t windowId, bool isPrivacy)
```

**描述**

设置指定窗口是否开启隐私模式。

**需要权限：** ohos.permission.PRIVACY\_WINDOW

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| bool isPrivacy | 指定窗口是否开启隐私模式。true表示开启隐私模式，false表示关闭隐私模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。  返回WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION，权限校验错误。 |

### OH\_WindowManager\_GetWindowProperties()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_GetWindowProperties(int32_t windowId, WindowManager_WindowProperties* windowProperties)
```

**描述**

获取指定窗口属性。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| [WindowManager\_WindowProperties](capi-windowmanager-windowproperties.md)\* windowProperties | 返回指向指定窗口的属性的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功，在windowProperties中返回窗口属性的指针。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。 |

### OH\_WindowManager\_Snapshot()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_Snapshot(int32_t windowId, OH_PixelmapNative* pixelMap)
```

**描述**

获取指定窗口截图。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。  窗口id非法或者窗口已经销毁，不能获取指定窗口截图，需要传入有效的窗口id才能成功获取指定窗口截图。  请通过窗口对象调用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)接口（ArkTS接口）获取有效的窗口id。 |
| [OH\_PixelmapNative](capi-struct.md)\* pixelMap | 返回指向指定窗口的截图的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功，在返回pixelMap中的像素图的指针。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_GetAllWindowLayoutInfoList()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_GetAllWindowLayoutInfoList(int64_t displayId,WindowManager_Rect** windowLayoutInfoList, size_t* windowLayoutInfoSize)
```

**描述**

获取指定屏幕上可见的窗口布局信息数组，按当前窗口层级排列，层级最高的对应数组下标为0。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t displayId | 指定屏幕的id。请通过窗口对象调用[getWindowProperties()](arkts-apis-window-window.md#getwindowproperties9)接口（ArkTS接口）获取有效的屏幕id。 |
| [WindowManager\_Rect](capi-windowmanager-rect.md)\*\* windowLayoutInfoList | 指定屏幕上可见的窗口布局信息数组的数组指针，作为出参使用。 |
| size\_t\* windowLayoutInfoSize | 指定屏幕上可见的窗口布局信息数组长度的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功，返回指定屏幕上可见的窗口布局信息数组的数组指针和数组长度的指针。  返回WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持功能。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_ReleaseAllWindowLayoutInfoList()

PhonePC/2in1TabletTVWearable

```
1. void OH_WindowManager_ReleaseAllWindowLayoutInfoList(WindowManager_Rect* windowLayoutInfoList)
```

**描述**

释放窗口布局信息数组占用的内存。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [WindowManager\_Rect](capi-windowmanager-rect.md)\* windowLayoutInfoList | 指定屏幕上可见的窗口布局信息数组的数组指针，可通过[OH\_WindowManager\_GetAllWindowLayoutInfoList](capi-oh-window-h.md#oh_windowmanager_getallwindowlayoutinfolist)接口获取。 |

### OH\_WindowManager\_InjectTouchEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_InjectTouchEvent(int32_t windowId, Input_TouchEvent* touchEvent, int32_t windowX, int32_t windowY)
```

**描述**

将多模触摸事件注入给目标窗口，仅支持注入同进程窗口，且该注入不会触发窗口焦点和层级变化，不会触发窗口拖拽，事件会直接发送给ArkUI。该接口需要在指定窗口加载UI之后调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口id。默认值为0。该参数为整数。 |
| [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 多模触摸事件，具体可见[Input\_TouchEvent](capi-input-input-touchevent.md)，事件定义在oh\_input\_manager.h中。该参数包含的部分字段有参数限制，其中，action应为大于等于0且小于等于3的整数；id、displayX、displayY和actionTime应为不小于0的整数。以上参数不符合限制条件会返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示：窗口管理器服务异常。 |
| int32\_t windowX | 注入事件相对于注入窗口的落点横坐标。该参数为整数。 |
| int32\_t windowY | 注入事件相对于注入窗口的落点纵坐标。该参数为整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_GetAllMainWindowInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_GetAllMainWindowInfo(WindowManager_MainWindowInfo** infoList, size_t* mainWindowInfoSize)
```

**描述**

获取全部主窗信息。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**需要权限：** ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [WindowManager\_MainWindowInfo](capi-windowmanager-windowmanager-mainwindowinfo.md)\*\* infoList | 指向主窗口信息列表的指针，作为出参使用。 |
| size\_t\* mainWindowInfoSize | 指向主窗口信息数组长度的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION，权限校验错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持功能。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_ReleaseAllMainWindowInfo()

PhonePC/2in1TabletTVWearable

```
1. void OH_WindowManager_ReleaseAllMainWindowInfo(WindowManager_MainWindowInfo* infoList)
```

**描述**

释放主窗口信息列表的内存。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [WindowManager\_MainWindowInfo](capi-windowmanager-windowmanager-mainwindowinfo.md)\* infoList | 主窗信息列表。 |

### OH\_WindowManager\_WindowSnapshotCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_WindowManager_WindowSnapshotCallback)(const OH_PixelmapNative** snapshotPixelMapList, size_t snapshotListSize)
```

**描述**

接收主窗口截图列表的回调接口。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PixelmapNative](capi-struct.md)\*\* snapshotPixelMapList | 窗口截图列表。 |
| size\_t snapshotListSize | 窗口截图列表的大小。 |

### OH\_WindowManager\_GetMainWindowSnapshot()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_GetMainWindowSnapshot(int32_t* windowIdList, size_t windowIdListSize, WindowManager_WindowSnapshotConfig config, OH_WindowManager_WindowSnapshotCallback callback)
```

**描述**

获取一个或多个指定windowId的主窗口截图。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**需要权限：** ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t\* windowIdList | 需要获取截图的主窗口ID列表。 |
| size\_t windowIdListSize | 主窗口ID列表的长度。 |
| [WindowManager\_WindowSnapshotConfig](i-windowmanager-windowmanager-windowsnapshotconfig.md) config | 获取窗口截图时的配置信息。 |
| [OH\_WindowManager\_WindowSnapshotCallback](capi-oh-window-h.md#oh_windowmanager_windowsnapshotcallback) callback | 获取窗口截图的回调对象。用于返回窗口截图列表，并按照指定的窗口ID列表顺序排列。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION，权限校验错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持功能。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_ReleaseMainWindowSnapshot()

PhonePC/2in1TabletTVWearable

```
1. void OH_WindowManager_ReleaseMainWindowSnapshot(const OH_PixelmapNative* snapshotPixelMapList)
```

**描述**

释放主窗口截图列表的内存。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PixelmapNative](capi-struct.md)\* snapshotPixelMapList | 窗口截图列表。 |

### OH\_WindowManager\_LockCursor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_LockCursor(int32_t windowId, bool isCursorFollowMovement)
```

**描述**

锁定鼠标光标，控制鼠标光标不超过指定窗口区域，同时可控制光标是否跟随鼠标移动。仅支持获焦窗口调用，失焦之后会自动取消锁定。

**需要权限：** ohos.permission.LOCK\_WINDOW\_CURSOR

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口ID。该参数为整数。 |
| bool isCursorFollowMovement | 设置鼠标光标的锁定模式，若为true，则光标会跟随鼠标移动；若为false，则光标不会跟随鼠标移动。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION，表示没有权限调用该接口。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持该设备。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |

### OH\_WindowManager\_UnlockCursor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_WindowManager_UnlockCursor(int32_t windowId)
```

**描述**

清除窗口设置的鼠标光标指定的模式。

**需要权限：** ohos.permission.LOCK\_WINDOW\_CURSOR

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 创建窗口时的窗口ID。该参数为整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION，表示没有权限调用该接口。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示不支持该设备。  返回WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL，表示窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL，表示窗口管理器服务异常。 |
