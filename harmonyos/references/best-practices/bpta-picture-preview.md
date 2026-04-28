---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-picture-preview
title: 图片预览器
breadcrumb: 最佳实践 > 布局与弹窗 > 图片预览器
category: best-practices
scraped_at: 2026-04-28T08:19:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:732883e69e6b1c38421cb16d73e51724ba64001570b5b9f13cbded3cf9bf90d8
---

## 概述

图片预览器是常见的开发应用场景。在诸多日常使用的软件中，图片预览器都是提升用户体验的关键组件。它允许用户在上传、分享或编辑图片之前，先对图片进行预览，从而确保图片的质量和效果符合预期。本文章将深入探讨实现图片预览器过程中的几个复杂场景，具体包括：图片如何“跟手”，如何计算并合理限制图片的边界，以及如何解决Swiper组件与滑动手势之间产生的冲突问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/DL-yESTwT2iYoaxZpFG8gg/zh-cn_image_0000002194011008.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=BE5E5F94406FCF1987473FFE9CC1B90915F4F609149B8836A715C4A1E395DD61 "点击放大")

## 实现原理

### 场景描述

基础的图片预览器功能包括如下操作：

1. 双指捏合图片，即实现对图片以双指中心点为基准点的缩放操作。
2. 双击图片即可切换其大小，当图片处于放大状态时，再次双击即恢复至默认尺寸。
3. 大图片支持左右滑动查看。
4. 点击或滑动图片指示器，主图会随之更新。

其中，缩放图片是通过矩阵变换功能matrix4来实现的，图片的平移是通过属性translate来实现的。

### 关键技术

图片预览器中的图片查看功能，主要由大图界面来承担，交互操作相对复杂。下面，简要梳理一下大图界面中基本手势的处理与计算方式。

**“跟手”的原理**

“跟手”操作细分为两大类别：平移“跟手”与缩放“跟手”。

在平移“跟手”中，无论用户的手指如何在屏幕上滑动，其触摸点相对于图片所保持的百分比位置始终保持不变。缩放“跟手”，则是在图片依据用户手势进行缩放调整时，用户手势的中心点不仅相对于屏幕上的坐标保持不变，而且相对于图片内容的百分比位置也保持不变。如下图所示，屏幕是蓝色区域，初始图片是橙色区域，放大后的图片是灰色区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/98eGjlJFTNabKMoiMnjLuw/zh-cn_image_0000002229451285.png?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=4F7B6625323BB99B30BDD127AB9913D6F4E5EFA94F606DA2AC885157045AD553)

假定当前图片位置是<lastScale, offsetX, offsetY>，控件原始宽高为<w, h>，本次缩放图片的缩放值为scale，缩放的中心点百分比位置为<centerX, centerY>，偏移为<offX, offY>，计算终点位置设为<scale', offsetX', offsetY'>。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/q-t9OtJrRSi1vPQnmmsiJQ/zh-cn_image_0000002194011004.png?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=A76CE3AAE48CA4B7CB5F3E8BA4094857D19D2ED5F6C0E101B544FC9B0D908013 "点击放大")

如上图所示，假定缩放时，未发生偏移，蓝色看作交互开始时的控件，橙色是交互后的控件，如果缩放中心点在图片中心（图1），那么控件最终的offset没有任何变化；如果缩放中心在最左边缘（图3），在放大的过程中，整个控件的中心向右发生了偏移。由此，可以计算出图片的最终位置。其中，图2、图3中的问号代表图片的偏移量，而图中的橙色圆点是图片缩放操作的中心点。在以下计算公式中，0.5 表示图片中心点的百分比位置，即 50% = 0.5。

* scale' = 上次手势结束时的缩放值 \* 本次缩放图片的缩放值。

  = lastScale \* scale
