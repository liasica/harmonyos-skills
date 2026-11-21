---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-message-reminder
title: 设置信息提醒
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 设置信息提醒
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:25+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:19859b9a25ceeaf7aa05b365882d0f0282e183da48d25e9d0e3c3fd7af8558ba
---

## 场景介绍

从5.1.0(18)版本开始，导航组件新增支持菜单栏设置信息提醒能力。

当应用开发者需要在导航组件菜单项右上角附加消息提醒时，可以通过设置标题栏菜单中的[badge](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationbadgeiconoptions)属性，实现信息提醒能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/-d50BJWbT7u8yxmmqD6x0w/zh-cn_image_0000002821837225.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=B538DC2423D7B21C5BEA13DED58547EE0759790830F6C1BC407004294AF34138)

## 开发步骤

1. 导入相关模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   import { HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
   ```
2. 创建一级导航组件，通过配置titleBar中menu的badge属性，设置信息提醒样式。

   ```typescript
   @Entry
   @Component
   struct Index {
     build() {
       HdsNavigation() { // 创建HdsNavigation组件
       }
       .titleBar({
         content: {
           // 标题栏内容设置
           menu: {
             // 标题栏菜单区域内容设置
             value: [{
               content: {
                 // 第一个菜单项内容设置
                 label: 'menu1',
                 icon: $r('sys.symbol.AI_search'),
                 isEnabled: true
               },
               badge: {
                 // 第一个菜单项信息提醒设置
                 count: 1
               }
             }, {
               content: {
                 // 设置第二个菜单项内容，设置为普通文本按钮
                 label: 'menu2',
                 icon: $r('sys.symbol.wifi'),
                 isEnabled: true,
                 componentId: 'menu_1',
                 action: () => {
                 }
               },
               badge: {
                 // 第二个菜单项信息提醒设置
                 value: '消息'
               }
             }]
           },
           title: { mainTitle: 'MainTitle' },
         }
       })
       .titleMode(HdsNavigationTitleMode.MINI)
       .hideBackButton(true)
     }
   }
   ```
