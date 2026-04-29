---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-385
title: 如何实现字体渐变效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现字体渐变效果
category: harmonyos-faqs
scraped_at: 2026-04-29T14:17:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b4295a58d1c87e34951e1052756675341e58ba1b97cb6efa8fdb10851545a069
---

**问题现象**

当通过linearGradient设置渐变时，默认是背景色的渐变，而非文字渐变的效果。应该如何实现文字渐变？

**可能原因**

由于linearGradient颜色渐变属于组件内容且绘制在背景上方，若仅对文本应用渐变，效果将作用于背景而非文字本身，其效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/hIpOfM1YRaC_7DGz1TusXA/zh-cn_image_0000002337430672.png?HW-CC-KV=V1&HW-CC-Date=20260429T061737Z&HW-CC-Expire=86400&HW-CC-Sign=98FB8420CC3A7E9C448B09864A256173E5D810AB0E1C6BF13CE3C0FC689AE72A)

**解决措施**

要实现作用在字体上，目前以下实现方式：

1、API20之前

* ArkTS侧可以结合blendMode将背景色裁掉。通过**混合模式（BlendMode）**可以指定当前像素如何与其下方的像素混合，可以用来实现裁切、蒙版、提亮等效果。关于BlendMode的具体使用可以参考：[BlendMode](../harmonyos-references/arkts-apis-graphics-drawing-e.md#blendmode)。

  实现文字渐变的示例如下：

  ```
  1. @Entry
  2. @Component
  3. struct Index {
  4. @State message: string = 'Hello World';

  6. build() {
  7. RelativeContainer() {
  8. Row() {
  9. Text(this.message)
  10. .fontSize(24)
  11. .fontWeight(FontWeight.Bold)
  12. .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)
  13. }
  14. .linearGradient({
  15. direction: GradientDirection.Right,
  16. colors: [['#ff0631f5', 0.0], ['#ff922626', 1]]
  17. })
  18. .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
  19. }
  20. .width('100%')
  21. .height('100%')
  22. }
  23. }
  ```

  [FontGradient.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/abce1db5a4cf676fd100dbd3a0acd02f5bb30358/ArkUI/entry/src/main/ets/pages/FontGradient.ets#L6-L28)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/bGnOyTilS7CrqW9ghLdJSw/zh-cn_image_0000002371468633.png?HW-CC-KV=V1&HW-CC-Date=20260429T061737Z&HW-CC-Expire=86400&HW-CC-Sign=01ACFF76D6FF8F7A3410319AE702FA7F758CBA773D554C6CE70B0785C6A482FF)
* C-API侧，使用方案同上，使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)的NODE\_BLEND\_MODE，以及NODE\_LINEAR\_GRADIENT进行设置；

2、API20及以上

* 采用ArkTS实现文字渐变，可以使用Text的[shaderStyle](../harmonyos-references/ts-basic-components-text.md#shaderstyle20)属性，直接设置字体的渐变，示例如下：

  ```
  1. @Entry
  2. @Component
  3. struct Index {
  4. @State message: string = 'Hello World';

  6. build() {
  7. RelativeContainer() {
  8. Text(this.message)
  9. .fontSize(24)
  10. .fontWeight(FontWeight.Bold)
  11. .shaderStyle({
  12. direction: GradientDirection.Right,
  13. colors: [['#ff0631f5', 0.0], ['#ff922626', 1]]
  14. })
  15. }
  16. .width('100%')
  17. .height('100%')
  18. }
  19. }
  ```

  [FontGradientPlanTwo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FontGradientPlanTwo.ets#L21-L40)
* 对于使用C-API开发的应用，可以使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)的 NODE\_TEXT\_LINEAR\_GRADIENT属性，实现文字渐变。

更多文字效果请参考：[基于Text组件及通用属性实现文字特效](https://gitcode.com/harmonyos_samples/text-effects)。
