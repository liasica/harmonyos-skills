---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-use-animation
title: 使用动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:52eee2106efb1b43a153de1b283aa6e44ac592f956cc58df46bcbe4e6226155c
---

## 使用属性动画

[ArkUI](arkui-overview.md)开发框架在[NDK](ndk-development-overview.md)接口主要提供属性动画，实现组件出现/消失转场。同时，可以通过Node-API桥接[ArkTS](arkts-overview.md)侧帧动画能力，实现Native侧的动画效果。

说明

* 需要从ArkTS侧获取[this.getUIContext()](../harmonyos-references/ts-custom-component-api.md#getuicontext)，传入到Native侧。
* 在Native侧通过[OH\_ArkUI\_GetContextFromNapiValue](../harmonyos-references/capi-native-node-napi-h.md#oh_arkui_getcontextfromnapivalue)方法获取context。
* 需要执行的动画属性变化必须写在[ArkUI\_ContextCallback](../harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback.md)中的callback中。
* 需要执行的动画属性，必须在执行动画之前设置过。
* 本篇示例仅提供核心接口的调用方法，完整的示例工程请参考[AnimationNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/AnimationNDK)。

提供全局[animateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)显式动画接口，来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态。

1. 在.ets文件中创建[NodeContent](../harmonyos-references/js-apis-arkui-nodecontent.md)，把NodeContent作为参数输出到Native方法中。

   ```
   1. // 初始化NodeContent对象。
   2. private rootSlot = new NodeContent();
   3. @State @Watch('changeNativeFlag') showNative: boolean = false;
   4. // ···
   5. changeNativeFlag(): void {
   6. // ···
   7. if (this.showNative) {
   8. // 传递NodeContent对象用于Native创建组件的挂载显示
   9. nativeNode?.createNativeRoot(this.rootSlot);
   10. } else {
   11. // ···
   12. }
   13. }
   ```

   [UseFrameAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/ets/pages/UseFrameAnimation.ets#L22-L49)
2. 解析NodeContent，转换为C中的[ArkUI\_NodeContentHandle](../harmonyos-references/capi-native-node-h.md)对象。

   ```
   1. // 获取NodeContent
   2. ArkUI_NodeContentHandle contentHandle;
   3. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/NativeEntry.cpp#L31-L35)
3. 获取[ArkUI\_NativeAnimateAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md) 对象。

   ```
   1. // 获取ArkUI_NativeAnimateAPI接口
   2. ArkUI_NativeAnimateAPI_1 *animateApi = nullptr;
   3. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_ANIMATE, ArkUI_NativeAnimateAPI_1, animateApi);
   ```

   [ArkUIAnimate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUIAnimate.h#L114-L118)
4. 设置[ArkUI\_AnimateOption](../harmonyos-references/capi-arkui-nativemodule-arkui-animateoption.md)参数，通过提供的C方法设置对应的参数。

   ```
   1. // 设置动画参数
   2. ArkUI_AnimateOption *option = OH_ArkUI_AnimateOption_Create();
   3. OH_ArkUI_AnimateOption_SetDuration(option, NUM_2000); // NUM_2000 = 2000
   4. OH_ArkUI_AnimateOption_SetTempo(option, 1.1);
   5. OH_ArkUI_AnimateOption_SetCurve(option, ARKUI_CURVE_EASE);
   6. ArkUI_CurveHandle cubicBezierCurve = OH_ArkUI_Curve_CreateCubicBezierCurve(0.5f, 4.0f, 1.2f, 0.0f);
   7. // 设置动画的动画曲线，优先于OH_ArkUI_AnimateOption_SetCurve生效
   8. OH_ArkUI_AnimateOption_SetICurve(option, cubicBezierCurve);
   9. OH_ArkUI_AnimateOption_SetDelay(option, NUM_20); // NUM_20 = 20
   10. OH_ArkUI_AnimateOption_SetIterations(option, NUM_1); // NUM_1 = 1
   11. OH_ArkUI_AnimateOption_SetPlayMode(option, ARKUI_ANIMATION_PLAY_MODE_REVERSE);
   12. ArkUI_ExpectedFrameRateRange *range = new ArkUI_ExpectedFrameRateRange;
   13. range->min = NUM_10; // NUM_10 = 10
   14. range->max = NUM_120; // NUM_120 = 120
   15. range->expected = NUM_60; // NUM_60 = 60
   16. OH_ArkUI_AnimateOption_SetExpectedFrameRateRange(option, range);
   ```

   [ArkUIAnimate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUIAnimate.h#L230-L247)
5. 设置回调参数。

   ```
   1. // 设置完成的回调
   2. ArkUI_AnimateCompleteCallback *completeCallback = new ArkUI_AnimateCompleteCallback;
   3. completeCallback->type = ARKUI_FINISH_CALLBACK_REMOVED;
   4. // 结构体AnimateData中包含ArkUI_AnimateOption* option和ArkUI_CurveHandle curve
   5. AnimateData* data = new AnimateData();
   6. data->option = option;
   7. data->curve = cubicBezierCurve;
   8. completeCallback->userData = reinterpret_cast<void*>(data);
   9. completeCallback->callback = [](void *userData) {
   10. AnimateData* data = reinterpret_cast<AnimateData*>(userData);
   11. if (data) {
   12. ArkUI_AnimateOption* option = data->option;
   13. ArkUI_CurveHandle curve = data->curve;
   14. if (option) {
   15. OH_ArkUI_AnimateOption_Dispose(option);
   16. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
   17. "Init", "CXX OH_ArkUI_AnimateOption_Dispose  success!");
   18. }
   19. if (curve) {
   20. OH_ArkUI_Curve_DisposeCurve(curve);
   21. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
   22. "Init", "CXX OH_ArkUI_Curve_DisposeCurve  success!");
   23. }
   24. delete data; // 释放结构体
   25. }
   26. };

   28. // 设置闭包函数
   29. static bool isback = true;
   30. ArkUI_ContextCallback *update = new ArkUI_ContextCallback;
   31. update->callback = [](void *user) {
   32. // 对应的属性变化 width height
   33. if (isback) {
   34. g_animateto_button->SetWidth(NUM_200); // NUM_200 = 200
   35. g_animateto_button->SetHeight(NUM_80); // NUM_80 = 80
   36. g_animateto_button->SetBackgroundColor(0xFFA280FF);
   37. } else {
   38. g_animateto_button->SetWidth(NUM_100); // NUM_100 = 100
   39. g_animateto_button->SetHeight(NUM_40); // NUM_40 = 40
   40. g_animateto_button->SetBackgroundColor(0xFFFF2E77);
   41. }
   42. isback = !isback;
   43. };
   44. // 执行对应的动画
   45. animateApi->animateTo(context, option, update, completeCallback);
   ```

   [ArkUIAnimate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUIAnimate.h#L249-L295)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/M53hcY5CSACCglaco0nR5A/zh-cn_image_0000002589324421.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052830Z&HW-CC-Expire=86400&HW-CC-Sign=CE1C247DCDF466FA40B76F765172D031FB070F7E454771BC581FD324E11FBAA5)

## 组件出现/消失转场

组件内转场通过NODE\_XX\_TRANSITION属性（XX包括：OPACITY、TRANSLATE、SCALE、ROTATE、MOVE）配置转场参数，在组件插入和删除时显示过渡动效（通过[NODE\_TRANSFORM\_CENTER](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)属性设置NODE\_SCALE\_TRANSITION和NODE\_ROTATE\_ROTATE动效的中心点坐标）。主要用于容器组件中子组件插入和删除时，提升用户体验。

1. 创建可交互界面，界面中包含Button，点击可以控制转场节点的添加和移除。其中 ArkUI\_NodeContentHandle 类型节点的获取与使用可参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

   ```
   1. constexpr int32_t BUTTON_CLICK_ID = 1;
   2. bool g_flag = false;
   3. ArkUI_NodeHandle parentNode;
   4. ArkUI_NodeHandle childNode;
   5. ArkUI_NodeHandle buttonNode;
   6. // ···
   7. void mainViewMethod(ArkUI_NodeContentHandle handle)
   8. {
   9. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   10. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   11. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   12. ArkUI_NumberValue widthValue[] = {{.f32 = 500}};
   13. ArkUI_AttributeItem widthItem = {.value = widthValue, .size = sizeof(widthValue) / sizeof(ArkUI_NumberValue)};
   14. nodeAPI->setAttribute(column, NODE_WIDTH, &widthItem);
   15. ArkUI_NumberValue heightValue[] = {{.f32 = 500}};
   16. ArkUI_AttributeItem heightItem = {.value = heightValue, .size = sizeof(heightValue) / sizeof(ArkUI_NumberValue)};
   17. nodeAPI->setAttribute(column, NODE_HEIGHT, &heightItem);
   18. ArkUI_NodeHandle buttonShow = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   19. ArkUI_NumberValue buttonWidthValue[] = {{.f32 = 200}};
   20. ArkUI_AttributeItem buttonWidthItem = {.value = buttonWidthValue,
   21. .size = sizeof(buttonWidthValue) / sizeof(ArkUI_NumberValue)};
   22. nodeAPI->setAttribute(buttonShow, NODE_WIDTH, &buttonWidthItem);
   23. ArkUI_NumberValue buttonHeightValue[] = {{.f32 = 50}};
   24. ArkUI_AttributeItem buttonHeightItem = {.value = buttonHeightValue,
   25. .size = sizeof(buttonHeightValue) / sizeof(ArkUI_NumberValue)};
   26. nodeAPI->setAttribute(buttonShow, NODE_HEIGHT, &buttonHeightItem);
   27. ArkUI_AttributeItem labelItem = {.string = "show"};
   28. nodeAPI->setAttribute(buttonShow, NODE_BUTTON_LABEL, &labelItem);
   29. ArkUI_NumberValue buttonOpenTypeValue[] = {{.i32 = static_cast<int32_t>(ARKUI_BUTTON_TYPE_NORMAL)}};
   30. ArkUI_AttributeItem buttonOpenTypeItem = {.value = buttonOpenTypeValue,
   31. .size = sizeof(buttonOpenTypeValue) / sizeof(ArkUI_NumberValue)};
   32. nodeAPI->setAttribute(buttonShow, NODE_BUTTON_TYPE, &buttonOpenTypeItem);
   33. ArkUI_NumberValue buttonShowMarginValue[] = {{.f32 = 20}};
   34. ArkUI_AttributeItem buttonShowMarginItem = {.value = buttonShowMarginValue,
   35. .size = sizeof(buttonShowMarginValue) / sizeof(ArkUI_NumberValue)};
   36. nodeAPI->setAttribute(buttonShow, NODE_MARGIN, &buttonShowMarginItem);
   37. nodeAPI->registerNodeEvent(buttonShow, NODE_ON_CLICK, BUTTON_CLICK_ID, nullptr);
   38. nodeAPI->addNodeEventReceiver(buttonShow, OnButtonShowClicked);
   39. parentNode = column;
   40. buttonNode = buttonShow;
   41. nodeAPI->addChild(column, buttonShow);
   42. OH_ArkUI_NodeContent_AddNode(handle, column);
   43. }
   ```

   [ArkUITransition.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUITransition.h#L24-L131)
2. 创建一个设置了[NODE\_ROTATE\_TRANSITION](../harmonyos-references/capi-native-node-h.md), [NODE\_SCALE\_TRANSITION](../harmonyos-references/capi-native-node-h.md), [NODE\_TRANSLATE\_TRANSITION](../harmonyos-references/capi-native-node-h.md)属性的节点，当目标节点上下树时会播放转场动画。

   ```
   1. ArkUI_NodeHandle CreateChildNode()
   2. {
   3. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   4. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   5. ArkUI_NodeHandle image = nodeAPI->createNode(ARKUI_NODE_IMAGE);
   6. ArkUI_AttributeItem imageSrcItem = {.string = "/pages/common/scenery.jpg"};
   7. nodeAPI->setAttribute(image, NODE_IMAGE_SRC, &imageSrcItem);
   8. ArkUI_NumberValue textWidthValue[] = {{.f32 = 300}};
   9. ArkUI_AttributeItem textWidthItem = {.value = textWidthValue,
   10. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
   11. nodeAPI->setAttribute(image, NODE_WIDTH, &textWidthItem);
   12. ArkUI_NumberValue textHeightValue[] = {{.f32 = 300}};
   13. ArkUI_AttributeItem textHeightItem = {.value = textHeightValue,
   14. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
   15. nodeAPI->setAttribute(image, NODE_HEIGHT, &textHeightItem);
   16. ArkUI_NumberValue transformCenterValue[] = {0.0f, 0.0f, 0.0f, 0.5f, 0.5f};
   17. ArkUI_AttributeItem transformCenterItem = {.value = transformCenterValue,
   18. .size = sizeof(transformCenterValue) / sizeof(ArkUI_NumberValue)};
   19. nodeAPI->setAttribute(image, NODE_TRANSFORM_CENTER, &transformCenterItem);
   20. ArkUI_NumberValue rotateAnimationValue[] = {
   21. 0.0f, 0.0f, 1.0f, 360.0f, 0.0f, {.i32 = 500}, {.i32 = static_cast<int32_t>(ARKUI_CURVE_SHARP)}};
   22. ArkUI_AttributeItem rotateAnimationItem = {.value = rotateAnimationValue,
   23. .size = sizeof(rotateAnimationValue) / sizeof(ArkUI_NumberValue)};
   24. nodeAPI->setAttribute(image, NODE_ROTATE_TRANSITION, &rotateAnimationItem);
   25. ArkUI_NumberValue scaleAnimationValue[] = {
   26. 0.0f, 0.0f, 0.0f, {.i32 = 500}, {.i32 = static_cast<int32_t>(ARKUI_CURVE_SHARP)}};
   27. ArkUI_AttributeItem scaleAnimationItem = {.value = scaleAnimationValue,
   28. .size = sizeof(scaleAnimationValue) / sizeof(ArkUI_NumberValue)};
   29. nodeAPI->setAttribute(image, NODE_SCALE_TRANSITION, &scaleAnimationItem);
   30. ArkUI_NumberValue translateAnimationValue[] = {
   31. 200, 200, 0.0f, {.i32 = 500}, {.i32 = static_cast<int32_t>(ARKUI_CURVE_SHARP)}};
   32. ArkUI_AttributeItem translateAnimationItem = {.value = translateAnimationValue,
   33. .size = sizeof(translateAnimationValue) / sizeof(ArkUI_NumberValue)};
   34. nodeAPI->setAttribute(image, NODE_TRANSLATE_TRANSITION, &translateAnimationItem);
   35. return image;
   36. }
   ```

   [ArkUITransition.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUITransition.h#L31-L68)
3. 在Button的监听回调里添加转场节点上下树逻辑，以此控制转场节点的入场和出场。

   ```
   1. void OnButtonShowClicked(ArkUI_NodeEvent *event)
   2. {
   3. if (!event) {
   4. return;
   5. }
   6. if (!childNode) {
   7. childNode = CreateChildNode();
   8. }
   9. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   10. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   11. if (g_flag) {
   12. g_flag = false;
   13. ArkUI_AttributeItem labelItem = {.string = "show"};
   14. nodeAPI->setAttribute(buttonNode, NODE_BUTTON_LABEL, &labelItem);
   15. nodeAPI->removeChild(parentNode, childNode);
   16. } else {
   17. g_flag = true;
   18. ArkUI_AttributeItem labelItem = {.string = "hide"};
   19. nodeAPI->setAttribute(buttonNode, NODE_BUTTON_LABEL, &labelItem);
   20. nodeAPI->addChild(parentNode, childNode);
   21. }
   22. }
   ```

   [ArkUITransition.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUITransition.h#L69-L92)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Hg6xssHrT7GlwfxUS4kOmg/zh-cn_image_0000002589244361.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052830Z&HW-CC-Expire=86400&HW-CC-Sign=F46BF1A4852992093741162ACB2F677C476CBEC7BC602CC6B2691C3FC2385E65)

## 使用关键帧动画

[keyframeAnimateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#keyframeanimateto)接口来指定若干个关键帧状态，实现分段的动画。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态。

该示例主要演示如何通过[keyframeAnimateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#keyframeanimateto)来设置关键帧动画，NDK接口开发的UI界面挂载到ArkTS主页面的完整流程可参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

```
1. // ArkUIColumnNode为工程内封装的node类型
2. auto column = std::make_shared<ArkUIColumnNode>();
3. // 设置宽度为300，NUM_300 = 300
4. column->SetWidth(NUM_300);
5. // 设置高度为250，NUM_250 = 250
6. column->SetHeight(NUM_250);
7. // 创建文本节点，内容区介绍“这是关键帧动画”
8. auto textNode = std::make_shared<ArkUITextNode>();
9. textNode->SetTextContent("这是关键帧动画");
10. // 设置宽度为120，NUM_120 = 120
11. textNode->SetWidth(NUM_120);
12. // 设置高度为120，NUM_120 = 120
13. textNode->SetHeight(NUM_50);
14. // 创建button，后续创建的关键帧动画作用在button组件上
15. auto button = std::make_shared<ArkUIButtonNode>();
16. // 设置button初始宽高，NUM_100 = 100
17. button->SetWidth(NUM_100);
18. button->SetHeight(NUM_100);
19. // 存储button全局变量，在onTouch注册时需要使用
20. g_keyframe_button = button;
21. // 注册点击事件到button上，NUM_1 = 1
22. button->RegisterNodeEvent(button->GetHandle(), NODE_ON_CLICK, NUM_1, nullptr);
23. g_keyframe_text = std::make_shared<ArkUITextNode>();
24. // 该函数为封装功能为在text组件中打印Animateto中参数值，使用者根据需要自行封装
25. g_keyframe_text->KeyframeAnimatetoToString();
26. auto onTouch = [](ArkUI_NodeEvent *event) {
27. // 点击button按钮时触发该逻辑，NUM_1 = 1
28. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_1) {
29. // 获取context对象
30. ArkUI_ContextHandle context = nullptr;
31. // std::shared_ptr<ArkUIButtonNode> g_keyframe_button存储button的全局变量，在onTouch注册时需要使用
32. context = OH_ArkUI_GetContextByNode(g_keyframe_button->GetHandle());
33. // 获取ArkUI_NativeAnimateAPI接口
34. ArkUI_NativeAnimateAPI_1 *animateApi = nullptr;
35. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_ANIMATE, ArkUI_NativeAnimateAPI_1, animateApi);

37. // 以下代码为创建关键帧动画的关键流程，包括设置关键帧动画参数、开启关键帧动画
38. // 设置ArkUI_KeyframeAnimateOption参数，通过提供的C方法设置对应的参数
39. // 关键帧动画状态数，NUM_2 = 2，NUM_500 = 500
40. ArkUI_KeyframeAnimateOption *option =  OH_ArkUI_KeyframeAnimateOption_Create(NUM_2);
41. OH_ArkUI_KeyframeAnimateOption_SetDelay(option, NUM_500);
42. // 第一段关键帧动画的持续时间，NUM_1000 = 1000，NUM_0 = 0
43. OH_ArkUI_KeyframeAnimateOption_SetDuration(option, NUM_1000, NUM_0);
44. // 第二段关键帧动画的持续时间，NUM_2000 = 2000，NUM_1 = 1
45. OH_ArkUI_KeyframeAnimateOption_SetDuration(option, NUM_2000, NUM_1);
46. // 关键帧动画播放次数，NUM_5 = 5
47. OH_ArkUI_KeyframeAnimateOption_SetIterations(option, NUM_5);
48. ArkUI_CurveHandle curve = OH_ArkUI_Curve_CreateCubicBezierCurve(0.5f, 4.0f, 1.2f, 0.0f);
49. // 以下四种曲线需要根据实际业务选择
50. ArkUI_CurveHandle springCurve = OH_ArkUI_Curve_CreateSpringCurve(0.5f, 4.0f, 1.2f, 0.0f);
51. ArkUI_CurveHandle springMotionCurve = OH_ArkUI_Curve_CreateSpringMotion(0.5f, 0.6f, 0.0f);
52. ArkUI_CurveHandle responsiveSpringMotionCurve = OH_ArkUI_Curve_CreateResponsiveSpringMotion(0.5f,
53. 4.0f, 1.2f);
54. ArkUI_CurveHandle interpolatingSpringCurve = OH_ArkUI_Curve_CreateInterpolatingSpring(0.5f,
55. 4.0f, 1.2f, 0.0f);
56. OH_ArkUI_KeyframeAnimateOption_SetCurve(option, curve, 1);
57. OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback(option, nullptr, [](void *userData) {
58. g_keyframe_button->SetWidth(NUM_150);
59. }, NUM_0); // 第一段关键帧时刻状态的闭包函数NUM_150 = 150，NUM_0 = 0
60. OH_ArkUI_KeyframeAnimateOption_RegisterOnEventCallback(option, nullptr, [](void *userData) {
61. g_keyframe_button->SetWidth(80);
62. }, NUM_1); // 第二段关键帧时刻状态的闭包函数NUM_1 = 1
63. KeyFrameAnimateToData* data = new KeyFrameAnimateToData();
64. data->option = option;
65. data->curve = curve;
66. OH_ArkUI_KeyframeAnimateOption_RegisterOnFinishCallback(option, nullptr, [](void *user) {
67. KeyFrameAnimateToData* data = reinterpret_cast<KeyFrameAnimateToData*>(user);
68. if (data) {
69. ArkUI_KeyframeAnimateOption* option = data->option;
70. ArkUI_CurveHandle curve = data->curve;
71. if (option) {
72. OH_ArkUI_KeyframeAnimateOption_Dispose(option);
73. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
74. "Init", "CXX OH_ArkUI_KeyframeAnimateOption_Dispose  success!");
75. }
76. if (curve) {
77. OH_ArkUI_Curve_DisposeCurve(curve);
78. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
79. "Init", "CXX OH_ArkUI_Curve_DisposeCurve  success!");
80. }
81. delete data; // 释放结构体
82. }
83. }); // 关键帧动画结束回调
84. ArkUI_ExpectedFrameRateRange *range = new ArkUI_ExpectedFrameRateRange;
85. range->max = NUM_120; // NUM_120 = 120
86. range->expected = NUM_60; // NUM_60 = 60
87. range->min = NUM_30; // NUM_30 = 30
88. OH_ArkUI_KeyframeAnimateOption_SetExpectedFrameRate(option, range); // 关键帧设置期望帧率

