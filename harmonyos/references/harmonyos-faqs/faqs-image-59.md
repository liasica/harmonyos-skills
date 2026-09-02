---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-59
title: 如何实现图片压缩
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何实现图片压缩
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae81d73d0ffab7adaf12a32b3ad014c94fe04850dd4c0a4b69c96cfa5cb9545d
---

## 问题现象

在应用开发中，图片压缩是一个极为常见的需求，例如在处理用户上传头像、发布图文动态时，往往需要将图片控制在一定大小以内。本文将围绕这一场景，介绍实现图片压缩的四种主流方案。

## 背景知识

图片压缩的核心目的，是在图片质量、文件体积和解码加载速度之间找到一个最优平衡点。在应用开发中，过大图片不仅消耗用户存储空间、增加网络传输负担，还会在解码时占用大量内存和CPU资源，导致应用卡顿。本文提供了以下四种压缩方案：

| 压缩方案 | 核心原理 | 实现手段 |
| --- | --- | --- |
| 质量压缩 | 改变图像的编码方式，通过舍弃部分不被人眼敏感的细节数据来减小文件体积。它不改变图片的尺寸，但会降低图像的清晰度。 | 使用ImagePacker的[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)方法，通过调整 quality 参数（0-100）来控制压缩程度 。 |
| 尺寸压缩 | 直接减少图片的像素数量，即缩小图片的宽高。这是一种最直接有效的减小图片内存占用和文件大小的方法。 | 操作PixelMap对象的[scale](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9)方法，通过传入宽高的缩放倍数来实现 。 |
| 智能压缩 | 一种目标导向的压缩策略。开发者设定一个期望的“目标文件大小”，系统自动迭代尝试质量压缩和尺寸压缩，直至图片大小最接近且不超过该目标值。 | 结合循环与二分法思想，通过不断调整scale倍数和quality参数，反复对PixelMap进行压缩并检查体积，最终找到最优平衡点 。 |
| 格式转换 | 将图片从一种编码格式转换为另一种，利用不同格式的算法特性来达到压缩目的。例如将有损的JPEG转换为压缩率更高的WebP。 | 在ImagePacker的PackingOption中指定输出format（如'image/webp'），将图片重新编码为指定格式 。 |

## 解决方案

图片压缩主要是通过packToData和scale实现图片压缩，通过对图片进行缩放或者设置编码参数进行压缩。具体实现可以参考以下几种方案。

### 方案一：质量压缩

通过修改编码质量参数quality，该参数仅对JPEG图片生效。WebP、PNG等图片均为无损编码。示例代码如下：

```ts
/**
 * 质量压缩
 */
async qualityCompressionMethod(quality: number) {
  const qualityCompressionMethod = await this.compressionMethod.compressionMethod(100, quality);
  this.showPixelMap = qualityCompressionMethod[0];
  this.savePixelMap = qualityCompressionMethod[1];
  this.afterCompressionSize = qualityCompressionMethod[2];
  this.showCompressFormat = qualityCompressionMethod[3];
}
```

compressionMethod方法代码如下：

```ts
/**
 * 压缩
 */
async compressionMethod(imageScaleVal: number,
  imageQualityVal: number): Promise<[PixelMap, PixelMap, string, string]> {
  const ALBUM_PATH: string = this.uris[0];
  const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
  let buffer = new ArrayBuffer(fs.statSync(file.fd).size);
  fs.readSync(file.fd, buffer);
  fs.closeSync(file);
  const decodingOptions: image.DecodingOptions = { editable: true };
  const imageSource: image.ImageSource = image.createImageSource(buffer);
  return new Promise<[PixelMap, PixelMap, string, string]>((resolve) => {
    imageSource.createPixelMap(decodingOptions).then(async (originalPixelMap: image.PixelMap) => {
      if (AppStorage.get('sizeFlag') != undefined) {
        this.sizeFlag = AppStorage.get('sizeFlag')!;
      }
      if (this.sizeFlag) {
        // 使用scale对图片进行缩放。入参分别为图片宽高的缩放倍数
        await originalPixelMap.scale(imageScaleVal / 100, imageScaleVal / 100);
        // savePixelMap用于把压缩后的图片保存到图库时使用。由于保存图片时调用的packToFile内部会做类似packing的处理，所以这里只保存scale缩放尺寸后的PixelMap。
        this.savePixelMap = originalPixelMap;
        this.imageQuality = imageScaleVal;
      }
      // savePixelMap用于把压缩后的图片保存到图库时使用。
      this.savePixelMap = originalPixelMap;
      if (AppStorage.get('outputCompressFmt') != undefined) {
        this.afterCompressFmt = AppStorage.get('outputCompressFmt')!;
      }

      // packing压缩图片
      let compressedImageData: ArrayBuffer =
        await this.packing(originalPixelMap, imageQualityVal, this.afterCompressFmt);
      // 压缩后的ArrayBuffer数据转PixelMap
      let imageSource = image.createImageSource(compressedImageData);
      let opts: image.DecodingOptions = { editable: true };
      // showPixelMap用于显示压缩后的图片
      const pixelMap: image.PixelMap = await imageSource.createPixelMap(opts);
      this.showPixelMap = pixelMap;
      // showCompressFormat用于显示压缩后的图片格式
      this.showCompressFormat = this.afterCompressFmt;
      // 显示估算packing压缩后的图片大小。该图片在内存中作为ArrayBuffer数据的压缩后大小，这一数值并不直接等同于该图片在最终保存到相册时的实际文件大小。
      this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
      resolve([this.showPixelMap, this.savePixelMap, this.afterCompressionSize, this.afterCompressFmt]);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `Failed to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
    });

  });
}
```

### 方案二：尺寸压缩

调用scale对图片的宽高进行缩放，缩放后的PixelMap通过packToData进行压缩。尺寸压缩不需要修改编码参数里的图片质量。示例代码如下：

```ts
/**
 * 尺寸压缩
 */
async sizeCompressionMethod(size: number) {
  this.sizeFlag = true;
  AppStorage.setOrCreate('sizeFlag', this.sizeFlag);
  const sizeCompressionMethod = await this.compressionMethod.compressionMethod(size, 100);
  this.showPixelMap = sizeCompressionMethod[0];
  this.afterCompressionSize = sizeCompressionMethod[2];
  this.showCompressFormat = sizeCompressionMethod[3];
}
```

### 方案三：智能压缩

智能压缩通过设置优先压缩图片质量和优先压缩图片尺寸。优先压缩图片质量是指优先通过调整图片质量进行压缩。但是如果图片质量压缩到最低仍然超过目标大小，则会再采用scale进行二次压缩。对于通过调整图片质量就能满足目标大小要求的图片，如果想要找到尽可能接近目标大小的最佳压缩大小，可以调低packing最小二分单位，但相应的压缩性能也会更差一些。优先压缩图片尺寸是指优先通过调整图片尺寸进行压缩。如果对图片质量要求不高但是需要压缩后的图片尺寸尽可能大一些也可以调低最低图片质量。示例代码如下：

```ts
/**
 * 智能压缩
 * @param qualityCompression：是否质量优先
 * @param maxCompressedImageSize 指定图片压缩目标大小，单位kb
 * @param minBisectUnit packing最小二分单位
 * @param minQuality 最低图片质量
 */
