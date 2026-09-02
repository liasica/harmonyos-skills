---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-7
title: 如何对相册图片进行编辑裁剪
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何对相册图片进行编辑裁剪
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:957d1274836cb9f01dabc80b875e69dd82395052654906ad24d6e6d29813abbf
---

可以通过[图片处理](../harmonyos-references/js-apis-image.md)模块的[pixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)方法对图片进行编辑裁剪。

其中包括但不限于：

* [pixelMap.crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)方法，可以根据输入的尺寸对图片进行裁剪。
* [pixelMap.opacity](../harmonyos-references/arkts-apis-image-pixelmap.md#opacity9)方法，可以通过设置透明比率对图片设置透明效果。
* [pixelMap.scale](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9)方法，可以根据输入的宽高对图片进行缩放。
* [pixelMap.rotate](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9)方法，可以根据输入的角度对图片进行旋转。
* [pixelMap.flip](../harmonyos-references/arkts-apis-image-pixelmap.md#flip9)方法，可以根据输入的条件对图片进行翻转。

以下示例代码为[pixelMap.crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)图片裁剪方法的使用：

```ts
// Crop 4:3
class RegionItem {
  /**
   * width coordinate.
   */
  x: number;

  /**
   * height coordinate.
   */
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

export async function cropCommon(pixelMap: PixelMap, cropWidth: number, cropHeight: number, cropPosition: RegionItem) {
  pixelMap.crop({
    size: {
      width: cropWidth,
      height: cropHeight
    },
    x: cropPosition.x,
    y: cropPosition.y
  });
}

// Pass in three parameters: image. PixelMap, image width, and image height. After obtaining the cropped image width and height,
// pass the parameters into the cropCommon method
export async function banner(pixelMap: PixelMap, width: number, height: number) {
  if (width <= height) {
    const cropWidth = width;
    const cropHeight = Math.floor(width * 0.75);
    const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
    cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
    return;
  }
  if (width * 0.75 >= height) {
    const cropWidth = Math.floor(height / 0.75);
    const cropHeight = height;
    const cropPosition = new RegionItem(Math.floor((width - cropWidth) / 2), 0);
    cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
    return;
  }
  const cropWidth = width;
  const cropHeight = Math.floor(width * 0.75);
  const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
  cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
}
```
