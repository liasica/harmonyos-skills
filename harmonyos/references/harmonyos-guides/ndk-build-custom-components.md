---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-custom-components
title: 构建自定义组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建自定义组件
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:27a26ac86f4823ed38d77c7f279154556268d305315aef5f31f3201c86303146
---

ArkUI开发框架在NDK接口提供了自定义UI组件的能力，这些能力包括自定义测算，自定义布局和自定义绘制。开发者通过注册相关自定义回调事件接入ArkUI开发框架的布局渲染流程，这些事件需要使用[registerNodeCustomEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomevent)来进行声明，并通过[addNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodecustomeventreceiver)函数添加组件自定义事件的监听器，在该监听器的回调函数中处理相关自定义测算，自定义布局和自定义绘制逻辑。

说明

* 自定义组件事件注册需要[addNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodecustomeventreceiver)声明监听器注册和[registerNodeCustomEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomevent)声明需要的自定义事件类型，监听器只能监听已声明的事件。
* 需要关注事件的反注册逻辑，如在组件销毁前调用[removeNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removenodecustomeventreceiver)移除事件监听器，[unregisterNodeCustomEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#unregisternodecustomevent)通知ArkUI框架已监听的自定义组件事件不再需要监听。
* [addNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodecustomeventreceiver)可以添加多个函数指针，每个函数指针都会在对应事件触发时触发，对应的[removeNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#removenodecustomeventreceiver)需要传递对应的函数指针用于移除监听。
* [registerNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomeventreceiver)是全局监听函数，不同于[addNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addnodecustomeventreceiver)，[registerNodeCustomEventReceiver](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomeventreceiver)能够监听所有Native组件的自定义事件触发，但只能传递一个函数指针，多次调用使用最后一次的函数指针进行回调，释放时使用unregisterNodeCustomEventReceiver进行反注册。
* 自定义组件相关接口（[measureNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#measurenode)、[layoutNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#layoutnode)、[setMeasuredSize](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setmeasuredsize)、[setLayoutPosition](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setlayoutposition)）仅允许在对应的自定义事件（[ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE、ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT](../harmonyos-references/capi-native-node-h.md#arkui_nodecustomeventtype)）回调中使用。

## 自定义布局容器

以下示例创建了一个自定义容器，该容器将子组件最大值加上额外边距作为自身大小，同时对子组件进行居中排布。

**图1** 自定义容器组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vSsjk44-QFaI8AjoihDFWg/zh-cn_image_0000002589324427.png?HW-CC-KV=V1&HW-CC-Date=20260429T052832Z&HW-CC-Expire=86400&HW-CC-Sign=401965EB3F7AA5DA689E956152AF9C7485EF791C22BDD715A892C7477A825434)

1. 按照[接入ArkTS页面](ndk-access-the-arkts-page.md)创建前置工程。
2. 创建自定义容器组件封装对象。

   ```
   1. // ArkUICustomContainerNode.h
   2. // 自定义容器组件示例

   4. #ifndef MYAPPLICATION_ARKUICUSTOMCONTAINERNODE_H
   5. #define MYAPPLICATION_ARKUICUSTOMCONTAINERNODE_H

   7. #include "ArkUINode.h"

   9. namespace NativeModule {

   11. class ArkUICustomContainerNode : public ArkUINode {
   12. public:
   13. // 使用自定义组件类型ARKUI_NODE_CUSTOM创建组件。
   14. ArkUICustomContainerNode()
   15. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_CUSTOM))
   16. {
   17. // 注册自定义事件监听器。
   18. nativeModule_->addNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   19. // 声明自定义事件并传递自身作为自定义数据。
   20. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE, 0, this);
   21. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT, 0, this);
   22. }

   24. ~ArkUICustomContainerNode() override
   25. {
   26. // 反注册自定义事件监听器。
   27. nativeModule_->removeNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   28. // 取消声明自定义事件。
   29. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE);
   30. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT);
   31. }

   33. void SetPadding(int32_t padding)
   34. {
   35. padding_ = padding;
   36. // 自定义属性事件更新需要主动调用标记脏区接口。
   37. nativeModule_->markDirty(handle_, NODE_NEED_MEASURE);
   38. }

   40. private:
   41. static void OnStaticCustomEvent(ArkUI_NodeCustomEvent *event)
   42. {
   43. // 获取组件实例对象，调用相关实例方法。
   44. auto customNode = reinterpret_cast<ArkUICustomContainerNode *>(OH_ArkUI_NodeCustomEvent_GetUserData(event));
   45. auto type = OH_ArkUI_NodeCustomEvent_GetEventType(event);
   46. switch (type) {
   47. case ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE:
   48. customNode->OnMeasure(event);
   49. break;
   50. case ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT:
   51. customNode->OnLayout(event);
   52. break;
   53. default:
   54. break;
   55. }
   56. }

   58. // 自定义测算逻辑。
   59. void OnMeasure(ArkUI_NodeCustomEvent *event)
   60. {
   61. auto layoutConstrain = OH_ArkUI_NodeCustomEvent_GetLayoutConstraintInMeasure(event);
   62. // 创建子节点布局限制，复用父组件布局中的百分比参考值。
   63. auto childLayoutConstrain = OH_ArkUI_LayoutConstraint_Copy(layoutConstrain);
   64. int32_t maxConstrain = 1000;
   65. OH_ArkUI_LayoutConstraint_SetMaxHeight(childLayoutConstrain, maxConstrain);
   66. OH_ArkUI_LayoutConstraint_SetMaxWidth(childLayoutConstrain, maxConstrain);
   67. OH_ArkUI_LayoutConstraint_SetMinHeight(childLayoutConstrain, 0);
   68. OH_ArkUI_LayoutConstraint_SetMinWidth(childLayoutConstrain, 0);

   70. // 测算子节点获取子节点最大值。
   71. auto totalSize = nativeModule_->getTotalChildCount(handle_);
   72. int32_t maxWidth = 0;
   73. int32_t maxHeight = 0;
   74. for (uint32_t i = 0; i < totalSize; i++) {
   75. auto child = nativeModule_->getChildAt(handle_, i);
   76. // 调用测算接口测算Native组件。
   77. nativeModule_->measureNode(child, childLayoutConstrain);
   78. auto size = nativeModule_->getMeasuredSize(child);
   79. if (size.width > maxWidth) {
   80. maxWidth = size.width;
   81. }
   82. if (size.height > maxHeight) {
   83. maxHeight = size.height;
   84. }
   85. }
   86. // 自定义测算为所有子节点大小加固定边距。该自定义节点最终的尺寸以此处设置的值为准。
   87. const int paddingMultiplier = 2;
   88. nativeModule_->setMeasuredSize(handle_, maxWidth + paddingMultiplier * padding_,
   89. maxHeight + paddingMultiplier * padding_);
   90. }

   92. void OnLayout(ArkUI_NodeCustomEvent *event)
   93. {
   94. // 获取父组件期望位置并设置。
   95. auto position = OH_ArkUI_NodeCustomEvent_GetPositionInLayout(event);
   96. nativeModule_->setLayoutPosition(handle_, position.x, position.y);

   98. // 设置子组件居中对齐。
   99. auto totalSize = nativeModule_->getTotalChildCount(handle_);
   100. auto selfSize = nativeModule_->getMeasuredSize(handle_);
   101. for (uint32_t i = 0; i < totalSize; i++) {
   102. auto child = nativeModule_->getChildAt(handle_, i);
   103. // 获取子组件大小。
   104. auto childSize = nativeModule_->getMeasuredSize(child);
   105. // 布局子组件位置。
   106. int32_t horizontalMargin = (selfSize.width - childSize.width) / 2;
   107. int32_t verticalMargin = (selfSize.height - childSize.height) / 2;
   108. nativeModule_->layoutNode(child, horizontalMargin, verticalMargin);
   109. }
   110. }

   112. int32_t padding_ = 100;
   113. };

   115. } // namespace NativeModule

   117. #endif // MYAPPLICATION_ARKUICUSTOMCONTAINERNODE_H
   ```

   [ArkUICustomContainerNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomContainerSample/entry/src/main/cpp/ArkUICustomContainerNode.h#L15-L133)
3. 使用自定义容器创建带文本的示例界面。

   ```
   1. #include "NativeEntry.h"

   3. #include "ArkUICustomContainerNode.h"
   4. #include "ArkUITextNode.h"
   5. #include "UITimer.h"

   7. #include <arkui/native_node_napi.h>
   8. #include <arkui/native_type.h>
   9. #include <js_native_api.h>

   11. namespace NativeModule {
   12. namespace {
   13. napi_env g_env;
   14. } // namespace

   16. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   17. {
   18. size_t argc = 1;
   19. napi_value args[1] = {nullptr};

   21. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   23. ArkUI_NodeContentHandle contentHandle;
   24. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   25. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   27. // 创建自定义容器和文本组件。
   28. auto node = std::make_shared<ArkUICustomContainerNode>();
   29. node->SetBackgroundColor(0xFFE0FFFF);
   30. auto textNode = std::make_shared<ArkUITextNode>();
   31. textNode->SetTextContent("CustomContainer Example");
   32. const int32_t fontSize = 16;
   33. textNode->SetFontSize(fontSize);
   34. textNode->SetBackgroundColor(0xFFfffacd);
   35. textNode->SetTextAlign(ARKUI_TEXT_ALIGNMENT_CENTER);
   36. node->AddChild(textNode);
   37. auto onClick = [](ArkUI_NodeEvent *event) {
   38. auto textNode = (ArkUITextNode *)OH_ArkUI_NodeEvent_GetUserData(event);
   39. textNode->SetFontColor(0xFF00FF7F);
   40. };
   41. textNode->RegisterOnClick(onClick, textNode.get());

   43. // 保持Native侧对象到管理类中，维护生命周期。
   44. NativeEntry::GetInstance()->SetRootNode(node);
   45. g_env = env;
   46. return nullptr;
   47. }

   49. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   50. {
   51. // 从管理类中释放Native侧对象。
   52. NativeEntry::GetInstance()->DisposeRootNode();
   53. return nullptr;
   54. }

   56. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomContainerSample/entry/src/main/cpp/NativeEntry.cpp#L15-L72)
4. 修改CMakeLists.txt，添加链接库。

   ```
   1. # CMakeLists.txt

   3. # the minimum version of CMake.
   4. cmake_minimum_required(VERSION 3.4.1)
   5. project(testndk)

   7. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   9. include_directories(${NATIVERENDER_ROOT_PATH}
   10. ${NATIVERENDER_ROOT_PATH}/include)

   12. add_library(entry SHARED NativeEntry.cpp napi_init.cpp)
   13. # target_link_libraries(entry PUBLIC libace_napi.z.so, libace_ndk.z.so, libhilog_ndk.z.so)

   15. find_library(
   16. # Sets the name of the path variable.
   17. hilog-lib
   18. # Specifies the name of the NDK library that
   19. # you want CMake to locate.
   20. hilog_ndk.z
   21. )

   23. find_library(
   24. # Sets the name of the path variable.
   25. libace-lib
   26. # Specifies the name of the NDK library that
   27. # you want CMake to locate.
   28. ace_ndk.z
   29. )

   31. find_library(
   32. # Sets the name of the path variable.
   33. libnapi-lib
   34. # Specifies the name of the NDK library that
   35. # you want CMake to locate.
   36. ace_napi.z
   37. )

   39. find_library(
   40. # Sets the name of the path variable.
   41. libuv-lib
   42. uv
   43. )

   45. target_link_libraries(entry PUBLIC
   46. ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} )
   ```

## 自定义绘制组件

以下示例创建了一个自定义绘制组件，该绘制组件能够绘制自定义矩形，并使用上述自定义容器进行布局排布。

**图2** 自定义绘制组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/dYn2KJ84RteFDuSTGKf8RA/zh-cn_image_0000002589244367.png?HW-CC-KV=V1&HW-CC-Date=20260429T052832Z&HW-CC-Expire=86400&HW-CC-Sign=B3DC45F3113969DF5856ACFB9823E015E37280DD25B8A50AD6108A172A1A3462)

1. 按照[自定义布局容器](ndk-build-custom-components.md#自定义布局容器)章节准备前置工程。
2. 创建自定义绘制组件封装对象。

   ```
   1. // ArkUICustomNode.h
   2. // 自定义绘制组件示例

   4. #ifndef MYAPPLICATION_ARKUICUSTOMNODE_H
   5. #define MYAPPLICATION_ARKUICUSTOMNODE_H

   7. #include <native_drawing/drawing_brush.h>
   8. #include <native_drawing/drawing_canvas.h>
   9. #include <native_drawing/drawing_path.h>

   11. #include "ArkUINode.h"

   13. namespace NativeModule {

   15. class ArkUICustomNode : public ArkUINode {
   16. public:
   17. // 使用自定义组件类型ARKUI_NODE_CUSTOM创建组件。
   18. ArkUICustomNode()
   19. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_CUSTOM))
   20. {
   21. // 注册自定义事件监听器。
   22. nativeModule_->addNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   23. // 声明自定义事件并传递自身作为自定义数据。
   24. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW, 0, this);
   25. }

   27. ~ArkUICustomNode() override
   28. {
   29. // 反注册自定义事件监听器。
   30. nativeModule_->removeNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   31. // 取消声明自定义事件。
   32. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW);
   33. }

   35. void SetRectColor(uint32_t color)
   36. {
   37. color_ = color;
   38. // 自定义绘制属性变更需要主动通知框架。
   39. nativeModule_->markDirty(handle_, NODE_NEED_RENDER);
   40. }

   42. private:
   43. static void OnStaticCustomEvent(ArkUI_NodeCustomEvent *event)
   44. {
   45. // 获取组件实例对象，调用相关实例方法。
   46. auto customNode = reinterpret_cast<ArkUICustomNode *>(OH_ArkUI_NodeCustomEvent_GetUserData(event));
   47. auto type = OH_ArkUI_NodeCustomEvent_GetEventType(event);
   48. switch (type) {
   49. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW:
   50. customNode->OnDraw(event);
   51. break;
   52. default:
   53. break;
   54. }
   55. }

   57. // 自定义绘制逻辑。
   58. void OnDraw(ArkUI_NodeCustomEvent *event)
   59. {
   60. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   61. // 获取图形绘制对象。
   62. auto drawCanvas = reinterpret_cast<OH_Drawing_Canvas *>(OH_ArkUI_DrawContext_GetCanvas(drawContext));
   63. // 获取组件大小。
   64. auto size = OH_ArkUI_DrawContext_GetSize(drawContext);
   65. // 绘制自定义内容。
   66. auto path = OH_Drawing_PathCreate();
   67. const float kQuarter = 0.25f;
   68. const float kThreeQuarters = 0.75f;
   69. OH_Drawing_PathMoveTo(path, size.width * kQuarter, size.height * kQuarter);
   70. OH_Drawing_PathLineTo(path, size.width * kThreeQuarters, size.height * kQuarter);
   71. OH_Drawing_PathLineTo(path, size.width * kThreeQuarters, size.height * kThreeQuarters);
   72. OH_Drawing_PathLineTo(path, size.width * kQuarter, size.height * kThreeQuarters);
   73. OH_Drawing_PathLineTo(path, size.width * kQuarter, size.height * kQuarter);
   74. OH_Drawing_PathClose(path);
   75. auto brush = OH_Drawing_BrushCreate();
   76. OH_Drawing_BrushSetColor(brush, color_);
   77. OH_Drawing_CanvasAttachBrush(drawCanvas, brush);
   78. OH_Drawing_CanvasDrawPath(drawCanvas, path);
   79. // 释放资源
   80. OH_Drawing_BrushDestroy(brush);
   81. OH_Drawing_PathDestroy(path);
   82. }

   84. uint32_t color_ = 0xFFFFE4B5;
   85. };

   87. } // namespace NativeModule

   89. #endif // MYAPPLICATION_ARKUICUSTOMNODE_H
   ```

   [ArkUICustomNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomDrawSample/entry/src/main/cpp/ArkUICustomNode.h#L15-L105)
3. 使用自定义绘制组件和自定义容器创建示例界面。

   ```
   1. #include "NativeEntry.h"

   3. #include "ArkUICustomContainerNode.h"
   4. #include "ArkUICustomNode.h"

   6. #include <arkui/native_node_napi.h>
   7. #include <arkui/native_type.h>
   8. #include <js_native_api.h>
   9. #include "UITimer.h"

   11. namespace NativeModule {
   12. namespace {
   13. napi_env g_env;
   14. } // namespace

   16. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   17. {
   18. size_t argc = 1;
   19. napi_value args[1] = {nullptr};

   21. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   23. // 获取NodeContent
   24. ArkUI_NodeContentHandle contentHandle;
   25. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   26. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   28. // 创建自定义容器和自定义绘制组件。
   29. auto node = std::make_shared<ArkUICustomContainerNode>();
   30. node->SetBackgroundColor(0xFFE0FFFF);
   31. auto customNode = std::make_shared<ArkUICustomNode>();
   32. customNode->SetBackgroundColor(0xFFD3D3D3);
   33. const int width = 150;
   34. const int height = 150;
   35. customNode->SetWidth(width);
   36. customNode->SetHeight(height);
   37. node->AddChild(customNode);
   38. auto onClick = [](ArkUI_NodeEvent *event) {
   39. auto customNode = (ArkUICustomNode *)OH_ArkUI_NodeEvent_GetUserData(event);
   40. customNode->SetRectColor(0xFF00FF7F);
   41. };
   42. customNode->RegisterOnClick(onClick, customNode.get());

   44. // 保持Native侧对象到管理类中，维护生命周期。
   45. NativeEntry::GetInstance()->SetRootNode(node);
   46. g_env = env;
   47. return nullptr;
   48. }

   50. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   51. {
   52. // 从管理类中释放Native侧对象。
   53. NativeEntry::GetInstance()->DisposeRootNode();
   54. return nullptr;
   55. }

   57. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/CustomDrawSample/entry/src/main/cpp/NativeEntry.cpp#L15-L74)
4. 修改CMakeLists.txt，添加链接库。

   ```
   1. # CMakeLists.txt

   3. # the minimum version of CMake.
   4. cmake_minimum_required(VERSION 3.4.1)
   5. project(testndk)

   7. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   9. include_directories(${NATIVERENDER_ROOT_PATH}
   10. ${NATIVERENDER_ROOT_PATH}/include)

   12. add_library(entry SHARED NativeEntry.cpp napi_init.cpp)
   13. # target_link_libraries(entry PUBLIC libace_napi.z.so, libace_ndk.z.so, libhilog_ndk.z.so)

   15. find_library(
   16. # Sets the name of the path variable.
   17. hilog-lib
   18. # Specifies the name of the NDK library that
   19. # you want CMake to locate.
   20. hilog_ndk.z
   21. )

   23. find_library(
   24. # Sets the name of the path variable.
   25. libace-lib
   26. # Specifies the name of the NDK library that
   27. # you want CMake to locate.
   28. ace_ndk.z
   29. )

   31. find_library(
   32. # Sets the name of the path variable.
   33. libnapi-lib
   34. # Specifies the name of the NDK library that
   35. # you want CMake to locate.
   36. ace_napi.z
   37. )

   39. find_library(
   40. # Sets the name of the path variable.
   41. libuv-lib
   42. uv
   43. )

   45. target_link_libraries(entry PUBLIC
   46. ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative_drawing.so)
   ```

## 不规则网格布局示例

以下示例创建了一个不规则网格布局容器，支持不同大小的网格单元，实现类似瀑布流的布局效果。完整示例请参考[CustomDrawIrregularSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/CustomDrawIrregularSample)。

**图3** 不规则网格布局效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/c7sdsolTT76ho8fvRF6nPQ/zh-cn_image_0000002558764560.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052832Z&HW-CC-Expire=86400&HW-CC-Sign=C4626E5B300C11BF1E19EEEB94058D80C8D3DC53442FD4D5A5D3A833664A6E12)