90. // 执行对应的动画
91. animateApi->keyframeAnimateTo(context, option);
92. auto delay = OH_ArkUI_KeyframeAnimateOption_GetDelay(option);
93. auto iter = OH_ArkUI_KeyframeAnimateOption_GetIterations(option);
94. auto expected = OH_ArkUI_KeyframeAnimateOption_GetExpectedFrameRate(option); // 获取关键帧动画参数的期望帧率
95. auto dur0 = OH_ArkUI_KeyframeAnimateOption_GetDuration(option, NUM_1); // NUM_1 = 1
96. auto dur1 = OH_ArkUI_KeyframeAnimateOption_GetDuration(option, NUM_1);
97. auto curves = OH_ArkUI_KeyframeAnimateOption_GetCurve(option, NUM_1); // 获取关键帧动画某段状态动画曲线
98. g_keyframe_text->KeyframeAnimatetoToString(dur0, dur1, delay, iter, *expected);
99. }
100. };
101. // 注册点击事件的回调函数
102. button->RegisterNodeEventReceiver(onTouch);
103. // 将button挂载在column上，返回column节点
104. column->AddChild(g_keyframe_text);
105. column->AddChild(textNode);
106. column->AddChild(button);
```

[ArkUIAnimate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUIAnimate.h#L81-L190)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/LOEyu362RIaRVaWYSpXIcw/zh-cn_image_0000002558764554.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052830Z&HW-CC-Expire=86400&HW-CC-Sign=390C9E9A8AF7A65CF1CCD8BCC94B17247BD297F25846005AC0AFFFF65D888BF4)

## 使用帧动画

帧动画具有逐帧回调的特性，便于开发者在每一帧中调整所需属性。通过提供[onFrame](../harmonyos-references/capi-native-animate-h.md#oh_arkui_animatoroption_registeronframecallback)逐帧回调，帧动画允许开发者在应用的每一帧设置属性值，从而实现组件属性值变化的自然过渡，营造出流畅的动画效果。帧动画接口可参考[createAnimator](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#createanimator)。

与属性动画相比，帧动画能让开发者实时感知动画进程，即时调整UI值，并具备事件即时响应和可暂停的优势，但在性能方面略逊于属性动画。当属性动画能满足需求时，建议优先采用属性动画接口实现。[animateTo](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#animateto)接口的使用可参考[使用属性动画](ndk-use-animation.md#使用属性动画)。

该示例主要演示如何通过[createAnimator](../harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1.md#createanimator)来设置帧动画，完整的示例工程请参考[AnimationNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/AnimationNDK)。

```
1. std::shared_ptr<ArkUIBaseNode> CreateAnimator()
2. {
3. auto column = std::make_shared<ArkUIColumnNode>();
4. column->SetWidth(NUM_300); // NUM_300 = 300
5. column->SetHeight(NUM_250); // NUM_250 = 250
6. // 创建文本节点，内容区介绍“这是animator动画”
7. auto textNode = std::make_shared<ArkUITextNode>();
8. textNode->SetTextContent("这是animator动画");
9. textNode->SetWidth(NUM_120); // NUM_120 = 120
10. textNode->SetHeight(NUM_50); // NUM_50 = 50
11. // 创建createButton，用于初始化animator参数
12. auto createButton = std::make_shared<ArkUIButtonNode>();
13. // 创建button，后续创建的animator动画作用在button组件上
14. auto button = std::make_shared<ArkUIButtonNode>();
15. // 设置button初始宽高，NUM_100 = 100
16. button->SetWidth(NUM_100);
17. button->SetHeight(NUM_100);
18. // 存储button全局变量，在onTouch注册时需要使用
19. g_animator_button = button;
20. // 注册点击事件到button上，NUM_3 = 3
21. createButton->RegisterNodeEvent(createButton->GetHandle(), NODE_ON_CLICK, NUM_3, nullptr);
22. g_animator_text = std::make_shared<ArkUITextNode>();
23. g_animator_text->AnimatorToString();
24. auto onTouch = [](ArkUI_NodeEvent *event) {
25. // 点击button按钮时触发该逻辑，NUM_3 = 3
26. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_3) {
27. // 获取context对象
28. static ArkUI_ContextHandle context = nullptr;
29. context = OH_ArkUI_GetContextByNode(g_animator_button->GetHandle());

31. // 获取ArkUI_NativeAnimateAPI接口
32. ArkUI_NativeAnimateAPI_1 *animateApi = nullptr;
33. OH_ArkUI_GetModuleInterface(ARKUI_NATIVE_ANIMATE, ArkUI_NativeAnimateAPI_1, animateApi);

35. // 以下代码为创建Animator动画的关键流程，包括设置Animator动画参数、开启Animator动画
36. // 设置ArkUI_AnimatorOption参数，通过提供的C方法设置对应的参数，NUM_0 = 0
37. static ArkUI_AnimatorOption *option =  OH_ArkUI_AnimatorOption_Create(NUM_0); // Animator动画状态数
38. OH_ArkUI_AnimatorOption_SetDuration(option, NUM_2000); // NUM_2000 = 2000
39. OH_ArkUI_AnimatorOption_SetDelay(option, NUM_10); // NUM_10 = 10
40. OH_ArkUI_AnimatorOption_SetIterations(option, NUM_3); // NUM_3 = 3
41. OH_ArkUI_AnimatorOption_SetFill(option, ARKUI_ANIMATION_FILL_MODE_NONE);
42. OH_ArkUI_AnimatorOption_SetDirection(option, ARKUI_ANIMATION_DIRECTION_NORMAL);
43. ArkUI_CurveHandle curve = OH_ArkUI_Curve_CreateCubicBezierCurve(0.5f, 4.0f, 1.2f, 0.0f); // 构造三阶贝塞尔曲线对象
44. OH_ArkUI_AnimatorOption_SetCurve(option, curve);
45. OH_ArkUI_AnimatorOption_SetBegin(option, NUM_100); // NUM_100 = 100
46. OH_ArkUI_AnimatorOption_SetEnd(option, NUM_150); // NUM_150 = 150
47. ArkUI_ExpectedFrameRateRange *range = new ArkUI_ExpectedFrameRateRange;
48. range->max = NUM_120; // NUM_120 = 120
49. range->expected = NUM_60; // NUM_60 = 60
50. range->min = NUM_30; // NUM_30 = 30
51. OH_ArkUI_AnimatorOption_SetExpectedFrameRateRange(option, range);
52. OH_ArkUI_AnimatorOption_SetKeyframe(option, 0.5, 120.5, NUM_0); // 设置animator动画关键帧参数，NUM_0 = 0
53. OH_ArkUI_AnimatorOption_SetKeyframeCurve(option, curve, NUM_0); // 设置animator动画关键帧曲线类型
54. OH_ArkUI_AnimatorOption_RegisterOnFrameCallback(option, nullptr, [](ArkUI_AnimatorOnFrameEvent *event)
55. {
56. OH_ArkUI_AnimatorOnFrameEvent_GetUserData(event); // 获取动画事件对象中的用户自定义对象
57. auto value = OH_ArkUI_AnimatorOnFrameEvent_GetValue(event); // 获取动画事件对象中的当前进度
58. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Init",
59. "CXX OH_ArkUI_AnimatorOption_RegisterOnFrameCallback  %{public}f", value);
60. g_animator_button->SetWidth(value);
61. });
62. OH_ArkUI_AnimatorOption_RegisterOnFinishCallback(option, nullptr, [](ArkUI_AnimatorEvent* event)
63. {
64. OH_ArkUI_AnimatorEvent_GetUserData(event); // 获取动画事件对象中的用户自定义对象
65. });
66. OH_ArkUI_AnimatorOption_RegisterOnCancelCallback(option, nullptr, [](ArkUI_AnimatorEvent* event)
67. {
68. });
69. OH_ArkUI_AnimatorOption_RegisterOnRepeatCallback(option, nullptr, [](ArkUI_AnimatorEvent* event)
70. {
71. });
72. // 执行对应的动画
73. animatorHandle = animateApi->createAnimator(context, option);

75. auto duration = OH_ArkUI_AnimatorOption_GetDuration(option);
76. auto delay = OH_ArkUI_AnimatorOption_GetDelay(option);
77. auto iterations = OH_ArkUI_AnimatorOption_GetIterations(option);
78. auto fill = OH_ArkUI_AnimatorOption_GetFill(option);
79. auto direction = OH_ArkUI_AnimatorOption_GetDirection(option);
80. auto curves = OH_ArkUI_AnimatorOption_GetCurve(option); // 获取animator动画插值曲线
81. auto begin = OH_ArkUI_AnimatorOption_GetBegin(option);
82. auto end = OH_ArkUI_AnimatorOption_GetEnd(option); // 获取animator动画插值终点
83. auto expected = OH_ArkUI_AnimatorOption_GetExpectedFrameRateRange(option); // 获取关键帧动画参数的期望帧率
84. auto keyframeTime = OH_ArkUI_AnimatorOption_GetKeyframeTime(option, NUM_0); // 获取animator动画关键帧时间
85. auto keyframeValue = OH_ArkUI_AnimatorOption_GetKeyframeValue(option, NUM_0); // 获取animator动画关键帧数值
86. auto keyframeCurve = OH_ArkUI_AnimatorOption_GetKeyframeCurve(option, NUM_0); // 获取animator动画关键帧动画插值曲线
87. g_animator_text->AnimatorToString(duration, delay, iterations, fill, direction, begin,
88. end, *expected, keyframeTime, keyframeValue);
89. }
90. };

