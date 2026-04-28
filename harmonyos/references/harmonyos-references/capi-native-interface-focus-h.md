---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-focus-h
title: native_interface_focus.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_interface_focus.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a72b5840dd4fb8b3ab91a38e7c3837eac7184c5b6f6177c8c2b8d8dba2552dd6
---

## 概述

PhonePC/2in1TabletTVWearable

定义焦点管理的相关接口，主要用于主动转移焦点或管理控制焦点转移默认行为，控制焦点激活态。

**引用文件：** <arkui/native\_interface\_focus.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NdkFocus](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkFocus)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_KeyProcessingMode](capi-native-interface-focus-h.md#arkui_keyprocessingmode) | ArkUI\_KeyProcessingMode | 按键事件处理的优先级。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ErrorCode OH\_ArkUI\_FocusRequest(ArkUI\_NodeHandle node)](capi-native-interface-focus-h.md#oh_arkui_focusrequest) | 为特定节点请求焦点。 |
| [void OH\_ArkUI\_FocusClear(ArkUI\_ContextHandle uiContext)](capi-native-interface-focus-h.md#oh_arkui_focusclear) | 将当前焦点清除到根容器节点。 |
| [void OH\_ArkUI\_FocusActivate(ArkUI\_ContextHandle uiContext, bool isActive, bool isAutoInactive)](capi-native-interface-focus-h.md#oh_arkui_focusactivate) | 设置当前界面的焦点激活态，获焦节点显示焦点框。 |
| [void OH\_ArkUI\_FocusSetAutoTransfer(ArkUI\_ContextHandle uiContext, bool autoTransfer)](capi-native-interface-focus-h.md#oh_arkui_focussetautotransfer) | 设置页面切换时，焦点转移行为。 |
| [void OH\_ArkUI\_FocusSetKeyProcessingMode(ArkUI\_ContextHandle uiContext, ArkUI\_KeyProcessingMode mode)](capi-native-interface-focus-h.md#oh_arkui_focussetkeyprocessingmode) | 设置按键事件处理的优先级。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_KeyProcessingMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeyProcessingMode
```

**描述：**

按键事件处理的优先级。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEY\_PROCESSING\_MODE\_FOCUS\_NAVIGATION = 0 | 按键事件用于移动焦点。 |
| ARKUI\_KEY\_PROCESSING\_MODE\_FOCUS\_ANCESTOR\_EVENT = 1 | 按键事件向上传递给祖先组件。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_FocusRequest()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_FocusRequest(ArkUI_NodeHandle node)
```

**描述：**

为特定节点请求焦点。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 请求成功。  [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE](capi-native-type-h.md#arkui_errorcode) 节点无法获得焦点。  [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE\_ANCESTOR](capi-native-type-h.md#arkui_errorcode) 祖先节点无法获得焦点。  [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_EXISTENT](capi-native-type-h.md#arkui_errorcode) 节点不存在。 |

### OH\_ArkUI\_FocusClear()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_FocusClear(ArkUI_ContextHandle uiContext)
```

**描述：**

将当前焦点清除到根容器节点。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |

### OH\_ArkUI\_FocusActivate()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_FocusActivate(ArkUI_ContextHandle uiContext, bool isActive, bool isAutoInactive)
```

**描述：**

设置当前界面的焦点激活态，获焦节点显示焦点框。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| bool isActive | 设置是否进入/退出焦点激活态。true表示进入焦点激活态，false表示退出焦点激活态。 |
| bool isAutoInactive | 当触摸事件或鼠标按下事件触发时，"true" 表示将状态设置为退出焦点激活态,"false" 表示在调用对应设置API前，保持当前状态。 |

### OH\_ArkUI\_FocusSetAutoTransfer()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_FocusSetAutoTransfer(ArkUI_ContextHandle uiContext, bool autoTransfer)
```

**描述：**

设置页面切换时，焦点转移行为。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| bool autoTransfer | 页面切换时，是否转移焦点。true表示页面切换时转移焦点，false表示页面切换时焦点不转移。 |

### OH\_ArkUI\_FocusSetKeyProcessingMode()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_FocusSetKeyProcessingMode(ArkUI_ContextHandle uiContext, ArkUI_KeyProcessingMode mode)
```

**描述：**

设置按键事件处理的优先级。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| [ArkUI\_KeyProcessingMode](capi-native-interface-focus-h.md#arkui_keyprocessingmode) mode | 按键事件处理的优先级。 |
