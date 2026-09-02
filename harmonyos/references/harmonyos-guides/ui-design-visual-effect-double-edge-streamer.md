---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-double-edge-streamer
title: 双边边缘流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 双边边缘流光
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:230164cd81ce031d5aeab35412c8b476f1eb7bd21a0f125db331d365415e402a
---

## 场景介绍

从6.0.0(20)版本开始，新增支持[双边边缘流光](../harmonyos-references/ui-design-hdseffect.md#effecttype)。

通过双边边缘流光接口可以设置组件的边缘发光效果，并且可以设置两条边的起始、终止位置和边缘颜色效果，常用于胶囊组件、屏幕边缘发光等。

## 开发步骤

1. 导入模块。

   ```typescript
   import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 设置双边边缘流光效果。

   ```typescript
   @Entry
   @Component
   struct Index {
     @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

     build() {
       Column() {
         Stack() {
         }
         .visualEffect(new hdsEffect.HdsEffectBuilder()
           .shaderEffect({
             effectType: hdsEffect.EffectType.DUAL_EDGE_FLOW_LIGHT,
             animation: {
               duration: 4000,
               iterations: -1,
               autoPlay: true,
               onFinish: () => {
                 console.info('Succeeded in finishing');
               }
             },
             controller: this.controller,
             params: {
               firstEdgeFlowLight: {
                 startPos: 0,
                 endPos: 1.0,
                 color: '#1AD0F1',
               },
               secondEdgeFlowLight: {
                 startPos: 0.5,
                 endPos: 1.5,
                 color: '#FFA4E5',
               }
             }
           })
           .buildEffect())
         .width(200)
         .borderRadius('50%')
         .clip(true)
         .height(200)
         .backgroundColor('#383838')
       }
       .justifyContent(FlexAlign.Center)
       .backgroundColor(Color.Black)
       .width('100%')
       .height('100%')
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/3vnPSlstRU2efsUcEgUH9Q/zh-cn_image_0000002706834246.gif)
