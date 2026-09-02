---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-crosslanguage
title: 设置自定义节点跨语言属性
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 设置自定义节点跨语言属性
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3b3d83dbf5bcffb0126914204ba53c0537c8c70d504c0b4456a0d7cd32219547
---

## 概述

ArkUI支持在前端使用ArkTS语言创建命令式节点，即[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点，也可以在Native侧使用C语言创建命令式节点，并且可以混合使用两类节点构建页面。

针对上述场景，ArkUI提供命令式节点跨语言属性设置功能，即使用ArkTS语言创建的命令式节点，可以在Native侧进行属性设置。使用C语言创建的节点，可以在ArkTS侧进行属性设置。

**说明** 

下述示例中，需要先进行Native侧配置，请参考[接入ArkTS页面](ndk-access-the-arkts-page.md)完成。

## 设置和获取跨语言配置

跨语言指的是跨越ArkTS语言和C语言。跨语言配置指的是命令式节点上对于跨语言操作的权限配置。

可以通过[setCrossLanguageOptions](../harmonyos-references/js-apis-arkui-framenode.md#setcrosslanguageoptions15)与[OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_setcrosslanguageoption)接口设置当前节点的跨语言配置。如果当前节点无法修改或设置跨语言配置，则会抛出异常信息。

可以使用[getCrossLanguageOptions](../harmonyos-references/js-apis-arkui-framenode.md#getcrosslanguageoptions15)与[OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getcrosslanguageoption)接口获取当前节点的跨语言配置。

以下示例描述了如何设置和获取ArkTS命令式节点的跨语言配置。

```ts
// Index.ets
import { NodeController, UIContext, FrameNode, typeNode, BuilderNode } from '@kit.ArkUI';

@Builder
function insideScroll() {
  Column() {
    ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
      Text(item.toString())
        .width("75%")
        .height(50)
        .backgroundColor(0xFFFFFF)
        .borderRadius(15)
        .fontSize(30)
        .textAlign(TextAlign.Center)
        .margin({ top: 10 })
    }, (item: number) => item.toString())
  }
  .width("100%")
}

class MyNodeController extends NodeController {
  uiContext: UIContext | null = null;
  rootNode: FrameNode | null = null;
  scrollNode: FrameNode | null = null;
  scroller: Scroller = new Scroller();

  makeNode(uiContext: UIContext): FrameNode | null {
    this.uiContext = uiContext;
    this.rootNode = new FrameNode(uiContext);
    this.rootNode.commonAttribute.width("80%").height("50%").borderWidth(2).margin(15);
    const scroll = typeNode.createNode(uiContext, 'Scroll');
    scroll.initialize(this.scroller).id("scroll");
    this.scrollNode = scroll;
    this.rootNode.appendChild(this.scrollNode);
    const builderNode = new BuilderNode(uiContext);
    builderNode.build(wrapBuilder(insideScroll));
    this.scrollNode?.appendChild(builderNode.getFrameNode());
    return this.rootNode;
  }
}

@Entry
@Component
struct CrossLanguage {
  myNodeController: MyNodeController = new MyNodeController()
  @State attributeSetting: boolean = false;
  @State getCrossLanguageOptions: string = '{"attributeSetting": false}';

  build() {
    Scroll() {
      Column({ space: 15 }) {
        Column() {
          Scroll() {
            Column() {
              NodeContainer(this.myNodeController)
              Button("setCrossLanguageOptions").margin({ bottom: 15})
                .onClick(() => {
                  this.attributeSetting = !this.attributeSetting;
                  this.myNodeController.scrollNode?.setCrossLanguageOptions({
                    attributeSetting: this.attributeSetting
                  });
                  // 若attributeSetting为true，表示scrollNode支持通过非ArkTS语言进行属性设置，否则为不支持
                  this.getCrossLanguageOptions = JSON.stringify(this.myNodeController.scrollNode?.getCrossLanguageOptions());
                })
              Text("CrossLanguageOptions: " + this.getCrossLanguageOptions)
            }
          }.scrollBarColor(Color.Transparent)
        }
        .width('100%')
        .height(350)
        .backgroundColor(0xeeeeee)
        .id('Part_TS')
      }
      .width('100%')
    }.scrollBarColor(Color.Transparent)
  }
}
```

## 跨语言设置节点属性

获取节点后，若节点的跨语言配置设置为允许属性设置，ArkTS侧可利用getAttribute接口获取修改Native节点属性的对象，Native侧可利用[setAttribute](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口修改ArkTS节点属性。

以下示例创建了ArkTS的[Scroll](../harmonyos-references/js-apis-arkui-framenode.md#scroll12)类型节点，并在Native侧修改了Scroll的属性。

1. 在ArkTS侧创建组件类型为Scroll的命令式节点。

   ```ts
   // Index.ets
   import nativeNode from 'libentry.so';
   import { NodeController, UIContext, FrameNode, typeNode, BuilderNode, NodeContent } from '@kit.ArkUI';

   @Builder
   function insideScroll() {
     Column() {
       ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
         Text(item.toString())
           .width("75%")
           .height(50)
           .backgroundColor(0xFFFFFF)
           .borderRadius(15)
           .fontSize(30)
           .textAlign(TextAlign.Center)
           .margin({ top: 10 })
       }, (item: number) => item.toString())
     }
     .width("100%")
   }

   class MyNodeController extends NodeController {
     uiContext: UIContext | null = null;
     rootNode: FrameNode | null = null;
     scrollNode: FrameNode | null = null;
     scroller: Scroller = new Scroller();

     makeNode(uiContext: UIContext): FrameNode | null {
       this.uiContext = uiContext;
       this.rootNode = new FrameNode(uiContext);
       this.rootNode.commonAttribute.width("80%").height("50%").borderWidth(2).margin(15);
       const scroll = typeNode.createNode(uiContext, 'Scroll');
       scroll.initialize(this.scroller).id("scroll");
       this.scrollNode = scroll;
       this.rootNode.appendChild(this.scrollNode);
       const builderNode = new BuilderNode(uiContext);
       builderNode.build(wrapBuilder(insideScroll));
       this.scrollNode?.appendChild(builderNode.getFrameNode());
       return this.rootNode;
     }
   }

   @Entry
   @Component
   struct CrossLanguage {
     private myNodeController: MyNodeController = new MyNodeController();
     @State attributeSetting: boolean = false;
     @State getCrossLanguageOptions: string = '{"attributeSetting": false}';
     private rootSlot = new NodeContent();

     aboutToAppear(): void {
       nativeNode.createNativeRoot(this.rootSlot);
     }

     build() {
       Scroll() {
         Column({ space: 15 }) {
           Column() {
             Scroll() {
               Column() {
                 NodeContainer(this.myNodeController)
                 Button("setCrossLanguageOptions").margin({ bottom: 15})
                   .onClick(() => {
                     this.attributeSetting = !this.attributeSetting;
                     this.myNodeController.scrollNode?.setCrossLanguageOptions({
                       attributeSetting: this.attributeSetting
                     });
                     // 若attributeSetting为true，表示scrollNode支持通过非ArkTS语言进行属性设置，否则为不支持
                     this.getCrossLanguageOptions = JSON.stringify(this.myNodeController.scrollNode?.getCrossLanguageOptions());
                   })
                 Text("CrossLanguageOptions: " + this.getCrossLanguageOptions)
               }
             }.scrollBarColor(Color.Transparent)
           }
           .width('100%')
           .height(350)
           .backgroundColor(0xeeeeee)
           .id('Part_TS')

           Column() {
             ContentSlot(this.rootSlot)
           }
           .width(500)
           .height(400)
           .id('Part_C')
         }
         .width('100%')
       }.scrollBarColor(Color.Transparent)
     }
   }
   ```
2. 新建CrossLanguageExample.h文件，在其中获取到目标节点（该节点在ArkTS侧创建），并设置属性。

   ```c
   // CrossLanguageExample.h
   #ifndef MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H
   #define MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H

   #include "ArkUINode.h"
   #include <hilog/log.h>

   namespace NativeModule {

   std::shared_ptr<ArkUIBaseNode> CreateCrossLanguageExample() {
       auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
       
       // 创建根节点Scroll
       ArkUI_NodeHandle scroll = nodeAPI->createNode(ARKUI_NODE_SCROLL);
       ArkUI_NumberValue length_value[] = {{.f32 = 480}};
       ArkUI_AttributeItem length_item = {length_value, sizeof(length_value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(scroll, NODE_WIDTH, &length_item);
       ArkUI_NumberValue length_value1[] = {{.f32 = 650}};
       ArkUI_AttributeItem length_item1 = {length_value1, sizeof(length_value1) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(scroll, NODE_HEIGHT, &length_item1);
       ArkUI_AttributeItem scroll_id = {.string = "Scroll_CAPI"};
       nodeAPI->setAttribute(scroll, NODE_ID, &scroll_id);
       
       // 创建Column
       ArkUI_NodeHandle column = nodeAPI->createNode(ARKUI_NODE_COLUMN);
       ArkUI_NumberValue value[] = {480};
       ArkUI_AttributeItem item = {value, sizeof(value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(column, NODE_WIDTH, &item);
       ArkUI_NumberValue column_bc[] = {{.u32 = 0xFFF00BB}};
       ArkUI_AttributeItem column_item = {column_bc, 1};
       nodeAPI->setAttribute(column, NODE_BACKGROUND_COLOR, &column_item);
       ArkUI_AttributeItem column_id = {.string = "Column_CAPI"};
       nodeAPI->setAttribute(column, NODE_ID, &column_id);
       
       // 创建Text
       ArkUI_NodeHandle text0 = nodeAPI->createNode(ARKUI_NODE_TEXT);
       ArkUI_NumberValue text_width[] = {300};
       ArkUI_AttributeItem text_item0 = {text_width, sizeof(text_width) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text0, NODE_WIDTH, &text_item0);
       ArkUI_NumberValue text_height[] = {50};
       ArkUI_AttributeItem text_item1 = {text_height, sizeof(text_height) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text0, NODE_HEIGHT, &text_item1);
       ArkUI_AttributeItem text_item = {.string = "C设置TS创建的节点属性"};
       nodeAPI->setAttribute(text0, NODE_TEXT_CONTENT, &text_item);
       ArkUI_NumberValue margin[] = {10};
       ArkUI_AttributeItem item_margin = {margin, sizeof(margin) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(text0, NODE_MARGIN, &item_margin);
       
       // 创建Row
       ArkUI_NodeHandle row0 = nodeAPI->createNode(ARKUI_NODE_ROW);
       ArkUI_NumberValue width_value[] = {{.f32=330}};
       ArkUI_AttributeItem width_item = {width_value, sizeof(width_value) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(row0, NODE_WIDTH, &width_item);
       nodeAPI->setAttribute(row0, NODE_HEIGHT, &text_item1);
       nodeAPI->setAttribute(row0, NODE_MARGIN, &item_margin);
       
       // 创建Button
       ArkUI_NodeHandle bt0 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
       ArkUI_NumberValue btn_width[] = {150};
       ArkUI_AttributeItem btn_item0 = {btn_width, sizeof(btn_width) / sizeof(ArkUI_NumberValue)};
       nodeAPI->setAttribute(bt0, NODE_WIDTH, &btn_item0);
       nodeAPI->setAttribute(bt0, NODE_HEIGHT, &text_item1);
       nodeAPI->setAttribute(bt0, NODE_MARGIN, &item_margin);
       ArkUI_AttributeItem bt0_item = {.string = "scrollBarColor"};
       nodeAPI->setAttribute(bt0, NODE_BUTTON_LABEL, &bt0_item);
       nodeAPI->registerNodeEvent(bt0, NODE_ON_CLICK, 0, nullptr);
       
       ArkUI_NodeHandle bt1 = nodeAPI->createNode(ARKUI_NODE_BUTTON);
       nodeAPI->setAttribute(bt1, NODE_WIDTH, &btn_item0);
       nodeAPI->setAttribute(bt1, NODE_HEIGHT, &text_item1);
       nodeAPI->setAttribute(bt1, NODE_MARGIN, &item_margin);
       ArkUI_AttributeItem bt1_item = {.string = "scrollBarWidth"};
       nodeAPI->setAttribute(bt1, NODE_BUTTON_LABEL, &bt1_item);
       nodeAPI->registerNodeEvent(bt1, NODE_ON_CLICK, 1, nullptr);
       
       // 注册事件
       auto onClick = [](ArkUI_NodeEvent *event) {
           ArkUI_NodeHandle node = OH_ArkUI_NodeEvent_GetNodeHandle(event);
           auto nodeAPI = NativeModuleInstance::GetInstance()->GetNativeNodeAPI();
           
           if (OH_ArkUI_NodeEvent_GetTargetId(event) == 0) {  // scrollBarColor
               ArkUI_NodeHandle node_ptr = nullptr;
               OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("scroll", &node_ptr);
               try {
                   ArkUI_NumberValue scroll_color_value[] = {{.u32 = 0xff00ff00}};
                   ArkUI_AttributeItem scroll_color_item = {scroll_color_value, sizeof(scroll_color_value) / sizeof(ArkUI_NumberValue)};
                   nodeAPI->setAttribute(node_ptr, NODE_SCROLL_BAR_COLOR, &scroll_color_item);
               } catch (...) {
                   OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample", "crossLanguage setAttribute error");
               }
           }
           
           if (OH_ArkUI_NodeEvent_GetTargetId(event) == 1) {  // scrollBarWidth
               ArkUI_NodeHandle node_ptr = nullptr;
               OH_ArkUI_NodeUtils_GetAttachedNodeHandleById("scroll", &node_ptr);
               try {
                   ArkUI_NumberValue scroll_width_value[] = {{20}};
                   ArkUI_AttributeItem scroll_width_item = {scroll_width_value, sizeof(scroll_width_value) / sizeof(ArkUI_NumberValue)};
                   nodeAPI->setAttribute(node_ptr, NODE_SCROLL_BAR_WIDTH, &scroll_width_item);
               } catch (...) {
                   OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "CrossLanguageExample", "crossLanguage setAttribute error");
               }
           }
       };
       nodeAPI->registerNodeEventReceiver(onClick);
       
       // 节点添加
       nodeAPI->addChild(scroll, column);
       nodeAPI->addChild(column, text0);
       nodeAPI->addChild(column, row0);
       nodeAPI->addChild(row0, bt0);
       nodeAPI->addChild(row0, bt1);
       
       return std::make_shared<ArkUINode>(scroll);
   }
   } // namespace NativeModule

   #endif // MYAPPLICATION_CROSSLANGUAGEEXAMPLE_H
   ```
3. 在NativeEntry.cpp中，挂载Native节点。

   ```c
   // NativeEntry.cpp

   #include <arkui/native_node_napi.h>
   #include <js_native_api.h>
   #include "NativeEntry.h"
   #include "CrossLanguageExample.h"

   namespace NativeModule {

   napi_value CreateNativeRoot(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value args[1] = {nullptr};

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 获取NodeContent
       ArkUI_NodeContentHandle contentHandle;
       OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
       NativeEntry::GetInstance()->SetContentHandle(contentHandle);

       // 创建节点
       auto node = CreateCrossLanguageExample();

       // 保持Native侧对象到管理类中，维护生命周期。
       NativeEntry::GetInstance()->SetRootNode(node);
       return nullptr;
   }

   napi_value DestroyNativeRoot(napi_env env, napi_callback_info info) {
       // 从管理类中释放Native侧对象。
       NativeEntry::GetInstance()->DisposeRootNode();
       return nullptr;
   }

   } // namespace NativeModule
   ```
4. 修改CMakeLists.txt，添加链接库。

   ```c
   // CMakeLists.txt
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(CAPI_DEMO)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()

   include_directories(${NATIVERENDER_ROOT_PATH}
                     ${NATIVERENDER_ROOT_PATH}/include)

   add_library(entry SHARED napi_init.cpp NativeEntry.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so hilog_ndk.z.so)
   ```
5. 运行程序，在ArkTS侧点击按钮，设置当前attributeSetting为true，在Native侧点击按钮，设置ArkTS侧Scroll组件滚动条的颜色和粗细属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/cwoM01m9SfyFTF7nSz-pGA/zh-cn_image_0000002736432991.gif)

## 支持跨语言设置属性的节点类型

仅以下节点类型支持跨语言设置节点属性。Native侧需要使用[OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid)获取待修改属性的节点，不支持对[OH\_ArkUI\_GetNodeHandleFromNapiValue](../harmonyos-references/capi-native-node-napi-h.md#oh_arkui_getnodehandlefromnapivalue)获取的目标节点跨语言设置属性。

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
