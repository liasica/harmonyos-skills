---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-drawing-capability-improve-performance
title: Drawing自绘制性能提升
breadcrumb: 最佳实践 > 图形 > 图形绘制 > Drawing自绘制性能提升
category: best-practices
scraped_at: 2026-04-28T08:20:52+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:bc228ebd4aefda693d3c473e77f1f9e674fe2e7e414f15e2643e6270eb76454c
---

## 概述

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布组件是用来显示自绘内容的组件，它具有保留历史绘制内容、增量绘制的特点。Canvas有[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)/[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)和[DrawingRenderingContext](../harmonyos-references/ts-drawingrenderingcontext.md)两套API，应用使用两套绘制API绘制的内容都可以在绑定的Canvas组件上显示。其中CanvasRenderingContext2D按照W3C标准封装了Native Drawing接口，可以方便快速复用Web应用的绘制逻辑，因此非常适用于Web应用和游戏、快速原型设计、数据可视化、在线绘图板、教学工具或创意应用等场景。

为了遵循W3C标准，实现过程中进行了多层的封装，涉及一些数据结构的转换，不如原生API那样接近硬件，因此对于性能要求比较高、绘制比较复杂，或者硬件依赖性比较强的场景（如高性能游戏开发、专业图形处理软件、桌面或移动应用等），使用Canvas CanvasRenderingContext2D绘制会存在一定的卡顿、掉帧等性能问题，此时可以直接使用Native Drawing接口自绘制替代Canvas CanvasRenderingContext2D绘制来提升绘制性能。

|  |  |  |
| --- | --- | --- |
| 方案 | 适用场景 | 特点 |
| 使用Canvas CanvasRenderingContext2D | Web应用和游戏、快速原型设计、数据可视化、在线绘图板、教学工具、创意应用 | 场景简单、跨平台、快捷灵活、兼容性强、开发维护成本低、性能要求低。 |
| 使用Native Drawing | 高性能游戏开发、专业图形处理软件、桌面或移动应用开发 | 场景复杂、资源管理精细、硬件依赖强、与平台深度集成、定制化、性能要求高。 |

## 原理机制

由于Canvas CanvasRenderingContext2D绘制本质上是对Native Drawing接口的封装，相对于直接使用Native Drawing接口，Canvas CanvasRenderingContext2D在实现过程中进行了多层的封装，涉及一些数据结构的转换。如果图片绘制比较复杂，执行的绘制指令可能会成倍数的增长，进而绘制性能下降的更加严重，导致卡顿、掉帧等问题。下面以实现在背景图上绘制1000个透明空心圆的玻璃效果来对比两者的性能差异。

## 场景示例

下图是一个绘制1000个透明空心圆与背景图融合的绘制场景，下面分别使用Canvas CanvasRenderingContext2D和Native侧的Drawing来实现该场景，并分析两者的性能差异。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/5eAgt3cqRg6MdEqxWpFnaA/zh-cn_image_0000002229450853.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=4779BED7A48EC5B6D5A1A15BF99E9ED3C1449C75F1507202DF2292700717660D "点击放大")

### 使用Canvas CanvasRenderingContext2D绘制