* offsetX' = 平移带来的偏移 + 缩放中心不在中心而带来的偏移。

  = (offsetX + offX) + (0.5 - centerX) \* 控件大小变化之差

  = (offsetX + offX) + (0.5 - centerX) \* (w \* lastScale - w \* lastScale \* scale)

  = (offsetX + offX) + (0.5 - centerX) \* w \* (scale - 1) \* lastScale

  = (offsetX + offX) + (0.5 - centerX) \* w \* (1 - scale) \* lastScale
* 同理 offsetY' = 平移带来的偏移 + 缩放中心不在中心而带来的偏移。

  = (offsetY + offY) + (0.5 - centerY) \* h \* (1 - scale) \* lastScale

  缩放中心百分比位置<centerX , centerY>计算。如下图，橙色为手机屏幕，触摸点反馈的坐标(x,y)是相较屏幕左上角的（假设控件布满全屏）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/x__APc6vRCOh5mVq0Maj1g/zh-cn_image_0000002229451301.png?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=19FAFBA8657D4DE2BE81A4A1699B5F7663F4B286C298F99EE7F67964E279743D)
* centerX = ( x - imgX ) / imgWidth

  = ( 触摸点坐标x- X方向图片左上角的坐标）/ 图片的宽度

  = ( 触摸点坐标x- ( ( 组件屏幕的宽度 - 当前图片的宽度) / 2 +上次图片X方向的偏移量)) / 图片的宽度
* 同理 centerY = ( y - imgY ) / imgHeight

  = ( 触摸点坐标y- Y方向图片左上角的坐标 ) / 图片的高度

  = ( 触摸点坐标y- ( ( 组件屏幕的高度 - 当前图片的高度) / 2 +上次图片Y方向的偏移量)) / 图片的高度

**边界限制的原理**

边界计算涉及两个方面：当前图片显示边界计算、offset范围计算。

* 当前图片显示边界计算可得出当前图片显示的位置，左右上下是否与显示区域边界对齐，如果已经对齐，则不能继续往某个方向继续拖动。
* 平移/缩放时必须对offset作限制，否则图片将被移出显示区域或是手势结束后周围有黑边。从原理上看，某个scale下offset（x&y方向上）的范围是固定的，所以只需在手势交互时根据当前的scale计算得出offsetRange即可（超出边界时取边界作为结果）。

假定下面两个图中显示区域为黑框区域，当前放大倍率是curScale。

如下图，当X方向offset到达上界时图片上边缘x坐标等于0：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/JOneC8MST9uBijJUZzX2cQ/zh-cn_image_0000002194011016.png?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=8DEFF9919AC4210445376751BB546502616CE9458FA8864110D921CF3006B265)

到达下界时，图片右边缘与显示区域右边缘重合：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/_yvy5ImzQMa6QlNhLi_4Ng/zh-cn_image_0000002193851408.png?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=1EB06A832E4B2C7AACA204221A2E3D56757122ED752C5973BB96B977629DCAD8)

```
1. // Calculate the actual display size of the scaled image.
2. let scaledImageWidth = this.imageWidth * this.curScale;
3. let scaledImageHeight = this.imageHeight * this.curScale;

5. // Calculation of X-axis boundaries
6. if (scaledImageWidth > this.componentWidth) {
7. // If the width of the picture exceeds the width of the screen, you can move it left and right.
8. let maxXOffset = (scaledImageWidth - this.componentWidth) / 2;
9. this.maxOffsetX = maxXOffset;
10. this.minOffsetX = -maxXOffset;
11. } else {
12. // The width of the image does not exceed the width of the screen. It should be centered and no X-axis offset is allowed.
13. this.maxOffsetX = 0;
14. this.minOffsetX = 0;
15. }
```

[CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L181-L196)

Y方向同理，上下界为：

