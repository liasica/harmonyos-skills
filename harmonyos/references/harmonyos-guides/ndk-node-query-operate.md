---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-node-query-operate
title: 查询和操作自定义节点
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 查询和操作自定义节点
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:36+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:36d2809402181f2a2c86ef429cd6b36de09d8094510ceedc9835d17153f17eef
---

NDK提供一系列节点查询、遍历、操作能力，通过使用以下接口，开发者可以高效地访问和操控节点。

以下场景基于[接入ArkTS页面](ndk-access-the-arkts-page.md)章节，创建前置工程。

## 查询节点uniqueId及通过uniqueId获取节点信息

uniqueId是系统分配的唯一标识的节点Id。

从API version 20开始，使用[OH\_ArkUI\_NodeUtils\_GetNodeUniqueId](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getnodeuniqueid)接口，可以获取目标节点的uniqueId。使用[OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getnodehandlebyuniqueid)接口，可以通过uniqueId获取目标节点的指针。

```
1. ArkUI_NativeNodeAPI_1* nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
2. ArkUI_NodeHandle testNode = nodeAPI->createNode(ARKUI_NODE_COLUMN);
3. ArkUI_NumberValue value[] = {VALUE_1};
4. ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
5. value[0].f32 = VALUE_2;
6. nodeAPI->setAttribute(testNode, NODE_WIDTH, &item);
7. nodeAPI->setAttribute(testNode, NODE_HEIGHT, &item);
8. struct IdList {
9. int32_t id = -1;
10. };
11. IdList *idl = new IdList;
12. int32_t uid = -1;
13. OH_ArkUI_NodeUtils_GetNodeUniqueId(testNode, &uid);
14. idl->id = uid;
15. auto button = nodeAPI->createNode(ARKUI_NODE_BUTTON);
16. value[0].f32 = VALUE_3;
17. nodeAPI->setAttribute(button, NODE_WIDTH, &item);
18. nodeAPI->setAttribute(button, NODE_HEIGHT, &item);
19. nodeAPI->addChild(testNode, button);
20. nodeAPI->registerNodeEvent(button, NODE_ON_CLICK, 1, idl);
21. OH_LOG_Print(LOG_APP, LOG_WARN, LOG_PRINT, "GetNodeUniqueId", "GetNodeHandleByUniqueId success1");
22. nodeAPI->registerNodeEventReceiver([](ArkUI_NodeEvent *event) {
23. auto targetId = OH_ArkUI_NodeEvent_GetTargetId(event);
24. if (targetId == 1) {
25. auto idl = (IdList *)OH_ArkUI_NodeEvent_GetUserData(event);
26. ArkUI_NodeHandle Test_Column;
27. auto ec = OH_ArkUI_NodeUtils_GetNodeHandleByUniqueId(idl->id, &Test_Column);
28. if (ec == 0) {
29. OH_LOG_Print(LOG_APP, LOG_WARN, LOG_PRINT, "GetNodeUniqueId", "GetNodeHandleByUniqueId success");
30. }
31. }
32. });
```

