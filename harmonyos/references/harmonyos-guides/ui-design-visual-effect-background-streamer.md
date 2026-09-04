---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-streamer
title: 背景流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 背景流光
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:16+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:d81198f91bf6a1b77d19ec008d10fcdfe2b0414f78839e2fbe277b4556ed4edc
---

## 场景介绍

从6.0.0(20)版本开始，新增支持[背景流光](../harmonyos-references/ui-design-hdseffect.md#effecttype)。

通过背景流光接口可以设置组件的背景流动发光效果，并且可以设置背景色及渐变背景色，常用于全屏幕背景流光等。

## 开发步骤

1. 导入模块。

   ```typescript
   import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 设置背景流光效果。

   ```typescript
   @Entry
   @Component
   struct UVFlowLight {
     @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

     build() {
       Stack() {
       }
       .visualEffect(new hdsEffect.HdsEffectBuilder()
         .shaderEffect({
           effectType: hdsEffect.EffectType.UV_BACKGROUND_FLOW_LIGHT,
           animation: {
             duration: 10000,
             iterations: -1,
             autoPlay: true,
             onFinish: ()=> {
               console.info('Succeeded in finishing');
             }
           },
           controller: this.controller
         })
         .buildEffect())
       .width('100%')
       .height('100%')
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/XU31rQDqTXaUrZdlt0iUrw/zh-cn_image_0000002742003439.jpg)
