---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preview-glitch-solution
title: 相机预览花屏解决方案
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机预览花屏解决方案
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:49+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:8c79dfe1c9be5655dcd55df49ab42818ae01174dca531ad72bc400cb9725fcbc
---

## 概述

开发者在[使用相机服务](camera-kit.md)时，如果仅用于预览流展示，通常使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件实现，如果需要获取每帧图像做二次处理(例如获取每帧图像完成二维码识别或人脸识别场景)，可以通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)中imageArrival事件监听预览流每帧数据，解析图像内容。在解析图像内容时，如果未考虑stride，直接通过使用width\*height读取图像内容去解析图像，会导致相机预览异常，从而出现相机预览花屏的现象。

当开发者获取预览流每帧图像buffer后，若发现图片内容出现花屏堆叠状，出现相机预览花屏现象，此时需要排查解析每帧图像，当预览流图像stride与width不一致时，需要对stride进行无效像素的去除处理。

## 实现原理

在计算机图形学和图像处理中，stride通常指的是在内存中存储多维数组（如图像或纹理）时，行与行之间的字节间隔，即每一行的起始地址与下一行的起始地址之间的距离，在本文中stride指的是图像的一行数据在内存中实际占用的字节数，出于内存对齐和提高读取效率的考虑，通常大于图像的宽度。

**说明** 

stride在不同的平台底层上报的值不同，开发者需根据实际业务获取stride后做处理适配。在本文中通过预览流帧数据的返回值image.Component.rowStride获取stride。

如下图：在一个width为3，height为3，stride为4的图片上（例如定义了一个480\*480分辨率的图像），实际分配内存并不是width\*height即3\*3（此处为定义的预览流分辨率的宽高比，即实际分配内存不是480\*480），而是stride\*height即4\*3，这样实现了内存对齐，方便硬件处理。

**图 1** 需正确处理stride

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/4dcosi_QSJKPcePGx-9dcg/zh-cn_image_0000002742123707.png)

如果开发者根据width和height数据去处理像素数据，即把0x00-0x09地址的数据当做像素去处理，就会出现解析了错误的像素数据的问题，并且使用了无效的像素0x03，0x07，会导致图片无法正常显示导致“相机花屏”现象。因此，要根据stride值处理预览数据流，去除无效的像素后送显，才能获取正确的预览流图像。

## 场景案例

以一种高频的用户使用场景为例，应用需要定义一个1080\*1080分辨率的预览流图像，此时的stride在相关平台的返回值为1088，此时需要对stride进行处理，处理无效像素后解析出正确的像素数据，避免出现预览流花屏。

【反例】未处理stride：当开发者创建PixelMap解析buffer时，直接按照宽去读取每行数据，没有处理stride，此时若解析了无效像素数据并传给Image组件直接送显，可能会出现预览流花屏现象。

以下为部分示例代码：

1. 应用通过image.ImageReceiver注册imageArrival图像回调方法，获取每帧图像数据实例image.Image，应用通过定义一个width为1080\*height为1080分辨率的预览流直接创建pixelMap，此时获取到的stride的值为1088，解析buffer时若直接按照宽去读取每行数据（使用了无效像素数据）并存储到全局变量stridePixel中，传给Image送显，会导致预览流花屏。

   ```typescript
   onImageArrival(receiver: image.ImageReceiver): void {
     receiver.on('imageArrival', () => {
       receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
         if (err || nextImage === undefined) {
           Logger.error(TAG, `requestPermissionsFromUser call Failed! error: ${err.code}`);
           return;
         }
         if (nextImage) {
           nextImage.getComponent(image.ComponentType.JPEG, async (_err, component: image.Component) => {
             let width: number = 1080;
             let height: number = 1080;
             let pixelMap: image.PixelMap | undefined = await image.createPixelMap(component.byteBuffer, {
               size: {
                 height: height,
                 width: width
               },
               srcPixelFormat: image.PixelMapFormat.NV21
             })
             AppStorage.setOrCreate('stridePixel', pixelMap);
             nextImage.release();
           })
         }
       });
     })
   }
   ```
2. 在初始相机模块时，调用onImageArrival()，将未处理的width和height作为size，创建PixelMap，通过在Image中传入被@StorageLink修饰的变量stridePixel进行数据刷新，图片送显。

   ```typescript
   @Component
   export struct PageThree {
     pathStack: NavPathStack = new NavPathStack();
     @State name: string = 'pageOne';
     @State isShowStridePixel: boolean = false;
     @StorageLink('stridePixel') @Watch('onStridePixel') stridePixel: image.PixelMap | undefined = undefined;
     @State imageWidth: number = 1080;
     @State imageHeight: number = 1080;
     @StorageLink('previewRotation') previewRotate: number = 0;

     onStridePixel(): void {
       this.isShowStridePixel = true;
     }

     aboutToAppear(): void {
       CameraService.initCamera(0, this.getUIContext());
     }

     aboutToDisappear(): void {
       CameraService.releaseCamera();
     }

     // ...
     build() {
       NavDestination() {
         // ...
         Column() {
           if (this.isShowStridePixel) {
             Image(this.stridePixel)
               .width(this.getUIContext().px2vp(this.imageWidth))
               .height(this.getUIContext().px2vp(this.imageHeight))
               .margin({ top: 150 })
               .rotate({
                 z: 0.5,
                 angle: this.previewRotate
               })
           }
           // ...
         }
         .justifyContent(FlexAlign.Center)
         .height('90%')
         .width('100%')
       }
       .backgroundColor(Color.White)
       .hideTitleBar(true)
       .onBackPressed(() => {
         this.pathStack.pop();
         return true;
       })
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack;
       })
     }
   }
   ```

