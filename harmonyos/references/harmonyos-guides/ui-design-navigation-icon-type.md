---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-icon-type
title: 图标类型设置
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 组件导航 > 图标类型设置
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8af710a90574e92c9fdca26585f3c300815cf31332706dfd39aca644ae3afa5b
---

## 场景介绍

从6.0.0(20)版本开始，导航组件新增了对文本型与图片型图标类型的支持。

当应用开发者需要配置图片型图标，或者使用普通文字型图标、单字图标时，可通过设置titleBar图标内容配置中的[type](../harmonyos-references/ui-design-hdsnavigation.md#hdsnavigationiconoptions)属性实现该功能。

图片型图标([IconStyleMode.LARGE](../harmonyos-references/ui-design-hdsnavigation.md#iconstylemode))：适用于需要展示完整图像的场景，例如应用的Logo、用户头像、宣传图或自定义图形按钮。

普通文字型图标([TextStyleMode.NORMAL](../harmonyos-references/ui-design-hdsnavigation.md#textstylemode))：常规的文本按钮，适用于功能选项、操作按钮等需要清晰表达文本含义的场景。

单字图标([TextStyleMode.SINGLE\_CHARACTER](../harmonyos-references/ui-design-hdsnavigation.md#textstylemode))：适用于需要节省空间的紧凑布局，常用于快速操作入口，建议仅在单个文字或字母的场景使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/GNKBeF82QDaGsrEIwE8zPQ/zh-cn_image_0000002736313339.jpg)

## 开发步骤

1. 导入相关模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsNavigationAttribute。具体请参考HdsNavigation的导入模块说明。
   import { TextStyleMode, IconStyleMode, HdsNavigation, HdsNavigationAttribute, HdsNavigationTitleMode } from '@kit.UIDesignKit';
   ```
2. 创建一级导航组件，通过配置titleBar中的menu上的type属性，实现文字型图标以及图片型图标大小设置。

   ```typescript
   @Entry
   @Component
   struct Index {
     build() {
       HdsNavigation() { // 创建HdsNavigation组件
       }
       .titleBar({
         content: {
           title: { mainTitle: '标题' },
           subIcon: {
             content: {
               // 设置用户头像，图片型图标类型
               icon: $r('app.media.contacts'), // contacts为自定义资源，开发者需替换本地资源
               type: IconStyleMode.LARGE,
               label: 'subIcon', // 无障碍播报内容
               isEnabled: true,
               action: () => {
               }
             }
           },
           menu: {
             // 设置菜单内容
             value: [{
               content: {
                 // 设置第一个菜单项内容，设置为普通文本按钮
                 label: '文本',
                 type: TextStyleMode.NORMAL,
                 isEnabled: true,
                 componentId: 'menu_1',
                 action: () => {
                 }
               }
             }, {
               content: {
                 // 设置第二个菜单项内容，设置为单字按钮
                 label: '单',
                 type: TextStyleMode.SINGLE_CHARACTER,
                 isEnabled: true,
                 componentId: 'menu_2',
                 action: () => {
                 }
               }
             }, {
               content: {
                 // 设置第三个菜单项内容，设置为通用图标按钮
                 label: 'largeIcon',
                 icon: $r('sys.symbol.AI_search'),
                 type: IconStyleMode.NORMAL,
                 isEnabled: true,
                 componentId: 'menu_3',
                 action: () => {
                 }
               }
             }],
             maxCount: 3 // 最大菜单显示个数配置
           }
         }
       })
       .titleMode(HdsNavigationTitleMode.MINI)
       .hideBackButton(true)
     }
   }
   ```
