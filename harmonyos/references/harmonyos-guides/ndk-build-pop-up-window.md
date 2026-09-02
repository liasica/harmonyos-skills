---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-pop-up-window
title: 构建弹窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建弹窗
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2b565810b310bc4713bed510c1c251009da4f78eeaf55fca0ac78b5e3e001513
---

可以通过创建弹窗控制器和创建自定义弹窗的内容对象两种方法显示自定义弹窗，设置其样式和内容。

[通过创建弹窗控制器显示自定义弹窗](ndk-build-pop-up-window.md#通过创建弹窗控制器显示自定义弹窗)：在命名为ArkUI\_NativeDialogAPI\_x （x表示版本）的结构体中，定义了弹窗接口集合，用于实现各种弹窗控制。从API version 12开始支持，使用方式可以参考[openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)接口。

[通过创建自定义弹窗的内容对象显示自定义弹窗](ndk-build-pop-up-window.md#通过创建自定义弹窗的内容对象显示自定义弹窗)：该方式下的弹窗接口在[native\_dialog.h](../harmonyos-references/capi-native-dialog-h.md#函数)的函数中定义。从API version 19开始支持，使用方式可以参考[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口。

**说明** 

* [OH\_ArkUI\_QueryModuleInterfaceByName](../harmonyos-references/capi-native-interface-h.md#oh_arkui_querymoduleinterfacebyname)用于获取指定类型的Native模块接口集合，可以通过其返回ArkUI\_NativeDialogHandle类型的数据调用Native模块中的接口。

## 创建和销毁自定义弹窗

### 通过创建弹窗控制器显示自定义弹窗

* 创建弹窗控制器：

  [ArkUI\_NativeDialogHandle](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h.md)表示指向弹窗控制器的指针，可以通过调用[ArkUI\_NativeDialogAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1.md)的[create](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1.md#create)接口创建一个弹窗控制器。

  该方法返回ArkUI\_NativeDialogHandle类型的数据。

  ```
  ArkUI_NativeDialogHandle g_dialogController = nullptr;
  // ···
      ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
          OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
      if (!g_dialogController) {
          g_dialogController = dialogAPI->create();
      }
  ```
* 当不再需要弹窗操作时，需要主动调用[dispose](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1.md#dispose)接口销毁弹窗控制器对象。

  ```
  ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
      OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
  dialogAPI->dispose(g_dialogController);
  g_dialogController = nullptr;
  ```

### 通过创建自定义弹窗的内容对象显示自定义弹窗

* 创建弹窗的内容对象：

  [ArkUI\_CustomDialogOptions](../harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions.md)自定义弹窗的内容对象，可以通过调用[OH\_ArkUI\_CustomDialog\_CreateOptions](../harmonyos-references/capi-native-dialog-h.md#oh_arkui_customdialog_createoptions)接口创建一个自定义弹窗的内容对象。

  该方法返回ArkUI\_CustomDialogOptions类型的指针。

  ```
  ArkUI_CustomDialogOptions* g_dialogOptions = nullptr;
  // ···
      auto textNode = std::make_shared<NativeModule::ArkUITextNode>();
      if (!g_dialogOptions) {
          g_dialogOptions = OH_ArkUI_CustomDialog_CreateOptions(textNode->GetHandle());
      }
  ```

  **说明** 

  ArkUITextNode的声明方式可以查看[ArkUINode.h](ndk-access-the-arkts-page.md#示例)文件中的实现文本组件。
* 当不再需要弹窗操作时，需要主动调用[OH\_ArkUI\_CustomDialog\_DisposeOptions](../harmonyos-references/capi-native-dialog-h.md#oh_arkui_customdialog_disposeoptions)接口销毁弹窗内容对象。

  ```
  OH_ArkUI_CustomDialog_DisposeOptions(g_dialogOptions);
  ```

## 设置弹窗样式

可以设置弹窗对齐方式、偏移量，弹窗背板圆角弧度、背景色、蒙层颜色以及区域等。

1. 创建弹窗内容节点。

   **说明** 

   此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2开始，新建工程或者模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOptions > resOptions > copyCodeResource > enable设置为true，详见[resOptions](ide-hvigor-build-profile.md#section754823013348)中相关介绍。

   ```
   ArkUI_NodeHandle CreateDialogContent()
   {
       ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
           OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
       ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
       ArkUI_NumberValue textWidthValue[] = {{.f32 = 300}};
       ArkUI_AttributeItem textWidthItem = {.value = textWidthValue,
                                            .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text, NODE_WIDTH, &textWidthItem);
       ArkUI_NumberValue textHeightValue[] = {{.f32 = 300}};
       ArkUI_AttributeItem textHeightItem = {.value = textHeightValue,
                                             .size = sizeof(textHeightValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text, NODE_HEIGHT, &textHeightItem);
       ArkUI_NodeHandle span = nodeAPI->createNode(ARKUI_NODE_SPAN);
       ArkUI_AttributeItem spanItem = {.string = "This is a dialog box"};
       nodeAPI->setAttribute(span, NODE_SPAN_CONTENT, &spanItem);
       ArkUI_NodeHandle imageSpan = nodeAPI->createNode(ARKUI_NODE_IMAGE_SPAN);
       // 图片src/main/ets/pages/common/sky.jpg需要替换为开发者所需的资源文件
       ArkUI_AttributeItem imageSpanItem = {.string = "/pages/common/sky.jpg"};
       nodeAPI->setAttribute(imageSpan, NODE_IMAGE_SPAN_SRC, &imageSpanItem);
       ArkUI_NumberValue imageSpanWidthValue[] = {{.f32 = 300}};
       ArkUI_AttributeItem imageSpanWidthItem = {.value = imageSpanWidthValue,
                                                 .size = sizeof(imageSpanWidthValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(imageSpan, NODE_WIDTH, &imageSpanWidthItem);
       ArkUI_NumberValue imageSpanHeightValue[] = {{.f32 = 200}};
       ArkUI_AttributeItem imageSpanHeightItem = {.value = imageSpanHeightValue,
                                                  .size = sizeof(imageSpanHeightValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(imageSpan, NODE_HEIGHT, &imageSpanHeightItem);
       nodeAPI->addChild(text, span);
       nodeAPI->addChild(text, imageSpan);
       return text;
   }
   ```
2. 以下介绍两种控制弹窗样式的方式，弹窗接口请参考[native\_dialog.h](../harmonyos-references/capi-native-dialog-h.md)。

   * 通过controller控制弹窗样式。

     ```
     void ShowDialog()
     {
         ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
             OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
         if (!g_dialogController) {
             g_dialogController = dialogAPI->create();
         }
         auto contentNode = CreateDialogContent();
         dialogAPI->setContent(g_dialogController, contentNode);
         dialogAPI->setContentAlignment(g_dialogController, static_cast<int32_t>(ARKUI_ALIGNMENT_BOTTOM), 0, 0);
         dialogAPI->setBackgroundColor(g_dialogController, 0xffffffff);
         dialogAPI->setCornerRadius(g_dialogController, 6.0f, 6.0f, 6.0f, 6.0f);
         dialogAPI->setModalMode(g_dialogController, false);
         dialogAPI->setAutoCancel(g_dialogController, true);
         dialogAPI->show(g_dialogController, false);
     }
     ```
   * 通过dialogOptions控制弹窗样式。

     ```
     int32_t g_id = 0;
     void OpenDialogCallBack(int32_t dialogId)
     {
         g_id = dialogId;
     }

     void OpenCustomDialog()
     {
         auto contentNode = CreateDialogContent();
         if (!g_dialogOptions) {
             g_dialogOptions = OH_ArkUI_CustomDialog_CreateOptions(contentNode);
         }
         OH_ArkUI_CustomDialog_SetAlignment(g_dialogOptions, static_cast<int32_t>(ARKUI_ALIGNMENT_BOTTOM), 0, 0);
         OH_ArkUI_CustomDialog_SetBackgroundColor(g_dialogOptions, 0xffffffff);
         OH_ArkUI_CustomDialog_SetCornerRadius(g_dialogOptions, 6.0f, 6.0f, 6.0f, 6.0f);
         OH_ArkUI_CustomDialog_SetModalMode(g_dialogOptions, false);
         OH_ArkUI_CustomDialog_SetAutoCancel(g_dialogOptions, true);
         OH_ArkUI_CustomDialog_SetBorderStyle(g_dialogOptions, ARKUI_BORDER_STYLE_SOLID,
                                              ARKUI_BORDER_STYLE_SOLID, ARKUI_BORDER_STYLE_SOLID, ARKUI_BORDER_STYLE_SOLID);
         OH_ArkUI_CustomDialog_OpenDialog(g_dialogOptions, OpenDialogCallBack);
     }
     ```
3. 弹窗关闭方式。

   * 通过controller关闭弹窗。

     ```
     void CloseDialog()
     {
         ArkUI_NativeDialogAPI_1 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_1 *>(
             OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_1"));
         dialogAPI->close(g_dialogController);
     }
     ```
   * 通过dialogOptions关闭弹窗。

     ```
     void CloseCustomDialog()
     {
         OH_ArkUI_CustomDialog_CloseDialog(g_id);
     }
     ```

## 弹窗的交互

可创建交互页面，打开或关闭弹窗。

1. 创建可交互界面，点击Button后弹窗。其中获取与使用ArkUI\_NodeContentHandle类型节点可参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

   ```
   constexpr int32_t BUTTON_CLICK_ID = 1;
   ArkUI_NodeHandle g_buttonNode = nullptr;

   void MainViewMethod(ArkUI_NodeContentHandle handle)
   {
       ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
           OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
       ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
       ArkUI_NumberValue widthValue[] = {{.f32 = 300}};
       ArkUI_AttributeItem widthItem = {.value = widthValue, .size = sizeof(widthValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(column, NODE_WIDTH, &widthItem);
       ArkUI_NumberValue heightValue[] = {{.f32 = 300}};
       ArkUI_AttributeItem heightItem = {.value = heightValue, .size = sizeof(heightValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(column, NODE_HEIGHT, &heightItem);
       
       g_buttonNode = nodeAPI->createNode(ARKUI_NODE_BUTTON);
       ArkUI_NumberValue buttonWidthValue[] = {{.f32 = 200}};
       ArkUI_AttributeItem buttonWidthItem = {.value = buttonWidthValue,
                                              .size = sizeof(buttonWidthValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(g_buttonNode, NODE_WIDTH, &buttonWidthItem);
       ArkUI_NumberValue buttonHeightValue[] = {{.f32 = 50}};
       ArkUI_AttributeItem buttonHeightItem = {.value = buttonHeightValue,
                                               .size = sizeof(buttonHeightValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(g_buttonNode, NODE_HEIGHT, &buttonHeightItem);
       ArkUI_AttributeItem labelItem = {.string = "Click Dialog Box"};
       nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
       ArkUI_NumberValue buttonTypeValue[] = {{.i32 = static_cast<int32_t>(ARKUI_BUTTON_TYPE_NORMAL)}};
       ArkUI_AttributeItem buttonTypeItem = {.value = buttonTypeValue,
                                             .size = sizeof(buttonTypeValue) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_TYPE, &buttonTypeItem);
       nodeAPI->registerNodeEvent(g_buttonNode, NODE_ON_CLICK, BUTTON_CLICK_ID, nullptr);
       nodeAPI->addNodeEventReceiver(g_buttonNode, OnButtonClicked);
       nodeAPI->addChild(column, g_buttonNode);
       OH_ArkUI_NodeContent_AddNode(handle, column);
   }
   ```
2. 创建Button事件的回调函数，当Button被点击时触发弹窗显示或关闭。

   * 触发controller弹窗。

     ```
     bool g_isShown = false;

     void OnButtonClicked(ArkUI_NodeEvent *event)
     {
         if (!event || !g_buttonNode) {
             return;
         }
         auto eventId = OH_ArkUI_NodeEvent_GetTargetId(event);
         if (eventId == BUTTON_CLICK_ID) {
             ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
                 OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
             if (g_isShown) {
                 g_isShown = false;
                 ArkUI_AttributeItem labelItem = {.string = "Show Dialog Box"};
                 nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
                 CloseDialog();
             } else {
                 g_isShown = true;
                 ArkUI_AttributeItem labelItem = {.string = "Close Dialog Box"};
                 nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
                 ShowDialog();
             }
         }
     }
     ```
   * 触发dialogOptions弹窗。

     ```
     void OnButtonClicked(ArkUI_NodeEvent *event)
     {
         if (!event || !g_buttonNode) {
             return;
         }
         auto eventId = OH_ArkUI_NodeEvent_GetTargetId(event);
         if (eventId == BUTTON_CLICK_ID) {
             ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
                 OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
             if (g_isShown) {
                 g_isShown = false;
                 ArkUI_AttributeItem labelItem = {.string = "Show Dialog Box"};
                 nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
                 CloseCustomDialog();
             } else {
                 g_isShown = true;
                 ArkUI_AttributeItem labelItem = {.string = "Close Dialog Box"};
                 nodeAPI->setAttribute(g_buttonNode, NODE_BUTTON_LABEL, &labelItem);
                 OpenCustomDialog();
             }
         }
     }
     ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/LRYC-JpyTae35vgJsAQK3w/zh-cn_image_0000002736313003.gif)

## 弹窗的生命周期

从API version 19开始，弹窗显示和关闭前后，存在四个生命周期：[registerOnWillAppear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registeronwillappear)、[registerOnDidAppear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registerondidappear)、[registerOnWillDisappear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registeronwilldisappear)、[registerOnDidDisappear](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md#registerondiddisappear)。

这些生命周期方法需要在调用show方法之前调用，生命周期的时序如下：

registerOnWillAppear -> 弹窗显示动画开始 -> 弹窗显示动画结束 -> registerOnDidAppear -> 弹窗显示完成 ->registerOnWillDisappear -> 弹窗关闭动画开始 -> 弹窗关闭动画结束 -> registerOnDidDisappear -> 弹窗关闭完成。

创建一个弹窗，弹窗显示和关闭时会触发生命周期的回调函数。其中 ArkUI\_NodeContentHandle 类型节点的获取与使用可参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

**说明** 

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2开始，新建工程或者模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOptions > resOptions > copyCodeResource > enable设置为true，详见[resOptions](ide-hvigor-build-profile.md#section754823013348)中相关介绍。

```
ArkUI_NodeHandle CreateDialogContent()
{
    ArkUI_NativeNodeAPI_1 *nodeAPI = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
        OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
    ArkUI_NodeHandle text = nodeAPI->createNode(ARKUI_NODE_TEXT);
    ArkUI_NumberValue textWidthValue[] = {{.f32 = 300}};
    ArkUI_AttributeItem textWidthItem = {.value = textWidthValue,
                                         .size = sizeof(textWidthValue) / sizeof(ArkUI_NumberValue)};
    nodeAPI->setAttribute(text, NODE_WIDTH, &textWidthItem);
    ArkUI_NumberValue textHeightValue[] = {{.f32 = 300}};
    ArkUI_AttributeItem textHeightItem = {.value = textHeightValue,
                                          .size = sizeof(textHeightValue) / sizeof(ArkUI_NumberValue)};
    nodeAPI->setAttribute(text, NODE_HEIGHT, &textHeightItem);
    ArkUI_NodeHandle span = nodeAPI->createNode(ARKUI_NODE_SPAN);
    ArkUI_AttributeItem spanItem = {.string = "This is a dialog box"};
    nodeAPI->setAttribute(span, NODE_SPAN_CONTENT, &spanItem);
    ArkUI_NodeHandle imageSpan = nodeAPI->createNode(ARKUI_NODE_IMAGE_SPAN);
    // 图片src/main/ets/pages/common/sky.jpg需要替换为开发者所需的资源文件
    ArkUI_AttributeItem imageSpanItem = {.string = "/pages/common/sky.jpg"};
    nodeAPI->setAttribute(imageSpan, NODE_IMAGE_SPAN_SRC, &imageSpanItem);
    ArkUI_NumberValue imageSpanWidthValue[] = {{.f32 = 300}};
    ArkUI_AttributeItem imageSpanWidthItem = {.value = imageSpanWidthValue,
                                              .size = sizeof(imageSpanWidthValue) / sizeof(ArkUI_NumberValue)};
    nodeAPI->setAttribute(imageSpan, NODE_WIDTH, &imageSpanWidthItem);
    ArkUI_NumberValue imageSpanHeightValue[] = {{.f32 = 200}};
    ArkUI_AttributeItem imageSpanHeightItem = {.value = imageSpanHeightValue,
                                               .size = sizeof(imageSpanHeightValue) / sizeof(ArkUI_NumberValue)};
    nodeAPI->setAttribute(imageSpan, NODE_HEIGHT, &imageSpanHeightItem);
    nodeAPI->addChild(text, span);
    nodeAPI->addChild(text, imageSpan);
    return text;
}

void OnWillAppearCallBack(void* userdata)
{
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnWillAppearCallBack");
}

void OnDidAppearCallBack(void* userdata)
{
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnDidAppearCallBack");
}

void OnWillDisappearCallBack(void* userdata)
{
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnWillDisappearCallBack");
}

void OnDidDisappearCallBack(void* userdata)
{
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "CustomDialogContentTest", "OnDidDisappearCallBack");
}

void ShowDialog()
{
    ArkUI_NativeDialogAPI_3 *dialogAPI = reinterpret_cast<ArkUI_NativeDialogAPI_3 *>(
        OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_DIALOG, "ArkUI_NativeDialogAPI_3"));
    if (!g_dialogController) {
        g_dialogController = dialogAPI->nativeDialogAPI1.create();
    }
    auto contentNode = CreateDialogContent();
    dialogAPI->nativeDialogAPI1.setContent(g_dialogController, contentNode);
    dialogAPI->nativeDialogAPI1.setAutoCancel(g_dialogController, true);
    dialogAPI->registerOnWillAppear(g_dialogController, nullptr, OnWillAppearCallBack);
    dialogAPI->registerOnDidAppear(g_dialogController, nullptr, OnDidAppearCallBack);
    dialogAPI->registerOnWillDisappear(g_dialogController, nullptr, OnWillDisappearCallBack);
    dialogAPI->registerOnDidDisappear(g_dialogController, nullptr, OnDidDisappearCallBack);
    dialogAPI->nativeDialogAPI1.show(g_dialogController, false);
}
```
