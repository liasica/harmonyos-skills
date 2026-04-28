---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reader-page-flip
title: 阅读器翻页
breadcrumb: 最佳实践 > 行业场景解决方案 > 新闻阅读 > 阅读器翻页
category: best-practices
scraped_at: 2026-04-28T08:21:55+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f3a28852870c798d6f97925b21de0e2100fd1865d9f092419d8f1047973e5ce8
---

## 概述

在文本阅读器应用上，翻页时可以使用不同的效果展示页面变更，通常有以下翻页效果：

* [上下翻页](bpta-reader-page-flip.md#section1232510531285)：向上或向下的滑动效果，适合垂直滚动的文本阅读（如电子书、长篇文章）。
* [覆盖翻页](bpta-reader-page-flip.md#section213018591812)：通过水平滑动使当前页面向左侧滑出显示下一页，上一页从左侧滑入覆盖当前页，形成连贯的过渡效果。
* [仿真翻页](bpta-reader-page-flip.md#section3853128914)：模拟真实纸张的弯曲、翻折动作，例如页面边缘的弧形变形与阴影投影，实现沉浸式的体验效果。

本文主要对上述翻页效果的实现进行讲解，旨在帮助开发者了解常见翻页动效开发的流程及实现细节。

## 上下翻页

### 场景描述

上下翻页时，页面内容沿着垂直方向移动。当用户向上滑动时，当前页面内容向上滑出屏幕顶部，同时下一页内容从屏幕底部滑入；向下滑动则相反（当前页向下滑出，上一页从顶部滑入）。实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/sUJgwTK1TgKSUPQ9vdLOog/zh-cn_image_0000002329710386.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002152Z&HW-CC-Expire=86400&HW-CC-Sign=244A4F5E364740DE6BB2C14237200658DF3057CE07103950FE4BD6B75A71B379 "点击放大")

### 实现原理

使用[List](../harmonyos-references/ts-container-list.md)组件作为容器组件，提供上下滑动的能力。使用[ListItem](../harmonyos-references/ts-container-listitem.md)组件存放每一页的内容。页面内容可以自行定义，本文使用Text组件展示文本内容。

### 开发步骤

1. 构建模拟数据。

   ```
   1. // entry/src/main/ets/view/UpDownFlipPage.ets
   2. @Link currentPageNum: number;
   3. private data: BasicDataSource = new BasicDataSource([]);
   4. // ...
   5. aboutToAppear(): void {
   6. for (let i = Constants.PAGE_FLIP_PAGE_START; i <= Constants.PAGE_FLIP_PAGE_END; i++) {
   7. this.data.pushItem(Constants.PAGE_FLIP_RESOURCE + i.toString());
   8. }
   9. // ...
   10. }
   ```

   [UpDownFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/UpDownFlipPage.ets#L24-L42)
2. 使用[List](../harmonyos-references/ts-container-list.md)组件实现上下翻页效果。

   ```
   1. // entry/src/main/ets/view/UpDownFlipPage.ets
   2. List({ initialIndex: this.currentPageNum - 1, scroller: this.scroller }) {
   3. LazyForEach(this.data, (item: string) => {
   4. ListItem() {
   5. Text($r(item))
   6. // ...
   7. }
   8. }, (item: string, index: number) => index + JSON.stringify(item))
   9. }
   10. // ...
   11. .onScrollIndex((firstIndex: number) => {
   12. this.currentPageNum = firstIndex + 1;
   13. })
   ```

   [UpDownFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/UpDownFlipPage.ets#L52-L79)

## 覆盖翻页

### 场景描述

覆盖翻页效果模拟卡片切换，新页面（上一页）从屏幕的左侧水平滑入，完全覆盖当前页面。当前页支持从屏幕另一侧滑出，滑出时显示下层新页面。在整个过程中页面没有弯曲或折叠效果，页面作为一个整体平面进行移动。效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/x9Lg3bGNQwqrikJd_0accA/zh-cn_image_0000002329870186.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002152Z&HW-CC-Expire=86400&HW-CC-Sign=91F781BEB95891B0273932CBF8E32171A5CD28292DA9CD025458289F6DBEA2C2 "点击放大")

### 实现原理

使用[Stack](../harmonyos-references/ts-container-stack.md)堆叠容器，存放1、2、3三个页面，借助图形变换的[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)平移属性，将上层页面向左平移屏幕宽度移至窗口左侧。使用[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件判断手势滑动方向及平移距离，依据滑动方向及平移距离，执行1页面向右平移滑入屏幕，或2页面向左平移滑出屏幕。滑动手势结束后通过[显式动画 (animateTo)](../harmonyos-references/ts-explicit-animation.md)完成页面平移至窗口边缘，并重新渲染1、2、3页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/vR0209YYS-65bGg5tlNZSQ/zh-cn_image_0000002427853450.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002152Z&HW-CC-Expire=86400&HW-CC-Sign=A971B27567D368F9FB59D87AEA09981D6DE6B4DBC9D437C8D71AC671686EA58A "点击放大")

### 开发步骤

1. 使用Stack堆叠容器存放3个页面，并将上层页面向左平移至屏幕外。

   ```
   1. // entry/src/main/ets/view/CoverFlipPage.ets
   2. @Component
   3. export struct CoverFlipPage {
   4. // ...
   5. @State offsetX: number = 0;
   6. @State screenW: number = 0;
   7. // ...

   9. build() {
   10. Stack() {
   11. // Next page.
   12. ReaderPage({ content: this.rightPageContent })

   14. // Current page.
   15. ReaderPage({ content: this.midPageContent })
   16. .translate({ x: this.offsetX >= Constants.PAGE_FLIP_ZERO ? Constants.PAGE_FLIP_ZERO : this.offsetX })
   17. // ...

   19. // Previous page, shift the window width to the left.
   20. ReaderPage({ content: this.leftPageContent })
   21. .translate({ x: -this.screenW + this.offsetX })
   22. // ...
   23. }
   24. // ...
   25. }
   26. // ...
   27. }
   ```

   [CoverFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/CoverFlipPage.ets#L22-L348)
2. 根据滑动手势事件获取平移的距离，修改状态变量offsetX刷新页面，控制页面移动。手势结束后调用自定义方法pageAnimateTo()方法执行显示动画，完成页面剩余滑动。

   ```
   1. // entry/src/main/ets/view/CoverFlipPage.ets
   2. .gesture(
   3. PanGesture(this.panOption)
   4. .onActionUpdate((event?: GestureEvent) => {
   5. // ...
   6. this.offsetX = event.offsetX;
   7. // ...
   8. })
   9. .onActionEnd(() => {
   10. // ...
   11. this.pageAnimateTo(false);
   12. // ...
   13. })
   14. )
   ```

   [CoverFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/CoverFlipPage.ets#L197-L282)
3. pageAnimateTo()方法中设置offsetX的结束值，手势向右时offsetX的值为屏幕宽度screenW，手势向左时offsetX的值为负的屏幕宽度-screenW。设置完成后animateTo方法自动插入过渡动画。动画播放结束后，onFinish()完成回调方法中重置offsetX为0，执行自定义方法simulatePageContent()方法更新各内容页ReaderPage组件展示的数据。

   ```
   1. // entry/src/main/ets/view/CoverFlipPage.ets
   2. private pageAnimateTo(isClick: boolean, isLeft?: boolean) {
   3. this.getUIContext().animateTo({
   4. duration: Constants.PAGE_FLIP_TO_AST_DURATION,
   5. curve: Curve.EaseOut,
   6. onFinish: () => {
   7. // ...
   8. this.offsetX = Constants.PAGE_FLIP_ZERO;
   9. this.simulatePageContent();
   10. // ...
   11. }
   12. }, () => {
   13. // ...
   14. this.offsetX = this.screenW;
   15. // ...
   16. this.offsetX = -this.screenW;
   17. // ...
   18. });
   19. }
   ```

   [CoverFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/CoverFlipPage.ets#L92-L161)

## 仿真翻页

### 场景描述

仿真翻页效果模拟真实纸质书的翻页体验。用户拖动页面的角落（右上角或右下角），被拖动的页面会随着手指的移动而卷曲、折叠。在翻动过程中，可以看到当前页的背面（为当前页的翻转显示效果）以及被翻页覆盖的下一页内容逐渐显露出来。翻页轨迹遵循贝塞尔曲线，并伴有阴影效果增强立体感。翻页效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/kYW157C-TDKxwGC8gpW1BA/zh-cn_image_0000002363628777.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002152Z&HW-CC-Expire=86400&HW-CC-Sign=13E4D0256EB212A4DCC7780DE8102B122DCC5B5D383CE68983CD29BB29F628C3 "点击放大")

### 实现原理

仿真翻页基于覆盖翻页的页面布局，使用系统接口对当前页或上一页进行截图保存为pixelMap，传递至ArkGraphics 2D的[@ohos.graphics.drawing (绘制模块)](../harmonyos-references/js-apis-graphics-drawing.md)的相关绘制接口实现了当前页、背页、阴影等区域的绘制。页面绘制通过滑动手势事件[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)触发，获取手指在屏幕上的位置，通过该位置信息计算仿真翻页曲线所依赖的相关点位。手势结束时使用定时器模拟滑动触摸的点位并触发页面绘制，判断结束条件终止绘制。

**仿真翻页绘制实现关键点**

1. 仿真翻页控制点。仿真翻页可以看作下图三个区域组合而成。要绘制出其中曲线及直线，需要计算出一组特定的坐标点（参考下图），计算公式详见开发步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/TQSlo8C_SBKnkInexx0BFQ/zh-cn_image_0000002329710434.png?HW-CC-KV=V1&HW-CC-Date=20260428T002152Z&HW-CC-Expire=86400&HW-CC-Sign=3125D50084E40919AA0A9EF46AF79FDDA38E84F8C5147C1A2EBAA384A0180DFF "点击放大")
2. 曲线绘制。为使用上述坐标点绘制出曲线，需要使用[@ohos.graphics.drawing (绘制模块)](../harmonyos-references/js-apis-graphics-drawing.md)的相关接口实现，如[Path.lineTo()](../harmonyos-references/arkts-apis-graphics-drawing-path.md#lineto)连接线段；[Path.quadTo()](../harmonyos-references/arkts-apis-graphics-drawing-path.md#quadto)实现二阶贝塞尔曲线；[Canvas.clipPath()](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#clippath12)实现对画布裁剪等。
3. 内容绘制。仿真翻页绘制的内容来源于使用[@ohos.arkui.componentSnapshot (组件截图)](../harmonyos-references/js-apis-arkui-componentsnapshot.md#componentsnapshotgetsync12)的[componentSnapshot.getSync()](../harmonyos-references/js-apis-arkui-componentsnapshot.md#componentsnapshotgetsync12)接口获取的组件截图pixelMap，然后使用[@ohos.graphics.drawing (绘制模块)](../harmonyos-references/js-apis-graphics-drawing.md)的[Canvas.drawPixelMapMesh()](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawpixelmapmesh12)实现绘制。
4. 阴影效果渲染。主要使用了[@ohos.graphics.drawing (绘制模块)](../harmonyos-references/js-apis-graphics-drawing.md)的[ShaderEffect](../harmonyos-references/arkts-apis-graphics-drawing-shadereffect.md)着色器实现。通过为画刷设置着色器效果，并设置相关参数，完成了渐变阴影的绘制。

### 开发步骤

1. 仿真翻页页面布局

   仿真翻页页面布局同覆盖翻页大体相同，屏幕区域保留当前页和下一页层叠，上一页向左移出屏幕。不同的是增加NodeContainer组件，在滑动手势事件触发时显示，用于绘制仿真翻页效果，翻页效果结束时隐藏。

   ```
   1. // entry/src/main/ets/view/EmulationFlipPage.ets
   2. Stack() {
   3. // Page area is the same as overlay page cover.
   4. ReaderPage({ content: this.rightPageContent })

   6. ReaderPage({ content: this.midPageContent })
   7. .translate({ x: this.offsetX >= Constants.PAGE_FLIP_ZERO ? Constants.PAGE_FLIP_ZERO : this.offsetX })
   8. .id('middlePage')// Mark the component ID and use it as a screenshot.
   9. // ...

   11. ReaderPage({ content: this.leftPageContent })
   12. .translate({ x: -this.screenW + this.offsetX })
   13. .id('leftPage') // Mark the component ID and use it as a screenshot.

   15. // Display when flipping pages, drawing the current or previous page.
   16. NodeContainer(this.myNodeController)
   17. .width(this.getUIContext().px2vp(this.windowWidth))
   18. .height(this.getUIContext().px2vp(this.windowHeight))
   19. .visibility(this.isNodeShow ? Visibility.Visible : Visibility.None)
   20. }
   ```

   [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L103-L141)
2. 滑动手势事件
   1. 滑动手势事件触发时，记录首个点的横纵坐标，作为手势的起始位置，横坐标用于判断手势结束时页面的滑动方向，纵坐标用于判断手势的起始位置，上部、中部或下部，绘制仿真翻页时区分仿真翻页的类型。

      ```
      1. // entry/src/main/ets/view/EmulationFlipPage.ets
      2. build() {
      3. // ...
      4. Stack() {
      5. // ...
      6. }
      7. .gesture(
      8. PanGesture({ fingers: 1 })
      9. .onActionUpdate((event: GestureEvent) => {
      10. // ...
      11. if (this.panPositionX === 0) {
      12. this.initPanPositionX(tmpFingerInfo);
      13. return;
      14. }
      15. // ...
      16. })
      17. // ...
      18. )
      19. // ...
      20. }
      21. // ...
      22. private initPanPositionX(tmpFingerInfo: FingerInfo): void {
      23. this.panPositionX = tmpFingerInfo.localX;
      24. let panPositionY = this.getUIContext().vp2px(tmpFingerInfo.localY);

      26. // Obtain the position of the first touch point and determine the starting area for sliding.
      27. if (panPositionY < (this.windowHeight / 3)) {
      28. this.drawPosition = DrawPosition.DP_TOP;
      29. } else if (panPositionY >
      30. (this.windowHeight * 2 / 3)) {
      31. this.drawPosition = DrawPosition.DP_BOTTOM;
      32. } else {
      33. this.drawPosition = DrawPosition.DP_MIDDLE;
      34. }
      35. }
      ```

      [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L97-L301)
   2. 在onActionUpdate回调中，当检测到第二个触摸点坐标时，与首个点横坐标进行比较。横坐标大于首个点，手势向右，截图上一页，用于绘制上一页的仿真翻页显示在屏幕中覆盖当前页；横坐标小于首个点，手势向左，截图当前页，用于绘制当前页仿真翻页效果露出下一页， 并隐藏当前页。设置NodeContainer组件为显示状态。

      ```
      1. // entry/src/main/ets/view/EmulationFlipPage.ets
      2. build() {
      3. // ...
      4. Stack() {
      5. // ...
      6. }
      7. .gesture(
      8. PanGesture({ fingers: 1 })
      9. .onActionUpdate((event: GestureEvent) => {
      10. // ...
      11. // Perform a check before starting to draw.
      12. if (!this.isDrawing) {
      13. // ...
      14. this.firstDrawingInit(tmpFingerInfo);
      15. }
      16. // ...
      17. })
      18. // ...
      19. )
      20. // ...
      21. }
      22. // ...
      23. private firstDrawingInit(tmpFingerInfo: FingerInfo): void {
      24. // The initial sliding direction of the page is used to determine whether to continue or cancel flipping forward or backward.
      25. if (this.panPositionX < tmpFingerInfo.localX) {
      26. // When flipping forward, take a screenshot of the previous page, and the flipping type is middle flipping.
      27. this.pageMoveForward = MoveForward.MF_FORWARD;
      28. this.snapPageId = 'leftPage';
      29. this.drawPosition = DrawPosition.DP_MIDDLE
      30. } else {
      31. // When flipping back, take a screenshot of the current page and hide it.
      32. this.pageMoveForward = MoveForward.MF_BACKWARD;
      33. this.snapPageId = 'middlePage';
      34. this.isMiddlePageHide = true;
      35. }

      37. // Take a screenshot after confirming the sliding direction of the page.
      38. if (this.pagePixelMap) {
      39. this.pagePixelMap.release();
      40. }
      41. try {
      42. this.pagePixelMap = this.getUIContext().getComponentSnapshot().getSync(this.snapPageId);
      43. } catch (error) {
      44. hilog.error(0x0000, 'EmulationFlip',
      45. `getComponentSnapshot().getSync failed. Cause: ${JSON.stringify(error)}`)
      46. }
      47. this.isDrawing = true;
      48. this.isNodeShow = true;
      49. }
      ```

      [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L98-L336)
   3. 准备绘制需要的坐标数据，横纵坐标转换为px单位，用于仿真翻页绘制，使用AppStorage保存。比较当前横坐标与上一次的横坐标，判断当前手势的方向，用于手势释放判断页面自动翻页的方向。记录当前横坐标。调用newRectNode()方法更新NodeContainer组件。

      ```
      1. // entry/src/main/ets/view/EmulationFlipPage.ets
      2. build() {
      3. // ...
      4. Stack() {
      5. // ...
      6. }
      7. .gesture(
      8. PanGesture({ fingers: 1 })
      9. .onActionUpdate((event: GestureEvent) => {
      10. // ...
      11. // Execute drawing.
      12. this.drawing(tmpFingerInfo);
      13. })
      14. // ...
      15. )
      16. // ...
      17. }
      18. // ...
      19. private drawing(tmpFingerInfo: FingerInfo): void {
      20. // Determine the latest sliding direction of the gesture, and after releasing the gesture,
      21. // combine it with the sliding direction of the page to determine whether to flip or cancel.
      22. if (this.panPositionX < tmpFingerInfo.localX) {
      23. this.gestureMoveForward = MoveForward.MF_FORWARD;
      24. this.panPositionX = tmpFingerInfo.localX;
      25. } else {
      26. this.gestureMoveForward = MoveForward.MF_BACKWARD;
      27. this.panPositionX = tmpFingerInfo.localX;
      28. }
      29. AppStorage.setOrCreate('drawState', DrawState.DS_MOVING);

      31. // Convert to px units.
      32. this.positionX = this.getUIContext().vp2px(tmpFingerInfo.localX);
      33. this.positionY = this.getUIContext().vp2px(tmpFingerInfo.localY);
      34. AppStorage.setOrCreate('positionX', this.positionX);
      35. AppStorage.setOrCreate('positionY', this.positionY);

      37. // Execute drawing.
      38. this.newRectNode();
      39. }
      ```

      [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L99-L365)
3. 仿真页面绘制
   1. NodeContainer组件控制器清空所有节点，新增渲染节点，渲染节点用于仿真翻页的绘制。

      ```
      1. // entry/src/main/ets/view/EmulationFlipPage.ets
      2. newRectNode() {
      3. // Creates a RectRenderNode object.
      4. const rectNode = new RectRenderNode();
      5. // ...
      6. this.myNodeController.clearNodes();
      7. this.myNodeController.addNode(rectNode);
      8. }
      ```

      [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L68-L85)
   2. 在RenderNode进行绘制时，draw()方法会被调用。首先执行初始化init()方法。通过AppStorage获取触摸点的横纵坐标，并判断手势起始位置，计算仿真翻页需要的坐标点以及绘制阴影时需要的相关数值。通过手势触摸点计算页角点A，限制A点纵坐标的范围，从而限制书页的翻起程度。保存点A的纵坐标。各点的计算方法见代码。计算结束后判断当前区域是否还在屏幕区域内，保存判断结果。

      ```
      1. // entry/src/main/ets/viewmodel/PageNodeController.ets
      2. export class RectRenderNode extends RenderNode {
      3. // ...
      4. draw(context: DrawContext): void {
      5. const canvas = context.canvas;

      7. // Initialize data.
      8. init();
      9. // ...
      10. }
      11. }
      12. // ...
      13. /**
      14. * Initialize data.
      15. */
      16. function init(): void {
      17. // ...
      18. // Obtain touch points.
      19. let x: number = AppStorage.get('positionX') as number;
      20. let y: number = AppStorage.get('positionY') as number;
      21. let viewWidth: number = AppStorage.get('windowWidth') as number;
      22. let viewHeight: number = AppStorage.get('windowHeight') as number;
      23. pointA = new MyPoint(x, y);
      24. // ...
      25. let touchPoint = new MyPoint(x, y);
      26. let drawState: number = AppStorage.get('drawState') as number;
      27. let drawStartPosition: number = AppStorage.get('drawPosition') as number;

      29. // Determine the area where sliding begins.
      30. if (DrawPosition.DP_TOP === drawStartPosition) {
      31. // The touch point is at the top.
      32. pointF = new MyPoint(viewWidth, 0);
      33. if (drawState !== DrawState.DS_RELEASE) {
      34. calcPointAByTouchPoint(touchPoint);
      35. }
      36. } else if (DrawPosition.DP_BOTTOM === drawStartPosition) {
      37. // The touch point is below.
      38. pointF = new MyPoint(viewWidth, viewHeight);
      39. if (drawState !== DrawState.DS_RELEASE) {
      40. calcPointAByTouchPoint(touchPoint);
      41. }
      42. } else {
      43. // The touch point is in the middle.
      44. pointA.y = viewHeight - 1;
      45. pointF.x = viewWidth;
      46. pointF.y = viewHeight;
      47. }
      48. // Saves the y-coordinate of point A.
      49. AppStorage.setOrCreate<number>('flipPositionY', pointA.y);

      51. // Calculate all path points.
      52. calcPointsXY();
      53. }

      55. /**
      56. * Calculate the y-coordinate of point A based on the touch point.
      57. * @param touchPoint Touch point.
      58. */
      59. function calcPointAByTouchPoint(touchPoint: MyPoint): void {
      60. let viewWidth: number = AppStorage.get('windowWidth') as number;
      61. let viewHeight: number = AppStorage.get('windowHeight') as number;
      62. let r = Constants.SIXTY_PERCENT * viewWidth;
      63. pointA.x = touchPoint.x;

      65. // Reset the y value and restrict the region where the y value is located.
      66. if (pointF.y === viewHeight) {
      67. let tmpY = viewHeight - Math.abs(Math.sqrt(Math.pow(r, 2) - Math.pow(touchPoint.x - (viewWidth - r), 2)))
      68. pointA.y = touchPoint.y >= tmpY ? touchPoint.y : tmpY;
      69. } else {
      70. let tmpY = Math.abs(Math.sqrt(Math.pow(r, 2) - Math.pow(touchPoint.x - (viewWidth - r), 2)))
      71. pointA.y = touchPoint.y >= tmpY ? tmpY : touchPoint.y;
      72. }
      73. }

      75. /**
      76. * Calculate the coordinates of each path point.
      77. */
      78. function calcPointsXY(): void {
      79. pointG.x = (pointA.x + pointF.x) / 2;
      80. pointG.y = (pointA.y + pointF.y) / 2;

      82. pointE.x = pointG.x - (pointF.y - pointG.y) * (pointF.y - pointG.y) / (pointF.x - pointG.x);
      83. pointE.y = pointF.y;

      85. pointH.x = pointF.x;
      86. pointH.y = pointG.y - (pointF.x - pointG.x) * (pointF.x - pointG.x) / (pointF.y - pointG.y);

      88. pointC.x = pointE.x - (pointF.x - pointE.x) / 2;
      89. pointC.y = pointF.y;

      91. pointJ.x = pointF.x;
      92. pointJ.y = pointH.y - (pointF.y - pointH.y) / 2;

      94. pointB = getIntersectionPoint(pointA, pointE, pointC, pointJ);
      95. pointK = getIntersectionPoint(pointA, pointH, pointC, pointJ);

      97. pointD.x = (pointC.x + 2 * pointE.x + pointB.x) / 4;
      98. pointD.y = (2 * pointE.y + pointC.y + pointB.y) / 4;

      100. pointI.x = (pointJ.x + 2 * pointH.x + pointK.x) / 4;
      101. pointI.y = (2 * pointH.y + pointJ.y + pointK.y) / 4;

      103. //Calculate the distance from point d to line ae and use it to draw shadows.
      104. let lA: number = pointA.y - pointE.y;
      105. let lB: number = pointE.x - pointA.x;
      106. let lC: number = pointA.x * pointE.y - pointE.x * pointA.y;
      107. lPathAShadowDis = Math.abs((lA * pointD.x + lB * pointD.y + lC) / Math.hypot(lA, lB));

      109. // Calculate the distance from point i to ah and use it to draw shadows.
      110. let rA: number = pointA.y - pointH.y;
      111. let rB: number = pointH.x - pointA.x;
      112. let rC: number = pointA.x * pointH.y - pointH.x * pointA.y;
      113. rPathAShadowDis = Math.abs((rA * pointI.x + rB * pointI.y + rC) / Math.hypot(rA, rB));

      115. // Check if the drawing area is still in the window. If it is not in the window, the drawing ends.
      116. if (!checkDrawingAreaInWindow()) {
      117. AppStorage.setOrCreate('isFinished', true);
      118. }
      119. }
      ```

      [PageNodeController.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/viewmodel/PageNodeController.ets#L123-L346)
   3. 绘制下一页上的阴影。使用上一步计算的相关数值，配置绘制阴影所需的着色器shaderEffect，使用canvas及画刷绘制阴影。

      ```
      1. // entry/src/main/ets/viewmodel/PageNodeController.ets
      2. export class RectRenderNode extends RenderNode {
      3. // ...
      4. draw(context: DrawContext): void {
      5. const canvas = context.canvas;

      7. // ...
      8. // Draw the shadow shown on the next page.
      9. drawPathBShadow(canvas);
      10. // ...
      11. }
      12. }
      13. // ...
      14. /**
      15. * Draw the shadow shown on the next page.
      16. *
      17. * @param canvas canvas
      18. */
      19. function drawPathBShadow(canvas: drawing.Canvas) {
      20. canvas.save()
      21. // Gradient color array.
      22. let deepColor: number = 0xff111111;
      23. let lightColor: number = 0x00111111;
      24. let gradientColors: number[] = [deepColor, lightColor];
      25. let viewWidth: number = AppStorage.get('windowWidth') as number;
      26. let viewHeight: number = AppStorage.get('windowHeight') as number;

      28. // The distance from A to F.
      29. let aToF = Math.hypot((pointA.x - pointF.x), (pointA.y - pointF.y));
      30. // The distance from A to F.
      31. let viewDiagonalLength = Math.hypot(viewWidth, viewHeight);

      33. let left: number = 0;
      34. let right: number = 0;
      35. let top: number = pointC.y;
      36. let bottom: number = viewDiagonalLength + pointC.y;

      38. if (pointF.x === viewWidth && pointF.y === 0) {
      39. // The F point is located in the upper right corner.
      40. left = pointC.x;
      41. right = pointC.x + aToF / 4;
      42. } else {
      43. left = pointC.x - aToF / 4;
      44. right = pointC.x;
      45. }

      47. // Calculate the rotation angle between two points (calculated in radians and converted into angles).
      48. let deltaX: number = pointH.y - pointF.y;
      49. let deltaY: number = pointE.x - pointF.x;
      50. let radians: number = Math.atan2(deltaY, deltaX);
      51. // Convert radians to angles.
      52. let rotateDegrees: number = radians * 180 / Math.PI;

      54. let startPt: common2D.Point = { x: pointF.y === 0 ? right : left, y: top };
      55. let endPt: common2D.Point = { x: pointF.y === 0 ? left : right, y: top };
      56. let shaderEffect = drawing.ShaderEffect.createLinearGradient(endPt, startPt, gradientColors, drawing.TileMode.MIRROR);

      58. // Perform rotation.
      59. canvas.rotate(rotateDegrees, pointC.x, pointC.y);

      61. // Draw shadows.
      62. let rect: common2D.Rect = {
      63. left: left,
      64. top: top,
      65. right: right,
      66. bottom: bottom
      67. };
      68. drawShadow(canvas, shaderEffect, rect);
      69. }
      70. // ...
      71. /**
      72. * Draw shaded areas.
      73. *
      74. * @param canvas canvas
      75. * @param shaderEffect shader effect
      76. * @param rect rect
      77. */
      78. function drawShadow(canvas: drawing.Canvas, shaderEffect: drawing.ShaderEffect, rect: common2D.Rect) {
      79. let tmpBrush = new drawing.Brush();
      80. tmpBrush.setShaderEffect(shaderEffect);
      81. canvas.attachBrush(tmpBrush);
      82. canvas.drawRect(rect.left, rect.top, rect.right, rect.bottom);
      83. canvas.detachBrush();
      84. canvas.restore();
      85. }
      ```

      [PageNodeController.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/viewmodel/PageNodeController.ets#L124-L783)
   4. 绘制仿真翻页背面内容及阴影。首先根据计算出的绘制曲线依赖的点，规划出背面区域pathC ，使用clipPath()方法裁剪出该区域。为绘制区域设置旋转矩阵，实现将截图获取的页面pixelMap，旋转并翻转成需要的背页效果。最后绘制背页区域的阴影，此处阴影计算的算法同上一步。

      ```
      1. // entry/src/main/ets/viewmodel/PageNodeController.ets
      2. export class RectRenderNode extends RenderNode {
      3. // ...
      4. draw(context: DrawContext): void {
      5. const canvas = context.canvas;

      7. // ...
      8. // Draw the back area for flipping pages.
      9. drawPathC(canvas);
      10. // ...
      11. }
      12. }
      13. // ...
      14. /**
      15. * Draw the back area for flipping pages.
      16. *
      17. * @param canvas canvas
      18. */
      19. function drawPathC(canvas: drawing.Canvas): void {
      20. if (canIUse('SystemCapability.Graphics.Drawing')) {
      21. canvas.attachBrush(pathABrush);
      22. pathC.reset();
      23. pathC.moveTo(pointI.x, pointI.y);
      24. pathC.lineTo(pointD.x, pointD.y);
      25. pathC.lineTo(pointB.x, pointB.y);
      26. pathC.lineTo(pointA.x, pointA.y);
      27. pathC.lineTo(pointK.x, pointK.y);
      28. pathC.close();
      29. canvas.drawPath(pathC);

      31. // Draw the content on the back.
      32. canvas.save();
      33. canvas.clipPath(pathC);

      35. // Set the inversion and rotation matrices.
      36. let eh = Math.hypot(pointF.x - pointE.x, pointH.y - pointF.y);
      37. let sin0 = (pointF.x - pointE.x) / eh;
      38. let cos0 = (pointH.y - pointF.y) / eh;
      39. let value: Array<number> = [0, 0, 0, 0, 0, 0, 0, 0, 1.0];
      40. value[0] = -(1 - 2 * sin0 * sin0);
      41. value[1] = 2 * sin0 * cos0;
      42. value[3] = 2 * sin0 * cos0;
      43. value[4] = 1 - 2 * sin0 * sin0;

      45. let matrix = new drawing.Matrix();
      46. matrix.reset();
      47. matrix.setMatrix(value);
      48. matrix.preTranslate(-pointE.x, -pointE.y);
      49. matrix.postTranslate(pointE.x, pointE.y);
      50. canvas.concatMatrix(matrix);

      52. // Draw the current page on the back.
      53. let pagePixelMap: image.PixelMap = AppStorage.get('pagePixelMap') as image.PixelMap;
      54. let viewWidth: number = AppStorage.get('windowWidth') as number;
      55. let viewHeight: number = AppStorage.get('windowHeight') as number;
      56. let verts: Array<number> = [0, 0, viewWidth, 0, 0, viewHeight, viewWidth, viewHeight];
      57. canvas.drawPixelMapMesh(pagePixelMap, 1, 1, verts, 0, null, 0);
      58. canvas.restore();

      60. // Change the color on the back.
      61. canvas.detachBrush();
      62. canvas.attachBrush(pathCBrush);
      63. canvas.drawPath(pathC);
      64. canvas.detachBrush();

      66. // Draw shadows in the back area.
      67. canvas.save();
      68. canvas.clipPath(pathC);
      69. drawPathCShadow(canvas);
      70. canvas.restore();
      71. }
      72. }
      ```

      [PageNodeController.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/viewmodel/PageNodeController.ets#L125-L453)
   5. 绘制页面左侧文字区域及阴影。根据计算出的绘制曲线依赖的点，规划出背面区域pathA，裁剪出该区域。将截图保存的页面pixelMap绘制在该区域，并绘制该区域的阴影。完成仿真翻页的绘制。

      ```
      1. // entry/src/main/ets/viewmodel/PageNodeController.ets
      2. export class RectRenderNode extends RenderNode {
      3. // ...
      4. draw(context: DrawContext): void {
      5. const canvas = context.canvas;

      7. // ...
      8. // Retrieve the cropped area of the current page.
      9. getPathA();

      11. // Draw the current page area.
      12. drawPathAContent(canvas);
      13. }
      14. }

      16. /**
      17. * Retrieve the cropped area of the current page.
      18. */
      19. function getPathA(): void {
      20. if (canIUse('SystemCapability.Graphics.Drawing')) {
      21. let viewWidth: number = AppStorage.get('windowWidth') as number;
      22. let viewHeight: number = AppStorage.get('windowHeight') as number;
      23. // Point F is located in the upper right corner, calculate pathA.
      24. if (pointF.x === viewWidth && pointF.y === 0) {
      25. pathA.reset();
      26. pathA.lineTo(pointC.x, pointC.y);
      27. pathA.quadTo(pointE.x, pointE.y, pointB.x, pointB.y);
      28. pathA.lineTo(pointA.x, pointA.y);
      29. pathA.lineTo(pointK.x, pointK.y);
      30. pathA.quadTo(pointH.x, pointH.y, pointJ.x, pointJ.y);
      31. pathA.lineTo(viewWidth, viewHeight);
      32. pathA.lineTo(0, viewHeight);
      33. pathA.close();
      34. }
      35. // Point F is located in the bottom right corner, calculate pathA.
      36. if (pointF.x === viewWidth && pointF.y === viewHeight) {
      37. pathA.reset();
      38. pathA.lineTo(0, viewHeight);
      39. pathA.lineTo(pointC.x, pointC.y);
      40. pathA.quadTo(pointE.x, pointE.y, pointB.x, pointB.y);
      41. pathA.lineTo(pointA.x, pointA.y);
      42. pathA.lineTo(pointK.x, pointK.y);
      43. pathA.quadTo(pointH.x, pointH.y, pointJ.x, pointJ.y);
      44. pathA.lineTo(viewWidth, 0);
      45. pathA.close();
      46. }
      47. }
      48. }
      49. // ...

      51. /**
      52. * Draw the current page area.
      53. *
      54. * @param canvas canvas
      55. */
      56. function drawPathAContent(canvas: drawing.Canvas): void {
      57. if (canIUse('SystemCapability.Graphics.Drawing')) {
      58. canvas.attachBrush(pathABrush);

      60. canvas.save();
      61. canvas.clipPath(pathA);

      63. // Obtain a screenshot pixelMap for displaying the current page.
      64. let pagePixelMap: image.PixelMap = AppStorage.get('pagePixelMap') as image.PixelMap;
      65. let viewWidth: number = AppStorage.get('windowWidth') as number;
      66. let viewHeight: number = AppStorage.get('windowHeight') as number;
      67. let verts: Array<number> = [0, 0, viewWidth, 0, 0, viewHeight, viewWidth, viewHeight];
      68. // Execute drawing.
      69. canvas.drawPixelMapMesh(pagePixelMap, 1, 1, verts, 0, null, 0);
      70. canvas.restore();

      72. // Draw the shadow of the current page.
      73. if (AppStorage.get('drawPosition') === DrawPosition.DP_MIDDLE) {
      74. drawPathAHorizontalShadow(canvas);
      75. } else {
      76. drawPathALeftShadow(canvas);
      77. drawPathARightShadow(canvas);
      78. }
      79. }
      80. }
      ```

      [PageNodeController.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/viewmodel/PageNodeController.ets#L126-L487)
4. 滑动手势结束。滑动手势结束后获取最后一次绘制的页角A点的纵坐标。判断当前手势的移动方向，设置自动绘制的步进值。使用定时器执行自动绘制。

   ```
   1. // entry/src/main/ets/view/EmulationFlipPage.ets
   2. build() {
   3. // ...
   4. Stack() {
   5. // ...
   6. }
   7. .gesture(
   8. PanGesture({ fingers: 1 })
   9. // ...
   10. .onActionEnd(() => {
   11. // ...

   13. // Perform automatic sliding.
   14. this.autoFlipPage();
   15. this.isDrawing = false;
   16. })
   17. )
   18. // ...
   19. }
   20. // ...

   22. /**
   23. * Perform automatic drawing.
   24. */
   25. private autoFlipPage(): void {
   26. AppStorage.set('drawState', DrawState.DS_RELEASE);
   27. // Get the vertical axis of the drawn footer.
   28. AppStorage.setOrCreate('positionY', (AppStorage.get('flipPositionY') as number));
   29. let num: number = Constants.DISTANCE_FRACTION;
   30. if (this.gestureMoveForward === MoveForward.MF_FORWARD) {
   31. // Page forward to calculate diff.
   32. let xDiff = (this.windowWidth - this.positionX) / num;
   33. let yDiff = 0;
   34. if (this.drawPosition === DrawPosition.DP_BOTTOM) {
   35. yDiff = (this.windowHeight - this.positionY) / num;
   36. } else {
   37. yDiff = (0 - this.positionY) / num;
   38. }

   40. this.setTimer(xDiff, yDiff, () => {
   41. this.newRectNode();
   42. });
   43. } else {
   44. // Next Page.
   45. this.setTimer(Constants.FLIP_X_DIFF, 0, () => {
   46. this.newRectNode();
   47. });
   48. }
   49. }
   ```

   [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L100-L425)
5. 自动绘制翻页动效
   1. 根据最后手势的移动方向，页面需要自动向右侧还原，或向左侧翻页。根据上一步获取的步进值，计算新的触摸点，执行新的绘制。并使用定时器更新触摸点。

      ```
      1. // entry/src/main/ets/view/EmulationFlipPage.ets
      2. private setTimer(xDiff: number, yDiff: number, drawNode: () => void) {
      3. // Automatically flip forward.
      4. if (this.gestureMoveForward === MoveForward.MF_FORWARD) {
      5. this.timeID = setInterval((xDiff: number, yDiff: number, drawNode: () => void) => {
      6. let x = AppStorage.get('positionX') as number + xDiff;
      7. let y = AppStorage.get('positionY') as number + yDiff;
      8. // Page forward termination condition.
      9. if (x >= (AppStorage.get('windowWidth') as number) - 1 || y >= (AppStorage.get('windowHeight') as number) ||
      10. y <= 0) {
      11. this.finishLastGesture();
      12. } else {
      13. AppStorage.setOrCreate('positionX', x);
      14. AppStorage.setOrCreate('positionY', y);
      15. drawNode();
      16. }
      17. }, Constants.TIMER_DURATION, xDiff, yDiff, drawNode);
      18. } else {
      19. // Automatically flip backwards.
      20. AppStorage.setOrCreate('isFinished', false);
      21. this.timeID = setInterval((xDiff: number, _: number, drawNode: () => void) => {
      22. let x = AppStorage.get('positionX') as number + xDiff;
      23. let y = AppStorage.get('positionY') as number;
      24. // Obtain the termination condition for determining when flipping back to draw.
      25. let isFinished: boolean = AppStorage.get('isFinished') as boolean;
      26. if (isFinished) {
      27. // End automatic drawing.
      28. this.finishLastGesture();
      29. } else {
      30. AppStorage.setOrCreate('positionX', x);
      31. AppStorage.setOrCreate('positionY', y);
      32. drawNode();
      33. }
      34. }, Constants.TIMER_DURATION, xDiff, yDiff, drawNode);
      35. }
      36. }
      ```

      [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L505-L549)
   2. 定时器中增加绘制结束条件判断，页面向右侧还原时使用触摸的横纵坐标判断，页面向左翻页使用计算曲线关键点时判断绘制区域是否还在屏幕内存储的结果。执行finishLastGesture()结束绘制。

      ```
      1. // entry/src/main/ets/view/EmulationFlipPage.ets
      2. private setTimer(xDiff: number, yDiff: number, drawNode: () => void) {
      3. // Automatically flip forward.
      4. if (this.gestureMoveForward === MoveForward.MF_FORWARD) {
      5. this.timeID = setInterval((xDiff: number, yDiff: number, drawNode: () => void) => {
      6. // ...
      7. // Page forward termination condition.
      8. if (x >= (AppStorage.get('windowWidth') as number) - 1 || y >= (AppStorage.get('windowHeight') as number) ||
      9. y <= 0) {
      10. this.finishLastGesture();
      11. } else {
      12. // ...
      13. }
      14. }, Constants.TIMER_DURATION, xDiff, yDiff, drawNode);
      15. } else {
      16. // Automatically flip backwards.
      17. AppStorage.setOrCreate('isFinished', false);
      18. this.timeID = setInterval((xDiff: number, _: number, drawNode: () => void) => {
      19. // ...
      20. // Obtain the termination condition for determining when flipping back to draw.
      21. let isFinished: boolean = AppStorage.get('isFinished') as boolean;
      22. if (isFinished) {
      23. // End automatic drawing.
      24. this.finishLastGesture();
      25. } else {
      26. // ...
      27. }
      28. }, Constants.TIMER_DURATION, xDiff, yDiff, drawNode);
      29. }
      30. }
      ```

      [EmulationFlipPage.ets](https://gitcode.com/HarmonyOS_Samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L506-L550)
6. 动效结束更新内容页。判断动效结束后，清空定时器，根据页面初始移动方向及最后的手势移动方向更新页面内容，重新绘制页面。重置相关手势、绘制过程的状态变量。此时结束一次仿真翻页的绘制。

   ```
   1. // entry/src/main/ets/view/EmulationFlipPage.ets
   2. private finishLastGesture() {
   3. clearInterval(this.timeID);
   4. this.timeID = -1;

   6. // Previous page.
   7. if (this.pageMoveForward === MoveForward.MF_FORWARD && this.gestureMoveForward === MoveForward.MF_FORWARD) {
   8. this.currentPageNum--;
   9. this.simulatePageContent();
   10. }

   12. // Next page.
   13. if (this.pageMoveForward === MoveForward.MF_BACKWARD && this.gestureMoveForward === MoveForward.MF_BACKWARD) {
   14. this.currentPageNum++;
   15. this.simulatePageContent();
   16. }

   18. AppStorage.setOrCreate('positionX', -1);
   19. AppStorage.setOrCreate('positionY', -1);
   20. AppStorage.setOrCreate('drawPosition', DrawPosition.DP_NONE);
   21. AppStorage.setOrCreate('drawState', DrawState.DS_NONE);
   22. this.isMiddlePageHide = false;
   23. this.isNodeShow = false;
   24. this.gestureMoveForward = MoveForward.MF_NONE;
   25. this.panPositionX = 0;
   26. this.drawPosition = DrawPosition.DP_NONE;
   27. this.isDrawing = false;
   28. this.pagePixelMap?.release();
   29. }
   ```

   [EmulationFlipPage.ets](https://gitcode.com/harmonyos_samples/PageFlip/blob/master/entry/src/main/ets/view/EmulationFlipPage.ets#L466-L494)

### 示例代码

[实现阅读器翻页效果](https://gitcode.com/harmonyos_samples/PageFlip)
