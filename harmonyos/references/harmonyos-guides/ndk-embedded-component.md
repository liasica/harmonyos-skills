---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embedded-component
title: 通过EmbeddedComponent拉起EmbeddedUIExtensionAbility
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 通过EmbeddedComponent拉起EmbeddedUIExtensionAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3095db1bae0b28e66370b46c139b53bd566a63df302fa36c8ead0ad90efc3271
---

ArkUI在Native侧提供的能力是ArkTS的子集，某些能力不会在Native侧提供，例如声明式UI语法、自定义struct组件及UI系统预置UI组件库。

从API version 20开始，ArkUI开发框架提供了Native侧嵌入EmbeddedComponent组件的能力，此能力依赖于[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)机制。EmbeddedComponent用于支持在当前页面嵌入同一应用内其他[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，负责页面布局和渲染。此功能主要用于有进程隔离需求的模块化开发场景。

说明

* 使用[OH\_ArkUI\_EmbeddedComponentOption\_Create](../harmonyos-references/capi-native-type-h.md#oh_arkui_embeddedcomponentoption_create)获取[ArkUI\_EmbeddedComponentOption](../harmonyos-references/i-arkui-nativemodule-arkui-embeddedcomponentoption.md)后，可以使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnError](../harmonyos-references/capi-native-type-h.md#oh_arkui_embeddedcomponentoption_setonerror)设置onError回调，使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](../harmonyos-references/capi-native-type-h.md#oh_arkui_embeddedcomponentoption_setonterminated)设置onTerminated回调。可以使用[OH\_ArkUI\_NodeUtils\_MoveTo](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_moveto)迁移节点。
* 使用[OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated](../harmonyos-references/capi-native-type-h.md#oh_arkui_embeddedcomponentoption_setonterminated)设置onTerminated回调时，返回的want参数，只支持提供方返回的want参数的key，value解析，不支持嵌套解析。
* 在EmbeddedComponent销毁时，调用[OH\_ArkUI\_EmbeddedComponentOption\_Dispose](../harmonyos-references/capi-native-type-h.md#oh_arkui_embeddedcomponentoption_dispose)释放内存。
* EmbeddedComponent组件需要使用[setAttribute](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)设置宽高才能显示。

本示例展示EmbeddedComponent组件NDK的基础使用方式，ability相关使用请参考[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)。示例应用的bundleName为"com.example.embeddeddemo"，同一应用下被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。本示例仅支持在具有多进程权限的设备上运行，例如PC/2in1。

```
1. #include <arkui/native_node.h>
2. #include <arkui/native_type.h>
3. #include <AbilityKit/ability_base/want.h> //引用元能力want头文件

5. // 注册事件
6. void onError(int32_t code, const char *name, const char *message) {}
7. void onTerminated(int32_t code, AbilityBase_Want *want) {}
8. const unsigned int LOG_PRINT_DOMAIN = 0xFF00;
9. #define SIZE_300 300
10. #define SIZE_401 401
11. #define SIZE_480 480
12. // ···
13. // 创建节点
14. ArkUI_NodeHandle embeddedNode = nodeAPI->createNode(ARKUI_NODE_EMBEDDED_COMPONENT);
15. // 设置属性
16. AbilityBase_Element Element = {.bundleName = "com.example.uiextensionandaccessibility",
17. .abilityName = "ExampleEmbeddedAbility",
18. .moduleName = "entry"};       // 由元能力提供接口
19. AbilityBase_Want *want = OH_AbilityBase_CreateWant(Element); // 由元能力提供接口
20. if (want == nullptr) {
21. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "AbilityBase_Want", "~PluginManager");
22. }
23. ArkUI_AttributeItem itemobjwant = {.object = want};
24. nodeAPI->setAttribute(embeddedNode, NODE_EMBEDDED_COMPONENT_WANT, &itemobjwant);

26. auto embeddedNode_option = OH_ArkUI_EmbeddedComponentOption_Create();
27. auto onErrorCallback = onError;
28. auto onTerminatedCallback = onTerminated;
29. OH_ArkUI_EmbeddedComponentOption_SetOnError(embeddedNode_option, onErrorCallback);
30. OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(embeddedNode_option, onTerminatedCallback);

32. ArkUI_AttributeItem itemobjembeddedNode = {.object = embeddedNode_option};
33. nodeAPI->setAttribute(embeddedNode, NODE_EMBEDDED_COMPONENT_OPTION, &itemobjembeddedNode);

35. // 设置基本属性，如宽高
36. ArkUI_NumberValue value[] = {SIZE_480};
37. ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
38. value[0].f32 = SIZE_300;
39. nodeAPI->setAttribute(embeddedNode, NODE_WIDTH, &item);
40. nodeAPI->setAttribute(embeddedNode, NODE_HEIGHT, &item);

42. // 创建Column
43. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
44. nodeAPI->setAttribute(column, NODE_WIDTH, &item);
45. ArkUI_NumberValue column_bc[] = {{.u32 = 0xFFF00BB}};
46. ArkUI_AttributeItem column_item = {column_bc, 1};
47. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &column_item);
48. ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
49. nodeAPI->setAttribute(column, NODE_ID, &column_id);

51. // 上树
52. nodeAPI->addChild(column, embeddedNode);
```

[embedded.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/UIExtensionAndAccessibility/entry/src/main/cpp/embedded/embedded.cpp#L21-L87)
