---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-55
title: PNG图片透明像素转白色
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > PNG图片透明像素转白色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:18a5196af3dbd782ca5d4ef6e97ff5559f9a28c001ebf6429312fb002de095ca
---

## 问题现象

将PNG图片分享到三方应用时，由于PNG图片存在透明通道，而三方应用不支持透明通道，因此PNG图片的透明背景会被转换成黑色背景。如何处理PNG图片，将透明背景转换为白色背景？

## 背景知识

* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)为图像像素类，用于读取或写入图像数据以及获取图像信息，常用于图片的显示与处理。
* [ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)将所支持格式的图片文件解码为PixelMap，用于显示或处理图片。当前支持的图片文件格式包括JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIC。
* [ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)将PixelMap压缩成不同格式的图片文件，当前支持将PixelMap编码为JPEG、Webp、PNG和HEIC格式。

## 解决方案

将PNG图片的透明背景修改为白色背景，需要解码PNG图片，读取图像像素数据；遍历像素数据，将透明像素修改为白色像素；最后将像素数据重新编码为图片文件。

具体步骤包括：

1. 首先通过ImageSource解码PNG图片为PixelMap。
2. 然后通过PixelMap获得图像的像素数据（RGBA）。遍历像素数据，将透明像素点（A=0）修改为白色像素点（R=255，G=255，B=255，A=255）。通过修改过的像素数据，生成白色背景PixelMap。
3. 最后通过ImagePacker将修改透明像素后的白色背景PixelMap重新编码为PNG图片。

完整示例参考如下：

```ts
import image from '@ohos.multimedia.image';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct PngWhiteBgDemo {
  @State whiteBgPixelMap?: image.PixelMap = undefined;

  async pngBg2WhiteBg(rawFilePath: string, outputPath: string) {
    const context = this.getUIContext().getHostContext() as Context;
    let imageSource: image.ImageSource | undefined;
    let imagePacker: image.ImagePacker | undefined;
    let origPixelMap: image.PixelMap | undefined;
    let outputFile: fileIo.File | undefined;
    try {
      // 解码PNG图片生成PixelMap
      const imgData = context.resourceManager.getRawFileContentSync(rawFilePath);
      imageSource = image.createImageSource(imgData.buffer.slice(0));
      origPixelMap = await imageSource.createPixelMap();
      // 读取PixelMap图像像素数据
      const pixelsBytesCnt = origPixelMap.getPixelBytesNumber();
      const pixelsBuffer = new ArrayBuffer(pixelsBytesCnt);
      await origPixelMap.readPixelsToBuffer(pixelsBuffer);
      // 将透明像素修改为白色像素
      const pixelsBufferView = new Uint8Array(pixelsBuffer);
      for (let idx = 0; idx < pixelsBytesCnt; idx += 4) {
        const alpha = pixelsBufferView[idx + 3];
        if (alpha === 0) {
          pixelsBufferView[idx] = 255; // R
          pixelsBufferView[idx + 1] = 255; // G
          pixelsBufferView[idx + 2] = 255; // B
          pixelsBufferView[idx + 3] = 255; // A
        }
      }
      // 生成白色背景的PixelMap
      const imgSize = (await origPixelMap.getImageInfo()).size;
      const initOpts: image.InitializationOptions = {
        size: imgSize,
        srcPixelFormat: image.PixelMapFormat.RGBA_8888,
      };
      this.whiteBgPixelMap = await image.createPixelMap(pixelsBuffer, initOpts);
      // 重新编码PixelMap生成图片文件，并保存入沙箱路径
      imagePacker = image.createImagePacker();
      const packOpts: image.PackingOption = {
        format: 'image/png',
        quality: 100,
      };
      const openMode = fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.CREATE;
      outputFile = fileIo.openSync(outputPath, openMode);
      await imagePacker.packToFile(this.whiteBgPixelMap, outputFile.fd, packOpts);
    } catch (err) {
      console.error(`Failed to convert background color, Cause: ${JSON.stringify(err)}`);
      return;
    } finally {
      if (origPixelMap) {
        origPixelMap.release();
      }
      if (imageSource) {
        imageSource.release();
      }
      if (imagePacker) {
        imagePacker.release();
      }
      if (outputFile) {
        fileIo.closeSync(outputFile.fd);
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      // 原始透明背景的Png图片
      Image($rawfile('startIcon.png'))
        .width('50%')
        .aspectRatio(1)
        .backgroundColor(Color.Black);
      // 修改背景颜色为白色后的PixelMap
      Image(this.whiteBgPixelMap)
        .width('50%')
        .aspectRatio(1)
        .backgroundColor(Color.Black);

      Button('Convert Background Color')
        .fontSize(20)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          let filePath = context.filesDir + '/output.png';
          await this.pngBg2WhiteBg('startIcon.png', filePath);
        });
    }
    .padding(16)
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

## 常见FAQ

Q：是否可以修改JPG格式图片的背景为白色。

A：JPG格式没有透明通道，不存在透明背景，不能直接修改JPG格式的背景为白色。
