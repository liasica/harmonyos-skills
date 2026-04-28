---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embed-render-components
title: 构建渲染节点
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建渲染节点
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3eee71f5c02266dbd6e8650964c7c8f8e2f4d50d988a19136faf7e80d46e324
---

从API version 20开始，ArkUI开发框架针对NDK接口，提供了直接构建渲染节点的能力，包括节点树操作、属性设置及含动画的自定义绘制。开发者通过调用渲染节点相关能力，可以绕过[registerNodeCustomEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodecustomevent)的测量布局过程，直接对节点进行绘制并调整其大小和位置。

* **渲染节点树操作相关的能力** ，例如[OH\_ArkUI\_RenderNodeUtils\_AddRenderNode](../harmonyos-references/capi-native-render-h.md#oh_arkui_rendernodeutils_addrendernode)、[OH\_ArkUI\_RenderNodeUtils\_AddChild](../harmonyos-references/capi-native-render-h.md#oh_arkui_rendernodeutils_addchild)等接口用于编辑渲染节点树的结构。仅类型为ARKUI\_NODE\_CUSTOM且无其他子节点的自定义节点（加超链接到nativeNode）能够挂载渲染节点，且最多挂载一个渲染节点。即渲染节点以子树形式挂载在类型为ARKUI\_NODE\_CUSTOM的叶子自定义节点上。
* **渲染节点属性设置的能力** ，详情请参考[函数](../harmonyos-references/capi-native-render-h.md#函数)，查看当前渲染节点支持的属性能力。
* **自定义绘制能力**，参考[OH\_ArkUI\_RenderNodeUtils\_SetContentModifierOnDraw](../harmonyos-references/capi-native-render-h.md#oh_arkui_rendernodeutils_setcontentmodifierondraw)及其相关接口，同时可以通过[OH\_ArkUI\_RenderNodeUtils\_SetFloatPropertyValue](../harmonyos-references/capi-native-render-h.md#oh_arkui_rendernodeutils_setfloatpropertyvalue)这一类绑定在ContentModifier的接口对自定义绘制的内容进行动态修改。

## 节点挂载与基础属性设置

以下示例创建了一个渲染节点，并进行了基础的节点挂载和属性设置操作。

1. 按照[接入ArkTS页面](ndk-access-the-arkts-page.md)创建前置工程。
2. 创建渲染节点能力对象。

   ```
   1. // NativeEntry.cpp
   2. // 自定义容器组件示例。
   3. #include <arkui/native_animate.h>
   4. #include <arkui/native_render.h>
   5. #include <arkui/native_type.h>
   6. #include <arkui/native_node_napi.h>
   7. #include <bits/alltypes.h>

   9. #include <string>

   11. #include <arkui/native_interface.h>
   12. #include <arkui/native_node.h>
   13. #include <native_drawing/drawing_canvas.h>
   14. #include <native_drawing/drawing_color.h>
   15. #include <native_drawing/drawing_path.h>
   16. #include <native_drawing/drawing_pen.h>

   18. ArkUI_NodeHandle testRenderNode(ArkUI_NativeNodeAPI_1 *nodeAPI) {
   19. // 创建NDK原有容器逻辑。
   20. ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_SCROLL);
   21. ArkUI_NumberValue valueWidth[] = {400};
   22. ArkUI_AttributeItem itemWidth = {valueWidth, sizeof(valueWidth) / sizeof(ArkUI_NumberValue)};
   23. nodeAPI->setAttribute(scroll, NODE_WIDTH, &itemWidth);
   24. ArkUI_NumberValue valueHeight[] = {600};
   25. ArkUI_AttributeItem itemHeight = {valueHeight, sizeof(valueHeight) / sizeof(ArkUI_NumberValue)};
   26. nodeAPI->setAttribute(scroll, NODE_HEIGHT, &itemHeight);
   27. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   28. nodeAPI->setAttribute(column, NODE_WIDTH, &itemWidth);
   29. nodeAPI->setAttribute(column, NODE_HEIGHT, &itemHeight);
   30. ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
   31. ArkUI_AttributeItem content = {.string = "黄色背景是C-API页面"};
   32. nodeAPI->setAttribute(text, NODE_TEXT_CONTENT, &content);
   33. nodeAPI->addChild(column, text);

   35. // 创建RenderNode容器 -- NDK侧的Custom组件。
   36. ArkUI_NodeHandle Custom = nodeAPI->createNode(ARKUI_NODE_CUSTOM);
   37. valueWidth[0].f32 = 400;
   38. nodeAPI->setAttribute(Custom, NODE_WIDTH, &itemWidth);
   39. nodeAPI->setAttribute(Custom, NODE_HEIGHT, &itemWidth);
   40. nodeAPI->addChild(column, Custom);

   42. // 节点操作类接口 创建 - 挂载 - 构建树。
   43. // 创建部分。
   44. auto renderRootNode = OH_ArkUI_RenderNodeUtils_CreateNode();
   45. auto firstChildRenderNode = OH_ArkUI_RenderNodeUtils_CreateNode();
   46. auto secondChildRenderNode = OH_ArkUI_RenderNodeUtils_CreateNode();
   47. auto thirdChildRenderNode = OH_ArkUI_RenderNodeUtils_CreateNode();

   49. auto result = OH_ArkUI_RenderNodeUtils_AddRenderNode(Custom, renderRootNode);
   50. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
   51. // 通过错误码判断根节点是否挂载成功。
   52. return scroll;
   53. }

   55. OH_ArkUI_RenderNodeUtils_AddChild(renderRootNode, firstChildRenderNode);
   56. OH_ArkUI_RenderNodeUtils_AddChild(renderRootNode, secondChildRenderNode);
   57. OH_ArkUI_RenderNodeUtils_AddChild(renderRootNode, thirdChildRenderNode);

   59. // 设置节点尺寸与位置。
   60. OH_ArkUI_RenderNodeUtils_SetSize(renderRootNode, 500, 500);
   61. OH_ArkUI_RenderNodeUtils_SetSize(firstChildRenderNode, 120, 120);
   62. OH_ArkUI_RenderNodeUtils_SetSize(secondChildRenderNode, 120, 120);
   63. OH_ArkUI_RenderNodeUtils_SetSize(thirdChildRenderNode, 120, 120);

   65. OH_ArkUI_RenderNodeUtils_SetPosition(renderRootNode, 300, 100);
   66. OH_ArkUI_RenderNodeUtils_SetPosition(firstChildRenderNode, 0, 0);
   67. OH_ArkUI_RenderNodeUtils_SetPosition(secondChildRenderNode, 140, 140);
   68. OH_ArkUI_RenderNodeUtils_SetPosition(thirdChildRenderNode, 280, 280);

   70. // 设置颜色，方便通过颜色观察到节点的显示范围。
   71. OH_ArkUI_RenderNodeUtils_SetBackgroundColor(renderRootNode, 0xFFFFFFFF);
   72. OH_ArkUI_RenderNodeUtils_SetBackgroundColor(firstChildRenderNode, 0xFFFF0000); // R
   73. OH_ArkUI_RenderNodeUtils_SetBackgroundColor(secondChildRenderNode, 0xFF00FF00); // G
   74. OH_ArkUI_RenderNodeUtils_SetBackgroundColor(thirdChildRenderNode, 0xFF0000FF); // B

   76. // 简单的属性设置示例。
   77. OH_ArkUI_RenderNodeUtils_SetRotation(secondChildRenderNode, 45, 45, 0); // xy轴旋转45度，z轴旋转0度

   79. // 边框属性实例。
   80. auto styleOption = OH_ArkUI_RenderNodeUtils_CreateNodeBorderStyleOption();
   81. OH_ArkUI_RenderNodeUtils_SetNodeBorderStyleOptionEdgeStyle(styleOption, ArkUI_BorderStyle::ARKUI_BORDER_STYLE_SOLID,
   82. ArkUI_EdgeDirection::ARKUI_EDGE_DIRECTION_ALL);
   83. OH_ArkUI_RenderNodeUtils_SetBorderStyle(firstChildRenderNode, styleOption);
   84. // 结构体使用完成后，销毁释放内存。
   85. OH_ArkUI_RenderNodeUtils_DisposeNodeBorderStyleOption(styleOption);
   86. styleOption = nullptr;

   88. auto widthOption = OH_ArkUI_RenderNodeUtils_CreateNodeBorderWidthOption();
   89. OH_ArkUI_RenderNodeUtils_SetNodeBorderWidthOptionEdgeWidth(widthOption, 5,
   90. ArkUI_EdgeDirection::ARKUI_EDGE_DIRECTION_ALL);
   91. OH_ArkUI_RenderNodeUtils_SetBorderWidth(firstChildRenderNode, widthOption);
   92. // 结构体使用完成后，销毁释放内存。
   93. OH_ArkUI_RenderNodeUtils_DisposeNodeBorderWidthOption(widthOption);
   94. widthOption = nullptr;

   96. auto colorOption = OH_ArkUI_RenderNodeUtils_CreateNodeBorderColorOption();
   97. OH_ArkUI_RenderNodeUtils_SetNodeBorderColorOptionEdgeColor(colorOption, 0xFF000000,
   98. ArkUI_EdgeDirection::ARKUI_EDGE_DIRECTION_ALL);
   99. result = OH_ArkUI_RenderNodeUtils_SetBorderColor(firstChildRenderNode, colorOption);
   100. // 结构体使用完成后，销毁释放内存。
   101. OH_ArkUI_RenderNodeUtils_DisposeNodeBorderColorOption(colorOption);
   102. colorOption = nullptr;

   104. nodeAPI->addChild(scroll, column);
   105. return scroll;
   106. }

   108. napi_value CreateNativeRoot(napi_env env, napi_callback_info info) {
   109. size_t argc = 1;
   110. napi_value args[1] = {nullptr};

   112. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   114. auto *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   115. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   116. if (nodeAPI != nullptr) {
   117. ArkUI_NodeHandle testNode;
   118. testNode = testRenderNode(nodeAPI);
   119. }

   121. NativeEntry::GetInstance()->SetRootNode(testNode);
   122. return nullptr;
   123. }
   ```

## 自定义绘制及动画

以下示例创建了一个渲染节点，调用自定义绘制能力并附加动画功能。

1. 按照[接入ArkTS页面](ndk-access-the-arkts-page.md)创建前置工程。
2. 创建渲染节点能力对象。

   ```
   1. // NativeEntry.cpp
   2. // 自定义容器组件示例。
   3. #include <arkui/native_animate.h>
   4. #include <arkui/native_render.h>
   5. #include <arkui/native_type.h>
   6. #include <arkui/native_node_napi.h>
   7. #include <bits/alltypes.h>

   9. #include <string>

   11. #include <arkui/native_interface.h>
   12. #include <arkui/native_node.h>
   13. #include <native_drawing/drawing_canvas.h>
   14. #include <native_drawing/drawing_color.h>
   15. #include <native_drawing/drawing_path.h>
   16. #include <native_drawing/drawing_pen.h>

   18. ArkUI_NodeHandle testRenderNode2(ArkUI_NativeNodeAPI_1 *nodeAPI, ArkUI_ContextHandle context) {

   20. ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   21. ArkUI_NumberValue valueWidth[] = {400};
   22. ArkUI_AttributeItem itemWidth = {valueWidth, sizeof(valueWidth) / sizeof(ArkUI_NumberValue)};
   23. nodeAPI->setAttribute(scroll, NODE_WIDTH, &itemWidth);
   24. ArkUI_NumberValue valueHeight[] = {600};
   25. ArkUI_AttributeItem itemHeight = {valueHeight, sizeof(valueHeight) / sizeof(ArkUI_NumberValue)};
   26. nodeAPI->setAttribute(scroll, NODE_HEIGHT, &itemHeight);
   27. valueHeight[0].u32 = 0xff00F100;
   28. nodeAPI->setAttribute(scroll, NODE_BACKGROUND_COLOR, &itemHeight);

   30. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   31. ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
   32. ArkUI_AttributeItem content = {.string = "这是C-API页面"};

   34. nodeAPI->setAttribute(text, NODE_TEXT_CONTENT, &content);

   36. ArkUI_NodeHandle Custom = nodeAPI->createNode(ARKUI_NODE_CUSTOM);
   37. auto renderNode = OH_ArkUI_RenderNodeUtils_CreateNode();
   38. OH_ArkUI_RenderNodeUtils_AddRenderNode(Custom, renderNode);
   39. OH_ArkUI_RenderNodeUtils_SetSize(renderNode, 1000, 1000);

   41. // Property的作用是触发set更新，同步更新modifier的Draw方法。
   42. struct AnimatableUserData {
   43. ArkUI_FloatAnimatablePropertyHandle width;
   44. ArkUI_FloatAnimatablePropertyHandle height;
   45. ArkUI_Vector2AnimatablePropertyHandle v2;
   46. ArkUI_ColorAnimatablePropertyHandle color;
   47. };

   49. // 设置基础值。
   50. AnimatableUserData *userData1 = new AnimatableUserData;
   51. auto widthAnimProperty = OH_ArkUI_RenderNodeUtils_CreateFloatAnimatableProperty(1000);
   52. userData1->width = widthAnimProperty;
   53. auto heightAnimProperty = OH_ArkUI_RenderNodeUtils_CreateFloatAnimatableProperty(1000);
   54. userData1->height = heightAnimProperty;
   55. auto vectorAnimP = OH_ArkUI_RenderNodeUtils_CreateVector2AnimatableProperty(1000, 1000);
   56. userData1->v2 = vectorAnimP;
   57. auto colorAnimP = OH_ArkUI_RenderNodeUtils_CreateColorAnimatableProperty(0xFFFF11FF);
   58. userData1->color = colorAnimP;

   60. // 关联组件和多个modifier。
   61. auto animModifier = OH_ArkUI_RenderNodeUtils_CreateContentModifier();
   62. OH_ArkUI_RenderNodeUtils_AttachContentModifier(renderNode, animModifier);
   63. // 关联modifier和property。
   64. OH_ArkUI_RenderNodeUtils_AttachFloatAnimatableProperty(animModifier, widthAnimProperty);
   65. OH_ArkUI_RenderNodeUtils_AttachFloatAnimatableProperty(animModifier, heightAnimProperty);
   66. OH_ArkUI_RenderNodeUtils_AttachVector2AnimatableProperty(animModifier, vectorAnimP);
   67. OH_ArkUI_RenderNodeUtils_AttachColorAnimatableProperty(animModifier, colorAnimP);

   69. // 设置自定义绘制内容。
   70. OH_ArkUI_RenderNodeUtils_SetContentModifierOnDraw(
   71. animModifier, userData1, [](ArkUI_DrawContext *context, void *userData) {
   72. AnimatableUserData *data = (AnimatableUserData *)userData;
   73. float width = 0;
   74. float height = 0;
   75. uint32_t color = 0;
   76. ArkUI_Vector2AnimatablePropertyHandle v2 = data->v2;
   77. // property主要为传值用，这里用x,y来替代width，实际使用时可以通过property来自定义所需参数。
   78. OH_ArkUI_RenderNodeUtils_GetVector2AnimatablePropertyValue(v2, &width, &height);
   79. ArkUI_ColorAnimatablePropertyHandle cp = data->color;
   80. OH_ArkUI_RenderNodeUtils_GetColorAnimatablePropertyValue(cp, &color);

   83. auto *canvas1 = OH_ArkUI_DrawContext_GetCanvas(context);
   84. OH_Drawing_Canvas *canvas = reinterpret_cast<OH_Drawing_Canvas *>(canvas1);
   85. auto path = OH_Drawing_PathCreate();
   86. OH_Drawing_PathMoveTo(path, width / 4, height / 4);
   87. OH_Drawing_PathLineTo(path, width * 3 / 4, height / 4);
   88. OH_Drawing_PathLineTo(path, width * 3 / 4, height * 3 / 4);
   89. OH_Drawing_PathLineTo(path, width / 4, height * 3 / 4);
   90. OH_Drawing_PathLineTo(path, width / 4, height / 4);
   91. OH_Drawing_PathClose(path);
   92. auto pen = OH_Drawing_PenCreate();
   93. OH_Drawing_PenSetWidth(pen, 10);
   94. OH_Drawing_PenSetColor(pen, color);
   95. OH_Drawing_CanvasAttachPen(canvas, pen);
   96. OH_Drawing_CanvasDrawPath(canvas, path);
   97. });

   99. // 用户自定义参数。
   100. ArkUI_ContextCallback *update = new ArkUI_ContextCallback;
   101. update->userData = userData1;
   102. update->callback = [](void *user) {
   103. AnimatableUserData *data = (AnimatableUserData *)user;
   104. OH_ArkUI_RenderNodeUtils_SetFloatAnimatablePropertyValue(data->width, 100);
   105. OH_ArkUI_RenderNodeUtils_SetFloatAnimatablePropertyValue(data->height, 100);
   106. OH_ArkUI_RenderNodeUtils_SetVector2AnimatablePropertyValue(data->v2, 100, 100);
   107. OH_ArkUI_RenderNodeUtils_SetColorAnimatablePropertyValue(data->color, 0xFF0011FF);
   108. };
   109. // 执行对应的动画。
   110. ArkUI_NativeAnimateAPI_1 *animateApi = nullptr;
   111. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_ANIMATE, ArkUI_NativeAnimateAPI_1, animateApi);

   113. ArkUI_AnimateCompleteCallback *completeCallback = new ArkUI_AnimateCompleteCallback;
   114. completeCallback->userData = userData1;
   115. completeCallback->type = ARKUI_FINISH_CALLBACK_REMOVED;
   116. completeCallback->callback = [](void *userData) {
   117. AnimatableUserData *data = (AnimatableUserData *)userData;
   118. };

   120. ArkUI_AnimateOption *option = OH_ArkUI_AnimateOption_Create();
   121. OH_ArkUI_AnimateOption_SetDuration(option, 2000);
   122. OH_ArkUI_AnimateOption_SetTempo(option, 1.1);
   123. OH_ArkUI_AnimateOption_SetCurve(option, ARKUI_CURVE_EASE);
   124. OH_ArkUI_AnimateOption_SetDelay(option, 20);
   125. OH_ArkUI_AnimateOption_SetIterations(option, 1);
   126. OH_ArkUI_AnimateOption_SetPlayMode(option, ARKUI_ANIMATION_PLAY_MODE_REVERSE);
   127. ArkUI_ExpectedFrameRateRange *range = new ArkUI_ExpectedFrameRateRange;
   128. range->min = 10;
   129. range->max = 120;
   130. range->expected = 60;
   131. OH_ArkUI_AnimateOption_SetExpectedFrameRateRange(option, range);
   132. animateApi->animateTo(context, option, update, completeCallback);

   135. nodeAPI->setAttribute(Custom, NODE_WIDTH, &itemWidth);
   136. nodeAPI->setAttribute(Custom, NODE_HEIGHT, &itemHeight);

   138. nodeAPI->addChild(column, text);
   139. nodeAPI->addChild(column, Custom);
   140. nodeAPI->addChild(scroll, column);
   141. return scroll;
   142. }

   144. napi_value CreateNativeRoot(napi_env env, napi_callback_info info) {
   145. size_t argc = 2;
   146. napi_value args[2] = {nullptr, nullptr};

   148. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   150. auto *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   151. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   152. if (nodeAPI != nullptr) {
   153. ArkUI_NodeHandle testNode;
   154. // 获取ets侧传入的context。
   155. ArkUI_ContextHandle context = nullptr;
   156. // 通过code判断是否获取成功。
   157. auto code = OH_ArkUI_GetContextFromNapiValue(env, args[1], &context);
   158. testNode = testRenderNode2(nodeAPI, context);
   159. }

   161. NativeEntry::GetInstance()->SetRootNode(testNode);
   162. return nullptr;
   163. }
   ```

## 混排挂载原生组件与渲染节点

从API version 22开始，开发者可以高效地混排挂载原生组件与渲染节点。具体操作为：获取原生组件对应的渲染节点，并将其挂载至非原生组件的渲染节点下，从而实现原生组件的渲染节点与非原生组件的渲染节点混排。

进行混排挂载前，需要对原生组件进行接纳操作。父节点接纳目标子节点后，子节点会成为父节点的附属节点，只有附属节点能够获取渲染节点，并将这个渲染节点挂载至渲染节点树的其他位置上。

### 接纳子节点为附属节点

满足以下条件的节点，可以作为[OH\_ArkUI\_NativeModule\_AdoptChild](../harmonyos-references/capi-native-node-h.md#oh_arkui_nativemodule_adoptchild)接口中的父节点接纳其他节点：

1. 父节点是CAPI侧创建的命令式节点。
2. 父节点是ArkTS侧创建的命令式节点。

满足以下条件的节点，可以作为OH\_ArkUI\_NativeModule\_AdoptChild接口中的子节点被其他父节点接纳：

1. 子节点是CAPI侧创建的命令式节点。
2. 子节点是ArkTS侧创建的命令式节点。
3. 子节点是BuilderNode下的根节点。

子节点被接纳为附属节点后，不允许再作为常规子节点挂载至其他节点，否则会抛出相应的错误码。但允许该子节点被其他父节点再次接纳，此时该子节点将会成为其他父节点的新附属节点。被接纳的子节点不是其父节点的真实子节点，不在子组件查询接口的查询范围，也不支持像常规子节点那样被操作，同时不接受父节点的测量布局和事件传递，仅接收父节点的[生命周期](uiability-lifecycle.md#概述)传递。

### 获取附属节点的渲染节点

节点处于被接纳的附属节点状态下，允许调用[OH\_ArkUI\_RenderNodeUtils\_GetRenderNode](../harmonyos-references/capi-native-render-h.md#oh_arkui_rendernodeutils_getrendernode)获取它对应的RenderNode。

调用[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)的[disposeNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#disposenode)接口主动销毁父节点时，需要额外调用[OH\_ArkUI\_RenderNodeUtils\_DisposeNode](../harmonyos-references/capi-native-render-h.md#oh_arkui_rendernodeutils_disposenode)释放该渲染节点，否则会发生内存泄漏。

### 操作来自附属节点的渲染节点

从被接纳的附属节点中获取渲染节点后，即可使用该渲染节点进行布局，约束与限制如下：

1. 将来自附属节点的渲染节点挂载至其他渲染节点下。

   来自附属节点的渲染节点只能作为子节点挂载至其他渲染节点下，或者从其他渲染节点下取消挂载，除此之外的任何操作都会执行失败并返回错误码。完成渲染节点挂载后，附属节点将会被绘制在该渲染节点对应的目标位置上。
2. 附属节点的渲染节点依赖离屏挂载状态。

   如果该附属节点被它的父节点调用[OH\_ArkUI\_NativeModule\_RemoveAdoptedChild](../harmonyos-references/capi-native-node-h.md#oh_arkui_nativemodule_removeadoptedchild)接口取消离屏挂载状态，那么该渲染节点也会随之一同从渲染节点树上被移除。
3. 来自附属节点的渲染节点，如果它对应的附属节点已不处于离屏挂载状态，不允许重新将它挂载至其他渲染节点上。

### 创建并接纳Web组件以实现混排挂载

在进行如下代码开发前，请参考[接入ArkTS页面](ndk-access-the-arkts-page.md)，创建前置工程。

完整示例请参考[native\_render\_node\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeRenderNodeSample)。

1. NDK初始化组件环境，并创建对应的渲染节点根节点。

   ```
   1. std::shared_ptr<ArkUIBaseNode> custom_ = nullptr;
   2. std::shared_ptr<ArkUIRenderNode> render_ = nullptr;

   4. std::shared_ptr<ArkUIBaseNode> testGetRenderNodeDemo()
   5. {
   6. auto scroll = std::make_shared<ArkUIScrollNode>();
   7. scroll->SetWidth(g_contentWidth);
   8. scroll->SetHeight(g_contentHeight);
   9. scroll->SetBackgroundColor(0xff00F100);

   11. auto column = std::make_shared<ArkUIColumnNode>();
   12. column->SetWidth(g_contentWidth);
   13. column->SetHeight(g_contentHeight);
   14. auto text = std::make_shared<ArkUITextNode>();
   15. text->SetTextContent("挂载从frameNode获取的renderNode示例，点击下方挂载按钮");
   16. text->SetWidth(g_num300);
   17. text->SetHeight(g_num100);

   19. auto Custom = std::make_shared<ArkUICustomNode>();
   20. Custom->SetWidth(g_contentWidth);
   21. Custom->SetHeight(g_num100);
   22. column->AddChild(text);
   23. column->AddChild(Custom);
   24. custom_ = Custom;

   26. // 布置可挂载环境，将renderNode作为Custom的根节点挂载。
   27. auto renderNode = std::make_shared<ArkUIRenderNode>();
   28. Custom->AddRenderNode(renderNode);
   29. renderNode->SetSize(g_num300, g_num300);
   30. Custom->AddRenderNode(renderNode);
   31. render_ = renderNode;

   33. scroll->AddChild(column);
   34. return scroll;
   35. }

   37. napi_value CreateRenderNodeGetNodeExample(napi_env env, napi_callback_info info)
   38. {
   39. size_t argc = 2;
   40. napi_value args[2] = {nullptr, nullptr};
   41. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   42. // 获取ArkTS侧组件挂载点。
   43. ArkUI_NodeContentHandle contentHandle;
   44. int32_t result = OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   45. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
   46. return nullptr;
   47. }

   49. // 创建Native侧组件树根节点。
   50. auto scrollNode = std::make_shared<ArkUIScrollNode>();
   51. // 将Native侧组件树根节点挂载到UI主树上。
   52. result = OH_ArkUI_NodeContent_AddNode(contentHandle, scrollNode->GetHandle());
   53. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
   54. OH_LOG_ERROR(LOG_APP, "OH_ArkUI_NodeContent_AddNode Failed %{public}d", result);
   55. return nullptr;
   56. }
   57. // 保存Native侧组件树。
   58. g_nodeMap[contentHandle] = scrollNode;
   59. auto rootNode = testGetRenderNodeDemo();
   60. scrollNode->AddChild(rootNode);
   61. return nullptr;
   62. }
   ```
2. ArkTS侧创建节点并传递该节点至CAPI。

   ```
   1. import { BuilderNode, FrameNode, NodeContent, NodeController, typeNode } from '@kit.ArkUI';
   2. import entry from 'libentry.so';
   3. import { webview } from '@kit.ArkWeb';

   5. // 定义传递参数的接口
   6. interface ParamsInterface {
   7. text: string;
   8. func: Function;
   9. }
   10. class MyNodeController extends NodeController {
   11. private imperativeNode: FrameNode | null = null;
   12. public rootNode: typeNode.Column |null = null;
   13. private buildNode: FrameNode | null = null;

   15. makeNode(uiContext: UIContext): FrameNode {
   16. this.rootNode = typeNode.createNode(uiContext, 'Column');

   18. this.imperativeNode = new FrameNode(uiContext);
   19. this.rootNode?.appendChild(this.imperativeNode);
   20. return this.rootNode;
   21. }

   23. adoptNode(uiContext:UIContext, message:string):void {
   24. let buildNode = new BuilderNode<[ParamsInterface]>(uiContext);
   25. // 创建节点树
   26. buildNode.build(wrapBuilder<[ParamsInterface]>(buildText), {
   27. text: message, func: () => {
   28. return 'FUNCTION';
   29. }
   30. }, { nestingBuilderSupported: true });
   31. this.buildNode = buildNode.getFrameNode();
   32. entry.adopt(buildNode);
   33. }
   34. removeAdoptedNode(uiContext:UIContext):void {
   35. entry.removeAdopt();
   36. }
   37. }

   39. @Builder
   40. function buildTextWithFunc(fun: Function) {
   41. Web({ src: 'https://www.example.com', controller: new webview.WebviewController() })
   42. }

   44. @Builder
   45. function buildText(params: ParamsInterface) {
   46. Column() {
   47. buildTextWithFunc(params.func)
   48. }
   49. }

   51. @Component
   52. struct CAPIComponent {
   53. private rootSlot = new NodeContent();

   55. aboutToAppear(): void {
   56. entry.createRenderNodeGetNodeExample(this.rootSlot, this.getUIContext())
   57. }

   59. aboutToDisappear(): void {
   60. // 页面销毁前释放已创建的Native组件。
   61. entry.disposeNodeTree(this.rootSlot)
   62. }

   64. build() {
   65. Column() {
   66. // Native组件挂载点。
   67. ContentSlot(this.rootSlot)
   68. }
   69. }
   70. }

   72. @Entry
   73. @Component
   74. struct Index {
   75. @State isShow: boolean = false;
   76. @State isAdopt: boolean = false;
   77. @State message: string = 'CreateNodeTree';
   78. @State adoptmsg: string = 'adopt web component';

   80. private myNodeController: MyNodeController = new MyNodeController();
   81. build() {
   82. Flex() {
   83. Column() {
   84. Text('create CustomDrawNode，')
   85. .fontSize(18)
   86. .fontWeight(FontWeight.Bold)
   87. Button(this.message)
   88. .onClick(() => {
   89. this.isShow = !this.isShow;
   90. })
   91. if (this.isShow) {
   92. CAPIComponent()

   94. Button(this.adoptmsg)
   95. .onClick(() => {
   96. if (this.isAdopt) {
   97. this.myNodeController.removeAdoptedNode(this.getUIContext());
   98. this.adoptmsg = 'adopt web component';
   99. } else {
   100. this.myNodeController.adoptNode(this.getUIContext(),this.message);
   101. this.adoptmsg = 'remove adopt web';
   102. }
   103. this.isAdopt = !this.isAdopt;
   104. })

   106. NodeContainer(this.myNodeController)
   107. }
   108. }.width('100%')
   109. }.width('100%')
   110. }
   111. }
   ```
3. C-API侧获取该节点，接纳节点并获取对应的渲染节点。

   ```
   1. napi_value Adopt(napi_env env, napi_callback_info info)
   2. {
   3. size_t argc = 1;
   4. napi_value args[1] = {nullptr};
   5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   6. // 获取ArkTS侧组件挂载点。
   7. int32_t result = OH_ArkUI_GetNodeHandleFromNapiValue(env, args[0], &nodeHandle_);
   8. if (result != ARKUI_ERROR_CODE_NO_ERROR) {
   9. return nullptr;
   10. }
   11. result = OH_ArkUI_NativeModule_AdoptChild(custom_->GetHandle(), nodeHandle_);
   12. OH_ArkUI_RenderNodeUtils_GetRenderNode(nodeHandle_, &renderHandle_);
   13. OH_ArkUI_RenderNodeUtils_AddChild(render_->GetHandle(), renderHandle_);
   14. return nullptr;
   15. }
   ```
4. C-API侧解除已被接纳节点的接纳状态，释放其对应的渲染节点。

   ```
   1. napi_value RemoveAdopt(napi_env env, napi_callback_info info)
   2. {
   3. OH_ArkUI_NativeModule_RemoveAdoptedChild(custom_->GetHandle(), nodeHandle_);
   4. // 解除节点的接纳状态后，需要额外调用OH_ArkUI_RenderNodeUtils_DisposeNode释放对应的渲染节点，否则会导致内存泄漏。
   5. OH_ArkUI_RenderNodeUtils_DisposeNode(renderHandle_);
   6. nodeHandle_ = nullptr;
   7. renderHandle_ = nullptr;
   8. return nullptr;
   9. }
   ```
