---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-53
title: 如何实现保存图片边缘增加贴边效果
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何实现保存图片边缘增加贴边效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:597742c0b791e2d562a45ce7bac8a12c04a6f405e10a17a76936172b2bddf1e8
---

## 问题现象

使用photoPicker选中一张图片，如何给图片增加一个贴边效果？

## 背景知识

* [PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)：图库选择器对象用于支持选择图片、视频等用户场景。使用前，需先创建PhotoViewPicker实例。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)为图像像素类，用于读取或写入图像数据以及获取图像信息，常用于图片的显示与处理。

## 解决方案

使用photoPicker选择一张图片，并将图片解码为PixelMap，获取图片宽高，根据需要的贴边宽度创建一个新的PixelMap并对像素点进行遍历，判断像素点位置，若在贴边范围内则填充贴边像素，在原图范围内则保持像素不变。

```ts
import image from '@ohos.multimedia.image';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined;

  async selectPhotoAddStroke(strokeWidth: number) {
    // 选择图库图片
    let selectedUris: Array<string> = [];
    try {
      let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoSelectOptions.maxSelectNumber = 1;
      photoSelectOptions.isPhotoTakingSupported = false;
      photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;

      let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
      let result = await photoViewPicker.select(photoSelectOptions);
      if (result.photoUris.length <= 0) {
        console.info(`No select`);
        return;
      }
      selectedUris = result.photoUris;
    } catch (err) {
      console.info(`Failed to select photo, error: ${JSON.stringify(err)}`);
      return;
    }

    // 解码图片
    let photoUri = selectedUris[0];
    let file: fileIo.File | undefined;
    let imageSource: image.ImageSource | undefined;
    let originalPixelMap: image.PixelMap | undefined;
    try {
      // 读取图片文件
      file = fileIo.openSync(photoUri, fileIo.OpenMode.READ_ONLY);
      let fileSize = fileIo.statSync(file.fd).size;
      let buffer = new ArrayBuffer(fileSize);
      fileIo.readSync(file.fd, buffer);
      // 解码图片
      imageSource = image.createImageSource(buffer);
      originalPixelMap = await imageSource.createPixelMap();
    } catch (err) {
      console.info(`Failed to decode selected photo, error: ${JSON.stringify(err)}`);
      return;
    } finally {
      if (imageSource) {
        await imageSource.release();
      }
      if (file) {
        fileIo.closeSync(file);
      }
    }

    // 给图片增加边缘效果
    try {
      let info = await originalPixelMap.getImageInfo();
      let width = info.size.width;
      let height = info.size.height;

      let pixelsBytesNumber = originalPixelMap.getPixelBytesNumber();
      let originalBuffer = new ArrayBuffer(pixelsBytesNumber);
      await originalPixelMap.readPixelsToBuffer(originalBuffer);

      let newWidth = width + 2 * strokeWidth;
      let newHeight = height + 2 * strokeWidth;
      let newBuffer = new ArrayBuffer(4 * newWidth * newHeight);

      let newBufferView = new Uint8Array(newBuffer);
      let originalView = new Uint8Array(originalBuffer);
      for (let x = 0; x < newWidth; ++x) {
        for (let y = 0; y < newHeight; ++y) {
          let idx = 4 * (x + newWidth * y);
          // 判断像素点位置，贴边范围内填充贴边像素，原图像范围内像素值不变，此处增加红色贴边，开发者可根据需要自行设置
          if ((x < strokeWidth || x >= width + strokeWidth) || (y < strokeWidth || y > height + strokeWidth)) {
            newBufferView[idx] = 255;
            newBufferView[idx + 1] = 0;
            newBufferView[idx + 2] = 0;
            newBufferView[idx + 3] = 255;
          } else {
            let originalIdx = 4 * ((x - strokeWidth) + (y - strokeWidth) * width);
            newBufferView[idx] = originalView[originalIdx];
            newBufferView[idx + 1] = originalView[originalIdx + 1];
            newBufferView[idx + 2] = originalView[originalIdx + 2];
            newBufferView[idx + 3] = originalView[originalIdx + 3];
          }
        }
      }

      let opts: image.InitializationOptions = {
        size: { width: newWidth, height: newHeight },
        srcPixelFormat: image.PixelMapFormat.RGBA_8888
      };
      this.pixelMap = await image.createPixelMap(newBuffer, opts);

      let newInfo = await this.pixelMap.getImageInfo();
      console.info(`${newInfo.size.width} * ${newInfo.size.height}`);
    } catch (err) {
      console.error(`Failed to create pixelmap add stroke, ${JSON.stringify(err)}`);
    } finally {
      if (originalPixelMap) {
        originalPixelMap.release();
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('Add Stroke')
        .fontSize(30)
        .onClick(async () => {
          await this.selectPhotoAddStroke(30); // 传参为边缘宽度，开发者根据需要自定义
        });

      Image(this.pixelMap)
        .width('100%')
        .aspectRatio(1)
        .objectFit(ImageFit.Contain);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

## 总结

对于矩形图片实现贴边效果可以直接获取矩形的宽高实现背景图的绘制，而对于不规则图片处理时，可以考虑使用[基于AscendC算子实现图像边缘检测](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_CANNKit-AscendC-sobel)，获取到图像边缘后对于边缘的像素点向外扩张，实现底部背景效果。
