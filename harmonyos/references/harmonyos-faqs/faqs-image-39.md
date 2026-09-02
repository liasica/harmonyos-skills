---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-39
title: 实现图片部分区域透明化
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 实现图片部分区域透明化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af24cc86fe5708e27b5645dfa35dc3ecfd25ba40a29167972c0d5e1f780281ff
---

## 问题现象

在图片处理时，如何实现图片部分区域自定义。例如使部分区域透明化，以达到图片部分显示的效果。

## 背景知识

* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)图像像素类，用于读取或写入图像数据以及获取图像信息。图片解码是指将所支持格式的图片文件解码成统一的PixelMap格式，目前支持的图片格式有JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIF。PixelMap主要用于图像显示或进一步处理。
* 通过接口[readPixelsToBufferSync](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelstobuffersync12)按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中，同步返回结果。对获取的像素数据做相应的处理，达到想要的效果。

## 解决方案

实现图片部分区域透明化，可参考以下步骤：

1. 使用图片解码获取需要转换的图片像素数据，生成后续操作中使用的PixelMap对象，可参考[使用ImageSource完成图片解码](../harmonyos-guides/image-decoding.md)。
2. 使用[getImageInfo](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfo7-1)获取图片宽高信息，为后续区域指定提供参考标准。
3. 使用readPixelsToBufferSync将图片像素数据写入缓冲区中，通过像素数组遍历，将符合条件的像素值进行替换。
4. 使用[createPixelMapSync](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmapsync12)将修改后的像素数据写入新的PixelMap图像中，并通过Image组件进行展示。

```ts
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

// 透明化方向枚举
enum TransparentDirection {
  Left,
  Right,
  Top,
  Bottom,
}

/**
 * 将图片按方向做部分透明处理
 * @param pixelMap：需要透明化处理的位图
 * @param type：透明化的方向
 * @param transparentCount：透明化的比例
 * @returns 处理好的图片
 */
function getTransparentPixelMap(pixelMap: PixelMap, type: TransparentDirection,
  transparentCount: number): image.PixelMap {
  let imageInfo = pixelMap.getImageInfoSync();
  let width = imageInfo.size.width;
  let height = imageInfo.size.height;
  // readBuffer：保存原始位图数据
  // desBuffer：保存透明化处理后的位图数据
  let readBuffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
  let desBuffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
  // 读取原始位图数据
  pixelMap.readPixelsToBufferSync(readBuffer);
  // uint32Buffer：原始位图数据，4个字节为一个像素
  let uint32Buffer: Uint32Array = new Uint32Array(readBuffer);
  let uint8BufferTemp: Uint8Array = new Uint8Array(desBuffer);
  // 透明化处理
  for (let h = 0; h < height; h++) {
    for (let w = 0; w < width; w++) {
      let index = h * width + w;
      let indexTemp = h * width + w;
      let pixelColor = uint32Buffer[index];
      // 遍历所有像素点，判断每个像素点是否需要透明化处理。
      let isTransparent = false;
      if (type == TransparentDirection.Left) {
        if (w < transparentCount * width) {
          isTransparent = true;
        }
      }
      if (type == TransparentDirection.Right) {
        if (w >= transparentCount * width) {
          isTransparent = true;
        }
      }
      if (type == TransparentDirection.Top) {
        if (h < transparentCount * height) {
          isTransparent = true;
        }
      }
      if (type == TransparentDirection.Bottom) {
        if (h >= transparentCount * height) {
          isTransparent = true;
        }
      }
      // 需要透明化处理的，Alpha值设置为0。不需要透明化处理的，复制原始像素值。
      if (isTransparent == true) {
        uint8BufferTemp[indexTemp * 4] = 255;
        uint8BufferTemp[indexTemp * 4 + 1] = 255;
        uint8BufferTemp[indexTemp * 4 + 2] = 255;
        uint8BufferTemp[indexTemp * 4 + 3] = 0;
      } else {
        uint8BufferTemp[indexTemp * 4] = (pixelColor >> 16) & 0x000000ff;
        uint8BufferTemp[indexTemp * 4 + 1] = (pixelColor >> 8) & 0x000000ff;
        uint8BufferTemp[indexTemp * 4 + 2] = (pixelColor >> 0) & 0x000000ff;
        uint8BufferTemp[indexTemp * 4 + 3] = (pixelColor >> 24) & 0x000000ff;
      }
    }
  }
  // 创建透明化处理后的PixelMap对象
  let color: ArrayBuffer = uint8BufferTemp.buffer as ArrayBuffer;
  let opts: image.InitializationOptions =
    { editable: true, pixelFormat: imageInfo.pixelFormat, size: { height: height, width: width } };
  let pixelMapTemp: image.PixelMap = image.createPixelMapSync(color, opts);
  return pixelMapTemp;
}

@Entry
@Component
struct ImageProcessingPage {
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State pixelMapTemp: image.PixelMap | undefined = undefined;
  @State pixelMapTemp1: image.PixelMap | undefined = undefined;

  getPixelMapByImage(resId: number) {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 获取resourceManager资源管理器
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    // 获取图片资源文件数据
    let fileUint8Arr = resourceMgr.getMediaContentSync(resId);
    // 通过图片资源文件的描述符创建ImageSource
    const imageSource: image.ImageSource = image.createImageSource(fileUint8Arr.buffer);
    let decodingOptions: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    };
    // 解码图片得到对应的PixelMap。
    const pixelMap: image.PixelMap = imageSource.createPixelMapSync(decodingOptions);
    return pixelMap;
  }

  aboutToAppear() {
    // startIcon仅作展示使用，开发者可以自行调整。
    this.pixelMap = this.getPixelMapByImage($r('app.media.startIcon').id);
  }

  @Styles
  ButtonStyle(){
    .backgroundColor('#0D9FFB')
    .width(120)
    .height(35)
    .margin({
      top: 5,
      bottom: 5,
      left: 5,
      right: 5
    });
  }

  build() {
    Column({ space: 5 }) {
      Image(this.pixelMap)
        .objectFit(ImageFit.Contain)
        .margin({ right: 5 })
        .width('45%')
        .height(200)
      Row() {
        Image(this.pixelMapTemp)
          .objectFit(ImageFit.Contain)
          .backgroundColor(Color.Grey)
          .margin({ right: 5 })
          .width('45%')
          .height(200)
        Image(this.pixelMapTemp1)
          .objectFit(ImageFit.Contain)
          .backgroundColor(Color.Grey)
          .width('45%')
          .height(200)
      }

      Text('图片透明处理')
      Row() {
        Button('右边透明50%').ButtonStyle()
          .onClick(() => {
            this.pixelMapTemp = getTransparentPixelMap(this.pixelMap as image.PixelMap, TransparentDirection.Right, 0.5);
          })
        Button('下边透明50%').ButtonStyle()
          .onClick(() => {
            this.pixelMapTemp1 =
              getTransparentPixelMap(this.pixelMap as image.PixelMap, TransparentDirection.Bottom, 0.5);
          })
      }
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
  }
}
```

## 总结

实现图片部分区域透明化，可以通过图片编解码修改指定区域像素值后，生成新的PixelMap用于图片展示，以达到部分图片显示的效果。除了实现部分区域透明化，也可以根据场景需求，将图片部分区域转换为指定颜色。
