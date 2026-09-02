---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-focus-h
title: native_interface_focus.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_interface_focus.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a2160d767d8b026191a26a1ef4762631f52c70cd17343aecc4b8ac1d55269d6a
---

## 概述

定义焦点管理的相关接口，主要用于主动转移焦点、管理控制焦点转移默认行为，以及控制焦点激活态，适用于页面切换、键盘导航等需要统一管理焦点状态和焦点转移行为的场景，有助于提升焦点控制的可预测性和交互体验。

**引用文件：** <arkui/native\_interface\_focus.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NdkFocus](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkFocus)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_KeyProcessingMode](capi-native-interface-focus-h.md#arkui_keyprocessingmode) | ArkUI\_KeyProcessingMode | 按键事件的处理模式。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ErrorCode OH\_ArkUI\_FocusRequest(ArkUI\_NodeHandle node)](capi-native-interface-focus-h.md#oh_arkui_focusrequest) | 为特定节点请求焦点。 |
| [void OH\_ArkUI\_FocusClear(ArkUI\_ContextHandle uiContext)](capi-native-interface-focus-h.md#oh_arkui_focusclear) | 将当前焦点清除到根容器节点。 |
| [void OH\_ArkUI\_FocusActivate(ArkUI\_ContextHandle uiContext, bool isActive, bool isAutoInactive)](capi-native-interface-focus-h.md#oh_arkui_focusactivate) | 设置当前界面的焦点激活态，获焦节点显示焦点框。 |
| [void OH\_ArkUI\_FocusSetAutoTransfer(ArkUI\_ContextHandle uiContext, bool autoTransfer)](capi-native-interface-focus-h.md#oh_arkui_focussetautotransfer) | 设置页面切换时焦点是否自动转移。 |
| [void OH\_ArkUI\_FocusSetKeyProcessingMode(ArkUI\_ContextHandle uiContext, ArkUI\_KeyProcessingMode mode)](capi-native-interface-focus-h.md#oh_arkui_focussetkeyprocessingmode) | 设置按键事件处理的优先级。 |

## 枚举类型说明

### ArkUI\_KeyProcessingMode

```c
enum ArkUI_KeyProcessingMode
```

**描述：**

按键事件的处理模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEY\_PROCESSING\_MODE\_FOCUS\_NAVIGATION = 0 | 按键事件用于移动焦点。 |
| ARKUI\_KEY\_PROCESSING\_MODE\_FOCUS\_ANCESTOR\_EVENT = 1 | 按键事件向上传递给祖先组件。 |

## 函数说明

### OH\_ArkUI\_FocusRequest()

```c
ArkUI_ErrorCode OH_ArkUI_FocusRequest(ArkUI_NodeHandle node)
```

**描述：**

为特定节点请求焦点，适用于需要主动将焦点移动到指定组件的场景，例如页面初始化后设置默认焦点或通过键盘、遥控器进行焦点导航。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要请求焦点的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 请求成功。  [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 节点无法获得焦点。  [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE\_ANCESTOR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 祖先节点无法获得焦点。  [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_EXISTENT](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 节点不存在。 |

### OH\_ArkUI\_FocusClear()

```c
void OH_ArkUI_FocusClear(ArkUI_ContextHandle uiContext)
```

**描述：**

将当前焦点清除到根容器节点，适用于退出当前焦点交互或需要重置页面焦点状态的场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | 需要清除焦点的UI实例对象的指针。 |

### OH\_ArkUI\_FocusActivate()

```c
void OH_ArkUI_FocusActivate(ArkUI_ContextHandle uiContext, bool isActive, bool isAutoInactive)
```

**描述：**

设置当前界面的焦点激活态，获焦节点显示焦点框，适用于需要在键盘、遥控器等非触摸交互中显示焦点位置的场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| bool isActive | 设置是否进入/退出焦点激活态。true表示进入焦点激活态，false表示退出焦点激活态。 |
| bool isAutoInactive | 当触摸事件或鼠标按下事件触发时，true表示将状态设置为退出焦点激活态，false表示在再次调用OH\_ArkUI\_FocusActivate设置焦点激活态前，保持当前状态。 |

### OH\_ArkUI\_FocusSetAutoTransfer()

```c
void OH_ArkUI_FocusSetAutoTransfer(ArkUI_ContextHandle uiContext, bool autoTransfer)
```

**描述：**

设置页面切换时焦点是否自动转移。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| bool autoTransfer | 页面切换时，是否转移焦点。true表示页面切换时自动转移焦点到新页面；false表示页面切换时焦点不转移。 |

### OH\_ArkUI\_FocusSetKeyProcessingMode()

```c
void OH_ArkUI_FocusSetKeyProcessingMode(ArkUI_ContextHandle uiContext, ArkUI_KeyProcessingMode mode)
```

**描述：**

设置按键事件处理的优先级，适用于需要在焦点导航和祖先组件按键事件处理之间选择优先策略的场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| [ArkUI\_KeyProcessingMode](capi-native-interface-focus-h.md#arkui_keyprocessingmode) mode | 按键事件处理的优先级。 |
