---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-draw
title: 自定义绘制
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 自定义绘制
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e5fef5dc07c9b39863abb287d2cc37c7076b9c7d08d7e003d84b64c3b7597304
---

## 概述

当某些组件本身的绘制内容不满足需求时，可使用组件自定义绘制功能，在原有组件基础上部分绘制、或者全部自行绘制，以达到预期效果。例如：独特的按钮形状、文字和图像混合的图标等。NDK提供了自定义绘制节点的能力，通过自定义绘制事件，开发者可以实现基于NDK侧[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)中ARKUI\_NODE\_CUSTOM类型节点的自绘制能力。

说明

* ArkTS的自定义绘制能力和示例请参考[自定义绘制修改器 (DrawModifier)](arkts-user-defined-extension-drawmodifier.md)。

## 自定义绘制层级

自定义绘制提供了五个绘制层级，从低到高依次为：内容背景层（drawBehind）、内容层（drawContent）、内容前景层（drawFront）、前景层（drawForeground）和浮层（drawOverlay）。开发者可以根据需求选择合适的层级进行绘制。自定义绘制层级图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Yg5dQocZQba_Q7joLum3lg/zh-cn_image_0000002552798376.png?HW-CC-KV=V1&HW-CC-Date=20260427T234017Z&HW-CC-Expire=86400&HW-CC-Sign=12EBF4B6BD857BA9ECBB145ED16F090B194D2C0AD7364B610F45792080517999)

开发者可以通过注册相应的事件类型来实现不同层级的自定义绘制，不同层级对应的枚举如下，NDK接口支持的事件类型范围请参考[ArkUI\_NodeCustomEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodecustomeventtype)枚举值。

| 事件类型 | 说明 |
| --- | --- |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND | 自定义内容背景层绘制类型，从API version 20开始支持。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW | 自定义内容层绘制类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT | 自定义内容前景层绘制类型，从API version 20开始支持。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_FOREGROUND\_DRAW | 自定义前景层绘制类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_OVERLAY\_DRAW | 自定义浮层绘制类型。 |

### 内容层自定义绘制示例

本示例通过注册内容层绘制事件ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW在节点内容层绘制一条从左上区域到右下区域的对角线段，效果图如下。

以下场景基于[接入ArkTS页面](ndk-access-the-arkts-page.md)章节，创建前置工程。内容绘制的完整示例请参考[NativeDrawPageSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/NativeDrawPageSample)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/SL2LSAAWSPKSUBNvbs2thQ/zh-cn_image_0000002552958070.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234017Z&HW-CC-Expire=86400&HW-CC-Sign=F9AA716401B49C2C37B36594CEE21146A23F7640872FD59B48B38288EFDB9575)

