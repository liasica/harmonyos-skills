---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-arkts
title: 画布的获取与绘制结果的显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 画布的获取与绘制结果的显示 > 画布的获取与绘制结果的显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:20+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:7d51af0ae60aa5a17b06836a743f1a1b23f16c18d373302a71df6adb84ba16bf
---

## 场景介绍

Canvas即画布，提供绘制基本图形的能力，用于在屏幕上绘制图形和处理图形。开发者可以通过Canvas实现自定义的绘图效果，增强应用的用户体验。

Canvas是图形绘制的核心，本章中提到的所有绘制操作（包括基本图形的绘制、文字的绘制、图片的绘制、图形变换等）都是基于Canvas的。

目前ArkTS有两种获取Canvas的方式：[获取可直接显示的Canvas画布](canvas-get-result-draw-arkts.md#获取可直接显示的canvas画布)、[获取离屏的Canvas](canvas-get-result-draw-arkts.md#离屏canvas画布的获取与显示)，前者在调用绘制接口之后无需进行额外的操作即可完成绘制结果的上屏显示，而后者需要依靠已有的显示手段来显示绘制结果。

## 获取可直接显示的Canvas画布

通过[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)获取可直接上屏显示的Canvas画布。

1. 导入依赖的相关文件。

   ```typescript
   import { UIContext, NodeController, FrameNode, RenderNode, DrawContext} from '@kit.ArkUI';
   ```

   ```typescript
   import { drawing } from '@kit.ArkGraphics2D';
   ```
2. 添加自定义RenderNode。

   ```typescript
   // 2. 自定义 RenderNode
   class MyRenderNodeDirectDisplay extends RenderNode {
     async draw(context: DrawContext) {
       const canvas = context.canvas;
       if (canvas === null) {
         console.error('Canvas is null.');
         return;
       }
       // 4. 自定义的绘制相关操作
       const brush = new drawing.Brush();
       if (brush === null) {
         console.error('Brush is null.');
         return;
       } else {
         brush.setColor({red: 255, blue: 0, green: 0, alpha: 255});
         canvas.attachBrush(brush);
         canvas.drawRect({left: 0, right: 300, top: 0, bottom: 300});
         canvas.detachBrush();
       }
     }
   }
   ```
3. 添加自定义[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)。

   ```typescript
   // 3. 自定义 NodeController
   class MyNodeControllerDirectDisplay extends NodeController {
     private rootNode: FrameNode | null = null;
     private myRenderNode = new MyRenderNodeDirectDisplay();

     makeNode(uiContext: UIContext): FrameNode {
       this.rootNode = new FrameNode(uiContext);
       if (this.rootNode === null) {
         return this.rootNode;
       }
       const renderNode = this.rootNode.getRenderNode();
       if (renderNode !== null) {
         this.myRenderNode.backgroundColor = 0xffffffff;
         this.myRenderNode.frame = { x: 0, y: 0, width: 4800, height: 4800 };
         this.myRenderNode.pivot = { x: 0.2, y: 0.8 };
         this.myRenderNode.scale = { x: 1, y: 1 };
         renderNode.appendChild(this.myRenderNode);
         renderNode.clipToFrame = true;
       }
       return this.rootNode;
     }
   }
   ```
4. 重写自定义RenderNode的[draw()](../harmonyos-references/js-apis-arkui-rendernode.md#draw)函数，获取Canvas进行自定义的绘制操作，即本章下文中的内容。

   ```typescript
   async draw(context: DrawContext) {
     const canvas = context.canvas;
     if (canvas === null) {
       console.error('Canvas is null.');
       return;
     }
     // 4. 自定义的绘制相关操作
     const brush = new drawing.Brush();
     if (brush === null) {
       console.error('Brush is null.');
       return;
     } else {
       brush.setColor({red: 255, blue: 0, green: 0, alpha: 255});
       canvas.attachBrush(brush);
       canvas.drawRect({left: 0, right: 300, top: 0, bottom: 300});
       canvas.detachBrush();
     }
   }
   ```
5. 将自定义NodeController进行显示。

   ```typescript
   @Entry
   @Component
   struct RenderTest {
     @State message: string = 'hello';
     myNodeController_1 = new MyNodeControllerDirectDisplay();
     myNodeController_2 = new MyNodeControllerIndirectDisplay();

     build() {
       Row() {
         Column() {
           Column(){
             Text($r('app.string.DirectCanvas'))
             // 直接上屏显示画布
             NodeContainer(this.myNodeController_1)
               .width('100%')
               .height('40%')
           }
           Column(){
             Text($r('app.string.OffScreenCanvas'))
             // 离屏画布
             NodeContainer(this.myNodeController_2)
               .width('100%')
               .height('40%')
               .margin({ top: 20 })
           }
         }
       }
     }
   }
   ```

## 离屏Canvas画布的获取与显示

1. 导入依赖的相关文件。

   ```typescript
   import { UIContext, NodeController, FrameNode, RenderNode, DrawContext} from '@kit.ArkUI';
   import { image } from '@kit.ImageKit';
   import { taskpool } from '@kit.ArkTS';
   import { drawing } from '@kit.ArkGraphics2D';
   ```
2. 添加自定义RenderNode。
3. 添加自定义[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)。
4. 在MyNodeController的aboutToAppear()函数中创建PixelMap。
5. 重写自定义RenderNode的[draw()](../harmonyos-references/js-apis-arkui-rendernode.md#draw)函数，在其中获取离屏Canvas进行绘制：

   1. 利用4中创建的PixelMap构造离屏Canvas。
   2. 对离屏Canvas进行自定义的绘制操作。
   3. 将离屏Canvas的绘制结果交给RenderNode。

   ```typescript
   // 2. 自定义RenderNode
   export class MyRenderNodeIndirectDisplay extends RenderNode {
     private pixelMap: image.PixelMap | null = null;
     setPixelMap(pixelMap: image.PixelMap) {
       this.pixelMap = pixelMap;
     }

     async draw(context: DrawContext) {
       const canvas = context.canvas;
       if (this.pixelMap != null) {
         // 5.1 利用4中创建的PixelMap构造离屏Canvas
         const canvas_ = new drawing.Canvas(this.pixelMap);

         // 5.2 离屏绘制
         const brush = new drawing.Brush();
         brush.setColor({ alpha: 255, red: 0, green: 0, blue: 255 });
         canvas_.attachBrush(brush);
         canvas_.drawRect({ left: 150, right: 575, top: 0, bottom: 600 });
         canvas_.detachBrush();

         // 5.3 将离屏Canvas的绘制结果交给RenderNode
         canvas.drawImage(this.pixelMap, 0, 0);
       }
     }
   }

   @Concurrent
   async function createPixelMapAsync() {
     // 4000000为需要创建的像素buffer大小，取值为：height * width *4
     const color : ArrayBuffer = new ArrayBuffer(4000000);
     let opts : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 1000, width: 1000 } };
     const pixel = await image.createPixelMap(color, opts);
     return pixel;
   }

   // 3. 自定义NodeController
   export class MyNodeControllerIndirectDisplay extends NodeController {
     private rootNode: FrameNode | null = null;
     private myRenderNode = new MyRenderNodeIndirectDisplay();

     // 4. 在MyNodeController的aboutToAppear中创建PixelMap
     aboutToAppear(): void {
       let task = new taskpool.Task(createPixelMapAsync);
       taskpool.execute(task).then((pixel:Object)=>{
         this.myRenderNode.setPixelMap(pixel as image.PixelMap);
         this.myRenderNode.invalidate();
       })
     }

     makeNode(uiContext: UIContext): FrameNode {
       this.rootNode = new FrameNode(uiContext);
       if (this.rootNode === null) {
         return this.rootNode;
       }

       const renderNode = this.rootNode.getRenderNode();
       if (renderNode !== null) {
         this.myRenderNode.backgroundColor = 0xffffffff;
         this.myRenderNode.frame = { x: 0, y: 0, width: 4800, height: 4800 };
         this.myRenderNode.pivot = { x: 0.2, y: 0.8 };
         this.myRenderNode.scale = { x: 1, y: 1 };
         renderNode.appendChild(this.myRenderNode);
         renderNode.clipToFrame = true;
       }
       return this.rootNode;
     }
   }
   ```
6. 将自定义NodeController进行显示。

   ```typescript
   @Entry
   @Component
   struct RenderTest {
     @State message: string = 'hello';
     myNodeController_1 = new MyNodeControllerDirectDisplay();
     myNodeController_2 = new MyNodeControllerIndirectDisplay();

     build() {
       Row() {
         Column() {
           Column(){
             Text($r('app.string.DirectCanvas'))
             // 直接上屏显示画布
             NodeContainer(this.myNodeController_1)
               .width('100%')
               .height('40%')
           }
           Column(){
             Text($r('app.string.OffScreenCanvas'))
             // 离屏画布
             NodeContainer(this.myNodeController_2)
               .width('100%')
               .height('40%')
               .margin({ top: 20 })
           }
         }
       }
     }
   }
   ```

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
