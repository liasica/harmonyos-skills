---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-sidebar-enbed-mode
title: 设置embed模式的侧边栏
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 侧边栏样式 > 设置embed模式的侧边栏
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3dcf953616e16d02b4bdf3a5369ccee639467162e3643e04951b12cb89d962d9
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置embed模式的侧边栏。

[HdsSideBar (侧边栏)](../harmonyos-references/ui-design-hdssidebar.md)提供可以显示和隐藏的侧边栏容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区，通过设置[sideBarContainerType](../harmonyos-references/ts-container-sidebarcontainer.md#sidebarcontainertype枚举说明)的值为SideBarContainerType.Embed，使得当前HdsSideBar为嵌入样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/878KLpfuRNW9s_Oq_vfr5g/zh-cn_image_0000002712404438.png)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsSideBar } from '@kit.UIDesignKit';
   ```
2. 设置图片。

   将图片资源，放到entry/src/main/resources/base/media下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/C5lVnNfwSQmUICy4dOnW_A/zh-cn_image_0000002742123387.png)
3. 创建HdsSideBar侧边栏组件，设置展开模式为embed。

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
         sideBarContainerType: SideBarContainerType.Embed,
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