【正例一】开发者使用width，height，stride三个值，处理相机预览流数据，处理stride方法一如下。

分两种情况：

1. 当stride和width相等时，按宽读取buffer不影响结果。
2. 当stride和width不等时，将相机返回的预览流数据即component.byteBuffer的数据去除stride，拷贝得到新的dstArr数据进行数据处理，将处理后的dstArr数组buffer，通过width和height直接创建pixelMap, 并存储到全局变量stridePixel中，传给Image送显。

   ```typescript
   onImageArrival(receiver: image.ImageReceiver): void {
     // ...
         if (nextImage) {
           nextImage.getComponent(image.ComponentType.JPEG,
             async (err, component: image.Component) => {
               let width: number = 1080;
               let height: number = 1080;
               let stride: number = component.rowStride;
               Logger.info(TAG, `receiver getComponent width:${width} height:${height} stride:${stride}`);
               if (stride === width) {
                 let pixelMap: image.PixelMap | undefined = await image.createPixelMap(component.byteBuffer, {
                   size: { height: height, width: width },
                   srcPixelFormat: image.PixelMapFormat.NV21,
                 })
                 AppStorage.setOrCreate('stridePixel', pixelMap);
               } else {
                 const dstBufferSize: number = width * height *
                   1.5;
                 const dstArr: Uint8Array = new Uint8Array(dstBufferSize);
                 for (let j = 0; j < height * 1.5; j++) {
                   const srcBuf: Uint8Array = new Uint8Array(component.byteBuffer, j * stride,
                     width);
                   dstArr.set(srcBuf, j * width);
                 }
                 let pixelMap: image.PixelMap | undefined = await image.createPixelMap(dstArr.buffer, {
                   size: { height: height, width: width },
                   srcPixelFormat: image.PixelMapFormat.NV21,
                 })
                 AppStorage.setOrCreate('stridePixel', pixelMap);
               }
               nextImage.release();
             })
         }
       });
     })
   }
   ```

【正例二】开发者使用width，height，stride三个值，处理相机预览流数据，处理stride方法二如下。

分两种情况：

1. 当stride和width相等时，与正例一情况一致，此处不再赘述。
2. 当stride和width不等时，如果应用想使用byteBuffer预览流数据创建pixelMap直接显示，可以根据stride\*height字节的大小先创建pixelMap，然后调用PixelMap的cropSync()方法裁剪掉多余的像素，从而正确处理stride，解决预览流花屏问题。

   ```typescript
   onImageArrival(receiver: image.ImageReceiver): void {
     receiver.on('imageArrival', () => {
       receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
         // ...
         if (nextImage) {
           nextImage.getComponent(image.ComponentType.JPEG, async (_err, component: image.Component) => {
             let width: number = 1080;
             let height: number = 1080;
             let stride: number = component.rowStride;
             Logger.info(TAG, `receiver getComponent width:${width} height:${height} stride:${stride}`);
             if (stride === width) {
               let pixelMap: image.PixelMap | undefined = await image.createPixelMap(component.byteBuffer, {
                 size: { height: height, width: width },
                 srcPixelFormat: image.PixelMapFormat.NV21,
               })
               AppStorage.setOrCreate('stridePixel', pixelMap);
             } else {
               let pixelMap: image.PixelMap | undefined = await image.createPixelMap(component.byteBuffer, {
                 size: { height: height, width: stride },
                 srcPixelFormat: 8,
               })
               try {
                 pixelMap.cropSync({
                   size: { width: width, height: height },
                   x: 0,
                   y: 0
                 })
                 let pixelBefore: PixelMap | undefined = AppStorage.get('stridePixel');
                 await pixelBefore?.release();
                 AppStorage.setOrCreate('stridePixel', pixelMap);
               } catch (error) {
                 let err: BusinessError = error as BusinessError;
                 hilog.warn(0x000, 'testTag', `setColorMode failed, code=${err.code}, message=${err.message}`);
               }
             }
             nextImage.release();
           })
         }
       });
     })
   }
   ```

## 效果对比

**表 1**

| （反例）未处理 stride | （正例）处理 stride 的方案一 | （正例）处理 stride 的方案二 |
| --- | --- | --- |
|  |  |  |

## 常见问题

### 如何获取相机预览流帧数据

通过ImageReceiver中imageArrival事件监听获取底层返回的图像数据，详细请参见[双路预览(ArkTS)](camera-dual-channel-preview.md#开发步骤)。

### 如何获取预览流图像的stride的值

可以通过预览流帧数据的返回值image.Component.rowStride获取stride。

## 示例代码

* [处理stride解决相机预览流花屏问题](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/DealStrideSolution)
