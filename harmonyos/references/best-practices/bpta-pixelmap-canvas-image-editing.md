---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pixelmap-canvas-image-editing
title: 基于PixelMap与Canvas实现图片编辑
breadcrumb: 最佳实践 > 行业场景解决方案 > 拍摄美化 > 基于PixelMap与Canvas实现图片编辑
category: best-practices
scraped_at: 2026-09-02T15:03:21+08:00
doc_updated_at: 2026-08-17
content_hash: sha256:e26ab97ecaef9629ac4f9071bcfede1dfc3d4be98a4196c1a246056ef90b2073
---

## 概述

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)是ArkUI框架中用于自定义绘制图形的核心组件，提供了灵活的绘制能力，支持绘制基础形状、文本、图片以及复杂的图形变换。

本文主要基于[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)和Canvas实现图片编辑处理，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据、图片水印添加等。

相关场景描述及关键技术点如下表所示：

| 功能描述 | **场景描述** | **关键技术点** |
| --- | --- | --- |
| 图片平移 | 沿水平/垂直方向调整图片位置，用于构图微调。 | 通过Canvas.[drawImage()](../harmonyos-references/ts-components-canvas-common-method.md#drawimage-1)结合图片偏移量，在画布上重绘图片实现平移。 |
| 图片水印添加 | 为图片添加水印文字，支持自定义水印文本、字号、透明度、角度、是否重复等，用于用户版权保护或品牌标识。 | 通过[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)离屏画布对象绘制原图叠加水印，并结合水印文本宽度、水印坐标、水印透明度、水印旋转、循环绘制水印，导出合成像素图更新预览。 |
| 其他场景参考《基于PixelMap编解码编辑图片开发实践》[功能描述](bpta-pixelmap-image-editing.md#table032535983016)。 | | |

本文主要介绍以下图片编辑功能的实现：

* [图片信息展示](bpta-pixelmap-canvas-image-editing.md#section954615833416)
* [图片按比例裁剪](bpta-pixelmap-canvas-image-editing.md#section1121785263415)
* [图片平移](bpta-pixelmap-canvas-image-editing.md#section1212125833415)
* [图片旋转](bpta-pixelmap-canvas-image-editing.md#section734176113514)
* [图片镜像翻转](bpta-pixelmap-canvas-image-editing.md#section790181203518)
* [图片等比缩放](bpta-pixelmap-canvas-image-editing.md#section74891720153520)
* [图片亮度调节](bpta-pixelmap-canvas-image-editing.md#section1399483012357)
* [图片透明度调节](bpta-pixelmap-canvas-image-editing.md#section15901146203511)
* [图片饱和度调节](bpta-pixelmap-canvas-image-editing.md#section3818105353513)
* [图片黑白滤镜](bpta-pixelmap-canvas-image-editing.md#section19705117362)
* [图片高亮滤镜](bpta-pixelmap-canvas-image-editing.md#section159302811368)
* [图片反转滤镜](bpta-pixelmap-canvas-image-editing.md#section18101338377)
* [图片模糊滤镜](bpta-pixelmap-canvas-image-editing.md#section1782616404373)
* [图片水印编辑](bpta-pixelmap-canvas-image-editing.md#section169301646143717)

## 图片信息展示

### 场景描述

获取图片信息展示在页面中。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/ALOHh7S5QtaycuEaiWmUSg/zh-cn_image_0000002701055813.png "点击放大")

### 实现原理

具体实现原理可参考《基于PixelMap编解码编辑图片开发实践》的图片信息展示[实现原理](bpta-pixelmap-image-editing.md#section1261510595272)。

### 开发步骤

具体开发步骤可参考《基于PixelMap编解码编辑图片开发实践》的图片信息展示[开发步骤](bpta-pixelmap-image-editing.md#section19815184162818)。

## 图片按比例裁剪

### 场景描述

将图片按照1:1、4:3或16:9进行裁剪。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/AM--GT_4SuaO4k0UfsTTqw/zh-cn_image_0000002671336004.gif "点击放大")

### 实现原理

具体实现原理可参考《基于PixelMap编解码编辑图片开发实践》的图片按比例裁剪[实现原理](bpta-pixelmap-image-editing.md#section65881029132712)。

### 开发步骤

具体开发步骤可参考《基于PixelMap编解码编辑图片开发实践》的图片按比例裁剪[开发步骤](bpta-pixelmap-image-editing.md#section185153402718)。

## 图片平移

### 场景描述

通过滑动Slider，在横向/纵向调节图片位置。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/C12u-mfvRWSA1kT3vaRYdA/zh-cn_image_0000002671176148.gif "点击放大")

### 实现原理

通过Slider控制横向/纵向的偏移量，将偏移量叠加到图片在Canvas上的绘制坐标中，触发画布重绘实现图片平移效果。

### 开发步骤

1. 在Slider组件的onChange()事件中，调用sliderChange()方法将滑块值换算为像素偏移量。

   ```typescript
   sliderChange(value: number, mode: SliderChangeMode) {
     // Only start when the slider drag is completed to avoid frequent calculations.
     if ((mode === SliderChangeMode.End) && (value !== this.currentTranslateData[this.currentTranslateIndex])) {
       // Reset offset when entering translation mode for the first time.
       if (this.isInitTranslateValue) {
         this.translateX = 0;
         this.translateY = 0;
       }
       // Save current slider value.
       this.currentTranslateData[this.currentTranslateIndex] = Math.round(value);
       if (this.currentTranslateIndex === 0) {
         // Lateral offset: offset = (display width of image + starting x-coordinate of image) * (slider value / 1000).
         this.translateX = (this.displaySize.width + this.displaySize.x) * (value / 1000);
       } else if (this.currentTranslateIndex === 1) {
         // Vertical offset: offset = image display height * (slider value / 1000).
         this.translateY = this.displaySize.height * (value / 1000);
       }
       // Trigger canvas redraw.
       this.flushPixelMapChange();
       this.isInitTranslateValue = false;
     }
   }
   ```

   ```typescript
   flushPixelMapChange() {
     setTimeout(() => {
       this.drawImageOnCanvas();
     }, this.refreshRate);
   }
   ```
2. 在drawImageOnCanvas()方法中绘制图片时，将平移偏移量叠加到最终坐标。

   ```typescript
   // Canvas drawing
   drawImageOnCanvas() {
     // ...

     try {
       // Clear the canvas.
       this.canvasRenderingContext.clearRect(0, 0, this.containerWidth, this.containerHeight);

       this.previewPixelMap?.getImageInfo().then((info) => {
         this.imageWidth = info.size.width; // Update to actual width after rotation.
         this.imageHeight = info.size.height; // Update to actual height after rotation.

         this.displaySize = this.calculateImageDisplaySize();

         if (this.displaySize.width > 0 && this.displaySize.height > 0) {
           // Overlay offset: base position + canvas offset + translation offset.
           const finalX = this.displaySize.x + this.canvasOffsetX + this.translateX;
           const finalY = this.displaySize.y + this.canvasOffsetY + this.translateY;
           // Redraw image.
           this.canvasRenderingContext.drawImage(
             this.previewPixelMap,
             finalX,
             finalY,
             this.displaySize.width,
             this.displaySize.height
           );
           this.savePixelMap = this.canvasRenderingContext.getPixelMap(0, 0, this.containerWidth, this.containerHeight);
         }
       });
     } catch (error) {
       hilog.error(DOMAIN, TAG, '%{public}s, %{public}s', 'Canvas drawing failed:', JSON.stringify(error));
     }
   }
   ```

## 图片旋转

### 场景描述

点击图片旋转按钮，改变图片显示方向。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/53KcVcUoTHWO27Km0OFqbQ/zh-cn_image_0000002701095735.gif "点击放大")

### 实现原理

1. 通过[rotateSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#rotatesync12)方法，对像素图执行-90°逆时针旋转，旋转后像素图宽高互换，重新排列像素数据。
2. 旋转导致图片宽高比反转，重新计算图片在画布中的居中显示尺寸与位置，通过calculateImageDisplaySize()方法交换基准宽高，确保旋转后图片仍正确适配画布。

### 开发步骤

1. 定义clonePixelMap()方法克隆像素图，避免直接修改原始数据。

   通过[getImageInfoSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfosync12)获取图像像素信息，使用[readPixelsToBufferSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelstobuffersync12)按照PixelMap的像素格式，读取PixelMap的图像像素数据写入缓冲区，并调用[createPixelMapSync()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmapsync12)通过图片解码参数创建PixelMap对象。

   ```typescript
   clonePixelMap(pixelMap: PixelMap, desiredPixelFormat?: image.PixelMapFormat): PixelMap {
     try {
       // Obtain image pixel information.
       const imageInfo = pixelMap.getImageInfoSync();
       const buffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
       const options: image.InitializationOptions = {
         srcPixelFormat: imageInfo.pixelFormat,
         pixelFormat: desiredPixelFormat ?? imageInfo.pixelFormat,
         size: imageInfo.size,
       };
       // Read pixel information and write to buffer.
       pixelMap.readPixelsToBufferSync(buffer);
       return image.createPixelMapSync(buffer, options); // Create pixelMap.
     } catch (err) {
       hilog.error(0xFF00, TAG, '%{public}s', 'have errors', `${JSON.stringify(err)}`);
       return pixelMap;
     }
   }
   ```
2. 在getStartEditPixelMap()中，根据编辑模式通过clonePixelMap()拷贝PixelMap对象并返回。

   ```typescript
   getStartEditPixelMap(mode: EditType): PixelMap {
     if (this.editMode !== mode) {
       this.editMode = mode;
       this.startEditPixelMap = this.finalEditPixelMap;
     }
     let target: PixelMap | undefined;
     switch (mode) {
       case EditType.CROP:
         target = this.startEditPixelMap;
         break;
       case EditType.MIRROR:
         target = this.finalEditPixelMap;
         break;
       case EditType.ROTATION:
         target = this.finalEditPixelMap;
         break;
       case EditType.FILTER:
         target = this.startEditPixelMap;
         break;
       case EditType.ADJUST:
         target = this.startEditPixelMap;
         break;
       case EditType.TRANSLATION:
         target = this.finalEditPixelMap;
         break;
       case EditType.SCALE:
         target = this.startEditPixelMap;
         break;
       case EditType.WATER:
         target = this.startEditPixelMap;
         break;
       default:
         target = this.finalEditPixelMap;
         break;
     }
     // Clone pixelMap.
     return this.clonePixelMap(target!);
   }
   ```
3. 在PixelMapManager类中定义rotateImage()方法，调用getStartEditPixelMap()获取当前编辑用的PixelMap对象，并执行[rotateSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#rotatesync12)传入-90，使图片在每次点击时逆时针旋转90°，并更新预览。

   ```typescript
   rotateImage() {
     // Obtain the cloned baseline pixel image.
     const px = this.getStartEditPixelMap(EditType.ROTATION);
     try {
       px.rotateSync(CommonConstants.ANTI_CLOCK); // Perform rotation.
     } catch (error) {
       Logger.error(TAG, `there is a error in rotateSync process with ${error?.code}`);
     }
     this.notifyPreviewUpdate(px); // Update Preview.
     this.finalEditPixelMap = px; // Save edited pixelMap.
   }
   ```
4. 旋转后像素宽高互换，在calculateImageDisplaySize()中isRotate标记处理旋转变化。
   * 当isRotate为true：不重新按宽高比计算，直接将上一次的displaySize宽高互换。
   * 当isRotate为false：正常按图片宽高比与容器宽高比计算适配尺寸。

   ```typescript
   calculateImageDisplaySize(): ImageDisplaySize {
     // ...

     const containerRatio = this.containerWidth / this.containerHeight;
     const imageRatio = this.imageWidth / this.imageHeight;
     const zoomFactor = this.currentZoom / 100; // Scaling factor: 0.8~1.2.

     let baseDisplayWidth: number;
     let baseDisplayHeight: number;
     if (this.currentEditMode === 0 && this.isRotate) {
       // Swap the width and height of the previous display size as the reference during rotation.
       baseDisplayWidth = this.displaySize!.height;
       baseDisplayHeight = this.displaySize!.width;
     } else {
       // Calculate the adaptation size based on aspect ratio.
       if (imageRatio > containerRatio) {
         // Width map: adapt according to container width.
         baseDisplayWidth = this.containerWidth;
         baseDisplayHeight = this.containerWidth / imageRatio;
       } else {
         // Height map: adapt according to container height.
         baseDisplayHeight = this.containerHeight;
         baseDisplayWidth = this.containerHeight * imageRatio;
       }
     }
     // Apply scaling factor.
     const displayWidth = baseDisplayWidth * zoomFactor; // base width * scaling factor
     const displayHeight = baseDisplayHeight * zoomFactor; // base width * scaling factor
     // Center offset.
     const x = (this.containerWidth - displayWidth) / 2;
     const y = (this.containerHeight - displayHeight) / 2;
     this.isRotate = false;
     return {
       x,
       y,
       width: displayWidth,
       height: displayHeight
     };
   }
   ```
5. 在页面点击事件中，调用PixelMapManager的rotateImage()执行图片旋转。并通过flushPixelMapChange()方法，执行drawImageOnCanvas()重绘显示图片旋转效果。

   ```typescript
   rotateImage() {
     this.isRotate = true;
     this.pixelMapManager?.rotateImage();
     this.flushPixelMapChange();
   }
   ```

   ```typescript
   // Clear the canvas.
   this.canvasRenderingContext.clearRect(0, 0, this.containerWidth, this.containerHeight);

   this.previewPixelMap?.getImageInfo().then((info) => {
     this.imageWidth = info.size.width; // Update to actual width after rotation.
     this.imageHeight = info.size.height; // Update to actual height after rotation.

     this.displaySize = this.calculateImageDisplaySize();

     if (this.displaySize.width > 0 && this.displaySize.height > 0) {
       // Overlay offset: base position + canvas offset + translation offset.
       const finalX = this.displaySize.x + this.canvasOffsetX + this.translateX;
       const finalY = this.displaySize.y + this.canvasOffsetY + this.translateY;
       // Redraw image.
       this.canvasRenderingContext.drawImage(
         this.previewPixelMap,
         finalX,
         finalY,
         this.displaySize.width,
         this.displaySize.height
       );
       this.savePixelMap = this.canvasRenderingContext.getPixelMap(0, 0, this.containerWidth, this.containerHeight);
     }
   });
   ```

## 图片镜像翻转

### 场景描述

点击镜像翻转按钮，使图片进行水平翻转。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/jtgVjAthR9agQUO1COJaMg/zh-cn_image_0000002701055815.gif "点击放大")

### 实现原理

通过[flip()](../harmonyos-references/arkts-apis-image-pixelmap.md#flip9-1)方法，根据输入的条件对图片进行翻转。

* horizontal：true表示进行水平翻转；false表示不进行水平翻转。
* vertical：true表示进行垂直翻转；false表示不进行垂直翻转。

### 开发步骤

1. 在PixelMapManager类中定义mirrorImage()，调用[flip()](../harmonyos-references/arkts-apis-image-pixelmap.md#flip9-1)方法对图片进行翻转，并更新预览。

   ```typescript
   mirrorImage(mirrorType: MirrorType) {
     // Obtain the cloned baseline pixel image.
     const px = this.getStartEditPixelMap(EditType.MIRROR);
     if (mirrorType === MirrorType.CLOCKWISE) {
       try {
         px.flip(true, false); // Perform flip.
       } catch (error) {
         Logger.error(TAG, `there is a error in flip process with ${error?.code}`);
       }
     }
     this.notifyPreviewUpdate(px); // Update Preview.
     this.finalEditPixelMap = px; // Save edited pixelMap.
   }
   ```
2. 在页面点击事件中，调用PixelMapManager的mirrorImage()方法执行图片翻转。并通过flushPixelMapChange()方法，执行drawImageOnCanvas()触发Canvas重绘，实现图片镜像翻转效果。

   ```typescript
   mirrorImage() {
     this.pixelMapManager?.mirrorImage(MirrorType.CLOCKWISE);
     this.flushPixelMapChange(); // Canvas redraw.
   }
   ```

## 图片等比缩放

### 场景描述

滑动Slider，图片按照比例进行缩小或放大。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/4dZJzODYTzeSJEU-_HYsOQ/zh-cn_image_0000002671336006.gif "点击放大")

### 实现原理

1. 通过[scale()](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9-1)方法，根据输入宽高的缩放倍数对图片进行缩放。
2. 缩放后像素图尺寸变化，在calculateImageDisplaySize()方法中，根据缩放因子重新计算图片在画布中的显示尺寸。

### 开发步骤

1. 在PixelMapManager类中定义editImageScale()，调用[scale()](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9-1)方法根据传入的缩放系数对图片进行缩放。

   ```typescript
   async editImageScale(scale: number) {
     // Obtain the cloned baseline pixel image.
     const px = this.getStartEditPixelMap(EditType.SCALE);
     await px.scale(scale, scale); // Scale proportionally.
     this.notifyPreviewUpdate(px); // Update Preview.
   }
   ```
2. 在calculateImageDisplaySize()中根据缩放因子重新计算尺寸。
   * zoomFactor = 1.0（100%）：显示尺寸 = 基础适配尺寸。图片完整居中显示。
   * zoomFactor = 1.2（120%）：显示尺寸 = 基础尺寸 \* 1.2。图片放大超出画布，四周裁剪。
   * zoomFactor = 0.8（80%）： 显示尺寸 = 基础尺寸 \* 0.8。图片缩小，四周留黑边。

   ```typescript
   calculateImageDisplaySize(): ImageDisplaySize {
     // ...

     const containerRatio = this.containerWidth / this.containerHeight;
     const imageRatio = this.imageWidth / this.imageHeight;
     const zoomFactor = this.currentZoom / 100; // Scaling factor: 0.8~1.2.

     let baseDisplayWidth: number;
     let baseDisplayHeight: number;
     if (this.currentEditMode === 0 && this.isRotate) {
       // Swap the width and height of the previous display size as the reference during rotation.
       baseDisplayWidth = this.displaySize!.height;
       baseDisplayHeight = this.displaySize!.width;
     } else {
       // Calculate the adaptation size based on aspect ratio.
       if (imageRatio > containerRatio) {
         // Width map: adapt according to container width.
         baseDisplayWidth = this.containerWidth;
         baseDisplayHeight = this.containerWidth / imageRatio;
       } else {
         // Height map: adapt according to container height.
         baseDisplayHeight = this.containerHeight;
         baseDisplayWidth = this.containerHeight * imageRatio;
       }
     }
     // Apply scaling factor.
     const displayWidth = baseDisplayWidth * zoomFactor; // base width * scaling factor
     const displayHeight = baseDisplayHeight * zoomFactor; // base width * scaling factor
     // Center offset.
     const x = (this.containerWidth - displayWidth) / 2;
     const y = (this.containerHeight - displayHeight) / 2;
     this.isRotate = false;
     return {
       x,
       y,
       width: displayWidth,
       height: displayHeight
     };
   }
   ```
3. 滑动Slider时，调用sliderZoomChange()方法，在滑动结束时且值发生变化后，将value除以100作为缩放系数传入editImageScale()中执行像素级缩放，并通过flushPixelMapChange()执行drawImageOnCanvas()方法重绘显示缩放效果。

   ```typescript
   async sliderZoomChange(value: number, mode: SliderChangeMode) {
     if ((mode === SliderChangeMode.End) && (value !== this.currentZoom)) {
       let zoom = value / 100;
       await this.pixelMapManager?.editImageScale(zoom);
       this.currentZoom = value;
       this.flushPixelMapChange();
     }
   }
   ```

## 图片亮度调节

### 场景描述

滑动Slider，调节图片显示亮度。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/rMohNcJsRbisFnnFooRmHQ/zh-cn_image_0000002671176158.gif "点击放大")

### 实现原理

通过线性缩放每个像素的RGB分量来改变图像的整体明暗程度。

对应公式：

R\_new = R\_original \* factor

G\_new = G\_original \* factor

B\_new = B\_original \* factorfactor = 当前调节值 / 100

原理说明：

* 当factor > 1时，RGB值增大，图像变亮。
* 当factor < 1时，RGB值减小，图像变暗。
* 当factor = 1时，保持原始亮度。

### 开发步骤

1. 定义execColorInfo()接收像素缓冲区、上次值、当前值、调节类型，计算调整后的RGB值，并确保值转回0~255范围内，返回处理后的缓冲区。

   ```typescript
   export function execColorInfo(bufferArray: ArrayBuffer, last: number, cur: number, hsvIndex: number) {
     // ...

     try {
       const pixelData = new Uint8ClampedArray(bufferArray);
       const adjustedData = new Uint8ClampedArray(pixelData.length);
       const bytesPerPixel = 4;
       const factor = cur / 100; // Adjustment factor
       for (let i = 0; i < pixelData.length; i += bytesPerPixel) {
         // Reserve the alpha channel
         adjustedData[i + 3] = pixelData[i + 3];
         // Skip the pixels that are completely transparent
         if (pixelData[i + 3] < 1) {
           continue;
         }
         if (hsvIndex === AdjustType.BRIGHTNESS) {
           // Calculate adjusted RGB values (keep relative proportions)
           let r = pixelData[i] * factor;
           let g = pixelData[i + 1] * factor;
           let b = pixelData[i + 2] * factor;

           // Ensure the value is in the valid range (0-255)
           adjustedData[i] = Math.max(0, Math.min(255, Math.round(r)));
           adjustedData[i + 1] = Math.max(0, Math.min(255, Math.round(g)));
           adjustedData[i + 2] = Math.max(0, Math.min(255, Math.round(b)));
         }
         // ...
       }
       return adjustedData.buffer;
     } catch (error) {
       hilog.error(DOMAIN, TAG, '%{public}s', 'error', `${JSON.stringify(error)}`);
       return null;
     }
   }
   ```
2. 在Worker线程中接收主线程消息，调用execColorInfo()处理后返回结果。

   ```typescript
   let workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   /**
    * Defines the event handler to be called when the worker thread receives a message sent by the host thread.
    * The event handler is executed in the worker thread.
    *
    * @param e message data
    */
   workerPort.onmessage = function (event: MessageEvents) {
     let bufferArray = event.data.buf;
     let last = event.data.last;
     let cur = event.data.cur;
     let adjustType = event.data.adjustType;
     let buffer = execColorInfo(bufferArray, last, cur, adjustType);
     workerPort.postMessage(buffer); // Return processed buffer.
   };
   ```
3. 在PixelMapManager中实现调节入口。
   1. 定义processAdjustWorker()方法，获取像素buffer发送至Worker子线程。

      ```typescript
      private processAdjustWorker(value: number, buffer: ArrayBuffer, adjustType: AdjustType): Promise<ArrayBuffer> {
        return new Promise((resolve) => {
          const message = new MessageItem(buffer, CommonConstants.SLIDER_MAX, value, adjustType);
          try {
            this.adjustWorker.postMessage(message);
          } catch (error) {
            hilog.error(0xFF00, TAG, '%{public}s', 'have errors', `${JSON.stringify(error)}`);
          }
          this.adjustWorker.onmessage = (event: MessageEvents) => {
            resolve(event.data);
          };
        });
      }
      ```
   2. 定义adjustImage()方法，调用processAdjustWorker()并传入当前亮度滑块值、像素buffer、调节类型（亮度），将处理后的buffer写回PixelMap。

      ```typescript
      async adjustImage(currentAdjustData: number[]) {
        // Obtain the cloned baseline pixel image.
        const px = this.getStartEditPixelMap(EditType.ADJUST);
        let buffer = new ArrayBuffer(px.getPixelBytesNumber());
        await px.readPixelsToBuffer(buffer); // Read the pixel data of pixelMap image.
        if (!buffer) {
          return;
        }
        if (currentAdjustData[AdjustType.BRIGHTNESS] !== CommonConstants.SLIDER_MAX) {
          try {
            buffer =
              await this.processAdjustWorker(currentAdjustData[AdjustType.BRIGHTNESS], buffer, AdjustType.BRIGHTNESS);
            // Write the brightness processed buffer back to pixelMap.
            px.writeBufferToPixelsSync(buffer);
          } catch (err) {
            hilog.error(0xFF00, TAG, '%{public}s', 'have errors', `${JSON.stringify(err)}`);
          }
        }
        // ...
        this.finalEditPixelMap = px;  // Save edited pixelMap.
        this.notifyPreviewUpdate(px); // Update Preview.
      }
      ```
4. 定义sliderChange()方法并执行adjustImage()。在Slider组件的onChange()事件中调用sliderChange()，当离手时触发，避免频繁计算，实现亮度调节。

   ```typescript
   async sliderChange(value: number, mode: SliderChangeMode) {
     if ((mode === SliderChangeMode.End) && (value !== this.currentAdjustData[this.currentAdjustType])) {
       const roundedValue = Math.round(value);
       this.currentAdjustData[this.currentAdjustType] = roundedValue;
       this.paramValues[this.currentAdjustType] = roundedValue;
       this.deviceListDialogController.open(); // Display loading pop-up window.
       await this.pixelMapManager?.adjustImage(this.paramValues);
       this.deviceListDialogController.close(); // Close pop-up window.
       this.flushPixelMapChange();
     }
   }
   ```

## 图片透明度调节

### 场景描述

滑动Slider，调节图片透明度。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/xYSbtl-tSfCNxAO68yVtqA/zh-cn_image_0000002701095807.gif "点击放大")

### 实现原理

具体实现原理可参考《基于PixelMap编解码编辑图片开发实践》的图片透明度调节[实现原理](bpta-pixelmap-image-editing.md#section995644621711)。

### 开发步骤

具体开发步骤可参考《基于PixelMap编解码编辑图片开发实践》的图片透明度调节[开发步骤](bpta-pixelmap-image-editing.md#section1682132314184)。

## 图片饱和度调节

### 场景描述

滑动Slider，调节图片饱和度。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AvTGtSokTV26OJ1yGaYyAw/zh-cn_image_0000002701055983.gif "点击放大")

### 实现原理

通过调整像素与其灰度值的距离，改变色彩鲜艳程度。

对应公式：

1. 计算像素亮度：

   luminance = 0.2126 \* r + 0.7152 \* g + 0.0722 \* b
2. 调整RGB分量（factor = 滑块当前值 / 100）：

   adjustedR = luminance + (r - luminance) \* factor

   adjustedG = luminance + (g - luminance) \* factor

   adjustedB = luminance + (b - luminance) \* factor

原理说明：

亮度系数：0.2126、0.7152、0.0722为ITU-R BT.709标准亮度转化系数。

* 当factor > 1时，颜色偏离灰度值更远，饱和度增加。
* 当factor < 1时，颜色向灰度值靠近，饱和度降低。
* 当factor = 0时，所有颜色等于亮度值，图像变为灰度图。

### 开发步骤

1. 在execColorInfo()内，提取图片RGB值并进行归一化处理，并调整饱和度向灰度值靠近或远离，将调整后的值转回0~255范围内写入缓冲区。

   ```typescript
   export function execColorInfo(bufferArray: ArrayBuffer, last: number, cur: number, hsvIndex: number) {
     // ...

     try {
       const pixelData = new Uint8ClampedArray(bufferArray);
       const adjustedData = new Uint8ClampedArray(pixelData.length);
       const bytesPerPixel = 4;
       const factor = cur / 100; // Adjustment factor
       for (let i = 0; i < pixelData.length; i += bytesPerPixel) {
         // Reserve the alpha channel
         adjustedData[i + 3] = pixelData[i + 3];
         // Skip the pixels that are completely transparent
         if (pixelData[i + 3] < 1) {
           continue;
         }
         // ...
         if (hsvIndex === AdjustType.SATURATION) {
           // Extract the RGB value and normalize it
           const r = pixelData[i] / 255;
           const g = pixelData[i + 1] / 255;
           const b = pixelData[i + 2] / 255;

           // Calculate the grayscale value
           const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;

           // Adjust saturation: move closer or further away from the grayscale value
           const adjustedR = luminance + (r - luminance) * factor;
           const adjustedG = luminance + (g - luminance) * factor;
           const adjustedB = luminance + (b - luminance) * factor;

           // Convert back to the 0-255 range and write to the buffer
           adjustedData[i] = Math.max(0, Math.min(255, Math.round(adjustedR * 255)));
           adjustedData[i + 1] = Math.max(0, Math.min(255, Math.round(adjustedG * 255)));
           adjustedData[i + 2] = Math.max(0, Math.min(255, Math.round(adjustedB * 255)));
         }
       }
       return adjustedData.buffer;
     } catch (error) {
       hilog.error(DOMAIN, TAG, '%{public}s', 'error', `${JSON.stringify(error)}`);
       return null;
     }
   }
   ```
2. 创建Worker线程接收主线程消息，调用execColorInfo()处理后返回结果。Worker实例初始化及与主线程通信，参考：图片亮度调节[开发步骤](bpta-pixelmap-canvas-image-editing.md#section262851718315)。
3. 在adjustImage()中，调用processAdjustWorker()将处理后的缓冲区传入[writeBufferToPixelsSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#writebuffertopixelssync12)，写入PixelMap。

   ```typescript
   async adjustImage(currentAdjustData: number[]) {
     // Obtain the cloned baseline pixel image.
     const px = this.getStartEditPixelMap(EditType.ADJUST);
     let buffer = new ArrayBuffer(px.getPixelBytesNumber());
     await px.readPixelsToBuffer(buffer); // Read the pixel data of pixelMap image.
     if (!buffer) {
       return;
     }
     // ...
     if (currentAdjustData[AdjustType.SATURATION] !== CommonConstants.SLIDER_MAX) {
       try {
         buffer =
           await this.processAdjustWorker(currentAdjustData[AdjustType.SATURATION], buffer, AdjustType.SATURATION);
         px.writeBufferToPixelsSync(buffer);
       } catch (err) {
         hilog.error(0xFF00, TAG, '%{public}s', 'have errors', `${JSON.stringify(err)}`);
       }
     }
     // ...
     this.finalEditPixelMap = px;  // Save edited pixelMap.
     this.notifyPreviewUpdate(px); // Update Preview.
   }
   ```
4. 在Slider组件的onChange()事件中调用sliderChange()，实现饱和度调节，参考图片亮度调节[开发步骤](bpta-pixelmap-canvas-image-editing.md#section262851718315)中的步骤4。

## 图片黑白滤镜

### 场景描述

选中黑白滤镜，图片显示黑白效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IgcpuG98QOu7BXD3LPj9SQ/zh-cn_image_0000002671336186.png "点击放大")

### 实现原理

通过[effectKit.createEffect()](../harmonyos-references/js-apis-effectkit.md#effectkitcreateeffect)创建滤镜效果器，调用[grayscale()](../harmonyos-references/js-apis-effectkit.md#grayscale)方法为图片添加灰度效果。

### 开发步骤

1. 在PixelMapManager类中定义handleFilter()方法，通过[effectKit.createEffect()](../harmonyos-references/js-apis-effectkit.md#effectkitcreateeffect)创建filter图像效果对象，通过传入的type值判断调用对应方法添加滤镜效果。

   type为FilterType.GRAYSCALE：调用[grayscale()](../harmonyos-references/js-apis-effectkit.md#grayscale)给图片添加灰度效果。

   ```typescript
   /**
    * Filter type
    */
   export enum FilterType {
     ORIGIN,
     GRAYSCALE,
     BRIGHTNESS,
     INVERT,
     BLUR,
   }
   ```

   ```typescript
   async handleFilter(type: FilterType) {
     // Obtain the cloned baseline pixel image.
     let px: PixelMap = this.getStartEditPixelMap(EditType.FILTER);
     let filter = effectKit.createEffect(px); // Create filter object.

     switch (type) {
       case FilterType.GRAYSCALE:
         px = await filter.grayscale().getEffectPixelMap();
         break;
       // ...
       default:
         break;
     }
     this.notifyPreviewUpdate(px); // Update Preview.
     this.finalEditPixelMap = px; // Save edited pixelMap.
   }
   ```
2. 在点击事件中调用handleFilter()方法，给图片添加滤镜效果，并通过flushPixelMapChange()方法，执行drawImageOnCanvas()重绘图片，显示黑白滤镜效果。

   ```typescript
   ForEach(this.filterData, (item: filterDataType, index) => {
     Column() {
       Image(this.filterThumbnails[index])
         // ...

       Text(item.title)
         // ...
     }
     .margin(2)
     .onClick(async () => {
       await this.pixelMapManager?.handleFilter(index);
       this.editState.currentFilterMode = index;
       this.flushPixelMapChange();
     })
   }, (item: string) => item)
   ```

## 图片高亮滤镜

### 场景描述

选中高亮滤镜，图片显示高亮效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/UrxQYellSJCD7Lg4f-AEug/zh-cn_image_0000002671176350.png "点击放大")

### 实现原理

具体实现原理可参考《基于PixelMap编解码编辑图片开发实践》的图片高亮滤镜[实现原理](bpta-pixelmap-image-editing.md#section93811654111718)。

### 开发步骤

具体开发步骤可参考《基于PixelMap编解码编辑图片开发实践》的图片高亮滤镜[开发步骤](bpta-pixelmap-image-editing.md#section44851932151820)。

## 图片反转滤镜

### 场景描述

选中反转滤镜，图片显示反转效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/LZp5bQJDRp67Wxm3C9qP6Q/zh-cn_image_0000002701095969.png "点击放大")

### 实现原理

具体实现原理可参考《基于PixelMap编解码编辑图片开发实践》的图片反转滤镜[实现原理](bpta-pixelmap-image-editing.md#section13668105616177)。

### 开发步骤

具体开发步骤可参考《基于PixelMap编解码编辑图片开发实践》的图片反转滤镜[开发步骤](bpta-pixelmap-image-editing.md#section762153411810)。

## 图片模糊滤镜

### 场景描述

选中模糊滤镜，图片显示模糊效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/DQ4kzMJ6Rrmt5Uul9K5N3g/zh-cn_image_0000002701056087.png "点击放大")

### 实现原理

具体实现原理可参考《基于PixelMap编解码编辑图片开发实践》的图片模糊滤镜[实现原理](bpta-pixelmap-image-editing.md#section111617598176)。

### 开发步骤

具体开发步骤可参考《基于PixelMap编解码编辑图片开发实践》的图片模糊滤镜[开发步骤](bpta-pixelmap-image-editing.md#section24363011810)。

## 图片水印编辑

### 场景描述

点击水印编辑，在弹窗中输入水印内容为图片添加水印，同时可以调整水印的位置、大小、透明度、旋转角度、选择是否重复等。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/4TxCRTlFR2eOQUw9xyBQDg/zh-cn_image_0000002671336272.gif "点击放大")

### 实现原理

通过[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)将原图绘制到Canvas，利用[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)设置水印字体/透明度/旋转后，通过[fillText()](../harmonyos-references/ts-components-canvas-common-method.md#filltext)绘制水印文字，最后获取合成后的PixelMap更新预览。重复水印则是在Canvas上按照固定间距进行循环绘制。

### 开发步骤

1. 在PixelMapManager类中定义addTextWatermark()方法，用以绘制单条水印：
   1. 通过getImageInfo()获取图片原始尺寸，调用[px2vp()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)将px转为vp。

      ```typescript
      // Obtain the cloned baseline pixel image.
      const px = this.getStartEditPixelMap(EditType.WATER);
      const imageInfo = await px.getImageInfo();
      const size = imageInfo.size;
      const imageWidth = uiContext.px2vp(size?.width);
      const imageHeight = uiContext.px2vp(size?.height);
      ```
   2. 通过[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)创建离屏画，调用[getContext()](../harmonyos-references/ts-components-offscreencanvas.md#getcontext10)创建二维渲染上下文的OffscreenCanvasRenderingContext2D对象，以及通过[drawImage()](../harmonyos-references/ts-components-canvas-common-method.md#drawimage-1)将原图绘制到Canvas上，并设置水印字体、填充色、透明度。

      ```typescript
      // Create offscreenCanvas.
      const offscreenCanvas = new OffscreenCanvas(imageWidth, imageHeight);
      // Get the drawing context of the offscreenCanvas component.
      const offscreenCanvasContext = offscreenCanvas.getContext('2d') as OffscreenCanvasRenderingContext2D;
      // Draw the original image on the canvas.
      offscreenCanvasContext.drawImage(pixelMap, 0, 0, imageWidth, imageHeight);
      // Set watermark text style.
      offscreenCanvasContext.font = `${uiContext.fp2px(config.fontSize)}px sans-serif`;
      offscreenCanvasContext.fillStyle = config.color;
      offscreenCanvasContext.globalAlpha = config.opacity;
      ```
   3. 通过[measureText()](../harmonyos-references/ts-components-canvas-common-method.md#measuretext)测量水印文本尺寸，并调用calculateWatermarkPosition()计算水印位置。

      通过rotation判断水印文字是否有旋转：

      * 有旋转时：保存当前的绘图上下文，移动坐标至水印文字中心，顺时针旋转坐标轴，以水印内容为原点进行绘制，并将保存的绘图上下文进行恢复。
      * 无旋转时：直接通过[fillText()](../harmonyos-references/ts-components-canvas-common-method.md#filltext)进行绘制。

      ```typescript
      // Measure text width and calculate watermark position.
      const textMetrics = offscreenCanvasContext.measureText(config.text);
      const textWidth = textMetrics.width;
      const textHeight = config.fontSize;

      const position = this.calculateWatermarkPosition(imageWidth, imageHeight, textWidth, textHeight, config.position);

      if (config.rotation && config.rotation !== 0) {
        offscreenCanvasContext.save();
        // Translate to the center of rotation.
        offscreenCanvasContext.translate(position.x + textWidth / 2, position.y + textHeight / 2);
        // rotate
        offscreenCanvasContext.rotate((config.rotation * Math.PI) / 180);
        offscreenCanvasContext.fillText(config.text, -textWidth / 2, textHeight / 4);
        offscreenCanvasContext.restore();
      } else {
        // No rotation, draw directly.
        offscreenCanvasContext.fillText(config.text, position.x, position.y + textHeight);
      }
      ```
   4. 通过[getPixelMap()](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)方法从Canvas中获取绘制后的PixelMap后，更新预览，并保存PixelMap。

      ```typescript
      const watermarkedPixelMap = offscreenCanvasContext.getPixelMap(0, 0, imageWidth, imageHeight);
      Logger.info(TAG, 'Watermark added successfully');
      this.notifyPreviewUpdate(watermarkedPixelMap);
      this.finalEditPixelMap = watermarkedPixelMap;
      ```
2. 绘制重复水印时，在addRepeatedWatermark()内通过actualSpacing控制水印内容间距，并通过双层for循环平铺绘制水印。

   ```typescript
   const defaultSpacing: SpacingConfig = { x: 200, y: 150 };
   const actualSpacing = spacing || defaultSpacing;
   // ...
   for (let x = 0; x < imageWidth; x += actualSpacing.x) {
     for (let y = 0; y < imageHeight; y += actualSpacing.y) {
       if (config.rotation && config.rotation !== 0) {
         context.save();
         context.translate(x + textWidth / 2, y + textHeight / 2);
         context.rotate((config.rotation * Math.PI) / 180);
         context.fillText(config.text, -textWidth / 2, textHeight / 4);
         context.restore();
       } else {
         context.fillText(config.text, x, y + textHeight);
       }
     }
   }
   ```
3. 在点击事件中调用addWatermark()方法，定义config水印配置对象，通过判断变量isRepeated调用对应方法，传入config对象及PixelMap。并通过flushPixelMapChange()方法，执行drawImageOnCanvas()将更新后的PixelMap绘制到Canvas，实现图片水印内容的添加。

   ```typescript
   // Add watermark
   private async addWatermark() {
     if (!this.previewPixelMap || this.watermarkText.trim() === '') {
       return;
     }
     try {
       const config: WatermarkConfig = {
         text: this.watermarkText,
         position: this.currentPosition,
         fontSize: this.fontSize,
         color: this.watermarkColor,
         opacity: this.watermarkOpacity,
         rotation: this.rotation
       };

       if (this.isRepeated) {
         // Add duplicate watermark.
         this.pixelMapManager?.addRepeatedWatermark(this.previewPixelMap, config);
       } else {
         // Add single watermark.
         this.pixelMapManager?.addTextWatermark(this.previewPixelMap, config);
       }

       this.flushPixelMapChange();
       this.hasWatermark = true;
     } catch (error) {
       hilog.error(DOMAIN, TAG, '%{public}s, %{public}s', 'Adding watermark failed:', JSON.stringify(error));
     }
   }
   ```

## 示例代码

* [基于PixelMap与Canvas实现图片编辑](https://gitcode.com/HarmonyOS_Samples/image-canvas-edit)
