---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-set-multi-window
title: 设置应用内多窗
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置应用内多窗
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:15+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:3e6444e8d053ae9996f7f1eac53c5d34e419e2db2dc29bac9c33c429945df9b1
---

## 场景介绍

从6.0.0(20)版本开始，新增支持应用内多窗。

当应用开发者需要使用应用内多窗图标（分屏按钮）时，可通过配置titleBar中的menu的[multiWindowEntryInAPPMenu](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationmenucontentoptions)属性实现该功能。

## 约束条件

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备形态，该组件不可交互，不响应点击事件。

## 开发步骤

1. 导入模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   import { HdsNavigation, HdsNavigationMenuContentOptions, HdsNavigationAttribute } from '@kit.UIDesignKit';
   import { Want } from '@kit.AbilityKit';
   ```
2. 创建一级导航组件，通过配置titleBar中的menu上的multiWindowEntryInAPPMenu属性，实现应用内多窗图标设置。

   ```typescript
   @Entry
   @Component
   struct MultiWindowEntryInAPPTest {
     private want: Want = {
       // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
       // 注意：以下参数仅为示例，请替换为实际应用的参数
       bundleName: 'com.example.myapplication',
       moduleName: 'entry',
       abilityName: 'FuncAbility',
     }
     @State menuContent: HdsNavigationMenuContentOptions = {
       multiWindowEntryInAPPMenu: {
         want: this.want
       },
       maxCount: 3,
       value: [
         { content: { label: 'menu1', icon: $r('sys.symbol.search_things'), } },
         { content: { label: 'menu2', icon: $r('sys.symbol.plus'), } }
       ]
     }

     build() {
       HdsNavigation() {
         Stack() {
           Text('Page1')
         }.alignContent(Alignment.Center)
         .width('100%')
         .height('100%')
       }
       .hideToolBar(false)
       .navBarWidth('100%')
       .titleBar({
         content: {
           title: {
             mainTitle: "Index"
           },
           menu: this.menuContent
         }
       })
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ebkmNhCyQiyRxUXcmnfwNg/zh-cn_image_0000002712404436.jpg)
