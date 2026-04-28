---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-streamer
title: 背景流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 背景流光
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e8ca2fccbfcde048e69fac16a10146f5137f5310361e3aa7535c056107472cbf
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持[背景流光](../harmonyos-references/ui-design-hdseffect.md#effecttype)。

通过背景流光接口可以设置组件的背景流动发光效果，并且可以设置背景色及渐变背景色，常用于全屏幕背景流光等。

## 开发步骤

1. 导入模块。

   ```
   1. import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 设置背景流光效果。

   ```
   1. @Entry
   2. @Component
   3. struct UVFlowLight {
   4. @State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();

   6. build() {
   7. Stack() {
   8. }
   9. .visualEffect(new hdsEffect.HdsEffectBuilder()
   10. .shaderEffect({
   11. effectType: hdsEffect.EffectType.UV_BACKGROUND_FLOW_LIGHT,
   12. animation: {
   13. duration: 10000,
   14. iterations: -1,
   15. autoPlay: true,
   16. onFinish: ()=> {
   17. console.info('Succeeded in finishing');
   18. }
   19. },
   20. controller: this.controller,
   21. })
   22. .buildEffect())
   23. .width('100%')
   24. .height('100%')
   25. }
   26. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/lnwWxemGTCufrinW7Im4Qw/zh-cn_image_0000002583478353.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234157Z&HW-CC-Expire=86400&HW-CC-Sign=B34E3247781AA120304FF497B60C6C4780076E5ACCDCE076FECABC6763CE2709)
