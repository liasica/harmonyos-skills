---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-51
title: 如何通过SVG字符串加载图片
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何通过SVG字符串加载图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:043d18c13899b585bd2a61eab9c5d45b68c42c2dc7ee00df2760b3226ed5cc5a
---

## 问题现象

通过其他三方库生成的SVG字符串，需要使用Image组件进行加载，如何实现？

## 背景知识

* [Image组件](../harmonyos-references/ts-basic-components-image.md)可显示矢量图（SVG格式的图片），SVG标签文档请参考[SVG标签说明](../harmonyos-references/ts-basic-svg.md)。如果SVG图片没有原始大小，需要给Image组件设置宽高，否则不显示。SVG图片不支持通过image标签引用svg格式和gif格式的本地其他图片。
* 加载SVG图片目前可行的方法有很多，例如下载为SVG文件，然后通过文件读取；或者解析为Uint8Array，然后转为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)进行加载，目前转为PixelMap方式可行性更高。

## 解决方案

需要显示的SVG图片样例效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/oxRpaxLaRuWZNRIH_gJOIg/zh-cn_image_0000002658911825.png "点击放大")

首先可以使用[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)类的[encodeInto](../harmonyos-references/js-apis-util.md#encodeinto9)方法，将SVG字符串转化为Uint8Array类型，然后使用[createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9-2)通过buffer创建ImageSource实例，最后使用[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)返回结果。

```ts
import { image } from '@kit.ImageKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined;
  // 将以下内容替换成从三方库得到的SVG字符串
  svgContent = '';

  async uint8ArrayToPixelMap(svg: string): Promise<image.PixelMap> {
    let encoder = new util.TextEncoder();
    const uint8Array = encoder.encodeInto(svg);
    const iconArray: ArrayBuffer = uint8Array.buffer.slice(0);
    let source = image.createImageSource(iconArray);
    const pixelMap = await source.createPixelMap();
    source.release();
    return pixelMap;
  }

  build() {
    Column() {
      Button('点击根据字符串加载SVG图片')
        .onClick(() => {
          this.uint8ArrayToPixelMap(this.svgContent).then((data: PixelMap) => {
            this.pixelMap = data;
          });
        })
        .margin({ top: 30, bottom: 30 })
      Image(this.pixelMap)
        .width('50%').height('50%')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .margin({ top: 30, bottom: 30 })
    }
    .height('100%')
    .width('100%')
  }
}
```