1. 通过[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)的[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口，传入[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodecustomeventtype)中的ARKUI\_NODE\_CUSTOM枚举值创建自定义节点。

   ```
   1. auto customNode = nodeAPI->createNode(ARKUI_NODE_CUSTOM);
   ```

   [Drawing.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NativeDrawPageSample/entry/src/main/cpp/Drawing.h#L39-L41)
2. 事件注册时将自定义节点、事件类型、事件ID和UserData作为参数传入。

   ```
   1. // UserData
   2. struct A {
   3. int32_t a = 6;
   4. bool flag = true;
   5. ArkUI_NodeHandle node;
   6. };
   7. A *a = new A;
   8. a->node = customNode;
   9. // ...
   10. nodeAPI->registerNodeCustomEvent(customNode, ARKUI_NODE_CUSTOM_EVENT_ON_FOREGROUND_DRAW, 1, a);
   11. // 事件回调函数的编写
   12. nodeAPI->registerNodeCustomEventReceiver([](ArkUI_NodeCustomEvent *event) {
   13. // 事件回调函数逻辑
   14. // ...
   15. });
   ```

   [Drawing.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NativeDrawPageSample/entry/src/main/cpp/Drawing.h#L54-L108)
3. 在回调函数中，通过[OH\_ArkUI\_NodeCustomEvent\_GetEventType](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecustomevent_geteventtype)获取自定义事件的事件类型，通过[OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecustomevent_geteventtargetid)获取事件ID，通过[OH\_ArkUI\_NodeCustomEvent\_GetUserData](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecustomevent_getuserdata)获取UserData，再根据事件类型和事件ID判断当前触发的是哪个绘制事件，从而执行对应的逻辑。

   ```
   1. auto type = OH_ArkUI_NodeCustomEvent_GetEventType(event);
   2. auto targetId = OH_ArkUI_NodeCustomEvent_GetEventTargetId(event);
   3. auto userData = reinterpret_cast<A *>(OH_ArkUI_NodeCustomEvent_GetUserData(event));
   ```

   [Drawing.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NativeDrawPageSample/entry/src/main/cpp/Drawing.h#L81-L79)
4. [OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodecustomevent_getdrawcontextindraw)通过自定义组件事件获取绘制上下文，并将其传入[OH\_ArkUI\_DrawContext\_GetCanvas](../harmonyos-references/capi-native-type-h.md#oh_arkui_drawcontext_getcanvas)以获取Canvas画布指针，该指针随后将转换为[OH\_Drawing\_Canvas](../harmonyos-references/capi-drawing-oh-drawing-canvas.md)指针进行绘制。

   ```
   1. // 获取自定义事件绘制的上下文。
   2. auto *drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   3. // 获取Canvas指针。
   4. auto *canvas1 = OH_ArkUI_DrawContext_GetCanvas(drawContext);
   5. // 转换为OH_Drawing_Canvas指针进行绘制。
   6. OH_Drawing_Canvas *canvas = reinterpret_cast<OH_Drawing_Canvas *>(canvas1);
   7. // 绘制逻辑。
   8. int32_t width = SIZE_1000;  // SIZE_1000 = 1000
   9. int32_t height = SIZE_1000; // SIZE_1000 = 1000
   10. auto path = OH_Drawing_PathCreate();
   11. OH_Drawing_PathMoveTo(path, width / SIZE_4, height / SIZE_4);                   // SIZE_4 = 4
   12. OH_Drawing_PathLineTo(path, width * SIZE_3 / SIZE_4, height * SIZE_3 / SIZE_4); // SIZE_3 = 3,SIZE_4 = 4
   13. OH_Drawing_PathClose(path);
   14. auto pen = OH_Drawing_PenCreate();
   15. OH_Drawing_PenSetWidth(pen, SIZE_10); // SIZE_10 = 10
   16. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x4A, 0x4F));
   17. OH_Drawing_CanvasAttachPen(canvas, pen);
   18. OH_Drawing_CanvasDrawPath(canvas, path);
   ```

   [Drawing.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NativeDrawPageSample/entry/src/main/cpp/Drawing.h#L82-L79)

### 多层级绘制示例

以下示例创建了一个自定义绘制组件，实现自定义矩形绘制、自定义绘制内容前景层和内容背景层，并支持使用[自定义布局容器](ndk-build-custom-components.md#自定义布局容器)进行布局排布。完整示例请参考[NativeNodeUtilsSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/NativeNodeUtilsSample)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/NO0yNSQwS7e7pZS4JGYiJQ/zh-cn_image_0000002583478071.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234017Z&HW-CC-Expire=86400&HW-CC-Sign=3C454FAD63AB72EFC83F0A544AAE2A19E00884FABDED9C863EA686E5AADCB364)

图中深蓝矩形为drawFront内容前景层，浅蓝色矩形为drawContent内容层，白色矩形为drawBehind内容背景层。三层的叠加关系用于验证多层级绘制顺序是否符合预期。

1. 按照[自定义布局容器](ndk-build-custom-components.md#自定义布局容器)章节准备前置工程。
2. 创建自定义绘制组件封装对象。

   ```
   1. #ifndef MYAPPLICATION_ARKUICUSTOMNODE_H
   2. #define MYAPPLICATION_ARKUICUSTOMNODE_H

   4. #include <native_drawing/drawing_brush.h>
   5. #include <native_drawing/drawing_canvas.h>
   6. #include <native_drawing/drawing_path.h>

   8. #include "ArkUINode.h"

   10. namespace NativeModule {
   11. class ArkUICustomNode : public ArkUINode {
   12. public:
   13. // 使用自定义组件类型ARKUI_NODE_CUSTOM创建组件。
   14. ArkUICustomNode()
   15. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_CUSTOM))
   16. {
   17. // 注册自定义事件监听器。
   18. nativeModule_->addNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   19. // 声明自定义事件并转递自身作为自定义数据。
   20. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT, 0, this);
   21. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW, 0, this);
   22. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND, 0, this);
   23. // 绘制完成事件通知。
   24. OH_ArkUI_RegisterDrawCallbackOnNodeHandle(handle_, nullptr, [](void* userData) {});
   25. }

   27. ~ArkUICustomNode() override
   28. {
   29. // 反注册自定义事件监听器。
   30. nativeModule_->removeNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   31. // 取消声明自定义事件。
   32. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT);
   33. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW);
   34. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND);
   35. OH_ArkUI_UnregisterDrawCallbackOnNodeHandle(handle_);
   36. }

   38. private:
   39. int32_t NUM_2 = 2;
   40. int32_t NUM_3 = 3;
   41. int32_t NUM_4 = 4;
   42. int32_t NUM_5 = 5;
   43. static void OnStaticCustomEvent(ArkUI_NodeCustomEvent *event)
   44. {
   45. // 获取组件实例对象，调用相关实例方法。
   46. // ...
   47. auto customNode = reinterpret_cast<ArkUICustomNode *>(OH_ArkUI_NodeCustomEvent_GetUserData(event));
   48. auto type = OH_ArkUI_NodeCustomEvent_GetEventType(event);
   49. switch (type) {
   50. // 绘制层级由低到高。
   51. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND:
   52. customNode->OnDrawBehind(event);
   53. break;
   54. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW:
   55. customNode->OnDraw(event);
   56. break;
   57. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT:
   58. customNode->OnDrawFront(event);
   59. break;
   60. // ...
   61. default:
   62. break;
   63. }
   64. }

   66. // 自定义绘制逻辑。
   67. void OnDrawBehind(ArkUI_NodeCustomEvent *event)
   68. {
   69. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   70. // 获取图形绘制对象。
   71. auto drawCanvas = reinterpret_cast<OH_Drawing_Canvas *>(OH_ArkUI_DrawContext_GetCanvas(drawContext));
   72. // 获取组件大小。
   73. auto size = OH_ArkUI_DrawContext_GetSize(drawContext);
   74. // 绘制自定义内容。
   75. auto path = OH_Drawing_PathCreate();
   76. OH_Drawing_PathMoveTo(path, size.width / NUM_5, size.height / NUM_5);
   77. OH_Drawing_PathLineTo(path, size.width * NUM_4 / NUM_5, size.height / NUM_5);
   78. OH_Drawing_PathLineTo(path, size.width * NUM_4 / NUM_5, size.height * NUM_4 / NUM_5);
   79. OH_Drawing_PathLineTo(path, size.width / NUM_5, size.height * NUM_4 / NUM_5);
   80. OH_Drawing_PathLineTo(path, size.width / NUM_5, size.height / NUM_5);
   81. OH_Drawing_PathClose(path);
   82. auto brush = OH_Drawing_BrushCreate();
   83. OH_Drawing_BrushSetColor(brush, 0xFFF0FAFF); // 蓝白色
   84. OH_Drawing_CanvasAttachBrush(drawCanvas, brush);
   85. OH_Drawing_CanvasDrawPath(drawCanvas, path);
   86. // 释放资源
   87. OH_Drawing_BrushDestroy(brush);
   88. OH_Drawing_PathDestroy(path);
   89. }

   91. void OnDraw(ArkUI_NodeCustomEvent *event)
   92. {
   93. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   94. // 获取图形绘制对象。
   95. auto drawCanvas = reinterpret_cast<OH_Drawing_Canvas *>(OH_ArkUI_DrawContext_GetCanvas(drawContext));
   96. // 获取组件大小。
   97. auto size = OH_ArkUI_DrawContext_GetSize(drawContext);
   98. // 绘制自定义内容。
   99. auto path = OH_Drawing_PathCreate();
   100. OH_Drawing_PathMoveTo(path, size.width / NUM_4, size.height / NUM_4);
   101. OH_Drawing_PathLineTo(path, size.width * NUM_3 / NUM_4, size.height / NUM_4);
   102. OH_Drawing_PathLineTo(path, size.width * NUM_3 / NUM_4, size.height * NUM_3 / NUM_4);
   103. OH_Drawing_PathLineTo(path, size.width / NUM_4, size.height * NUM_3 / NUM_4);
   104. OH_Drawing_PathLineTo(path, size.width / NUM_4, size.height / NUM_4);
   105. OH_Drawing_PathClose(path);
   106. auto brush = OH_Drawing_BrushCreate();
   107. OH_Drawing_BrushSetColor(brush, 0xff2787D9); // 浅蓝色
   108. OH_Drawing_CanvasAttachBrush(drawCanvas, brush);
   109. OH_Drawing_CanvasDrawPath(drawCanvas, path);
   110. // 释放资源
   111. OH_Drawing_BrushDestroy(brush);
   112. OH_Drawing_PathDestroy(path);
   113. }

   115. void OnDrawFront(ArkUI_NodeCustomEvent *event)
   116. {
   117. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   118. // 获取图形绘制对象。
   119. auto drawCanvas = reinterpret_cast<OH_Drawing_Canvas *>(OH_ArkUI_DrawContext_GetCanvas(drawContext));
   120. // 获取组件大小。
   121. auto size = OH_ArkUI_DrawContext_GetSize(drawContext);
   122. // 绘制自定义内容。
   123. auto path = OH_Drawing_PathCreate();
   124. OH_Drawing_PathMoveTo(path, size.width / NUM_3, size.height / NUM_3);
   125. OH_Drawing_PathLineTo(path, size.width * NUM_2 / NUM_3, size.height / NUM_3);
   126. OH_Drawing_PathLineTo(path, size.width * NUM_2 / NUM_3, size.height * NUM_2 / NUM_3);
   127. OH_Drawing_PathLineTo(path, size.width / NUM_3, size.height * NUM_2 / NUM_3);
   128. OH_Drawing_PathLineTo(path, size.width / NUM_3, size.height / NUM_3);
   129. OH_Drawing_PathClose(path);
   130. auto brush = OH_Drawing_BrushCreate();
   131. OH_Drawing_BrushSetColor(brush, 0xFF004AAF); // 深蓝色
   132. OH_Drawing_CanvasAttachBrush(drawCanvas, brush);
   133. OH_Drawing_CanvasDrawPath(drawCanvas, path);
   134. // 释放资源
   135. OH_Drawing_BrushDestroy(brush);
   136. OH_Drawing_PathDestroy(path);
   137. }
   138. // ...
   139. };

   141. } // namespace NativeModule

   143. #endif // MYAPPLICATION_ARKUICUSTOMNODE_H
   ```

   [ArkUICustomNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NativeNodeUtilsSample/entry/src/main/cpp/ArkUICustomNode.h#L17-L219)
3. 使用自定义绘制组件和自定义容器创建示例界面。

   ```
   1. #include <arkui/native_node_napi.h>
   2. #include <arkui/native_type.h>
   3. #include <js_native_api.h>

   5. #include "NativeEntry.h"
   6. #include "ArkUICustomContainerNode.h"
   7. #include "ArkUICustomNode.h"
   8. #include "ArkUIMessageMaskNode.h"

   10. // 全局环境变量声明
   11. static napi_env g_env = nullptr;
   12. // ...
   13. namespace NativeModule {
   14. // ...
   15. #define SIZE_150 150
   16. // ...
   17. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   18. {
   19. size_t argc = 1;
   20. napi_value args[1] = {nullptr};

   22. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   24. // 获取NodeContent。
   25. ArkUI_NodeContentHandle contentHandle;
   26. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   27. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   29. // 创建自定义容器和自定义绘制组件。
   30. auto node = std::make_shared<ArkUICustomContainerNode>();
   31. node->SetBackgroundColor(0xFFD5D5D5); // 浅灰色。
   32. auto customNode = std::make_shared<ArkUICustomNode>();
   33. customNode->SetBackgroundColor(0xFF707070); // 深灰色。
   34. customNode->SetWidth(SIZE_150);
   35. customNode->SetHeight(SIZE_150);
   36. node->AddChild(customNode);

   38. // 保持Native侧对象到管理类中，维护生命周期。
   39. NativeEntry::GetInstance()->SetRootNode(node);
   40. g_env = env;
   41. return nullptr;
   42. }

   44. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   45. {
   46. // 从管理类中释放Native侧对象。
   47. NativeEntry::GetInstance()->DisposeRootNode();
   48. return nullptr;
   49. }
   50. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NativeNodeUtilsSample/entry/src/main/cpp/NativeEntry.cpp#L28-L668)

## 通过前景绘制实现消息蒙层

以下示例创建了一个消息提示组件，通过内容层绘制消息气泡与文本，并在前景层叠加星标装饰，实现消息高亮提示效果，常用于消息提醒和引导标记等场景。完整示例请参考[NativeNodeUtilsSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/NativeNodeUtilsSample)。

未添加消息蒙层，未添加蒙层，没有前景层叠加星标装饰效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/47m3ZcJGTyGkNQuJLS46gQ/zh-cn_image_0000002552798422.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234017Z&HW-CC-Expire=86400&HW-CC-Sign=485E96BBE9D6EC0707148CEB871515490ACA9C01E618A9F136E08F0774096C47)

添加消息蒙层，添加后有前景层叠加星标装饰效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/jjRwsEJVS8KfvYh6Yk6NkQ/zh-cn_image_0000002583438117.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234017Z&HW-CC-Expire=86400&HW-CC-Sign=DC2D71EEECB6A623C9C489C709D91FB40BCD71BBBF99C6095926474A79E06F1E)

1. 按照[多层级绘制示例](arkts-user-defined-draw.md#多层级绘制示例)章节准备前置工程。
2. 创建消息蒙层组件封装对象。

   ```
   1. #ifndef MYAPPLICATION_ARKUIMESSAGEMASKNODE_H
   2. #define MYAPPLICATION_ARKUIMESSAGEMASKNODE_H

   4. #include <cmath>
   5. #include <native_drawing/drawing_brush.h>
   6. #include <native_drawing/drawing_canvas.h>
   7. #include <native_drawing/drawing_color_filter.h>
   8. #include <native_drawing/drawing_font.h>
   9. #include <native_drawing/drawing_font_collection.h>
   10. #include <native_drawing/drawing_path.h>
   11. #include <native_drawing/drawing_pen.h>
   12. #include <native_drawing/drawing_point.h>
   13. #include <native_drawing/drawing_rect.h>
   14. #include <native_drawing/drawing_round_rect.h>
   15. #include <native_drawing/drawing_text_typography.h>

   17. #include <string>

   19. #include "ArkUINode.h"

   21. namespace NativeModule {
   22. class ArkUIMessageMaskNode : public ArkUINode {
   23. public:
   24. // 使用自定义组件类型ARKUI_NODE_CUSTOM创建组件
   25. ArkUIMessageMaskNode()
   26. : ArkUINode(
   27. (NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_CUSTOM))
   28. {
   29. // 注册自定义事件监听器
   30. nativeModule_->addNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   31. // 声明自定义事件并转递自身作为自定义数据
   32. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT, 0, this);
   33. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW, 0, this);
   34. nativeModule_->registerNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND, 0, this);
   35. }

   37. ~ArkUIMessageMaskNode() override
   38. {
   39. // 反注册自定义事件监听器
   40. nativeModule_->removeNodeCustomEventReceiver(handle_, OnStaticCustomEvent);
   41. // 取消声明自定义事件
   42. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT);
   43. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW);
   44. nativeModule_->unregisterNodeCustomEvent(handle_, ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND);
   45. }

   47. // 设置消息文本
   48. void SetMessage(const std::string& message)
   49. {
   50. message_ = message;
   51. nativeModule_->markDirty(handle_, NODE_NEED_RENDER);
   52. }

   54. // 设置是否显示蒙层
   55. void SetMaskVisible(bool visible)
   56. {
   57. maskVisible_ = visible;
   58. nativeModule_->markDirty(handle_, NODE_NEED_RENDER);
   59. }

   61. private:
   62. static constexpr int starDecorationCount = 3;
   63. static constexpr int starPointCount = 5;
   64. static constexpr float starStartAngleDegrees = -90.0f;
   65. static constexpr float starAngleStepDegrees = 72.0f;
   66. static constexpr float starInnerAngleOffsetDegrees = 36.0f;
   67. static constexpr float starInnerRadiusRatio = 0.4f;
   68. static constexpr float degreeToRadian = 3.14159265f / 180.0f;
   69. static constexpr float messageTextFontSize = 23.0f;

   71. static void OnStaticCustomEvent(ArkUI_NodeCustomEvent* event)
   72. {
   73. auto customNode = reinterpret_cast<ArkUIMessageMaskNode*>(OH_ArkUI_NodeCustomEvent_GetUserData(event));
   74. auto type = OH_ArkUI_NodeCustomEvent_GetEventType(event);
   75. switch (type) {
   76. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND:
   77. customNode->OnDrawBehind(event);
   78. break;
   79. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW:
   80. customNode->OnDraw(event);
   81. break;
   82. case ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT:
   83. customNode->OnDrawFront(event);
   84. break;
   85. default:
   86. break;
   87. }
   88. }

   90. // 自定义内容背景层：绘制聊天界面背景
   91. void OnDrawBehind(ArkUI_NodeCustomEvent* event)
   92. {
   93. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   94. auto canvas = reinterpret_cast<OH_Drawing_Canvas*>(OH_ArkUI_DrawContext_GetCanvas(drawContext));
   95. auto size = OH_ArkUI_DrawContext_GetSize(drawContext);

   97. // 绘制浅灰色背景
   98. auto bgRect = OH_Drawing_RectCreate(0, 0, size.width, size.height);
   99. auto brush = OH_Drawing_BrushCreate();
   100. OH_Drawing_BrushSetColor(brush, 0xFFF5F5F5);
   101. OH_Drawing_CanvasAttachBrush(canvas, brush);
   102. OH_Drawing_CanvasDrawRect(canvas, bgRect);
   103. OH_Drawing_CanvasDetachBrush(canvas);
   104. OH_Drawing_BrushDestroy(brush);
   105. OH_Drawing_RectDestroy(bgRect);
   106. }

   108. // 自定义内容层
   109. void OnDraw(ArkUI_NodeCustomEvent* event)
   110. {
   111. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   112. auto canvas = reinterpret_cast<OH_Drawing_Canvas*>(OH_ArkUI_DrawContext_GetCanvas(drawContext));
   113. auto size = OH_ArkUI_DrawContext_GetSize(drawContext);

   115. float padding = 50.0f;
   116. float bubbleWidth = size.width - 2 * padding;
   117. float bubbleHeight = size.height - 2 * padding;
   118. float cornerRadius = 8.0f;
   119. float textX = padding + 15.0f;
   120. float textY = padding + 20.0f;
   121. float textMaxWidth = bubbleWidth - 30.0f;

   123. // 绘制气泡阴影
   124. auto shadowRect = OH_Drawing_RectCreate(
   125. padding + 2, padding + 2, padding + bubbleWidth + 2, padding + bubbleHeight + 2);
   126. auto* shadowRoundRect = OH_Drawing_RoundRectCreate(shadowRect, cornerRadius, cornerRadius);
   127. auto shadowBrush = OH_Drawing_BrushCreate();
   128. OH_Drawing_BrushSetColor(shadowBrush, 0x30000000);
   129. OH_Drawing_CanvasAttachBrush(canvas, shadowBrush);
   130. OH_Drawing_CanvasDrawRoundRect(canvas, shadowRoundRect);
   131. OH_Drawing_CanvasDetachBrush(canvas);
   132. OH_Drawing_BrushDestroy(shadowBrush);
   133. OH_Drawing_RoundRectDestroy(shadowRoundRect);
   134. OH_Drawing_RectDestroy(shadowRect);

   136. // 绘制绿色气泡背景
   137. auto bubbleRect = OH_Drawing_RectCreate(padding, padding, padding + bubbleWidth, padding + bubbleHeight);
   138. auto* bubbleRoundRect = OH_Drawing_RoundRectCreate(bubbleRect, cornerRadius, cornerRadius);
   139. auto bubbleBrush = OH_Drawing_BrushCreate();
   140. OH_Drawing_BrushSetColor(bubbleBrush, 0xFF95EC69);
   141. OH_Drawing_CanvasAttachBrush(canvas, bubbleBrush);
   142. OH_Drawing_CanvasDrawRoundRect(canvas, bubbleRoundRect);
   143. OH_Drawing_CanvasDetachBrush(canvas);
   144. OH_Drawing_BrushDestroy(bubbleBrush);

   146. // 绘制气泡边框
   147. auto pen = OH_Drawing_PenCreate();
   148. OH_Drawing_PenSetWidth(pen, 1.0f);
   149. OH_Drawing_PenSetColor(pen, 0xFF7FD65A);
   150. OH_Drawing_CanvasAttachPen(canvas, pen);
   151. OH_Drawing_CanvasDrawRoundRect(canvas, bubbleRoundRect);
   152. OH_Drawing_CanvasDetachPen(canvas);
   153. OH_Drawing_PenDestroy(pen);
   154. OH_Drawing_RoundRectDestroy(bubbleRoundRect);
   155. OH_Drawing_RectDestroy(bubbleRect);

   157. // 绘制消息文本
   158. DrawMessageText(canvas, textX, textY, textMaxWidth);
   159. }

   161. // 自定义内容前景层：绘制装饰性蒙层
   162. void OnDrawFront(ArkUI_NodeCustomEvent* event)
   163. {
   164. if (!maskVisible_) {
   165. return;
   166. }

   168. auto drawContext = OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(event);
   169. auto canvas = reinterpret_cast<OH_Drawing_Canvas*>(OH_ArkUI_DrawContext_GetCanvas(drawContext));

   171. float padding = 50.0f;

   173. auto starBrush = OH_Drawing_BrushCreate();
   174. OH_Drawing_BrushSetColor(starBrush, 0x88FFFFFF);
   175. OH_Drawing_CanvasAttachBrush(canvas, starBrush);

   177. const float starRadius = 13.0f;
   178. const float textLeftX = padding + 26.0f;
   179. const float textRightX = padding + 146.0f;
   180. const float starBottomY = padding + 50.0f;
   181. const float starTopY = padding + 10.0f;
   182. for (int i = 0; i < starDecorationCount; ++i) {
   183. float t = static_cast<float>(i) / static_cast<float>(starDecorationCount - 1);
   184. float starX = textLeftX + (textRightX - textLeftX) * t;
   185. float starY = starBottomY + (starTopY - starBottomY) * t;
   186. DrawStar(canvas, starX, starY, starRadius);
   187. }

   189. OH_Drawing_CanvasDetachBrush(canvas);
   190. OH_Drawing_BrushDestroy(starBrush);
   191. }

   193. // 绘制五角星
   194. void DrawStar(OH_Drawing_Canvas* canvas, float cx, float cy, float radius)
   195. {
   196. auto path = OH_Drawing_PathCreate();
   197. for (int i = 0; i < starPointCount; ++i) {
   198. float angle = starStartAngleDegrees + i * starAngleStepDegrees;
   199. float rad = angle * degreeToRadian;
   200. float x = cx + radius * std::cos(rad);
   201. float y = cy + radius * std::sin(rad);
   202. if (i == 0) {
   203. OH_Drawing_PathMoveTo(path, x, y);
   204. } else {
   205. OH_Drawing_PathLineTo(path, x, y);
   206. }

   208. // 内角点
   209. float innerAngle = angle + starInnerAngleOffsetDegrees;
   210. float innerRad = innerAngle * degreeToRadian;
   211. float innerX = cx + radius * starInnerRadiusRatio * std::cos(innerRad);
   212. float innerY = cy + radius * starInnerRadiusRatio * std::sin(innerRad);
   213. OH_Drawing_PathLineTo(path, innerX, innerY);
   214. }

   216. OH_Drawing_PathClose(path);
   217. OH_Drawing_CanvasDrawPath(canvas, path);
   218. OH_Drawing_PathDestroy(path);
   219. }

   221. // 绘制消息文本
   222. void DrawMessageText(OH_Drawing_Canvas* canvas, float x, float y, float maxWidth)
   223. {
   224. // 创建字体集合
   225. auto* fontCollection = OH_Drawing_CreateFontCollection();

   227. // 创建排版样式
   228. auto* typographyStyle = OH_Drawing_CreateTypographyStyle();
   229. OH_Drawing_SetTypographyTextAlign(typographyStyle, TEXT_ALIGN_LEFT);

   231. // 创建排版处理器
   232. auto* typographyHandler = OH_Drawing_CreateTypographyHandler(typographyStyle, fontCollection);

   234. // 创建文本样式
   235. auto* textStyle = OH_Drawing_CreateTextStyle();
   236. OH_Drawing_SetTextStyleColor(textStyle, 0xFF000000); // 纯黑
   237. OH_Drawing_SetTextStyleFontSize(textStyle, messageTextFontSize);
   238. OH_Drawing_SetTextStyleFontWeight(textStyle, FONT_WEIGHT_400);
   239. auto textBrush = OH_Drawing_BrushCreate();
   240. OH_Drawing_BrushSetColor(textBrush, 0xFF000000);
   241. OH_Drawing_SetTextStyleForegroundBrush(textStyle, textBrush);

   243. // 添加文本
   244. OH_Drawing_TypographyHandlerPushTextStyle(typographyHandler, textStyle);
   245. OH_Drawing_TypographyHandlerAddText(typographyHandler, message_.c_str());
   246. OH_Drawing_TypographyHandlerPopTextStyle(typographyHandler);

   248. // 创建排版对象并绘制
   249. auto* typography = OH_Drawing_CreateTypography(typographyHandler);
   250. OH_Drawing_TypographyLayout(typography, maxWidth);
   251. OH_Drawing_TypographyPaint(typography, canvas, x, y);

   253. // 释放资源
   254. OH_Drawing_DestroyTextStyle(textStyle);
   255. OH_Drawing_DestroyTypography(typography);
   256. OH_Drawing_DestroyTypographyHandler(typographyHandler);
   257. OH_Drawing_DestroyTypographyStyle(typographyStyle);
   258. OH_Drawing_DestroyFontCollection(fontCollection);
   259. OH_Drawing_BrushDestroy(textBrush);
   260. }

   262. std::string message_ = "";
   263. bool maskVisible_ = false;
   264. };
   265. } // namespace NativeModule

   267. #endif // MYAPPLICATION_ARKUIMESSAGEMASKNODE_H
   ```
3. 使用消息蒙层组件创建示例界面。

   ```
   1. #include <arkui/native_node_napi.h>
   2. #include <arkui/native_type.h>
   3. #include <js_native_api.h>

   5. #include "NativeEntry.h"
   6. #include "ArkUICustomContainerNode.h"
   7. #include "ArkUICustomNode.h"
   8. #include "ArkUIMessageMaskNode.h"

   10. // 全局环境变量声明
   11. static napi_env g_env = nullptr;
   12. // ...
   13. namespace NativeModule {
   14. // ...
   15. napi_value CreateNativeMessageRoot(napi_env env, napi_callback_info info)
   16. {
   17. constexpr int32_t messageMaskWidth = 400;
   18. constexpr int32_t messageMaskHeight = 200;

   20. size_t argc = 1;
   21. napi_value args[1] = {nullptr};

   23. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   25. // 避免重复创建导致的重复挂载
   26. NativeEntry::GetInstance()->DisposeRootNode();

   28. // 获取NodeContent
   29. ArkUI_NodeContentHandle contentHandle;
   30. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   31. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   33. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
   34. auto rootColumn = std::make_shared<ArkUIColumnNode>();
   35. auto rootColumnHandle = rootColumn->GetHandle();

   37. // 设置根容器样式
   38. ArkUI_NumberValue paddingValue[] = {{.f32 = 20.0f}};
   39. ArkUI_AttributeItem paddingItem = {paddingValue, 1};
   40. nodeAPI->setAttribute(rootColumnHandle, NODE_PADDING, &paddingItem);

   42. ArkUI_NumberValue bgColorValue[] = {{.u32 = 0xFFFFFFFF}};
   43. ArkUI_AttributeItem bgColorItem = {bgColorValue, 1};
   44. nodeAPI->setAttribute(rootColumnHandle, NODE_BACKGROUND_COLOR, &bgColorItem);

   46. // 创建消息气泡组件
   47. auto maskNode = std::make_shared<ArkUIMessageMaskNode>();
   48. maskNode->SetWidth(messageMaskWidth);
   49. maskNode->SetHeight(messageMaskHeight);
   50. maskNode->SetMessage("您有一条新消息");
   51. maskNode->SetMaskVisible(false);  // 初始不显示蒙层

   53. // 创建按钮用于切换蒙层效果
   54. auto buttonNode = std::make_shared<ArkUINode>(nodeAPI->createNode(ARKUI_NODE_BUTTON));
   55. auto buttonHandle = buttonNode->GetHandle();

   57. // 设置按钮文本
   58. ArkUI_AttributeItem labelItem;
   59. const char* buttonLabel = "切换蒙层效果";
   60. labelItem.string = buttonLabel;
   61. nodeAPI->setAttribute(buttonHandle, NODE_BUTTON_LABEL, &labelItem);

   63. // 设置按钮样式
   64. ArkUI_NumberValue marginValue[] = {{.f32 = 20.0f}};
   65. ArkUI_AttributeItem marginItem = {marginValue, 1};
   66. nodeAPI->setAttribute(buttonHandle, NODE_MARGIN, &marginItem);

   68. ArkUI_NumberValue btnBgColorValue[] = {{.u32 = 0xFF2787D9}};
   69. ArkUI_AttributeItem btnBgColorItem = {btnBgColorValue, 1};
   70. nodeAPI->setAttribute(buttonHandle, NODE_BACKGROUND_COLOR, &btnBgColorItem);

   72. // 设置按钮点击事件
   73. auto onClick = [](ArkUI_NodeEvent *event) {
   74. auto maskNode = (ArkUIMessageMaskNode *)OH_ArkUI_NodeEvent_GetUserData(event);
   75. static bool highlighted = false;
   76. highlighted = !highlighted;
   77. maskNode->SetMaskVisible(highlighted);
   78. };
   79. buttonNode->RegisterOnClick(onClick, maskNode.get());

   81. // 将组件添加到根容器
   82. rootColumn->AddChild(buttonNode);
   83. rootColumn->AddChild(maskNode);

   85. // 保持Native侧对象到管理类中，维护生命周期
   86. NativeEntry::GetInstance()->SetRootNode(rootColumn);
   87. return nullptr;
   88. }

   90. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   91. {
   92. // 从管理类中释放Native侧对象。
   93. NativeEntry::GetInstance()->DisposeRootNode();
   94. return nullptr;
   95. }
   96. } // namespace NativeModule
   ```
