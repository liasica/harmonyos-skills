---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-60
title: 使用rotate接口对PixelMap多次旋转后图像逐渐变小
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 使用rotate接口对PixelMap多次旋转后图像逐渐变小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1522556ce5566207b4a539b0d8f49ebf9949bb0bf6f372602e2bc88d191ee4a2
---

## 问题现象

使用[Image](../harmonyos-references/ts-basic-components-image.md)组件显示[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)图像数据，对PixelMap图像使用[rotate](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9)接口多次旋转后，图片逐渐变小，直到几乎消失不见。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/ImulG6fERCa1oi0XYPmojw/zh-cn_image_0000002628552512.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)组件用于显示图片，支持加载PixelMap类型的数据源。[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性用于设置图片的填充效果，当取值为[ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit).Contain时将会对图片保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)是图像像素类，用于读取或写入图像数据以及获取图像信息。[rotate](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9)接口会根据输入的角度对PixelMap进行旋转，当旋转的角度不是90的整数倍时，旋转后PixelMap的尺寸会发生改变。

## 问题定位

出现问题的核心代码如下：

1. 使用Image组件显示PixelMap数据，组件id为'ImageContent'，objectFit属性设置为ImageFit.Contain，确保图片完整显示。
2. 旋转图片时，先获取Image组件的组件截图，对组件截图旋转相应的角度后，将旋转后的PixelMap赋值给状态变量currentPixelMap，显示在Image组件上。

   ```ts
   // 显示PixelMap图像
   Image(this.currentPixelMap)
     .id('ImageContent')
     .objectFit(ImageFit.Contain)

   // 旋转PixelMap图像的函数
   rotateImage: (rotate: number) => void = (rotate: number) => {
     let pixelMap = componentSnapshot.getSync('ImageContent'); // 获取Image组件的组件截图
     pixelMap?.rotateSync(rotate);                             // 对Image组件的截图旋转相应的角度
     this.currentPixelMap = pixelMap;                          // 用旋转后的组件截图刷新Image组件显示的PixelMap数据
   }
   ```

每次旋转时都是对Image组件截图，并对截图内容进行旋转，然后将旋转后的内容重新显示在Image组件上。存在以下问题：

1. Image组件本身会对图像进行缩放，当objectFit属性设置为ImageFit.Contain时，会放大或者缩小图像使得图像完全显示在显示边界内，若图像本身的宽高比和Image组件的宽高比不一致时，图像不能正好完全铺满Image组件，这时对Image组件截图得到的PixelMap中图像只占一部分，另一部分是组件的背景。
2. 使用rotate接口对图像进行旋转后，当旋转角度不是90的整数倍时，旋转后图像的尺寸会变大，这时旋转前的图像只占据了旋转后图像的一部分。如果对旋转后的图像继续旋转非90度的整数倍，那么图像的尺寸会再次变大，原始图像占据的部分会越来越小，显示在Image组件上时就会逐渐变小。

## 分析结论

在旋转图像时，旋转的不是原始图像，而是对Image组件的截图进行旋转，并且每次旋转都是在上一次旋转得到的图像上进行旋转，而旋转角度为非90度的整数倍时，旋转后的图像尺寸会发生变化，旋转前只占据旋转后图像的一部分，连续多次旋转后，原始图像在图像中占据的部分会越来越小，因此当显示在Image组件上时，看起来图像逐渐变小。

参考代码如下：

```ts
import image from '@ohos.multimedia.image';
import { Context } from '@kit.AbilityKit';

@Entry
@Component
export struct PixelMapRotateSmallerDemo {
  @State rotationPixelMap: image.PixelMap | undefined = undefined; // 旋转PixelMap
  private pixelMap: image.PixelMap | undefined = undefined; // 原始PixelMap
  private rotation: number = 0; // 旋转角度

  async aboutToAppear(): Promise<void> {
    let imageSource: image.ImageSource | undefined;
    try {
      // 读取图片文件，这里以Rawfile目录下的img.png图片为例
      let context = this.getUIContext().getHostContext() as Context;
      let fileData: Uint8Array = context.resourceManager.getRawFileContentSync('img.png');
      // 解码图片文件为PixelMap
      imageSource = image.createImageSource(fileData.buffer.slice(0));
      this.pixelMap = await imageSource.createPixelMap();

      this.rotationPixelMap = await this.getPixelmap();
    } catch (err) {
      console.error(`Failed to load image, Cause: ${JSON.stringify(err)}`);
    } finally {
      if (imageSource) {
        await imageSource.release();
      }
    }
  }

  async getPixelmap() {
    if (this.pixelMap === undefined) {
      return undefined;
    }
    try {
      // 从原始PixelMap读取像素数据
      let bufferSize = this.pixelMap.getPixelBytesNumber();
      let pixelsBuffer = new ArrayBuffer(bufferSize);
      this.pixelMap.readPixelsToBufferSync(pixelsBuffer);
      let info = this.pixelMap.getImageInfoSync();
      // 创建新的PixelMap，确保每次都在原图基础上旋转
      let initOpts: image.InitializationOptions = {
        size: info.size,
        srcPixelFormat: info.pixelFormat,
      };
      let pixelMap = await image.createPixelMap(pixelsBuffer, initOpts);
      return pixelMap;
    } catch (err) {
      console.error(`Failed to copy pixelmap, Cause: ${JSON.stringify(err)}`);
      return undefined;
    }
  }

  async rotatePixelmap() {
    // 设置旋转角度，每次旋转30度
    this.rotation = (this.rotation + 30) % 360;
    let oldPixelMap: image.PixelMap | undefined;
    try {
      let newPixelMap = await this.getPixelmap();
      if (newPixelMap === undefined) {
        return;
      }
      // 旋转PixelMap
      newPixelMap.rotateSync(this.rotation);
      // 保存旧PixelMap
      oldPixelMap = this.rotationPixelMap;
      // 更新PixelMap
      this.rotationPixelMap = newPixelMap;
    } catch (err) {
      console.error(`failed to rotate image, Cause: ${JSON.stringify(err)}`);
    } finally {
      if (oldPixelMap) {
        oldPixelMap.release();
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      Image(this.rotationPixelMap)
        .width('100%')
        .aspectRatio(1)
        .objectFit(ImageFit.None);

      Button() {
        Text('Rotate')
          .padding(8)
          .fontSize(30)
          .fontColor(Color.White);
      }
      .backgroundColor('#0A59F7')
      .onClick(() => {
        this.rotatePixelmap();
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 修改建议

多次旋转图像时，确保每次旋转都是在原始图像的基础上旋转。
