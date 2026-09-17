---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-streamer
title: 背景流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 背景流光
category: harmonyos-guides
scraped_at: 2026-09-18T06:45:22+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:b685be780c971329efecc56739112b8d840fec89a19ea15e630cf34e994cfd5a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/YuUFfP7_Qte972-a0rwP_A/zh-cn_image_0000002727591054.jpg)