[InquireUniqueId.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/InquireUniqueId.cpp#L24-L62)

## 通过用户id获取节点信息

使用[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid)接口，可以通过用户设置的id获取目标节点的指针。

1. ArkTS侧接入Native组件。

   ```
   1. import nativeNode from 'libentry.so';
   2. import { NodeContent } from '@kit.ArkUI';

   4. @Entry
   5. @Component
   6. struct GetNodeById {
   7. private rootSlot = new NodeContent();

   9. aboutToAppear(): void {
   10. nativeNode.createUserIdNode(this.rootSlot);
   11. }

   13. build() {
   14. Scroll() {
   15. Column({ space: 15 }) {
   16. Column() {
   17. ContentSlot(this.rootSlot)
   18. }
   19. }
   20. .width('100%')
   21. }.scrollBarColor(Color.Transparent)
   22. }
   23. }
   ```

   [GetNodeById.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/ets/pages/GetNodeById.ets#L16-L40)
2. 新建GetNodeByIdExample.h文件，在其中创建Text节点并设置id属性，通过OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById接口拿到节点。

   ```
   1. // GetNodeByIdExample.h
   2. #ifndef MYAPPLICATION_GETNODEBYID_H
   3. #define MYAPPLICATION_GETNODEBYID_H

   5. #include "ArkUINode.h"
   6. #include <hilog/log.h>

   8. namespace NativeModule {

   10. std::shared_ptr<ArkUIBaseNode> CreateGetNodeByIdExample()
   11. {
   12. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

   14. // 创建传入事件节点结构体
   15. struct A {
   16. ArkUI_NodeHandle node;
   17. };
   18. A* a = new A;

   20. // 创建根节点Scroll
   21. ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_SCROLL);
   22. ArkUI_NumberValue length_value[] = {{.f32 = 480}};
   23. ArkUI_AttributeItem length_item = {length_value, sizeof(length_value) / sizeof(ArkUI_NumberValue)};
   24. nodeAPI->setAttribute(scroll, NODE_WIDTH, &length_item);
   25. ArkUI_NumberValue length_value1[] = {{.f32 = 650}};
   26. ArkUI_AttributeItem length_item1 = {length_value1, sizeof(length_value1) / sizeof(ArkUI_NumberValue)};
   27. nodeAPI->setAttribute(scroll, NODE_HEIGHT, &length_item1);
   28. ArkUI_AttributeItem scroll_id = {.string = "Scroll_CAPI"};
   29. nodeAPI->setAttribute(scroll, NODE_ID, &scroll_id);

   31. // 创建Column
   32. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   33. ArkUI_NumberValue value[] = {480};
   34. ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
   35. nodeAPI->setAttribute(column, NODE_WIDTH, &item);
   36. ArkUI_NumberValue column_bc[] = {{.u32 = 0xFFF00BB}};
   37. ArkUI_AttributeItem column_item = {column_bc, 1};
   38. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &column_item);
   39. ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
   40. nodeAPI->setAttribute(column, NODE_ID, &column_id);

   42. // 创建Text
   43. ArkUI_NodeHandle text0 = nodeAPI->createNode(ARKUI_NODE_TEXT);
   44. ArkUI_NumberValue text_width[] = {300};
   45. ArkUI_AttributeItem text_item0 = {text_width, sizeof(text_width) / sizeof(ArkUI_NumberValue)};
   46. nodeAPI->setAttribute(text0, NODE_WIDTH, &text_item0);
   47. ArkUI_NumberValue text_height[] = {50};
   48. ArkUI_AttributeItem text_item1 = {text_height, sizeof(text_height) / sizeof(ArkUI_NumberValue)};
   49. nodeAPI->setAttribute(text0, NODE_HEIGHT, &text_item1);
   50. ArkUI_AttributeItem text_item = {.string = "示例Text节点"};
   51. nodeAPI->setAttribute(text0, NODE_TEXT_CONTENT, &text_item);
   52. ArkUI_NumberValue margin[] = {10};
   53. ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};
   54. nodeAPI->setAttribute(text0, NODE_MARGIN, &item_margin);
   55. ArkUI_AttributeItem text0_id = {.string = "Text0_CAPI"};
   56. nodeAPI->setAttribute(text0, NODE_ID, &text0_id);
   57. a->node = text0;

   59. // 创建Row
   60. ArkUI_NodeHandle row0 = nodeAPI->createNode(ARKUI_NODE_ROW);
   61. ArkUI_NumberValue width_value[] = {{.f32=330}};
   62. ArkUI_AttributeItem width_item = {width_value, sizeof(width_value) / sizeof(ArkUI_NumberValue)};
   63. nodeAPI->setAttribute(row0, NODE_WIDTH, &width_item);
   64. nodeAPI->setAttribute(row0, NODE_HEIGHT, &text_item1);
   65. nodeAPI->setAttribute(row0, NODE_MARGIN, &item_margin);

   67. // 创建Button
   68. ArkUI_NodeHandle bt0 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   69. ArkUI_NumberValue btn_width[] = {150};
   70. ArkUI_AttributeItem btn_item0 = {btn_width, sizeof(btn_width) / sizeof(ArkUI_NumberValue)};
   71. nodeAPI->setAttribute(bt0, NODE_WIDTH, &btn_item0);
   72. nodeAPI->setAttribute(bt0, NODE_HEIGHT, &text_item1);
   73. nodeAPI->setAttribute(bt0, NODE_MARGIN, &item_margin);
   74. ArkUI_AttributeItem bt0_item = {.string = "GetAttachedNodeHandleById"};
   75. nodeAPI->setAttribute(bt0, NODE_BUTTON_LABEL, &bt0_item);
   76. nodeAPI->registerNodeEvent(bt0, NODE_ON_CLICK, 0, a);

   78. // 注册事件
   79. auto onClick = [](ArkUI_NodeEvent *event) {
   80. ArkUI_NodeHandle node = OH_ArkUI_NodeEvent_GetNodeHandle(event);
   81. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

   83. if (OH_ArkUI_NodeEvent_GetTargetId(event) == 0) {  // GetAttachedNodeHandleById
   84. A* a = (A*)OH_ArkUI_NodeEvent_GetUserData(event);
   85. ArkUI_NodeHandle node = nullptr;
   86. auto res = OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("Text0_CAPI", &node);
   87. if (node == a->node) {
   88. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "GetNodeByIdExample", "get Text0_CAPI success");
   89. } else {
   90. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "GetNodeByIdExample", "get Text0_CAPI failed");
   91. }
   92. }
   93. };
   94. nodeAPI->registerNodeEventReceiver(onClick);

   96. // 节点添加
   97. nodeAPI->addChild(scroll, column);
   98. nodeAPI->addChild(column, text0);
   99. nodeAPI->addChild(column, row0);
   100. nodeAPI->addChild(row0, bt0);

   102. return std::make_shared<ArkUINode>(scroll);
   103. }
   104. } // namespace NativeModule

   106. #endif // MYAPPLICATION_GETNODEBYID_H
   ```

   [GetNodeByIdExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/GetNodeByIdExample.h#L16-L123)
3. 在NativeEntry.cpp中，挂载Native节点。

   ```
   1. // NativeEntry.cpp
   2. #include <arkui/native_node_napi.h>
   3. #include <hilog/log.h>
   4. #include <js_native_api.h>
   5. #include "NativeEntry.h"
   6. #include "MoveToExample.h"
   7. #include "GetNodeByIdExample.h"

   10. namespace NativeModule {
   11. // ...
   12. static napi_value CreateNativeRoot(napi_env env, napi_callback_info info, const char *who, MakeNodeFn makeNodeFn)
   13. {
   14. size_t argc = 1;
   15. napi_value args[1] = {nullptr};

   17. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   19. // 获取NodeContent
   20. ArkUI_NodeContentHandle contentHandle;
   21. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   22. if (contentHandle == nullptr) {
   23. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, K_LOG_DOMAIN,
   24. "%{public}s nodeContentHandle is null", who);
   25. return nullptr;
   26. }
   27. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   29. // 创建节点
   30. auto node = makeNodeFn();

   32. // 保持Native侧对象到管理类中，维护生命周期。
   33. NativeEntry::GetInstance()->SetRootNode(node);
   34. return nullptr;
   35. }

   37. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   38. {
   39. // 从管理类中释放Native侧对象。
   40. NativeEntry::GetInstance()->DisposeRootNode();
   41. return nullptr;
   42. }
   43. // ...
   44. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/NativeEntry.cpp#L23-L97)
4. 运行程序，点击按钮，打印节点获取成功信息。

## 移动节点

使用[OH\_ArkUI\_NodeUtils\_MoveTo](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_moveto)接口，可以将Native节点移动到新的父节点下，从而按需改变节点树结构。

说明

当前仅支持以下类型的[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)进行移动操作：ARKUI\_NODE\_STACK、ARKUI\_NODE\_XCOMPONENT、ARKUI\_NODE\_EMBEDDED\_COMPONENT。对于其他类型的节点，移动操作不会生效。

1. ArkTS侧接入Native组件。

   ```
   1. // MoveTo.ets
   2. import nativeNode from 'libentry.so';
   3. import { NodeContent } from '@kit.ArkUI';

   5. @Entry
   6. @Component
   7. struct MoveTo {
   8. private rootSlot = new NodeContent();

   10. aboutToAppear(): void {
   11. nativeNode.createMoveToNode(this.rootSlot);
   12. }

   14. build() {
   15. Scroll() {
   16. Column({ space: 15 }) {
   17. Column() {
   18. ContentSlot(this.rootSlot)
   19. }
   20. }
   21. .width('100%')
   22. }.scrollBarColor(Color.Transparent)
   23. }
   24. }
   ```

   [MoveTo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/ets/pages/MoveTo.ets#L16-L41)
2. 新建MoveTo.h文件，在其中创建Stack节点，通过OH\_ArkUI\_NodeUtils\_MoveTo接口移动Stack节点。

   ```
   1. // MoveToExample.h
   2. #ifndef MYAPPLICATION_MOVETO_H
   3. #define MYAPPLICATION_MOVETO_H

   5. #include "ArkUINode.h"
   6. #include <hilog/log.h>

   8. namespace NativeModule {

   10. std::shared_ptr<ArkUIBaseNode> CreateMoveToExample()
   11. {
   12. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

   14. // 创建传入事件节点结构体
   15. struct A {
   16. ArkUI_NodeHandle node;
   17. ArkUI_NodeHandle targetParent;
   18. };
   19. A* a = new A;

   21. // 创建根节点Scroll
   22. ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_SCROLL);
   23. ArkUI_NumberValue length_value[] = {{.f32 = 480}};
   24. ArkUI_AttributeItem length_item = {length_value, sizeof(length_value) / sizeof(ArkUI_NumberValue)};
   25. nodeAPI->setAttribute(scroll, NODE_WIDTH, &length_item);
   26. ArkUI_NumberValue length_value1[] = {{.f32 = 650}};
   27. ArkUI_AttributeItem length_item1 = {length_value1, sizeof(length_value1) / sizeof(ArkUI_NumberValue)};
   28. nodeAPI->setAttribute(scroll, NODE_HEIGHT, &length_item1);
   29. ArkUI_AttributeItem scroll_id = {.string = "Scroll_CAPI"};
   30. nodeAPI->setAttribute(scroll, NODE_ID, &scroll_id);

   32. // 创建Column
   33. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   34. ArkUI_NumberValue value[] = {480};
   35. ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
   36. nodeAPI->setAttribute(column, NODE_WIDTH, &item);
   37. ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
   38. nodeAPI->setAttribute(column, NODE_ID, &column_id);

   40. // 创建Row
   41. ArkUI_NumberValue text_height[] = {50};
   42. ArkUI_AttributeItem text_item1 = {text_height, sizeof(text_height) / sizeof(ArkUI_NumberValue)};
   43. ArkUI_NumberValue margin[] = {10};
   44. ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};
   45. ArkUI_NodeHandle row0 = nodeAPI->createNode(ARKUI_NODE_ROW);
   46. ArkUI_NumberValue width_value[] = {{.f32=330}};
   47. ArkUI_AttributeItem width_item = {width_value, sizeof(width_value) / sizeof(ArkUI_NumberValue)};
   48. nodeAPI->setAttribute(row0, NODE_WIDTH, &width_item);
   49. nodeAPI->setAttribute(row0, NODE_HEIGHT, &text_item1);
   50. nodeAPI->setAttribute(row0, NODE_MARGIN, &item_margin);

   52. ArkUI_NodeHandle row1 = nodeAPI->createNode(ARKUI_NODE_ROW);
   53. nodeAPI->setAttribute(row1, NODE_WIDTH, &width_item);
   54. nodeAPI->setAttribute(row1, NODE_HEIGHT, &text_item1);
   55. nodeAPI->setAttribute(row1, NODE_MARGIN, &item_margin);
   56. a->targetParent = row1;

   58. ArkUI_NodeHandle row2 = nodeAPI->createNode(ARKUI_NODE_ROW);
   59. nodeAPI->setAttribute(row2, NODE_WIDTH, &width_item);
   60. nodeAPI->setAttribute(row2, NODE_HEIGHT, &text_item1);
   61. nodeAPI->setAttribute(row2, NODE_MARGIN, &item_margin);

   63. // 创建Stack
   64. ArkUI_NodeHandle stack0 = nodeAPI->createNode(ARKUI_NODE_STACK);
   65. ArkUI_NumberValue stack_value[] = {{.f32=50}};
   66. ArkUI_AttributeItem stack_item1 = {stack_value, sizeof(width_value) / sizeof(ArkUI_NumberValue)};
   67. nodeAPI->setAttribute(stack0, NODE_WIDTH, &stack_item1);
   68. nodeAPI->setAttribute(stack0, NODE_HEIGHT, &stack_item1);
   69. ArkUI_NumberValue stack_bc[] = {{.u32 = 0xFFFFB6C1}};
   70. ArkUI_AttributeItem stack_item2 = {stack_bc, 1};
   71. nodeAPI->setAttribute(stack0, NODE_BACKGROUND_COLOR, &stack_item2);
   72. a->node = stack0;

   74. ArkUI_NodeHandle stack1 = nodeAPI->createNode(ARKUI_NODE_STACK);
   75. nodeAPI->setAttribute(stack1, NODE_WIDTH, &stack_item1);
   76. nodeAPI->setAttribute(stack1, NODE_HEIGHT, &stack_item1);
   77. ArkUI_NumberValue stack_bc1[] = {{.u32 = 0xFF6495ED}};
   78. ArkUI_AttributeItem stack_item3 = {stack_bc1, 1};
   79. nodeAPI->setAttribute(stack1, NODE_BACKGROUND_COLOR, &stack_item3);

   81. ArkUI_NodeHandle stack2 = nodeAPI->createNode(ARKUI_NODE_STACK);
   82. nodeAPI->setAttribute(stack2, NODE_WIDTH, &stack_item1);
   83. nodeAPI->setAttribute(stack2, NODE_HEIGHT, &stack_item1);
   84. ArkUI_NumberValue stack_bc2[] = {{.u32 = 0xFF90EE90}};
   85. ArkUI_AttributeItem stack_item4 = {stack_bc2, 1};
   86. nodeAPI->setAttribute(stack2, NODE_BACKGROUND_COLOR, &stack_item4);

   88. ArkUI_NodeHandle stack3 = nodeAPI->createNode(ARKUI_NODE_STACK);
   89. nodeAPI->setAttribute(stack3, NODE_WIDTH, &stack_item1);
   90. nodeAPI->setAttribute(stack3, NODE_HEIGHT, &stack_item1);
   91. nodeAPI->setAttribute(stack3, NODE_BACKGROUND_COLOR, &stack_item2);

   93. ArkUI_NodeHandle stack4 = nodeAPI->createNode(ARKUI_NODE_STACK);
   94. nodeAPI->setAttribute(stack4, NODE_WIDTH, &stack_item1);
   95. nodeAPI->setAttribute(stack4, NODE_HEIGHT, &stack_item1);
   96. nodeAPI->setAttribute(stack4, NODE_BACKGROUND_COLOR, &stack_item3);

   98. ArkUI_NodeHandle stack5 = nodeAPI->createNode(ARKUI_NODE_STACK);
   99. nodeAPI->setAttribute(stack5, NODE_WIDTH, &stack_item1);
   100. nodeAPI->setAttribute(stack5, NODE_HEIGHT, &stack_item1);
   101. nodeAPI->setAttribute(stack5, NODE_BACKGROUND_COLOR, &stack_item4);

   103. // 创建Button
   104. ArkUI_NodeHandle bt0 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   105. ArkUI_NumberValue btn_width[] = {150};
   106. ArkUI_AttributeItem btn_item0 = {btn_width, sizeof(btn_width) / sizeof(ArkUI_NumberValue)};
   107. nodeAPI->setAttribute(bt0, NODE_WIDTH, &btn_item0);
   108. nodeAPI->setAttribute(bt0, NODE_HEIGHT, &text_item1);
   109. nodeAPI->setAttribute(bt0, NODE_MARGIN, &item_margin);
   110. ArkUI_AttributeItem bt0_item = {.string = "MoveTo"};
   111. nodeAPI->setAttribute(bt0, NODE_BUTTON_LABEL, &bt0_item);
   112. nodeAPI->registerNodeEvent(bt0, NODE_ON_CLICK, 0, a);

   114. // 注册事件
   115. auto onClick = [](ArkUI_NodeEvent *event) {
   116. ArkUI_NodeHandle node = OH_ArkUI_NodeEvent_GetNodeHandle(event);
   117. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

   119. if (OH_ArkUI_NodeEvent_GetTargetId(event) == 0) {  // MoveTo
   120. A* a = (A*)OH_ArkUI_NodeEvent_GetUserData(event);
   121. auto res = OH_ArkUI_NodeUtils_MoveTo(a->node, a->targetParent, 2);
   122. }
   123. };
   124. nodeAPI->registerNodeEventReceiver(onClick);

   126. // 节点添加
   127. nodeAPI->addChild(scroll, column);
   128. nodeAPI->addChild(column, row0);
   129. nodeAPI->addChild(column, row1);
   130. nodeAPI->addChild(column, row2);
   131. nodeAPI->addChild(row0, stack0);
   132. nodeAPI->addChild(row0, stack1);
   133. nodeAPI->addChild(row0, stack2);
   134. nodeAPI->addChild(row1, stack3);
   135. nodeAPI->addChild(row1, stack4);
   136. nodeAPI->addChild(row1, stack5);
   137. nodeAPI->addChild(row2, bt0);

   139. return std::make_shared<ArkUINode>(scroll);
   140. }
   141. } // namespace NativeModule

   143. #endif // MYAPPLICATION_MOVETO_H
   ```

   [MoveToExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/MoveToExample.h#L16-L160)
3. 在NativeEntry.cpp中，挂载Native节点。

   ```
   1. // NativeEntry.cpp
   2. #include <arkui/native_node_napi.h>
   3. #include <hilog/log.h>
   4. #include <js_native_api.h>
   5. #include "NativeEntry.h"
   6. #include "MoveToExample.h"
   7. #include "GetNodeByIdExample.h"

   10. namespace NativeModule {
   11. // ...
   12. static napi_value CreateNativeRoot(napi_env env, napi_callback_info info, const char *who, MakeNodeFn makeNodeFn)
   13. {
   14. size_t argc = 1;
   15. napi_value args[1] = {nullptr};

   17. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   19. // 获取NodeContent
   20. ArkUI_NodeContentHandle contentHandle;
   21. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   22. if (contentHandle == nullptr) {
   23. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, K_LOG_DOMAIN,
   24. "%{public}s nodeContentHandle is null", who);
   25. return nullptr;
   26. }
   27. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   29. // 创建节点
   30. auto node = makeNodeFn();

   32. // 保持Native侧对象到管理类中，维护生命周期。
   33. NativeEntry::GetInstance()->SetRootNode(node);
   34. return nullptr;
   35. }

   37. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   38. {
   39. // 从管理类中释放Native侧对象。
   40. NativeEntry::GetInstance()->DisposeRootNode();
   41. return nullptr;
   42. }
   43. // ...
   44. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/NativeEntry.cpp#L23-L97)
4. 运行程序，点击按钮，Stack节点会移动到目标位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/PkuRU4P7Shq7neZLV9_78w/zh-cn_image_0000002589324431.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052834Z&HW-CC-Expire=86400&HW-CC-Sign=3569E90BFAF2FC8219E2CE430B94AE506FE874CE06580DE399C6852C6FA1DF15)

