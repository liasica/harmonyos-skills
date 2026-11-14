---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-sidebar-overlay-mode
title: 设置overlay模式的侧边栏
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 侧边栏样式 > 设置overlay模式的侧边栏
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:21+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:c686aae8d5ebd2e3be340e410e7d7219fe868b22baac435fcb8276316911a4aa
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置overlay模式的侧边栏。

[HdsSideBar (侧边栏)](../harmonyos-references/ui-design-hdssidebar.md)提供可以显示和隐藏的侧边栏容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区，通过设置[sideBarContainerType](../harmonyos-references/ts-container-sidebarcontainer.md#sidebarcontainertype枚举说明)的值为SideBarContainerType.Overlay，使得当前HdsSideBar为悬浮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/S3f5gLxqSh2mT5zZgERPDg/zh-cn_image_0000002817426705.png?HW-CC-KV=V1&HW-CC-Date=20261114T004542Z&HW-CC-Expire=31536000000&HW-CC-Sign=52E2409D160CE31BC4D9528953E9FBEF12E87FCDFD6B51F39365F68EEDC5CE1F)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsSideBar } from '@kit.UIDesignKit';
   ```
2. 设置图片。

   将图片资源，放到entry/src/main/resources/base/media下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/GMA1sWqGSBOg9eM4LEsjLg/zh-cn_image_0000002788467286.png?HW-CC-KV=V1&HW-CC-Date=20261114T004542Z&HW-CC-Expire=31536000000&HW-CC-Sign=851FF0032186D6A6477D4E395700EDCE6F93D038003107E1CBB8421516C89315)
3. 创建HdsSideBar侧边栏组件，设置展开模式为overlay。

   ```typescript
   @Entry
   @ComponentV2
   struct Index {
     @Local isSideBarContainerMask: boolean = true;
     @Local blankHeight: number = 48;
     @Local isAutoHide: boolean = false;
     @Local isShowSidebar: boolean = true;
     @Local triggerValueReplace: number = 0;
     // 左侧侧边栏区
     @Builder
     SideBarPanelBuilder() {
       Column() {
         Blank().height(this.blankHeight)
         Text('HDSSideBar Menu 1')
           .fontSize(14)
         Text('HDSSideBar Menu 2')
           .fontSize(14)
       }
       .width('100%')
       .height('100%')
     }
     // 右侧内容区
     @Builder
     ContentPanelBuilder() {
       Column(){
         Blank().height(this.blankHeight)
         Image($r('app.media.view')) // view为自定义资源，开发者需替换本地资源
           .width('80%')
           .height('50%')
           .margin({ top: 8 })
           .padding({
             right: '16vp',
             left: '16vp',
             bottom: '16vp'
           })
           .borderRadius(8)
         Column() {
           Text('HDSSideBar content text1')
             .fontSize(14)
           Text('HDSSideBar content text2')
             .fontSize(14)
         }
         Button() {
           SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open_sidebar') : $r('sys.symbol.close_sidebar'))
             .fontWeight(FontWeight.Normal)
             .fontSize($r('sys.float.ohos_id_text_size_headline7'))
             .fontColor([$r('sys.color.ohos_id_color_titlebar_icon')])
             .hitTestBehavior(HitTestMode.None)
         }
         .id('side_bar_button')
         .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
         .height(24)
         .width(24)
         .animation({ curve: Curve.Sharp, duration: 100 })
         .onClick(() => {
           this.isShowSidebar = !this.isShowSidebar;
         })
       }
     }
     @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
     @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder
     @Builder
     HDSSideBarBuilder() {
       HdsSideBar({
         sideBarPanelBuilder: (): void => {
           this.sideBarBuilder()
         },
         contentPanelBuilder: (): void => {
           this.contentBuilder()
         },
         autoHide: this.isAutoHide,
         contentAreaMask: this.isSideBarContainerMask,
         sideBarContainerType: SideBarContainerType.Overlay,
         isShowSideBar: this.isShowSidebar,
         $isShowSideBar: (isShowSidebar: boolean) => {
           this.isShowSidebar = !isShowSidebar
         },
       })
     }
     @Builder
     build() {
       Stack() {
         this.HDSSideBarBuilder()
       }
     }
   }
   ```
