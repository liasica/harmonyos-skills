---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-scope-task
title: 在NDK中保证多实例场景功能正常
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 在NDK中保证多实例场景功能正常
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:05e160beee31de785c323dd05bec21141a8d4784b84c62f10f602a5b47cea18d
---

API version 20开始，ArkUI开发框架新增了[OH\_ArkUI\_RunTaskInScope](../harmonyos-references/capi-native-node-h.md#oh_arkui_runtaskinscope)接口，解决Native侧多实例场景下的组件操作问题。该功能通过动态切换执行上下文，确保跨实例组件属性设置的合法性，避免实例上下文不匹配导致的接口调用异常。

在NDK多窗口开发时，可能会涉及到组件的跨实例设置属性等场景，使用该能力可确保在调用跨实例组件设置属性时的上下文正确性，避免跨实例接口调用失败。

说明

* 适用于NDK多窗口开发中不同UI实例间的交互场景，例如在页面B中修改页面A创建的组件属性或未挂载到UI树的组件逻辑。
* 支持通过userData参数传递自定义数据结构（如组件指针、业务参数等），便于在回调任务中精准定位目标组件。
* 与[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid)等接口配合使用，有效规避跨实例访问导致的空指针或权限异常问题。

本示例展示OH\_ArkUI\_RunTaskInScope接口的基础使用方式，OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById用于获取前置实例页面内的组件，相关使用请参考[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid)，此处userData传入的数据类型为最终要设置的组件指针，便于设置对应组件属性。

```
1. const uint32_t VALUE_2 = 250;
2. const uint32_t VALUE_3 = 480;
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkScopeTask/entry/src/main/cpp/napi_init.cpp#L27-L30)

```
1. //page1
2. ArkUI_NodeHandle button = nodeAPI->createNode(ARKUI_NODE_BUTTON);
3. ArkUI_AttributeItem LABEL_Item = {.string = "pageOneButton"};
4. // 设置id，用于在第二个页面内通过接口查找
5. ArkUI_AttributeItem id = {.string = "pageOneButton"};
6. nodeAPI->setAttribute(button, NODE_ID, &id);
7. nodeAPI->setAttribute(button, NODE_BUTTON_LABEL, &LABEL_Item);
8. nodeAPI->addChild(textContainer, button);
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkScopeTask/entry/src/main/cpp/napi_init.cpp#L41-L50)

```
1. //page2
2. //pageOneButton由前置页面创建，通过OH_ArkUI_NodeUtils_GetAttachedNodeHandleById在第二个页面获取。
3. ArkUI_NodeHandle pageOneButton = nullptr;
4. auto errorCode = OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("pageOneButton", &pageOneButton);
5. if (errorCode != ARKUI_ERROR_CODE_NO_ERROR) {
6. OH_LOG_ERROR(LOG_APP, "test Failed to get pageOneButton handle, error code: %{public}d", errorCode);
7. return nullptr;
8. }
9. auto uiContext = OH_ArkUI_GetContextByNode(pageOneButton);
10. if (uiContext == nullptr) {
11. OH_LOG_ERROR(LOG_APP, "test Failed to get UI context for pageOneButton");
12. return nullptr;
13. }
14. OH_ArkUI_RunTaskInScope(uiContext, pageOneButton, [](void *userData) {
15. auto *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
16. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
17. auto pageOneButton = (ArkUI_NodeHandle)userData;
18. ArkUI_NumberValue value[] = {VALUE_3};
19. ArkUI_AttributeItem LABEL_Item = {.string = "success"};
20. value[0].f32 = VALUE_2;
21. ArkUI_AttributeItem button_Item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
22. nodeAPI->setAttribute(pageOneButton, NODE_BUTTON_LABEL, &LABEL_Item);
23. nodeAPI->setAttribute(pageOneButton, NODE_WIDTH, &button_Item);
24. });
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkScopeTask/entry/src/main/cpp/napi_init.cpp#L108-L133)