## 在当前即时帧触发节点属性更新

从API version 21开始，使用[OH\_ArkUI\_NativeModule\_InvalidateAttributes](../harmonyos-references/capi-native-node-h.md#oh_arkui_nativemodule_invalidateattributes)接口，在当前帧即时触发节点属性更新，避免组件切换过程中出现闪烁。

1. ArkTS侧接入Native组件。

   ```
   1. import testNapi from 'libentry.so';
   2. import { NodeContent } from '@kit.ArkUI';

   4. @Component
   5. struct ImageContent {
   6. private nodeContent: NodeContent = new NodeContent();

   8. aboutToAppear() {
   9. // 通过C-API创建节点，并添加到管理器nodeContent上
   10. testNapi.createNativeNode(this.nodeContent);
   11. }
   12. build() {
   13. Column() {
   14. // 显示nodeContent管理器里存放的Native侧的组件
   15. ContentSlot(this.nodeContent)
   16. }
   17. }
   18. }

   20. @Entry
   21. @Component
   22. struct Index {
   23. @State message: string = 'Hello World';
   24. @State showParent: boolean = true;
   25. build() {
   26. Row() {
   27. Column() {
   28. // $r('app.string.Switch')需要替换为开发者所需的资源文件。
   29. Button($r('app.string.Switch')).onClick(()=>{
   30. this.showParent = !this.showParent;
   31. }).margin(20)
   32. if(this.showParent) {
   33. ImageContent()
   34. } else {
   35. ImageContent()
   36. }
   37. }
   38. .width('100%')
   39. }
   40. .height('100%')
   41. }
   42. }
   ```

   [Attribute.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/ets/pages/Attribute.ets#L16-L60)
2. 新建Attribute\_util.h用于设置组件属性。

   ```
   1. #ifndef MYAPPLICATION_ATTRIBUTE_UTIL_H
   2. #define MYAPPLICATION_ATTRIBUTE_UTIL_H

   4. #include <arkui/native_node.h>
   5. #include <cstdint>
   6. #include <string>
   7. class AttributeUtil {
   8. public:
   9. ArkUI_NativeNodeAPI_1 *api_;
   10. ArkUI_NodeHandle node_;
   11. AttributeUtil(ArkUI_NodeHandle node, ArkUI_NativeNodeAPI_1 *api)
   12. {
   13. this->node_ = node;
   14. api_ = api;
   15. }
   16. int32_t Width(float width)
   17. {
   18. ArkUI_NumberValue NODE_WIDTH_value[] = {width};
   19. ArkUI_AttributeItem NODE_WIDTH_Item = {NODE_WIDTH_value, 1};
   20. return api_->setAttribute(node_, NODE_WIDTH, &NODE_WIDTH_Item);
   21. }
   22. int32_t Height(float height)
   23. {
   24. ArkUI_NumberValue NODE_HEIGHT_value[] = {height};
   25. ArkUI_AttributeItem NODE_HEIGHT_Item = {NODE_HEIGHT_value, 1};
   26. return api_->setAttribute(node_, NODE_HEIGHT, &NODE_HEIGHT_Item);
   27. }
   28. int32_t ImageSrc(std::string src)
   29. {
   30. ArkUI_AttributeItem NODE_IMAGE_SRC_VALUE = {.string = src.c_str()};
   31. return api_->setAttribute(node_, NODE_IMAGE_SRC, &NODE_IMAGE_SRC_VALUE);
   32. }
   33. int32_t ImageSyncLoad()
   34. {
   35. ArkUI_NumberValue NODE_TRANSLATE_ITEM_VALUE[] = {{.i32 = 1}};
   36. ArkUI_AttributeItem NODE_BORDER_WIDTH_ITEM = {NODE_TRANSLATE_ITEM_VALUE, 1};
   37. return api_->setAttribute(node_, NODE_IMAGE_SYNC_LOAD, &NODE_BORDER_WIDTH_ITEM);
   38. }
   39. };
   40. #endif // MYAPPLICATION_ATTRIBUTE_UTIL_H
   ```

   [Attribute\_util.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/Attribute_util.h#L16-L57)
3. 在nai\_init.cpp中，挂载Native节点。

   ```
   1. #include "Attribute_util.h"
   2. #include "napi/native_api.h"
   3. #include <arkui/native_interface.h>
   4. #include <arkui/native_node.h>
   5. #include <arkui/native_node_napi.h>
   6. #include <hilog/log.h>
   7. #include <js_native_api.h>
   8. #include <js_native_api_types.h>
   9. // ...
   10. const unsigned int NUMBER_2 = 2;
   11. const unsigned int NUMBER_WIDTH = 100;
   12. const unsigned int NUMBER_HEIGHT = 100;

   14. static napi_value Add(napi_env env, napi_callback_info info)
   15. {
   16. size_t argc = NUMBER_2;
   17. napi_value args[NUMBER_2] = {nullptr};

   19. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   21. napi_valuetype valuetype0;
   22. napi_typeof(env, args[0], &valuetype0);

   24. napi_valuetype valuetype1;
   25. napi_typeof(env, args[1], &valuetype1);

   27. double value0;
   28. napi_get_value_double(env, args[0], &value0);

   30. double value1;
   31. napi_get_value_double(env, args[1], &value1);

   33. napi_value sum;
   34. napi_create_double(env, value0 + value1, &sum);

   36. return sum;
   37. }

   39. static ArkUI_NativeNodeAPI_1 *nodeAPI = nullptr;

   41. static napi_value NAPI_Global_createNativeNode(napi_env env, napi_callback_info info)
   42. {
   43. size_t argc = 1;
   44. napi_value args[1] = {nullptr};
   45. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   46. ArkUI_NodeContentHandle contentHandle;
   47. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   48. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nodeAPI);
   49. // 创建Image组件
   50. auto imageNode = nodeAPI->createNode(ARKUI_NODE_IMAGE);
   51. AttributeUtil imageNodeAttr(imageNode, nodeAPI);
   52. // 设置image组件属性
   53. imageNodeAttr.ImageSrc("resources/base/media/startIcon.png");
   54. imageNodeAttr.ImageSyncLoad();
   55. imageNodeAttr.Width(NUMBER_WIDTH);
   56. imageNodeAttr.Height(NUMBER_HEIGHT);
   57. // 在当前即时帧触发节点属性更新
   58. OH_ArkUI_NativeModule_InvalidateAttributes(imageNode);
   59. // 挂载image组件到组件树
   60. OH_ArkUI_NodeContent_AddNode(contentHandle, imageNode);
   61. return nullptr;
   62. }

   64. EXTERN_C_START
   65. static napi_value Init(napi_env env, napi_value exports)
   66. {
   67. napi_property_descriptor desc[] = {
   68. {"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
   69. {"createNativeNode", nullptr, NAPI_Global_createNativeNode, nullptr, nullptr, nullptr, napi_default, nullptr},
   70. // ...
   71. };
   72. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   73. return exports;
   74. }
   75. EXTERN_C_END

   77. static napi_module demoModule = {
   78. .nm_version = 1,
   79. .nm_flags = 0,
   80. .nm_filename = nullptr,
   81. .nm_register_func = Init,
   82. .nm_modname = "entry",
   83. .nm_priv = ((void*)0),
   84. .reserved = { 0 },
   85. };

   87. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   88. {
   89. napi_module_register(&demoModule);
   90. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/napi_init.cpp#L18-L122)
4. 运行程序，点击按钮，切换图片正常展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Px9Nqj8nRHqBJoYpQvq9-w/zh-cn_image_0000002589244371.png?HW-CC-KV=V1&HW-CC-Date=20260429T052834Z&HW-CC-Expire=86400&HW-CC-Sign=D8BB7868F4E5F07A643A6533CB0A35319941924D1750C7E1AE42944B66DCB384)

## 用不同的展开模式获取对应下标的子节点

NDK支持通过不同的展开方式获取目标节点下的有效节点信息。例如，在LazyForEach场景下，可以处理存在多个子节点的情况。

从API version 20开始，使用[OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getfirstchildindexwithoutexpand)接口，可以获取目标节点的第一个存在于组件树的节点。使用[OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getlastchildindexwithoutexpand)接口，可以获取目标节点的最后一个存在于组件树的节点。[OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getchildwithexpandmode)接口，可以通过不同的节点展开模式获取对应下标的子节点。

说明

节点展开方式请参考[ArkUI\_ExpandMode](../harmonyos-references/capi-native-type-h.md#arkui_expandmode)，此处推荐使用ARKUI\_LAZY\_EXPAND懒展开方式，智能识别对应场景。

1. 通过ArkTS构造LazyForEach及ArkTS的下树节点展开场景。

   ```
   1. import { NodeController, FrameNode, UIContext, BuilderNode, ExpandMode, LengthUnit } from '@kit.ArkUI';

   3. const TEST_TAG: string = "FrameNode ";

   5. // BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
   6. class BasicDataSource implements IDataSource {
   7. private listeners: DataChangeListener[] = [];
   8. private originDataArray: string[] = [];

   10. public totalCount(): number {
   11. return 0;
   12. }

   14. public getData(index: number): string {
   15. return this.originDataArray[index];
   16. }

   18. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
   19. registerDataChangeListener(listener: DataChangeListener): void {
   20. if (this.listeners.indexOf(listener) < 0) {
   21. console.info('add listener');
   22. this.listeners.push(listener);
   23. }
   24. }

   26. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
   27. unregisterDataChangeListener(listener: DataChangeListener): void {
   28. const pos = this.listeners.indexOf(listener);
   29. if (pos >= 0) {
   30. console.info('remove listener');
   31. this.listeners.splice(pos, 1);
   32. }
   33. }

   35. // 通知LazyForEach组件需要重载所有子组件
   36. notifyDataReload(): void {
   37. this.listeners.forEach(listener => {
   38. listener.onDataReloaded();
   39. })
   40. }

   42. // 通知LazyForEach组件需要在index对应索引处添加子组件
   43. notifyDataAdd(index: number): void {
   44. this.listeners.forEach(listener => {
   45. listener.onDataAdd(index);
   46. // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
   47. })
   48. }

   50. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
   51. notifyDataChange(index: number): void {
   52. this.listeners.forEach(listener => {
   53. listener.onDataChange(index);
   54. // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
   55. })
   56. }

   58. // 通知LazyForEach组件需要在index对应索引处删除该子组件
   59. notifyDataDelete(index: number): void {
   60. this.listeners.forEach(listener => {
   61. listener.onDataDelete(index);
   62. // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
   63. })
   64. }

   66. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
   67. notifyDataMove(from: number, to: number): void {
   68. this.listeners.forEach(listener => {
   69. listener.onDataMove(from, to);
   70. // 写法2：listener.onDatasetChange(
   71. //         [{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
   72. })
   73. }

   75. notifyDatasetChange(operations: DataOperation[]): void {
   76. this.listeners.forEach(listener => {
   77. listener.onDatasetChange(operations);
   78. })
   79. }
   80. }

   82. class MyDataSource extends BasicDataSource {
   83. private dataArray: string[] = []

   85. public totalCount(): number {
   86. return this.dataArray.length;
   87. }

   89. public getData(index: number): string {
   90. return this.dataArray[index];
   91. }

   93. public addData(index: number, data: string): void {
   94. this.dataArray.splice(index, 0, data);
   95. this.notifyDataAdd(index);
   96. }

   98. public pushData(data: string): void {
   99. this.dataArray.push(data);
   100. this.notifyDataAdd(this.dataArray.length - 1);
   101. }
   102. }

   104. class Params {
   105. data: MyDataSource | null = null;
   106. scroller: Scroller | null = null;
   107. constructor(data: MyDataSource, scroller: Scroller) {
   108. this.data = data;
   109. this.scroller = scroller;
   110. }
   111. }

   113. @Builder
   114. function buildData(params: Params) {
   115. List({ scroller: params.scroller }) {
   116. LazyForEach(params.data, (item: string) => {
   117. ListItem() {
   118. Column() {
   119. Text(item)
   120. .fontSize(20)
   121. .onAppear(() => {
   122. console.info(TEST_TAG + " node appear: " + item)
   123. })
   124. .backgroundColor(Color.Pink)
   125. .margin({
   126. top: 30,
   127. bottom: 30,
   128. left: 10,
   129. right: 10
   130. })
   131. }
   132. }
   133. .id(item)
   134. }, (item: string) => item)
   135. }
   136. .cachedCount(5)
   137. .listDirection(Axis.Horizontal)
   138. }

   140. class MyNodeController extends NodeController {
   141. private rootNode: FrameNode | null = null;
   142. private uiContext: UIContext | null = null;
   143. private data: MyDataSource = new MyDataSource();
   144. private scroller: Scroller = new Scroller();

   146. makeNode(uiContext: UIContext): FrameNode | null {
   147. this.uiContext = uiContext;
   148. for (let i = 0; i <= 20; i++) {
   149. this.data.pushData(`N${i}`);
   150. }
   151. const params: Params = new Params(this.data, this.scroller);
   152. const dataNode: BuilderNode<[Params]> = new BuilderNode(uiContext);
   153. dataNode.build(wrapBuilder<[Params]>(buildData), params);
   154. this.rootNode = dataNode.getFrameNode();
   155. const scrollToIndexOptions: ScrollToIndexOptions = {
   156. extraOffset: {
   157. value: 20, unit: LengthUnit.VP
   158. }
   159. };
   160. this.scroller.scrollToIndex(6, true, ScrollAlign.START, scrollToIndexOptions);
   161. return this.rootNode;
   162. }

   164. // 获取不展开场景下第一个活跃节点的下标
   165. getFirstChildIndexWithoutExpand() {
   166. console.info(`${TEST_TAG} getFirstChildIndexWithoutExpand: ${this.rootNode!.getFirstChildIndexWithoutExpand()}`);
   167. }

   169. // 获取不展开场景下最后一个活跃节点的下标
   170. getLastChildIndexWithoutExpand() {
   171. console.info(`${TEST_TAG} getLastChildIndexWithoutExpand: ${this.rootNode!.getLastChildIndexWithoutExpand()}`);
   172. }

   174. // 用不展开的方式获取节点
   175. getChildWithNotExpand() {
   176. const childNode = this.rootNode!.getChild(3, ExpandMode.NOT_EXPAND);
   177. console.info(TEST_TAG + " getChild(3, ExpandMode.NOT_EXPAND): " + childNode?.getId());
   178. if (childNode?.getId() === "N9") {
   179. console.info(TEST_TAG + " getChild(3, ExpandMode.NOT_EXPAND)  result: success.");
   180. } else {
   181. console.info(TEST_TAG + " getChild(3, ExpandMode.NOT_EXPAND)  result: fail.");
   182. }
   183. }

   185. // 以展开的方式获取节点
   186. getChildWithExpand() {
   187. const childNode = this.rootNode!.getChild(3, ExpandMode.EXPAND);
   188. console.info(TEST_TAG + " getChild(3, ExpandMode.EXPAND): " + childNode?.getId());
   189. if (childNode?.getId() === "N3") {
   190. console.info(TEST_TAG + " getChild(3, ExpandMode.EXPAND)  result: success.");
   191. } else {
   192. console.info(TEST_TAG + " getChild(3, ExpandMode.EXPAND)  result: fail.");
   193. }
   194. }

   196. getChildWithLazyExpand() {
   197. const childNode = this.rootNode!.getChild(3, ExpandMode.LAZY_EXPAND);
   198. console.info(TEST_TAG + " getChild(3, ExpandMode.LAZY_EXPAND): " + childNode?.getId());
   199. if (childNode?.getId() === "N3") {
   200. console.info(TEST_TAG + " getChild(3, ExpandMode.LAZY_EXPAND)  result: success.");
   201. } else {
   202. console.info(TEST_TAG + " getChild(3, ExpandMode.LAZY_EXPAND)  result: fail.");
   203. }
   204. }
   205. }

   207. @Entry
   208. @Component
   209. struct Index {
   210. private myNodeController: MyNodeController = new MyNodeController();
   211. private scroller: Scroller = new Scroller();

   213. build() {
   214. Scroll(this.scroller) {
   215. Column({ space: 8 }) {
   216. Column() {
   217. Text("This is a NodeContainer.")
   218. .textAlign(TextAlign.Center)
   219. .borderRadius(10)
   220. .backgroundColor(0xFFFFFF)
   221. .width('100%')
   222. .fontSize(16)
   223. NodeContainer(this.myNodeController)
   224. .borderWidth(1)
   225. .width(300)
   226. .height(100)
   227. }

   229. Button("getFirstChildIndexWithoutExpand")
   230. .width(300)
   231. .onClick(() => {
   232. this.myNodeController.getFirstChildIndexWithoutExpand();
   233. })
   234. Button("getLastChildIndexWithoutExpand")
   235. .width(300)
   236. .onClick(() => {
   237. this.myNodeController.getLastChildIndexWithoutExpand();
   238. })
   239. Button("getChildWithNotExpand")
   240. .width(300)
   241. .onClick(() => {
   242. this.myNodeController.getChildWithNotExpand();
   243. })
   244. Button("getChildWithExpand")
   245. .width(300)
   246. .onClick(() => {
   247. this.myNodeController.getChildWithExpand();
   248. })
   249. Button("getChildWithLazyExpand")
   250. .width(300)
   251. .onClick(() => {
   252. this.myNodeController.getChildWithLazyExpand();
   253. })
   254. }
   255. .width("100%")
   256. }
   257. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
   258. }
   259. }
   ```
2. NDK侧通过[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid)接口获取ArkTS组件，并通过懒展开模式获取对应的子组件信息。

   ```
   1. ArkUI_NodeHandle childNode = nullptr;
   2. OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("N3", &childNode);

   4. uint32_t index = 0;
   5. OH_ArkUI_NodeUtils_GetFirstChildIndexWithoutExpand(childNode, &index);
   6. uint32_t index1 = 0;
   7. OH_ArkUI_NodeUtils_GetLastChildIndexWithoutExpand(childNode, &index1);
   8. ArkUI_NodeHandle child = nullptr;
   9. auto result = OH_ArkUI_NodeUtils_GetChildWithExpandMode(childNode, 3, &child, 0);
   10. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "Manager",
   11. "firstChildIndex - lastChildIndex == %{d -- %{public}d, -- getResult = %{public}d",
   12. index, index1, result);
   ```

   [ShowSubcomponentInfo.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NdkNodeQueryOperate/entry/src/main/cpp/ShowSubcomponentInfo.h#L30-L43)
3. 查看日志打印的对应错误码返回是否正确，以此判断是否成功获取到对应子节点。

## 节点是否处于渲染状态

从API version 23开始，使用[OH\_ArkUI\_NativeModule\_IsInRenderState](../harmonyos-references/capi-native-node-h.md#oh_arkui_nativemodule_isinrenderstate)接口，可以查询节点是否在渲染树上。

1. ArkTS侧接入Native组件。

   ```
   1. //Index.ets

   3. import testNapi from 'libentry.so';
   4. import { NodeContent } from '@kit.ArkUI';

   6. @Component
   7. struct TestContent {
   8. private nodeContent: NodeContent = new NodeContent();

   10. aboutToAppear() {
   11. // 通过C-API创建节点，并添加到管理器nodeContent上
   12. testNapi.createNativeNode(this.nodeContent);
   13. }
   14. build() {
   15. Column() {
   16. // 显示nodeContent管理器里存放的Native侧的组件
   17. ContentSlot(this.nodeContent)
   18. }
   19. }
   20. }

   22. @Entry
   23. @Component
   24. struct Index {
   25. @State message: string = 'Hello World';
   26. @State showParent: boolean = true;
   27. build() {
   28. Row() {
   29. Column() {
   30. TestContent()
   31. }
   32. .width('100%')
   33. }
   34. .height('100%')
   35. }
   36. }
   ```
2. 新建Attribute\_util .h用于设置组件属性。

   ```
   1. #ifndef MYAPPLICATION_ATTRIBUTE_UTIL_H
   2. #define MYAPPLICATION_ATTRIBUTE_UTIL_H
   3. #include <arkui/native_node.h>
   4. #include <cstdint>
   5. #include <string>
   6. class AttributeUtil {
   7. public:
   8. ArkUI_NativeNodeAPI_1 *api_;
   9. ArkUI_NodeHandle node_;
   10. AttributeUtil(ArkUI_NodeHandle node, ArkUI_NativeNodeAPI_1 *api) {
   11. this->node_ = node;
   12. api_ = api;
   13. }
   14. int32_t width(float width) {
   15. ArkUI_NumberValue NODE_WIDTH_value[] = {width};
   16. ArkUI_AttributeItem NODE_WIDTH_Item = {NODE_WIDTH_value, 1};
   17. return api_->setAttribute(node_, NODE_WIDTH, &NODE_WIDTH_Item);
   18. }
   19. int32_t height(float height) {
   20. ArkUI_NumberValue NODE_HEIGHT_value[] = {height};
   21. ArkUI_AttributeItem NODE_HEIGHT_Item = {NODE_HEIGHT_value, 1};
   22. return api_->setAttribute(node_, NODE_HEIGHT, &NODE_HEIGHT_Item);
   23. }

   25. int32_t buttonLabel(std::string text) {
   26. ArkUI_AttributeItem NODE_TRANSLATE_ITEM_LABEL = {.string = text.c_str()};
   27. return api_->setAttribute(node_, NODE_BUTTON_LABEL, &NODE_TRANSLATE_ITEM_LABEL);
   28. }

   30. int32_t text(std::string str) {
   31. ArkUI_AttributeItem TEXT_ITEM = {.string = str.c_str()};
   32. return api_->setAttribute(node_, NODE_TEXT_CONTENT, &TEXT_ITEM);
   33. }

   35. int32_t visibility(int isSHow) {
   36. ArkUI_NumberValue NODE_VISIBILITY_ITEM_VALUE = {.i32 = isSHow};
   37. ArkUI_AttributeItem NODE_VISIBILITY__ITEM = {&NODE_VISIBILITY_ITEM_VALUE, 1};
   38. return api_->setAttribute(node_, NODE_VISIBILITY, &NODE_VISIBILITY__ITEM);
   39. }

   41. int32_t margin(float value) {
   42. ArkUI_NumberValue NODE_margin_ITEM_VALUE = {.f32 = value};
   43. ArkUI_AttributeItem NODE_MARGIN_ITEM = {&NODE_margin_ITEM_VALUE, 1};
   44. return api_->setAttribute(node_, NODE_MARGIN, &NODE_MARGIN_ITEM);
   45. }
   46. };

   48. #endif // MYAPPLICATION_ATTRIBUTE_UTIL_H
   ```
3. 在nai\_init.cpp中，挂载Native节点。

   ```
   1. #include "napi/native_api.h"
   2. #include "AttributeUtil.h"
   3. #include <arkui/native_interface.h>
   4. #include <arkui/native_node.h>
   5. #include <arkui/native_node_napi.h>
   6. #include <hilog/log.h>

   8. static ArkUI_NativeNodeAPI_1 *nodeAPI = nullptr;
   9. static ArkUI_NodeHandle textNode = nullptr;
   10. static bool showText = false;

   12. namespace Event {
   13. void onClickFunc(ArkUI_NodeEvent *event) {
   14. AttributeUtil textAttr(textNode, nodeAPI);
   15. if (showText) {
   16. textAttr.visibility(0);
   17. } else {
   18. textAttr.visibility(1);
   19. }
   20. showText = !showText;
   21. bool isOnRenderTree = false;
   22. OH_ArkUI_NativeModule_IsInRenderState(textNode, &isOnRenderTree);
   23. OH_LOG_Print(LOG_APP, LOG_INFO, 1, "event","on render tree statie is %{public}d", isOnRenderTree);
   24. }
   25. } // namespace Event

   28. static napi_value NAPI_Global_createNativeNode(napi_env env, napi_callback_info info) {
   29. size_t argc = 1;
   30. napi_value args[1] = {nullptr};
   31. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   32. ArkUI_NodeContentHandle contentHandle;
   33. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   34. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_NODE, ArkUI_NativeNodeAPI_1, nodeAPI);
   35. auto columnTest = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   36. AttributeUtil columnAttr(columnTest, nodeAPI);
   37. columnAttr.width(300);
   38. columnAttr.height(300);
   39. auto buttonNode = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   40. nodeAPI->addChild(columnTest, buttonNode);
   41. AttributeUtil buttonAttr(buttonNode, nodeAPI);
   42. buttonAttr.width(200);
   43. buttonAttr.height(30);
   44. buttonAttr.margin(20);
   45. buttonAttr.buttonLabel("change text visibility");
   46. nodeAPI->registerNodeEvent(buttonNode, NODE_ON_CLICK, 1, nullptr);
   47. nodeAPI->registerNodeEventReceiver(Event::onClickFunc);
   48. textNode = nodeAPI->createNode(ARKUI_NODE_TEXT);
   49. nodeAPI->addChild(columnTest, textNode);
   50. AttributeUtil textAttr(textNode, nodeAPI);
   51. textAttr.text("hello word");
   52. OH_ArkUI_NodeContent_AddNode(contentHandle, columnTest);
   53. return nullptr;
   54. }
   55. EXTERN_C_START
   56. static napi_value Init(napi_env env, napi_value exports) {
   57. napi_property_descriptor desc[] = {
   58. {"createNativeNode", nullptr, NAPI_Global_createNativeNode, nullptr, nullptr, nullptr, napi_default, nullptr}};
   59. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   60. return exports;
   61. }
   62. EXTERN_C_END

   64. static napi_module demoModule = {
   65. .nm_version = 1,
   66. .nm_flags = 0,
   67. .nm_filename = nullptr,
   68. .nm_register_func = Init,
   69. .nm_modname = "entry",
   70. .nm_priv = ((void *)0),
   71. .reserved = {0},
   72. };

   74. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
4. 运行程序，点击change text visibility后打印text是否在渲染树上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_EDl_fhRTICme_2QKbf5jA/zh-cn_image_0000002558764564.png?HW-CC-KV=V1&HW-CC-Date=20260429T052834Z&HW-CC-Expire=86400&HW-CC-Sign=E43F4C4BF2829A7DEEE809D6651ED99C1795130CB98B4030BB4A00C542E8E125)
