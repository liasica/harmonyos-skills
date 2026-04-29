---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-crosslanguage
title: 设置自定义节点跨语言属性
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 设置自定义节点跨语言属性
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:600742ecd2152e8640d79163ba2394915a22492e4cbff8d85014f05435e8fccf
---

## 概述

ArkUI支持在前端使用ArkTS语言创建命令式节点，即[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点，也可以在Native侧使用C语言创建命令式节点，并且可以混合使用两类节点构建页面。

针对上述场景，ArkUI提供命令式节点跨语言属性设置功能，即使用ArkTS语言创建的命令式节点，可以在Native侧进行属性设置。使用C语言创建的节点，可以在ArkTS侧进行属性设置。

说明

下述示例中，需要先进行Native侧配置，请参考[接入ArkTS页面](ndk-access-the-arkts-page.md)完成。

## 设置和获取跨语言配置

跨语言指的是跨越ArkTS语言和C语言。跨语言配置指的是命令式节点上对于跨语言操作的权限配置。

可以通过[setCrossLanguageOptions](../harmonyos-references/js-apis-arkui-framenode.md#setcrosslanguageoptions15)与[OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_setcrosslanguageoption)接口设置当前节点的跨语言配置。如果当前节点无法修改或设置跨语言配置，则会抛出异常信息。

可以使用[getCrossLanguageOptions](../harmonyos-references/js-apis-arkui-framenode.md#getcrosslanguageoptions15)与[OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getcrosslanguageoption)接口获取当前节点的跨语言配置。

以下示例描述了如何设置和获取ArkTS命令式节点的跨语言配置。

```
1. // Index.ets
2. import { NodeController, UIContext, FrameNode, typeNode, BuilderNode } from '@kit.ArkUI';

4. @Builder
5. function insideScroll() {
6. Column() {
7. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
8. Text(item.toString())
9. .width("75%")
10. .height(50)
11. .backgroundColor(0xFFFFFF)
12. .borderRadius(15)
13. .fontSize(30)
14. .textAlign(TextAlign.Center)
15. .margin({ top: 10 })
16. }, (item: string) => item)
17. }
18. .width("100%")
19. }

21. class MyNodeController extends NodeController {
22. uiContext: UIContext | null = null;
23. rootNode: FrameNode | null = null;
24. scrollNode: FrameNode | null = null;
25. scroller: Scroller = new Scroller();

27. makeNode(uiContext: UIContext): FrameNode | null {
28. this.uiContext = uiContext;
29. this.rootNode = new FrameNode(uiContext);
30. this.rootNode.commonAttribute.width("80%").height("50%").borderWidth(2).margin(15);
31. const scroll = typeNode.createNode(uiContext, 'Scroll');
32. scroll.initialize(this.scroller).id("scroll");
33. this.scrollNode = scroll;
34. this.rootNode.appendChild(this.scrollNode);
35. const builderNode = new BuilderNode(uiContext);
36. builderNode.build(wrapBuilder(insideScroll));
37. this.scrollNode?.appendChild(builderNode.getFrameNode());
38. return this.rootNode;
39. }
40. }

42. @Entry
43. @Component
44. struct CrossLanguage {
45. myNodeController: MyNodeController = new MyNodeController()
46. @State attributeSetting: boolean = false;
47. @State getCrossLanguageOptions: string = '{"attributeSetting": false}';

49. build() {
50. Scroll() {
51. Column({ space: 15 }) {
52. Column() {
53. Scroll() {
54. Column() {
55. NodeContainer(this.myNodeController)
56. Button("setCrossLanguageOptions").margin({ bottom: 15})
57. .onClick(() => {
58. this.attributeSetting = !this.attributeSetting;
59. this.myNodeController.scrollNode?.setCrossLanguageOptions({
60. attributeSetting: this.attributeSetting
61. });
62. // 若attributeSetting为true，表示scrollNode支持通过非ArkTS语言进行属性设置，否则为不支持
63. this.getCrossLanguageOptions = JSON.stringify(this.myNodeController.scrollNode?.getCrossLanguageOptions());
64. })
65. Text("CrossLanguageOptions: " + this.getCrossLanguageOptions)
66. }
67. }.scrollBarColor(Color.Transparent)
68. }
69. .width('100%')
70. .height(350)
71. .backgroundColor(0xeeeeee)
72. .id('Part_TS')
73. }
74. .width('100%')
75. }.scrollBarColor(Color.Transparent)
76. }
77. }
```

## 跨语言设置节点属性

获取节点后，若节点的跨语言配置设置为允许属性设置，ArkTS侧可利用getAttribute接口获取修改Native节点属性的对象，Native侧可利用[setAttribute](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口修改ArkTS节点属性。

以下示例创建了ArkTS的[Scroll](../harmonyos-references/js-apis-arkui-framenode.md#scroll12)类型节点，并在Native侧修改了Scroll的属性。

1. 在ArkTS侧创建组件类型为Scroll的命令式节点。

   ```
   1. // Index.ets
   2. import nativeNode from 'libentry.so';
   3. import { NodeController, UIContext, FrameNode, typeNode, BuilderNode, NodeContent } from '@kit.ArkUI';

   5. @Builder
   6. function insideScroll() {
   7. Column() {
   8. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
   9. Text(item.toString())
   10. .width("75%")
   11. .height(50)
   12. .backgroundColor(0xFFFFFF)
   13. .borderRadius(15)
   14. .fontSize(30)
   15. .textAlign(TextAlign.Center)
   16. .margin({ top: 10 })
   17. }, (item: string) => item)
   18. }
   19. .width("100%")
   20. }

   22. class MyNodeController extends NodeController {
   23. uiContext: UIContext | null = null;
   24. rootNode: FrameNode | null = null;
   25. scrollNode: FrameNode | null = null;
   26. scroller: Scroller = new Scroller();

   28. makeNode(uiContext: UIContext): FrameNode | null {
   29. this.uiContext = uiContext;
   30. this.rootNode = new FrameNode(uiContext);
   31. this.rootNode.commonAttribute.width("80%").height("50%").borderWidth(2).margin(15);
   32. const scroll = typeNode.createNode(uiContext, 'Scroll');
   33. scroll.initialize(this.scroller).id("scroll");
   34. this.scrollNode = scroll;
   35. this.rootNode.appendChild(this.scrollNode);
   36. const builderNode = new BuilderNode(uiContext);
   37. builderNode.build(wrapBuilder(insideScroll));
   38. this.scrollNode?.appendChild(builderNode.getFrameNode());
   39. return this.rootNode;
   40. }
   41. }

   43. @Entry
   44. @Component
   45. struct CrossLanguage {
   46. private myNodeController: MyNodeController = new MyNodeController();
   47. @State attributeSetting: boolean = false;
   48. @State getCrossLanguageOptions: string = '{"attributeSetting": false}';
   49. private rootSlot = new NodeContent();

   51. aboutToAppear(): void {
   52. nativeNode.createNativeRoot(this.rootSlot);
   53. }

   55. build() {
   56. Scroll() {
   57. Column({ space: 15 }) {
   58. Column() {
   59. Scroll() {
   60. Column() {
   61. NodeContainer(this.myNodeController)
   62. Button("setCrossLanguageOptions").margin({ bottom: 15})
   63. .onClick(() => {
   64. this.attributeSetting = !this.attributeSetting;
   65. this.myNodeController.scrollNode?.setCrossLanguageOptions({
   66. attributeSetting: this.attributeSetting
   67. });
   68. // 若attributeSetting为true，表示scrollNode支持通过非ArkTS语言进行属性设置，否则为不支持
   69. this.getCrossLanguageOptions = JSON.stringify(this.myNodeController.scrollNode?.getCrossLanguageOptions());
   70. })
   71. Text("CrossLanguageOptions: " + this.getCrossLanguageOptions)
   72. }
   73. }.scrollBarColor(Color.Transparent)
   74. }
   75. .width('100%')
   76. .height(350)
   77. .backgroundColor(0xeeeeee)
   78. .id('Part_TS')

   80. Column() {
   81. ContentSlot(this.rootSlot)
   82. }
   83. .width(500)
   84. .height(400)
   85. .id('Part_C')
   86. }
   87. .width('100%')
   88. }.scrollBarColor(Color.Transparent)
   89. }
   90. }
   ```
2. 新建CrossLanguageExample.h文件，在其中获取到目标节点（该节点在ArkTS侧创建），并设置属性。

   ```
   1. // CrossLanguageExample.h
   2. #ifndef MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H
   3. #define MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H

   5. #include "ArkUINode.h"
   6. #include <hilog/log.h>

   8. namespace NativeModule {

   10. std::shared_ptr<ArkUIBaseNode> CreateCrossLanguageExample() {
   11. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

   13. // 创建根节点Scroll
   14. ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_SCROLL);
   15. ArkUI_NumberValue length_value[] = {{.f32 = 480}};
   16. ArkUI_AttributeItem length_item = {length_value, sizeof(length_value) / sizeof(ArkUI_NumberValue)};
   17. nodeAPI->setAttribute(scroll, NODE_WIDTH, &length_item);
   18. ArkUI_NumberValue length_value1[] = {{.f32 = 650}};
   19. ArkUI_AttributeItem length_item1 = {length_value1, sizeof(length_value1) / sizeof(ArkUI_NumberValue)};
   20. nodeAPI->setAttribute(scroll, NODE_HEIGHT, &length_item1);
   21. ArkUI_AttributeItem scroll_id = {.string = "Scroll_CAPI"};
   22. nodeAPI->setAttribute(scroll, NODE_ID, &scroll_id);

   24. // 创建Column
   25. ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
   26. ArkUI_NumberValue value[] = {480};
   27. ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
   28. nodeAPI->setAttribute(column, NODE_WIDTH, &item);
   29. ArkUI_NumberValue column_bc[] = {{.u32 = 0xFFF00BB}};
   30. ArkUI_AttributeItem column_item = {column_bc, 1};
   31. nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &column_item);
   32. ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
   33. nodeAPI->setAttribute(column, NODE_ID, &column_id);

   35. // 创建Text
   36. ArkUI_NodeHandle text0 = nodeAPI->createNode(ARKUI_NODE_TEXT);
   37. ArkUI_NumberValue text_width[] = {300};
   38. ArkUI_AttributeItem text_item0 = {text_width, sizeof(text_width) / sizeof(ArkUI_NumberValue)};
   39. nodeAPI->setAttribute(text0, NODE_WIDTH, &text_item0);
   40. ArkUI_NumberValue text_height[] = {50};
   41. ArkUI_AttributeItem text_item1 = {text_height, sizeof(text_height) / sizeof(ArkUI_NumberValue)};
   42. nodeAPI->setAttribute(text0, NODE_HEIGHT, &text_item1);
   43. ArkUI_AttributeItem text_item = {.string = "C设置TS创建的节点属性"};
   44. nodeAPI->setAttribute(text0, NODE_TEXT_CONTENT, &text_item);
   45. ArkUI_NumberValue margin[] = {10};
   46. ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};
   47. nodeAPI->setAttribute(text0, NODE_MARGIN, &item_margin);

   49. // 创建Row
   50. ArkUI_NodeHandle row0 = nodeAPI->createNode(ARKUI_NODE_ROW);
   51. ArkUI_NumberValue width_value[] = {{.f32=330}};
   52. ArkUI_AttributeItem width_item = {width_value, sizeof(width_value) / sizeof(ArkUI_NumberValue)};
   53. nodeAPI->setAttribute(row0, NODE_WIDTH, &width_item);
   54. nodeAPI->setAttribute(row0, NODE_HEIGHT, &text_item1);
   55. nodeAPI->setAttribute(row0, NODE_MARGIN, &item_margin);

   57. // 创建Button
   58. ArkUI_NodeHandle bt0 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   59. ArkUI_NumberValue btn_width[] = {150};
   60. ArkUI_AttributeItem btn_item0 = {btn_width, sizeof(btn_width) / sizeof(ArkUI_NumberValue)};
   61. nodeAPI->setAttribute(bt0, NODE_WIDTH, &btn_item0);
   62. nodeAPI->setAttribute(bt0, NODE_HEIGHT, &text_item1);
   63. nodeAPI->setAttribute(bt0, NODE_MARGIN, &item_margin);
   64. ArkUI_AttributeItem bt0_item = {.string = "scrollBarColor"};
   65. nodeAPI->setAttribute(bt0, NODE_BUTTON_LABEL, &bt0_item);
   66. nodeAPI->registerNodeEvent(bt0, NODE_ON_CLICK, 0, nullptr);

   68. ArkUI_NodeHandle bt1 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
   69. nodeAPI->setAttribute(bt1, NODE_WIDTH, &btn_item0);
   70. nodeAPI->setAttribute(bt1, NODE_HEIGHT, &text_item1);
   71. nodeAPI->setAttribute(bt1, NODE_MARGIN, &item_margin);
   72. ArkUI_AttributeItem bt1_item = {.string = "scrollBarWidth"};
   73. nodeAPI->setAttribute(bt1, NODE_BUTTON_LABEL, &bt1_item);
   74. nodeAPI->registerNodeEvent(bt1, NODE_ON_CLICK, 1, nullptr);

   76. // 注册事件
   77. auto onClick = [](ArkUI_NodeEvent *event) {
   78. ArkUI_NodeHandle node = OH_ArkUI_NodeEvent_GetNodeHandle(event);
   79. auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();

   81. if (OH_ArkUI_NodeEvent_GetTargetId(event) == 0) {  // scrollBarColor
   82. ArkUI_NodeHandle node_ptr = nullptr;
   83. OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("scroll", &node_ptr);
   84. try {
   85. ArkUI_NumberValue scroll_color_value[] = {{.u32 = 0xff00ff00}};
   86. ArkUI_AttributeItem scroll_color_item = {scroll_color_value, sizeof(scroll_color_value) / sizeof(ArkUI_NumberValue)};
   87. nodeAPI->setAttribute(node_ptr, NODE_SCROLL_BAR_COLOR, &scroll_color_item);
   88. } catch (...) {
   89. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample", "crossLanguage setAttribute error");
   90. }
   91. }

   93. if (OH_ArkUI_NodeEvent_GetTargetId(event) == 1) {  // scrollBarWidth
   94. ArkUI_NodeHandle node_ptr = nullptr;
   95. OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("scroll", &node_ptr);
   96. try {
   97. ArkUI_NumberValue scroll_width_value[] = {{20}};
   98. ArkUI_AttributeItem scroll_width_item = {scroll_width_value, sizeof(scroll_width_value) / sizeof(ArkUI_NumberValue)};
   99. nodeAPI->setAttribute(node_ptr, NODE_SCROLL_BAR_WIDTH, &scroll_width_item);
   100. } catch (...) {
   101. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample", "crossLanguage setAttribute error");
   102. }
   103. }
   104. };
   105. nodeAPI->registerNodeEventReceiver(onClick);

   107. // 节点添加
   108. nodeAPI->addChild(scroll, column);
   109. nodeAPI->addChild(column, text0);
   110. nodeAPI->addChild(column, row0);
   111. nodeAPI->addChild(row0, bt0);
   112. nodeAPI->addChild(row0, bt1);

   114. return std::make_shared<ArkUINode>(scroll);
   115. }
   116. } // namespace NativeModule

   118. #endif // MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H
   ```
3. 在NativeEntry.cpp中，挂载Native节点。

   ```
   1. // NativeEntry.cpp

   4. #include <arkui/native_node_napi.h>
   5. #include <js_native_api.h>
   6. #include "NativeEntry.h"
   7. #include "CrossLanguageExample.h"

   10. namespace NativeModule {

   13. napi_value CreateNativeRoot(napi_env env, napi_callback_info info) {
   14. size_t argc = 1;
   15. napi_value args[1] = {nullptr};

   18. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   21. // 获取NodeContent
   22. ArkUI_NodeContentHandle contentHandle;
   23. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   24. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   27. // 创建节点
   28. auto node = CreateCrossLanguageExample();

   31. // 保持Native侧对象到管理类中，维护生命周期。
   32. NativeEntry::GetInstance()->SetRootNode(node);
   33. return nullptr;
   34. }

   37. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info) {
   38. // 从管理类中释放Native侧对象。
   39. NativeEntry::GetInstance()->DisposeRootNode();
   40. return nullptr;
   41. }

   44. } // namespace NativeModule
   ```
4. 修改CMakeLists.txt，添加链接库。

   ```
   1. // CMakeLists.txt
   2. # the minimum version of CMake.
   3. cmake_minimum_required(VERSION 3.5.0)
   4. project(CAPI_DEMO)

   6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   8. if(DEFINED PACKAGE_FIND_FILE)
   9. include(${PACKAGE_FIND_FILE})
   10. endif()

   12. include_directories(${NATIVERENDER_ROOT_PATH}
   13. ${NATIVERENDER_ROOT_PATH}/include)

   15. add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
   16. target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so hilog_ndk.z.so)
   ```
5. 运行程序，在ArkTS侧点击按钮，设置当前attributeSetting为true，在Native侧点击按钮，设置ArkTS侧Scroll组件滚动条的颜色和粗细属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/J4AX8vFiRPmQLWnxMyUn-Q/zh-cn_image_0000002589244315.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=C3A26371351CE1FDD671DC0CEB5D2C919F90D21E14DA3D168AE205A9322C9085)

## 支持跨语言设置属性的节点类型

仅以下节点类型支持跨语言设置节点属性。

| ArkTS侧[TypedFrameNode](../harmonyos-references/js-apis-arkui-framenode.md#typedframenode12)类型 | Native侧[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)类型 | ArkTS属性获取接口 | ArkTS控制器获取/绑定接口 |
| --- | --- | --- | --- |
| [Button](../harmonyos-references/js-apis-arkui-framenode.md#button12) | ARKUI\_NODE\_BUTTON | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributebutton20) | NA |
| [Checkbox](../harmonyos-references/js-apis-arkui-framenode.md#checkbox18) | ARKUI\_NODE\_CHECKBOX | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributecheckbox20) | NA |
| [Radio](../harmonyos-references/js-apis-arkui-framenode.md#radio18) | ARKUI\_NODE\_RADIO | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeradio20) | NA |
| [Slider](../harmonyos-references/js-apis-arkui-framenode.md#slider18) | ARKUI\_NODE\_SLIDER | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeslider20) | NA |
| [Toggle](../harmonyos-references/js-apis-arkui-framenode.md#toggle18) | ARKUI\_NODE\_TOGGLE | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetoggle20) | NA |
| [Progress](../harmonyos-references/js-apis-arkui-framenode.md#progress12) | ARKUI\_NODE\_PROGRESS | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeprogress20) | NA |
| [LoadingProgress](../harmonyos-references/js-apis-arkui-framenode.md#loadingprogress12) | ARKUI\_NODE\_LOADING\_PROGRESS | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeloadingprogress20) | NA |
| [Image](../harmonyos-references/js-apis-arkui-framenode.md#image12) | ARKUI\_NODE\_IMAGE | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeimage20) | NA |
| [XComponent](../harmonyos-references/js-apis-arkui-framenode.md#xcomponent12) | ARKUI\_NODE\_XCOMPONENT | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributexcomponent20) | getController |
| [Column](../harmonyos-references/js-apis-arkui-framenode.md#column12) | ARKUI\_NODE\_COLUMN | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributecolumn20) | NA |
| [Row](../harmonyos-references/js-apis-arkui-framenode.md#row12) | ARKUI\_NODE\_ROW | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributerow20) | NA |
| [Stack](../harmonyos-references/js-apis-arkui-framenode.md#stack12) | ARKUI\_NODE\_STACK | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributestack20) | NA |
| [Flex](../harmonyos-references/js-apis-arkui-framenode.md#flex12) | ARKUI\_NODE\_FLEX | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeflex20) | NA |
| [RelativeContainer](../harmonyos-references/js-apis-arkui-framenode.md#relativecontainer12) | ARKUI\_NODE\_RELATIVE\_CONTAINER | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributerelativecontainer20) | NA |
| [Swiper](../harmonyos-references/js-apis-arkui-framenode.md#swiper12) | ARKUI\_NODE\_SWIPER | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeswiper20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerswiper20) |
| [Scroll](../harmonyos-references/js-apis-arkui-framenode.md#scroll12) | ARKUI\_NODE\_SCROLL | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributescroll15) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerscroll15) |
| [List](../harmonyos-references/js-apis-arkui-framenode.md#list12) | ARKUI\_NODE\_LIST | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributelist20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerlist20) |
| [ListItem](../harmonyos-references/js-apis-arkui-framenode.md#listitem12) | ARKUI\_NODE\_LIST\_ITEM | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributelistitem20) | NA |
| [ListItemGroup](../harmonyos-references/js-apis-arkui-framenode.md#listitemgroup12) | ARKUI\_NODE\_LIST\_ITEM\_GROUP | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributelistitemgroup20) | NA |
| [WaterFlow](../harmonyos-references/js-apis-arkui-framenode.md#waterflow12) | ARKUI\_NODE\_WATER\_FLOW | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributewaterflow20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollerwaterflow20) |
| [FlowItem](../harmonyos-references/js-apis-arkui-framenode.md#flowitem12) | ARKUI\_NODE\_FLOW\_ITEM | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributeflowitem20) | NA |
| [Grid](../harmonyos-references/js-apis-arkui-framenode.md#grid14) | ARKUI\_NODE\_GRID | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributegrid20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollergrid20) |
| [GridItem](../harmonyos-references/js-apis-arkui-framenode.md#griditem14) | ARKUI\_NODE\_GRID\_ITEM | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributegriditem20) | NA |
| [Text](../harmonyos-references/js-apis-arkui-framenode.md#text12) | ARKUI\_NODE\_TEXT | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetext20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollertext20) |
| [TextInput](../harmonyos-references/js-apis-arkui-framenode.md#textinput12) | ARKUI\_NODE\_TEXT\_INPUT | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetextinput20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollertextinput20) |
| [TextArea](../harmonyos-references/js-apis-arkui-framenode.md#textarea14) | ARKUI\_NODE\_TEXT\_AREA | [getAttribute](../harmonyos-references/js-apis-arkui-framenode.md#getattributetextarea20) | [bindController](../harmonyos-references/js-apis-arkui-framenode.md#bindcontrollertextarea20) |