92. // 注册点击事件的回调函数
93. createButton->RegisterNodeEventReceiver(onTouch);
94. createButton->SetButtonLabel("create");
95. // 创建容器，用于存放button按键
96. auto buttoColumn = std::make_shared<ArkUIColumnNode>();
97. buttoColumn->SetPadding(NUM_30, false); // 设置布局格式，调整组件内间距，NUM_30 = 30
98. buttoColumn->SetWidth(NUM_300); // NUM_300 = 300
99. // 创建容器，用于存放playButton按键
100. auto playButtonColumn = std::make_shared<ArkUIColumnNode>();
101. playButtonColumn->SetPadding(NUM_10, false); // 设置布局格式，调整组件内间距，NUM_10 = 10
102. playButtonColumn->SetWidth(NUM_300); // NUM_300 = 300
103. // 设置animator播放按钮
104. auto playButton = std::make_shared<ArkUIButtonNode>();
105. playButton->SetButtonLabel("play");
106. playButton->RegisterNodeEvent(playButton->GetHandle(), NODE_ON_CLICK, NUM_4, nullptr);
107. auto onTouchPlay = [](ArkUI_NodeEvent *event) {
108. // 点击button按钮时触发该逻辑，NUM_4 = 4
109. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_4) {
110. OH_ArkUI_Animator_Play(animatorHandle);
111. }
112. };
113. playButton->RegisterNodeEventReceiver(onTouchPlay);
114. // 设置animator结束按钮
115. auto finishButton = std::make_shared<ArkUIButtonNode>();
116. finishButton->SetButtonLabel("finish");
117. finishButton->RegisterNodeEvent(finishButton->GetHandle(), NODE_ON_CLICK, NUM_5, nullptr); // NUM_5 = 5
118. auto onTouchFinish = [](ArkUI_NodeEvent *event) {
119. // 点击button按钮时触发该逻辑，NUM_5 = 5
120. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_5) {
121. OH_ArkUI_Animator_Finish(animatorHandle);
122. }
123. };
124. finishButton->RegisterNodeEventReceiver(onTouchFinish);
125. // 创建容器，用于存放resetButton按键
126. auto resetButtonColumn = std::make_shared<ArkUIColumnNode>();
127. resetButtonColumn->SetPadding(NUM_10, false); // 设置布局格式，调整组件内间距，NUM_10 = 10
128. resetButtonColumn->SetWidth(NUM_300); // NUM_300 = 300
129. // 设置animator更新按钮
130. auto resetButton = std::make_shared<ArkUIButtonNode>();
131. resetButton->SetButtonLabel("reset");
132. resetButton->RegisterNodeEvent(resetButton->GetHandle(), NODE_ON_CLICK, NUM_6, nullptr); // NUM_6 = 6
133. auto onTouchReset = [](ArkUI_NodeEvent *event) {
134. // 点击button按钮时触发该逻辑，NUM_6 = 6
135. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_6) {
136. static ArkUI_AnimatorOption *option =  OH_ArkUI_AnimatorOption_Create(NUM_0); // Animator动画状态数
137. OH_ArkUI_AnimatorOption_SetDuration(option, NUM_1000); // NUM_1000 = 1000
138. OH_ArkUI_AnimatorOption_SetDelay(option, NUM_0);
139. OH_ArkUI_AnimatorOption_SetIterations(option, NUM_4); // NUM_4 = 4
140. // 根据实际业务需求选择下述两种曲线，设置OH_ArkUI_AnimatorOption_SetCurve
141. auto curve = OH_ArkUI_Curve_CreateCurveByType(ARKUI_CURVE_EASE); // 动画以低速开始，然后加快，在结束前变慢
142. auto stepsCurve = OH_ArkUI_Curve_CreateStepsCurve(NUM_20, true); // 构造阶梯曲线对象，NUM_20 = 20
143. OH_ArkUI_AnimatorOption_SetCurve(option, curve);
144. OH_ArkUI_AnimatorOption_SetBegin(option, NUM_200); // NUM_200 = 200
145. OH_ArkUI_AnimatorOption_SetEnd(option, NUM_100); // NUM_100 = 100
146. OH_ArkUI_AnimatorOption_RegisterOnFrameCallback(option, nullptr, [](ArkUI_AnimatorOnFrameEvent *event)
147. {
148. OH_ArkUI_AnimatorOnFrameEvent_GetUserData(event); // 获取动画事件对象中的用户自定义对象
149. auto value = OH_ArkUI_AnimatorOnFrameEvent_GetValue(event); // 获取动画事件对象中的当前进度
150. g_animator_button->SetWidth(value);
151. });
152. OH_ArkUI_Animator_ResetAnimatorOption(animatorHandle, option);
153. }
154. };
155. resetButton->RegisterNodeEventReceiver(onTouchReset);
156. // 设置animator暂停按钮
157. auto pauseButton = std::make_shared<ArkUIButtonNode>();
158. pauseButton->SetButtonLabel("pause");
159. pauseButton->RegisterNodeEvent(pauseButton->GetHandle(), NODE_ON_CLICK, NUM_7, nullptr); // NUM_7 = 7
160. auto onTouchPause = [](ArkUI_NodeEvent *event) {
161. // 点击button按钮时触发该逻辑，NUM_7 = 7
162. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_7) {
163. OH_ArkUI_Animator_Pause(animatorHandle);
164. }
165. };
166. pauseButton->RegisterNodeEventReceiver(onTouchPause);
167. // 创建容器，用于存放cancelButton按键
168. auto cancelButtonColumn = std::make_shared<ArkUIColumnNode>();
169. cancelButtonColumn->SetPadding(NUM_10, false); // 设置布局格式，调整组件内间距，NUM_10 = 10
170. cancelButtonColumn->SetWidth(NUM_300); // NUM_300 = 300
171. // 设置animator取消按钮
172. auto cancelButton = std::make_shared<ArkUIButtonNode>();
173. cancelButton->SetButtonLabel("cancel");
174. cancelButton->RegisterNodeEvent(cancelButton->GetHandle(), NODE_ON_CLICK, NUM_8, nullptr); // NUM_8 = 8
175. auto onTouchCancel = [](ArkUI_NodeEvent *event) {
176. // 点击button按钮时触发该逻辑，NUM_8 = 8
177. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_8) {
178. OH_ArkUI_Animator_Cancel(animatorHandle);
179. }
180. };
181. cancelButton->RegisterNodeEventReceiver(onTouchCancel);
182. // 设置animator以相反的顺序播放按钮
183. auto reverseButton = std::make_shared<ArkUIButtonNode>();
184. reverseButton->SetButtonLabel("reverse");
185. reverseButton->RegisterNodeEvent(reverseButton->GetHandle(), NODE_ON_CLICK, NUM_9, nullptr);
186. auto onTouchReverse = [](ArkUI_NodeEvent *event) {
187. // 点击button按钮时触发该逻辑，NUM_9 = 9
188. if (OH_ArkUI_NodeEvent_GetTargetId(event) == NUM_9) {
189. OH_ArkUI_Animator_Reverse(animatorHandle);
190. }
191. };
192. reverseButton->RegisterNodeEventReceiver(onTouchReverse);
193. // 将button挂载在column上，返回column节点
194. column->AddChild(g_animator_text);
195. column->AddChild(textNode);
196. column->AddChild(button);
197. buttoColumn->AddChild(createButton);
198. playButtonColumn->AddChild(playButton);
199. buttoColumn->AddChild(playButtonColumn);
200. buttoColumn->AddChild(finishButton);
201. resetButtonColumn->AddChild(resetButton);
202. buttoColumn->AddChild(resetButtonColumn);
203. buttoColumn->AddChild(pauseButton);
204. cancelButtonColumn->AddChild(cancelButton);
205. buttoColumn->AddChild(cancelButtonColumn);
206. buttoColumn->AddChild(reverseButton);
207. column->AddChild(buttoColumn);
208. return column;
209. }
```

[ArkUIAnimate.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AnimationNDK/entry/src/main/cpp/ArkUIAnimate.h#L446-L656)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/aZ-8w4PjQaCHA9fDiyZyBw/zh-cn_image_0000002558604898.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052830Z&HW-CC-Expire=86400&HW-CC-Sign=C1E2976CEE2AA1292FD021427269F514E6A34F9AB09D016BCC0F3C982B2DBF52)
