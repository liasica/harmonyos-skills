---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/y-arkui-accessibilityprovidercallbackswithinstance
title: ArkUI_AccessibilityProviderCallbacksWithInstance
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibilityProviderCallbacksWithInstance
category: harmonyos-references
scraped_at: 2026-04-28T08:04:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e7180e78335b0d673b088b288c2c57f6e174ae38be74a174266c8fd5f3a261a1
---

```
1. typedef struct {...} ArkUI_AccessibilityProviderCallbacksWithInstance
```

## 概述

PhonePC/2in1TabletTVWearable

适配多实例场景第三方操作[provider](pi-arkui-accessibility-arkui-accessibilityprovider.md)回调函数结构定义，需要第三方平台实现的相关函数，通过[OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallbackwithinstance)注册到系统侧。

**起始版本：** 15

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*findAccessibilityNodeInfosById)(const char\* instanceId, int64\_t elementId,ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](y-arkui-accessibilityprovidercallbackswithinstance.md#findaccessibilitynodeinfosbyid) | 基于指定的节点，查询所需的节点信息。支持多实例场景。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findAccessibilityNodeInfosByText)(const char\* instanceId, int64\_t elementId, const char\* text,int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](y-arkui-accessibilityprovidercallbackswithinstance.md#findaccessibilitynodeinfosbytext) | 基于指定的节点，查询满足指定组件文本内容的节点信息。支持多实例场景。由接入方平台实现的回调函数，注册给系统侧调用。 |
| [int32\_t (\*findFocusedAccessibilityNode)(const char\* instanceId, int64\_t elementId,ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](y-arkui-accessibilityprovidercallbackswithinstance.md#findfocusedaccessibilitynode) | 从指定节点查找已经聚焦的节点。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。 |
| [int32\_t (\*findNextFocusAccessibilityNode)(const char\* instanceId, int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction,int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](y-arkui-accessibilityprovidercallbackswithinstance.md#findnextfocusaccessibilitynode) | 从指定节点查询指定方向的节点。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。 |
| [int32\_t (\*executeAccessibilityAction)(const char\* instanceId, int64\_t elementId,ArkUI\_Accessibility\_ActionType action, ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)](y-arkui-accessibilityprovidercallbackswithinstance.md#executeaccessibilityaction) | 对指定节点执行指定的操作。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。 |
| [int32\_t (\*clearFocusedFocusAccessibilityNode)(const char\* instanceId)](y-arkui-accessibilityprovidercallbackswithinstance.md#clearfocusedfocusaccessibilitynode) | 清除当前获焦的节点。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。 |
| [int32\_t (\*getAccessibilityNodeCursorPosition)(const char\* instanceId, int64\_t elementId,int32\_t requestId, int32\_t\* index)](y-arkui-accessibilityprovidercallbackswithinstance.md#getaccessibilitynodecursorposition) | 获取当前组件中（文本组件）光标位置。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### findAccessibilityNodeInfosById()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findAccessibilityNodeInfosById)(const char* instanceId, int64_t elementId,ArkUI_AccessibilitySearchMode mode, int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

基于指定的节点，查询所需的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilitySearchMode](capi-native-interface-accessibility-h.md#arkui_accessibilitysearchmode) mode | 无障碍服务的搜索模式。 |
| int32\_t requestId | 请求id，用于关联请求过程，建议日志打印时附带输出该信息，方便问题定位。 |
| [ArkUI\_AccessibilityElementInfoList](i-accessibility-arkui-accessibilityelementinfolist.md)\* elementList | 本次查询到的所有无障碍元素列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### findAccessibilityNodeInfosByText()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findAccessibilityNodeInfosByText)(const char* instanceId, int64_t elementId, const char* text,int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

基于指定的节点，查询满足指定组件文本内容的节点信息。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| const char\* text | 组件需要匹配的文本内容。 |
| int32\_t requestId | 请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。 |
| [ArkUI\_AccessibilityElementInfoList](i-accessibility-arkui-accessibilityelementinfolist.md)\* elementList | 本次查询到的所有无障碍元素列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### findFocusedAccessibilityNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findFocusedAccessibilityNode)(const char* instanceId, int64_t elementId,ArkUI_AccessibilityFocusType focusType, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

从指定节点查找已经聚焦的节点。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilityFocusType](capi-native-interface-accessibility-h.md#arkui_accessibilityfocustype) focusType | 焦点类型。 |
| int32\_t requestId | 请求id，用于关联请求过程，建议日志打印时附带输出该信息，方便问题定位。 |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 本次查询到的无障碍元素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### findNextFocusAccessibilityNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*findNextFocusAccessibilityNode)(const char* instanceId, int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

从指定节点查询指定方向的节点。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_AccessibilityFocusMoveDirection](capi-native-interface-accessibility-h.md#arkui_accessibilityfocusmovedirection) direction | 搜索方向。 |
| int32\_t requestId | 请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。 |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 本次查询到的无障碍元素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### executeAccessibilityAction()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*executeAccessibilityAction)(const char* instanceId, int64_t elementId,ArkUI_Accessibility_ActionType action, ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)
```

**描述：**

对指定节点执行指定的操作。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| [ArkUI\_Accessibility\_ActionType](capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype) action | 需要执行的操作，比如聚焦、点击和长按等。 |
| [ArkUI\_AccessibilityActionArguments](i-accessibility-arkui-accessibilityactionarguments.md) \*actionArguments | 控制操作的参数。 |
| int32\_t requestId | 请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### clearFocusedFocusAccessibilityNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*clearFocusedFocusAccessibilityNode)(const char* instanceId)
```

**描述：**

清除当前获焦的节点。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### getAccessibilityNodeCursorPosition()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*getAccessibilityNodeCursorPosition)(const char* instanceId, int64_t elementId,int32_t requestId, int32_t* index)
```

**描述：**

获取当前组件中（文本组件）光标位置。由接入方平台实现的回调函数，注册给系统侧调用。支持多实例场景。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方框架的实例编码。 |
| int64\_t elementId | 无障碍元素的唯一编号。 |
| int32\_t requestId | 请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。 |
| int32\_t\* index | 光标的位置结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |
