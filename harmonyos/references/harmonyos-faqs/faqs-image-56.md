---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-56
title: YUV格式图片如何转换为RGB格式并展示
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > YUV格式图片如何转换为RGB格式并展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2ef512cb3ffd27431130f5b311f05517a6eb27891fb13e42575cd8a01bdc111b
---

## 问题现象

如何将YUV格式图片转换为RGB格式并展示？比如YUV422采样格式，NV16或者YUYV存储格式的YUV图片。

## 背景知识

**一、YUV简介。**

YUV是一种颜色编码方法，常使用在各个视频处理组件中。大多数视频采集芯片输出的原始图像数据通常为YUV格式（如YUV422、YUV420等），后续视频处理流程会基于该YUV数据进行预处理（如降噪/缩放）、视频编码（如H.264/H.265压缩），最终生成编码后的视频码流。

YUV编码采用了明亮度和色度表示每个像素的颜色。其中Y表示明亮度（Luminance、Luma），也就是灰阶值。U、V表示色度（Chrominance或Chroma），描述的是色调和饱和度。YCbCr其实是YUV经过缩放和偏移的翻版。其中Y与YUV中的Y含义一致，Cb，Cr同样都指色彩，只是在表示方法上不同而已。YCbCr其中Y是指亮度分量，Cb指蓝色色度分量，而Cr指红色色度分量。

**二、YUV采样格式和存储格式。**

以NV16和YUYV为例，存储顺序简介以及图例参考如下表格：

| 存储格式 | 存储顺序简介 | 存储顺序图例 |
| --- | --- | --- |
| NV16 | NV16是YUV422Semi-Planar的一种，Y分量单独存放，UV分量交错存放。UV在排列的时候，从U开始，总长度为w＊h＊2。 |  |
| YUYV | YUYV属于YUV422Interleaved的一种。事实上，Interleaved是属于Packed的，但是在422中，用Interleaved更加形象一些。在Packed内部，YUV的排列顺序是YUVY，两个Y共用一组UV。 |  |

**三、YUV与RGB之间的转换。**

在图像处理过程中，经常会遇到YUV与RGB之间的转换，以BT601 full range标准为基础，YUV和RGB转换的公式如下：

BT601 full range RGB=[0, 255], Y=[16, 235], UV=[16, 240]。

```ts
R = 1.164 * (Y - 16) + 1.596 * (V - 128)
G = 1.164 * (Y - 16) - 0.392 * (U - 128) - 0.812 * (V - 128)
B = 1.164 * (Y - 16) + 2.016 * (U - 128)
```

## 解决方案

展示YUV格式的图片，首先要确认YUV的采样格式，存储格式，以及YUV与RGB的转换公式。将YUV数据转为RGB数据，再将RGB数据编码为pixelMap。

比如YUV图片是YUV422采样格式，NV16或者YUYV的存储格式，BT601 full range的转换公式。

1. 将YUV数据转为RGB数据，示例代码如下：

   ```ts
   // nv16数据转为rgba数据
   convertNv16ToRgba(nv16Data: Uint8Array, width: number, height: number): Uint8Array {
     const rgbaData = new Uint8Array(width * height * 4);
     const yPlaneSize = width * height;

     for (let i = 0; i < width * height; i++) {
       const row = Math.floor(i / width);
       const col = i % width;
       // Y分量
       const y = nv16Data[i];
       // UV分量 (NV16水平2:1下采样)
       const uvRow = row;
       const uvCol = Math.floor(col / 2) * 2;
       const uvIndex = yPlaneSize + (uvRow * width) + uvCol;

       let u = 0, v = 0;
       if (col % 2 === 0) {
         u = nv16Data[uvIndex];
         v = nv16Data[uvIndex + 1];
       } else {
         u = nv16Data[uvIndex - 2];
         v = nv16Data[uvIndex - 1];
       }
       // 使用查找表快速转换
       const rgb = this.fastYuvToRgb(y, u, v);
       // 填充RGBA
       const rgbaIndex = i * 4;
       rgbaData[rgbaIndex] = rgb.b;
       rgbaData[rgbaIndex + 1] = rgb.g;
       rgbaData[rgbaIndex + 2] = rgb.r;
       rgbaData[rgbaIndex + 3] = 255;
     }
     return rgbaData;
   }

   // yuyv数据转为rgba数据
   convertYuyvToRgba(yuyvArray: Uint8Array, width: number, height: number): Uint8Array {
     const evenWidth = width % 2 === 0 ? width : width + 1;
     // 创建RGBA缓冲区
     const rgbaBuffer = new ArrayBuffer(evenWidth * height * 4);
     const rgbaArray = new Uint8Array(rgbaBuffer);

     for (let y = 0; y < height; y++) {
       for (let x = 0; x < evenWidth; x += 2) {
         const yuyvIdx = (y * evenWidth + x) * 2;
         // 获取YUYV分量
         const y1 = yuyvArray[yuyvIdx]; // Y1
         const u = yuyvArray[yuyvIdx + 1]; // U
         const y2 = yuyvArray[yuyvIdx + 2]; // Y2
         const v = yuyvArray[yuyvIdx + 3]; // V
         // 转换为RGB
         const rgb1 = this.fastYuvToRgb(y1, u, v);
         const rgb2 = this.fastYuvToRgb(y2, u, v);
         // 填入RGBA数组
         const idx1 = (y * evenWidth + x) * 4;
         const idx2 = (y * evenWidth + x + 1) * 4;
         if (x < width) {
           rgbaArray[idx1] = rgb1.b; // B
           rgbaArray[idx1 + 1] = rgb1.g; // G
           rgbaArray[idx1 + 2] = rgb1.r; // R
           rgbaArray[idx1 + 3] = 255; // A（完全不透明）
         }
         if ((x + 1) < width) {
           rgbaArray[idx2] = rgb2.b;
           rgbaArray[idx2 + 1] = rgb2.g;
           rgbaArray[idx2 + 2] = rgb2.r;
           rgbaArray[idx2 + 3] = 255;
         }
       }
     }
     return rgbaArray;
   }

   /**
    * 快速YUV转RGB (整数运算)
    */
   fastYuvToRgb(y: number, u: number, v: number): rgbInfo {
     // 使用整数运算的近似公式
     const c = y - 16;
     const d = u - 128;
     const e = v - 128;

     // 使用整数运算 (乘以1000避免浮点数运算)
     let r = (1164 * c + 1596 * e) / 1000;
     let g = (1164 * c - 392 * d - 812 * e) / 1000;
     let b = (1164 * c + 2016 * d) / 1000;

     // 限制范围
     r = Math.min(255, Math.max(0, Math.round(r)));
     g = Math.min(255, Math.max(0, Math.round(g)));
     b = Math.min(255, Math.max(0, Math.round(b)));

     return { r, g, b };
   }
   ```