intelligentCompressionMethod(qualityCompression: boolean, maxCompressedImageSize: number, minBisectUnit: number,
  minQuality: number): Promise<[PixelMap, PixelMap, string, string]> {
  // 获取图库中选择的图片路径
  const ALBUM_PATH: string = this.uris[0];
  const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
  let buffer: ArrayBuffer = new ArrayBuffer(fs.statSync(file.fd).size);
  // 读取图片到buffer
  fs.readSync(file.fd, buffer);
  fs.closeSync(file);
  // 通过缓冲区创建图片源实例
  const imageSource: image.ImageSource = image.createImageSource(buffer);
  // 设置解码参数DecodingOptions，解码获取PixelMap图片对象。
  const decodingOptions: image.DecodingOptions = {
    editable: true, // 是否可编辑。当取值为false时，图片不可二次编辑，如crop等操作将失败。
  };
  return new Promise<[PixelMap, PixelMap, string, string]>((resolve, reject) => {
    imageSource.createPixelMap(decodingOptions).then(async (originalPixelMap: image.PixelMap) => {
      try {
        if (AppStorage.get('outputCompressFmt') != undefined) {
          this.afterCompressFmt = AppStorage.get('outputCompressFmt')!;
        }
        // 压缩图片
        await this.compressedImage(qualityCompression, originalPixelMap, maxCompressedImageSize, minBisectUnit,
          minQuality);
        this.promptAction.showToast({ message: '智能压缩完成！' });
        resolve([this.showPixelMap!, this.savePixelMap!, this.afterCompressionSize, this.showCompressFormat]);
      } catch (err) {
        hilog.error(0x0000, TAG, `Failed to compress image, error code: ${err.code}, message: ${err.message}.`);
        reject(err);
      }
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `Failed to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
      reject(err);
    });
  });
}
```

优先压缩图片质量示例代码如下：

```ts
/**
 * 优先压缩图片尺寸
 * @param sourcePixelMap 原始待压缩图片的PixelMap
 * @param maxCompressedImageSize 指定图片的压缩目标大小
 * @param quality
 */
async scalePriorityCompress(sourcePixelMap: image.PixelMap, maxCompressedImageSize: number, quality: number) {
  let compressedImageData: ArrayBuffer = await this.packing(sourcePixelMap, quality, this.afterCompressFmt);
  // 如果调整过最低图片质量，先计算最低图片质量是否满足要求。如果设定的最低图片质量已经满足目标大小，则直接返回
  if (quality !== IMAGE_QUALITY_HUNDRED &&
    (compressedImageData.byteLength <= maxCompressedImageSize * BYTE_CONVERSION)) {
    // 保存最终压缩的图片质量，用于保存到图库时使用
    this.intelligentCompressionQuality = quality;
    // ArrayBuffer转PixelMap，并保存图片相关数据
    let imageSource = image.createImageSource(compressedImageData);
    let opts: image.DecodingOptions = { editable: true };
    this.showPixelMap = await imageSource.createPixelMap(opts);
    this.savePixelMap = sourcePixelMap;
    this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
    // 更新显示压缩后的图片格式
    this.showCompressFormat = this.afterCompressFmt;
    return;
  }
  // scale压缩图片尺寸。采用while循环每次递减0.4，最终查找到最接近指定图片压缩目标大小的缩放倍数的图片压缩数据。
  let imageScale = 1; // 定义图片宽高的缩放倍数，1表示原比例。
  const REDUCE_SCALE = 0.5;
  const AFTER_COMPRESS_FMT = this.afterCompressFmt;
  // 判断压缩后的图片大小是否大于指定图片的压缩目标大小，如果大于，继续降低缩放倍数压缩。
  while (compressedImageData.byteLength > maxCompressedImageSize * BYTE_CONVERSION) {
    if (imageScale > 0) {
      // 性能知识点: 由于scale会直接修改图片PixelMap数据，所以不适用二分查找scale缩放倍数。这里采用循环递减0.4倍缩放图片，
      // 来查找确定最适合的缩放倍数。如果对图片压缩质量要求不高，建议调高每次递减的缩放倍数，减少循环，提升scale压缩性能。
      imageScale = imageScale - REDUCE_SCALE; // 每次缩放倍数减
      // 使用scale对图片尺寸进行缩放
      await sourcePixelMap.scale(imageScale, imageScale);
      // packing压缩
      compressedImageData = await this.packing(sourcePixelMap, quality, AFTER_COMPRESS_FMT);
    } else {
      // imageScale缩放倍数小于等于0时，没有意义，结束压缩。
      break;
    }
  }
  this.intelligentCompressionQuality = quality;
  let imageSource = image.createImageSource(compressedImageData);
  let opts: image.DecodingOptions = { editable: true };
  this.showPixelMap = await imageSource.createPixelMap(opts);
  this.savePixelMap = sourcePixelMap;
  this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
  this.showCompressFormat = this.afterCompressFmt;
  // 可能会存在scale每次缩小倍数设置过大，导致无法压缩到图片压缩目标大小，弹窗提示
  if (compressedImageData.byteLength > maxCompressedImageSize * BYTE_CONVERSION) {
    let uiContext = AppStorage.get('context') as UIContext;
    uiContext.showAlertDialog({
      message: '当前在设置的scale每次缩小倍数条件下，无法压缩到目标大小，建议调低scale每次缩小倍数后再试',
      alignment: DialogAlignment.Center
    });
  }
}
```

优先压缩图片尺寸示例代码如下：

```ts
/**
 * 优先压缩图片尺寸
 * @param sourcePixelMap 原始待压缩图片的PixelMap
 * @param maxCompressedImageSize 指定图片的压缩目标大小
 * @param quality
 */
async scalePriorityCompress(sourcePixelMap: image.PixelMap, maxCompressedImageSize: number, quality: number) {
  let compressedImageData: ArrayBuffer = await this.packing(sourcePixelMap, quality, this.afterCompressFmt);
  // 如果调整过最低图片质量，先计算最低图片质量是否满足要求。如果设定的最低图片质量已经满足目标大小，则直接返回
  if (quality !== IMAGE_QUALITY_HUNDRED &&
    (compressedImageData.byteLength <= maxCompressedImageSize * BYTE_CONVERSION)) {
    // 保存最终压缩的图片质量，用于保存到图库时使用
    this.intelligentCompressionQuality = quality;
    // ArrayBuffer转PixelMap，并保存图片相关数据
    let imageSource = image.createImageSource(compressedImageData);
    let opts: image.DecodingOptions = { editable: true };
    this.showPixelMap = await imageSource.createPixelMap(opts);
    this.savePixelMap = sourcePixelMap;
    this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
    // 更新显示压缩后的图片格式
    this.showCompressFormat = this.afterCompressFmt;
    return;
  }
  // scale压缩图片尺寸。采用while循环每次递减0.4，最终查找到最接近指定图片压缩目标大小的缩放倍数的图片压缩数据。
  let imageScale = 1; // 定义图片宽高的缩放倍数，1表示原比例。
  const REDUCE_SCALE = 0.5;
  const AFTER_COMPRESS_FMT = this.afterCompressFmt;
  // 判断压缩后的图片大小是否大于指定图片的压缩目标大小，如果大于，继续降低缩放倍数压缩。
  while (compressedImageData.byteLength > maxCompressedImageSize * BYTE_CONVERSION) {
    if (imageScale > 0) {
      // 性能知识点: 由于scale会直接修改图片PixelMap数据，所以不适用二分查找scale缩放倍数。这里采用循环递减0.4倍缩放图片，
      // 来查找确定最适合的缩放倍数。如果对图片压缩质量要求不高，建议调高每次递减的缩放倍数，减少循环，提升scale压缩性能。
      imageScale = imageScale - REDUCE_SCALE; // 每次缩放倍数减
      // 使用scale对图片尺寸进行缩放
      await sourcePixelMap.scale(imageScale, imageScale);
      // packing压缩
      compressedImageData = await this.packing(sourcePixelMap, quality, AFTER_COMPRESS_FMT);
    } else {
      // imageScale缩放倍数小于等于0时，没有意义，结束压缩。
      break;
    }
  }
  this.intelligentCompressionQuality = quality;
  let imageSource = image.createImageSource(compressedImageData);
  let opts: image.DecodingOptions = { editable: true };
  this.showPixelMap = await imageSource.createPixelMap(opts);
  this.savePixelMap = sourcePixelMap;
  this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
  this.showCompressFormat = this.afterCompressFmt;
  // 可能会存在scale每次缩小倍数设置过大，导致无法压缩到图片压缩目标大小，弹窗提示
  if (compressedImageData.byteLength > maxCompressedImageSize * BYTE_CONVERSION) {
    let uiContext = AppStorage.get('context') as UIContext;
    uiContext.showAlertDialog({
      message: '当前在设置的scale每次缩小倍数条件下，无法压缩到目标大小，建议调低scale每次缩小倍数后再试',
      alignment: DialogAlignment.Center
    });
  }
}
```

### 方案四：格式转换

通过格式转换实现图片压缩。常见的图片文件格式文件大小对比：

| 格式 | 文件大小 |
| --- | --- |
| PNG | 无损压缩格式，文件大小通常比有损压缩格式（如JPEG）要大。 |
| JPG | 有损压缩格式，文件大小通常比PNG小得多。通过调整压缩参数，可以进一步减小文件大小，但会牺牲图像质量。 |
| WEBP | 支持有损和无损压缩，文件大小通常比JPEG和PNG更小。有损压缩模式下，WebP可以在保持较高图像质量的同时，显著减小文件大小。 |

本示例以JPEG格式转换，示例代码如下：

```ts
/**
 * 格式转换压缩
 */
formatConversionMethod(format: string): Promise<[PixelMap, PixelMap, string, string]> {
  this.afterCompressFmt = format;
  AppStorage.setOrCreate('convertFormat', format);
  const ALBUM_PATH: string = this.uris[0];
  const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
  let buffer = new ArrayBuffer(fs.statSync(file.fd).size);
  fs.readSync(file.fd, buffer);
  fs.closeSync(file);
  const decodingOptions: image.DecodingOptions = { editable: true };
  const imageSource: image.ImageSource = image.createImageSource(buffer);
  return new Promise<[PixelMap, PixelMap, string, string]>((resolve, reject) => {
    imageSource.createPixelMap(decodingOptions).then(async (pixelMap: image.PixelMap) => {
      this.savePixelMap = pixelMap;
      // packing压缩图片
      let compressedImageData: ArrayBuffer =
        await this.packing(pixelMap, this.imageQuality, this.afterCompressFmt);
      // 压缩后的ArrayBuffer数据转PixelMap
      let imageSource = image.createImageSource(compressedImageData);
      let opts: image.DecodingOptions = { editable: true };
      // showPixelMap用于显示压缩后的图片
      this.showPixelMap = await imageSource.createPixelMap(opts);
      // showCompressFormat用于显示压缩后的图片格式
      this.showCompressFormat = this.afterCompressFmt;
      // 显示估算packing压缩后的图片大小。该图片在内存中作为ArrayBuffer数据的压缩后大小，这一数值并不直接等同于该图片在最终保存到相册时的实际文件大小。
      this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
      this.promptAction.showToast({ message: '格式转换压缩完成！' });
      resolve([this.showPixelMap, this.savePixelMap, this.afterCompressionSize, this.afterCompressFmt]);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `Failed to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
      reject(err);
    });
  });
}
```

完整示例代码如下：

Index.ets：

```ts
import { emitter } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { PromptAction } from '@kit.ArkUI';
import { CompressionMethod } from './compression';

