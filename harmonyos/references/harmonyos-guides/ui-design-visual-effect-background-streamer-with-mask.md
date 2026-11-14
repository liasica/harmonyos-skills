---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-streamer-with-mask
title: 自带背景的双边流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 自带背景的双边流光
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:21+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:61c102b9f5d00b6b890c4b4cb750ed69e122fe5fb0c3728f679cac5a286cfb62
---

## 场景介绍

从6.0.0(20)版本开始，新增支持[自带背景的双边流光](../harmonyos-references/ui-design-hds-visual-component.md#hdsscenetype)。

通过通用视效组件HdsVisualComponent提供的自带背景的双边流光效果场景接口，支持设置两条边缘流光的起始、终止位置、边缘颜色效果以及与流光相叠加的背景板颜色，用于胶囊组件、屏幕边缘发光等。

## 开发步骤

1. 导入模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsVisualComponentAttribute。具体请参考HdsVisualComponent的导入模块说明。
   import {
     HdsVisualComponent,
     HdsVisualComponentAttribute,
     HdsSceneController,
     HdsSceneType
   } from '@kit.UIDesignKit';
   ```
2. 使用HdsVisualComponent组件，指定场景类型为DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK，并且设置场景参数。

   ```typescript
   @Entry
   @Component
   struct EdgeFlowLightVisualComponent {
     @State sceneController: HdsSceneController = new HdsSceneController()
       .setSceneParams({
         backgroundMaskColors: [Color.Green, Color.Red],
         firstEdgeFlowLight: {
           startPos: 0,
           endPos: 0.5,
           color: Color.Red
         },
         secondEdgeFlowLight: {
           startPos: 0,
           endPos: -0.5,
           color: Color.Green
         }
       })

     build() {
       Stack() {
         HdsVisualComponent()
           .scene(HdsSceneType.DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK, this.sceneController, () => {
             console.info('Succeeded in finishing');
           })
           .width('100%')
           .height('50%')
       }
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/TFX_6yHMTmCn2kf8i2usjQ/zh-cn_image_0000002817506789.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004542Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F47774525B520CE4DC6E214E8CD98F5C447720CBD9859BFDF8CE6E7B7D17FEF)
