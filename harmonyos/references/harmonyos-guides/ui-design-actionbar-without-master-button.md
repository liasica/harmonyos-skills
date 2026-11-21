---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-actionbar-without-master-button
title: 设置无主按钮的组件
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 核心操作栏 > 设置无主按钮的组件
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:25+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:c88be860b71e485584802702395e69ccfaab30966c8313770e243c13c4c3b2d3
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置无主按钮的组件。

[HdsActionBar (操作栏)](../harmonyos-references/ui-design-hdsactionbar.md)组件支持多个按钮的样式。当应用开发者需要多个按钮并且没有主按钮，没有展开和收缩的动效时，可以通过设置左按钮和右按钮配置样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/UhvNqvVtS46kIQtkfU6ubg/zh-cn_image_0000002821837239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011000Z&HW-CC-Expire=31536000000&HW-CC-Sign=04938A884CDB10121757168FC3CB4F524959A0A30F65D0A8869022E6A413A9BA)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsActionBar, ActionBarButton } from '@kit.UIDesignKit'
   ```
2. 创建左边的按钮数组startButtons，创建右边的按钮数组endButtons，无主按钮，不支持切换展开和收缩状态。

   ```typescript
   @Entry
   @ComponentV2
   struct Index {

     build() {
       Column() {
         HdsActionBar({
           startButtons: [new ActionBarButton({
             baseIcon: $r('sys.symbol.stopwatch_fill')
           }), new ActionBarButton({
             baseIcon: $r('sys.symbol.stopwatch_fill')
           })],
           endButtons: [new ActionBarButton({
             baseIcon: $r('sys.symbol.mic_fill')
           })]
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