const SPACE_SIX: number = 6; // 组件间距
const SPACE_THIRTY: number = 30; // 组件间距
const FONT_WEIGHT: number = 500;
const BYTE_CONVERSION: number = 1024; // 字节转换

@Entry
@Component
struct Index {
  @State beforeCompressImgSize: string = ''; // 压缩前图片宽高
  @State afterCompressImgSize: string = ''; // 压缩后图片宽高
  @State @Watch('afterCompressChange') afterCompressionSize: string = ''; // 压缩后的图片大小,单位kb
  @State outputFormatIndex: number = 0; // 输出格式初始项，默认原格式
  @State @Watch('compressFormatChange') showCompressFormat: string = ''; // 在页面上显示压缩后的图片格式
  @State showPixelMap: image.PixelMap | undefined = undefined; // 页面上显示压缩后的图片
  @State sizeFlag: boolean = false; // 是否尺寸缩模式
  @State savePixelMap: image.PixelMap | undefined = undefined; // 保存压缩后的图片
  private context: UIContext = this.getUIContext(); // 获取getPhotoAccessHelper需要的context
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  private outputFormat: string[] = ['原格式', 'PNG', 'JPEG', 'WEBP']; // 图片输出格式
  private compressionMethod: CompressionMethod = new CompressionMethod();
  @StorageLink('photoCount') selectPhotoCount: number = 0;
  @StorageLink('beforeCompressFmt') beforeCompressFmt: string = '';
  @StorageLink('afterCompressFmt') afterCompressFmt: string = '';
  @StorageLink('beforeCompressByteLength') beforeCompressByteLength1: number = 0;
  @StorageLink('uris') selcteUris: Array<string> = [];
  @StorageLink('convertFormat') convertFormat: string = '';

