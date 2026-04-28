---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-arkts
title: 画布的获取与绘制结果的显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 画布的获取与绘制结果的显示 > 画布的获取与绘制结果的显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7f6a45d0594255330b0735bd21910ffc63252aa6a3efbe15f83af1a9de4a9bd
---

## 场景介绍

Canvas即画布，提供绘制基本图形的能力，用于在屏幕上绘制图形和处理图形。开发者可以通过Canvas实现自定义的绘图效果，增强应用的用户体验。

Canvas是图形绘制的核心，本章中提到的所有绘制操作（包括基本图形的绘制、文字的绘制、图片的绘制、图形变换等）都是基于Canvas的。

目前ArkTS有两种获取Canvas的方式：[获取可直接显示的Canvas画布](canvas-get-result-draw-arkts.md#获取可直接显示的canvas画布)、[获取离屏的Canvas](canvas-get-result-draw-arkts.md#离屏canvas画布的获取与显示)，前者在调用绘制接口之后无需进行额外的操作即可完成绘制结果的上屏显示，而后者需要依靠已有的显示手段来显示绘制结果。

## 获取可直接显示的Canvas画布

通过[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)获取可直接上屏显示的Canvas画布。

1. 导入依赖的相关文件。

   ```
   1. import { UIContext, NodeController, FrameNode, RenderNode, DrawContext} from '@kit.ArkUI';
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L18-L20)

   ```
   1. import { drawing } from '@kit.ArkGraphics2D';
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L23-L25)
2. 添加自定义RenderNode。

   ```
   1. // 2. 自定义 RenderNode
   2. class MyRenderNodeDirectDisplay extends RenderNode {
   3. async draw(context: DrawContext) {
   4. const canvas = context.canvas;
   5. if (canvas === null) {
   6. console.error('Canvas is null.');
   7. return;
   8. }
   9. // 4. 自定义的绘制相关操作
   10. const brush = new drawing.Brush();
   11. if (brush === null) {
   12. console.error('Brush is null.');
   13. return;
   14. } else {
   15. brush.setColor({red: 255, blue: 0, green: 0, alpha: 255});
   16. canvas.attachBrush(brush);
   17. canvas.drawRect({left: 0, right: 300, top: 0, bottom: 300});
   18. }
   19. }
   20. }
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L28-L51)
3. 添加自定义[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)。

   ```
   1. // 3. 自定义 NodeController
   2. class MyNodeControllerDirectDisplay extends NodeController {
   3. private rootNode: FrameNode | null = null;
   4. private myRenderNode = new MyRenderNodeDirectDisplay();

   6. makeNode(uiContext: UIContext): FrameNode {
   7. this.rootNode = new FrameNode(uiContext);
   8. if (this.rootNode === null) {
   9. return this.rootNode;
   10. }
   11. const renderNode = this.rootNode.getRenderNode();
   12. if (renderNode !== null) {
   13. this.myRenderNode.backgroundColor = 0xffffffff;
   14. this.myRenderNode.frame = { x: 0, y: 0, width: 4800, height: 4800 };
   15. this.myRenderNode.pivot = { x: 0.2, y: 0.8 };
   16. this.myRenderNode.scale = { x: 1, y: 1 };
   17. renderNode.appendChild(this.myRenderNode);
   18. renderNode.clipToFrame = true;
   19. }
   20. return this.rootNode;
   21. }
   22. }
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L53-L76)
4. 重写自定义RenderNode的[draw()](../harmonyos-references/js-apis-arkui-rendernode.md#draw)函数，获取Canvas进行自定义的绘制操作，即本章下文中的内容。

   ```
   1. async draw(context: DrawContext) {
   2. const canvas = context.canvas;
   3. if (canvas === null) {
   4. console.error('Canvas is null.');
   5. return;
   6. }
   7. // 4. 自定义的绘制相关操作
   8. const brush = new drawing.Brush();
   9. if (brush === null) {
   10. console.error('Brush is null.');
   11. return;
   12. } else {
   13. brush.setColor({red: 255, blue: 0, green: 0, alpha: 255});
   14. canvas.attachBrush(brush);
   15. canvas.drawRect({left: 0, right: 300, top: 0, bottom: 300});
   16. }
   17. }
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L31-L49)
5. 将自定义NodeController进行显示。

   ```
   1. @Entry
   2. @Component
   3. struct RenderTest {
   4. @State message: string = 'hello';
   5. myNodeController_1 = new MyNodeControllerDirectDisplay();
   6. myNodeController_2 = new MyNodeControllerIndirectDisplay();

   8. build() {
   9. Row() {
   10. Column() {
   11. Column(){
   12. Text($r('app.string.DirectCanvas'))
   13. // 直接上屏显示画布
   14. NodeContainer(this.myNodeController_1)
   15. .width('100%')
   16. .height('40%')
   17. }
   18. Column(){
   19. Text($r('app.string.OffScreenCanvas'))
   20. // 离屏画布
   21. NodeContainer(this.myNodeController_2)
   22. .width('100%')
   23. .height('40%')
   24. .margin({ top: 20 })
   25. }
   26. }
   27. }
   28. }
   29. }
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L147-L177)