```
1. // Calculate the actual display size of the scaled image.
2. let scaledImageWidth = this.imageWidth * this.curScale;
3. let scaledImageHeight = this.imageHeight * this.curScale;

5. // ...

7. // Y-axis boundary calculation
8. if (scaledImageHeight > this.componentHeight) {
9. // If the image height exceeds the screen height, it can be scrolled up and down.
10. let maxYOffset = (scaledImageHeight - this.componentHeight) / 2;
11. this.maxOffsetY = maxYOffset;
12. this.minOffsetY = -maxYOffset;
13. } else {
14. // The height of the image does not exceed the height of the screen. It should be centered and no Y-axis offset is allowed.
15. this.maxOffsetY = 0;
16. this.minOffsetY = 0;
17. }
```

[CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L180-L210)

## 场景实现

### 跟手的实现

跟手技术细分为两大类别：平移“跟手”与缩放“跟手”，接下来，将对这两者进行讲解。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/8o73XaSFRNWiBOiTFMBqYg/zh-cn_image_0000002229336801.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=18DE6222AFEF52FEB0E0D7A27E186E0AF977D0ABFEBF26882D1748A637ED2DB7 "点击放大")

1. 响应平移手势：使用PanGesture接口实现滑动手势控制，为了实现单指滑动效果，需将参数fingers设置为1，当图片拖动后，即可获取当前图片的偏移量，具体为event.offsetX与event.offsetY。

   ```
   1. // Slide picture
   2. // Swiping left and right under the default size should switch images
   3. PanGesture({ fingers: 1, distance: this.isDisableSwipe ? 3 : 50 })
   4. .onActionUpdate((event: GestureEvent) => {
   5. this.isDisableSwipe = this.imageModel.panGestureUpdate(event);
   6. })
   7. .onActionEnd(() => {
   8. this.imageModel.gestureEnd();
   9. }),
   ```

   [ImageItemView.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/view/ImageItemView.ets#L115-L125)
2. 图片平移：在onScale()方法中，算出图片经过拖动后，在X轴方向和Y轴方向上的新位置，分别为curOffsetX和curOffsetY，即为平移“跟手”后图片的位置。

   ```
   1. // Pan gestures callback during movement.
   2. panGestureUpdate(event: GestureEvent): boolean {
   3. this.onScale(event.scale, event.offsetX, event.offsetY);
   4. this.pictureBoundaryRestriction();
   5. return this.isDisableSwipe;
   6. }

   8. // ...

   10. // Calculates the offset X and offset Y of the current picture and the scaling value of the current picture.
   11. onScale(scale: number, offX: number, offY: number): void {
   12. // ...
   13. if (this.curScale < this.maxScale) {
   14. this.curOffsetY =
   15. (this.lastOffsetY + offY) + (0.5 - this.centerY) * this.imageHeight * (1 - scale) * this.lastScale;
   16. this.curOffsetX =
   17. (this.lastOffsetX + offX) + (0.5 - this.centerX) * this.imageWidth * (1 - scale) * this.lastScale;
   18. }
   19. // When the image is in the process of moving, it has not reached the boundary point.
   20. this.isArriveBoundary = false;
   21. // If the image has not reached the boundary, do not allow the image to be switched.
   22. if (!this.isArriveBoundary) {
   23. this.isDisableSwipe = true;
   24. }
   25. }
   ```

   [CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L240-L379)
3. 响应缩放手势：使用捏合手势PinchGesture接口，将参数fingers设置为2。当捏合手势识别成功时，onActionStart()回调被适时触发，在这一过程中，会计算出当前图片缩放中心百分比位置。手势移动过程中会触发onActionUpdate()回调函数，在onActionUpdate()回调函数里计算出当前图片的缩放值以及图片在X方向和Y方向的偏移量，并实时更新图片的位置。

   ```
   1. // Two-finger scaling
   2. PinchGesture({ fingers: 2, distance: 1 })
   3. .onActionStart((event: GestureEvent) => {
   4. this.imageModel.pinchGestureStart(event);
   5. if (this.isOverlay) {
   6. this.isOverlay = false;
   7. }
   8. })
   9. .onActionUpdate((event: GestureEvent) => {
   10. this.isDisableSwipe = this.imageModel.pinchGestureUpdate(event);
   11. })
   12. .onActionEnd(() => {
   13. this.imageModel.pinchGestureEnd();
   14. }),
   ```

   [ImageItemView.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/view/ImageItemView.ets#L128-L141)
4. 图片缩放中心百分比位置的计算：成功识别到双指捏合手势触发onActionStart()函数，计算出图片缩放中心的百分比位置this.center，this.center用于图片缩放时，所产生的偏移量（若缩放中心并非位于图片中心点），下面将具体介绍图片缩放中心的百分比位置的计算方法：
   * cX = Math.max((centerX - imgX) / imgDisplayWidth, 0)

     = Math.max((centerX - ((this.componentWidth - ( (this.imageWidth \* this.lastScale))) / 2 + this.lastOffsetX)) / (this.imageWidth \* this.lastScale), 0)

     = Math.max((捏合手势中心点的X轴坐标 - ((组件屏幕的宽度 - (图片的宽度 \* 上次图片的缩放值)) / 2 + 上次图片Y方向的偏移量)) / ( 图片的宽度 \* 上次图片的缩放值 ), 0)
   * cY = Math.max((centerY - imgY) / imgDisplayHeight, 0);

     = Math.max((centerY - ((this.componentHeight - (this.imageHeight \* this.lastScale)) / 2 + this.lastOffsetY)) / (this.imageHeight \* this.lastScale), 0)

     = Math.max((捏合手势中心点的Y轴坐标 - ((组件屏幕的高度 - (图片的高度 \* 上次图片的缩放值)) / 2 + 上次图片Y方向的偏移量)) / (图片的高度 \* 上次图片的缩放值), 0)

     ```
     1. // Calculates the percentage position of the current zoom center relative to the picture
     2. evaluateCenter(centerX: number, centerY: number): [number, number] {
     3. let imgDisplayWidth = this.imageWidth * this.lastScale;
     4. let imgDisplayHeight = this.imageHeight * this.lastScale;
     5. let imgX = (this.componentWidth - imgDisplayWidth) / 2 + this.lastOffsetX;
     6. let imgY = (this.componentHeight - imgDisplayHeight) / 2 + this.lastOffsetY;
     7. let cX = Math.max((centerX - imgX) / imgDisplayWidth, 0);
     8. let cY = Math.max((centerY - imgY) / imgDisplayHeight, 0);
     9. return [cX, cY];
     10. }

     12. // ...

     14. // Pinch gesture recognition successful callback.
     15. pinchGestureStart(event: GestureEvent): void {
     16. this.center = this.evaluateCenter(event.pinchCenterX, event.pinchCenterY);
     17. this.centerX = 1 - this.center[0];
     18. this.centerY = 1 - this.center[1];
     19. AppStorage.setOrCreate('isImgDefaultSize', false);
     20. }
     ```

     [CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L216-L255)
5. 图片缩放：在捏合手势触发移动操作时，通过调用自定义onScale()方法，计算得出当前图片的缩放值以及由双指缩放动作引起的水平偏移量curOffsetX和垂直偏移量curOffsetY，最后，调用matrix4.identity().scale()对图片进行缩放，至此，图片的缩放“跟手”操作已完成。

   ```
   1. // General picture scaling value method.
   2. pictureScaling(scale: number): void {
   3. this.matrix = matrix4.identity().scale({
   4. x: scale,
   5. y: scale
   6. }).copy();
   7. }

   9. // ...

   11. // Pinch gestures callback during a move.
   12. pinchGestureUpdate(event: GestureEvent): boolean {
   13. this.onScale(event.scale, event.offsetX, event.offsetY);
   14. this.pictureScaling(this.curScale);
   15. if (this.curScale > this.defaultScaleValue) {
   16. this.isDisableSwipe = true;
   17. }
   18. this.pictureBoundaryRestriction();
   19. return this.isDisableSwipe;
   20. }

   22. // ...

   24. // Calculates the offset X and offset Y of the current picture and the scaling value of the current picture.
   25. onScale(scale: number, offX: number, offY: number): void {
   26. if (this.lastScale * scale > this.maxScale) {
   27. this.curScale = this.maxScale;
   28. } else if (this.lastScale * scale < this.minScale) {
   29. this.curScale = this.minScale;
   30. } else {
   31. this.curScale = this.lastScale * scale;
   32. }
   33. if (this.lastScale * scale === this.maxScale) {
   34. this.curScale -= 0.001;
   35. }
   36. this.evaluateOffsetRange();
   37. if (this.curScale < this.maxScale) {
   38. this.curOffsetY =
   39. (this.lastOffsetY + offY) + (0.5 - this.centerY) * this.imageHeight * (1 - scale) * this.lastScale;
   40. this.curOffsetX =
   41. (this.lastOffsetX + offX) + (0.5 - this.centerX) * this.imageWidth * (1 - scale) * this.lastScale;
   42. }
   43. // When the image is in the process of moving, it has not reached the boundary point.
   44. this.isArriveBoundary = false;
   45. // If the image has not reached the boundary, do not allow the image to be switched.
   46. if (!this.isArriveBoundary) {
   47. this.isDisableSwipe = true;
   48. }
   49. }
   ```

   [CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L167-L380)

### 边界限制的实现

1. 图片边界限制：主要涉及两个方面：当前图片显示边界的计算以及offset范围计算。

   调用自定义initCurrentImageInfo()方法，计算出当前图片的宽度this.imageModel.imageWidth和高度this.imageModel.imageHeight。

   ```
   1. /**
   2. * Set information about the current image: uri, whRatio, pixelMap, defaultSize, maxScaleValue
   3. * Obtain the Image information in advance for the size setting of
   4. * the image component and subsequent related calculations
   5. */
   6. initCurrentImageInfo(): void {
   7. try {
   8. let img = this.context.resourceManager.getMediaContentSync(this.imageData?.id);
   9. let imageSource = image.createImageSource(img.buffer.slice(0));
   10. imageSource.getImageInfo(0).then((data: image.ImageInfo) => {
   11. this.imageWHRatio = data.size.width / data.size.height;
   12. // Calculate scale ratios for both width and height to ensure image fits completely
   13. let widthRatio = this.imageModel.componentWidth / data.size.width;
   14. let heightRatio = this.imageModel.componentHeight / data.size.height;
   15. // Use the smaller ratio to ensure the image fits within the screen bounds
   16. let scaleRatio = Math.min(widthRatio, heightRatio);
   17. this.imageModel.imageWidth = data.size.width * scaleRatio;
   18. this.imageModel.imageHeight = data.size.height * scaleRatio;
   19. }).catch((err: BusinessError) => {
   20. hilog.error(0x0000, TAG, `[error][getImageInfo]${err.message}`);
   21. });
   22. } catch (err) {
   23. hilog.error(0x0000, TAG, `GetMediaContentSync failed. Cause code: ${err.code}, message: ${err.message}`);
   24. }
   25. }
   ```

   [ImageItemView.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/view/ImageItemView.ets#L57-L81)

   调用自定义windowSize()方法，计算出当前组件的宽度this.componentWidth和高度this.componentHeight。

   最后，调用自定义evaluateOffsetRange()方法，在图片缩放后，计算出图片在四个方向上的边界值：具体包括最大水平偏移量this.maxOffsetX、最小水平偏移量this.minOffsetX、最大垂直偏移量this.maxOffsetY以及最小垂直偏移量this.minOffsetY

   ```
   1. // Get window size.
   2. windowSize(): void {
   3. window.getLastWindow(context).then((window: window.Window) => {
   4. try {
   5. this.componentWidth = uiContext!.px2vp(window.getWindowProperties().windowRect.width);
   6. this.componentHeight = uiContext!.px2vp(window.getWindowProperties().windowRect.height);
   7. } catch (err) {
   8. hilog.error(DOMAIN, TAG, FORMAT,
   9. `GetWindowProperties failed. Cause code: ${err.code}, message: ${err.message}`);
   10. }
   11. }).catch((err: BusinessError) => {
   12. hilog.error(DOMAIN, TAG, FORMAT, `GetLastWindow failed. Cause code: ${err.code}, message: ${err.message}`);
   13. });
   14. }

   16. // ...

   18. // Calculate the range of the picture boundary.
   19. evaluateOffsetRange(): void {
   20. // Calculate the actual display size of the scaled image.
   21. let scaledImageWidth = this.imageWidth * this.curScale;
   22. let scaledImageHeight = this.imageHeight * this.curScale;

   24. // Calculation of X-axis boundaries
   25. if (scaledImageWidth > this.componentWidth) {
   26. // If the width of the picture exceeds the width of the screen, you can move it left and right.
   27. let maxXOffset = (scaledImageWidth - this.componentWidth) / 2;
   28. this.maxOffsetX = maxXOffset;
   29. this.minOffsetX = -maxXOffset;
   30. } else {
   31. // The width of the image does not exceed the width of the screen. It should be centered and no X-axis offset is allowed.
   32. this.maxOffsetX = 0;
   33. this.minOffsetX = 0;
   34. }

   36. // Y-axis boundary calculation
   37. if (scaledImageHeight > this.componentHeight) {
   38. // If the image height exceeds the screen height, it can be scrolled up and down.
   39. let maxYOffset = (scaledImageHeight - this.componentHeight) / 2;
   40. this.maxOffsetY = maxYOffset;
   41. this.minOffsetY = -maxYOffset;
   42. } else {
   43. // The height of the image does not exceed the height of the screen. It should be centered and no Y-axis offset is allowed.
   44. this.maxOffsetY = 0;
   45. this.minOffsetY = 0;
   46. }
   47. }
   ```

   [CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L150-L212)
2. 图片在滑动或缩放过程中，一旦触及边界，便会触发restrictBound()方法进行判断。若图片抵达最上方边界，则立即将当前Y方向的偏移位置this.curOffsetY设置为该方向的最大偏移值this.maxOffsetY，以此实现对边界的有效限制。同样的逻辑也适用于其他三个方向：当图片到达最下方、最左侧或最右侧边界时，也会相应地调整其偏移位置，确保图片始终在规定的范围内活动。

   当图片滑动至左边界或右边界时，this.isDisableSwipe会被设置为false；此时，Swiper组件将激活滑动切换功能，允许用户切换图片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/5wMU5RYMQyyjkH8eV5ZdCQ/zh-cn_image_0000002194010992.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001942Z&HW-CC-Expire=86400&HW-CC-Sign=FDDDAB7E22133C012107C58099AB51D3F0935341F9E9E40A3D7E1AEC9468CB6B "点击放大")

   ```
   1. // Picture Boundary Restriction
   2. pictureBoundaryRestriction(): void {
   3. // X-axis boundary restriction
   4. if (this.curOffsetX > this.maxOffsetX) {
   5. this.curOffsetX = this.maxOffsetX;
   6. this.isDisableSwipe = false;
   7. this.isArriveBoundary = true;
   8. } else if (this.curOffsetX < this.minOffsetX) {
   9. this.curOffsetX = this.minOffsetX;
   10. this.isDisableSwipe = false;
   11. this.isArriveBoundary = true;
   12. }
   13. // Y-axis boundary limit
   14. if (this.curOffsetY > this.maxOffsetY) {
   15. this.curOffsetY = this.maxOffsetY;
   16. } else if (this.curOffsetY < this.minOffsetY) {
   17. this.curOffsetY = this.minOffsetY;
   18. }
   19. // When the image cannot fill the entire screen, force it to be centered.
   20. let scaledImageWidth = this.imageWidth * this.curScale;
   21. let scaledImageHeight = this.imageHeight * this.curScale;
   22. if (scaledImageWidth <= this.componentWidth) {
   23. // The width of the image does not exceed the screen. Force the X-axis to be centered.
   24. this.curOffsetX = 0;
   25. }
   26. if (scaledImageHeight <= this.componentHeight) {
   27. // The height of the image does not exceed the screen, and the Y-axis is forced to be centered.
   28. this.curOffsetY = 0;
   29. }
   30. }
   ```

   [CommonModel.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/model/CommonModel.ets#L259-L288)

### 实现Swiper组件与滑动手势冲突的解决方案

当Swiper组件与PanGesture滑动手势事件在同一组件上并发作用时，两者之间的冲突会导致Swiper无法正常切换图片。下面，将详细讲解如何有效解决Swiper组件与滑动手势之间的冲突问题。

说明

* Swiper组件内包含了[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)拖动手势事件，用于滑动轮播子组件。[disableSwipe](../harmonyos-references/ts-container-swiper.md#disableswipe8)属性设为true会取消内部的PanGesture事件监听。

1. 需要将Swiper组件的disableSwipe属性设置为变量this.isDisableSwipe，即disableSwipe(this.isDisableSwipe)。

   当图片处于默认尺寸，或是已滑动到左右边界之时，应将this.isDisableSwipe的值设定为false；当图片处于放大状态且尚未滑动至左右边界时，应将this.isDisableSwipe的值设定为true。

   ```
   1. @Builder
   2. PhotoSwiper() {
   3. Swiper(this.homeSwipeController) {
   4. ForEach(this.ImgData, (img: Resource) => {
   5. ImageItemView({
   6. imageData: img,
   7. isOverlay: this.isOverlay
   8. })
   9. .width('100%')
   10. .height('100%')
   11. }, (img: Resource, index: number) => JSON.stringify(img) + index)
   12. }
   13. // ...
   14. .disableSwipe(this.isDisableSwipe)
   15. // ...
   ```

   [HomePage.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/pages/HomePage.ets#L157-L202)
2. PanGesture接口被用于实现滑动手势控制，其中参数distance需根据变量进行动态设置与判断。具体而言，当this.isDisableSwipe被设置为true时，Swiper组件将禁用滑动切换功能，此时，为了保持拖动图片时的流畅性，需要将distance的值设定为一个较小的数值。相反，当this.isDisableSwipe为false时，Swiper组件则会启用滑动切换功能，此时，为了让用户能够更灵敏地触发Swiper组件的滑动操作，distance的值则需适当增大，以优化用户的交互体验。至此，Swiper组件与滑动手势之间的冲突问题便得到解决。

   ```
   1. PanGesture({ fingers: 1, distance: this.isDisableSwipe ? 3 : 50 })
   ```

   [ImageItemView.ets](https://gitcode.com/HarmonyOS_Samples/PicturePreview/blob/master/entry/src/main/ets/view/ImageItemView.ets#L118-L118)

## 常见问题

### 在Swiper组件中，当为图片子组件配置了PanGesture后，swiper无法正常翻页，该如何解决手势冲突？

通过使用Swiper组件的disableSwipe属性，进行动态赋值，在图片保持默认尺寸或图片在放大状态下已触及边界时，将disableSwipe属性设置为false，从而使得Swiper能够切换图片；当图片处于放大状态且尚未到达边界时，则将disableSwipe属性设为true，此时Swiper的切换功能将被禁用。

### 当图片被放大后，若在拖动图片的过程中，该如何控制其边界，确保图片不会超出显示区域的界限？

该问题涉及到图片边界的约束。主要涉及两个方面：当前图片显示边界计算以及offset范围计算。当前图片显示边界计算可得出当前图片显示的位置，左右上下是否与显示区域边界对齐，如果已经对齐，则不能继续往某个方向继续拖动。平移/缩放时必须对offset作限制，否则图片将被移出显示区域或是手势结束后周围有黑边。只需在手势交互时根据当前的scale计算得出offset的范围即可（超出边界时取边界作为结果），即可对图片边界进行限制。

## 示例代码

* [基于ArkUI实现图片预览功能](https://gitcode.com/harmonyos_samples/PicturePreview)