  /**
   * 压缩后图片大小
   */
  afterCompressChange() {
    emitter.emit('ImageCompression0', {
      data: {
        afterCompressionSize: this.afterCompressionSize
      }
    });
  }

  /**
   * 压缩后图片格式
   */
  compressFormatChange() {
    emitter.emit('ImageCompression1', {
      data: {
        showCompressFormat: this.showCompressFormat
      }
    });
  }

  /**
   * 尺寸压缩
   */
  async sizeCompressionMethod(size: number) {
    this.sizeFlag = true;
    AppStorage.setOrCreate('sizeFlag', this.sizeFlag);
    const sizeCompressionMethod = await this.compressionMethod.compressionMethod(size, 100);
    this.showPixelMap = sizeCompressionMethod[0];
    this.afterCompressionSize = sizeCompressionMethod[2];
    this.showCompressFormat = sizeCompressionMethod[3];
  }

  /**
   * 质量压缩
   */
  async qualityCompressionMethod(quality: number) {
    const qualityCompressionMethod = await this.compressionMethod.compressionMethod(100, quality);
    this.showPixelMap = qualityCompressionMethod[0];
    this.savePixelMap = qualityCompressionMethod[1];
    this.afterCompressionSize = qualityCompressionMethod[2];
    this.showCompressFormat = qualityCompressionMethod[3];
  }

  /**
   * 显示压缩前和压缩后图片
   */
  @Builder
  displayImage() {
    Row() {
      Text('压缩前：')
        .fontWeight(FONT_WEIGHT)
        .fontSize(16);

      if (this.selectPhotoCount > 0) {
        Text((this.beforeCompressByteLength1 / BYTE_CONVERSION).toFixed(1))
          .fontWeight(FONT_WEIGHT)
          .fontSize(20)
          .fontColor('#ff0e9eff');
        Text('kb  格式：')
          .fontSize(16);
        Text(this.beforeCompressFmt.toUpperCase()).fontSize(16);
      }
    }
    .width('100%')
    .padding({
      left: 15,
      right: 15
    })
    .margin({ bottom: 5 });

    Column() {
      if (this.selectPhotoCount > 0) {
        Image(this.selcteUris[0])
          .objectFit(ImageFit.Contain)
          .onComplete((event) => {
            if (event) {
              this.beforeCompressImgSize = event?.width.toString() + '*' + event?.height.toString();
            }
          });
        Text(this.beforeCompressImgSize)
          .fontSize(13)
          .opacity(0.8)
          .margin(10);
      } else {
        Image($r('app.media.image_compression_add_photo')) // 此处仅为样例，请开发者更换为可用图片
          .objectFit(ImageFit.None)
          .height(50)
          .margin({ top: 30, bottom: 10 });
        Text('点击添加图片')
          .fontSize(14);
      }
    }
    .onClick(() => {
      // 初始化
      this.afterCompressionSize = '';
      this.outputFormatIndex = 0;
      // 拉起图库选择图片
      this.compressionMethod.selectPhotoFromAlbum();
    })
    .width('70%')
    .height(150)
    .backgroundColor(Color.White)
    .padding(5)
    .margin({ bottom: 15 })
    .borderRadius(5);

    Row() {
      Text('压缩后：')
        .fontWeight(FONT_WEIGHT)
        .fontSize(16);
      Text(this.afterCompressionSize)
        .fontWeight(FONT_WEIGHT)
        .fontSize(20)
        .fontColor('#ff0e9eff');
      if (this.afterCompressionSize !== '') {

        Text('kb  格式：')
          .fontSize(16);
        Text(this.showCompressFormat)
          .fontSize(16);
      }
    }
    .width('100%')
    .padding({
      left: 15,
      right: 15
    })
    .margin({ top: 10, bottom: 5 });

    Column() {
      if (this.afterCompressionSize !== '') {
        Image(this.showPixelMap)
          .objectFit(ImageFit.Contain)
          .onComplete((event) => {
            if (event) {
              this.afterCompressImgSize = event?.width.toString() + '*' + event?.height.toString();
              emitter.emit('ImageCompression3', {
                data: {
                  afterCompressImgSize: this.afterCompressImgSize
                }
              });
            }
          });
        Text(this.afterCompressImgSize)
          .fontSize(13)
          .opacity(0.8)
          .margin(10);
      }
    }
    .width('70%')
    .height(150)
    .backgroundColor(Color.White)
    .padding(5)
    .margin({ bottom: 20 })
    .borderRadius(5);
  }

  /**
   * 获取当前选中的输出格式
   * @returns selectFormat 格式名
   */
  getSelectFormat(): string {
    let selectFormat: string = '';
    switch (this.outputFormatIndex) {
      case 0: // 原格式
        selectFormat = this.beforeCompressFmt.toUpperCase();
        break;
      case 1: // PNG
        selectFormat = 'PNG';
        break;
      case 2: // JPEG
        selectFormat = 'JPEG';
        break;
      case 3: // WEBP
        selectFormat = 'WEBP';
        break;
    }
    return selectFormat;
  }

  /**
   * 输出格式菜单
   */
  @Builder
  outputFormatMenu() {
    Column() {
      ForEach(this.outputFormat, (item: string, index: number) => {
        Column() {
          Flex({
            direction: FlexDirection.Row,
            justifyContent: FlexAlign.SpaceBetween,
            alignItems: ItemAlign.Center
          }) {
            Text(item)
              .fontSize(15);
            Image($r('app.media.image_compression_ok'))// 此处仅为样例，请开发者更换为可用图片
              .visibility(this.outputFormatIndex === index ? Visibility.Visible : Visibility.Hidden)
              .width(20)
              .height(20);
          }
          .height(48);

          Divider()
            .visibility(index !== 3 ? Visibility.Visible : Visibility.Hidden)
            .width('100%');
        }
        .width(80)
        .onClick(() => {
          this.outputFormatIndex = index;
          switch (item) {
            case '原格式':
              this.afterCompressFmt = this.beforeCompressFmt;
              AppStorage.setOrCreate('outputCompressFmt', this.afterCompressFmt);
              break;
            case 'PNG':
              this.afterCompressFmt = 'PNG';
              AppStorage.setOrCreate('outputCompressFmt', this.afterCompressFmt);
              break;
            case 'JPEG':
              this.afterCompressFmt = 'JPEG';
              AppStorage.setOrCreate('outputCompressFmt', this.afterCompressFmt);
              break;
            case 'WEBP':
              this.afterCompressFmt = 'WEBP';
              AppStorage.setOrCreate('outputCompressFmt', this.afterCompressFmt);
              break;
          }
        });
      }, (item: string) => item);
    }
    .borderRadius(10)
    .backgroundColor(Color.White)
    .width(100)
    .focusable(false);
  }

