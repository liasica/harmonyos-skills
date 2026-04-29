---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-pop-up-window
title: 构建弹窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建弹窗
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:786477fa0370912661b901cc4a8a2b07854492ab76f6da6390f3bd8c51438fab
---

可以通过创建弹窗控制器和创建自定义弹窗的内容对象两种方法显示自定义弹窗，设置其样式和内容。

[通过创建弹窗控制器显示自定义弹窗](ndk-build-pop-up-window.md#通过创建弹窗控制器显示自定义弹窗)：在命名为ArkUI\_NativeDialogAPI\_x （x表示版本）的结构体中，定义了弹窗接口集合，用于实现各种弹窗控制。

[通过创建自定义弹窗的内容对象显示自定义弹窗](ndk-build-pop-up-window.md#通过创建自定义弹窗的内容对象显示自定义弹窗)：该方式下的弹窗接口在[native\_dialog.h](../harmonyos-references/capi-native-dialog-h.md#函数)的函数中定义。

说明

* 通过创建弹窗控制器来显示自定义弹窗，使用方式可以参考[openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)接口。
* 通过创建自定义弹窗的内容对象来显示自定义弹窗，使用方式可以参考[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口。
* [OH\_ArkUI\_QueryModuleInterfaceByName](../harmonyos-references/capi-native-interface-h.md#oh_arkui_querymoduleinterfacebyname)用于获取指定类型的Native模块接口集合，可以通过其返回ArkUI\_NativeDialogHandle类型的数据调用Native模块中的接口。

## 创建和销毁自定义弹窗

### 通过创建弹窗控制器显示自定义弹窗

* 创建弹窗控制器：

  [ArkUI\_NativeDialogHandle](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h.md)表示指向弹窗控制器的指针，可以通过调用[ArkUI\_NativeDialogAPI\_x](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1.md)的[create](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1.md#create)接口创建一个弹窗控制器。

  该方法返回ArkUI\_NativeDialogHandle类型的数据。

  ```
  1. ArkUI_NativeDialogHandle g_dialogController = nullptr;
  2. // ···
  3. ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
  4. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
  5. if (!g_dialogController) {
  6. g_dialogController = dialogAPI->create();
  7. }
  ```

  [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L38-L50)
* 当不再需要弹窗操作时，需要主动调用[dispose](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1.md#dispose)接口销毁弹窗控制器对象。

  ```
  1. ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
  2. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
  3. dialogAPI->dispose(g_dialogController);
  4. g_dialogController = nullptr;
  ```

  [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L181-L186)

### 通过创建自定义弹窗的内容对象显示自定义弹窗

* 创建弹窗的内容对象：

  [ArkUI\_CustomDialogOptions](../harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions.md)自定义弹窗的内容对象，可以通过调用[OH\_ArkUI\_CustomDialog\_CreateOptions](../harmonyos-references/capi-native-dialog-h.md#oh_arkui_customdialog_createoptions)接口创建一个自定义弹窗的内容对象。

  该方法返回ArkUI\_CustomDialogOptions类型的指针。

  ```
  1. ArkUI_CustomDialogOptions* g_dialogOptions = nullptr;
  2. // ···
  3. auto textNode = std::make_shared<NativeModule::ArkUITextNode>();
  4. if (!g_dialogOptions) {
  5. g_dialogOptions = OH_ArkUI_CustomDialog_CreateOptions(textNode->GetHandle());
  6. }
  ```

  [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L396-L406)

  说明

  ArkUITextNode的声明方式可以查看[ArkUINode.h](ndk-access-the-arkts-page.md#示例)文件中的实现文本组件。
* 当不再需要弹窗操作时，需要主动调用[OH\_ArkUI\_CustomDialog\_DisposeOptions](../harmonyos-references/capi-native-dialog-h.md#oh_arkui_customdialog_disposeoptions)接口销毁弹窗控制器对象。

  ```
  1. OH_ArkUI_CustomDialog_DisposeOptions(g_dialogOptions);
  ```

  [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L486-L488)

## 设置弹窗样式

可以设置弹窗对齐方式、偏移量，弹窗背板圆角弧度、背景色、蒙层颜色以及区域等。

1. 创建弹窗内容节点。

   说明

   此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2开始，新建工程或者模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOptions > resOptions > copyCodeResource > enable设置为true，详见[resOptions](ide-hvigor-build-profile.md#table1476161719356)中相关介绍。

   ```
   1. ArkUI_NodeHandle CreateDialogContent()
   2. {
   3. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   4. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   5. ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
   6. ArkUI_NumberValue textWidthValue[] = {{.f32 = 300}};
   7. ArkUI_AttributeItem textWidthItem = {.value = textWidthValue,
   8. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
   9. nodeAPI->setAttribute(text, NODE_WIDTH, &textWidthItem);
   10. ArkUI_NumberValue textHeightValue[] = {{.f32 = 300}};
   11. ArkUI_AttributeItem textHeightItem = {.value = textHeightValue,
   12. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
   13. nodeAPI->setAttribute(text, NODE_HEIGHT, &textHeightItem);
   14. ArkUI_NodeHandle span = nodeAPI->createNode(ARKUI_NODE_SPAN);
   15. ArkUI_AttributeItem spanItem = {.string = "This is a dialog box"};
   16. nodeAPI->setAttribute(span, NODE_SPAN_CONTENT, &spanItem);
   17. ArkUI_NodeHandle imageSpan = nodeAPI->createNode(ARKUI_NODE_IMAGE_SPAN);
   18. // 图片src/main/ets/pages/common/sky.jpg需要替换为开发者所需的资源文件
   19. ArkUI_AttributeItem imageSpanItem = {.string = "/pages/common/sky.jpg"};
   20. nodeAPI->setAttribute(imageSpan, NODE_IMAGE_SPAN_SRC, &imageSpanItem);
   21. ArkUI_NumberValue imageSpanWidthValue[] = {{.f32 = 300}};
   22. ArkUI_AttributeItem imageSpanWidthItem = {.value = imageSpanWidthValue,
   23. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
   24. nodeAPI->setAttribute(imageSpan, NODE_WIDTH, &imageSpanWidthItem);
   25. ArkUI_NumberValue imageSpanHeightValue[] = {{.f32 = 200}};
   26. ArkUI_AttributeItem imageSpanHeightItem = {.value = imageSpanHeightValue,
   27. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
   28. nodeAPI->setAttribute(imageSpan, NODE_HEIGHT, &imageSpanHeightItem);
   29. nodeAPI->addChild(text, span);
   30. nodeAPI->addChild(text, imageSpan);
   31. return text;
   32. }
   ```

   [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L101-L134)
2. 以下介绍两种控制弹窗样式的方式，弹窗接口请参考[native\_dialog.h](../harmonyos-references/capi-native-dialog-h.md)。

   * 通过controller控制弹窗样式。

     ```
     1. void ShowDialog()
     2. {
     3. ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
     4. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
     5. if (!g_dialogController) {
     6. g_dialogController = dialogAPI->create();
     7. }
     8. auto contentNode = CreateDialogContent();
     9. dialogAPI->setContent(g_dialogController, contentNode);
     10. dialogAPI->setContentAlignment(g_dialogController, static_cast<int32_t>(ARKUI_ALIGNMENT_BOTTOM), 0, 0);
     11. dialogAPI->setBackgroundColor(g_dialogController, 0xffffffff);
     12. dialogAPI->setCornerRadius(g_dialogController, 6.0f, 6.0f, 6.0f, 6.0f);
     13. dialogAPI->setModalMode(g_dialogController, false);
     14. dialogAPI->setAutoCancel(g_dialogController, true);
     15. dialogAPI->show(g_dialogController, false);
     16. }
     ```

     [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L41-L60)
   * 通过dialogOptions控制弹窗样式。

     ```
     1. int32_t g_id = 0;
     2. void OpenDialogCallBack(int32_t dialogId)
     3. {
     4. g_id = dialogId;
     5. }

     7. void OpenCustomDialog()
     8. {
     9. auto contentNode = CreateDialogContent();
     10. if (!g_dialogOptions) {
     11. g_dialogOptions = OH_ArkUI_CustomDialog_CreateOptions(contentNode);
     12. }
     13. OH_ArkUI_CustomDialog_SetAlignment(g_dialogOptions, static_cast<int32_t>(ARKUI_ALIGNMENT_BOTTOM), 0, 0);
     14. OH_ArkUI_CustomDialog_SetBackgroundColor(g_dialogOptions, 0xffffffff);
     15. OH_ArkUI_CustomDialog_SetCornerRadius(g_dialogOptions, 6.0f, 6.0f, 6.0f, 6.0f);
     16. OH_ArkUI_CustomDialog_SetModalMode(g_dialogOptions, false);
     17. OH_ArkUI_CustomDialog_SetAutoCancel(g_dialogOptions, true);
     18. OH_ArkUI_CustomDialog_SetBorderStyle(g_dialogOptions, ARKUI_BORDER_STYLE_SOLID,
     19. ARKUI_BORDER_STYLE_SOLID, ARKUI_BORDER_STYLE_SOLID, ARKUI_BORDER_STYLE_SOLID);
     20. OH_ArkUI_CustomDialog_OpenDialog(g_dialogOptions, OpenDialogCallBack);
     21. }
     ```

     [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L257-L279)
3. 弹窗关闭方式。

   * 通过controller关闭弹窗。

     ```
     1. void CloseDialog()
     2. {
     3. ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
     4. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
     5. dialogAPI->close(g_dialogController);
     6. }
     ```

     [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L136-L143)
   * 通过dialogOptions关闭弹窗。

     ```
     1. void CloseCustomDialog()
     2. {
     3. OH_ArkUI_CustomDialog_CloseDialog(g_id);
     4. }
     ```

     [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L281-L286)

## 弹窗的交互

可创建交互页面，打开或关闭弹窗。

1. 创建可交互界面，点击Button后弹窗。其中获取与使用ArkUI\_NodeContentHandle类型节点可参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

   ```
   1. constexpr int32_t BUTTON_CLICK_ID = 1;
   2. ArkUI_NodeHandle g_buttonNode = nullptr;

   4. void MainViewMethod(ArkUI_NodeContentHandle handle)
   5. {
   6. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
   7. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
   8. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   9. ArkUI_NumberValue widthValue[] = {{.f32 = 300}};
   10. ArkUI_AttributeItem widthItem = {.value = widthValue, .size = sizeof(widthValue) / sizeof(ArkUI_NumberValue)};
   11. nodeAPI->setAttribute(column, NODE_WIDTH, &widthItem);
   12. ArkUI_NumberValue heightValue[] = {{.f32 = 300}};
   13. ArkUI_AttributeItem heightItem = {.value = heightValue, .size = sizeof(heightValue) / sizeof(ArkUI_NumberValue)};
   14. nodeAPI->setAttribute(column, NODE_HEIGHT, &heightItem);

   16. g_buttonNode = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   17. ArkUI_NumberValue buttonWidthValue[] = {{.f32 = 200}};
   18. ArkUI_AttributeItem buttonWidthItem = {.value = buttonWidthValue,
   19. .size = sizeof(buttonWidthValue) / sizeof(ArkUI_NumberValue)};
   20. nodeAPI->setAttribute(g_buttonNode, NODE_WIDTH, &buttonWidthItem);
   21. ArkUI_NumberValue buttonHeightValue[] = {{.f32 = 50}};
   22. ArkUI_AttributeItem buttonHeightItem = {.value = buttonHeightValue,
   23. .size = sizeof(buttonHeightValue) / sizeof(ArkUI_NumberValue)};
   24. nodeAPI->setAttribute(g_buttonNode, NODE_HEIGHT, &buttonHeightItem);
   25. ArkUI_AttributeItem labelItem = {.string = "Click Dialog Box"};
   26. nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
   27. ArkUI_NumberValue buttonTypeValue[] = {{.i32 = static_cast<int32_t>(ARKUI_BUTTON_TYPE_NORMAL)}};
   28. ArkUI_AttributeItem buttonTypeItem = {.value = buttonTypeValue,
   29. .size = sizeof(buttonTypeValue) / sizeof(ArkUI_NumberValue)};
   30. nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_TYPE, &buttonTypeItem);
   31. nodeAPI->registerNodeEvent(g_buttonNode, NODE_ON_CLICK, BUTTON_CLICK_ID, nullptr);
   32. nodeAPI->addNodeEventReceiver(g_buttonNode, OnButtonClicked);
   33. nodeAPI->addChild(column, g_buttonNode);
   34. OH_ArkUI_NodeContent_AddNode(handle, column);
   35. }
   ```

   [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L63-L99)
2. 创建Button事件的回调函数，当Button被点击时触发弹窗显示或关闭。

   * 触发controller弹窗。

     ```
     1. bool g_isShown = false;

     3. void OnButtonClicked(ArkUI_NodeEvent *event)
     4. {
     5. if (!event || !g_buttonNode) {
     6. return;
     7. }
     8. auto eventId = OH_ArkUI_NodeEvent_GetTargetId(event);
     9. if (eventId == BUTTON_CLICK_ID) {
     10. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
     11. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
     12. if (g_isShown) {
     13. g_isShown = false;
     14. ArkUI_AttributeItem labelItem = {.string = "Show Dialog Box"};
     15. nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
     16. CloseDialog();
     17. } else {
     18. g_isShown = true;
     19. ArkUI_AttributeItem labelItem = {.string = "Close Dialog Box"};
     20. nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
     21. ShowDialog();
     22. }
     23. }
     24. }
     ```

     [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L147-L172)
   * 触发dialogOptions弹窗。

     ```
     1. void OnButtonClicked(ArkUI_NodeEvent *event)
     2. {
     3. if (!event || !g_buttonNode) {
     4. return;
     5. }
     6. auto eventId = OH_ArkUI_NodeEvent_GetTargetId(event);
     7. if (eventId == BUTTON_CLICK_ID) {
     8. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
     9. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
     10. if (g_isShown) {
     11. g_isShown = false;
     12. ArkUI_AttributeItem labelItem = {.string = "Show Dialog Box"};
     13. nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
     14. CloseCustomDialog();
     15. } else {
     16. g_isShown = true;
     17. ArkUI_AttributeItem labelItem = {.string = "Close Dialog Box"};
     18. nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
     19. OpenCustomDialog();
     20. }
     21. }
     22. }
     ```

     [nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L289-L312)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/qBpzcxAwSzSOCEGqlaoatw/zh-cn_image_0000002558604902.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052832Z&HW-CC-Expire=86400&HW-CC-Sign=A6D6101C447B23EC3E227CDE9FBE6030D3E9A2BD464F2B7CF91BA59A8B54AEFF)

## 弹窗的生命周期

从API version 19开始，弹窗显示和关闭前后，存在四个生命周期：[registerOnWillAppear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registeronwillappear)、[registerOnDidAppear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registerondidappear)、[registerOnWillDisappear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registeronwilldisappear)、[registerOnDidDisappear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registerondiddisappear)。

这些生命周期方法需要在调用show方法之前调用，生命周期的时序如下：

registerOnWillAppear -> 弹窗显示动画开始 -> 弹窗显示动画结束 -> registerOnDidAppear -> 弹窗显示完成 ->registerOnWillDisappear -> 弹窗关闭动画开始 -> 弹窗关闭动画结束 -> registerOnDidDisappear -> 弹窗关闭完成。

创建一个弹窗，弹窗显示和关闭时会触发生命周期的回调函数。其中 ArkUI\_NodeContentHandle 类型节点的获取与使用可参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2开始，新建工程或者模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOptions > resOptions > copyCodeResource > enable设置为true，详见[resOptions](ide-hvigor-build-profile.md#table1476161719356)中相关介绍。

```
1. ArkUI_NodeHandle CreateDialogContent()
2. {
3. ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
4. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
5. ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
6. ArkUI_NumberValue textWidthValue[] = {{.f32 = 300}};
7. ArkUI_AttributeItem textWidthItem = {.value = textWidthValue,
8. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
9. nodeAPI->setAttribute(text, NODE_WIDTH, &textWidthItem);
10. ArkUI_NumberValue textHeightValue[] = {{.f32 = 300}};
11. ArkUI_AttributeItem textHeightItem = {.value = textHeightValue,
12. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
13. nodeAPI->setAttribute(text, NODE_HEIGHT, &textHeightItem);
14. ArkUI_NodeHandle span = nodeAPI->createNode(ARKUI_NODE_SPAN);
15. ArkUI_AttributeItem spanItem = {.string = "This is a dialog box"};
16. nodeAPI->setAttribute(span, NODE_SPAN_CONTENT, &spanItem);
17. ArkUI_NodeHandle imageSpan = nodeAPI->createNode(ARKUI_NODE_IMAGE_SPAN);
18. // 图片src/main/ets/pages/common/sky.jpg需要替换为开发者所需的资源文件
19. ArkUI_AttributeItem imageSpanItem = {.string = "/pages/common/sky.jpg"};
20. nodeAPI->setAttribute(imageSpan, NODE_IMAGE_SPAN_SRC, &imageSpanItem);
21. ArkUI_NumberValue imageSpanWidthValue[] = {{.f32 = 300}};
22. ArkUI_AttributeItem imageSpanWidthItem = {.value = imageSpanWidthValue,
23. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
24. nodeAPI->setAttribute(imageSpan, NODE_WIDTH, &imageSpanWidthItem);
25. ArkUI_NumberValue imageSpanHeightValue[] = {{.f32 = 200}};
26. ArkUI_AttributeItem imageSpanHeightItem = {.value = imageSpanHeightValue,
27. .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
28. nodeAPI->setAttribute(imageSpan, NODE_HEIGHT, &imageSpanHeightItem);
29. nodeAPI->addChild(text, span);
30. nodeAPI->addChild(text, imageSpan);
31. return text;
32. }

34. void OnWillAppearCallBack(void* userdata)
35. {
36. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnWillAppearCallBack");
37. }

39. void OnDidAppearCallBack(void* userdata)
40. {
41. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnDidAppearCallBack");
42. }

44. void OnWillDisappearCallBack(void* userdata)
45. {
46. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnWillDisappearCallBack");
47. }

49. void OnDidDisappearCallBack(void* userdata)
50. {
51. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnDidDisappearCallBack");
52. }

54. void ShowDialog()
55. {
56. ArkUI_NativeDialogAPI_3 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_3 *>(
57. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_3"));
58. if (!g_dialogController) {
59. g_dialogController = dialogAPI->nativeDialogAPI1.create();
60. }
61. auto contentNode = CreateDialogContent();
62. dialogAPI->nativeDialogAPI1.setContent(g_dialogController, contentNode);
63. dialogAPI->nativeDialogAPI1.setAutoCancel(g_dialogController, true);
64. dialogAPI->registerOnWillAppear(g_dialogController, nullptr, OnWillAppearCallBack);
65. dialogAPI->registerOnDidAppear(g_dialogController, nullptr, OnDidAppearCallBack);
66. dialogAPI->registerOnWillDisappear(g_dialogController, nullptr, OnWillDisappearCallBack);
67. dialogAPI->registerOnDidDisappear(g_dialogController, nullptr, OnDidDisappearCallBack);
68. dialogAPI->nativeDialogAPI1.show(g_dialogController, false);
69. }
```

[nativedialogdemo.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeDialogSample/entry/src/main/cpp/customdialog/nativedialogdemo.cpp#L529-L599)
