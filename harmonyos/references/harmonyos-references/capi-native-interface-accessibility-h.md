---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h
title: native_interface_accessibility.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_interface_accessibility.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e1aaacd800b66f772f28524adaeee3eaf7198ab6d9e15a73eb92e385e5802cc
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于访问Native Accessibility的API，提供无障碍相关能力。

**引用文件：** <arkui/native\_interface\_accessibility.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**相关示例：** [AccessibilityCapi](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/AccessibilityCapi)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_AccessibleAction](capi-arkui-accessibility-arkui-accessibleaction.md) | ArkUI\_AccessibleAction | 无障碍操作内容结构。 |
| [ArkUI\_AccessibleRect](capi-arkui-accessibility-arkui-accessiblerect.md) | ArkUI\_AccessibleRect | 节点所在坐标位置。 |
| [ArkUI\_AccessibleRangeInfo](capi-arkui-accessibility-arkui-accessiblerangeinfo.md) | ArkUI\_AccessibleRangeInfo | 用于特定组件设置组件的当前值、最大值、最小值，如Slider、Rating、Progress组件。 |
| [ArkUI\_AccessibleGridInfo](capi-arkui-accessibility-arkui-accessiblegridinfo.md) | ArkUI\_AccessibleGridInfo | 用于特定组件设置组件的行数、列数以及选择模式，如List、Flex、Select、Swiper组件。 |
| [ArkUI\_AccessibleGridItemInfo](i-arkui-accessibility-arkui-accessiblegriditeminfo.md) | ArkUI\_AccessibleGridItemInfo | 用于特定组件设置组件的属性值，如List、Flex、Select、Swiper组件。 |
| [ArkUI\_AccessibilityProviderCallbacks](accessibility-arkui-accessibilityprovidercallbacks.md) | ArkUI\_AccessibilityProviderCallbacks | 第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH\_ArkUI\_AccessibilityProviderRegisterCallback注册到系统侧。 |
| [ArkUI\_AccessibilityProviderCallbacksWithInstance](y-arkui-accessibilityprovidercallbackswithinstance.md) | ArkUI\_AccessibilityProviderCallbacksWithInstance | 适配多实例场景第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance注册到系统侧。 |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md) | ArkUI\_AccessibilityElementInfo | 无障碍节点信息，用于向无障碍服务、辅助应用（屏幕朗读）传递节点信息。 |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md) | ArkUI\_AccessibilityEventInfo | 无障碍事件信息。当无障碍服务或辅助应用要求控件执行操作后，需要发送执行成功事件。 |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md) | ArkUI\_AccessibilityProvider | 该结构体为第三方操作提供者，用于承载回调函数的实现。 |
| [ArkUI\_AccessibilityActionArguments](i-accessibility-arkui-accessibilityactionarguments.md) | ArkUI\_AccessibilityActionArguments | 用于设置无障碍操作的具体参数。 |
| [ArkUI\_AccessibilityElementInfoList](i-accessibility-arkui-accessibilityelementinfolist.md) | ArkUI\_AccessibilityElementInfoList | 提供封装的ArkUI\_AccessibilityElementInfo的List实例。 |
| [ArkUI\_Node\*](capi-arkui-nativemodule-arkui-node8h.md) | ArkUI\_NodeHandle | 定义ArkUI native组件实例对象指针。  **起始版本：** 23 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_Accessibility\_ActionType](capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype) | ArkUI\_Accessibility\_ActionType | Accessibility操作类型的枚举。 |
| [ArkUI\_AccessibilityEventType](capi-native-interface-accessibility-h.md#arkui_accessibilityeventtype) | ArkUI\_AccessibilityEventType | Accessibility事件类型的枚举。 |
| [ArkUI\_AcessbilityErrorCode](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode) | ArkUI\_AcessbilityErrorCode | Accessibility错误代码状态的枚举。 |
| [ArkUI\_AccessibilitySearchMode](capi-native-interface-accessibility-h.md#arkui_accessibilitysearchmode) | ArkUI\_AccessibilitySearchMode | Accessibility搜索类型的枚举。 |
| [ArkUI\_AccessibilityFocusType](capi-native-interface-accessibility-h.md#arkui_accessibilityfocustype) | ArkUI\_AccessibilityFocusType | Accessibility焦点类型的枚举。 |
| [ArkUI\_AccessibilityFocusMoveDirection](capi-native-interface-accessibility-h.md#arkui_accessibilityfocusmovedirection) | ArkUI\_AccessibilityFocusMoveDirection | Accessibility焦点移动方向的枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_ArkUI\_AccessibilityProviderRegisterCallback(ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityProviderCallbacks\* callbacks)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback) | 第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH\_ArkUI\_AccessibilityProviderRegisterCallback注册到系统侧。 |
| [int32\_t OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance(const char\* instanceId,ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityProviderCallbacksWithInstance\* callbacks)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallbackwithinstance) | 无障碍多实例场景第三方平台注册回调函数。 |
| [void OH\_ArkUI\_SendAccessibilityAsyncEvent(ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityEventInfo\* eventInfo,void (\*callback)(int32\_t errorCode))](capi-native-interface-accessibility-h.md#oh_arkui_sendaccessibilityasyncevent) | 主动上报事件接口，通知无障碍服务。 |
| [ArkUI\_AccessibilityElementInfo\* OH\_ArkUI\_AddAndGetAccessibilityElementInfo(ArkUI\_AccessibilityElementInfoList\* list)](capi-native-interface-accessibility-h.md#oh_arkui_addandgetaccessibilityelementinfo) | 在指定的list中增加element成员，并返回element结构。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetElementId(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t elementId)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetelementid) | 为ArkUI\_AccessibilityElementInfo设置componentId。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetParentId(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t parentId)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetparentid) | 为ArkUI\_AccessibilityElementInfo设置parentId。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetComponentType(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* componentType)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetcomponenttype) | 为ArkUI\_AccessibilityElementInfo设置组件类型。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetContents(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* contents)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetcontents) | 为ArkUI\_AccessibilityElementInfo设置组件文本内容。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetHintText(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* hintText)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosethinttext) | 为ArkUI\_AccessibilityElementInfo设置提示文本。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityText(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityText)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilitytext) | 为ArkUI\_AccessibilityElementInfo设置Accessibility文本。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityDescription(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityDescription)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilitydescription) | 为ArkUI\_AccessibilityElementInfo设置Accessibility描述信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t childCount, int64\_t\* childNodeIds)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetchildnodeids) | 为ArkUI\_AccessibilityElementInfo设置childCount和childNodeIds。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetOperationActions(ArkUI\_AccessibilityElementInfo\* elementInfo,int32\_t operationCount, ArkUI\_AccessibleAction\* operationActions)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetoperationactions) | 为ArkUI\_AccessibilityElementInfo设置operationActions。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleRect\* screenRect)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetscreenrect) | 为ArkUI\_AccessibilityElementInfo设置屏幕区域。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetCheckable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool checkable)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetcheckable) | 为ArkUI\_AccessibilityElementInfo设置是否可查。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetChecked(ArkUI\_AccessibilityElementInfo\* elementInfo, bool checked)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetchecked) | 为ArkUI\_AccessibilityElementInfo设置是否被检查。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetFocusable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool focusable)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetfocusable) | 为ArkUI\_AccessibilityElementInfo设置是否可聚焦。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetFocused(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isFocused)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetfocused) | 为ArkUI\_AccessibilityElementInfo设置是否聚焦。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetVisible(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isVisible)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetvisible) | 为ArkUI\_AccessibilityElementInfo设置是否可见。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityFocused(ArkUI\_AccessibilityElementInfo\* elementInfo, bool accessibilityFocused)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilityfocused) | 为ArkUI\_AccessibilityElementInfo设置元素是否处于无障碍焦点状态。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelected(ArkUI\_AccessibilityElementInfo\* elementInfo, bool selected)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetselected) | 为ArkUI\_AccessibilityElementInfo设置是否被选中。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetClickable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool clickable)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetclickable) | 为ArkUI\_AccessibilityElementInfo设置是否支持点击。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetLongClickable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool longClickable)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetlongclickable) | 为ArkUI\_AccessibilityElementInfo设置是否支持长按。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEnabled(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isEnabled)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetenabled) | 为ArkUI\_AccessibilityElementInfo设置是否启用。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetIsPassword(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isPassword)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetispassword) | 为ArkUI\_AccessibilityElementInfo设置是否为密码。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetScrollable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool scrollable)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetscrollable) | 为ArkUI\_AccessibilityElementInfo设置是否支持滚动。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEditable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool editable)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfoseteditable) | 为ArkUI\_AccessibilityElementInfo设置是否支持编辑。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetIsHint(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isHint)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetishint) | 为ArkUI\_AccessibilityElementInfo设置提示状态。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetRangeInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleRangeInfo\* rangeInfo)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetrangeinfo) | 为ArkUI\_AccessibilityElementInfo设置rangeInfo。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetGridInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleGridInfo\* gridInfo)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetgridinfo) | 为ArkUI\_AccessibilityElementInfo设置网格信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetGridItemInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleGridItemInfo\* gridItem)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetgriditeminfo) | 为ArkUI\_AccessibilityElementInfo设置网格容器中单项内容容器。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextStart(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t selectedTextStart)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetselectedtextstart) | 为ArkUI\_AccessibilityElementInfo设置选中文本的起始位置。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextEnd(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t selectedTextEnd)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetselectedtextend) | 为ArkUI\_AccessibilityElementInfo设置选中文本的结束位置。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetCurrentItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t currentItemIndex)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetcurrentitemindex) | 为ArkUI\_AccessibilityElementInfo设置当前获焦控件的位置信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetStartItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t startItemIndex)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetstartitemindex) | 为ArkUI\_AccessibilityElementInfo设置当前屏幕中显示的第一个元素的位置信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEndItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t endItemIndex)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetenditemindex) | 为ArkUI\_AccessibilityElementInfo设置当前屏幕中显示的最后一个元素的位置信息。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetItemCount(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t itemCount)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetitemcount) | 为ArkUI\_AccessibilityElementInfo设置特定组件的元素总数。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOffset(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t offset)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilityoffset) | 为ArkUI\_AccessibilityElementInfo设置内容区相对于元素顶部坐标的滚动像素偏移量。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityGroup(ArkUI\_AccessibilityElementInfo\* elementInfo, bool accessibilityGroup)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilitygroup) | 为ArkUI\_AccessibilityElementInfo设置无障碍分组。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityLevel)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilitylevel) | 为ArkUI\_AccessibilityElementInfo设置无障碍重要性。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetZIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t zIndex)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetzindex) | 为ArkUI\_AccessibilityElementInfo设置组件z序。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI\_AccessibilityElementInfo\* elementInfo, float opacity)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetaccessibilityopacity) | 为ArkUI\_AccessibilityElementInfo设置透明度。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBackgroundColor(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* backgroundColor)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetbackgroundcolor) | 为ArkUI\_AccessibilityElementInfo设置背景色。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBackgroundImage(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* backgroundImage)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetbackgroundimage) | 为ArkUI\_AccessibilityElementInfo设置背景图。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBlur(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* blur)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosetblur) | 为ArkUI\_AccessibilityElementInfo设置模糊度。 |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetHitTestBehavior(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* hitTestBehavior)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityelementinfosethittestbehavior) | 为ArkUI\_AccessibilityElementInfo设置触摸测试的响应逻辑及节点阻塞规则。 |
| [ArkUI\_AccessibilityElementInfo\* OH\_ArkUI\_CreateAccessibilityElementInfo(void)](capi-native-interface-accessibility-h.md#oh_arkui_createaccessibilityelementinfo) | 创建一个ArkUI\_AccessibilityElementInfo对象，创建后需要调用OH\_ArkUI\_DestoryAccessibilityElementInfo释放。 |
| [void OH\_ArkUI\_DestoryAccessibilityElementInfo(ArkUI\_AccessibilityElementInfo\* elementInfo)](capi-native-interface-accessibility-h.md#oh_arkui_destoryaccessibilityelementinfo) | 销毁一个ArkUI\_AccessibilityElementInfo对象。 |
| [ArkUI\_AccessibilityEventInfo\* OH\_ArkUI\_CreateAccessibilityEventInfo(void)](capi-native-interface-accessibility-h.md#oh_arkui_createaccessibilityeventinfo) | 创建一个ArkUI\_AccessibilityEventInfo对象，创建后需要调用OH\_ArkUI\_DestoryAccessibilityEventInfo释放。 |
| [void OH\_ArkUI\_DestoryAccessibilityEventInfo(ArkUI\_AccessibilityEventInfo\* eventInfo)](capi-native-interface-accessibility-h.md#oh_arkui_destoryaccessibilityeventinfo) | 销毁ArkUI\_AccessibilityEventInfo对象。 |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetEventType(ArkUI\_AccessibilityEventInfo\* eventInfo, ArkUI\_AccessibilityEventType eventType)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityeventseteventtype) | 为ArkUI\_AccessibilityEventInfo设置事件类型。 |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI\_AccessibilityEventInfo\* eventInfo, const char\* textAnnouncedForAccessibility)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityeventsettextannouncedforaccessibility) | 为ArkUI\_AccessibilityEventInfo设置textAnnouncedForAccessibility。 |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetRequestFocusId(ArkUI\_AccessibilityEventInfo\* eventInfo, int32\_t requestFocusId)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityeventsetrequestfocusid) | 为ArkUI\_AccessibilityEventInfo设置请求焦点id。 |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetElementInfo(ArkUI\_AccessibilityEventInfo\* eventInfo, ArkUI\_AccessibilityElementInfo\* elementInfo)](capi-native-interface-accessibility-h.md#oh_arkui_accessibilityeventsetelementinfo) | 为ArkUI\_AccessibilityEventInfo设置elementInfo。 |
| [int32\_t OH\_ArkUI\_FindAccessibilityActionArgumentByKey(ArkUI\_AccessibilityActionArguments\* arguments, const char\* key, char\*\* value)](capi-native-interface-accessibility-h.md#oh_arkui_findaccessibilityactionargumentbykey) | 获取ArkUI\_AccessibilityActionArguments中指定key的value值。 |
| [int32\_t OH\_ArkUI\_NativeModule\_GetNativeAccessibilityProvider(ArkUI\_NodeHandle\* node, ArkUI\_AccessibilityProvider\*\* provider)](capi-native-interface-accessibility-h.md#oh_arkui_nativemodule_getnativeaccessibilityprovider) | 获取指向[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)对象指针的二级指针变量。  其中[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)对象与传入的[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)的实例一一对应。  三方框架将自身UI组件映射为[ARKUI\_NODE\_CUSTOM](capi-native-node-h.md#arkui_nodetype)类型的[RenderNode](js-apis-arkui-rendernode.md)并得到[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。  再调用OH\_ArkUI\_NativeModule\_GetNativeAccessibilityProvider接口获取[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)指针并注册无障碍回调。  最终实现ArkUI无障碍服务对三方框架UI的识别与事件触发。  仅当三方框架将自身UI组件映射为[ARKUI\_NODE\_CUSTOM](capi-native-node-h.md#arkui_nodetype)的[RenderNode](js-apis-arkui-rendernode.md)，该接口才会生效，否则会报错误码。  本接口通过[RenderNode](js-apis-arkui-rendernode.md)实现三方框架的接入，仅支持[ARKUI\_NODE\_CUSTOM](capi-native-node-h.md#arkui_nodetype)接入无障碍服务，可以实现无障碍控件树获取能力。  不支持多线程并发，由三方框架保证调用时的线程安全。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_Accessibility\_ActionType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_Accessibility_ActionType
```

**描述：**

Accessibility操作类型的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_INVALID = 0 | 无效值。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CLICK = 0x00000010 | 收到事件后，组件需要对点击做出响应。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_LONG\_CLICK = 0x00000020 | 收到事件后，组件需要对长点击做出响应。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_GAIN\_ACCESSIBILITY\_FOCUS = 0x00000040 | 表示获取辅助功能焦点的操作，特定组件已聚焦。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CLEAR\_ACCESSIBILITY\_FOCUS = 0x00000080 | 表示清除辅助功能焦点的操作。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SCROLL\_FORWARD = 0x00000100 | 滚动组件响应向前滚动动作。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SCROLL\_BACKWARD = 0x00000200 | 滚动组件响应反向滚动操作。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_COPY = 0x00000400 | 复制文本组件的选定内容。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_PASTE = 0x00000800 | 粘贴文本组件的选定内容。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CUT = 0x00001000 | 剪切文本组件的选定内容。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SELECT\_TEXT = 0x00002000 | 针对文本组件进行选择操作。结合ArkUI\_AccessibilityActionArguments使用，配置selectTextBegin（表示选择起始位置），selectTextEnd（表示选择结束位置），selectTextInForWard（true表示为前光标，false表示为后光标）进入编辑区选择一段文本内容。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SET\_TEXT = 0x00004000 | 设置文本组件的文本内容。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SET\_CURSOR\_POSITION = 0x00100000 | 针对文本组件设置光标位置，结合ArkUI\_AccessibilityActionArguments使用，配置可输入文本控件的光标位置。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_NEXT\_HTML\_ITEM = 0x02000000 | 焦点移动操作中支持查找下一个焦点。此处的HTML并不代表网页元素，仅用于表示具有可自行查找下一个可见聚焦组件的能力，与Web支持的能力相似。实现[findNextFocusAccessibilityNode](accessibility-arkui-accessibilityprovidercallbacks.md#findnextfocusaccessibilitynode)的能力才可配置该属性。  **起始版本：** 15 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_PREVIOUS\_HTML\_ITEM = 0x04000000 | 焦点移动操作中支持查找上一个焦点。此处的HTML并不代表网页元素，仅用于表示具有可自行查找上一个可见聚焦组件的能力，与Web支持的能力相似。实现findNextFocusAccessibilityNode的能力才可配置该属性。  **起始版本：** 15 |

### ArkUI\_AccessibilityEventType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilityEventType
```

**描述：**

Accessibility事件类型的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_INVALID = 0 | 无效值。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_CLICKED = 0x00000001 | 点击事件，在UI组件响应后发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_LONG\_CLICKED = 0x00000002 | 长点击事件，在UI组件响应后发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_SELECTED = 0x00000004 | 被选中事件，控件响应完成后发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_TEXT\_UPDATE = 0x00000010 | 文本更新事件，需要在文本更新时发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_STATE\_UPDATE = 0x00000020 | 页面更新事件，当页面跳转、切换、大小更改或移动时发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_CONTENT\_UPDATE = 0x00000800 | 页面内容发生变化时需要发送事件。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_SCROLLED = 0x000001000 | scrolled事件，当可滚动的组件上发生滚动事件时，会发送此事件。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ACCESSIBILITY\_FOCUSED = 0x00008000 | Accessibility焦点事件，在UI组件响应后发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ACCESSIBILITY\_FOCUS\_CLEARED = 0x00010000 | Accessibility焦点清除事件，在UI组件响应后发送。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_REQUEST\_ACCESSIBILITY\_FOCUS = 0x02000000 | 主动请求指定节点聚焦。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_OPEN = 0x20000000 | UI组件上报页面打开事件。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_CLOSE = 0x08000000 | UI组件上报页面关闭事件。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ANNOUNCE\_FOR\_ACCESSIBILITY = 0x10000000 | 广播Accessibility事件，请求主动播放指定的内容事件。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_FOCUS\_NODE\_UPDATE = 0x10000001 | 焦点更新事件，用于焦点更新场景。 |

### ArkUI\_AcessbilityErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AcessbilityErrorCode
```

**描述：**

Accessibility错误代码状态的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL = 0 | 成功。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_FAILED = -1 | 失败。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER = -2 | 无效参数。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_OUT\_OF\_MEMORY = -3 | 内存不足。 |

### ArkUI\_AccessibilitySearchMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilitySearchMode
```

**描述：**

Accessibility搜索类型的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_CURRENT = 0 | 查询当前节点。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_PREDECESSORS = 1 << 0 | 查询父节点。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_SIBLINGS = 1 << 1 | 查询兄弟节点。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_CHILDREN = 1 << 2 | 查询下一层孩子节点。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_RECURSIVE\_CHILDREN = 1 << 3 | 查询所有孩子节点。 |

### ArkUI\_AccessibilityFocusType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilityFocusType
```

**描述：**

Accessibility焦点类型的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_FOCUS\_TYPE\_INVALID = -1 | 无效值。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_FOCUS\_TYPE\_INPUT = 1 << 0 | 输入焦点类型。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_FOCUS\_TYPE\_ACCESSIBILITY = 1 << 1 | Accessibility焦点类型。 |

### ArkUI\_AccessibilityFocusMoveDirection

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_AccessibilityFocusMoveDirection
```

**描述：**

Accessibility焦点移动方向的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_INVALID = 0 | 无效值。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_UP = 0x00000001 | 焦点向上移动。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_DOWN = 0x00000002 | 焦点向下移动。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_LEFT = 0x00000004 | 焦点向左移动。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_RIGHT = 0x00000008 | 焦点向右移动。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_FORWARD = 0x00000010 | 焦点向下一个可聚焦节点移动，基于查询请求中指定的基准节点。 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_BACKWARD = 0x00000020 | 焦点向上一个可聚焦节点移动，基于查询请求中指定的基准节点。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_AccessibilityProviderRegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityProviderRegisterCallback(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacks* callbacks)
```

**描述：**

第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH\_ArkUI\_AccessibilityProviderRegisterCallback注册到系统侧。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\* provider | 表示指向ArkUI\_AccessibilityProvider实例的指针。 |
| [ArkUI\_AccessibilityProviderCallbacks](accessibility-arkui-accessibilityprovidercallbacks.md)\* callbacks | 表示指向GetAccessibilityNodeCursorPosition实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功，则返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  如果参数错误，则返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(const char* instanceId, ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacksWithInstance* callbacks)
```

**描述：**

无障碍多实例场景第三方平台注册回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* instanceId | 第三方平台接入的实例ID，用于区分多实例场景中不同的第三方实例，ID由第三方平台指定与维护。 |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\* provider | 第三方平台接入provider句柄。 |
| [ArkUI\_AccessibilityProviderCallbacksWithInstance](y-arkui-accessibilityprovidercallbackswithinstance.md)\* callbacks | 表示指向ArkUI\_AccessibilityProviderCallbacksWithInstance实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_SendAccessibilityAsyncEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_SendAccessibilityAsyncEvent(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityEventInfo* eventInfo, void (*callback)(int32_t errorCode))
```

**描述：**

主动上报事件接口，通知无障碍服务。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\* provider | 第三方平台接入provider句柄。 |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* eventInfo | 表示指向Accessibility事件信息的指针。 |
| void (\*callback)(int32\_t errorCode) | 表示指向SendAccessibilityAsyncEvent的回调。 |

### OH\_ArkUI\_AddAndGetAccessibilityElementInfo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AccessibilityElementInfo* OH_ArkUI_AddAndGetAccessibilityElementInfo(ArkUI_AccessibilityElementInfoList* list)
```

**描述：**

在指定的list中增加element成员，并返回element结构。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfoList](i-accessibility-arkui-accessibilityelementinfolist.md)\* list | 指定的ArkUI\_AccessibilityElementInfoList结构，新创建的ElementInfo成员加入该list后返回给函数调用方。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* | 返回创建完成的ArkUI\_AccessibilityElementInfo结构指针；如果创建失败，则返回NULL。 |

### OH\_ArkUI\_AccessibilityElementInfoSetElementId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetElementId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t elementId)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置componentId。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | ArkUI\_AccessibilityElementInfo指针。 |
| int32\_t elementId | 无障碍元素的唯一编号。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetParentId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetParentId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t parentId)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置parentId。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t parentId | 表示元素的父组件无障碍编号。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetComponentType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetComponentType(ArkUI_AccessibilityElementInfo* elementInfo, const char* componentType)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置组件类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* componentType | 表示元素所属的组件类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetContents()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetContents(ArkUI_AccessibilityElementInfo* elementInfo, const char* contents)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置组件文本内容。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* contents | 表示元素被无障碍服务所识别的文本内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetHintText()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetHintText(ArkUI_AccessibilityElementInfo* elementInfo, const char* hintText)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置提示文本。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* hintText | 表示提示文本。 默认为""。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityText()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityText(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityText)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置Accessibility文本。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* accessibilityText | 表示Accessibility文本。默认为""。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityDescription()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityDescription)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置Accessibility描述信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* accessibilityDescription | 表示Accessibility描述信息。 默认为""。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(ArkUI_AccessibilityElementInfo* elementInfo, int32_t childCount, int64_t* childNodeIds)
```

**描述：**

设置ArkUI\_AccessibilityElementInfo的childCount和childNodeIds。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t childCount | 表示孩子节点数量。默认值为0。 |
| int64\_t\* childNodeIds | 表示孩子节点id集合。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetOperationActions()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetOperationActions(ArkUI_AccessibilityElementInfo* elementInfo,int32_t operationCount, ArkUI_AccessibleAction* operationActions)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置operationActions。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t\* operationCount | 组件支持的action数量。 |
| [ArkUI\_AccessibleAction](capi-arkui-accessibility-arkui-accessibleaction.md)\* operationActions | 组件支持的action。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetScreenRect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetScreenRect(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRect* screenRect)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置屏幕区域。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| [ArkUI\_AccessibleRect](capi-arkui-accessibility-arkui-accessiblerect.md)\* screenRect | 表示屏幕区域。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetCheckable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetCheckable(ArkUI_AccessibilityElementInfo* elementInfo, bool checkable)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否可查。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool checkable | 表示是否可查。true表示可查，false表示不可查。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetChecked()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetChecked(ArkUI_AccessibilityElementInfo* elementInfo, bool checked)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否被检查。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool checked | 表示是否被检查。true表示被检查过，false表示未被检查。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetFocusable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetFocusable(ArkUI_AccessibilityElementInfo* elementInfo, bool focusable)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否可聚焦。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool focusable | 表示是否可聚焦。true表示可聚焦，false表示不可聚焦。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetFocused()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool isFocused)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否聚焦。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool isFocused | 表示是否聚焦。true表示已聚焦，false表示未聚焦。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetVisible()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetVisible(ArkUI_AccessibilityElementInfo* elementInfo, bool isVisible)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否可见。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool isVisible | 表示是否可见。true表示可见，false表示不可见。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityFocused()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityFocused)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置元素是否处于无障碍焦点状态。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool accessibilityFocused | 表示是否被无障碍聚焦。true表示被无障碍聚焦，false表示未被无障碍聚焦。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetSelected()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetSelected(ArkUI_AccessibilityElementInfo* elementInfo, bool selected)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否被选中。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool selected | 表示是否被选中。true表示被选中，false表示未选中。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetClickable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool clickable)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否支持点击。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool clickable | 表示是否支持点击。true表示支持，false表示不支持。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetLongClickable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetLongClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool longClickable)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否支持长按。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool longClickable | 表示是否支持长按。true表示支持，false表示不支持。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetEnabled(ArkUI_AccessibilityElementInfo* elementInfo, bool isEnabled)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否启用。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool isEnabled | 表示是否启用。true表示启用，false表示未启用。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetIsPassword()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetIsPassword(ArkUI_AccessibilityElementInfo* elementInfo, bool isPassword)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否为密码。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool isPassword | 表示是否为密码。true表示是密码，false表示不是密码。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetScrollable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetScrollable(ArkUI_AccessibilityElementInfo* elementInfo, bool scrollable)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否支持滚动。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool scrollable | 表示是否支持滚动。true表示支持，false表示不支持。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetEditable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetEditable(ArkUI_AccessibilityElementInfo* elementInfo, bool editable)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置是否支持编辑。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool editable | 表示是否支持编辑。true表示支持，false表示不支持。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetIsHint()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetIsHint(ArkUI_AccessibilityElementInfo* elementInfo, bool isHint)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置提示状态。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool isHint | 表示是否为提示状态。true表示是提示状态，false表示不是提示状态。在提示状态下才会获取hintText信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetRangeInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetRangeInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRangeInfo* rangeInfo)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置rangeInfo。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| [ArkUI\_AccessibleRangeInfo](capi-arkui-accessibility-arkui-accessiblerangeinfo.md)\* rangeInfo | 表示特定组件的当前值、最大值、最小值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetGridInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetGridInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridInfo* gridInfo)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置网格信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| [ArkUI\_AccessibleGridInfo](capi-arkui-accessibility-arkui-accessiblegridinfo.md)\* gridInfo | 表示特定组件的行数、列数以及选择模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetGridItemInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetGridItemInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridItemInfo* gridItem)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置网格容器中单项内容容器。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| [ArkUI\_AccessibleGridItemInfo](i-arkui-accessibility-arkui-accessiblegriditeminfo.md)\* gridItem | 表示特定组件的属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextStart()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextStart)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置选中文本的起始位置。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t selectedTextStart | 文本类控件使用，设置选中文本的起始位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextEnd()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextEnd)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置选中文本的结束位置。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t selectedTextEnd | 文本类控件使用，设置选中文本的结束位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetCurrentItemIndex()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t currentItemIndex)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置当前获焦控件的位置信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t currentItemIndex | 当前获焦控件的位置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetStartItemIndex()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetStartItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t startItemIndex)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置当前屏幕中显示的第一个元素的位置信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t startItemIndex | 当前屏幕中显示的第一个元素的位置信息。List、Select、Swiper、Tab\_Bar等组件使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetEndItemIndex()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetEndItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t endItemIndex)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置当前屏幕中显示的最后一个元素的位置信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t endItemIndex | 当前屏幕中显示的最后一个元素的位置信息。List、Select、Swiper、Tab\_Bar等组件使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetItemCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetItemCount(ArkUI_AccessibilityElementInfo* elementInfo, int32_t itemCount)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置特定组件的元素总数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t itemCount | 表示特定组件的元素总数。如List、Select、Swiper、Tab\_Bar等组件使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOffset()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset(ArkUI_AccessibilityElementInfo* elementInfo, int32_t offset)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置内容区相对于元素顶部坐标的滚动像素偏移量。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t offset | 对于可滚动类控件，如[List](ts-container-list.md)、[Grid](ts-container-grid.md)，内容区相对于元素顶部坐标的滚动像素偏移量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityGroup()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityGroup)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置无障碍分组。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| bool accessibilityGroup | 表示是否启用无障碍分组。true表示启用，false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityLevel)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置无障碍重要性。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* accessibilityLevel | 表示组件的无障碍重要性，用于控制某个组件是否被无障碍辅助服务所识别。  - auto：由系统根据当前组件的属性自动判断该组件是否重要，决定是否让无障碍辅助服务识别该组件。  - yes：表示该组件重要，允许无障碍辅助服务识别该组件。  - no：表示该组件不重要，不允许无障碍辅助服务识别该组件。  - no-hide-descendants：表示该组件及其子孙节点都不重要，不允许无障碍辅助服务识别该组件及其子孙节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetZIndex()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetZIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t zIndex)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置组件z序。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| int32\_t zIndex | 组件z序，用于控制元素在垂直于屏幕的z轴上的位置。[UiTest](js-apis-uitest.md)需要使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOpacity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI_AccessibilityElementInfo* elementInfo, float opacity)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置透明度。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| float opacity | 表示透明度。其取值范围是0到1，其中1表示完全不透明，0表示完全透明。[UiTest](js-apis-uitest.md)需要使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetBackgroundColor()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundColor(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundColor)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置背景色。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* backgroundColor | 表示背景色。数据为"#ARGB"格式，例如非透明白色，即"#FFFFFFFF"。[UiTest](js-apis-uitest.md)需要使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetBackgroundImage()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundImage(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundImage)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置背景图片。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* backgroundImage | 表示背景图片。[UiTest](js-apis-uitest.md)需要使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetBlur()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetBlur(ArkUI_AccessibilityElementInfo* elementInfo, const char* blur)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置模糊度。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* blur | 表示模糊度。[UiTest](js-apis-uitest.md)需要使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityElementInfoSetHitTestBehavior()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior(ArkUI_AccessibilityElementInfo* elementInfo, const char* hitTestBehavior)
```

**描述：**

为ArkUI\_AccessibilityElementInfo设置触摸测试的响应逻辑及节点阻塞规则。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |
| const char\* hitTestBehavior | 表示hitTest模式，取值范围参考[HitTestMode](ts-appendix-enums.md#hittestmode9)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_CreateAccessibilityElementInfo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AccessibilityElementInfo* OH_ArkUI_CreateAccessibilityElementInfo(void)
```

**描述：**

创建一个ArkUI\_AccessibilityElementInfo对象，创建后需要调用OH\_ArkUI\_DestoryAccessibilityElementInfo释放。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* | 返回ArkUI\_AccessibilityElementInfo对象。 |

### OH\_ArkUI\_DestoryAccessibilityElementInfo()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DestoryAccessibilityElementInfo(ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

销毁一个ArkUI\_AccessibilityElementInfo对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示指向ArkUI\_AccessibilityElementInfo的指针。 |

### OH\_ArkUI\_CreateAccessibilityEventInfo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_AccessibilityEventInfo* OH_ArkUI_CreateAccessibilityEventInfo(void)
```

**描述：**

创建一个ArkUI\_AccessibilityEventInfo对象，创建后需要调用OH\_ArkUI\_DestoryAccessibilityEventInfo释放。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* | 返回ArkUI\_AccessibilityEventInfo对象。 |

### OH\_ArkUI\_DestoryAccessibilityEventInfo()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DestoryAccessibilityEventInfo(ArkUI_AccessibilityEventInfo* eventInfo)
```

**描述：**

销毁ArkUI\_AccessibilityEventInfo对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* eventInfo | 需要被销毁的ArkUI\_AccessibilityEventInfo对象。 |

### OH\_ArkUI\_AccessibilityEventSetEventType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityEventSetEventType(ArkUI_AccessibilityEventInfo* eventInfo,  ArkUI_AccessibilityEventType eventType)
```

**描述：**

为ArkUI\_AccessibilityEventInfo设置事件类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* eventInfo | 表示事件信息。 |
| [ArkUI\_AccessibilityEventType](capi-native-interface-accessibility-h.md#arkui_accessibilityeventtype) eventType | 表示事件类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityEventSetTextAnnouncedForAccessibility()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI_AccessibilityEventInfo* eventInfo,  const char* textAnnouncedForAccessibility)
```

**描述：**

为ArkUI\_AccessibilityEventInfo设置主动播报的内容。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* eventInfo | 表示事件信息。 |
| const char\* textAnnouncedForAccessibility | 表示主动播报的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityEventSetRequestFocusId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityEventSetRequestFocusId(ArkUI_AccessibilityEventInfo* eventInfo,  int32_t requestFocusId)
```

**描述：**

为ArkUI\_AccessibilityEventInfo设置请求焦点id。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* eventInfo | 表示事件信息。 |
| int32\_t requestFocusId | 表示请求焦点id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_AccessibilityEventSetElementInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AccessibilityEventSetElementInfo(ArkUI_AccessibilityEventInfo* eventInfo,  ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

为ArkUI\_AccessibilityEventInfo设置elementInfo。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityEventInfo](i-arkui-accessibility-arkui-accessibilityeventinfo.md)\* eventInfo | 表示事件信息。 |
| [ArkUI\_AccessibilityElementInfo](arkui-accessibility-arkui-accessibilityelementinfo.md)\* elementInfo | 表示ArkUI\_AccessibilityElementInfo元素信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_FindAccessibilityActionArgumentByKey()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_FindAccessibilityActionArgumentByKey(ArkUI_AccessibilityActionArguments* arguments, const char* key, char** value)
```

**描述：**

获取ArkUI\_AccessibilityActionArguments中指定key的value值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_AccessibilityActionArguments](i-accessibility-arkui-accessibilityactionarguments.md)\* arguments | 表示ArkUI\_AccessibilityActionArguments对象信息。 |
| const char\* key | 表示key。 |
| char\*\* value | 表示value。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。  参数错误返回[ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](capi-native-interface-accessibility-h.md#arkui_acessbilityerrorcode)。 |

### OH\_ArkUI\_NativeModule\_GetNativeAccessibilityProvider()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_GetNativeAccessibilityProvider(ArkUI_NodeHandle* node, ArkUI_AccessibilityProvider** provider)
```

**描述：**

获取指向[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)对象指针的二级指针变量。

其中[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)对象与传入的[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)的实例一一对应。

三方框架将自身UI组件映射为[ARKUI\_NODE\_CUSTOM](capi-native-node-h.md#arkui_nodetype)类型的[RenderNode](js-apis-arkui-rendernode.md)并得到[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。

再调用OH\_ArkUI\_NativeModule\_GetNativeAccessibilityProvider接口获取[ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)指针并注册无障碍回调。

最终实现ArkUI无障碍服务对三方框架UI的识别与事件触发。

仅当三方框架将自身UI组件映射为[ARKUI\_NODE\_CUSTOM](capi-native-node-h.md#arkui_nodetype)的[RenderNode](js-apis-arkui-rendernode.md)，该接口才会生效，否则会报错误码。

本接口通过[RenderNode](js-apis-arkui-rendernode.md)实现三方框架的接入，仅支持[ARKUI\_NODE\_CUSTOM](capi-native-node-h.md#arkui_nodetype)接入无障碍服务，可以实现无障碍控件树获取能力。

不支持多线程并发，由三方框架保证调用时的线程安全。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\* node | 指向一个ArkUI\_NodeHandle对象的指针。 |
| [ArkUI\_AccessibilityProvider](pi-arkui-accessibility-arkui-accessibilityprovider.md)\*\* provider | 指向一个ArkUI\_AccessibilityProvider类型对象的指针。provider用于注册无障碍回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回状态码。  成功返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode)。  参数错误返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode)。  参数错误：1. 传入的参数node或者provider为空指针。  2. node对应的ArkUI\_NodeHandle类型不为ARKUI\_NODE\_CUSTOM。 |