  @Builder
  outputFormatSet() {
    Row() {
      Text('输出格式：')
        .fontSize(16)
        .fontWeight(FONT_WEIGHT);
      Blank();
      Row() {
        Text(this.outputFormat[this.outputFormatIndex])
          .fontSize(15)
          .opacity(0.8);

        Image($r('app.media.image_compression_spinner'))// 此处仅为样例，请开发者更换为可用图片
          .width(22)
          .height(16)
          .opacity(0.5)
          .margin({
            left: 8,
            right: 8
          });
      }
      .id('outputFormat')
      .bindMenu(this.outputFormatMenu(), { placement: Placement.Top });
    }
    .width('100%')
    .height(48)
    .borderRadius(10)
    .backgroundColor(Color.White)
    .padding({
      left: 15,
      right: 15,
      top: 10,
      bottom: 10
    });
  }

  /**
   * 保存到相册
   */
  @Builder
  compressAndSave() {
    Row({ space: SPACE_THIRTY }) {
      SaveButton({ text: SaveDescription.SAVE_IMAGE, buttonType: ButtonType.Capsule })
        .height(40)
        .borderRadius(12)
        .onClick(async () => {
          if (this.afterCompressionSize === '') {
            this.context.showAlertDialog({
              message: '请先压缩',
              alignment: DialogAlignment.Center
            });
            return;
          }
          if (this.showCompressFormat == this.convertFormat || this.showCompressFormat == this.getSelectFormat()) {
            await this.compressionMethod.saveImageToAlbum();

          } else {
            this.context.showAlertDialog({
              message: '请先压缩该输出格式后再试',
              alignment: DialogAlignment.Center
            });
            return;
          }

        });
    };
  }

