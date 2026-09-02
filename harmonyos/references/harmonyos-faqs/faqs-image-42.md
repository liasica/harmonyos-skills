---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-42
title: Image如何显示gif动图
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > Image如何显示gif动图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6d50b07509056c3464420ac37f81b1db75084c7afbb7b8501bad6c7790a5a76e
---

## 问题现象

gif图解码出来的PixelMap放到Image组件中只显示静态图，怎么显示动图？

## 背景知识

* [Image组件](../harmonyos-guides/arkts-graphics-display.md)支持图片的显示，支持加载存档图类型的数据源，包括本地资源、网络资源、Resource资源、媒体库资源和base64，也支持加载PixelMap像素图。
* [ImageSource.createPixelMapList](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmaplist10)支持图片解码并返回PixelMap数组。针对动图如gif、Webp，此接口返回每帧图片数据；针对静态图，此接口返回唯一的一帧图片数据。

## 解决方案

gif图片可以通过createPixelMapList创建PixelMap数组，然后传入[AnimatedDrawableDescriptor](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)类型播放PixelMap数组动画。

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageGifDemo {
  animationOpt: AnimationOptions = { duration: 1000, iterations: -1 };
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor([], this.animationOpt);
  uiContext: UIContext = this.getUIContext();

  build() {
    Column({ space: 20 }) {
      Button('test')
        .onClick(async () => {
          // app.media.gif1是gif文件，需要自行配置
          let pixelMaps = await this.getPixmapFromMedia($r('app.media.gif1'));
          this.animated = new AnimatedDrawableDescriptor(pixelMaps, this.animationOpt);
        })

      Image(this.animated)
        .width('200')
        .height('200')
    }.width('100%')
    .alignItems(HorizontalAlign.Center)
  }

  // 读取资源文件返回PixelMap数组
  private async getPixmapFromMedia(resource: Resource) {
    let uint8Array = await this.uiContext.getHostContext()?.resourceManager.getMediaContent(resource.id);
    let imageSource = image.createImageSource(uint8Array!.buffer.slice(0, uint8Array!.buffer.byteLength));
    let pixelMapList = await imageSource.createPixelMapList({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    return pixelMapList;
  }
}
```

## 总结

Image组件通过AnimatedDrawableDescriptor类型传入PixelMap数组即可实现gif动画的播放。
