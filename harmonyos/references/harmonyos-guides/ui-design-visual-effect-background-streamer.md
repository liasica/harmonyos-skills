---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-streamer
title: 背景流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 背景流光
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3008a6641e1a85fd05a1e7bf2900842a4ed2a9aed20ce8c054552e5a6226c8d1
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/k84F696vRtO3ouINyFH-rQ/zh-cn_image_0000002589244657.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053025Z&HW-CC-Expire=86400&HW-CC-Sign=FC1159A841C6D53F92486C07A24EDFF1E345A00C5167CB7BC1154D508EBD3351)
