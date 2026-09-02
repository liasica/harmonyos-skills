---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pixelmap-image-editing
title: 基于PixelMap实现图片编辑
breadcrumb: 最佳实践 > 行业场景解决方案 > 拍摄美化 > 基于PixelMap实现图片编辑
category: best-practices
scraped_at: 2026-09-02T15:03:20+08:00
doc_updated_at: 2026-08-10
content_hash: sha256:2dfcc9e6f7ffeb0616b5f45f7f90368148c8c8f02096b380cc1d336c95cf22cd
---

## 概述

在移动应用开发中，图片编辑功能是用户日常使用的高频场景，例如：相册的图片编辑、社交媒体中对图片的滤镜美化等。

[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)是HarmonyOS中用于表示图像像素数据的核心类。它提供了一种无压缩的位图格式，允许开发者直接读取、写入像素数据，并获取图像信息，是进行图像处理、变换和绘制的基础。本文主要介绍如何使用PixelMap对图片进行编辑处理，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据等。

相关功能场景描述及关键技术点如下表所示：

1. 图片基础编辑功能。

   | 功能描述 | **场景描述** | **关键技术点** |
   | --- | --- | --- |
   | [图片信息展示](bpta-pixelmap-image-editing.md#section1729293110516) | 查看图片元数据，包括图片尺寸、像素格式、HDR属性等信息，帮助用户在编辑图片前了解图片基础属性。 | 通过[getImageInfo()](../harmonyos-references/arkts-apis-image-imagesource.md#getimageinfo-1)获取图片元数据。 |
   | [图片按比例裁剪](bpta-pixelmap-image-editing.md#section13500103313513) | 按比例裁剪图片，适配不同平台要求，例如：头像（1:1）、广告（4:3）、视频封面（16:9）。 | 计算图片裁剪宽高比，通过PixelMap.[crop()](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9-1)裁剪。 |
   | [图片平移](bpta-pixelmap-image-editing.md#section113871741115120) | 沿水平/垂直方向调整图片位置，用于构图微调。 | 计算图片横纵方向偏移量，通过PixelMap.[translate()](../harmonyos-references/arkts-apis-image-pixelmap.md#translate9-1)执行图片在横纵方向上进行平移。 |
   | [图片旋转](bpta-pixelmap-image-editing.md#section990884915118) | 图片逆时针旋转，修正拍摄角度偏差，适配不同显示方向。 | 计算图片旋转角度，调用PixelMap.[rotate()](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9-1)对图片进行旋转。 |
   | [图片镜像翻转](bpta-pixelmap-image-editing.md#section142018561516) | 图片水平翻转，创建对称效果，用于创意设计、制作倒影效果。 | 通过变量控制翻转方向，调用PixelMap.[flipSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#flipsync12)翻转图片。 |
   | [图片等比缩放](bpta-pixelmap-image-editing.md#section15900114135212) | 图片按照80%~120%范围进行缩放，适配不同设备屏幕尺寸。 | 等比缩放比例计算，通过PixelMap.[scale()](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9-1)执行图片缩放。 |
2. 图片调节功能。

   | 功能描述 | **场景描述** | **关键技术点** |
   | --- | --- | --- |
   | [图片亮度调节](bpta-pixelmap-image-editing.md#section3308181519522) | 通过滑块调节图片整体明暗程度，适用于光线不足或过强的图片。 | 像素级RGB数据处理，通过线性缩放算法RGB\_new = RGB \* factor，结合Worker线程异步处理避免卡顿。 |
   | [图片透明度调节](bpta-pixelmap-image-editing.md#section18203523145211) | 通过滑块调节图片透明度，创建半透明叠加效果，用于UI遮罩或背景虚化。 | 通过PixelMap.[opacity()](../harmonyos-references/arkts-apis-image-pixelmap.md#opacity9-1)接口，直接修改Alpha通道。 |
   | [图片饱和度调节](bpta-pixelmap-image-editing.md#section8695327165213) | 通过滑块调节图片饱和度，增强或降低色彩鲜艳程度，实现图片艺术风格调整。 | 像素级RGB数据处理，通过亮度公式结合饱和度算法，并结合Worker线程异步处理。 |
   | [图片滤镜添加](bpta-pixelmap-image-editing.md#section2124103385214) | 为图片添加预置滤镜效果，用于图片艺术创作、风格化处理。 | 通过[effectKit.createEffect()](../harmonyos-references/js-apis-effectkit.md#effectkitcreateeffect)创建filter图像效果对象，并结合对应接口实现滤镜效果添加。 |

## 图片信息展示

### 场景描述

获取图片信息展示在页面中。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/uJnJbkxyT3eqLzdtLryt3g/zh-cn_image_0000002701095653.png "点击放大")

### 实现原理

通过ImageSource的[getImageInfo()](../harmonyos-references/arkts-apis-image-imagesource.md#getimageinfo-1)方法获取图片大小、像素格式、色彩空间、透明度、图片格式、是否为HDR等信息，并结合基础组件将图片信息展示在页面中。

### 开发步骤

1. 通过[image.createImageSource()](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource)创建ImageSource实例，并调用[getImageInfo()](../harmonyos-references/arkts-apis-image-imagesource.md#getimageinfo-1)方法获取图片信息。

   ```typescript
   this.imageSource = await createImageSourceFromResource(this.getUIContext());
   // ...
   this.imageSource.getImageInfo((err, imageInfo) => {
     if (err) {
       Logger.error(`Failed to get image info: code = ${err?.code}, message = ${err?.message}`);
       return;
     }
     Object.keys(imageInfo).forEach((key) => {
       if (key === 'size') {
         Object.keys(imageInfo[key]).forEach((chlKey) => {
           this.imageInfoArr.push({
             label: chlKey,
             value: imageInfo[key][chlKey]
           });
         });
       } else {
         this.imageInfoArr.push({
           label: key,
           value: imageInfo[key]
         })
       }
     });
   });
   ```
2. 展示图片信息。

   ```typescript
   List() {
     ForEach(this.imageInfoArr, (item: ImageInfoItem) => {
       ListItem() {
         Row() {
           Text(item.label)
             // ...
           Text(item.value + '')
             // ...
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.SpaceBetween)
         .padding({ left: 12, right: 12 })
       }
       .width('100%')
       .height(48)
     }, (item: ImageInfoItem) => item.label)
   }
   .divider({
     strokeWidth: 0.5,
     color: 'rgba(0,0,0,0.2)',
     startMargin: 12,
     endMargin: 12
   })
   // ...
   ```

## 图片按比例裁剪

### 场景描述

在编辑图片时，将图片按照1:1、4:3或16:9进行裁剪。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Q5n36TBoRU6MjxQvl3R8Ag/zh-cn_image_0000002701055737.gif "点击放大")

### 实现原理

通过[crop()](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9-1)方法，根据输入的尺寸对图片进行裁剪。

**说明** 

图片裁剪尺寸取值范围不能超过图片的宽高。

### 开发步骤

1. 自定义square()方法，按照1:1进行裁剪：
   * width < height（竖图）：裁剪宽高均为图片原始宽度；x = 0，y垂直居中。
   * width >= height（横图/正方形图片）：裁剪宽高均为图片原始高度；x水平居中，y = 0。

   ```typescript
   /**
    * Crop image to 1:1 square ratio. The crop region is centered.
    *
    * @param pixelMap - The image to crop.
    * @param width - Original image width.
    * @param height - Original image height.
    */
   export async function square(pixelMap: PixelMap, width: number, height: number) {
     try {
       if (width < height) {
         await pixelMap.crop({
           size: {
             width: width,
             height: width
           },
           x: 0,
           y: Math.round((height - width) / CommonConstants.AVERAGE_WEIGHT_WIDTH)
         });
       } else {
         await pixelMap.crop({
           size: {
             width: height,
             height: height
           },
           x: Math.round((width - height) / CommonConstants.AVERAGE_WEIGHT_WIDTH),
           y: 0
         });
       }
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `square crop failed: ${error.code}, ${error.message}`);
     }
   }
   ```
2. 自定义banner()方法，按照4:3进行裁剪：
   1. width <= height（竖图）：裁剪宽度 = 图片宽度；裁剪高度 = width \* 3/4；x = 0，y垂直居中。
   2. width > height，且width \* 3/4 >= height（横图但高度较小）：裁剪高度 = 图片高度；裁剪宽度 = height / (3/4)；y = 0，x水平居中。
   3. width > height，但width \* 3/4 < height（横图但高度偏大）：同情况a，以图片宽度为基准进行裁剪。
   4. 调用cropCommon()方法，执行pixelMap.crop()完成图片裁剪。

   ```typescript
   export async function cropCommon(pixelMap: PixelMap, cropWidth: number, cropHeight: number, cropPosition: RegionItem) {
     try {
       await pixelMap.crop({
         size: {
           width: cropWidth,
           height: cropHeight
         },
         x: cropPosition.x,
         y: cropPosition.y
       });
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `cropCommon failed: ${error.code}, ${error.message}`);
     }
   }
   ```

   ```typescript
   /**
    * Crop image to 4:3 ratio. The crop region is centered.
    *
    * @param pixelMap - The image to crop.
    * @param width - Original image width.
    * @param height - Original image height.
    */
   export async function banner(pixelMap: PixelMap, width: number, height: number) {
     if (width <= height) {
       const cropWidth = width;
       const cropHeight = Math.floor(width * CommonConstants.CROP_RATE_4_3);
       const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / CommonConstants.AVERAGE_WEIGHT_WIDTH));
       await cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
       return;
     }
     if (width * CommonConstants.CROP_RATE_4_3 >= height) {
       const cropWidth = Math.floor(height / CommonConstants.CROP_RATE_4_3);
       const cropHeight = height;
       const cropPosition = new RegionItem(Math.floor((width - cropWidth) / CommonConstants.AVERAGE_WEIGHT_WIDTH), 0);
       await cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
       return;
     }

     const cropWidth = width;
     const cropHeight = Math.floor(width * CommonConstants.CROP_RATE_4_3);
     const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / CommonConstants.AVERAGE_WEIGHT_WIDTH));
     await cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
   }
   ```
3. 自定义rectangle()方法，按照16:9进行裁剪，实现方式同4:3。

   ```typescript
   /**
    * Crop image to 16:9 ratio. The crop region is centered.
    *
    * @param pixelMap - The image to crop.
    * @param width - Original image width.
    * @param height - Original image height.
    */
   export async function rectangle(pixelMap: PixelMap, width: number, height: number) {
     if (width <= height) {
       const cropWidth = width;
       const cropHeight = Math.floor(width * (CommonConstants.CROP_RATE_9_16));
       const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / CommonConstants.AVERAGE_WEIGHT_WIDTH));
       await cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
       return;
     }
     if (width * (CommonConstants.CROP_RATE_9_16) >= height) {
       const cropWidth = Math.floor(height / (CommonConstants.CROP_RATE_9_16));
       const cropHeight = height;
       const cropPosition = new RegionItem(Math.floor((width - cropWidth) / CommonConstants.AVERAGE_WEIGHT_WIDTH), 0);
       await cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
       return;
     }

     const cropWidth = width;
     const cropHeight = Math.floor(width * (CommonConstants.CROP_RATE_9_16));
     const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / CommonConstants.AVERAGE_WEIGHT_WIDTH));
     await cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
   }
   ```

## 图片平移

### 场景描述

通过滑动Slider，在横向/纵向调节图片位置。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Lxb4bsKiQzG2L7030OFxcw/zh-cn_image_0000002671335926.gif "点击放大")

### 实现原理

通过[translate()](../harmonyos-references/arkts-apis-image-pixelmap.md#translate9-1)方法，根据输入的坐标对图片进行位置变换。

### 开发步骤

1. 在Slider的onChange()事件中，传入Slider进度值及状态。

   ```typescript
   TabContent() {
     TranslateView({
       onTranslateChange: (value: number, mode: SliderChangeMode) => {
         this.editController?.handleTranslateChange(value, mode);
       }
     })
   }
   ```

   ```typescript
   Slider({
     value: this.editState.currentTranslateData[this.editState.currentTranslateMode],
     step: 1,
     min: 0,
     max: 1000,
     // ...
   })
     // ...
     .onChange((value: number, mode: SliderChangeMode) => {
       if (this.onTranslateChange !== undefined) {
         this.onTranslateChange(value > 1000 ? 1000 : value, mode);
       }
     })
   ```
2. 在滑动结束时且值有变化时，计算偏移量moveValue，并更新状态。再根据平移方向（currentTranslateMode为0时为水平平移，否则为垂直平移），调用translateImage()传入偏移量moveValue执行平移。

   ```typescript
   async handleTranslateChange(value: number, mode: SliderChangeMode): Promise<void> {
     if (mode === SliderChangeMode.End &&
       value !== this.editState.currentTranslateData[this.editState.currentTranslateMode]) {
       const moveValue: number =
         Math.round(value) - this.editState.currentTranslateData[this.editState.currentTranslateMode];
       this.editState.updateTranslateData(this.editState.currentTranslateMode, Math.round(value));
       if (this.editState.currentTranslateMode === 0) {
         // horizontal translation.
         await this.pixelMapManager.translateImage({ x: moveValue, y: 0 });
       } else {
         // vertical translation.
         await this.pixelMapManager.translateImage({ x: 0, y: moveValue });
       }
     }
   }
   ```
3. 在getStartEditPixelMap()中，根据编辑模式通过[cloneSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#clonesync18)拷贝PixelMap对象并返回。
   1. 基于PixelMap起点：适用类型包括图片的裁剪、调节（亮度/透明度/饱和度）、滤镜（黑白/高亮/翻转/模糊等）、缩放，基于同一起点重新计算PixelMap。例如：图片亮度从50%调整至80%，均从原图计算。
   2. 基于PixelMap结果：适用类型包括图片的旋转、镜像、平移，基于上次编辑结果进行累加。例如：图片从90°旋转至180°，基于上次旋转后的结果再次旋转。

   ```typescript
   getStartEditPixelMap(mode: EditType): PixelMap | undefined {
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
       default:
         target = this.finalEditPixelMap;
         break;
     }
     if (target !== null && target !== undefined) {
       return this.clonePixelMap(target);
     }
     return undefined;
   }
   ```

   ```typescript
   // Copy the current Pixelmap object.
   clonePixelMap(pixelMap: PixelMap): PixelMap {
     try {
       return pixelMap.cloneSync();
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `${error.code}, ${error.message}`);
       return pixelMap;
     }
   }
   ```
4. 在translateImage()方法中获取PixelMap，调用[translate()](../harmonyos-references/arkts-apis-image-pixelmap.md#translate9-1)方法对图片进行横向/纵向平移，并保存平移结果，将编辑后的PixelMap传入notifyPreviewUpdate()，通知页面更新预览图片，实现图片在横向/纵向上位置的变换。

   ```typescript
   async translateImage(moveValue: TranslateValue) {
     const px = this.getStartEditPixelMap(EditType.TRANSLATION);
     if (px === null || px === undefined) {
       return;
     }
     try {
       await px.translate(moveValue.x, moveValue.y); // Perform image offset.
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `translate failed: ${error.code}, ${error.message}`);
     }
     this.finalEditPixelMap = px; // Save the edited PixelMap.
     try {
       this.notifyPreviewUpdate(px); // Update Preview.
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `${error.code}, ${error.message}`);
     }
   }
   ```

## 图片旋转

### 场景描述

单击图片旋转按钮，改变图片显示方向。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/27WI3qYfQ3umPRJMJ_6PHA/zh-cn_image_0000002671176072.gif "点击放大")

### 实现原理

通过[rotate()](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9-1)方法，根据输入的角度对图片进行旋转。

### 开发步骤

1. 单击图片旋转图标时，调用rotateImage()方法更新图片旋转角度：旋转角度 = (当前角度 - 90 + 360) % 360，使图片每次逆时针旋转90°。

   ```typescript
   rotateImage(): void {
     this.editState.rotationAngle = (this.editState.rotationAngle - 90 + 360) % 360;
     this.pixelMapManager.cropImage(this.editState.currentCropMode, this.editState.rotationAngle,
       this.editState.isMirrored);
   }
   ```
2. 在cropImage()方法中，调用applyTransforms()执行[rotate()](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9-1)方法传入旋转角度对图片进行旋转，并更新预览图片。

   ```typescript
   async cropImage(proportion: CropType, rotationAngle: number, isMirrored: boolean) {
     // ...

     await this.applyTransforms(px, rotationAngle, isMirrored);
     this.finalEditPixelMap = px;
     this.notifyPreviewUpdate(px);
   }
   ```

   ```typescript
   private async applyTransforms(px: PixelMap, rotationAngle: number, isMirrored: boolean): Promise<void> {
     if (rotationAngle !== 0) {
       try {
         await px.rotate(rotationAngle);
       } catch (error) {
         Logger.error(TAG, `there is a error in rotate process with ${error?.code}`);
       }
     }
     // ...
   }
   ```

## 图片镜像翻转

### 场景描述

单击镜像翻转图标，使图片进行水平翻转。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/WWpelVcGQY-FKNYIeVOcYg/zh-cn_image_0000002701095655.gif "点击放大")

### 实现原理

通过[flipSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#flipsync12)方法，根据输入的条件对图片进行翻转：

* horizontal：true表示进行水平翻转；false表示不进行水平翻转。
* vertical：true表示进行垂直翻转；false表示不进行垂直翻转。

### 开发步骤

1. 单击图片翻转图标时，调用mirrorImage()方法修改图片翻转状态。

   ```screen
   mirrorImage(): void {
     this.editState.isMirrored = !this.editState.isMirrored;
     this.pixelMapManager.cropImage(this.editState.currentCropMode, this.editState.rotationAngle,
       this.editState.isMirrored);
   }
   ```
2. 在cropImage()方法中，调用applyTransforms()执行[flipSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#flipsync12)方法传入(true, false)水平翻转，并重新渲染图片。

   ```typescript
   async cropImage(proportion: CropType, rotationAngle: number, isMirrored: boolean) {
     if (this.originCropPixelMap !== null && this.originCropPixelMap !== undefined) {
       // ...

       await this.applyTransforms(px, rotationAngle, isMirrored);
       this.finalEditPixelMap = px;
       this.notifyPreviewUpdate(px);
     }
   }
   ```

   ```typescript
   private async applyTransforms(px: PixelMap, rotationAngle: number, isMirrored: boolean): Promise<void> {
     // ...
     if (isMirrored) {
       try {
         px.flipSync(true, false);
       } catch (error) {
         Logger.error(TAG, `there is a error in mirror process with ${error?.code}`);
       }
     }
   }
   ```

## 图片等比缩放

### 场景描述

滑动Slider，图片按照比例进行缩小或放大。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/bLS2dIeXQg-hANVeOq5sLQ/zh-cn_image_0000002701055781.gif "点击放大")

### 实现原理

通过[scale()](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9-1)方法，根据输入宽高的缩放倍数对图片进行缩放。

### 开发步骤

1. 滑动Slider时，调用handleZoomChange()方法，在滑动结束时且值发生变化后，将value除以100作为缩放系数传入editImageScale()中。

   ```typescript
   async handleZoomChange(value: number, mode: SliderChangeMode): Promise<void> {
     if (mode === SliderChangeMode.End && value !== this.editState.currentZoom) {
       await this.pixelMapManager.editImageScale(value / 100);
       this.editState.currentZoom = value;
     }
   }
   ```
2. 执行[scale()](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9-1)方法对图片进行缩小/放大，并更新预览图片。

   ```typescript
   async editImageScale(scale: number) {
     const px = this.getStartEditPixelMap(EditType.SCALE);
     if (px === null || px === undefined) {
       return;
     }
     try {
       await px.scale(scale, scale);
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `${error.code}, ${error.message}`);
     }
     this.finalEditPixelMap = px;
     this.notifyPreviewUpdate(px);
   }
   ```

## 图片亮度调节

### 场景描述

滑动Slider，调节图片显示亮度。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/hvug5MO6RpKrDC_JKhOWFA/zh-cn_image_0000002671335972.gif "点击放大")

### 实现原理

通过线性缩放每个像素的RGB分量来改变图像的整体明暗程度。

对应公式：

R\_new = R\_original \* factor

G\_new = G\_original \* factor

B\_new = B\_original \* factor

factor = 当前调节值 / 100

原理说明：

* 当factor > 1时，RGB值增大，图像变亮。
* 当factor < 1时，RGB值减小，图像变暗。
* 当factor = 1时，保持原始亮度。

### 开发步骤

1. 定义adjustBrightness()方法计算亮度值，结合Math.max(0, Math.min(255, Math.round(...)))确保RGB值在0~255范围内。

   ```typescript
   function adjustBrightness(pixelData: Uint8ClampedArray, adjustedData: Uint8ClampedArray, i: number,
     factor: number): void {
     const r = pixelData[i] * factor;
     const g = pixelData[i + 1] * factor;
     const b = pixelData[i + 2] * factor;

     adjustedData[i] = Math.max(0, Math.min(255, Math.round(r)));
     adjustedData[i + 1] = Math.max(0, Math.min(255, Math.round(g)));
     adjustedData[i + 2] = Math.max(0, Math.min(255, Math.round(b)));
   }
   ```
2. 定义execColorInfo()函数，遍历图片像素，根据调节类型调用adjustBrightness()计算亮度值。

   ```typescript
   export function execColorInfo(bufferArray: ArrayBuffer, last: number, cur: number, hsvIndex: number) {
     // ...

     try {
       const pixelData = new Uint8ClampedArray(bufferArray);
       const adjustedData = new Uint8ClampedArray(pixelData.length);
       const bytesPerPixel = 4;
       const factor = cur / 100;
       for (let i = 0; i < pixelData.length; i += bytesPerPixel) {
         adjustedData[i + 3] = pixelData[i + 3];

         if (pixelData[i + 3] < 1) {
           continue;
         }
         if (hsvIndex === AdjustType.BRIGHTNESS) {
           adjustBrightness(pixelData, adjustedData, i, factor);
         }
         // ...
       }
       return adjustedData.buffer;
     } catch (error) {
       Logger.error(TAG, `Failed to set adjustedData: code = ${error?.code}, message = ${error?.message}`);
       return null;
     }
   }
   ```
3. 在Worker线程中处理像素操作，返回处理后的buffer。

   ```typescript
   workerPort.onmessage = (event: MessageEvents) => {
     // ...
     let bufferArray: ArrayBuffer = data.buf;
     let last: number = data.last;
     let cur: number = data.cur;
     let adjustType: AdjustType = data.adjustType;
     let buffer = execColorInfo(bufferArray, last, cur, adjustType);
     try {
       // Return the processed buffer.
       workerPort.postMessage(buffer);
     } catch (error) {
       Logger.error(TAG, `post message error: code = ${error?.code}, message = ${error?.message}`);
     }
   };
   ```
4. 在PixelMapManager类中：
   * 定义processAdjustWorker()方法，获取像素buffer发送至Worker子线程，实现Worker通信。

     ```typescript
     private async processAdjustWorker(value: number, buffer: ArrayBuffer, adjustType: AdjustType): Promise<ArrayBuffer> {
       await this.adjustLock;

       return new Promise((resolve) => {
         this.adjustLock = new Promise<void>((release) => {
           const message = new MessageItem(buffer, CommonConstants.SLIDER_MAX, value, adjustType);
           try {
             this.adjustWorker.postMessage(message);
           } catch (error) {
             Logger.error(TAG, `postMessage failed, code is ${error.code}, message is ${error.message}`);
             release();
           }
           this.adjustWorker.onmessage = (event: MessageEvents) => {
             resolve(event.data);
             release();
           };
         });
       });
     }
     ```
   * 定义adjustImage()方法，调用processAdjustWorker()并传入当前亮度滑块值、像素buffer、调节类型（亮度），将处理后的buffer写回PixelMap。

     ```typescript
     async adjustImage(currentAdjustData: number[]) {
       // Obtain the cloned baseline pixel image.
       const px = this.getStartEditPixelMap(EditType.ADJUST);
       if (px === null || px === undefined) {
         return;
       }
       let buffer = new ArrayBuffer(px.getPixelBytesNumber());
       await px.readPixelsToBuffer(buffer).catch((err: BusinessError) => {
         Logger.error(TAG, `readPixelsToBuffer failed: ${err.code}, ${err.message}`);
       });
       if (!buffer) {
         return;
       }
       if (currentAdjustData[AdjustType.BRIGHTNESS] !== CommonConstants.SLIDER_MAX) {
         buffer = await this.processAdjustWorker(
           currentAdjustData[AdjustType.BRIGHTNESS],
           buffer,
           AdjustType.BRIGHTNESS
         );
         try {
           px.writeBufferToPixelsSync(buffer); // Write the processed buffer back to Pixelmap.
         } catch (err) {
           let error = err as BusinessError;
           Logger.error(TAG, `${error.code}, ${error.message}`);
         }
       }
       // ...
       this.finalEditPixelMap = px; // Save edited pixelMap.
       this.notifyPreviewUpdate(px); // Update Preview.
     }
     ```
5. 定义sliderChange()方法并执行adjustImage()。在Slider组件的onChange()事件中调用sliderChange()，当离手时触发，避免频繁计算，实现亮度调节。

   ```typescript
   async sliderChange(value: number, mode: SliderChangeMode) {
     if ((mode === SliderChangeMode.End) && (value !== this.editState.currentAdjustData[this.currentAdjustType])) {
       const roundedValue = Math.round(value);
       this.editState.currentAdjustData[this.currentAdjustType] = roundedValue;
       this.paramValues[this.currentAdjustType] = roundedValue;
       this.deviceListDialogController.open();
       try {
         await this.pixelMapManager?.adjustImage(this.paramValues);
       } catch (err) {
         let error = err as BusinessError;
         Logger.error('SliderCustom', `adjustImage failed: code = ${error?.code}, message = ${error?.message}`);
       } finally {
         this.deviceListDialogController.close();
       }
     }
   }
   ```

   ```typescript
   Slider({
     value: this.editState.currentAdjustData[this.currentAdjustType],
     step: CommonConstants.SLIDER_STEP,
     min: this.min,
     max: this.max,
     // ...
   })
     // ...
     .onChange((value: number, mode: SliderChangeMode) => {
       this.sliderChange(value > this.max ? this.max : value, mode);
     })
   ```

## 图片透明度调节

### 场景描述

滑动Slider，调节图片透明度。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/F-WiJzumTPaz9vscuBc4Bw/zh-cn_image_0000002671176144.gif "点击放大")

### 实现原理

通过[opacity()](../harmonyos-references/arkts-apis-image-pixelmap.md#opacity9-1)设置PixelMap的透明度。透明度值通过滑块值归一化得到：opacity = sliderValue / 100。

### 开发步骤

1. 通过PixelMap的[opacity()](../harmonyos-references/arkts-apis-image-pixelmap.md#opacity9-1)方法实现透明度调节，并更新预览。

   ```typescript
   async adjustImage(currentAdjustData: number[]) {
     // Obtain the cloned baseline pixel image.
     const px = this.getStartEditPixelMap(EditType.ADJUST);
     if (px === null || px === undefined) {
       return;
     }
     let buffer = new ArrayBuffer(px.getPixelBytesNumber());
     await px.readPixelsToBuffer(buffer).catch((err: BusinessError) => {
       Logger.error(TAG, `readPixelsToBuffer failed: ${err.code}, ${err.message}`);
     });
     if (!buffer) {
       return;
     }
     // ...
     if (currentAdjustData[AdjustType.OPACITY] !== CommonConstants.SLIDER_MAX) {
       const opacity = currentAdjustData[AdjustType.OPACITY] / CommonConstants.SLIDER_MAX;
       try {
         await px.opacity(opacity).catch((err: BusinessError) => {
           Logger.error(TAG, `opacity failed: ${err.code}, ${err.message}`);
         });
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `${error.code}, ${error.message}`);
       }
     }
     this.finalEditPixelMap = px; // Save edited pixelMap.
     this.notifyPreviewUpdate(px); // Update Preview.
   }
   ```
2. 在Slider组件的onChange()事件中调用sliderChange()，实现透明度调节，参考：图片亮度调节[开发步骤](bpta-pixelmap-image-editing.md#li73171351133011)。

## 图片饱和度调节

### 场景描述

滑动Slider，调节图片饱和度。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/zDiQ4eaVRGKxD1GZeb6YKA/zh-cn_image_0000002701095731.gif "点击放大")

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

1. 定义adjustSaturation()方法，计算图片饱和度。将RGB值除以255归一化到[0, 1]区间进行计算。使用标准亮度公式，对亮度进行计算，将计算结果乘以255并四舍五入转回0~255范围内。

   ```typescript
   function adjustSaturation(pixelData: Uint8ClampedArray, adjustedData: Uint8ClampedArray, i: number,
     factor: number): void {
     const r = pixelData[i] / 255;
     const g = pixelData[i + 1] / 255;
     const b = pixelData[i + 2] / 255;

     const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;

     const adjustedR = luminance + (r - luminance) * factor;
     const adjustedG = luminance + (g - luminance) * factor;
     const adjustedB = luminance + (b - luminance) * factor;

     adjustedData[i] = Math.max(0, Math.min(255, Math.round(adjustedR * 255)));
     adjustedData[i + 1] = Math.max(0, Math.min(255, Math.round(adjustedG * 255)));
     adjustedData[i + 2] = Math.max(0, Math.min(255, Math.round(adjustedB * 255)));
   }
   ```
2. 在execColorInfo()中，根据调节类型调用adjustSaturation()计算图片饱和度。

   ```typescript
   export function execColorInfo(bufferArray: ArrayBuffer, last: number, cur: number, hsvIndex: number) {
     // ...

     try {
       const pixelData = new Uint8ClampedArray(bufferArray);
       const adjustedData = new Uint8ClampedArray(pixelData.length);
       const bytesPerPixel = 4;
       const factor = cur / 100;
       for (let i = 0; i < pixelData.length; i += bytesPerPixel) {
         adjustedData[i + 3] = pixelData[i + 3];

         if (pixelData[i + 3] < 1) {
           continue;
         }
         // ...
         if (hsvIndex === AdjustType.SATURATION) {
           adjustSaturation(pixelData, adjustedData, i, factor);
         }
       }
       return adjustedData.buffer;
     } catch (error) {
       Logger.error(TAG, `Failed to set adjustedData: code = ${error?.code}, message = ${error?.message}`);
       return null;
     }
   }
   ```
3. Worker线程处理及Worker通信，参考：图片亮度调节[开发步骤](bpta-pixelmap-image-editing.md#li7523135152515)。
4. 在adjustImage()方法中，获取PixelMap的像素数据到Buffer，调用处理图片饱和度，并更新预览图像。

   ```typescript
   async adjustImage(currentAdjustData: number[]) {
     // Obtain the cloned baseline pixel image.
     const px = this.getStartEditPixelMap(EditType.ADJUST);
     if (px === null || px === undefined) {
       return;
     }
     let buffer = new ArrayBuffer(px.getPixelBytesNumber());
     await px.readPixelsToBuffer(buffer).catch((err: BusinessError) => {
       Logger.error(TAG, `readPixelsToBuffer failed: ${err.code}, ${err.message}`);
     });
     if (!buffer) {
       return;
     }
     // ...
     if (currentAdjustData[AdjustType.SATURATION] !== CommonConstants.SLIDER_MAX) {
       try {
         buffer = await this.processAdjustWorker(
           currentAdjustData[AdjustType.SATURATION],
           buffer,
           AdjustType.SATURATION
         );
         // Write the processed buffer back to Pixelmap.
         px.writeBufferToPixelsSync(buffer);
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `${error.code}, ${error.message}`);
       }
     }
     // ...
     this.finalEditPixelMap = px; // Save edited pixelMap.
     this.notifyPreviewUpdate(px); // Update Preview.
   }
   ```
5. 在Slider组件的onChange()事件中调用sliderChange()，实现图片饱和度调节，参考：图片亮度调节[开发步骤](bpta-pixelmap-image-editing.md#section2758132011188)中的步骤5。

## 图片黑白滤镜

### 场景描述

选中黑白滤镜，图片显示黑白效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/7DTqUSYmSEKwaF-pHeyalQ/zh-cn_image_0000002701055811.png "点击放大")

### 实现原理

通过[effectKit.createEffect()](../harmonyos-references/js-apis-effectkit.md#effectkitcreateeffect)创建滤镜效果器，调用[grayscale()](../harmonyos-references/js-apis-effectkit.md#grayscale)方法为图片添加灰度效果。

### 开发步骤

1. 获取编辑用的PixelMap，通过[effectKit.createEffect()](../harmonyos-references/js-apis-effectkit.md#effectkitcreateeffect)创建filter图像效果对象，根据传入的滤镜类型应用对应效果。

   当type为FilterType.GRAYSCALE时，调用[grayscale()](../harmonyos-references/js-apis-effectkit.md#grayscale)给图片添加灰度效果，通过getEffectPixelMap()获取处理后的PixelMap，再通过notifyPreviewUpdate()方法更新预览。

   ```typescript
   async handleFilter(type: FilterType) {
     // Obtain the cloned baseline pixel image.
     let startMap = this.getStartEditPixelMap(EditType.FILTER);
     if (startMap === null || startMap === undefined) {
       return;
     }
     let px: PixelMap = startMap;
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
2. 在点击事件中调用handleFilter()并传入当前点击item的索引，应用黑白滤镜效果。

   ```typescript
   ForEach(this.filterData, (item: filterDataType, index: number) => {
     Flex({
       direction: this.currentBreakpoint === 'lg' ? FlexDirection.Row : FlexDirection.Column,
       alignItems: ItemAlign.Center
     }) {
       Image(this.filterThumbnails[index])
         // ...

       Text(item.title)
         // ...
     }
     // ...
     .onClick(() => {
       this.pixelMapManager?.handleFilter(index);
       this.editState.currentFilterMode = index;
     })
   }, (item: filterDataType) => item.key)
   ```

## 图片高亮滤镜

### 场景描述

选中高亮滤镜，图片显示高亮效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/dPMaL9LDT_29nc8LI50pTw/zh-cn_image_0000002671336002.png "点击放大")

### 实现原理

通过effectKit效果器，调用[brightness()](../harmonyos-references/js-apis-effectkit.md#brightness)方法为图片添加高亮效果。

### 开发步骤

1. 当type为FilterType.BRIGHTNESS时，调用[brightness()](../harmonyos-references/js-apis-effectkit.md#brightness)给图片添加高亮效果，再获取处理后的PixelMap，并更新预览图片。

   ```typescript
   async handleFilter(type: FilterType) {
     // Obtain the cloned baseline pixel image.
     let startMap = this.getStartEditPixelMap(EditType.FILTER);
     if (startMap === null || startMap === undefined) {
       return;
     }
     let px: PixelMap = startMap;
     let filter = effectKit.createEffect(px); // Create filter object.

     switch (type) {
       // ...
       case FilterType.BRIGHTNESS:
         px = await filter.brightness(0.7).getEffectPixelMap();
         break;
       // ...
       default:
         break;
     }
     this.notifyPreviewUpdate(px); // Update Preview.
     this.finalEditPixelMap = px; // Save edited pixelMap.
   }
   ```
2. 在点击事件中调用handleFilter()并传入当前点击item的索引，应用高亮滤镜效果，参考黑白滤镜[开发步骤](bpta-pixelmap-image-editing.md#section07091429161817)中的步骤2。

## 图片反转滤镜

### 场景描述

选中反转滤镜，图片显示反转效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/lWCCHWYhTB2SdfLGcWHKNw/zh-cn_image_0000002671176146.png "点击放大")

### 实现原理

通过effectKit效果器，调用[invert()](../harmonyos-references/js-apis-effectkit.md#invert12)方法为图片添加反转效果。

### 开发步骤

1. 当type为FilterType.INVERT时，调用[invert()](../harmonyos-references/js-apis-effectkit.md#invert12)给图片添加反转效果，再获取处理后的PixelMap，并重新渲染图片。

   ```typescript
   async handleFilter(type: FilterType) {
     // Obtain the cloned baseline pixel image.
     let startMap = this.getStartEditPixelMap(EditType.FILTER);
     if (startMap === null || startMap === undefined) {
       return;
     }
     let px: PixelMap = startMap;
     let filter = effectKit.createEffect(px); // Create filter object.

     switch (type) {
       // ...
       case FilterType.INVERT:
         px = await filter.invert().getEffectPixelMap();
         break;
       // ...
       default:
         break;
     }
     this.notifyPreviewUpdate(px); // Update Preview.
     this.finalEditPixelMap = px; // Save edited pixelMap.
   }
   ```
2. 在点击事件中调用handleFilter()并传入当前点击item的索引，应用反转滤镜效果，参考黑白滤镜[开发步骤](bpta-pixelmap-image-editing.md#section07091429161817)中的步骤2。

## 图片模糊滤镜

### 场景描述

选中模糊滤镜，图片显示模糊效果。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/HHZRnBDDSueBxKizJd7Eyw/zh-cn_image_0000002701095733.png "点击放大")

### 实现原理

通过effectKit效果器，调用[blur()](../harmonyos-references/js-apis-effectkit.md#blur)方法为图片添加模糊效果。

### 开发步骤

1. 当type为FilterType.BLUR时，调用[blur()](../harmonyos-references/js-apis-effectkit.md#blur)给图片添加模糊效果，再获取处理后的PixelMap，并重新渲染图片。

   ```typescript
   async handleFilter(type: FilterType) {
     // Obtain the cloned baseline pixel image.
     let startMap = this.getStartEditPixelMap(EditType.FILTER);
     if (startMap === null || startMap === undefined) {
       return;
     }
     let px: PixelMap = startMap;
     let filter = effectKit.createEffect(px); // Create filter object.

     switch (type) {
       // ...
       case FilterType.BLUR:
         px = await filter.blur(5).getEffectPixelMap();
         break;
       default:
         break;
     }
     this.notifyPreviewUpdate(px); // Update Preview.
     this.finalEditPixelMap = px; // Save edited pixelMap.
   }
   ```
2. 在点击事件中调用handleFilter()并传入当前点击item的索引，应用模糊滤镜效果，参考黑白滤镜[开发步骤](bpta-pixelmap-image-editing.md#section07091429161817)中的步骤2。

## 示例代码

* [基于PixelMap编解码图片编辑功能](https://gitcode.com/HarmonyOS_Samples/PixelMapImageEdit)
