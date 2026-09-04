---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-color
title: 按压阴影
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 按压阴影
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:16+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:fe0d40f646b79211218afac6d660cee0bf3275387cec0710967df2704e7f321b
---

## 场景介绍

从6.0.0(20)版本开始，新增支持[按压阴影](../harmonyos-references/ui-design-hdseffect.md#pressshadow)。

通过按压阴影接口可以设置组件的背景色变化效果，一般常用于组件按压交互时的背景色变化场景。

## 开发步骤

1. 导入模块。

   ```typescript
   import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 创建按压阴影效果。

   ```typescript
   @Entry
   @Component
   struct PressShadowExample {
     @State buttonBlendState: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
     @State buttonGradientState: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

     build() {
       NavDestination() {
         Column({ space: 50 }) {
           Button('BLEND_WHITE', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
             .visualEffect(new hdsEffect.HdsEffectBuilder()
               .pressShadow(this.buttonBlendState)
               .buildEffect())
             .onTouch((event: TouchEvent) => {
               if (event.type === TouchType.Down) {
                 this.buttonBlendState = hdsEffect.PressShadowType.BLEND_WHITE;
               } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
                 this.buttonBlendState = hdsEffect.PressShadowType.NONE;
               }
             })

           Button('GRADIENT', { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
             .visualEffect(new hdsEffect.HdsEffectBuilder()
               .pressShadow(this.buttonGradientState)
               .buildEffect())
             .onTouch((event: TouchEvent) => {
               if (event.type === TouchType.Down) {
                 this.buttonGradientState = hdsEffect.PressShadowType.BLEND_GRADIENT;
               } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
                 this.buttonGradientState = hdsEffect.PressShadowType.NONE;
               }
             })
         }
         .height('70%')
         .justifyContent(FlexAlign.Center)
       }
       .width('100%')
       .height('100%')
       .title('Button example')
       .backgroundColor('#040404')
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/6gk_WCm6QqO1_jxClLqxsQ/zh-cn_image_0000002742123399.gif)
