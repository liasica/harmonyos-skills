---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-color
title: 按压阴影
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 按压阴影
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0745ad416ab8d5e7e50cc5cb33e7c1f0675df89ffd52cd047faf414d28caf665
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持[按压阴影](../harmonyos-references/ui-design-hdseffect.md#pressshadow)。

通过按压阴影接口可以设置组件的背景色变化效果，一般常用于组件按压交互时的背景色变化场景。

## 开发步骤

1. 导入模块。

   ```
   1. import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 创建按压阴影效果。

   ```
   1. @Entry
   2. @Component
   3. struct PressShadowExample {
   4. @State button_blend_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
   5. @State button_gradient_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

   7. build() {
   8. NavDestination() {
   9. Column({ space: 50 }) {
   10. Button("BLEND_WHITE", { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
   11. .visualEffect(new hdsEffect.HdsEffectBuilder()
   12. .pressShadow(this.button_blend_state)
   13. .buildEffect())
   14. .onTouch((event: TouchEvent) => {
   15. if (event.type === TouchType.Down) {
   16. this.button_blend_state =  hdsEffect.PressShadowType.BLEND_WHITE;
   17. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
   18. this.button_blend_state =  hdsEffect.PressShadowType.NONE;
   19. }
   20. })

   22. Button("GRADIENT", { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
   23. .visualEffect(new hdsEffect.HdsEffectBuilder()
   24. .pressShadow(this.button_gradient_state)
   25. .buildEffect())
   26. .onTouch((event: TouchEvent) => {
   27. if (event.type === TouchType.Down) {
   28. this.button_gradient_state =  hdsEffect.PressShadowType.BLEND_GRADIENT;
   29. } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
   30. this.button_gradient_state =  hdsEffect.PressShadowType.NONE;
   31. }
   32. })
   33. }
   34. .height('70%')
   35. .justifyContent(FlexAlign.Center)
   36. }
   37. .width('100%')
   38. .height('100%')
   39. .title('Button example')
   40. .backgroundColor('#040404')
   41. }
   42. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/XpcNAviGQ9ue7AgTFZzIlw/zh-cn_image_0000002583438397.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234157Z&HW-CC-Expire=86400&HW-CC-Sign=D70E7209E15557846A96E8ED09E4026C8E1E572577E4B6F45CCAF0454FE5A16E)
