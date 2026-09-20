---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-actionbar-main-buttons
title: 设置有主按钮的组件
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 核心操作栏 > 设置有主按钮的组件
category: harmonyos-guides
scraped_at: 2026-09-21T06:17:38+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:d261798b9eee0536b570d3e632004986cfece33d249e9e30aa123a84d24b95c5
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置有主按钮的组件。

[HdsActionBar (操作栏)](../harmonyos-references/ui-design-hdsactionbar.md)组件支持多个按钮的样式。当应用开发者需要多个按钮并且有主按钮，支持展开和收缩的动效时，可以通过设置主按钮配置样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/hUQa3TkwSE-yhGsJ49kXqg/zh-cn_image_0000002733434512.gif)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit';
   ```
2. 创建左边的按钮数组startButtons，创建右边的按钮数组endButtons，创建主按钮primaryButton，设置isExpand初始值是true表示HdsActionBar的初始状态是展开状态，点击主按钮会收起，再次点击可以展开。

   ```typescript
   @Entry
   @ComponentV2
   struct Index {
     @Local isExpand: boolean = true;

     @Local isPrimaryIconChanged: boolean = false;

     @Local primaryHoverTips: ResourceStr = '开始';

     build() {
       Column() {
         HdsActionBar({
           startButtons: [new ActionBarButton({
             baseIcon: $r('sys.symbol.stopwatch_fill')
           })],
           endButtons: [new ActionBarButton({
             baseIcon: $r('sys.symbol.mic_fill')
           })],
           primaryButton: new ActionBarButton({
             baseIcon: $r('sys.symbol.plus'),
             altIcon: $r('sys.symbol.play_fill'),
             onClick: () => {
               this.isExpand = !this.isExpand;
               this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
               if (this.isPrimaryIconChanged) {
                 this.primaryHoverTips = '暂停';
               } else {
                 this.primaryHoverTips = '开始';
               }
             },
             hoverTips: this.primaryHoverTips
           }),
           actionBarStyle: new ActionBarStyle({
             isPrimaryIconChanged: this.isPrimaryIconChanged
           }),
           isExpand: this.isExpand
         })
       }
       .width('100%')
       .height('100%')
       .backgroundColor(0xF1F3F5)
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center)
     }
   }
   ```
