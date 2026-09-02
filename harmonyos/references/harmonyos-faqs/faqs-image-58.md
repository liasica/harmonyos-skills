---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-58
title: 点击图片时如何判断点击的位置是否为透明区域
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 点击图片时如何判断点击的位置是否为透明区域
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:859a9195653dc6f9fbbd66d8a75c8716ff6bf6aaf4b751ce51d78706aeef570e
---

## 问题现象

一张SVG图片渲染在UI界面上，点击该图片时，如何区分当前点击位置是有图案的非透明区域还是无图案的透明区域？

## 背景知识

[Image](../harmonyos-references/ts-basic-components-image.md)组件用于在应用中显示图片，支持加载[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)类型的位图数据。Image组件被点击时，会触发[onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)事件，onClick事件回调中会返回点击位置的坐标。

[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)类用于将支持格式的图片文件解码成[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，当前支持的图片文件格式包括JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIF。

ImageSource类的[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7-2)接口通过图片解码参数[DecodingOptions](../harmonyos-references/arkts-apis-image-i.md#decodingoptions7)创建PixelMap。图片解码参数支持设置解码的像素格式，默认值为RGBA\_8888，其中A（Alpha）代表像素的透明度信息，当Alpha值为0时代表透明像素。

## 解决方案

1. 创建[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)对象，将需要显示的SVG图片解码成RGBA\_8888格式[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)对象。使用[Image](../harmonyos-references/ts-basic-components-image.md)组件显示SVG解码生成的PixelMap对象。注意Image组件与PixelMap位图的宽高比保持一致，确保位图正好完全占据Image组件。
2. 通过[Image](../harmonyos-references/ts-basic-components-image.md)组件的[onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)事件获得用户点击的图片位置，然后通过Image组件和PixelMap对象的缩放比例计算得到对应的像素点位置，最后通过PixelMap类的[readPixelsSync](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelssync12)方法得到对应像素点的值，根据该像素点Alpha分量的值判断是否为透明像素。

完整参考代码如下：

```ts
import image from '@ohos.multimedia.image';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const IMAGE_WIDTH = 300;

@Entry
@Component
struct Index {
  @State ratio: number = 1;
  @State imageWidth: number = 1;
  @State isTransport: string = '非透明';
  @State imagePixelMap: image.PixelMap | undefined = undefined;
  private pixelMapWidth: number = 1;

  async aboutToAppear(): Promise<void> {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    try {
      // 加载资源目录图片文件picture.svg
      let content: Uint8Array = resourceMgr.getMediaContentSync($r('app.media.picture').id);
      let imageSource: image.ImageSource = image.createImageSource(content.buffer.slice(0));
      let decodingOptions: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
      };
      this.imagePixelMap = await imageSource.createPixelMap(decodingOptions);
      let imageSize: Size = this.imagePixelMap.getImageInfoSync().size;
      let aspectRatio = imageSize.width / imageSize.height;
      this.pixelMapWidth = imageSize.width;

      this.imageWidth = this.getUIContext().vp2px(IMAGE_WIDTH);
      this.ratio = aspectRatio;
    } catch (err) {
      console.info(`Failed to get pixel map, ${JSON.stringify(err)}`);
    }
  }

  isTransportPixel(posX: number, posY: number): boolean {
    if (this.imagePixelMap === undefined) {
      throw Error('PixelMap is undefined');
    }
    // 读取对应位置的像素点数据
    let area: image.PositionArea = {
      pixels: new ArrayBuffer(4),
      offset: 0,
      stride: 4,
      region: { size: { height: 1, width: 1 }, x: Math.floor(posX), y: Math.floor(posY) },
    };
    try {
      this.imagePixelMap.readPixelsSync(area);
    } catch (err) {
      console.error(`failed to read pixels, error is ${JSON.stringify(err)}`);
      throw Error(err);
    }
    // 判断是否为透明像素点
    let pixelsView: Uint8Array = new Uint8Array(area.pixels);
    let alphaValue: number = pixelsView[3];
    console.info(`${pixelsView[0]} ${pixelsView[1]} ${pixelsView[2]} ${pixelsView[3]}`);

    return alphaValue === 0;
  }

  build() {
    Column({ space: 20 }) {
      Text(this.isTransport)
        .padding(5)
        .fontSize(20);

      Image(this.imagePixelMap)
        .width(IMAGE_WIDTH)
        .aspectRatio(this.ratio)
        .borderWidth(1)
        .borderColor(Color.Black)
        .objectFit(ImageFit.Contain)
        .backgroundColor('0xF1F3F5')
        .onClick((event: ClickEvent) => {
          let radio = this.pixelMapWidth / this.imageWidth;
          let posX: number = this.getUIContext().vp2px(event.x) * radio;
          let posY: number = this.getUIContext().vp2px(event.y) * radio;
          try {
            let isTransport = this.isTransportPixel(posX, posY);
            if (isTransport) {
              this.isTransport = '透明';
            } else {
              this.isTransport = '非透明';
            }
          } catch (err) {
            console.error(`failed to get pixels from image, error is ${JSON.stringify(err)}`);
          }
        });
    }
    // .padding(16)
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
