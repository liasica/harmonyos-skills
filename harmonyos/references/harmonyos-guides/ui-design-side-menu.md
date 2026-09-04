---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-side-menu
title: 侧边栏菜单样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 侧边栏菜单样式
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:716ebf6a5acb3ff8fa469850f732dab3c910114f61a63dd37605d3702969f8c0
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置侧边栏菜单样式。

[HdsSideMenu (侧边菜单)](../harmonyos-references/ui-design-hdssidemenu.md)提供一种菜单栏样式组件。设置侧边栏对应的一级菜单和二级菜单，并显示其新消息数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/LjHAUJq2QlaoK9pg8_XpGw/zh-cn_image_0000002712244474.png)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsSideMenu, HdsSideMenuMainItem, HdsSideMenuSubItem, HdsSideMenuBadgeParam, HdsSideBar } from '@kit.UIDesignKit';
   import { SymbolGlyphModifier } from '@kit.ArkUI';
   ```
2. 设置对应的一级菜单和二级菜单，并显示其新消息数量。

   ```typescript
   @Entry
   @ComponentV2
   struct Index {
     @Local showControlButton: boolean = true;
     @Local sideBarMask: boolean = false;
     @Local autoHide: boolean = true;
     @Local barStateTypeText: string = 'Select BarState';
     @Local widthIndex: number = 0;
     @Local badgeNumber: HdsSideMenuBadgeParam = { count: 50 };
     @Local useTheme: boolean = false;
     @Local selectedIndex: number = 2;
     @Local selectedTransparency: number = 0.6;
     @Local str: string = '短信';
     @Local isShowSidebar: boolean = true;
     listOptionsDefault?: HdsSideMenuMainItem[] = [
       new HdsSideMenuMainItem(
         {
           symbol: new SymbolGlyphModifier($r('sys.symbol.ohos_folder_badge_plus')).fontSize(14),
           // label: $r('sys.string.TextView_engr_phone')
         }),
       new HdsSideMenuMainItem({
         icon: $r('sys.symbol.person_wave_3'),
         label: 'Tuesday',
         hdsSideMenuSubItem: [
           new HdsSideMenuSubItem({ label: this.str, badge: this.badgeNumber })],
       }),
       new HdsSideMenuMainItem({
         symbol: new SymbolGlyphModifier($r('sys.symbol.person_crop_circle_fill_1')),
         label: 'Wednesday'
       }),
     ]
     @Builder
     SideBarPanelBuilder() {
       Column() {
         HdsSideMenu({
           items: this.listOptionsDefault,
           selectedIndex: this.selectedIndex,
           $selectedIndex: (selectedIndex: number) => {
             this.selectedIndex = selectedIndex
           }
         })
       }
       .height('100%')
     }
     // 右侧内容区
     @Builder
     ContentPanelBuilder() {
       Column() {
         Column() {
           Button() {
             SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open_sidebar') : $r('sys.symbol.close_sidebar'))
               .fontWeight(FontWeight.Normal)
               .fontSize($r('sys.float.ohos_id_text_size_headline7'))
               .fontColor([$r('sys.color.ohos_id_color_titlebar_icon')])
               .hitTestBehavior(HitTestMode.None)
           }
           .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
           .height(24)
           .width(24)
           .animation({ curve: Curve.Sharp, duration: 100 })
           .onClick(() => {
             this.isShowSidebar = !this.isShowSidebar;
           })
         }
       }
       .height('100%')
       .width('100%')
     }
     @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder
     @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
     @Builder
     build() {
       Column() {
         HdsSideBar({
           sideBarPanelBuilder: (): void => {
             this.sideBarBuilder()
           },
           contentPanelBuilder: (): void => {
             this.contentBuilder()
           },
           isShowSideBar: this.isShowSidebar,
           $isShowSideBar: (isShowSidebar: boolean) => {
             this.isShowSidebar = !isShowSidebar
           }
         })
       }
     }
   }
   ```
