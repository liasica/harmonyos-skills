---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityprovidercallbacks
title: ArkUI_AccessibilityProviderCallbacks
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibilityProviderCallbacks
category: harmonyos-references
scraped_at: 2026-09-05T06:17:57+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:594b20b4cd922af5692d7c65a728acf5f472a35bf1d0611a7885b6f388140788
---

```c
typedef struct ArkUI_AccessibilityProviderCallbacks {...} ArkUI_AccessibilityProviderCallbacks
```

## 概述

第三方[provider](capi-arkui-accessibility-arkui-accessibilityprovider.md)回调函数结构定义，需要第三方平台实现的相关函数，通过[OH\_ArkUI\_AccessibilityProviderRegisterCallback](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback)注册到系统侧。适用于读屏软件、语音控制、开关控制等无障碍辅助场景，第三方平台通过实现这些回调响应系统的无障碍查询和操作请求。所有的回调函数执行线程为IPC线程，非UI线程。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*findAccessibilityNodeInfosById)(int64\_t elementId, ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#findaccessibilitynodeinfosbyid) | 查询指定节点的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findAccessibilityNodeInfosByText)(int64\_t elementId, const char\* text, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#findaccessibilitynodeinfosbytext) | 基于指定的节点，查询满足指定文本内容的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findFocusedAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#findfocusedaccessibilitynode) | 从指定节点出发，根据焦点类型查找当前已获得焦点的节点，并将该节点元素信息返回。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findNextFocusAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#findnextfocusaccessibilitynode) | 根据参考节点和查找方向，查询下一个可以聚焦的节点。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*executeAccessibilityAction)(int64\_t elementId, ArkUI\_Accessibility\_ActionType action, ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#executeaccessibilityaction) | 在指定的无障碍节点上执行无障碍Action操作。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*clearFocusedFocusAccessibilityNode)()](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#clearfocusedfocusaccessibilitynode) | 清除当前焦点节点的焦点状态。例如，当无障碍服务需要重置焦点高亮或用户切换到其他交互区域时触发。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*getAccessibilityNodeCursorPosition)(int64\_t elementId, int32\_t requestId, int32\_t\* index)](capi-arkui-accessibility-arkui-accessibilityprovidercallbacks.md#getaccessibilitynodecursorposition) | 查询指定节点的当前光标位置。例如，当读屏软件需要播报光标位置或语音输入法定位文本插入点时触发。由接入方平台实现的回调函数，注册给系统侧调用。 |

## 成员函数说明

### findAccessibilityNodeInfosById()

```c
int32_t (*findAccessibilityNodeInfosById)(int64_t elementId, ArkUI_AccessibilitySearchMode mode, int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

查询指定节点的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号，取值应为系统已分配的有效元素ID。 |
| [ArkUI\_AccessibilitySearchMode](capi-native-interface-accessibility-h.md#arkui_accessibilitysearchmode) mode | 表示无障碍搜索模式。具体取值及含义参见[ArkUI\_AccessibilitySearchMode](capi-native-interface-accessibility-h.md#arkui_accessibilitysearchmode)。 |
| int32\_t requestId | 表示请求ID，由系统侧生成，用于标识一次无障碍请求。 |
| [ArkUI\_AccessibilityElementInfoList](capi-arkui-accessibility-arkui-accessibilityelementinfolist.md)\* elementList | 表示无障碍元素信息列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。可能原因：传入的elementId无效或elementList为空指针。处理步骤：请检查参数elementId、mode、elementList的有效性。 |

### findAccessibilityNodeInfosByText()

```c
int32_t (*findAccessibilityNodeInfosByText)(int64_t elementId, const char* text, int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

基于指定的节点，查询满足指定文本内容的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| const char\* text | 表示用于查找节点的文本内容。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfoList](capi-arkui-accessibility-arkui-accessibilityelementinfolist.md)\* elementList | 表示无障碍元素信息列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### findFocusedAccessibilityNode()

```c
int32_t (*findFocusedAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusType focusType, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

从指定节点出发，根据焦点类型查找当前已获得焦点的节点，并将该节点元素信息返回。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilityFocusType](capi-native-interface-accessibility-h.md#arkui_accessibilityfocustype) focusType | 表示焦点的类型。具体取值及含义参见[ArkUI\_AccessibilityFocusType](capi-native-interface-accessibility-h.md#arkui_accessibilityfocustype)。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfo](capi-arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示查询到的无障碍元素信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### findNextFocusAccessibilityNode()

```c
int32_t (*findNextFocusAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

根据参考节点和查找方向，查询下一个可以聚焦的节点。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilityFocusMoveDirection](capi-native-interface-accessibility-h.md#arkui_accessibilityfocusmovedirection) direction | 表示查找方向。具体取值及含义参见[ArkUI\_AccessibilityFocusMoveDirection](capi-native-interface-accessibility-h.md#arkui_accessibilityfocusmovedirection)。 |
| int32\_t requestId | 表示请求ID。 |
| [ArkUI\_AccessibilityElementInfo](capi-arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示无障碍元素信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### executeAccessibilityAction()

```c
int32_t (*executeAccessibilityAction)(int64_t elementId, ArkUI_Accessibility_ActionType action, ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)
```

**描述：**

在指定的无障碍节点上执行无障碍Action操作。例如，当读屏软件用户通过语音指令或开关控制触发点击、滚动、选择等操作时，系统通过此回调通知第三方平台执行相应动作。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_Accessibility\_ActionType](capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype) action | 表示要执行的动作。具体取值及含义参见[ArkUI\_Accessibility\_ActionType](capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype)。 |
| [ArkUI\_AccessibilityActionArguments](capi-arkui-accessibility-arkui-accessibilityactionarguments.md) \*actionArguments | 表示动作的参数。 |
| int32\_t requestId | 表示请求ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### clearFocusedFocusAccessibilityNode()

```c
int32_t (*clearFocusedFocusAccessibilityNode)()
```

**描述：**

清除当前焦点节点的焦点状态。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |

### getAccessibilityNodeCursorPosition()

```c
int32_t (*getAccessibilityNodeCursorPosition)(int64_t elementId, int32_t requestId, int32_t* index)
```

**描述：**

查询指定节点的当前光标位置。由接入方平台实现的回调函数，注册给系统侧调用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| int32\_t requestId | 表示请求ID。 |
| int32\_t\* index | 表示光标位置的索引，取值为非负整数，表示光标在文本中的字符位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示操作成功。  [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)，表示参数错误。 |
