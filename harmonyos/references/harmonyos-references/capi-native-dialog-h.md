---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h
title: native_dialog.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_dialog.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1fa8d496f761af3511947234d93ef7d74a380f1ccfa686157de64920bec90479
---

## 概述

提供ArkUI在Native侧的自定义弹窗接口定义集合，支持创建、显示、更新、关闭自定义弹窗，以及设置弹窗样式、背景、边框、阴影等属性，支持注册弹窗生命周期事件监听，适用于需要在Native侧实现灵活弹窗交互的场景。

**引用文件：** <arkui/native\_dialog.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeDialogSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeDialogSample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NativeDialogAPI\_1](capi-arkui-nativemodule-arkui-nativedialogapi-1.md) | ArkUI\_NativeDialogAPI\_1 | ArkUI提供的Native侧自定义弹窗接口集合。 |
| [ArkUI\_NativeDialogAPI\_2](capi-arkui-nativemodule-arkui-nativedialogapi-2.md) | ArkUI\_NativeDialogAPI\_2 | ArkUI提供的Native侧自定义弹窗接口集合。 |
| [ArkUI\_NativeDialogAPI\_3](capi-arkui-nativemodule-arkui-nativedialogapi-3.md) | ArkUI\_NativeDialogAPI\_3 | ArkUI提供的Native侧自定义弹窗接口集合。 |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md) | ArkUI\_DialogDismissEvent | 定义弹窗关闭事件对象。 |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md) | ArkUI\_CustomDialogOptions | 定义自定义弹窗的配置选项。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_DismissReason](capi-native-dialog-h.md#arkui_dismissreason) | ArkUI\_DismissReason | 弹窗关闭的触发方式。 |
| [ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode) | ArkUI\_LevelMode | 设置弹窗显示层级。 |
| [ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode) | ArkUI\_ImmersiveMode | 指定嵌入式弹窗的蒙层覆盖区域。 |
| [OH\_ArkUI\_DialogDisplayModeInSubWindow](capi-native-dialog-h.md#oh_arkui_dialogdisplaymodeinsubwindow) | OH\_ArkUI\_DialogDisplayModeInSubWindow | 弹窗在子窗口中的显示模式。 |
| [ArkUI\_DialogState](capi-native-dialog-h.md#arkui_dialogstate) | ArkUI\_DialogState | 弹窗的状态。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef bool (\*ArkUI\_OnWillDismissEvent)(int32\_t reason)](capi-native-dialog-h.md#arkui_onwilldismissevent) | ArkUI\_OnWillDismissEvent | 弹窗关闭的回调函数。 |
| [void OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss(ArkUI\_DialogDismissEvent\* event, bool shouldBlockDismiss)](capi-native-dialog-h.md#oh_arkui_dialogdismissevent_setshouldblockdismiss) | - | 设置是否需要屏蔽系统关闭弹窗行为，true表示屏蔽系统行为，不关闭弹窗，false表示不屏蔽。 |
| [void\* OH\_ArkUI\_DialogDismissEvent\_GetUserData(ArkUI\_DialogDismissEvent\* event)](capi-native-dialog-h.md#oh_arkui_dialogdismissevent_getuserdata) | - | 获取弹窗关闭事件对象中的用户自定义数据指针。 |
| [int32\_t OH\_ArkUI\_DialogDismissEvent\_GetDismissReason(ArkUI\_DialogDismissEvent\* event)](capi-native-dialog-h.md#oh_arkui_dialogdismissevent_getdismissreason) | - | 获取弹窗关闭事件对象中的关闭原因。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_OpenDialog(ArkUI\_CustomDialogOptions\* options, void (\*callback)(int32\_t dialogId))](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog) | - | 弹出自定义弹窗。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_UpdateDialog(ArkUI\_CustomDialogOptions\* options, void (\*callback)(int32\_t dialogId))](capi-native-dialog-h.md#oh_arkui_customdialog_updatedialog) | - | 更新自定义弹窗。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_CloseDialog(int32\_t dialogId)](capi-native-dialog-h.md#oh_arkui_customdialog_closedialog) | - | 关闭自定义弹窗。 |
| [ArkUI\_CustomDialogOptions\* OH\_ArkUI\_CustomDialog\_CreateOptions(ArkUI\_NodeHandle content)](capi-native-dialog-h.md#oh_arkui_customdialog_createoptions) | - | 创建自定义弹窗配置。 |
| [void OH\_ArkUI\_CustomDialog\_DisposeOptions(ArkUI\_CustomDialogOptions\* options)](capi-native-dialog-h.md#oh_arkui_customdialog_disposeoptions) | - | 销毁自定义弹窗配置。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetLevelMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_LevelMode levelMode)](capi-native-dialog-h.md#oh_arkui_customdialog_setlevelmode) | - | 设置弹窗的显示层级。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetLevelUniqueId(ArkUI\_CustomDialogOptions\* options, int32\_t uniqueId)](capi-native-dialog-h.md#oh_arkui_customdialog_setleveluniqueid) | - | 设置弹窗显示层级页面下的节点id。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetImmersiveMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_ImmersiveMode immersiveMode)](capi-native-dialog-h.md#oh_arkui_customdialog_setimmersivemode) | - | 设置嵌入式弹窗蒙层的显示区域。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundColor(ArkUI\_CustomDialogOptions\* options, uint32\_t backgroundColor)](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundcolor) | - | 设置弹窗的背景颜色。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetCornerRadius(ArkUI\_CustomDialogOptions\* options, float topLeft, float topRight, float bottomLeft, float bottomRight)](capi-native-dialog-h.md#oh_arkui_customdialog_setcornerradius) | - | 设置弹窗的圆角半径。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBorderWidth(ArkUI\_CustomDialogOptions\* options, float top, float right, float bottom, float left, ArkUI\_LengthMetricUnit unit)](capi-native-dialog-h.md#oh_arkui_customdialog_setborderwidth) | - | 设置弹窗的边框宽度。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBorderColor(ArkUI\_CustomDialogOptions\* options, uint32\_t top, uint32\_t right, uint32\_t bottom, uint32\_t left)](capi-native-dialog-h.md#oh_arkui_customdialog_setbordercolor) | - | 设置弹窗的边框颜色。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBorderStyle(ArkUI\_CustomDialogOptions\* options, int32\_t top, int32\_t right, int32\_t bottom, int32\_t left)](capi-native-dialog-h.md#oh_arkui_customdialog_setborderstyle) | - | 设置弹窗的边框样式。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetWidth(ArkUI\_CustomDialogOptions\* options, float width, ArkUI\_LengthMetricUnit unit)](capi-native-dialog-h.md#oh_arkui_customdialog_setwidth) | - | 设置弹窗的背板宽度。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetHeight(ArkUI\_CustomDialogOptions\* options, float height, ArkUI\_LengthMetricUnit unit)](capi-native-dialog-h.md#oh_arkui_customdialog_setheight) | - | 设置弹窗的背板高度。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetShadow(ArkUI\_CustomDialogOptions\* options, ArkUI\_ShadowStyle shadow)](capi-native-dialog-h.md#oh_arkui_customdialog_setshadow) | - | 设置弹窗的背板阴影。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetCustomShadow(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* customShadow)](capi-native-dialog-h.md#oh_arkui_customdialog_setcustomshadow) | - | 设置弹窗的背板阴影。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle(ArkUI\_CustomDialogOptions\* options, ArkUI\_BlurStyle blurStyle)](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundblurstyle) | - | 设置弹窗的背板模糊材质。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetAlignment(ArkUI\_CustomDialogOptions\* options, int32\_t alignment, float offsetX, float offsetY)](capi-native-dialog-h.md#oh_arkui_customdialog_setalignment) | - | 设置弹窗的对齐模式。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetModalMode(ArkUI\_CustomDialogOptions\* options, bool isModal)](capi-native-dialog-h.md#oh_arkui_customdialog_setmodalmode) | - | 设置自定义弹窗是否开启模态样式的弹窗。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetAutoCancel(ArkUI\_CustomDialogOptions\* options, bool autoCancel)](capi-native-dialog-h.md#oh_arkui_customdialog_setautocancel) | - | 设置自定义弹窗是否允许点击遮罩层退出。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetSubwindowMode(ArkUI\_CustomDialogOptions\* options, bool showInSubwindow)](capi-native-dialog-h.md#oh_arkui_customdialog_setsubwindowmode) | - | 设置弹窗是否在子窗口显示此弹窗。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetDisplayModeInSubWindow(ArkUI\_CustomDialogOptions\* options, OH\_ArkUI\_DialogDisplayModeInSubWindow displayModeInSubWindow)](capi-native-dialog-h.md#oh_arkui_customdialog_setdisplaymodeinsubwindow) | - | 设置弹窗在子窗口中的显示模式。 |
| [int32\_t OH\_ArkUI\_NativeModule\_CustomDialog\_SetSystemMaterial(ArkUI\_NativeDialogHandle handle, ArkUI\_ImmersiveMaterialHandle material)](capi-native-dialog-h.md#oh_arkui_nativemodule_customdialog_setsystemmaterial) | - | 设置指定弹窗的沉浸式材质。 |
| [int32\_t OH\_ArkUI\_NativeModule\_CustomDialog\_SetSystemMaterialInOptions(ArkUI\_CustomDialogOptions\* options, ArkUI\_ImmersiveMaterialHandle material)](capi-native-dialog-h.md#oh_arkui_nativemodule_customdialog_setsystemmaterialinoptions) | - | 设置弹窗参数的沉浸式材质属性。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetMask(ArkUI\_CustomDialogOptions\* options, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)](capi-native-dialog-h.md#oh_arkui_customdialog_setmask) | - | 设置自定义弹窗遮罩属性。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetKeyboardAvoidMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_KeyboardAvoidMode keyboardAvoidMode)](capi-native-dialog-h.md#oh_arkui_customdialog_setkeyboardavoidmode) | - | 设置弹窗避让键盘的模式。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetHoverModeEnabled(ArkUI\_CustomDialogOptions\* options, bool enabled)](capi-native-dialog-h.md#oh_arkui_customdialog_sethovermodeenabled) | - | 设置弹窗是否响应悬停态。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetHoverModeArea(ArkUI\_CustomDialogOptions\* options, ArkUI\_HoverModeAreaType hoverModeAreaType)](capi-native-dialog-h.md#oh_arkui_customdialog_sethovermodearea) | - | 设置悬停态下弹窗默认展示区域。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillDismissCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))](capi-native-dialog-h.md#oh_arkui_customdialog_registeronwilldismisscallback) | - | 注册系统关闭自定义弹窗的监听事件。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillAppearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](capi-native-dialog-h.md#oh_arkui_customdialog_registeronwillappearcallback) | - | 注册自定义弹窗显示动效前的监听事件。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnDidAppearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](capi-native-dialog-h.md#oh_arkui_customdialog_registerondidappearcallback) | - | 注册自定义弹窗弹出时的监听事件。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillDisappearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](capi-native-dialog-h.md#oh_arkui_customdialog_registeronwilldisappearcallback) | - | 注册自定义弹窗退出动效前的监听事件。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnDidDisappearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](capi-native-dialog-h.md#oh_arkui_customdialog_registerondiddisappearcallback) | - | 注册自定义弹窗消失时的监听事件。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_GetState(ArkUI\_NativeDialogHandle handle, ArkUI\_DialogState\* state)](capi-native-dialog-h.md#oh_arkui_customdialog_getstate) | - | 获取弹窗的状态。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyleOptions(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* backgroundBlurStyleOptions)](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundblurstyleoptions) | - | 设置弹窗的背景模糊效果。 |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundEffect(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* backgroundEffect)](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundeffect) | - | 设置弹窗的背景效果参数。 |

## 枚举类型说明

### ArkUI\_DismissReason

```c
enum ArkUI_DismissReason
```

**描述：**

弹窗关闭的触发方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DIALOG\_DISMISS\_BACK\_PRESS = 0 | 点击三键back、侧滑（左滑/右滑）、键盘ESC触发。 |
| DIALOG\_DISMISS\_TOUCH\_OUTSIDE = 1 | 点击遮罩层触发。 |
| DIALOG\_DISMISS\_CLOSE\_BUTTON = 2 | 点击关闭按钮。 |
| DIALOG\_DISMISS\_SLIDE\_DOWN = 3 | 下拉关闭。 |

### ArkUI\_LevelMode

```c
enum ArkUI_LevelMode
```

**描述：**

设置弹窗显示层级。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LEVEL\_MODE\_OVERLAY = 0 | 显示在应用最上层。 |
| ARKUI\_LEVEL\_MODE\_EMBEDDED = 1 | 嵌入式显示在应用的页面内。 |

### ArkUI\_ImmersiveMode

```c
enum ArkUI_ImmersiveMode
```

**描述：**

指定嵌入式弹窗的蒙层覆盖区域。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMMERSIVE\_MODE\_DEFAULT = 0 | 弹窗蒙层按照显示页面给定的布局约束显示。 |
| ARKUI\_IMMERSIVE\_MODE\_EXTEND = 1 | 弹窗蒙层可扩展至覆盖状态栏和导航条。 |

### OH\_ArkUI\_DialogDisplayModeInSubWindow

```c
enum OH_ArkUI_DialogDisplayModeInSubWindow
```

**描述：**

弹窗在子窗口中的显示模式。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARKUI\_DIALOG\_DISPLAY\_MODE\_SCREEN\_BASED = 0 | 弹窗在屏幕居中显示。 |
| OH\_ARKUI\_DIALOG\_DISPLAY\_MODE\_WINDOW\_BASED = 1 | 弹窗在应用窗口居中显示。 |

### ArkUI\_DialogState

```c
enum ArkUI_DialogState
```

**描述：**

弹窗的状态。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| DIALOG\_UNINITIALIZED = 0 | 未初始化，控制器未与dialog绑定时。 |
| DIALOG\_INITIALIZED = 1 | 已初始化，控制器与dialog绑定后。 |
| DIALOG\_APPEARING = 2 | 显示中，dialog显示动画过程中。 |
| DIALOG\_APPEARED = 3 | 已显示，dialog显示动画结束。 |
| DIALOG\_DISAPPEARING = 4 | 消失中，dialog消失动画过程中。 |
| DIALOG\_DISAPPEARED = 5 | 已消失，dialog消失动画结束后。 |

## 函数说明

### ArkUI\_OnWillDismissEvent()

```c
typedef bool (*ArkUI_OnWillDismissEvent)(int32_t reason)
```

**描述：**

弹窗关闭的回调函数。

**起始版本：** 12

**参数:**

| 参数项 | 描述 |
| --- | --- |
| int32\_t reason | 触发弹窗关闭的原因，取值为[ArkUI\_DismissReason](capi-native-dialog-h.md#arkui_dismissreason)枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回任意值都表示不关闭弹窗。 |

### OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss()

```c
void OH_ArkUI_DialogDismissEvent_SetShouldBlockDismiss(ArkUI_DialogDismissEvent* event, bool shouldBlockDismiss)
```

**描述：**

设置是否需要屏蔽系统关闭弹窗行为。true表示屏蔽系统行为，不关闭弹窗；false表示不屏蔽。当弹窗中有用户未完成的重要操作（如表单填写未保存、支付确认等）时，可以通过设置shouldBlockDismiss为true来阻止用户通过点击三键back、侧滑、键盘ESC等系统方式关闭弹窗，强制用户完成操作或点击关闭按钮。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md)\* event | 弹窗关闭事件对象指针。 |
| bool shouldBlockDismiss | 是否需要屏蔽系统关闭弹窗行为。true表示屏蔽系统行为，不关闭弹窗；false表示不屏蔽，允许系统关闭弹窗。 |

### OH\_ArkUI\_DialogDismissEvent\_GetUserData()

```c
void* OH_ArkUI_DialogDismissEvent_GetUserData(ArkUI_DialogDismissEvent* event)
```

**描述：**

获取弹窗关闭事件对象中的用户自定义数据指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md)\* event | 弹窗关闭事件对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 返回注册回调时传入的用户自定义数据指针，常用于在回调函数中获取上下文信息。 |

### OH\_ArkUI\_DialogDismissEvent\_GetDismissReason()

```c
int32_t OH_ArkUI_DialogDismissEvent_GetDismissReason(ArkUI_DialogDismissEvent* event)
```

**描述：**

获取弹窗关闭事件对象中的关闭原因。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md)\* event | 弹窗关闭事件对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 关闭原因，异常情况返回-1。  [DIALOG\_DISMISS\_BACK\_PRESS](capi-native-dialog-h.md#arkui_dismissreason) 点击三键back、侧滑（左滑/右滑）、键盘ESC触发。  [DIALOG\_DISMISS\_TOUCH\_OUTSIDE](capi-native-dialog-h.md#arkui_dismissreason) 点击遮罩层触发。  [DIALOG\_DISMISS\_CLOSE\_BUTTON](capi-native-dialog-h.md#arkui_dismissreason) 点击关闭按钮。  [DIALOG\_DISMISS\_SLIDE\_DOWN](capi-native-dialog-h.md#arkui_dismissreason) 下拉关闭。 |

### OH\_ArkUI\_CustomDialog\_OpenDialog()

```c
int32_t OH_ArkUI_CustomDialog_OpenDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))
```

**描述：**

弹出自定义弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void (\*callback)(int32\_t dialogId) | 开启弹窗的回调，返回弹窗ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_UpdateDialog()

```c
int32_t OH_ArkUI_CustomDialog_UpdateDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))
```

**描述：**

更新自定义弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void (\*callback)(int32\_t dialogId) | 更新弹窗的回调，返回弹窗ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_CloseDialog()

```c
int32_t OH_ArkUI_CustomDialog_CloseDialog(int32_t dialogId)
```

**描述：**

关闭自定义弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t dialogId | 需要关闭的弹窗ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_CreateOptions()

```c
ArkUI_CustomDialogOptions* OH_ArkUI_CustomDialog_CreateOptions(ArkUI_NodeHandle content)
```

**描述：**

创建自定义弹窗配置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) content | 自定义弹窗的内容节点指针，类型为ArkUI\_NodeHandle。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* | 自定义弹窗配置的指针。 |

### OH\_ArkUI\_CustomDialog\_DisposeOptions()

```c
void OH_ArkUI_CustomDialog_DisposeOptions(ArkUI_CustomDialogOptions* options)
```

**描述：**

销毁自定义弹窗配置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 自定义弹窗配置的指针。 |

### OH\_ArkUI\_CustomDialog\_SetLevelMode()

```c
int32_t OH_ArkUI_CustomDialog_SetLevelMode(ArkUI_CustomDialogOptions* options, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 指向自定义弹窗options的指针。 |
| [ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode) levelMode | 弹窗显示层级的枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetLevelUniqueId()

```c
int32_t OH_ArkUI_CustomDialog_SetLevelUniqueId(ArkUI_CustomDialogOptions* options, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 指向自定义弹窗options的指针。 |
| int32\_t uniqueId | 指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetImmersiveMode()

```c
int32_t OH_ArkUI_CustomDialog_SetImmersiveMode(ArkUI_CustomDialogOptions* options, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 指向自定义弹窗options的指针。 |
| [ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode) immersiveMode | 嵌入式弹窗蒙层覆盖区域的枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundColor()

```c
int32_t OH_ArkUI_CustomDialog_SetBackgroundColor(ArkUI_CustomDialogOptions* options, uint32_t backgroundColor)
```

**描述：**

设置弹窗的背景颜色。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| uint32\_t backgroundColor | 弹窗背景颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetCornerRadius()

```c
int32_t OH_ArkUI_CustomDialog_SetCornerRadius(ArkUI_CustomDialogOptions* options, float topLeft, float topRight, float bottomLeft, float bottomRight)
```

**描述：**

设置弹窗的圆角半径。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float topLeft | 弹窗左上角的圆角半径，单位：vp。默认值：32vp。 |
| float topRight | 弹窗右上角的圆角半径，单位：vp。默认值：32vp。 |
| float bottomLeft | 弹窗左下角的圆角半径，单位：vp。默认值：32vp。 |
| float bottomRight | 弹窗右下角的圆角半径，单位：vp。默认值：32vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBorderWidth()

```c
int32_t OH_ArkUI_CustomDialog_SetBorderWidth(ArkUI_CustomDialogOptions* options, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的边框宽度。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float top | 弹窗上边框的宽度，单位：vp。 |
| float right | 弹窗右边框的宽度，单位：vp。 |
| float bottom | 弹窗下边框的宽度，单位：vp。 |
| float left | 弹窗左边框的宽度，单位：vp。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 指定宽度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBorderColor()

```c
int32_t OH_ArkUI_CustomDialog_SetBorderColor(ArkUI_CustomDialogOptions* options, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left)
```

**描述：**

设置弹窗的边框颜色。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| uint32\_t top | 弹窗上边框的颜色，0xARGB格式。 |
| uint32\_t right | 弹窗右边框的颜色，0xARGB格式。 |
| uint32\_t bottom | 弹窗下边框的颜色，0xARGB格式。 |
| uint32\_t left | 弹窗左边框的颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBorderStyle()

```c
int32_t OH_ArkUI_CustomDialog_SetBorderStyle(ArkUI_CustomDialogOptions* options, int32_t top, int32_t right, int32_t bottom, int32_t left)
```

**描述：**

设置弹窗的边框样式。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| int32\_t top | 弹窗上边框的样式，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t right | 弹窗右边框的样式，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t bottom | 弹窗下边框的样式，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t left | 弹窗左边框的样式，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetWidth()

```c
int32_t OH_ArkUI_CustomDialog_SetWidth(ArkUI_CustomDialogOptions* options, float width, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的背板宽度。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float width | 弹窗的背板宽度，单位：vp。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 指定宽度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetHeight()

```c
int32_t OH_ArkUI_CustomDialog_SetHeight(ArkUI_CustomDialogOptions* options, float height, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的背板高度。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float height | 弹窗的背板高度，单位：vp。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 指定高度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetShadow()

```c
int32_t OH_ArkUI_CustomDialog_SetShadow(ArkUI_CustomDialogOptions* options, ArkUI_ShadowStyle shadow)
```

**描述：**

设置弹窗的背板阴影。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_ShadowStyle](capi-native-type-visual-h.md#arkui_shadowstyle) shadow | 弹窗的背板阴影样式，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetCustomShadow()

```c
int32_t OH_ArkUI_CustomDialog_SetCustomShadow(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* customShadow)
```

**描述：**

设置弹窗的背板阴影。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [const ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)\* customShadow | 弹窗的自定义阴影参数，格式与[ArkUI\_NodeAttributeType](capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_CUSTOM\_SHADOW属性一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle()

```c
int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyle(ArkUI_CustomDialogOptions* options, ArkUI_BlurStyle blurStyle)
```

**描述：**

设置弹窗的背板模糊材质。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_BlurStyle](capi-native-type-visual-h.md#arkui_blurstyle) blurStyle | 弹窗的背板模糊材质，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetAlignment()

```c
int32_t OH_ArkUI_CustomDialog_SetAlignment(ArkUI_CustomDialogOptions* options, int32_t alignment, float offsetX, float offsetY)
```

**描述：**

设置弹窗的对齐模式。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| int32\_t alignment | 弹窗的对齐模式，参数类型[ArkUI\_Alignment](capi-layout-h.md#arkui_alignment)。 |
| float offsetX | 弹窗的水平偏移量，浮点型，单位：vp。 |
| float offsetY | 弹窗的垂直偏移量，浮点型，单位：vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetModalMode()

```c
int32_t OH_ArkUI_CustomDialog_SetModalMode(ArkUI_CustomDialogOptions* options, bool isModal)
```

**描述：**

设置自定义弹窗是否开启模态窗口模式。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool isModal | 设置是否开启模态窗口模式。模态窗口模式有蒙层，非模态窗口模式无蒙层。设置为true表示开启模态窗口模式。设置为false表示关闭模态窗口模式。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetAutoCancel()

```c
int32_t OH_ArkUI_CustomDialog_SetAutoCancel(ArkUI_CustomDialogOptions* options, bool autoCancel)
```

**描述：**

设置是否允许通过点击遮罩层退出自定义弹窗。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool autoCancel | 是否允许点击遮罩层退出弹窗。true表示允许退出，false表示不允许退出。  默认值：true |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetSubwindowMode()

```c
int32_t OH_ArkUI_CustomDialog_SetSubwindowMode(ArkUI_CustomDialogOptions* options, bool showInSubwindow)
```

**描述：**

设置弹窗是否在子窗口显示。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

配合[OH\_ArkUI\_CustomDialog\_SetDisplayModeInSubWindow](capi-native-dialog-h.md#oh_arkui_customdialog_setdisplaymodeinsubwindow)方法使用时，可进一步设置弹窗在子窗口中的显示模式。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool showInSubwindow | 是否在子窗口显示弹窗。值为true：弹窗可以显示在主窗口外，独立子窗口。值为false：弹窗显示在应用内，非独立子窗口。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_CustomDialog\_SetSystemMaterial()

```c
int32_t OH_ArkUI_NativeModule_CustomDialog_SetSystemMaterial(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMaterialHandle material)
```

**描述：**

设置指定弹窗的沉浸式材质。沉浸式材质根据设备算力等级分为不同等级。材质等级由[ArkUI\_MaterialLevel](capi-native-material-h.md#arkui_materiallevel)定义，可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取。在高算力和中算力设备上，会影响材质层的滤镜效果和阴影（[OH\_ArkUI\_CustomDialog\_SetShadow](capi-native-dialog-h.md#oh_arkui_customdialog_setshadow)或[OH\_ArkUI\_CustomDialog\_SetCustomShadow](capi-native-dialog-h.md#oh_arkui_customdialog_setcustomshadow)）、背景模糊[OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundblurstyle)、背景效果[OH\_ArkUI\_CustomDialog\_SetBackgroundEffect](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundeffect)效果。在低算力设备上，会影响背景颜色[OH\_ArkUI\_CustomDialog\_SetBackgroundColor](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundcolor)、背景模糊[OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundblurstyle)、背景效果[OH\_ArkUI\_CustomDialog\_SetBackgroundEffect](capi-native-dialog-h.md#oh_arkui_customdialog_setbackgroundeffect)、边框颜色[OH\_ArkUI\_CustomDialog\_SetBorderColor](capi-native-dialog-h.md#oh_arkui_customdialog_setbordercolor)、边框宽度[OH\_ArkUI\_CustomDialog\_SetBorderWidth](capi-native-dialog-h.md#oh_arkui_customdialog_setborderwidth)和阴影（[OH\_ArkUI\_CustomDialog\_SetShadow](capi-native-dialog-h.md#oh_arkui_customdialog_setshadow)或[OH\_ArkUI\_CustomDialog\_SetCustomShadow](capi-native-dialog-h.md#oh_arkui_customdialog_setcustomshadow)）效果。依据设备算力档位自动生效交互形变和流光效果，高算力设备生效交互形变和流光效果，中算力设备生效交互形变效果，低算力设备不生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_CustomDialog\_SetSystemMaterialInOptions()

```c
int32_t OH_ArkUI_NativeModule_CustomDialog_SetSystemMaterialInOptions(ArkUI_CustomDialogOptions* options, ArkUI_ImmersiveMaterialHandle material)
```

**描述：**

设置弹窗参数的沉浸式材质属性。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 指向弹窗参数对象的指针。 |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetDisplayModeInSubWindow()

```c
int32_t OH_ArkUI_CustomDialog_SetDisplayModeInSubWindow(ArkUI_CustomDialogOptions* options, OH_ArkUI_DialogDisplayModeInSubWindow displayModeInSubWindow)
```

**描述：**

设置弹窗在子窗口中的显示模式。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

本方法仅在弹窗通过[OH\_ArkUI\_CustomDialog\_SetSubwindowMode](capi-native-dialog-h.md#oh_arkui_customdialog_setsubwindowmode)设置为子窗口显示时生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [OH\_ArkUI\_DialogDisplayModeInSubWindow](capi-native-dialog-h.md#oh_arkui_dialogdisplaymodeinsubwindow) displayModeInSubWindow | 弹窗在子窗口中的显示模式，类型为[OH\_ArkUI\_DialogDisplayModeInSubWindow](capi-native-dialog-h.md#oh_arkui_dialogdisplaymodeinsubwindow)。  默认值：OH\_ARKUI\_DIALOG\_DISPLAY\_MODE\_SCREEN\_BASED |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetMask()

```c
int32_t OH_ArkUI_CustomDialog_SetMask(ArkUI_CustomDialogOptions* options, uint32_t maskColor, const ArkUI_Rect* maskRect)
```

**描述：**

设置自定义弹窗遮罩属性。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| uint32\_t maskColor | 弹窗的遮罩颜色，0xARGB格式。 |
| [const ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md)\* maskRect | 遮罩层区域范围的指针，遮罩层区域内的事件不透传，在遮罩层区域外的事件透传。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetKeyboardAvoidMode()

```c
int32_t OH_ArkUI_CustomDialog_SetKeyboardAvoidMode(ArkUI_CustomDialogOptions* options, ArkUI_KeyboardAvoidMode keyboardAvoidMode)
```

**描述：**

设置弹窗避让键盘的模式。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_KeyboardAvoidMode](capi-native-type-h.md#arkui_keyboardavoidmode) keyboardAvoidMode | 键盘避让模式，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetHoverModeEnabled()

```c
int32_t OH_ArkUI_CustomDialog_SetHoverModeEnabled(ArkUI_CustomDialogOptions* options, bool enabled)
```

**描述：**

设置弹窗是否响应悬停态。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool enabled | 是否响应悬停态。true表示响应，false表示不响应。默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetHoverModeArea()

```c
int32_t OH_ArkUI_CustomDialog_SetHoverModeArea(ArkUI_CustomDialogOptions* options, ArkUI_HoverModeAreaType hoverModeAreaType)
```

**描述：**

设置悬停态下弹窗默认展示区域。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_HoverModeAreaType](capi-native-type-h.md#arkui_hovermodeareatype) hoverModeAreaType | 悬停态区域，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnWillDismissCallback()

```c
int32_t OH_ArkUI_CustomDialog_RegisterOnWillDismissCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))
```

**描述：**

注册系统关闭自定义弹窗的监听事件。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(ArkUI\_DialogDismissEvent\* event) | 监听自定义弹窗关闭的回调事件。  - event: 回调函数的入参，捕获关闭原因。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnWillAppearCallback()

```c
int32_t OH_ArkUI_CustomDialog_RegisterOnWillAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗显示动效前的监听事件。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗显示动效前的事件回调。入参userData为用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnDidAppearCallback()

```c
int32_t OH_ArkUI_CustomDialog_RegisterOnDidAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗弹出时的监听事件。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗弹出后的事件回调。入参userData为用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnWillDisappearCallback()

```c
int32_t OH_ArkUI_CustomDialog_RegisterOnWillDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗退出动效前的监听事件。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗退出动效前的事件回调。入参userData为用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnDidDisappearCallback()

```c
int32_t OH_ArkUI_CustomDialog_RegisterOnDidDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗消失时的监听事件。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗消失时的事件回调。入参userData为用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_GetState()

```c
int32_t OH_ArkUI_CustomDialog_GetState(ArkUI_NativeDialogHandle handle, ArkUI_DialogState* state)
```

**描述：**

获取弹窗的状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_DialogState](capi-native-dialog-h.md#arkui_dialogstate)\* state | 自定义弹窗的状态指针，用于接收返回的状态值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyleOptions()

```c
int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyleOptions(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundBlurStyleOptions)
```

**描述：**

设置弹窗的背景模糊效果。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [const ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)\* backgroundBlurStyleOptions | 弹窗的背景模糊效果。参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。  .value[1]?.i32：表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[2]?.f32：表示模糊效果程度，取[0.0,1.0]范围内的值，超出有效值区间时，小于0.0取0.0，大于1.0取1.0。  .value[3]?.u32：表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[4]?.u32：表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[5]?.i32：表示模糊激活策略，取[ArkUI\_BlurStyleActivePolicy](capi-native-type-visual-h.md#arkui_blurstyleactivepolicy)枚举值。  .value[6]?.u32：表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xARGB类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundEffect()

```c
int32_t OH_ArkUI_CustomDialog_SetBackgroundEffect(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundEffect)
```

**描述：**

设置弹窗的背景效果参数。

**说明** 

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [const ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)\* backgroundEffect | 弹窗的背景效果参数。参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：表示模糊半径，单位为vp。  .value[1]?.f32：表示饱和度。  .value[2]?.f32：表示亮度。  .value[3]?.u32：表示颜色，0xARGB类型。  .value[4]?.i32：表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[5]?.u32：表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[6]?.u32：表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[7]?.i32：表示模糊激活策略，取[ArkUI\_BlurStyleActivePolicy](capi-native-type-visual-h.md#arkui_blurstyleactivepolicy)枚举值。  .value[8]?.u32：表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xARGB类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |
