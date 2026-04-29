---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-point-light
title: 点光源效果
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 视效 > 点光源效果
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a697a3d6749ff90e5497c0bc01948d8c682d0051c73cba730ea35cd3423b6a0f
---

## 场景介绍

从6.0.0(20) Beta1版本开始，新增支持[点光源效果](../harmonyos-references/ui-design-hdseffect.md#pointlight)。

通过点光源接口可以设置组件的发光效果以及被照亮的受光效果，使得组件交互体验更显沉浸。

## 约束与限制

单个组件最多同时受12个光源照亮。

## 开发步骤

1. 导入模块。

   ```
   1. import { hdsEffect } from '@kit.UIDesignKit';
   ```
2. 创建点光源发光效果。如果需要发光，配置sourceType属性；如果需要被照亮，配置illuminatedType属性。

   以下代码表示：当中间的Button点击时，产生点光源效果，重复点击触发不同点光源效果。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State bloomValue: number = 0;
   5. @State index: number = 0;
   6. @State illuminatedType: hdsEffect.PointLightIlluminatedType = hdsEffect.PointLightIlluminatedType.NONE;
   7. @State button_gradient_state: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
   8. @State lightIntensity: number = 10;
   9. @State types: hdsEffect.PointLightIlluminatedType[] =
   10. [hdsEffect.PointLightIlluminatedType.NONE, hdsEffect.PointLightIlluminatedType.BORDER,
   11. hdsEffect.PointLightIlluminatedType.CONTENT, hdsEffect.PointLightIlluminatedType.BORDER_CONTENT,
   12. hdsEffect.PointLightIlluminatedType.DEFAULT_FEATHERING_BORDER];

   14. build() {
   15. Flex({
   16. direction: FlexDirection.Column,
   17. justifyContent: FlexAlign.Center,
   18. alignItems: ItemAlign.Center,
   19. }) {
   20. // 纵向循环
   21. ForEach(Array<number>(4).fill(0), (row: number) => {
   22. Flex({
   23. direction: FlexDirection.Row,
   24. justifyContent: FlexAlign.Center,
   25. alignItems: ItemAlign.Center,
   26. }) {
   27. // 横向循环
   28. ForEach(Array<number>(4).fill(0), (col: number) => {
   29. Flex()
   30. .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
   31. illuminatedType: this.illuminatedType,
   32. }).buildEffect())
   33. .backgroundColor(0x808080)
   34. .size({ width: 60, height: 60 })
   35. .borderRadius(50)
   36. .margin({ top: 20, right: 10, left: 10 }) // 添加间距
   37. })
   38. }
   39. .width('100%') // 设置 Row 组件的宽度为 100%
   40. })

   42. Flex({
   43. direction: FlexDirection.Row,
   44. justifyContent: FlexAlign.Center, // 使用 SpaceBetween 来均匀分布间距
   45. alignItems: ItemAlign.Center,
   46. }) {
   47. Flex()
   48. .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
   49. illuminatedType: this.illuminatedType,
   50. }).buildEffect())
   51. .backgroundColor(0x808080)
   52. .size({ width: 60, height: 60 })
   53. .borderRadius(50)
   54. .margin({ top: 20, right: 10, left: 10 })

   56. Button('点击发光')
   57. .size({ width: 140, height: 60 })
   58. .backgroundColor(0x808080)
   59. .fontColor(0xADD8E6)
   60. .visualEffect(new hdsEffect.HdsEffectBuilder()
   61. .pressShadow(this.button_gradient_state)
   62. .pointLight({
   63. options: {
   64. color: Color.White,
   65. intensity: this.lightIntensity,
   66. height: 150
   67. }
   68. })
   69. .pressShadow(this.button_gradient_state)
   70. .buildEffect())
   71. .onClick(() => {
   72. if (this.index <= 3) {
   73. this.index++;
   74. this.illuminatedType = this.types[this.index];
   75. this.button_gradient_state = hdsEffect.PressShadowType.BLEND_GRADIENT;
   76. }
   77. let message = 'NONE';
   78. if (this.illuminatedType == 1) {
   79. message = 'BORDER';
   80. } else if (this.illuminatedType == 2) {
   81. message = 'CONTENT';
   82. } else if (this.illuminatedType == 3) {
   83. message = 'BORDER_CONTENT';
   84. } else {
   85. message = 'DEFAULT_FEATHERING_BORDER';
   86. }
   87. this.getUIContext().getPromptAction().showToast({
   88. message: message,
   89. duration: 2000,
   90. bottom: '80%'
   91. });
   92. })
   93. .margin({ top: 20, right: 10, left: 10 })

   95. Flex()
   96. .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
   97. illuminatedType: this.illuminatedType,
   98. }).buildEffect())
   99. .backgroundColor(0x808080)
   100. .size({ width: 60, height: 60 })
   101. .borderRadius(50)
   102. .margin({ top: 20, right: 10, left: 10 })
   103. }
   104. .width('100%') // 设置 Row 组件的宽度为 100%

   106. ForEach(Array<number>(4).fill(0), (row: number) => {
   107. Flex({
   108. direction: FlexDirection.Row,
   109. justifyContent: FlexAlign.Center,
   110. alignItems: ItemAlign.Center,
   111. }) {
   112. // 横向循环
   113. ForEach(Array<number>(4).fill(0), (col: number) => {
   114. Flex()
   115. .visualEffect(new hdsEffect.HdsEffectBuilder().pointLight({
   116. illuminatedType: this.illuminatedType,
   117. }).buildEffect())
   118. .backgroundColor(0x808080)
   119. .size({ width: 60, height: 60 })
   120. .borderRadius(50)
   121. .margin({ top: 20, right: 10, left: 10 })
   122. })
   123. }
   124. .width('100%') // 设置 Row 组件的宽度为 100%
   125. })
   126. }
   127. .backgroundColor(Color.Black)
   128. }
   129. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/2XzCTjWJQn2fUWsTJ7vw8g/zh-cn_image_0000002558764850.png?HW-CC-KV=V1&HW-CC-Date=20260429T053024Z&HW-CC-Expire=86400&HW-CC-Sign=CF9AF6551478A6AC5B73E0FFFE947814939312D068B33CDD700CEE9752739B64)
