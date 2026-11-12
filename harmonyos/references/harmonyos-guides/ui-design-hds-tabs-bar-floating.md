---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating
title: 设置页签栏的悬浮样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的悬浮样式
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:35fb9ecae9af76ed77c9bc676aadfddb15584001e9f9e68aca2d5367db8df950
---

## 场景介绍

从6.1.0(23) 版本开始，新增支持设置页签栏的悬浮样式以及迷你栏。

## 页签栏

页签栏悬浮样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/EKmElj9lSVSrs-hqfFjY0Q/zh-cn_image_0000002815399121.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3379BA66A47B19A783848C5F954BE36C6AB16F7E302538390D7A1D0253E5D4E)

## 迷你栏

迷你栏是新增的自定义区域，跟页签栏高度相等且水平对齐，支持展开和折叠两种样式。

迷你栏的折叠样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/fhZIA_vKShG4vsuljI0_jg/zh-cn_image_0000002786519546.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B55522AEF4E8E3103D738336CC1288F6C67CED77D117C89FE67FBA2E5AC4014)

迷你栏的展开样式如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/11xAp34KRpKyb1jjxoe-hg/zh-cn_image_0000002786359618.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE260A469004A1CB832CE045955AE8520BDBF0C249B8A4235512488B496A2679)

## 约束条件

1. 布局位置：设置[barPosition](../harmonyos-references/ui-design-hdstabs.md#barposition)为BarPosition.End且[vertical](../harmonyos-references/ui-design-hdstabs.md#vertical)为false，使页签栏置于容器底部。
2. 层级叠加：设置[barOverlap](../harmonyos-references/ui-design-hdstabs.md#baroverlap)为true，使TabBar悬浮于TabContent。
3. 样式限制，当前仅支持以下样式配置：
   * [BottomTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#bottomtabbarstyle9)（底部标签栏样式）
   * [CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)（自定义构建器）

## 开发步骤

1. 导入相关模块。

   ```typescript
    // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
    import { HdsTabs, HdsTabsAttribute, HdsTabsController, hdsMaterial } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barFloatingStyle样式，并设置barOverlap为true，vertical为false，barPosition为BarPosition.End，可实现页签栏的悬浮样式。若在barFloatingStyle中设置miniBar，则可实现迷你栏。

   ```typescript
   @Entry
   @Component
   struct Index {
     // 初始化HdsTabs控制器
     private controller: HdsTabsController = new HdsTabsController();

     @Builder
     miniBarBuilder() {
       Row() {
         Column() {
           Image($r('app.media.alarm_stop'))
             .width(40)
             .height(40)
             .borderRadius(40)
         }.width(48).height(48).justifyContent(FlexAlign.Center).margin({left: 4, right: 4})

         Text('Hello')

         Column() {
           Image($r('sys.media.ohos_ic_public_pause'))
             .width(40)
             .height(40)
             .borderRadius(40)
         }.width(48).height(48).justifyContent(FlexAlign.Center)
       }
     }

     build() {
       Column() {
         HdsTabs({ controller: this.controller }) {
           TabContent() {
             Scroll() {
               Column(){
                 Image($r('app.media.ocean'))
                 Image($r('app.media.desert'))
                 Image($r('app.media.mountain'))
                 Image($r('app.media.sunset'))
               }
             }
           }
           .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Green'))

           TabContent() {
             Image($r('app.media.ocean'))
           }
           .tabBar(new BottomTabBarStyle($r('sys.media.wifi_router_fill'), 'Blue'))

           TabContent() {
             Image($r('app.media.ocean'))
           }
           .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Yellow'))
         }
         // 设置barOverlap为true，vertical为false，barPosition为BarPosition.End
         .barOverlap(true)
         .barPosition(BarPosition.End)
         .vertical(false)
         // 设置页签栏悬浮样式
         .barFloatingStyle({
           barWidth: { smallWidth: 200, mediumWidth: 300, largeWidth: 400 },
           barBottomMargin: 28,
           gradientMask: { maskColor: '#66F1F3F5', maskHeight: 92 },
           systemMaterialEffect: {
             materialType: hdsMaterial.MaterialType.IMMERSIVE,
             materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
           },
           // 设置迷你栏，若不设置，则仅有页签栏
           miniBar: {
             miniBarBuilder: () => this.miniBarBuilder()
           }
         })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