## 离屏Canvas画布的获取与显示

1. 导入依赖的相关文件。

   ```
   1. import { UIContext, NodeController, FrameNode, RenderNode, DrawContext} from '@kit.ArkUI';
   2. import { image } from '@kit.ImageKit';
   3. import { taskpool } from '@kit.ArkTS';
   4. import { drawing } from '@kit.ArkGraphics2D';
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L17-L26)
2. 添加自定义RenderNode。
3. 添加自定义[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)。
4. 在MyNodeController的aboutToAppear()函数中创建PixelMap。
5. 重写自定义RenderNode的[draw()](../harmonyos-references/js-apis-arkui-rendernode.md#draw)函数，在其中获取离屏Canvas进行绘制：

   1. 利用4中创建的PixelMap构造离屏Canvas。
   2. 对离屏Canvas进行自定义的绘制操作。
   3. 将离屏Canvas的绘制结果交给RenderNode。

   ```
   1. // 2. 自定义RenderNode
   2. export class MyRenderNodeIndirectDisplay extends RenderNode {
   3. private pixelMap: image.PixelMap | null = null;
   4. setPixelMap(pixelMap: image.PixelMap) {
   5. this.pixelMap = pixelMap;
   6. }

   8. async draw(context: DrawContext) {
   9. const canvas = context.canvas;
   10. if (this.pixelMap != null) {
   11. // 5.1 利用4中创建的PixelMap构造离屏Canvas
   12. const canvas_ = new drawing.Canvas(this.pixelMap);

   14. // 5.2 离屏绘制
   15. const brush = new drawing.Brush();
   16. brush.setColor({ alpha: 255, red: 0, green: 0, blue: 255 });
   17. canvas_.attachBrush(brush);
   18. canvas_.drawRect({ left: 150, right: 575, top: 0, bottom: 600 });

   20. // 5.3 将离屏Canvas的绘制结果交给RenderNode
   21. canvas.drawImage(this.pixelMap, 0, 0);
   22. }
   23. }
   24. }

   26. @Concurrent
   27. async function createPixelMapAsync() {
   28. // 4000000为需要创建的像素buffer大小，取值为：height * width *4
   29. const color : ArrayBuffer = new ArrayBuffer(4000000);
   30. let opts : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 1000, width: 1000 } };
   31. const pixel = await image.createPixelMap(color, opts);
   32. return pixel;
   33. }

   35. // 3. 自定义NodeController
   36. export class MyNodeControllerIndirectDisplay extends NodeController {
   37. private rootNode: FrameNode | null = null;
   38. private myRenderNode = new MyRenderNodeIndirectDisplay();

   40. // 4. 在MyNodeController的aboutToAppear中创建PixeMap
   41. aboutToAppear(): void {
   42. let task = new taskpool.Task(createPixelMapAsync);
   43. taskpool.execute(task).then((pixel:Object)=>{
   44. this.myRenderNode.setPixelMap(pixel as image.PixelMap);
   45. this.myRenderNode.invalidate();
   46. })
   47. }

   49. makeNode(uiContext: UIContext): FrameNode {
   50. this.rootNode = new FrameNode(uiContext);
   51. if (this.rootNode === null) {
   52. return this.rootNode;
   53. }

   55. const renderNode = this.rootNode.getRenderNode();
   56. if (renderNode !== null) {
   57. this.myRenderNode.backgroundColor = 0xffffffff;
   58. this.myRenderNode.frame = { x: 0, y: 0, width: 4800, height: 4800 };
   59. this.myRenderNode.pivot = { x: 0.2, y: 0.8 };
   60. this.myRenderNode.scale = { x: 1, y: 1 };
   61. renderNode.appendChild(this.myRenderNode);
   62. renderNode.clipToFrame = true;
   63. }
   64. return this.rootNode;
   65. }
   66. }
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L78-L145)
6. 将自定义NodeController进行显示。

   ```
   1. @Entry
   2. @Component
   3. struct RenderTest {
   4. @State message: string = 'hello';
   5. myNodeController_1 = new MyNodeControllerDirectDisplay();
   6. myNodeController_2 = new MyNodeControllerIndirectDisplay();

   8. build() {
   9. Row() {
   10. Column() {
   11. Column(){
   12. Text($r('app.string.DirectCanvas'))
   13. // 直接上屏显示画布
   14. NodeContainer(this.myNodeController_1)
   15. .width('100%')
   16. .height('40%')
   17. }
   18. Column(){
   19. Text($r('app.string.OffScreenCanvas'))
   20. // 离屏画布
   21. NodeContainer(this.myNodeController_2)
   22. .width('100%')
   23. .height('40%')
   24. .margin({ top: 20 })
   25. }
   26. }
   27. }
   28. }
   29. }
   ```

   [CanvasGetResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/CanvasGetResult.ets#L147-L177)

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