  build() {
    Column({ space: SPACE_SIX }) {
      this.displayImage();
      // 输出格式
      this.outputFormatSet();
      Button('质量压缩')
        .onClick(() => {
          if (this.selectPhotoCount <= 0) {
            this.context.showAlertDialog({
              message: '请先添加待压缩的图片',
              alignment: DialogAlignment.Center
            });
            return;
          }
          // 质量压缩
          this.qualityCompressionMethod(50);
          this.promptAction.showToast({ message: '质量压缩完成！' });

        });
      Button('尺寸压缩')
        .onClick(() => {
          if (this.selectPhotoCount <= 0) {
            this.context.showAlertDialog({
              message: '请先添加待压缩的图片',
              alignment: DialogAlignment.Center
            });
            return;
          }
          // 尺寸压缩
          this.sizeCompressionMethod(50);
          this.promptAction.showToast({ message: '尺寸压缩完成！' });
        });
      Button('智能压缩')
        .onClick(async () => {
          if (this.selectPhotoCount <= 0) {
            this.context.showAlertDialog({
              message: '请先添加待压缩的图片',
              alignment: DialogAlignment.Center
            });
            return;
          }
          // 智能压缩
          const intelligentCompressionMethodCallBack =
            await this.compressionMethod.intelligentCompressionMethod(true, 600, 10, 80);
          this.showPixelMap = intelligentCompressionMethodCallBack[0];
          this.savePixelMap = intelligentCompressionMethodCallBack[1];
          this.afterCompressionSize = intelligentCompressionMethodCallBack[2];
          this.showCompressFormat = intelligentCompressionMethodCallBack[3];
        });

      Button('格式转换')
        .align(Alignment.Center)
        .onClick(async () => {
          if (this.selectPhotoCount <= 0) {
            this.context.showAlertDialog({
              message: '请先添加待压缩的图片',
              alignment: DialogAlignment.Center
            });
            return;
          }
          // 传入需要转换的格式
          const formatConversionMethod = await this.compressionMethod.formatConversionMethod('JPEG');
          this.showPixelMap = formatConversionMethod[0];
          this.savePixelMap = formatConversionMethod[1];
          this.afterCompressionSize = formatConversionMethod[2];
          this.showCompressFormat = formatConversionMethod[3];
        });
      // 保存到相册
      this.compressAndSave();
    }
    .padding({
      top: 10,
      left: 20,
      right: 20,
      bottom: 10
    })
    .backgroundColor('#99e3e3e3')
    .height('100%')
    .width('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```

compression.ets：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { PromptAction } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

const TAG = 'IMAGE_COMPRESSION';
const BYTE_CONVERSION: number = 1024; // 字节转换
const IMAGE_QUALITY_ZERO: number = 0; // 图片质量0
const IMAGE_QUALITY_HUNDRED: number = 100; // 图片质量100

export class CompressionMethod {
  private uris: Array<string> = []; // 保存图库选择的结果uri
  private photoCount: number = 0; // 选择图片的个数
  private beforeCompressFmt: string = ''; // 压缩前图片格式
  private afterCompressFmt: string = ''; // 压缩后图片格式
  private beforeCompressByteLength: number = 0; // 压缩前图片字节长度
  private sizeFlag: boolean = false; // 是否尺寸缩模式
  private savePixelMap: image.PixelMap | undefined = undefined; // 保存压缩后的图片
  private imageQuality: number = 100; // 图片压缩质量
  private showPixelMap: image.PixelMap | undefined = undefined; // 页面上显示压缩后的图片
  private afterCompressionSize: string = ''; // 压缩后的图片大小,单位kb
  private showCompressFormat: string = ''; // 在页面上显示压缩后的图片格式
  private qualityCompression: boolean = true; // 是否质量压缩模式
  private intelligentCompressionQuality: number = 0; // 自动模式保存图片的质量
  promptAction: PromptAction = (AppStorage.get('context') as UIContext).getPromptAction();

  /**
   * 拉起图库选择图片
   */
  async selectPhotoFromAlbum() {
    // 创建图库选项实例
    const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    // 设置选择的媒体文件类型为Image
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    // 设置选择媒体文件的最大数目
    photoSelectOptions.maxSelectNumber = 1;
    // 创建图库选择器实例
    const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
    // 调用photoViewPicker.select()接口拉起图库界面进行图片选择，图片选择成功后，返回photoSelectResult结果集。
    photoViewPicker.select(photoSelectOptions).then((photoSelectResult) => {
      // select返回的uri权限是只读权限，需要将uri写入全局变量@State中即可进行读取文件数据操作。
      this.uris = photoSelectResult.photoUris;
      AppStorage.setOrCreate('uris', this.uris);
      this.photoCount = this.uris.length;
      AppStorage.setOrCreate('photoCount', this.photoCount);
      if (this.photoCount > 0) {
        const ALBUM_PATH: string = photoSelectResult.photoUris[0];
        // 找到最后一个点（.）的索引位置
        let lastDotIndex = ALBUM_PATH.lastIndexOf('.');
        // 使用slice方法从最后一个点之后的位置开始截取字符串到末尾
        this.beforeCompressFmt =
          ALBUM_PATH.slice(lastDotIndex + 1) === 'jpg' ? 'jpeg' : ALBUM_PATH.slice(lastDotIndex + 1);
        AppStorage.setOrCreate('beforeCompressFmt', this.beforeCompressFmt);
        this.afterCompressFmt = this.beforeCompressFmt.toUpperCase();
        AppStorage.setOrCreate('afterCompressFmt', this.afterCompressFmt);
        // 读取选择图片的buffer
        const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
        // 获取选择图片的字节长度
        this.beforeCompressByteLength = fs.statSync(file.fd).size;
        AppStorage.setOrCreate('beforeCompressByteLength', this.beforeCompressByteLength);
        fs.closeSync(file);
      }
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `PhotoViewPicker.select failed :, error code: ${err.code}, message: ${err.message}.`);
    });
  }

  /**
   * packing压缩
   * @param sourcePixelMap 原始待压缩图片的PixelMap
   * @param imageQuality 图片质量参数
   * @param packingFormat 目标格式。当前只支持"image/jpeg"、"image/webp" 和 "image/png"
   * @returns data 返回压缩后的图片数据
   */
  async packing(sourcePixelMap: image.PixelMap, imageQuality: number, packingFormat: string): Promise<ArrayBuffer> {
    const imagePackerApi = image.createImagePacker();
    const packOpts: image.PackingOption = { format: 'image/' + packingFormat, quality: imageQuality };
    const data: ArrayBuffer = await imagePackerApi.packToData(sourcePixelMap, packOpts);
    return data;
  }

  /**
   * 压缩
   */
  async compressionMethod(imageScaleVal: number,
    imageQualityVal: number): Promise<[PixelMap, PixelMap, string, string]> {
    const ALBUM_PATH: string = this.uris[0];
    const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
    let buffer = new ArrayBuffer(fs.statSync(file.fd).size);
    fs.readSync(file.fd, buffer);
    fs.closeSync(file);
    const decodingOptions: image.DecodingOptions = { editable: true };
    const imageSource: image.ImageSource = image.createImageSource(buffer);
    return new Promise<[PixelMap, PixelMap, string, string]>((resolve) => {
      imageSource.createPixelMap(decodingOptions).then(async (originalPixelMap: image.PixelMap) => {
        if (AppStorage.get('sizeFlag') != undefined) {
          this.sizeFlag = AppStorage.get('sizeFlag')!;
        }
        if (this.sizeFlag) {
          // 使用scale对图片进行缩放。入参分别为图片宽高的缩放倍数
          await originalPixelMap.scale(imageScaleVal / 100, imageScaleVal / 100);
          // savePixelMap用于把压缩后的图片保存到图库时使用。由于保存图片时调用的packToFile内部会做类似packing的处理，所以这里只保存scale缩放尺寸后的PixelMap。
          this.savePixelMap = originalPixelMap;
          this.imageQuality = imageScaleVal;
        }
        // savePixelMap用于把压缩后的图片保存到图库时使用。
        this.savePixelMap = originalPixelMap;
        if (AppStorage.get('outputCompressFmt') != undefined) {
          this.afterCompressFmt = AppStorage.get('outputCompressFmt')!;
        }

        // packing压缩图片
        let compressedImageData: ArrayBuffer =
          await this.packing(originalPixelMap, imageQualityVal, this.afterCompressFmt);
        // 压缩后的ArrayBuffer数据转PixelMap
        let imageSource = image.createImageSource(compressedImageData);
        let opts: image.DecodingOptions = { editable: true };
        // showPixelMap用于显示压缩后的图片
        const pixelMap: image.PixelMap = await imageSource.createPixelMap(opts);
        this.showPixelMap = pixelMap;
        // showCompressFormat用于显示压缩后的图片格式
        this.showCompressFormat = this.afterCompressFmt;
        // 显示估算packing压缩后的图片大小。该图片在内存中作为ArrayBuffer数据的压缩后大小，这一数值并不直接等同于该图片在最终保存到相册时的实际文件大小。
        this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
        resolve([this.showPixelMap, this.savePixelMap, this.afterCompressionSize, this.afterCompressFmt]);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG, `Failed to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
      });

    });
  }

  /**
   * packing二分方式循环压缩
   * @param sourcePixelMap 原始待压缩图片的PixelMap
   * @param compressedImageData 图片压缩的ArrayBuffer
   * @param maxCompressedImageByte 压缩目标图像字节长度
   * @param minBisectUnit 最小二分单位
   */
  async packingImage(sourcePixelMap: image.PixelMap, compressedImageData: ArrayBuffer, maxCompressedImageByte: number,
    minBisectUnit: number) {
    let saveImageQuality: number = 0;
    const DICHOTOMY_ACCURACY = minBisectUnit;
    // 图片质量参数范围为0-100，这里以minBisectUnit为最小二分单位创建用于packing二分图片质量参数的数组。
    const packingArray: number[] = [];
    // 性能知识点: 如果对图片压缩质量要求不高，建议调高minBisectUnit（对应‘packing最小二分单位’），减少循环，提升packing压缩性能。
    for (let i = 0; i <= 100; i += DICHOTOMY_ACCURACY) {
      packingArray.push(i);
    }
    let left = 0; // 定义二分搜索范围的左边界
    let right = packingArray.length - 1; // 定义二分搜索范围的右边界
    const AFTER_COMPRESS_FMT = this.afterCompressFmt;
    // 二分压缩图片
    while (left <= right) {
      const mid = Math.floor((left + right) / 2); // 定义二分搜索范围的中间位置
      saveImageQuality = packingArray[mid]; // 获取二分中间位置的图片质量值
      // 根据传入的图片质量参数进行packing压缩，返回压缩后的图片文件流数据。
      compressedImageData = await this.packing(sourcePixelMap, saveImageQuality, AFTER_COMPRESS_FMT);
      // 判断查找一个尽可能接近但不超过压缩目标的压缩大小
      if (compressedImageData.byteLength <= maxCompressedImageByte) {
        // 二分目标值在右半边，继续在更高的图片质量参数（即mid + 1）中搜索
        left = mid + 1;
        // 判断mid是否已经二分到最后，如果二分完了，退出
        if (mid === packingArray.length - 1) {
          break;
        }
        // 获取下一次二分的图片质量参数（mid+1）压缩的图片文件流数据
        compressedImageData = await this.packing(sourcePixelMap, packingArray[mid + 1], AFTER_COMPRESS_FMT);
        // 判断用下一次图片质量参数（mid+1）压缩的图片大小是否大于指定图片的压缩目标大小。如果大于，说明当前图片质量参数（mid）压缩出来的
        // 图片大小最接近指定图片的压缩目标大小。传入当前图片质量参数mid，得到最终目标图片压缩数据。
        if (compressedImageData.byteLength > maxCompressedImageByte) {
          compressedImageData = await this.packing(sourcePixelMap, packingArray[mid], AFTER_COMPRESS_FMT);
          break;
        }
      } else {
        // 目标值不在当前范围的右半部分，将搜索范围的右边界向左移动，以缩小搜索范围并继续在下一次迭代中查找左半部分。
        right = mid - 1;
      }
    }
    // 保存最终压缩的图片质量，用于保存到图库时使用
    this.intelligentCompressionQuality = saveImageQuality;
    // ArrayBuffer转PixelMap，并保存相关数据
    let imageSource = image.createImageSource(compressedImageData);
    let opts: image.DecodingOptions = { editable: true };
    this.showPixelMap = await imageSource.createPixelMap(opts);
    this.savePixelMap = sourcePixelMap;
    this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
  }

  /**
   * 优先压缩图片尺寸
   * @param sourcePixelMap 原始待压缩图片的PixelMap
   * @param maxCompressedImageSize 指定图片的压缩目标大小
   * @param quality
   */
  async scalePriorityCompress(sourcePixelMap: image.PixelMap, maxCompressedImageSize: number, quality: number) {
    let compressedImageData: ArrayBuffer = await this.packing(sourcePixelMap, quality, this.afterCompressFmt);
    // 如果调整过最低图片质量，先计算最低图片质量是否满足要求。如果设定的最低图片质量已经满足目标大小，则直接返回
    if (quality !== IMAGE_QUALITY_HUNDRED &&
      (compressedImageData.byteLength <= maxCompressedImageSize * BYTE_CONVERSION)) {
      // 保存最终压缩的图片质量，用于保存到图库时使用
      this.intelligentCompressionQuality = quality;
      // ArrayBuffer转PixelMap，并保存图片相关数据
      let imageSource = image.createImageSource(compressedImageData);
      let opts: image.DecodingOptions = { editable: true };
      this.showPixelMap = await imageSource.createPixelMap(opts);
      this.savePixelMap = sourcePixelMap;
      this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
      // 更新显示压缩后的图片格式
      this.showCompressFormat = this.afterCompressFmt;
      return;
    }
    // scale压缩图片尺寸。采用while循环每次递减0.4，最终查找到最接近指定图片压缩目标大小的缩放倍数的图片压缩数据。
    let imageScale = 1; // 定义图片宽高的缩放倍数，1表示原比例。
    const REDUCE_SCALE = 0.5;
    const AFTER_COMPRESS_FMT = this.afterCompressFmt;
    // 判断压缩后的图片大小是否大于指定图片的压缩目标大小，如果大于，继续降低缩放倍数压缩。
    while (compressedImageData.byteLength > maxCompressedImageSize * BYTE_CONVERSION) {
      if (imageScale > 0) {
        // 性能知识点: 由于scale会直接修改图片PixelMap数据，所以不适用二分查找scale缩放倍数。这里采用循环递减0.4倍缩放图片，
        // 来查找确定最适合的缩放倍数。如果对图片压缩质量要求不高，建议调高每次递减的缩放倍数，减少循环，提升scale压缩性能。
        imageScale = imageScale - REDUCE_SCALE; // 每次缩放倍数减
        // 使用scale对图片尺寸进行缩放
        await sourcePixelMap.scale(imageScale, imageScale);
        // packing压缩
        compressedImageData = await this.packing(sourcePixelMap, quality, AFTER_COMPRESS_FMT);
      } else {
        // imageScale缩放倍数小于等于0时，没有意义，结束压缩。
        break;
      }
    }
    this.intelligentCompressionQuality = quality;
    let imageSource = image.createImageSource(compressedImageData);
    let opts: image.DecodingOptions = { editable: true };
    this.showPixelMap = await imageSource.createPixelMap(opts);
    this.savePixelMap = sourcePixelMap;
    this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
    this.showCompressFormat = this.afterCompressFmt;
    // 可能会存在scale每次缩小倍数设置过大，导致无法压缩到图片压缩目标大小，弹窗提示
    if (compressedImageData.byteLength > maxCompressedImageSize * BYTE_CONVERSION) {
      let uiContext = AppStorage.get('context') as UIContext;
      uiContext.showAlertDialog({
        message: '当前在设置的scale每次缩小倍数条件下，无法压缩到目标大小，建议调低scale每次缩小倍数后再试',
        alignment: DialogAlignment.Center
      });
    }
  }

  /**
   * 优先压缩图片质量
   * @param sourcePixelMap 原始待压缩图片的PixelMap
   * @param maxCompressedImageSize 指定图片的压缩目标大小
   */
  async qualityPriorityCompress(sourcePixelMap: image.PixelMap, maxCompressedImageSize: number, minBisectUnit: number) {
    let compressedImageData: ArrayBuffer =
      await this.packing(sourcePixelMap, IMAGE_QUALITY_ZERO, this.afterCompressFmt);
    // 先判断图片质量参数设置最低0能否满足目标大小。如果能满足目标大小，则直接使用packing二分图片质量。如果不满足，则质量参数固定为0，进行scale尺寸压缩
    if (compressedImageData.byteLength <= maxCompressedImageSize * BYTE_CONVERSION) {
      // 满足目标大小，直接使用packing二分
      await this.packingImage(sourcePixelMap, compressedImageData, maxCompressedImageSize * BYTE_CONVERSION,
        minBisectUnit);
    } else {
      // 不满足目标大小，质量参数设置为0，再进行scale尺寸压缩
      await this.scalePriorityCompress(sourcePixelMap, maxCompressedImageSize, IMAGE_QUALITY_ZERO);
    }
    // 更新显示压缩后的图片格式
    this.showCompressFormat = this.afterCompressFmt;
  }

  /**
   * 图片压缩
   * @param sourcePixelMap：原始待压缩图片的PixelMap对象
   * @param maxCompressedImageSize：指定图片的压缩目标大小，单位kb
   */
  async compressedImage(isqualityCompression: boolean, sourcePixelMap: image.PixelMap, maxCompressedImageSize: number,
    minBisectUnit: number, minQuality: number): Promise<void> {
    this.qualityCompression = isqualityCompression;
    // 判断是优先压缩质量还是优先压缩尺寸
    if (isqualityCompression) {
      // 优先压缩质量
      await this.qualityPriorityCompress(sourcePixelMap, maxCompressedImageSize, minBisectUnit);
    } else {
      // 优先压缩尺寸
      await this.scalePriorityCompress(sourcePixelMap, maxCompressedImageSize, minQuality);
    }
  }

  /**
   * 智能压缩
   * @param qualityCompression：是否质量优先
   * @param maxCompressedImageSize 指定图片压缩目标大小，单位kb
   * @param minBisectUnit packing最小二分单位
   * @param minQuality 最低图片质量
   */
  intelligentCompressionMethod(qualityCompression: boolean, maxCompressedImageSize: number, minBisectUnit: number,
    minQuality: number): Promise<[PixelMap, PixelMap, string, string]> {
    // 获取图库中选择的图片路径
    const ALBUM_PATH: string = this.uris[0];
    const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
    let buffer: ArrayBuffer = new ArrayBuffer(fs.statSync(file.fd).size);
    // 读取图片到buffer
    fs.readSync(file.fd, buffer);
    fs.closeSync(file);
    // 通过缓冲区创建图片源实例
    const imageSource: image.ImageSource = image.createImageSource(buffer);
    // 设置解码参数DecodingOptions，解码获取PixelMap图片对象。
    const decodingOptions: image.DecodingOptions = {
      editable: true, // 是否可编辑。当取值为false时，图片不可二次编辑，如crop等操作将失败。
    };
    return new Promise<[PixelMap, PixelMap, string, string]>((resolve, reject) => {
      imageSource.createPixelMap(decodingOptions).then(async (originalPixelMap: image.PixelMap) => {
        try {
          if (AppStorage.get('outputCompressFmt') != undefined) {
            this.afterCompressFmt = AppStorage.get('outputCompressFmt')!;
          }
          // 压缩图片
          await this.compressedImage(qualityCompression, originalPixelMap, maxCompressedImageSize, minBisectUnit,
            minQuality);
          this.promptAction.showToast({ message: '智能压缩完成！' });
          resolve([this.showPixelMap!, this.savePixelMap!, this.afterCompressionSize, this.showCompressFormat]);
        } catch (err) {
          hilog.error(0x0000, TAG, `Failed to compress image, error code: ${err.code}, message: ${err.message}.`);
          reject(err);
        }
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG, `Failed to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
        reject(err);
      });
    });
  }

  /**
   * 格式转换压缩
   */
  formatConversionMethod(format: string): Promise<[PixelMap, PixelMap, string, string]> {
    this.afterCompressFmt = format;
    AppStorage.setOrCreate('convertFormat', format);
    const ALBUM_PATH: string = this.uris[0];
    const file = fs.openSync(ALBUM_PATH, fs.OpenMode.READ_ONLY);
    let buffer = new ArrayBuffer(fs.statSync(file.fd).size);
    fs.readSync(file.fd, buffer);
    fs.closeSync(file);
    const decodingOptions: image.DecodingOptions = { editable: true };
    const imageSource: image.ImageSource = image.createImageSource(buffer);
    return new Promise<[PixelMap, PixelMap, string, string]>((resolve, reject) => {
      imageSource.createPixelMap(decodingOptions).then(async (pixelMap: image.PixelMap) => {
        this.savePixelMap = pixelMap;
        // packing压缩图片
        let compressedImageData: ArrayBuffer =
          await this.packing(pixelMap, this.imageQuality, this.afterCompressFmt);
        // 压缩后的ArrayBuffer数据转PixelMap
        let imageSource = image.createImageSource(compressedImageData);
        let opts: image.DecodingOptions = { editable: true };
        // showPixelMap用于显示压缩后的图片
        this.showPixelMap = await imageSource.createPixelMap(opts);
        // showCompressFormat用于显示压缩后的图片格式
        this.showCompressFormat = this.afterCompressFmt;
        // 显示估算packing压缩后的图片大小。该图片在内存中作为ArrayBuffer数据的压缩后大小，这一数值并不直接等同于该图片在最终保存到相册时的实际文件大小。
        this.afterCompressionSize = (compressedImageData.byteLength / BYTE_CONVERSION).toFixed(1);
        this.promptAction.showToast({ message: '格式转换压缩完成！' });
        resolve([this.showPixelMap, this.savePixelMap, this.afterCompressionSize, this.afterCompressFmt]);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG, `Failed to create PixelMap, error code: ${err.code}, message: ${err.message}.`);
        reject(err);
      });
    });
  }

  /**
   * 保存图片到图库
   * @returns
   */
  async saveImageToAlbum(): Promise<void> {
    // 获取相册管理模块的实例
    const HELPER =
      photoAccessHelper.getPhotoAccessHelper((AppStorage.get('context') as UIContext).getHostContext() as common.UIAbilityContext);
    // 指定待创建的文件类型、后缀和创建选项，创建图片资源
    const URI = await HELPER.createAsset(photoAccessHelper.PhotoType.IMAGE, this.afterCompressFmt);
    let file = await fs.open(URI, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    let imagePacker = image.createImagePacker();
    let packOpts: image.PackingOption = {
      format: 'image/' + this.afterCompressFmt,
      quality: this.qualityCompression ? this.intelligentCompressionQuality : this.imageQuality
    };
    // 指定打包参数，将PixelMap图片源编码后直接打包进文件
    imagePacker.packToFile(this.savePixelMap, file.fd, packOpts, async (err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, TAG, `Failed to pack the image to file, error code: ${err.code}, message: ${err.message}.`);
      } else {
        try {
          this.promptAction.showToast({ message: '已保存至相册！' });
        } catch (error) {
          console.error(`showToast args error is ${error}`);
        }
      }
      await fs.close(file.fd).catch(() => {
        console.info('close file succeed');
      }).finally(() => {
        imagePacker.release();
      });
    });
  }
}
```

EntryAbility.ets：

```ts
import { ConfigurationConstant, UIAbility} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      let context = windowStage.getMainWindowSync().getUIContext();
      AppStorage.setOrCreate('context', context);
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

## 总结

HarmonyOS的图片处理生态，以PixelMap为统一数据核心，以ImagePacker和ImageSource为关键接口，构建了一个从“存储”到“内存”再到“渲染”的全链路能力矩阵。开发者可以参考以下压缩方式选择矩阵表根据自己的需求选择不同的压缩方案。

| 压缩方式 | 适用场景 | 目标文件大小 | 质量要求 | 推荐参数 |
| --- | --- | --- | --- | --- |
| 质量压缩 | 社交分享、即时通讯 | 中等 (100-500KB) | 中等 | quality: 70-80 |
| 尺寸压缩 | 头像、缩略图、列表 | 小 (<100KB) | 中低 | maxSize: 200-800px |
| 智能压缩 | 上传限制、存储优化 | 精确控制 | 自适应 | targetKB: 200 |
| 格式转换 | 现代App、Web应用 | 中等 | 高（同等质量） | quality: 75-85 |
