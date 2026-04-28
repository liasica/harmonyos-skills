---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-textarea-event
title: 监听输入框事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用文本 > 监听输入框事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3050df3ec8958a3deaafa572d2065222823376cb6feb93ec93476f59a49a2c5c
---

输入框包含多种交互行为，开发者可注册事件监听并获取状态。

要实现实时搜索功能，可注册[NODE\_TEXT\_AREA\_ON\_CHANGE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件，输入框文本发生变化时会收到通知，并能获取当前文本内容。

要实现文字过滤功能，可注册[NODE\_TEXT\_AREA\_ON\_WILL\_INSERT](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件，在文字即将插入前会收到通知，通过返回值控制文字是否插入。

要实现用户编辑文字前后页面布局的不同，可注册[NODE\_TEXT\_AREA\_ON\_EDIT\_CHANGE](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件，输入框编辑状态切换时会收到通知。

以下示例基于[接入ArkTS页面章节](ndk-access-the-arkts-page.md)，说明如何监听输入框的事件及数据解析。

* 注册事件

  事件注册有统一接口，详情请参见[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)。输入框支持的事件类型，请参见[NativeNode组件支持的事件类型定义](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，搜索前缀NODE\_TEXT\_AREA\_。

  ```
  1. ArkUI_NodeHandle text = nodeApi->createNode(ARKUI_NODE_TEXT);
  2. ArkUI_NumberValue textWidth[] = {{.f32 = 300}};
  3. ArkUI_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
  4. nodeApi->setAttribute(text, NODE_WIDTH, &textWidthItem);
  5. // ···
  6. ArkUI_NodeHandle selectionText = nodeApi->createNode(ARKUI_NODE_TEXT);
  7. ArkUI_NumberValue selectionTextWidth[] = {{.f32 = 300}};
  8. ArkUI_AttributeItem selectionTextWidthItem = {.value = selectionTextWidth, .size = 1};
  9. nodeApi->setAttribute(selectionText, NODE_WIDTH, &selectionTextWidthItem);
  10. // ···
  11. const ArkUI_AttributeItem *attributeItem = nodeApi->getAttribute(textArea, NODE_UNIQUE_ID);
  12. auto id = attributeItem->value[0].i32;
  13. nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_CHANGE, id, text);
  14. nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_PASTE, id, text);
  15. nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE, id, selectionText);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextAreaEventNDK/entry/src/main/cpp/manager.cpp#L48-L82)
* 注册事件回调

  事件回调注册有统一接口，详情请参见[registerNodeEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver)。

  ```
  1. nodeApi->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
  2. ArkUI_NodeEventType eventType = OH_ArkUI_NodeEvent_GetEventType(event);
  3. ArkUI_AttributeItem content;
  4. if (eventType == NODE_TEXT_AREA_ON_CHANGE || eventType == NODE_TEXT_AREA_ON_PASTE) {
  5. ArkUI_StringAsyncEvent *stringEvent = OH_ArkUI_NodeEvent_GetStringAsyncEvent(event);
  6. content = {.string = stringEvent->pStr };
  7. } else if (eventType == NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE) {
  8. ArkUI_NodeComponentEvent *componentEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event);
  9. std::stringstream selectContent;
  10. selectContent << "start: " << componentEvent->data[0].i32 << " , end: " << componentEvent->data[1].i32;
  11. content = {.string = selectContent.str().c_str() };
  12. } else {
  13. return;
  14. }
  15. ArkUI_NodeHandle textNode = reinterpret_cast<ArkUI_NodeHandle>(OH_ArkUI_NodeEvent_GetUserData(event));
  16. if (textNode) {
  17. ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
  18. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
  19. nodeApi->setAttribute(textNode, NODE_TEXT_CONTENT, &content);
  20. }
  21. });
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextAreaEventNDK/entry/src/main/cpp/manager.cpp#L90-L112)
* 完整示例

  本篇示例仅提供核心接口的调用方法，完整的示例工程请参考[TextAreaEventNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/TextAreaEventNDK)。

  ```
  1. #include "manager.h"
  2. #include <sstream>
  3. #include <arkui/native_interface.h>
  4. #include <arkui/styled_string.h>

  6. namespace NativeNode::Manager {
  7. constexpr int32_t NUM_10 = 10;
  8. constexpr int32_t NUM_28 = 28;
  9. constexpr int32_t NUM_400 = 400;
  10. NodeManager &NodeManager::GetInstance()
  11. {
  12. static NodeManager instance;
  13. return instance;
  14. }

  16. void NodeManager::SetXComponent(OH_NativeXComponent *xComponent) { xComponent_ = xComponent; }

  18. void NodeManager::CreateTextAreaNode()
  19. {
  20. if (!xComponent_) {
  21. return;
  22. }
  23. ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
  24. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
  25. if (nodeApi == nullptr) {
  26. return;
  27. }
  28. ArkUI_NodeHandle column = nodeApi->createNode(ARKUI_NODE_COLUMN);
  29. ArkUI_NumberValue colWidth[] = {{.f32 = 300}};
  30. ArkUI_AttributeItem widthItem = {.value = colWidth, .size = 1};
  31. nodeApi->setAttribute(column, NODE_WIDTH, &widthItem);

  33. ArkUI_NodeHandle text = nodeApi->createNode(ARKUI_NODE_TEXT);
  34. ArkUI_NumberValue textWidth[] = {{.f32 = 300}};
  35. ArkUI_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
  36. nodeApi->setAttribute(text, NODE_WIDTH, &textWidthItem);
  37. ArkUI_NumberValue textHeight[] = {{.f32 = 100}};
  38. ArkUI_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
  39. nodeApi->setAttribute(text, NODE_HEIGHT, &textHeightItem);

  41. nodeApi->addChild(column, text);

  43. ArkUI_NodeHandle selectionText = nodeApi->createNode(ARKUI_NODE_TEXT);
  44. ArkUI_NumberValue selectionTextWidth[] = {{.f32 = 300}};
  45. ArkUI_AttributeItem selectionTextWidthItem = {.value = selectionTextWidth, .size = 1};
  46. nodeApi->setAttribute(selectionText, NODE_WIDTH, &selectionTextWidthItem);
  47. nodeApi->addChild(column, selectionText);
  48. ArkUI_NodeHandle textArea = nodeApi->createNode(ARKUI_NODE_TEXT_AREA);
  49. ArkUI_NumberValue textAreaWidth[] = {{.f32 = 300}};
  50. ArkUI_AttributeItem textAreaWidthItem = {.value = textAreaWidth, .size = 1};
  51. nodeApi->setAttribute(textArea, NODE_WIDTH, &textAreaWidthItem);

  53. ArkUI_NumberValue borderWidth[] = {{.f32 = 1}};
  54. ArkUI_AttributeItem borderWidthItem = {.value = borderWidth, .size = 1};
  55. nodeApi->setAttribute(textArea, NODE_BORDER_WIDTH, &borderWidthItem);

  57. const ArkUI_AttributeItem *attributeItem = nodeApi->getAttribute(textArea, NODE_UNIQUE_ID);
  58. auto id = attributeItem->value[0].i32;
  59. nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_CHANGE, id, text);
  60. nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_PASTE, id, text);
  61. nodeApi->registerNodeEvent(textArea, NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE, id, selectionText);
  62. TextAreaNodeEventReceiver(nodeApi);
  63. nodeApi->addChild(column, textArea);
  64. OH_NativeXComponent_AttachNativeRootNode(xComponent_, column);
  65. }

  67. void NodeManager::TextAreaNodeEventReceiver(ArkUI_NativeNodeAPI_1* nodeApi)
  68. {
  69. nodeApi->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
  70. ArkUI_NodeEventType eventType = OH_ArkUI_NodeEvent_GetEventType(event);
  71. ArkUI_AttributeItem content;
  72. if (eventType == NODE_TEXT_AREA_ON_CHANGE || eventType == NODE_TEXT_AREA_ON_PASTE) {
  73. ArkUI_StringAsyncEvent *stringEvent = OH_ArkUI_NodeEvent_GetStringAsyncEvent(event);
  74. content = {.string = stringEvent->pStr };
  75. } else if (eventType == NODE_TEXT_AREA_ON_TEXT_SELECTION_CHANGE) {
  76. ArkUI_NodeComponentEvent *componentEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event);
  77. std::stringstream selectContent;
  78. selectContent << "start: " << componentEvent->data[0].i32 << " , end: " << componentEvent->data[1].i32;
  79. content = {.string = selectContent.str().c_str() };
  80. } else {
  81. return;
  82. }
  83. ArkUI_NodeHandle textNode = reinterpret_cast<ArkUI_NodeHandle>(OH_ArkUI_NodeEvent_GetUserData(event));
  84. if (textNode) {
  85. ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
  86. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
  87. nodeApi->setAttribute(textNode, NODE_TEXT_CONTENT, &content);
  88. }
  89. });
  90. }
  91. } // namespace NativeNode::Manager
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextAreaEventNDK/entry/src/main/cpp/manager.cpp#L15-L115)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/WoLrj5XWScqvBYPiVnKxCQ/zh-cn_image_0000002552798418.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234015Z&HW-CC-Expire=86400&HW-CC-Sign=EE8ADFD9B76B8F789DE14A71321181144CC39364CB679AEF54DFD7069BAE5948)
