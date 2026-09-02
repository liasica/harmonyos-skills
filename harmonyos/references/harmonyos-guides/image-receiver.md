---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver
title: 使用ImageReceiver完成图片接收
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片接收 > 使用ImageReceiver完成图片接收
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e2b4a1a528096b67391b5c0f172c68d7d9bd9a8aee37a7948157dbc5b8a847bd
---

图片接收类ImageReceiver用于获取组件SurfaceId，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

**说明** 

Receiver作为消费者，需要有对应的生产者提供数据才能实现完整功能。常见的生产者是相机的拍照流或预览流。ImageReceiver只作为图片的接收方、消费者，在ImageReceiver设置的size、format等属性实际上并不会生效，图片createImageReceiver时传入的参数不产生实际影响。图片属性需要在发送方、生产者进行设置，如在使用[createpreviewoutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput)创建相机预览流时配置[profile](../harmonyos-references/arkts-apis-camera-i.md#profile)。

ImageReceiver可以接收相机预览流中的图片，实现[双路预览](camera-dual-channel-preview.md)。

相关API的详细介绍请参见[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)。

## 开发步骤

创建ImageReceiver对象，获取SurfaceId创建预览流，注册图像监听，按需处理预览流每帧图像。

1. 导入相关模块包。

   ```typescript
   import { image } from '@kit.ImageKit'
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit'
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建ImageReceiver对象，通过ImageReceiver对象可获取预览流SurfaceId。

   ```typescript
   async function initImageReceiver(): Promise<void> {
     // 创建ImageReceiver对象。createImageReceiver的参数不会对接收到的数据产生实际影响。
     let size: image.Size = { width: imageWidth, height: imageHeight };
     // capacity为期望缓存数量，实际值由设备能力决定，此处8仅为示例值。
     let imageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
     // 获取预览流SurfaceId。
     let imageReceiverSurfaceId = await imageReceiver.getReceivingSurfaceId();
     console.info(`initImageReceiver imageReceiverSurfaceId:${imageReceiverSurfaceId}`);
   }
   ```
3. 注册监听处理预览流每帧图像数据：通过ImageReceiver中imageArrival事件监听获取底层返回的图像数据。详细的API说明请参考[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)。

   ```typescript
   function onImageArrival(receiver: image.ImageReceiver) {
     // 注册imageArrival监听。
     receiver.on('imageArrival', () => {
       // 获取图像。
       receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
         if (err || nextImage === undefined) {
           console.error('readNextImage failed');
           return;
         }
         // 解析图像内容。
         (async () => {
           try {
             let imgComponent = await nextImage.getComponent(image.ComponentType.JPEG);
             if (!imgComponent.byteBuffer) {
               console.error('byteBuffer is null');
               return;
             }
             // 详情见下方解析图片buffer数据参考，本示例以方式一为例。
             let width = nextImage.size.width; // 获取图片的宽。
             let height = nextImage.size.height; // 获取图片的高。
             let stride = imgComponent.rowStride; // 获取图片的stride。
             console.debug(`getComponent with width:${width} height:${height} stride:${stride}`);
             // stride与width一致。
             if (stride == width) {
               let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
                 size: { height: height, width: width },
                 srcPixelFormat: image.PixelMapFormat.NV21,
               })
             } else {
               // stride与width不一致。
               const dstBufferSize = width * height * 1.5;
               const dstArr = new Uint8Array(dstBufferSize);
               for (let j = 0; j < height * 1.5; j++) {
                 // 不同设备内存不同，若内存太小，则无法全部写完。
                 const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width);
                 dstArr.set(srcBuf, j * width);
               }
               let pixelMap = await image.createPixelMap(dstArr.buffer, {
                 size: { height: height, width: width },
                 srcPixelFormat: image.PixelMapFormat.NV21,
               })
             }
           } catch (error) {
             console.error('getComponent failed');
           } finally {
             // 确保当前buffer没有在使用的情况下，可进行资源释放。
             // 如果对buffer进行异步操作，需要在异步操作结束后再释放该资源（nextImage.release()）。
             await nextImage.release();
           }
         })();
       })
     })
   }
   ```

通过[image.Component](../harmonyos-references/arkts-apis-image-i.md#component9)解析图片的buffer数据。

**注意** 

需要确认图像的宽（width）是否与行距（rowStride）一致，如果不一致可参考以下方式一和方式二进行预处理。

方式一：去除imgComponent.byteBuffer中stride数据，拷贝得到新的buffer，调用不支持stride的接口处理buffer。

```typescript
// stride与width不一致。
const dstBufferSize = width * height * 1.5
const dstArr = new Uint8Array(dstBufferSize)
for (let j = 0; j < height * 1.5; j++) {
  const srcBuf = new Uint8Array(imgComponent.byteBuffer, j * stride, width)
  dstArr.set(srcBuf, j * width)
}
let pixelMap = await image.createPixelMap(dstArr.buffer, {
  size: { height: height, width: width },
  srcPixelFormat: image.PixelMapFormat.NV21,
})
```

方式二：根据stride \* height创建pixelMap，然后调用pixelMap的cropSync方法裁剪掉多余的像素。

```typescript
// 创建pixelMap，width传入行距（stride）的值。
let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
  size:{height: height, width: stride}, srcPixelFormat: image.PixelMapFormat.NV21});
// 裁剪多余的像素。
try {
  pixelMap.cropSync({size:{width:width, height:height}, x:0, y:0});
} catch (err) {
  hilog.error(0x00000, TAG, `adjust bufferSize failed: ${err}!`);
}
```
