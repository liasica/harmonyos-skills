---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/accessibility-arkui-accessibilityprovidercallbacks
title: ArkUI_AccessibilityProviderCallbacks
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibilityProviderCallbacks
category: harmonyos-references
scraped_at: 2026-04-28T08:04:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ca05b2ee9d6bb670778e42481072f3435e230693dd9b3c2047f2076689e943dd
---

```
1. typedef struct {...} ArkUI_AccessibilityProviderCallbacks
```

## 概述

PhonePC/2in1TabletTVWearable

第三方操作[provider](pi-arkui-accessibility-arkui-accessibilityprovider.md)回调函数结构定义，需要第三方平台实现的相关函数，通过[OH\_ArkUI\_AccessibilityProviderRegisterCallback](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback)注册到系统侧。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*findAccessibilityNodeInfosById)(int64\_t elementId, ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](accessibility-arkui-accessibilityprovidercallbacks.md#findaccessibilitynodeinfosbyid) | 查询指定节点的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findAccessibilityNodeInfosByText)(int64\_t elementId, const char\* text, int32\_t requestId,ArkUI\_AccessibilityElementInfoList\* elementList)](accessibility-arkui-accessibilityprovidercallbacks.md#findaccessibilitynodeinfosbytext) | 基于指定的节点，查询满足指定text内容的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findFocusedAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](accessibility-arkui-accessibilityprovidercallbacks.md#findfocusedaccessibilitynode) | 从指定节点出发，根据焦点类型查找当前已获得焦点的节点，并将该节点元素信息返回。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findNextFocusAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](accessibility-arkui-accessibilityprovidercallbacks.md#findnextfocusaccessibilitynode) | 根据参考节点查询可以聚焦的节点，根据模式和方向查询下一个可以聚焦的节点。 |
| [int32\_t (\*executeAccessibilityAction)(int64\_t elementId, ArkUI\_Accessibility\_ActionType action,ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)](accessibility-arkui-accessibilityprovidercallbacks.md#executeaccessibilityaction) | 在指定节点上执行Action操作。 |
| [int32\_t (\*clearFocusedFocusAccessibilityNode)()](accessibility-arkui-accessibilityprovidercallbacks.md#clearfocusedfocusaccessibilitynode) | 清除当前焦点节点的焦点状态。 |
| [int32\_t (\*getAccessibilityNodeCursorPosition)(int64\_t elementId, int32\_t requestId, int32\_t\* index)](accessibility-arkui-accessibilityprovidercallbacks.md#getaccessibilitynodecursorposition) | 查询指定节点的当前光标位置。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### findAccessibilityNodeInfosById()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findAccessibilityNodeInfosById)(int64_t elementId, ArkUI_AccessibilitySearchMode mode,int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

查询指定节点的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilitySearchMode](capi-native-interface-accessibility-h.md#arkui_accessibilitysearchmode) mode | 表示无障碍搜索模式。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfoList](i-accessibility-arkui-accessibilityelementinfolist.md)\* elementList | 表示无障碍元素信息列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### findAccessibilityNodeInfosByText()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findAccessibilityNodeInfosByText)(int64_t elementId, const char* text, int32_t requestId,ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

基于指定的节点，查询满足指定text内容的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| const char\* text | 表示无障碍文本。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfoList](i-accessibility-arkui-accessibilityelementinfolist.md)\* elementList | 表示无障碍元素信息列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### findFocusedAccessibilityNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findFocusedAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusType focusType, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

从指定节点出发，根据焦点类型查找当前已获得焦点的节点，并将该节点元素信息返回。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilityFocusType](capi-native-interface-accessibility-h.md#arkui_accessibilityfocustype) focusType | 表示焦点的类型。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示无障碍元素信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### findNextFocusAccessibilityNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findNextFocusAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

根据参考节点的模式和查找方向查询下一个可以聚焦的节点。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilityFocusMoveDirection](capi-native-interface-accessibility-h.md#arkui_accessibilityfocusmovedirection) direction | 表示查找方向。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 查询到的无障碍元素信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### executeAccessibilityAction()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*executeAccessibilityAction)(int64_t elementId, ArkUI_Accessibility_ActionType action,ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)
```

**描述：**

在指定的无障碍节点上执行无障碍Action操作。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_Accessibility\_ActionType](capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype) action | 表示要执行的动作。 |
| [ArkUI\_AccessibilityActionArguments](i-accessibility-arkui-accessibilityactionarguments.md) \*actionArguments | 表示动作的参数。 |
| int32\_t requestId | 表示请求的ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### clearFocusedFocusAccessibilityNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*clearFocusedFocusAccessibilityNode)()
```

**描述：**

清除当前焦点节点的焦点状态。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### getAccessibilityNodeCursorPosition()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*getAccessibilityNodeCursorPosition)(int64_t elementId, int32_t requestId, int32_t* index)
```

**描述：**

查询指定节点的当前光标位置。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| int32\_t requestId | 表示请求的ID。 |
| int32\_t\* index | 表示光标位置的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |
