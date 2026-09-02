---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-40
title: 如何加载显示不同深度的图片数据
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何加载显示不同深度的图片数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:755d0a746d4a003a12e54a629095066d5af26415637289001f49c99252a20125
---

## 问题现象

对于深度BPP为1，或深度BPP为8的图片数据ArrayBuffer，应该如何转为图片显示？

## 背景知识

在计算机图形学中，BPP（Bits Per Pixel）代表每像素的颜色深度，也就是存储一个像素所需的位数。BPP越高，图像的颜色表现力越丰富，但所需的存储空间也越大。

具体来说，BPP值与图像中每个像素可以表示的颜色数量直接相关。例如，8BPP的图像每个像素使用8位来表示颜色，可以表示256种颜色。而24BPP的图像，每个像素使用24位，其中红、绿、蓝各8位，可以表示超过1600万种颜色，通常用于高质量的真彩色图像。

## 解决方案

使用图片数据创建PixelMap对象可使用[image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)，常用的深度BPP与图片像素的关系如下所示。

| BPP | 说明 | 输出格式 |
| --- | --- | --- |
| 1 | 二值图（黑白图） | 每个像素用1位表示是黑色还是白色。 |
| 8 | 灰度图 | 灰度图像，每个像素用8位表示，可表示256种灰度。 |
| 24 | RGB彩色图 | RGB 真彩色，每个像素用24位表示（8位红色+8位绿色+8位蓝色），可表示1677万种颜色，是目前最常见的图像格式之一。 |
| 32 | ARGB彩色图 | RGB真彩色加上Alpha通道（透明度），每个像素用32位表示，可以实现半透明效果。 |

将不同深度的图像数据转换为PixelMap，为了保证图片正常显示，需要确定图像数据宽度的准确性，将图像二进制数据ImageData保存在文件中并引用。参考如下：

```ts
import { image } from '@kit.ImageKit';
import { buffer } from '@kit.ArkTS';
import { imageData } from '../common/ImageData';

function convertBitmapArrayToPixels(readBuffer: ArrayBuffer, width: number, height: number, bpp: number) {
  let byteBuffer: Uint8Array = new Uint8Array(readBuffer);
  let byteBufferTemp: Uint8Array = new Uint8Array(new ArrayBuffer(readBuffer.byteLength));
  // 二值化黑白图，每个比特表示像素是黑色还是白色
  if (bpp == 1) {
    byteBufferTemp = new Uint8Array(new ArrayBuffer(byteBuffer.byteLength * 8 * 4));
    for (let index = 0; index < byteBuffer.length; index++) {
      for (let i = 0; i < 8; i++) {
        let value: number = (byteBuffer[index] >> (7 - i)) & 0x00000001;
        if (value == 1) {
          byteBufferTemp[(index * 8 + i) * 4] = 255;
          byteBufferTemp[(index * 8 + i) * 4 + 1] = 255;
          byteBufferTemp[(index * 8 + i) * 4 + 2] = 255;
          byteBufferTemp[(index * 8 + i) * 4 + 3] = 255;
        } else {
          byteBufferTemp[(index * 8 + i) * 4] = 0;
          byteBufferTemp[(index * 8 + i) * 4 + 1] = 0;
          byteBufferTemp[(index * 8 + i) * 4 + 2] = 0;
          byteBufferTemp[(index * 8 + i) * 4 + 3] = 255;
        }

      }
    }
  }
  // 灰度化灰度图，每个字节表示像素的灰度值
  if (bpp == 8) {
    byteBufferTemp = new Uint8Array(new ArrayBuffer(readBuffer.byteLength * 4));
    for (let index = 0; index < byteBuffer.length; index++) {
      let value = byteBuffer[index];
      byteBufferTemp[index * 4] = value;
      byteBufferTemp[index * 4 + 1] = value;
      byteBufferTemp[index * 4 + 2] = value;
      byteBufferTemp[index * 4 + 3] = 255;
    }
  }
  // RGB彩色图，每三个字节表示像素的rgb颜色
  if (bpp == 24) {
    byteBufferTemp = new Uint8Array(new ArrayBuffer(4 * byteBuffer.byteLength / 3));
    for (let i = 0; i < byteBuffer.length / 3; i++) {
      byteBufferTemp[i * 4] = byteBuffer[i * 3];
      byteBufferTemp[i * 4 + 1] = byteBuffer[i * 3 + 1];
      byteBufferTemp[i * 4 + 2] = byteBuffer[i * 3 + 2];
      byteBufferTemp[i * 4 + 3] = 255;
    }
  }
  let color: ArrayBuffer = byteBufferTemp.buffer as ArrayBuffer;
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: height, width: width } };
  let pixelMapTemp: image.PixelMap = image.createPixelMapSync(color, opts);
  return pixelMapTemp;
}

@Entry
@Component
struct BppPixelMapPage {
  @State pixelMapTemp: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Image(this.pixelMapTemp)
        .objectFit(ImageFit.Contain)
        .width('49%')
        .height(240);
      Button('读取图片')
        .width(150)
        .onClick(() => {
          // 文章图片数据仅作为示例，需要保证传入图片的宽高属性准确，否则会导致崩溃
          this.pixelMapTemp = convertBitmapArrayToPixels(buffer.from(imageData).buffer, 787, 1146, 8);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 总结

加载显示不同深度的图片数据，可参考以下步骤：

1. 获取图片二进制数据，并写入缓冲区。
2. 根据深度（BPP）不同，采取对应的像素数据处理。
3. 将处理完成的像素数据通过image.createPixelMap创建新的PixelMap实例并展示。需要注意的是，创建PixelMap需要确保图片宽高属性正确，当宽高属性错误时，会因为跨距问题导致图像出现斜条纹。
