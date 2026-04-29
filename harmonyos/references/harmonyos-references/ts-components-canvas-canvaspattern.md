---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern
title: CanvasPattern
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > CanvasPattern
category: harmonyos-references
scraped_at: 2026-04-29T13:52:24+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:0ce8940183ea9782e632f60fb4e4b869d8c5922ba0d719dd67117c87f4a4de3f
---

一个Object对象，使用[createPattern](ts-canvasrenderingcontext2d.md#createpattern)方法创建，通过指定图像和重复方式创建图片填充的模板。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 方法

PhonePC/2in1TabletTVWearable

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(transform?: Matrix2D): void

使用Matrix2D对象作为参数，对当前CanvasPattern进行矩阵变换。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transform | [Matrix2D](ts-components-canvas-matrix2d.md) | 否 | 转换矩阵。  异常值undefined和null按无效值不做矩阵变换处理。  默认值：不做矩阵变换 |

## 示例

PhonePC/2in1TabletTVWearable

通过setTransform对当前CanvasPattern进行矩阵变换。

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasPatternPage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private matrix: Matrix2D = new Matrix2D();
8. // "common/pattern.jpg"需要替换为开发者所需的图像资源文件
9. private img: ImageBitmap = new ImageBitmap("common/pattern.jpg");
10. private pattern: CanvasPattern | null = null;

12. build() {
13. Column() {
14. Button("Click to set transform")
15. .onClick(() => {
16. this.matrix.scaleY = 1
17. this.matrix.scaleX = 1
18. this.matrix.translateX = 50
19. this.matrix.translateY = 200
20. if (this.pattern) {
21. this.pattern.setTransform(this.matrix)
22. }
23. this.context.fillRect(0, 0, 480, 720)
24. })
25. .width("45%")
26. .margin("5px")
27. Canvas(this.context)
28. .width('100%')
29. .height('80%')
30. .backgroundColor('#FFFFFF')
31. .onReady(() => {
32. this.pattern = this.context.createPattern(this.img, 'no-repeat')
33. this.matrix.scaleY = 0.5
34. this.matrix.scaleX = 0.5
35. this.matrix.translateX = 50
36. this.matrix.translateY = 50
37. if (this.pattern) {
38. this.context.fillStyle = this.pattern
39. this.pattern.setTransform(this.matrix)
40. }
41. this.context.fillRect(0, 0, 480, 720)
42. })
43. }
44. .width('100%')
45. .height('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/C8wdRjMPS_eDAJlr7abcyg/zh-cn_image_0000002558606794.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=780CD0C6162D00BBCC55DE4CF562D66339E467AA9DD9396443320642FDF4ADEF)
