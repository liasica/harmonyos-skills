---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-double-edge-streamer
title: 双边边缘流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 双边边缘流光
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:1f1c7f8b9cc23c6624cfae8f5c8e7ae2d7e8160bf690604570d816dd40a73fc7
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/bffhEv7wQx29WnZ4fFXJdQ/zh-cn_image_0000002786359624.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCE797EC80EF9BD7B744EBD356CBC7CEEE1C8DA724C86D2BD7F2F1FA5159A289)