2. 完整示例代码如下：

   ```ts
   import { resourceManager } from '@kit.LocalizationKit';
   import { image } from '@kit.ImageKit';

   export class rgbInfo {
     r: number = 0;
     g: number = 0;
     b: number = 0;
   }

   @Entry
   @Component
   struct YuvTogrba {
     @State pixelMapNv16: PixelMap | undefined = undefined;
     @State pixelMapYuyv: PixelMap | undefined = undefined;
     private context: Context = this.getUIContext().getHostContext() as Context;

     // nv16数据转为rgba数据
     convertNv16ToRgba(nv16Data: Uint8Array, width: number, height: number): Uint8Array {
       const rgbaData = new Uint8Array(width * height * 4);
       const yPlaneSize = width * height;

       for (let i = 0; i < width * height; i++) {
         const row = Math.floor(i / width);
         const col = i % width;
         // Y分量
         const y = nv16Data[i];
         // UV分量 (NV16水平2:1下采样)
         const uvRow = row;
         const uvCol = Math.floor(col / 2) * 2;
         const uvIndex = yPlaneSize + (uvRow * width) + uvCol;

         let u = 0, v = 0;
         if (col % 2 === 0) {
           u = nv16Data[uvIndex];
           v = nv16Data[uvIndex + 1];
         } else {
           u = nv16Data[uvIndex - 2];
           v = nv16Data[uvIndex - 1];
         }
         // 使用查找表快速转换
         const rgb = this.fastYuvToRgb(y, u, v);
         // 填充RGBA
         const rgbaIndex = i * 4;
         rgbaData[rgbaIndex] = rgb.b;
         rgbaData[rgbaIndex + 1] = rgb.g;
         rgbaData[rgbaIndex + 2] = rgb.r;
         rgbaData[rgbaIndex + 3] = 255;
       }
       return rgbaData;
     }

     // yuyv数据转为rgba数据
     convertYuyvToRgba(yuyvArray: Uint8Array, width: number, height: number): Uint8Array {
       const evenWidth = width % 2 === 0 ? width : width + 1;
       // 创建RGBA缓冲区
       const rgbaBuffer = new ArrayBuffer(evenWidth * height * 4);
       const rgbaArray = new Uint8Array(rgbaBuffer);

       for (let y = 0; y < height; y++) {
         for (let x = 0; x < evenWidth; x += 2) {
           const yuyvIdx = (y * evenWidth + x) * 2;
           // 获取YUYV分量
           const y1 = yuyvArray[yuyvIdx]; // Y1
           const u = yuyvArray[yuyvIdx + 1]; // U
           const y2 = yuyvArray[yuyvIdx + 2]; // Y2
           const v = yuyvArray[yuyvIdx + 3]; // V
           // 转换为RGB
           const rgb1 = this.fastYuvToRgb(y1, u, v);
           const rgb2 = this.fastYuvToRgb(y2, u, v);
           // 填入RGBA数组
           const idx1 = (y * evenWidth + x) * 4;
           const idx2 = (y * evenWidth + x + 1) * 4;
           if (x < width) {
             rgbaArray[idx1] = rgb1.b; // B
             rgbaArray[idx1 + 1] = rgb1.g; // G
             rgbaArray[idx1 + 2] = rgb1.r; // R
             rgbaArray[idx1 + 3] = 255; // A（完全不透明）
           }
           if ((x + 1) < width) {
             rgbaArray[idx2] = rgb2.b;
             rgbaArray[idx2 + 1] = rgb2.g;
             rgbaArray[idx2 + 2] = rgb2.r;
             rgbaArray[idx2 + 3] = 255;
           }
         }
       }
       return rgbaArray;
     }

     /**
      * 快速YUV转RGB (整数运算)
      */
     fastYuvToRgb(y: number, u: number, v: number): rgbInfo {
       // 使用整数运算的近似公式
       const c = y - 16;
       const d = u - 128;
       const e = v - 128;

       // 使用整数运算 (乘以1000避免浮点数运算)
       let r = (1164 * c + 1596 * e) / 1000;
       let g = (1164 * c - 392 * d - 812 * e) / 1000;
       let b = (1164 * c + 2016 * d) / 1000;

       // 限制范围
       r = Math.min(255, Math.max(0, Math.round(r)));
       g = Math.min(255, Math.max(0, Math.round(g)));
       b = Math.min(255, Math.max(0, Math.round(b)));

       return { r, g, b };
     }

     build() {
       Row() {
         Column() {
           Row() {
             Column() {
               Image(this.pixelMapNv16)
                 .margin({ bottom: 10 })
                 .width('45%')
                 .height(140)
               Button('nv16转rgba')
                 .onClick(() => {
                   const resourceMgr: resourceManager.ResourceManager = this.context.resourceManager;
                   let rawBuf = resourceMgr.getRawFileContentSync('test_nv16.yuv'); // 需要替换为rawfile目录下实际nv16存储格式的yuv数据
                   let readBuffer = this.convertNv16ToRgba(rawBuf, 550, 400); // 像素宽高要根据实际的yuv数据填写
                   let opts: image.InitializationOptions =
                     { editable: true, pixelFormat: 3, size: { height: 400, width: 550 } }; // 像素宽高要根据实际的yuv数据填写
                   this.pixelMapNv16 = image.createPixelMapSync(readBuffer.buffer, opts);
                 })
             }.margin({ right: 5 })

             Column() {
               Image(this.pixelMapYuyv)
                 .margin({ bottom: 10 })
                 .width('45%')
                 .height(140)
               Button('yuyv转rgba')
                 .onClick(() => {
                   const resourceMgr: resourceManager.ResourceManager = this.context.resourceManager;
                   let rawBuf = resourceMgr.getRawFileContentSync('test_yuyv.yuv'); // 需要替换为rawfile目录下实际yuyv存储格式的yuv数据
                   let readBuffer = this.convertYuyvToRgba(rawBuf, 550, 400); // 像素宽高要根据实际的yuv数据填写
                   let opts: image.InitializationOptions =
                     { editable: true, pixelFormat: 3, size: { height: 400, width: 550 } }; // 像素宽高要根据实际的yuv数据填写
                   this.pixelMapYuyv = image.createPixelMapSync(readBuffer.buffer, opts);
                 })
             }.margin({ left: 5 })
           }
         }.width('100%')
       }.height('100%')
     }
   }
   ```
