---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-geometric-shape-drawing
title: 绘制几何图形 (Shape)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 几何图形绘制 > 绘制几何图形 (Shape)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb58d01015c8531fd0ac7b341510fc6f8011ed26a496778805481c04560e9675
---

绘制组件用于在页面绘制图形，Shape组件是绘制组件的父组件，包含所有绘制组件的通用属性。具体用法请参考[Shape](../harmonyos-references/ts-drawing-components-shape.md)。

## 创建绘制组件

绘制组件可以由以下两种形式创建：

* 绘制组件使用Shape作为父组件，实现类似SVG的效果。接口调用为以下形式：

  ```
  1. Shape(value?: PixelMap)
  ```

  该接口用于创建带有父组件的绘制组件，其中value用于设置绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。

  ```
  1. Shape() {
  2. Rect().width(300).height(50)
  3. }
  ```

  [Shape.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/Shape.ets#L22-L26)
* 绘制组件单独使用，用于在页面上绘制指定的图形。有7种绘制类型，分别为[Circle](../harmonyos-references/ts-drawing-components-circle.md)（圆形）、[Ellipse](../harmonyos-references/ts-drawing-components-ellipse.md)（椭圆形）、[Line](../harmonyos-references/ts-drawing-components-line.md)（直线）、[Polyline](../harmonyos-references/ts-drawing-components-polyline.md)（折线）、[Polygon](../harmonyos-references/ts-drawing-components-polygon.md)（多边形）、[Path](../harmonyos-references/ts-drawing-components-path.md)（路径）、[Rect](../harmonyos-references/ts-drawing-components-rect.md)（矩形）。以Circle的接口调用为例：

  ```
  1. Circle(value?: { width?: string | number, height?: string | number })
  ```

  该接口用于在页面绘制圆形，其中width用于设置圆形的宽度，height用于设置圆形的高度，圆形直径由宽高最小值确定。

  ```
  1. Circle({ width: 150, height: 150 })
  ```

  [Shape.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/Shape.ets#L27-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/kGKYuzb9Sf2cnsojTBKO1g/zh-cn_image_0000002552957928.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=F5DABCFB7575CB44DE9A6C362FF50B807DB33CD3A460BD2DF561976024C6D6DE)

## 形状视口viewPort

```
1. viewPort(value: { x?: number | string, y?: number | string, width?: number | string, height?: number | string })
```

形状视口viewPort指定用户空间中的一个矩形，该矩形映射到为关联的SVG元素建立的视区边界。viewPort属性的值包含x、y、width和height四个可选参数，x和y表示视区的左上角坐标，width和height表示其尺寸。

以下三个示例说明如何使用viewPort：

* 通过形状视口对图形进行放大与缩小。

  ```
  1. class Tmp {
  2. public x: number = 0;
  3. public y: number = 0;
  4. public width: number = 75;
  5. public height: number = 75;
  6. }

  8. class TmpOne {
  9. public x: number = 0;
  10. public y: number = 0;
  11. public width: number = 300;
  12. public height: number = 300;
  13. }

  15. @Entry
  16. @Component
  17. struct ViewPort1 {
  18. viep: Tmp = new Tmp();
  19. viep1: TmpOne = new TmpOne();

  21. build() {
  22. Column() {
  23. // 画一个宽高都为75的圆
  24. // 请将$r('app.string.OriginalSizeCircle')替换为实际资源文件，在本示例中该资源文件的value值为"原始尺寸Circle组件"
  25. Text($r('app.string.OriginalSizeCircle')).margin({ top: 20 })
  26. Circle({ width: 75, height: 75 }).fill('rgb(39, 135, 217)')

  28. Row({ space: 10 }) {
  29. Column() {
  30. // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为75的viewPort。
  31. // 用一个蓝色的矩形来填充viewPort，在viewPort中绘制一个直径为75的圆。
  32. // 绘制结束，viewPort会根据组件宽高放大两倍。
  33. // 请将$r('app.string.EnlargedCircle')替换为实际资源文件，在本示例中该资源文件的value值为"shape内放大的Circle组件"
  34. Text($r('app.string.EnlargedCircle'))
  35. Shape() {
  36. Rect().width('100%').height('100%').fill('rgb(39, 135, 217)')
  37. Circle({ width: 75, height: 75 }).fill('rgb(213, 213, 213)')
  38. }
  39. .viewPort(this.viep)
  40. .width(150)
  41. .height(150)
  42. .backgroundColor('rgb(23, 169, 141)')
  43. }

  45. Column() {
  46. // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为300的viewPort。
  47. // 用一个绿色的矩形来填充viewPort，在viewPort中绘制一个直径为75的圆。
  48. // 绘制结束，viewPort会根据组件宽高缩小两倍。
  49. // 请将$r('app.string.ShrunkCircle')替换为实际资源文件，在本示例中该资源文件的value值为"Shape内缩小的Circle组件"
  50. Text($r('app.string.ShrunkCircle'))
  51. Shape() {
  52. Rect().width('100%').height('100%').fill('rgb(213, 213, 213)')
  53. Circle({ width: 75, height: 75 }).fill('rgb(39, 135, 217)')
  54. }
  55. .viewPort(this.viep1)
  56. .width(150)
  57. .height(150)
  58. .backgroundColor('rgb(23, 169, 141)')
  59. }
  60. }
  61. }
  62. }
  63. }
  ```

  [ViewPort1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/ViewPort1.ets#L16-L80)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/vRneTajZQGGkBao4KrRbzw/zh-cn_image_0000002583477929.png?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=E470203A61DD886769C40905AB0438980C61A0C49E79C41EA8A0B90AB16040BF)
* 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewPort。用一个蓝色的矩形来填充viewPort，在viewPort中绘制一个半径为75的圆。

  ```
  1. class TmpTwo {
  2. public x: number = 0;
  3. public y: number = 0;
  4. public width: number = 300;
  5. public height: number = 300;
  6. }

  8. @Entry
  9. @Component
  10. struct ViewPort2 {
  11. viep: TmpTwo = new TmpTwo();

  13. build() {
  14. Column() {
  15. Shape() {
  16. Rect().width('100%').height('100%').fill('#0097D4')
  17. Circle({ width: 150, height: 150 }).fill('#E87361')
  18. }
  19. .viewPort(this.viep)
  20. .width(300)
  21. .height(300)
  22. .backgroundColor('#F5DC62')
  23. }
  24. }
  25. }
  ```

  [ViewPort2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/ViewPort2.ets#L16-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/XR_Sz-ZkTrWycRkTkp83Qw/zh-cn_image_0000002552798280.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=CBC68880F9810B4B0BE6E7689844FFD4C96DD95001171C47CCC6D77500705CDF)
* 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewPort。用一个蓝色的矩形来填充viewPort，在viewPort中绘制一个半径为75的圆，将viewPort向右方和下方各平移150。

  ```
  1. class TmpThree {
  2. public x: number = -150;
  3. public y: number = -150;
  4. public width: number = 300;
  5. public height: number = 300;
  6. }

  8. @Entry
  9. @Component
  10. struct ViewPort3 {
  11. viep: TmpThree = new TmpThree();

  13. build() {
  14. Column() {
  15. Shape() {
  16. Rect().width('100%').height('100%').fill('#0097D4')
  17. Circle({ width: 150, height: 150 }).fill('#E87361')
  18. }
  19. .viewPort(this.viep)
  20. .width(300)
  21. .height(300)
  22. .backgroundColor('#F5DC62')
  23. }
  24. }
  25. }
  ```

  [ViewPort3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/ViewPort3.ets#L16-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/PVG--0ynSa-nAZr7ax8QAQ/zh-cn_image_0000002583437975.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=A67DB44E37847EE540CF1BE9C197661245724CCD2FBDBA16CF39C8457D6FF443)

## 自定义样式

说明

示例通过commands来绘制路径，commands参数说明请参考[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)。

绘制组件支持通过各种属性更改组件样式。

* 通过[fill](../harmonyos-references/ts-drawing-components-path.md#fill)可以设置组件填充区域颜色。

  ```
  1. Path()
  2. .width(100)
  3. .height(100)
  4. .commands('M150 0 L300 300 L0 300 Z')
  5. .fill('#E87361')
  6. .strokeWidth(0)
  ```

  [Fill.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/Fill.ets#L21-L28)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/3OSRr3SHSjKM0MNcSmV7lg/zh-cn_image_0000002552957930.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=789462BB019CC864C79EF6B6A81983E7EAF94EFB41F0625451E9C7BB30A7FEED)
* 通过[stroke](../harmonyos-references/ts-drawing-components-path.md#stroke)可以设置组件边框颜色。

  ```
  1. Path()
  2. .width(100)
  3. .height(100)
  4. .fillOpacity(0)
  5. .commands('M150 0 L300 300 L0 300 Z')
  6. .stroke(Color.Red)
  ```

  [Stroke.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/Stroke.ets#L21-L28)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/G7rgjCWRSzudKWZWcFHvIg/zh-cn_image_0000002583477931.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=92D1FFDECCE6F38F39627A403970EA94F33783EBDA7149C01713378CEDFF05CC)
* 通过[strokeOpacity](../harmonyos-references/ts-drawing-components-path.md#strokeopacity)可以设置边框透明度。

  ```
  1. Path()
  2. .width(100)
  3. .height(100)
  4. .fillOpacity(0)
  5. .commands('M150 0 L300 300 L0 300 Z')
  6. .stroke(Color.Red)
  7. .strokeWidth(10)
  8. .strokeOpacity(0.2)
  ```

  [StrokeOpacity.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/StrokeOpacity.ets#L21-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/MFaFZMjUQ92N8LRaObhRdA/zh-cn_image_0000002552798282.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=635FEC04042EFE36978E7AF17FDE0ABDEE36F0862126F941B3AA7417644EAE4A)
* 通过[strokeLineJoin](../harmonyos-references/ts-drawing-components-polyline.md#strokelinejoin)可以设置线条拐角绘制样式。拐角绘制样式分为Bevel(使用斜角连接路径段)、Miter(使用尖角连接路径段)、Round(使用圆角连接路径段)。

  ```
  1. Polyline()
  2. .width(100)
  3. .height(100)
  4. .fillOpacity(0)
  5. .stroke(Color.Red)
  6. .strokeWidth(8)
  7. .points([[20, 0], [0, 100], [100, 90]])
  8. // 设置折线拐角处为圆弧
  9. .strokeLineJoin(LineJoinStyle.Round)
  ```

  [StrokeLineJoin.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/StrokeLineJoin.ets#L21-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/fEPy4HC6TsmjQtySz8QKQg/zh-cn_image_0000002583437977.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=C6D398435A345D6B64C176127C46BE09F706F7A6070BAA5B1C1B08B4EB70BD6A)
* 通过[strokeMiterLimit](../harmonyos-references/ts-drawing-components-polyline.md#strokemiterlimit)设置斜接长度与边框宽度比值的极限值。

  斜接长度表示外边框外边交点到内边交点的距离，边框宽度即[strokeWidth](../harmonyos-references/ts-drawing-components-polyline.md#strokewidth)属性的值。

  strokeMiterLimit取值需大于等于1，且在[strokeLineJoin](../harmonyos-references/ts-drawing-components-polyline.md#strokelinejoin)属性取值LineJoinStyle.Miter时生效。

  ```
  1. Polyline()
  2. .width(100)
  3. .height(100)
  4. .fillOpacity(0)
  5. .stroke(Color.Red)
  6. .strokeWidth(10)
  7. .points([[20, 0], [20, 100], [100, 100]])
  8. // 设置折线拐角处为尖角
  9. .strokeLineJoin(LineJoinStyle.Miter)
  10. // 设置斜接长度与线宽的比值
  11. .strokeMiterLimit(1/Math.sin(45))
  12. Polyline()
  13. .width(100)
  14. .height(100)
  15. .fillOpacity(0)
  16. .stroke(Color.Red)
  17. .strokeWidth(10)
  18. .points([[20, 0], [20, 100], [100, 100]])
  19. .strokeLineJoin(LineJoinStyle.Miter)
  20. .strokeMiterLimit(1.42)
  ```

  [StrokeMiterLimit.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/StrokeMiterLimit.ets#L21-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/3McfVm8qQ4O0nf3yZvvaUA/zh-cn_image_0000002552957932.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=CBB9BD8D8F5769E73811EDC741CEE73F2DBE42D4856C59738A9365A153114FA7)
* 通过[antiAlias](../harmonyos-references/ts-drawing-components-circle.md#antialias)设置是否开启抗锯齿，默认值为true（开启抗锯齿）。

  ```
  1. // 开启抗锯齿
  2. Circle()
  3. .width(150)
  4. .height(200)
  5. .fillOpacity(0)
  6. .strokeWidth(5)
  7. .stroke(Color.Black)
  ```

  [AntiAlias.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/AntiAlias.ets#L22-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/b9nCOTUrRne0aYxrKgoMwQ/zh-cn_image_0000002583477933.png?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=89392601D0D0276234404A9BA4F95F14F0ADAA110479499BDF53BA7C37E19642)

  ```
  1. // 关闭抗锯齿
  2. Circle()
  3. .width(150)
  4. .height(200)
  5. .fillOpacity(0)
  6. .strokeWidth(5)
  7. .stroke(Color.Black)
  8. .antiAlias(false)
  ```

  [AntiAlias.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/AntiAlias.ets#L32-L41)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/EAoC6hXET4-Qc9_o_gvR5A/zh-cn_image_0000002552798284.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=DB1E58855D2E998409E2C30CE784733A0F46D41CEBC5B5909C7E88E3E5D7CDAB)
* 通过[mesh](../harmonyos-references/ts-drawing-components-shape.md#mesh8)设置网格效果，实现图像局部扭曲。

  说明

  示例通过commands来绘制路径，commands参数说明请参考[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)。

  ```
  1. import { FrameNode, NodeController, RenderNode } from '@kit.ArkUI';
  2. import { image } from '@kit.ImageKit';
  3. import { drawing } from '@kit.ArkGraphics2D';

  5. let offCanvas: OffscreenCanvas = new OffscreenCanvas(150, 150);
  6. let ctx = offCanvas.getContext('2d');

  8. class DrawingRenderNode extends RenderNode {
  9. private verts_: Array<number> = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360];

  11. setVerts(verts: Array<number>): void {
  12. this.verts_ = verts
  13. }

  15. async draw(context: DrawContext) {
  16. const canvas = context.canvas;
  17. let pixelMap = ctx.getPixelMap(0, 0, 150, 150);
  18. const brush = new drawing.Brush(); // 只支持brush，使用pen没有绘制效果。
  19. canvas.attachBrush(brush);
  20. let verts: number[] = [0, 0, 410, 0, 50, 0, 0, 180, 50, 180, 410, 180, 0, 360, 410, 360, 50, 360];
  21. ; // 18
  22. canvas.drawPixelMapMesh(pixelMap, 2, 2, verts, 0, null, 0);
  23. canvas.detachBrush();
  24. }
  25. }

  27. const renderNode = new DrawingRenderNode();
  28. renderNode.frame = {
  29. x: 0,
  30. y: 0,
  31. width: 150,
  32. height: 150
  33. };

  35. class MyNodeController extends NodeController {
  36. private rootNode: FrameNode | null = null;

  38. makeNode(uiContext: UIContext): FrameNode | null {
  39. this.rootNode = new FrameNode(uiContext);

  41. const rootRenderNode = this.rootNode.getRenderNode();
  42. if (rootRenderNode !== null) {
  43. rootRenderNode.appendChild(renderNode);
  44. }
  45. return this.rootNode;
  46. }
  47. }

  49. @Entry
  50. @Component
  51. struct Mesh {
  52. private myNodeController: MyNodeController = new MyNodeController();
  53. @State showShape: boolean = false;
  54. @State pixelMap: image.PixelMap | undefined = undefined;
  55. @State shapeWidth: number = 150;
  56. @State strokeWidth: number = 1;
  57. @State meshArray: Array<number> = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360];

  59. aboutToAppear(): void {
  60. // 'resources/base/media/image.png'需要替换为开发者所需的图像资源文件
  61. let img: ImageBitmap = new ImageBitmap('resources/base/media/image.png');
  62. ctx.drawImage(img, 0, 0, 100, 100);
  63. this.pixelMap = ctx.getPixelMap(0, 0, 150, 150);
  64. }

  66. build() {
  67. Column() {
  68. Image(this.pixelMap)
  69. .backgroundColor('#86C5E3')
  70. .width(150)
  71. .height(150)
  72. .onClick(() => {
  73. // 'resources/base/media/image.png'需要替换为开发者所需的图像资源文件
  74. let img: ImageBitmap = new ImageBitmap('resources/base/media/image.png');
  75. ctx.drawImage(img, 0, 0, 100, 100);
  76. this.pixelMap = ctx.getPixelMap(1, 1, 150, 150);
  77. this.myNodeController.rebuild();
  78. this.strokeWidth += 1;
  79. })

  81. NodeContainer(this.myNodeController)
  82. .width(150)
  83. .height(150)
  84. .backgroundColor(Color.Grey)
  85. .onClick(() => {
  86. this.meshArray = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360, 0];
  87. })
  88. Button('change mesh')
  89. .margin(5)
  90. .onClick(() => {
  91. this.meshArray = [0, 0, 410, 0, 50, 0, 0, 180, 50, 180, 410, 180, 0, 360, 410, 360, 50, 360];
  92. })
  93. Button('Show Shape')
  94. .margin(5)
  95. .onClick(() => {
  96. this.showShape = !this.showShape;
  97. })

  99. if (this.showShape) {
  100. Shape(this.pixelMap) {
  101. Path().width(150).height(60).commands('M0 0 L400 0 L400 150 Z')
  102. }
  103. .fillOpacity(0.2)
  104. .backgroundColor(Color.Grey)
  105. .width(this.shapeWidth)
  106. .height(150)
  107. .mesh(this.meshArray, 2, 2)
  108. .fill(0x317AF7)
  109. .stroke(0xEE8443)
  110. .strokeWidth(this.strokeWidth)
  111. .strokeLineJoin(LineJoinStyle.Miter)
  112. .strokeMiterLimit(5)

  114. Shape(this.pixelMap) {
  115. Path().width(150).height(60).commands('M0 0 L400 0 L400 150 Z')
  116. }
  117. .fillOpacity(0.2)
  118. .backgroundColor(Color.Grey)
  119. .width(this.shapeWidth)
  120. .height(150)
  121. .fill(0x317AF7)
  122. .stroke(0xEE8443)
  123. .strokeWidth(this.strokeWidth)
  124. .strokeLineJoin(LineJoinStyle.Miter)
  125. .strokeMiterLimit(5)
  126. .onDragStart(() => {
  127. })

  129. // mesh只对shape传入pixelMap时生效，此处不生效
  130. Shape() {
  131. Path().width(150).height(60).commands('M0 0 L400 0 L400 150 Z')
  132. }
  133. .fillOpacity(0.2)
  134. .backgroundColor(Color.Grey)
  135. .width(this.shapeWidth)
  136. .height(150)
  137. .mesh(this.meshArray, 2, 2)
  138. .fill(0x317AF7)
  139. .stroke(0xEE8443)
  140. .strokeWidth(this.strokeWidth)
  141. .strokeLineJoin(LineJoinStyle.Miter)
  142. .strokeMiterLimit(5)
  143. .onClick(() => {
  144. this.pixelMap = undefined;
  145. })
  146. }
  147. }
  148. }
  149. }
  ```

  [Mesh.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/Mesh.ets#L16-L166)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/UC5T26G4S02jZmeu8oSZLw/zh-cn_image_0000002583437979.png?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=CD5D0AFF14832EC71612DFF81615B7237CBFB1C53776307A52F3F42C87DF3A6F)

## 场景示例

### 绘制封闭路径

在Shape的(-80, -5)点绘制一个封闭路径，填充颜色0x317AF7，线条宽度3，边框颜色红色，拐角样式锐角（默认值）。

说明

示例通过commands来绘制路径，commands参数说明请参考[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)。

```
1. @Entry
2. @Component
3. struct ShapeExample {
4. build() {
5. Column({ space: 10 }) {
6. Shape() {
7. Path().width(200).height(60).commands('M0 0 L400 0 L400 150 Z')
8. }
9. .viewPort({
10. x: -80,
11. y: -5,
12. width: 500,
13. height: 300
14. })
15. .fill('rgb(213, 213, 213)')
16. .stroke('rgb(39, 135, 217)')
17. .strokeWidth(3)
18. .strokeLineJoin(LineJoinStyle.Miter)
19. .strokeMiterLimit(5)
20. }.width('100%').margin({ top: 15 })
21. }
22. }
```

[ShapeExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/ShapeExample.ets#L16-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/CmFOsz7MR_-jm7oakBzvZg/zh-cn_image_0000002552957934.png?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=E78E6CB278031C27D5620FB351C8BA843C056C8B0C192C48F1324DAB45FFED10)

### 绘制圆和圆环

绘制一个直径为150的圆，和一个直径为150、线条为红色虚线的圆环（宽高设置不一致时以短边为直径）。

说明

本示例通过strokeDashArray属性设置边框间隙来实现红色虚线的圆环，strokeDashArray属性参考[strokeDashArray](../harmonyos-references/ts-drawing-components-shape.md#strokedasharray)。

```
1. @Entry
2. @Component
3. struct CircleExample {
4. build() {
5. Column({ space: 10 }) {
6. // 绘制一个直径为150的圆
7. Circle({ width: 150, height: 150 })
8. // 绘制一个直径为150、线条为红色虚线的圆环
9. Circle()
10. .width(150)
11. .height(200)
12. .fillOpacity(0)
13. .strokeWidth(3)
14. .stroke(Color.Red)
15. .strokeDashArray([1, 2])
16. // ...
17. }.width('100%')
18. }
19. }
```

[CircleExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/CircleExample.ets#L16-L46)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/a6II6i1LROeSl7sUBKbWfg/zh-cn_image_0000002583477935.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=F8578B3D5DF6A13909EFA7ADDB3FF7E7D0270AF46B0510A2611C22383C0C85A2)

### UI视觉属性作用效果

说明

[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)、[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)等通用属性作用于组件的背景区域，而不会在组件具体的内容区域生效。

```
1. @Entry
2. @Component
3. struct CircleExample {
4. build() {
5. Column({ space: 10 }) {
6. // ...
7. // 绘制一个直径为150的圆
8. Circle()
9. .width(150)
10. .height(200)
11. .backgroundColor(Color.Pink) // 会生效在一个150*200大小的矩形区域，而非仅在绘制的一个直径为150的圆形区域
12. }.width('100%')
13. }
14. }
```

[CircleExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ShapeDrawing/entry/src/main/ets/pages/CircleExample.ets#L17-L45)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/lH4Jbc6XQxSyjviqlrKUBQ/zh-cn_image_0000002552798286.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233947Z&HW-CC-Expire=86400&HW-CC-Sign=2799F40C2F2678FE0B8F3D8CAA0A52646FD14A1364C08890ADF05E09F9A226F6)