Canvas CanvasRenderingContext2D使用[globalCompositeOperation](../harmonyos-references/ts-canvasrenderingcontext2d.md#globalcompositeoperation)属性来实现各种图层混合模式，此处将该属性的值设置为destination-out来实现透明空心圆。具体实现步骤如下：

1. 使用自定义组件GlassCoverView来实现透明圆圈。在首页点击"Begin Draw"按钮，随机生成1000个0-1的位置列表。

   ```
   1. import GlassCoverView from './GlassCoverView';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State pointsToDraw: number[][] = [];

   8. /**
   9. * Make a list of 1000 0-1 positions and draw circles at the corresponding positions
   10. */
   11. startDraw(): void {
   12. this.pointsToDraw = [];
   13. for (let index = 0; index < 1000; index++) {
   14. this.pointsToDraw.push([Math.random(), Math.random()]);
   15. }
   16. }

   18. build() {
   19. Stack() {
   20. Image($r('app.media.layered_image'))
   21. .width('100%')
   22. .height('100%')
   23. // Transparent circle custom component, in which 1000 transparent circles are drawn
   24. GlassCoverView({ pointsToDraw: this.pointsToDraw })
   25. .width('100%')
   26. .height('100%')
   27. Row() {
   28. Button('Begin Draw')
   29. .width('100%')
   30. .height(40)
   31. }
   32. .padding({
   33. right: 16,
   34. bottom: 16,
   35. left: 16
   36. })
   37. .onClick(() => {
   38. this.startDraw();
   39. })
   40. }
   41. .alignContent(Alignment.Bottom)
   42. .width('100%')
   43. .height('100%')
   44. }
   45. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/ets/view/Index.ets#L17-L61)
2. GlassCoverView子页面使用@Watch装饰器，监控到首页位置列表数据pointsToDraw更新后，在页面上绘制1000个透明空心圆圈（具体参见 onDraw()方法）。

   ```
   1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';

   3. const DOMAIN = 0x0000;
   4. const TAG = 'GlassCoverView';
   5. const FORMAT = '%{public}s';

   7. /**
   8. * Glass cladding effect
   9. */
   10. @Preview
   11. @Component
   12. export default struct GlassCoverView {
   13. @Prop @Watch('onDraw') pointsToDraw: number[][] = [];
   14. private settings = new RenderingContextSettings(true);
   15. private renderContext = new CanvasRenderingContext2D(this.settings);
   16. private viewWidth: number = 0;
   17. private viewHeight: number = 0;

   19. build() {
   20. Stack() {
   21. Canvas(this.renderContext)
   22. .width('100%')
   23. .height('100%')
   24. .onAreaChange((_: Area, newValue: Area) => {
   25. this.handleAreaChange(newValue);
   26. })
   27. }
   28. .height('100%')
   29. .width('100%')
   30. }

   32. private handleAreaChange(area: Area): void {
   33. this.viewWidth = parseInt(area.width.toString());
   34. this.viewHeight = parseInt(area.height.toString());
   35. this.onDraw();
   36. }

   38. private onDraw(): void {
   39. const canvas = this.renderContext;
   40. canvas.reset();
   41. if (canvas === undefined) {
   42. return;
   43. }
   44. // Hollow transparent circle
   45. hiTraceMeter.startTrace('slow', 1);
   46. hilog.info(DOMAIN, TAG, FORMAT, 'debug: slow start');
   47. // Save drawing context
   48. canvas.save();
   49. // Clears the specified pixel within the given rectangle
   50. canvas.clearRect(0, 0, this.viewWidth, this.viewHeight);
   51. // Specifies the fill color of the drawing
   52. canvas.fillStyle = '#77CCCCCC';
   53. // Fill a rectangle
   54. canvas.fillRect(0, 0, this.viewWidth, this.viewHeight);
   55. // Draw a hollow circle
   56. canvas.globalCompositeOperation = 'destination-out';
   57. canvas.fillStyle = '#CCCCCC';
   58. this.pointsToDraw.forEach((xy: number[]) => {
   59. this.drawOneCell(canvas, xy[0] * this.viewWidth, xy[1] * this.viewHeight, this.getUIContext().px2vp(15));
   60. })
   61. canvas.fill();
   62. // Restore the saved drawing context
   63. canvas.restore();
   64. hilog.info(DOMAIN, TAG, FORMAT, 'debug: slow end');
   65. hiTraceMeter.finishTrace('slow', 1);
   66. }

   68. /**
   69. * Draw a circle according to the specified position and width
   70. */
   71. private drawOneCell(canvas: CanvasRenderer, x: number, y: number, width: number): void {
   72. canvas.moveTo(x + width, y);
   73. canvas.arc(x, y, width, 0, Math.PI * 2);
   74. }
   75. }
   ```

   [GlassCoverView.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/ets/view/GlassCoverView.ets#L17-L91)

   使用Canvas CanvasRenderingContext2D绘制的trace图，可以看到绘制1000个圆圈耗时14.9毫秒。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/tYxuvo4WQDGE4obFoUnmMg/zh-cn_image_0000002283607973.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=1DC1A9DFB346D20B318C5C904378AE56BC63DE5540763F53229144E9063155BF)

### 使用Native侧Drawing绘制

Native Drawing主要使用分层接口[OH\_Drawing\_CanvasSaveLayer()](../harmonyos-references/capi-drawing-canvas-h.md#oh_drawing_canvassavelayer)和融合接口[OH\_Drawing\_BrushSetBlendMode()](../harmonyos-references/capi-drawing-brush-h.md#oh_drawing_brushsetblendmode)来实现多图融合效果。通过在前端创建一个自绘制节点[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)，并将图形绘制上下文及背景图参数通过Native侧暴露的接口传入，由Native使用相应Drawing接口进行绘制。具体实现步骤如下：

1. 前端定义一个[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)自绘制渲染节点，将背景图this.pMap及图形绘制上下文context传入Native，调用Native侧的nativeOnDraw接口进行绘制。

   ```
   1. // entry\src\main\ets\pages\Index.ets
   2. // Define a RenderNode self-drawing RenderNode MyRenderNode, so as to draw with the interface of Native
   3. class MyRenderNode extends RenderNode {
   4. private drawType: DrawType = DrawType.NONE;
   5. private pMap: image.PixelMap | undefined = undefined; // background image

   7. draw(context: DrawContext): void {
   8. // Call the Native onDraw interface on the native side to draw, and pass in the background image this.pMap and the graphic drawing context as parameters
   9. testNapi.nativeOnDraw(666, context, uiContext?.vp2px(this.size.width), uiContext?.vp2px(this.size.height),
   10. this.drawType, this.pMap);
   11. }

   13. // Set the drawing type
   14. resetType(type: DrawType): void {
   15. this.drawType = type;
   16. }

   18. // Set the background picture
   19. setPixelMap(p: PixelMap): void {
   20. this.pMap = p;
   21. }
   22. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/ets/pages/Index.ets#L36-L57)

   新建一个自绘制渲染节点，并定义一个[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)，对该节点进行管理。

   ```
   1. // entry\src\main\ets\pages\Index.ets
   2. // Create a MyRenderNode object
   3. const newNode = new MyRenderNode();
   4. // Defines the size and location of the newNode
   5. newNode.frame = {
   6. x: 0,
   7. y: 0,
   8. width: 980,
   9. height: 1280
   10. };

   12. // Mount the MyRenderNode object node on the NodeContainer
   13. class MyNodeController extends NodeController {
   14. private rootNode: FrameNode | null = null;

   16. makeNode(uiContext: UIContext): FrameNode | null {
   17. this.rootNode = new FrameNode(uiContext);
   18. if (this.rootNode === null) {
   19. return null;
   20. }
   21. const renderNode = this.rootNode.getRenderNode();
   22. if (renderNode !== null) {
   23. renderNode.appendChild(newNode);
   24. }
   25. return this.rootNode;
   26. }
   27. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/ets/pages/Index.ets#L61-L87)
2. 在页面中将自绘制节点挂载到[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)上。

   ```
   1. // entry\src\main\ets\pages\Index.ets
   2. @Entry
   3. @Component
   4. struct Index {
   5. private myNodeController: MyNodeController = new MyNodeController();

   7. aboutToAppear(): void {
   8. const context: Context = this.getUIContext().getHostContext()!;
   9. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   10. resourceMgr.getRawFileContent('drawImage.jpg').then((fileData: Uint8Array) => {
   11. hilog.info(DOMAIN, TAG, FORMAT, `success in getRawFileContent`);
   12. const buffer = fileData.buffer.slice(0);
   13. const imageSource: image.ImageSource = image.createImageSource(buffer);
   14. imageSource.createPixelMap().then((pMap: image.PixelMap) => {
   15. // Self-drawing rendering node background map
   16. newNode.setPixelMap(pMap);
   17. }).catch((err: BusinessError) => {
   18. hilog.error(DOMAIN, TAG, FORMAT, `fail to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
   19. }).catch((err: BusinessError) => {
   20. hilog.error(DOMAIN, TAG, FORMAT,
   21. `fail to getRawFileContent, error code: ${err.code}, message: ${err.message}.`);
   22. });
   23. }).catch((err: BusinessError) => {
   24. hilog.error(DOMAIN, TAG, FORMAT,
   25. `callback getRawFileContent failed, error code: ${err.code}, message: ${err.message}.`);
   26. });
   27. }

   29. build() {
   30. Stack() {
   31. // Mount the self-drawn rendering node to NodeContainer
   32. NodeContainer(this.myNodeController)
   33. .height('100%')
   34. Row() {
   35. Button('Begin Draw')
   36. .width('100%')
   37. .height(40)
   38. .onClick(() => {
   39. newNode.resetType(DrawType.IMAGE);
   40. newNode.invalidate();
   41. })
   42. }
   43. .padding({
   44. right: 16,
   45. bottom: 16,
   46. left: 16
   47. })
   48. }
   49. .alignContent(Alignment.Bottom)
   50. .width('100%')
   51. .height('100%')
   52. }
   53. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/ets/pages/Index.ets#L91-L143)
3. Native侧暴露绘制接口nativeOnDraw()供前端调用，该接口绑定Native侧的OnDraw()函数，ArkTS传入的参数在该函数中处理。

   ```
   1. // entry\src\main\cpp\native_bridge.cpp
   2. EXTERN_C_START
   3. static napi_value Init(napi_env env, napi_value exports) {
   4. napi_property_descriptor desc[] = {
   5. // Expose the NativeOnDraw interface for the front-end to call and bind the native OnDraw function
   6. {"nativeOnDraw", nullptr, OnDraw, nullptr, nullptr, nullptr, napi_default, nullptr}};
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   10. EXTERN_C_END
   ```

   [native\_bridge.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/cpp/native_bridge.cpp#L172-L181)
4. 在OnDraw()函数中接收前端传入的参数，主要是图形绘制上下文与背景图。

   ```
   1. // entry\src\main\cpp\native_bridge.cpp
   2. static napi_value OnDraw(napi_env env, napi_callback_info info) {
   3. size_t argc = 6;
   4. napi_value args[6] = {nullptr};

   6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   8. int32_t id;
   9. napi_get_value_int32(env, args[0], &id);

   11. // Graphic drawing context parameters
   12. void *temp = nullptr;
   13. napi_unwrap(env, args[1], &temp);
   14. OH_Drawing_Canvas *canvas = reinterpret_cast<OH_Drawing_Canvas *>(temp);

   16. int32_t width;
   17. napi_get_value_int32(env, args[2], &width);

   19. int32_t height;
   20. napi_get_value_int32(env, args[3], &height);

   22. DRAWING_LOGI("OnDraw, width:%{public}d, height:%{public}d", width, height);
   23. int32_t drawOption;
   24. napi_get_value_int32(env, args[4], &drawOption);
   25. // Background image parameters
   26. NativePixelMap *nativePixelMap = OH_PixelMap_InitNativePixelMap(env, args[5]);
   27. if (drawOption == IMAGE) {
   28. // Call the fusion drawing interface to draw
   29. NativeOnDrawPixelMap(canvas, nativePixelMap);
   30. }
   31. return nullptr;
   32. }
   ```

   [native\_bridge.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/cpp/native_bridge.cpp#L137-L168)
5. 在NativeOnDrawPixelMap函数中实现透明圆圈绘制（主要使用[OH\_Drawing\_CanvasSaveLayer()](../harmonyos-references/capi-drawing-canvas-h.md#oh_drawing_canvassavelayer)分层接口及 [OH\_Drawing\_BrushSetBlendMode()](../harmonyos-references/capi-drawing-brush-h.md#oh_drawing_brushsetblendmode)融合接口得到图形融合效果）。

   ```
   1. // entry\src\main\cpp\native_bridge.cpp
   2. enum DrawType { NONE, PATH, TEXT, IMAGE };
   3. #define DRAW_MAX_NUM 1000 // Maximum number of drawn circles

   5. // Generate random coordinates
   6. static int RangedRand(int range_min, int range_max) {
   7. int r = ((double)rand() / RAND_MAX) * (range_max - range_min) + range_min;
   8. return r;
   9. }

   11. void DrawCircle(OH_Drawing_Path *path, int x, int y, int width) {
   12. OH_Drawing_PathMoveTo(path, x + width, y);
   13. OH_Drawing_Rect *rect = OH_Drawing_RectCreate(x - width, y - width, x + width, y + width);
   14. OH_Drawing_PathAddArc(path, rect, 0, 360);
   15. }

   17. // Scene draw by fusion of hollow circle and background image
   18. static void NativeOnDrawPixelMap(OH_Drawing_Canvas *canvas, NativePixelMap *nativeMap) {
   19. // Draw a background picture
   20. OH_Drawing_CanvasSave(canvas);
   21. OH_Drawing_PixelMap *pixelMap = OH_Drawing_PixelMapGetFromNativePixelMap(nativeMap);
   22. // Create a sampling option object
   23. OH_Drawing_SamplingOptions *sampling = OH_Drawing_SamplingOptionsCreate(FILTER_MODE_NEAREST, MIPMAP_MODE_NONE);
   24. // Acquiring a background image drawing area
   25. OH_Drawing_Rect *src = OH_Drawing_RectCreate(0, 0, 360, 693);
   26. // Create a render area
   27. OH_Drawing_Rect *dst = OH_Drawing_RectCreate(0, 0, 1300, 2800);
   28. // Create a brush
   29. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
   30. OH_Drawing_CanvasAttachBrush(canvas, brush);
   31. // Render the background image to the designated area of the canvas.
   32. OH_Drawing_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, sampling);
   33. OH_Drawing_CanvasDetachBrush(canvas);

   35. // Call hierarchical interface
   36. OH_Drawing_CanvasSaveLayer(canvas, dst, brush);

   38. // Painting mask layer
   39. OH_Drawing_Rect *rect2 = OH_Drawing_RectCreate(0, 0, 1300, 2800);
   40. OH_Drawing_Brush *brush2 = OH_Drawing_BrushCreate();
   41. // Set the brush color
   42. OH_Drawing_BrushSetColor(brush2, OH_Drawing_ColorSetArgb(0x77, 0xCC, 0xCC, 0xCC));
   43. OH_Drawing_CanvasAttachBrush(canvas, brush2);
   44. OH_Drawing_CanvasDrawRect(canvas, rect2);
   45. OH_Drawing_CanvasDetachBrush(canvas);

   47. OH_Drawing_Point *point = OH_Drawing_PointCreate(800, 1750);
   48. OH_Drawing_Brush *brush3 = OH_Drawing_BrushCreate();
   49. // Set the brush and blending mode of the circle.
   50. OH_Drawing_BrushSetBlendMode(brush3, BLEND_MODE_DST_OUT);
   51. OH_Drawing_CanvasAttachBrush(canvas, brush3);
   52. // Circle
   53. OH_Drawing_Path *path = OH_Drawing_PathCreate();
   54. int x = 0;
   55. int y = 0;
   56. for (int i = 0; i < DRAW_MAX_NUM; i++) {
   57. x = RangedRand(0, 1300);
   58. y = RangedRand(0, 2800);
   59. DrawCircle(path, x, y, 15);
   60. }
   61. OH_Drawing_CanvasDrawPath(canvas, path);

   63. // Destroy the object
   64. OH_Drawing_CanvasDetachBrush(canvas);
   65. OH_Drawing_RectDestroy(rect2);
   66. OH_Drawing_BrushDestroy(brush2);
   67. OH_Drawing_BrushDestroy(brush3);
   68. OH_Drawing_PointDestroy(point);
   69. OH_Drawing_BrushDestroy(brush);
   70. OH_Drawing_CanvasRestore(canvas);
   71. OH_Drawing_SamplingOptionsDestroy(sampling);
   72. OH_Drawing_RectDestroy(src);
   73. OH_Drawing_RectDestroy(dst);
   74. OH_Drawing_PathDestroy(path);
   75. OH_Drawing_PixelMapDissolve(pixelMap);
   76. }
   ```

   [native\_bridge.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/NdkDrawing/entry/src/main/cpp/native_bridge.cpp#L52-L127)

   使用Native侧Drawing绘制trace图，可以看到绘制1000个圆圈耗时2.4毫秒，相较于Canvas CanvasRenderingContext2D绘制有较大的性能提升。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Um2tHuJMRZGx9liCTsHHcw/zh-cn_image_0000002283528493.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=233CD4818DB566209764E1B4C6A4F048D9A2697BD5D7A01406F9D9492C4951A4)

## 效果对比

|  |  |  |
| --- | --- | --- |
| **方案** | **圆圈数量** | **耗时** |
| Canvas CanvasRenderingContext2D 画透明圈 | 1000 | 14.9毫秒 |
| Native Drawing画透明圈 | 1000 | 2.4毫秒 |

通过上述对比可以发现，在实现较大数量透明空心圆这样的复杂的绘制场景，相比于Canvas CanvasRenderingContext2D，使用Native [Drawing](../harmonyos-references/capi-drawing-canvas-h.md)可以得到明显的性能提升。以上只是实现透明空心圆融合场景，针对实心圆及其他融合场景（如[globalCompositeOperation](../harmonyos-references/ts-canvasrenderingcontext2d.md#globalcompositeoperation)属性的其他值），由于实现机制的不同，绘制指令数量也存在差异，从而性能数据会存在一些差异。实际应用中，可以根据实际情况，在对性能要求不高的情况采用Canvas CanvasRenderingContext2D，如果对性能要求比较高，建议使用Native [Drawing](../harmonyos-references/capi-drawing-canvas-h.md)进行绘制。

## 示例代码

* [Drawing自绘制性能提升](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/NdkDrawing)
