---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/design-visual-effect-background-streamer-with-mask
title: 自带背景的双边流光
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 自带背景的双边流光
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ce975191787415e61869ea066dec7a23b58f22ceb4157a6be8d0c49fa2405a3
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持[自带背景的双边流光](../harmonyos-references/ui-design-hds-visual-component.md#hdsscenetype)。

通过通用视效组件HdsVisualComponent提供的自带背景的双边流光效果场景接口，支持设置两条边缘流光的起始、终止位置、边缘颜色效果以及与流光相叠加的背景板颜色，用于胶囊组件、屏幕边缘发光等。

## 开发步骤

1. 导入模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入HdsVisualComponentAttribute。具体请参考HdsVisualComponent的导入模块说明。
   2. import {
   3. HdsVisualComponent,
   4. HdsVisualComponentAttribute,
   5. HdsSceneController,
   6. HdsSceneType
   7. } from '@kit.UIDesignKit';
   ```
2. 使用HdsVisualComponent组件，指定场景类型为DUAL\_EDGE\_FLOW\_LIGHT\_WITH\_BACKGROUND\_MASK，并且设置场景参数。

   ```
   1. @Entry
   2. @Component
   3. struct EdgeFlowLightVisualComponent {
   4. @State sceneController: HdsSceneController = new HdsSceneController()
   5. .setSceneParams({
   6. backgroundMaskColors: [Color.Green, Color.Red],
   7. firstEdgeFlowLight: {
   8. startPos: 0,
   9. endPos: 0.5,
   10. color: Color.Red
   11. },
   12. secondEdgeFlowLight: {
   13. startPos: 0,
   14. endPos: -0.5,
   15. color: Color.Green
   16. }
   17. })

   19. build() {
   20. Stack() {
   21. HdsVisualComponent()
   22. .scene(HdsSceneType.DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK, this.sceneController, () => {
   23. console.info('Succeeded in finishing');
   24. })
   25. .width('100%')
   26. .height('50%')
   27. }
   28. }
   29. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/DU6A3HUMRKGr2TFrXIbHaA/zh-cn_image_0000002552798704.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234157Z&HW-CC-Expire=86400&HW-CC-Sign=90B0558745889E8F907D95E328BBE085A3527AEA707C1064040B401BC260025D)
