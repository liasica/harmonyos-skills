---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h
title: native_dialog.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_dialog.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:065bad6395e35349926121f8e943b31342200c8909ea3413549c36005a86b0d3
---

## 概述

PhonePC/2in1TabletTVWearable

提供ArkUI在Native侧的自定义弹窗接口定义集合。

**引用文件：** <arkui/native\_dialog.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeDialogSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeDialogSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NativeDialogAPI\_1](capi-arkui-nativemodule-arkui-nativedialogapi-1.md) | ArkUI\_NativeDialogAPI\_1 | ArkUI提供的Native侧自定义弹窗接口集合。 |
| [ArkUI\_NativeDialogAPI\_2](capi-arkui-nativemodule-arkui-nativedialogapi-2.md) | ArkUI\_NativeDialogAPI\_2 | ArkUI提供的Native侧自定义弹窗接口集合。 |
| [ArkUI\_NativeDialogAPI\_3](capi-arkui-nativemodule-arkui-nativedialogapi-3.md) | ArkUI\_NativeDialogAPI\_3 | ArkUI提供的Native侧自定义弹窗接口集合。 |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md) | ArkUI\_DialogDismissEvent | 定义弹窗关闭事件对象。 |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md) | ArkUI\_CustomDialogOptions | 定义自定义弹窗的内容对象。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_DismissReason](capi-native-dialog-h.md#arkui_dismissreason) | ArkUI\_DismissReason | 弹窗关闭的触发方式。 |
| [ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode) | ArkUI\_LevelMode | 设置弹窗显示层级。 |
| [ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode) | ArkUI\_ImmersiveMode | 指定嵌入式弹窗的蒙层覆盖区域。 |
| [ArkUI\_DialogState](capi-native-dialog-h.md#arkui_dialogstate) | ArkUI\_DialogState | 枚举对话框的状态。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef bool (\*ArkUI\_OnWillDismissEvent)(int32\_t reason)](capi-native-dialog-h.md#arkui_onwilldismissevent) | ArkUI\_OnWillDismissEvent | 弹窗关闭的回调函数。 |
| [void OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss(ArkUI\_DialogDismissEvent\* event, bool shouldBlockDismiss)](capi-native-dialog-h.md#oh_arkui_dialogdismissevent_setshouldblockdismiss) | - | 设置是否需要屏蔽系统关闭弹窗行为，true表示屏蔽系统行为，不关闭弹窗，false表示不屏蔽。 |
| [void\* OH\_ArkUI\_DialogDismissEvent\_GetUserData(ArkUI\_DialogDismissEvent\* event)](capi-native-dialog-h.md#oh_arkui_dialogdismissevent_getuserdata) | - | 获取弹窗关闭事件对象中的用户自定义数据指针。 |
| [int32\_t OH\_ArkUI\_DialogDismissEvent\_GetDismissReason(ArkUI\_DialogDismissEvent\* event)](capi-native-dialog-h.md#oh_arkui_dialogdismissevent_getdismissreason) | - | 获取交互式关闭事件指针中的关闭原因。 |
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

PhonePC/2in1TabletTVWearable

### ArkUI\_DismissReason

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DismissReason
```

**描述：**

弹窗关闭的触发方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DIALOG\_DISMISS\_BACK\_PRESS = 0 | 点击三键back、侧滑（左滑/右滑）、键盘ESC触发。 |
| DIALOG\_DISMISS\_TOUCH\_OUTSIDE = 1 | 点击遮障层触发。 |
| DIALOG\_DISMISS\_CLOSE\_BUTTON = 2 | 点击关闭按钮。 |
| DIALOG\_DISMISS\_SLIDE\_DOWN = 3 | 下拉关闭。 |

### ArkUI\_LevelMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_LevelMode
```

**描述：**

设置弹窗显示层级。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LEVEL\_MODE\_OVERLAY = 0 | 显示在应用最上层。 |
| ARKUI\_LEVEL\_MODE\_EMBEDDED = 1 | 嵌入式显示在应用的页面内。 |

### ArkUI\_ImmersiveMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_ImmersiveMode
```

**描述：**

指定嵌入式弹窗的蒙层覆盖区域。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMMERSIVE\_MODE\_DEFAULT = 0 | 弹窗蒙层按照显示页面给定的布局约束显示。 |
| ARKUI\_IMMERSIVE\_MODE\_EXTEND = 1 | 弹窗蒙层可扩展至覆盖状态栏和导航条。 |

### ArkUI\_DialogState

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DialogState
```

**描述：**

枚举对话框的状态。

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

PhonePC/2in1TabletTVWearable

### ArkUI\_OnWillDismissEvent()

PhonePC/2in1TabletTVWearable

```
1. typedef bool (*ArkUI_OnWillDismissEvent)(int32_t reason)
```

**描述：**

弹窗关闭的回调函数。

**起始版本：** 12

**参数:**

| 名称 | 描述 |
| --- | --- |
| reason | 触发弹窗关闭的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回任意值都表示不关闭弹窗。 |

### OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DialogDismissEvent_SetShouldBlockDismiss(ArkUI_DialogDismissEvent* event, bool shouldBlockDismiss)
```

**描述：**

设置是否需要屏蔽系统关闭弹窗行为，true表示屏蔽系统行为，不关闭弹窗，false表示不屏蔽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md)\* event | 弹窗关闭事件对象指针。 |
| bool shouldBlockDismiss | 实现需要屏蔽系统关闭弹窗行为。 |

### OH\_ArkUI\_DialogDismissEvent\_GetUserData()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_DialogDismissEvent_GetUserData(ArkUI_DialogDismissEvent* event)
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
| void\* | 用户自定义数据指针。 |

### OH\_ArkUI\_DialogDismissEvent\_GetDismissReason()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DialogDismissEvent_GetDismissReason(ArkUI_DialogDismissEvent* event)
```

**描述：**

获取交互式关闭事件指针中的关闭原因。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DialogDismissEvent](capi-arkui-nativemodule-arkui-dialogdismissevent.md)\* event | 弹窗关闭事件对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 关闭原因，异常情况返回-1。  [DIALOG\_DISMISS\_BACK\_PRESS](capi-native-dialog-h.md#arkui_dismissreason) 点击三键back、侧滑（左滑/右滑）、键盘ESC关闭。  [DIALOG\_DISMISS\_TOUCH\_OUTSIDE](capi-native-dialog-h.md#arkui_dismissreason) 点击遮障层时。  [DIALOG\_DISMISS\_CLOSE\_BUTTON](capi-native-dialog-h.md#arkui_dismissreason) 点击关闭按钮。  [DIALOG\_DISMISS\_SLIDE\_DOWN](capi-native-dialog-h.md#arkui_dismissreason) 下拉关闭。 |

### OH\_ArkUI\_CustomDialog\_OpenDialog()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_OpenDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))
```

**描述：**

弹出自定义弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void (\*callback)(int32\_t dialogId) | 开启弹窗的回调，返回入参是弹窗ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_UpdateDialog()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_UpdateDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))
```

**描述：**

更新自定义弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void (\*callback)(int32\_t dialogId) | 更新弹窗的回调，返回入参是弹窗ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_CloseDialog()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_CloseDialog(int32_t dialogId)
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
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_CreateOptions()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_CustomDialogOptions* OH_ArkUI_CustomDialog_CreateOptions(ArkUI_NodeHandle content)
```

**描述：**

创建自定义弹窗配置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) content | 自定义弹窗的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* | 自定义弹窗配置的指针。 |

### OH\_ArkUI\_CustomDialog\_DisposeOptions()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_CustomDialog_DisposeOptions(ArkUI_CustomDialogOptions* options)
```

**描述：**

销毁自定义弹窗配置。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 自定义弹窗配置的指针。 |

### OH\_ArkUI\_CustomDialog\_SetLevelMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetLevelMode(ArkUI_CustomDialogOptions* options, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

说明

本方法需要在调用[OH\_ArkUI\_CustomDialog\_OpenDialog](capi-native-dialog-h.md#oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 指向自定义弹窗options的指针。 |
| [ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode) levelMode | 显示层级的枚举值， 类型为[ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetLevelUniqueId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetLevelUniqueId(ArkUI_CustomDialogOptions* options, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

说明

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
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetImmersiveMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetImmersiveMode(ArkUI_CustomDialogOptions* options, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 指向自定义弹窗options的指针。 |
| [ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode) immersiveMode | 显示区域类型的枚举值， 类型为[ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBackgroundColor(ArkUI_CustomDialogOptions* options, uint32_t backgroundColor)
```

**描述：**

设置弹窗的背景颜色。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| uint32\_t backgroundColor | 弹窗背景颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetCornerRadius()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetCornerRadius(ArkUI_CustomDialogOptions* options, float topLeft, float topRight, float bottomLeft, float bottomRight)
```

**描述：**

设置弹窗的圆角半径。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float topLeft | 弹窗左上角的圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float topRight | 弹窗右上角的圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float bottomLeft | 弹窗左下角的圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float bottomRight | 弹窗右下角的圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBorderWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBorderWidth(ArkUI_CustomDialogOptions* options, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的边框宽度。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float top | 弹窗上边框的宽度。 |
| float right | 弹窗右边框的宽度。 |
| float bottom | 弹窗下边框的宽度。 |
| float left | 弹窗左边框的宽度。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 指定宽度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBorderColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBorderColor(ArkUI_CustomDialogOptions* options, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left)
```

**描述：**

设置弹窗的边框颜色。

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
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBorderStyle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBorderStyle(ArkUI_CustomDialogOptions* options, int32_t top, int32_t right, int32_t bottom, int32_t left)
```

**描述：**

设置弹窗的边框样式。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| int32\_t top | 弹窗上边框的样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t right | 弹窗右边框的样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t bottom | 弹窗下边框的样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t left | 弹窗左边框的样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetWidth(ArkUI_CustomDialogOptions* options, float width, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的背板宽度。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float width | 弹窗的背板宽度。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 指定宽度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetHeight(ArkUI_CustomDialogOptions* options, float height, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的背板高度。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| float height | 弹窗的背板高度。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 指定高度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetShadow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetShadow(ArkUI_CustomDialogOptions* options, ArkUI_ShadowStyle shadow)
```

**描述：**

设置弹窗的背板阴影。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_ShadowStyle](capi-native-type-h.md#arkui_shadowstyle) shadow | 弹窗的背板阴影样式，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetCustomShadow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetCustomShadow(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* customShadow)
```

**描述：**

设置弹窗的背板阴影。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [const ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)\* customShadow | 弹窗的自定义阴影参数，格式与[ArkUI\_NodeAttributeType](capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_CUSTOM\_SHADOW属性一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyle(ArkUI_CustomDialogOptions* options, ArkUI_BlurStyle blurStyle)
```

**描述：**

设置弹窗的背板模糊材质。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle) blurStyle | 弹窗的背板模糊材质，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetAlignment()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetAlignment(ArkUI_CustomDialogOptions* options, int32_t alignment, float offsetX, float offsetY)
```

**描述：**

设置弹窗的对齐模式。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| int32\_t alignment | 弹窗的对齐模式，参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。 |
| float offsetX | 弹窗的水平偏移量，浮点型，单位：vp。 |
| float offsetY | 弹窗的垂直偏移量，浮点型，单位：vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetModalMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetModalMode(ArkUI_CustomDialogOptions* options, bool isModal)
```

**描述：**

设置自定义弹窗是否开启模态样式的弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool isModal | 设置是否开启模态窗口。模态窗口有蒙层，非模态窗口无蒙层。设置为true表示开启模态窗口。设置为false表示关闭模态窗口。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetAutoCancel()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetAutoCancel(ArkUI_CustomDialogOptions* options, bool autoCancel)
```

**描述：**

设置自定义弹窗是否允许点击遮罩层退出。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool autoCancel | 设置是否允许点击遮罩层退出，true表示关闭弹窗，false表示不关闭弹窗。  默认值：true |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetSubwindowMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetSubwindowMode(ArkUI_CustomDialogOptions* options, bool showInSubwindow)
```

**描述：**

设置弹窗是否在子窗口显示此弹窗。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool showInSubwindow | 设置弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true：弹窗可以显示在主窗口外，独立子窗口。值为false：弹窗显示在应用内，非独立子窗口。  默认值：false |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetMask()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetMask(ArkUI_CustomDialogOptions* options, uint32_t maskColor, const ArkUI_Rect* maskRect)
```

**描述：**

设置自定义弹窗遮罩属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| uint32\_t maskColor | 弹窗的遮罩颜色，0xargb格式。 |
| [const ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md)\* maskRect | 遮蔽层区域范围的指针，遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。参数类型[ArkUI\_Rect](capi-arkui-nativemodule-arkui-rect.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetKeyboardAvoidMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetKeyboardAvoidMode(ArkUI_CustomDialogOptions* options, ArkUI_KeyboardAvoidMode keyboardAvoidMode)
```

**描述：**

设置弹窗避让键盘的模式。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_KeyboardAvoidMode](capi-native-type-h.md#arkui_keyboardavoidmode) keyboardAvoidMode | 键盘避让模式，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetHoverModeEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetHoverModeEnabled(ArkUI_CustomDialogOptions* options, bool enabled)
```

**描述：**

设置弹窗是否响应悬停态。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| bool enabled | 是否响应悬停态，默认false。值为true时响应悬停态，值为false时不响应悬停态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetHoverModeArea()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetHoverModeArea(ArkUI_CustomDialogOptions* options, ArkUI_HoverModeAreaType hoverModeAreaType)
```

**描述：**

设置悬停态下弹窗默认展示区域。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [ArkUI\_HoverModeAreaType](capi-native-type-h.md#arkui_hovermodeareatype) hoverModeAreaType | 悬停态区域，枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnWillDismissCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_RegisterOnWillDismissCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))
```

**描述：**

注册系统关闭自定义弹窗的监听事件。

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
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnWillAppearCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_RegisterOnWillAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗显示动效前的监听事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗显示动效前的事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnDidAppearCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_RegisterOnDidAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗弹出时的监听事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗弹出后的事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnWillDisappearCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_RegisterOnWillDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗退出动效前的监听事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗退出动效前的事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_RegisterOnDidDisappearCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_RegisterOnDidDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗消失时的监听事件。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| void\* userData | 用户自定义数据指针。 |
| void (\*callback)(void\* userData) | 弹窗消失时的事件回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_GetState()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_GetState(ArkUI_NativeDialogHandle handle, ArkUI_DialogState* state)
```

**描述：**

获取弹窗的状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_DialogState](capi-native-dialog-h.md#arkui_dialogstate)\* state | 自定义弹窗的状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyleOptions()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyleOptions(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundBlurStyleOptions)
```

**描述：**

设置弹窗的背景模糊效果。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [const ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)\* backgroundBlurStyleOptions | 弹窗的背景模糊效果。参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。  .value[1]?.i32：表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[2]?.f32：表示模糊效果程度，取[0.0,1.0]范围内的值，超出有效值区间时取边界值。  .value[3]?.u32：表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[4]?.u32：表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[5]?.i32：表示模糊激活策略，取[ArkUI\_BlurStyleActivePolicy](capi-native-type-h.md#arkui_blurstyleactivepolicy)枚举值。  .value[6]?.u32：表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomDialog\_SetBackgroundEffect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CustomDialog_SetBackgroundEffect(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundEffect)
```

**描述：**

设置弹窗的背景效果参数。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_CustomDialogOptions](capi-arkui-nativemodule-arkui-customdialogoptions.md)\* options | 弹窗参数。 |
| [const ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)\* backgroundEffect | 弹窗的背景效果参数。参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：表示模糊半径，单位为vp。  .value[1]?.f32：表示饱和度。  .value[2]?.f32：表示亮度。  .value[3]?.u32：表示颜色，0xargb类型。  .value[4]?.i32：表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[5]?.u32：表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[6]?.u32：表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]，超出有效值范围，取0。  .value[7]?.i32：表示模糊激活策略，取[ArkUI\_BlurStyleActivePolicy](capi-native-type-h.md#arkui_blurstyleactivepolicy)枚举值。  .value[8]?.u32：表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