1. 按照[自定义布局容器](ndk-build-custom-components.md#自定义布局容器)章节准备前置工程。
2. 创建不规则网格布局容器组件封装对象。

   ```
   1. // ArkUIIrregularGridNode.h
   2. // 不规则网格布局容器示例

   4. #ifndef MYAPPLICATION_ARKUIIRREGULARGRIDNODE_H
   5. #define MYAPPLICATION_ARKUIIRREGULARGRIDNODE_H

   7. #include "ArkUINode.h"
   8. #include <vector>
   9. #include <map>

   11. namespace NativeModule {

   13. // 网格单元配置
   14. struct GridItemConfig {
   15. int32_t rowSpan = 1;    // 占据的行数
   16. int32_t columnSpan = 1; // 占据的列数
   17. };

   19. class ArkUIIrregularGridNode : public ArkUINode {
   20. public:
   21. // 使用自定义组件类型ARKUI_NODE_CUSTOM创建组件
   22. ArkUIIrregularGridNode()
   23. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_CUSTOM))
   24. {
   25. // 注册自定义事件监听器
   26. nativeModule_->addNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   27. // 声明自定义事件并传递自身作为自定义数据
   28. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE, 0, this);
   29. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT, 0, this);
   30. }

   32. ~ArkUIIrregularGridNode() override
   33. {
   34. // 反注册自定义事件监听器
   35. nativeModule_->removeNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   36. // 取消声明自定义事件
   37. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE);
   38. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT);
   39. }

   41. // 设置列数
   42. void SetColumnCount(int32_t count)
   43. {
   44. columnCount_ = count;
   45. nativeModule_->markDirty(handle_, NODE_NEED_MEASURE);
   46. }

   48. // 设置网格间距
   49. void SetGap(int32_t gap)
   50. {
   51. gap_ = gap;
   52. nativeModule_->markDirty(handle_, NODE_NEED_MEASURE);
   53. }

   55. // 设置子组件的网格配置
   56. void SetItemConfig(ArkUI_NodeHandle child, int32_t rowSpan, int32_t columnSpan)
   57. {
   58. GridItemConfig config;
   59. config.rowSpan = rowSpan;
   60. config.columnSpan = columnSpan;
   61. itemConfigs_[child] = config;
   62. nativeModule_->markDirty(handle_, NODE_NEED_MEASURE);
   63. }

   65. private:
   66. static void OnStaticCustomEvent(ArkUI_NodeCustomEvent *event)
   67. {
   68. // 获取组件实例对象，调用相关实例方法
   69. auto customNode = reinterpret_cast<ArkUIIrregularGridNode *>(OH_ArkUI_NodeCustomEvent_GetUserData(event));
   70. auto type = OH_ArkUI_NodeCustomEvent_GetEventType(event);
   71. switch (type) {
   72. case ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE:
   73. customNode->OnMeasure(event);
   74. break;
   75. case ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT:
   76. customNode->OnLayout(event);
   77. break;
   78. default:
   79. break;
   80. }
   81. }

   83. // 测算单个子组件并更新列高信息
   84. void MeasureChild(ArkUI_NodeHandle child, int32_t cellWidth,
   85. ArkUI_LayoutConstraint *childConstraint, std::vector<int32_t> &columnHeights)
   86. {
   87. GridItemConfig config = {1, 1};
   88. auto it = itemConfigs_.find(child);
   89. if (it != itemConfigs_.end()) {
   90. config = it->second;
   91. }
   92. if (config.columnSpan > columnCount_) {
   93. config.columnSpan = columnCount_;
   94. }

   96. int32_t startColumn = FindLowestColumn(columnHeights, config.columnSpan);
   97. int32_t startY = 0;
   98. for (int32_t col = startColumn; col < startColumn + config.columnSpan && col < columnCount_; col++) {
   99. if (columnHeights[col] > startY) {
   100. startY = columnHeights[col];
   101. }
   102. }

   104. int32_t itemWidth = cellWidth * config.columnSpan + gap_ * (config.columnSpan - 1);
   105. OH_ArkUI_LayoutConstraint_SetMaxWidth(childConstraint, itemWidth);
   106. OH_ArkUI_LayoutConstraint_SetMinWidth(childConstraint, itemWidth);
   107. nativeModule_->measureNode(child, childConstraint);
   108. auto size = nativeModule_->getMeasuredSize(child);

   110. LayoutItemInfo info;
   111. info.x = startColumn * (cellWidth + gap_);
   112. info.y = startY;
   113. info.width = size.width;
   114. info.height = size.height;
   115. layoutInfo_.push_back(info);

   117. int32_t newHeight = startY + size.height + gap_;
   118. for (int32_t col = startColumn; col < startColumn + config.columnSpan && col < columnCount_; col++) {
   119. columnHeights[col] = newHeight;
   120. }
   121. }

   123. // 自定义测算逻辑：不规则网格布局
   124. void OnMeasure(ArkUI_NodeCustomEvent *event)
   125. {
   126. auto layoutConstrain = OH_ArkUI_NodeCustomEvent_GetLayoutConstraintInMeasure(event);
   127. int32_t maxWidth = OH_ArkUI_LayoutConstraint_GetMaxWidth(layoutConstrain);

   129. int32_t totalGap = gap_ * (columnCount_ - 1);
   130. int32_t cellWidth = (maxWidth - totalGap) / columnCount_;

   132. auto childConstraint = OH_ArkUI_LayoutConstraint_Copy(layoutConstrain);
   133. std::vector<int32_t> columnHeights(columnCount_, 0);
   134. layoutInfo_.clear();

   136. auto totalSize = nativeModule_->getTotalChildCount(handle_);
   137. for (uint32_t i = 0; i < totalSize; i++) {
   138. auto child = nativeModule_->getChildAt(handle_, i);
   139. MeasureChild(child, cellWidth, childConstraint, columnHeights);
   140. }

   142. int32_t maxHeight = 0;
   143. for (int32_t height : columnHeights) {
   144. if (height > maxHeight) {
   145. maxHeight = height;
   146. }
   147. }
   148. if (maxHeight > gap_) {
   149. maxHeight -= gap_;
   150. }

   152. nativeModule_->setMeasuredSize(handle_, maxWidth, maxHeight);
   153. OH_ArkUI_LayoutConstraint_Dispose(childConstraint);
   154. }

   156. void OnLayout(ArkUI_NodeCustomEvent *event)
   157. {
   158. // 获取父组件期望位置并设置
   159. auto position = OH_ArkUI_NodeCustomEvent_GetPositionInLayout(event);
   160. nativeModule_->setLayoutPosition(handle_, position.x, position.y);

   162. // 布局子组件
   163. auto totalSize = nativeModule_->getTotalChildCount(handle_);
   164. for (uint32_t i = 0; i < totalSize && i < layoutInfo_.size(); i++) {
   165. auto child = nativeModule_->getChildAt(handle_, i);
   166. nativeModule_->layoutNode(child, layoutInfo_[i].x, layoutInfo_[i].y);
   167. }
   168. }

   170. // 找到最矮的列，确保可以放下指定列跨度的项
   171. int32_t FindLowestColumn(const std::vector<int32_t>& columnHeights, int32_t columnSpan)
   172. {
   173. int32_t lowestColumn = 0;
   174. int32_t lowestHeight = INT32_MAX;

   176. // 遍历所有可能的起始列
   177. for (int32_t col = 0; col <= columnCount_ - columnSpan; col++) {
   178. // 找到这个范围内最高的列
   179. int32_t maxHeightInRange = 0;
   180. for (int32_t i = col; i < col + columnSpan; i++) {
   181. if (columnHeights[i] > maxHeightInRange) {
   182. maxHeightInRange = columnHeights[i];
   183. }
   184. }

   186. // 如果这个范围的最高点比当前最低点还低，更新最低列
   187. if (maxHeightInRange < lowestHeight) {
   188. lowestHeight = maxHeightInRange;
   189. lowestColumn = col;
   190. }
   191. }

   193. return lowestColumn;
   194. }

   196. struct LayoutItemInfo {
   197. int32_t x;
   198. int32_t y;
   199. int32_t width;
   200. int32_t height;
   201. };

   203. int32_t columnCount_ = 3;
   204. int32_t gap_ = 10;
   205. std::map<ArkUI_NodeHandle, GridItemConfig> itemConfigs_;
   206. std::vector<LayoutItemInfo> layoutInfo_;
   207. };

   209. } // namespace NativeModule

   211. #endif // MYAPPLICATION_ARKUIIRREGULARGRIDNODE_H
   ```
3. 使用不规则网格布局容器创建示例界面。

   ```
   1. #include "NativeEntry.h"

   3. #include "ArkUIIrregularGridNode.h"
   4. #include "ArkUINode.h"

   6. #include <arkui/native_node_napi.h>
   7. #include <arkui/native_type.h>
   8. #include <js_native_api.h>
   9. #include <utility>
   10. #include <vector>

   12. namespace NativeModule {
   13. namespace {
   14. napi_env g_env = nullptr;

   16. constexpr uint32_t GRID_BACKGROUND_COLOR = 0xFFF5F5F5;
   17. constexpr int32_t GRID_COLUMN_COUNT = 4;
   18. constexpr int32_t GRID_GAP = 8;
   19. constexpr float GRID_ITEM_RADIUS = 8.0f;
   20. constexpr float GRID_ITEM_BORDER_WIDTH = 1.0f;
   21. constexpr uint32_t GRID_ITEM_BORDER_COLOR = 0xFFCCCCCC;
   22. constexpr float GRID_ITEM_BASE_HEIGHT = 60.0f;
   23. constexpr float GRID_ITEM_HEIGHT_STEP = 40.0f;

   25. using GridItemSize = std::pair<int32_t, int32_t>;

   27. const std::vector<GridItemSize>& GetGridItemSizes()
   28. {
   29. static const std::vector<GridItemSize> itemSizes = {
   30. {1, 1}, // 小方块
   31. {2, 1}, // 竖长条
   32. {1, 3}, // 横长条
   33. {2, 2}, // 大方块
   34. {1, 1}, // 小方块
   35. {1, 2}, // 横条
   36. {3, 1}, // 很长的竖条
   37. };
   38. return itemSizes;
   39. }

   41. const std::vector<uint32_t>& GetGridItemColors()
   42. {
   43. static const std::vector<uint32_t> colors = {
   44. 0xFF64B5F6, // 蓝色
   45. 0xFFE57373, // 红色
   46. 0xFF81C784, // 绿色
   47. 0xFFFFB74D, // 橙色
   48. 0xFF9575CD, // 紫色
   49. 0xFF4DB6AC, // 青色
   50. 0xFFFFD54F, // 黄色
   51. 0xFFF06292, // 粉色
   52. 0xFF7986CB, // 靛蓝
   53. 0xFFA1887F, // 棕色
   54. };
   55. return colors;
   56. }

   58. void SetNodeColorAttribute(ArkUI_NativeNodeAPI_1* nodeAPI, ArkUI_NodeHandle node, uint32_t color)
   59. {
   60. ArkUI_NumberValue bgColor[] = {{.u32 = color}};
   61. ArkUI_AttributeItem bgColorItem = {bgColor, 1};
   62. nodeAPI->setAttribute(node, NODE_BACKGROUND_COLOR, &bgColorItem);
   63. }

   65. void SetNodeBorderRadiusAttribute(ArkUI_NativeNodeAPI_1* nodeAPI, ArkUI_NodeHandle node, float radius)
   66. {
   67. ArkUI_NumberValue radiusValue[] = {{.f32 = radius}};
   68. ArkUI_AttributeItem radiusItem = {radiusValue, 1};
   69. nodeAPI->setAttribute(node, NODE_BORDER_RADIUS, &radiusItem);
   70. }

   72. void SetNodeBorderStyle(ArkUI_NativeNodeAPI_1* nodeAPI, ArkUI_NodeHandle node)
   73. {
   74. ArkUI_NumberValue borderWidth[] = {{.f32 = GRID_ITEM_BORDER_WIDTH}};
   75. ArkUI_AttributeItem borderWidthItem = {borderWidth, 1};
   76. nodeAPI->setAttribute(node, NODE_BORDER_WIDTH, &borderWidthItem);

   78. ArkUI_NumberValue borderColor[] = {{.u32 = GRID_ITEM_BORDER_COLOR}};
   79. ArkUI_AttributeItem borderColorItem = {borderColor, 1};
   80. nodeAPI->setAttribute(node, NODE_BORDER_COLOR, &borderColorItem);
   81. }

   83. void SetNodeHeightByRowSpan(ArkUI_NativeNodeAPI_1* nodeAPI, ArkUI_NodeHandle node, int32_t rowSpan)
   84. {
   85. float minHeight = GRID_ITEM_BASE_HEIGHT + (rowSpan - 1) * GRID_ITEM_HEIGHT_STEP;
   86. ArkUI_NumberValue minHeightValue[] = {{.f32 = minHeight}};
   87. ArkUI_AttributeItem minHeightItem = {minHeightValue, 1};
   88. nodeAPI->setAttribute(node, NODE_HEIGHT, &minHeightItem);
   89. }

   91. void AddGridItems(
   92. ArkUI_NativeNodeAPI_1* nodeAPI,
   93. const std::shared_ptr<ArkUIIrregularGridNode>& gridNode,
   94. const std::vector<GridItemSize>& itemSizes,
   95. const std::vector<uint32_t>& colors)
   96. {
   97. for (size_t i = 0; i < itemSizes.size(); ++i) {
   98. auto itemNode = nodeAPI->createNode(ARKUI_NODE_STACK);
   99. SetNodeColorAttribute(nodeAPI, itemNode, colors[i % colors.size()]);
   100. SetNodeBorderRadiusAttribute(nodeAPI, itemNode, GRID_ITEM_RADIUS);
   101. SetNodeBorderStyle(nodeAPI, itemNode);
   102. SetNodeHeightByRowSpan(nodeAPI, itemNode, itemSizes[i].first);
   103. gridNode->SetItemConfig(itemNode, itemSizes[i].first, itemSizes[i].second);
   104. nodeAPI->addChild(gridNode->GetHandle(), itemNode);
   105. }
   106. }
   107. } // namespace

   109. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   110. {
   111. size_t argc = 1;
   112. napi_value args[1] = {nullptr};
   113. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   115. ArkUI_NodeContentHandle contentHandle;
   116. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   117. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   119. auto gridNode = std::make_shared<ArkUIIrregularGridNode>();
   120. gridNode->SetBackgroundColor(GRID_BACKGROUND_COLOR);
   121. gridNode->SetColumnCount(GRID_COLUMN_COUNT);
   122. gridNode->SetGap(GRID_GAP);

   124. auto* nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
   125. AddGridItems(nodeAPI, gridNode, GetGridItemSizes(), GetGridItemColors());

   127. // 保持Native侧对象到管理类中，维护生命周期
   128. NativeEntry::GetInstance()->SetRootNode(gridNode);
   129. g_env = env;
   130. return nullptr;
   131. }

   133. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   134. {
   135. // 从管理类中释放Native侧对象
   136. NativeEntry::GetInstance()->DisposeRootNode();
   137. return nullptr;
   138. }

   140. } // namespace NativeModule
   ```
