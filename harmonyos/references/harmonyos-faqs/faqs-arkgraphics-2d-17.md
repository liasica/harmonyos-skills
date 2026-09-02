---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-17
title: 如何实现多张图片的拼接
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何实现多张图片的拼接
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:23+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:3b9c0bb2cfe82c722c7f56035e51eb15e8d99d4ebf3ffe3f12c80a73de1158d2
---

## 问题现象

在图片处理中，如何将不同图片进行拼接，如长图图片的合成。

## 背景知识

对图片进行拼接绘制可以使用Canvas或writePixels进行绘制，两者的使用优劣对比如下：

* Canvas组件具有自绘制的能力，目前有[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)/[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)和[DrawingRenderingContext](../harmonyos-references/ts-drawingrenderingcontext.md)两套API，应用使用两套绘制API绘制的内容都可以在绑定的Canvas组件上显示。
* 对于绘画逻辑简单，但使用图片量级大对性能要求高的场景，可以通过图片编解码直接对图片像素数据进行操作，并用writePixels获取指定区域像素信息，主要实现流程和步骤参考[图形绘制与显示开发概述](../harmonyos-guides/graphic-drawing-overview.md)。

| 方法 | 优点 | 缺点 |
| --- | --- | --- |
| Canvas | 简单实现，支持快速对图像进行裁剪等操作，支持复杂图形的绘制。 | 涉及多次绘图操作时性能显著降低，内存占用较高。 |
| writePixels | 高性能图像处理，可以减少内存开销并提升效率。 | 开发及维护难度更大，仅针对图片像素进行操作，需要手动管理像素数据。 |

## 解决方案

**方案一**：使用Canvas实现长图图片的绘制。

获取拼接图片的宽高信息，通过在Canvas画布上使用[drawImage](../harmonyos-references/ts-components-canvas-common-method.md#drawimage)绘制，将第二张图片的绘制初始坐标根据第一张图片的宽高信息设置，即可实现将图片横向拼接或竖向拼接，最后使用[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)将画布绘制的图像创建为新的PixelMap。常见开发场景如下：

* 合成多张图片，并添加一定的图标装饰，常用于社交通信。
* 相机长图拍摄，每隔一段时间或一定距离获取当前预览帧图片，于离屏画布上实现长图片绘制。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/T-eZUH4uT5umevc9C70jZw/zh-cn_image_0000002628393350.png "点击放大")

绘制图片会根据drawImage设置的图片绘制区域进行等比例缩放，常用的图片像素处理格式有ImageBitmap和PixelMap，两者的使用优劣对比如下表所示：

| 方法 | 优点 | 缺点 |
| --- | --- | --- |
| ImageBitmap | 可直接用于绘图和图像预览，支持跨平台使用。 | 不可修改像素，处理能力有限。 |
| PixelMap | 可以对图片像素数据进行修改，适用于自定义图像处理逻辑。 | 内存占用较高，性能相对较慢。 |

**说明** 

ImageBitmap对象仅接受实际文件路径（如ets/common/test.jpg），因为/resource资源目录在编译时会被打包进应用中，其中的资源并没有实际路径，所以对于放在/resources资源目录下的图片需要使用resourceManager将图片创建为可操作的PixelMap对象。

使用ImageBitmap在Canvas上绘制长图的参考代码如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct CanvasDrawing {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column({ space: 30 }) {
      Button('点击选择图片并使用Canvas进行绘制')
        .onClick(() => {
          this.selectPhoto();
        })
      Canvas(this.context)
        .width('90%')
        .height('90%')
        .backgroundColor('#F1F3F5')
        .borderRadius(10)
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
  }

  async selectPhoto() {
    this.context.clearRect(0, 0, 800, 800);
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let photoPickerOptions = new photoAccessHelper.PhotoSelectOptions();
    photoPickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoPickerOptions.maxSelectNumber = 2;
    let photoSelectResult = await photoPicker.select(photoPickerOptions);
    let img: ImageBitmap = new ImageBitmap(photoSelectResult.photoUris[0]);
    let img2: ImageBitmap = new ImageBitmap(photoSelectResult.photoUris[1]);
    let ratio: number = img.height / img.width;
    let offCanvas: OffscreenCanvas = new OffscreenCanvas(800, 800);
    let height: number = 200 * ratio > 300 ? 300 : 300 * ratio;
    let width: number = 200 * ratio > 300 ? 300 / ratio : 300;
    let offContext = offCanvas.getContext('2d', this.settings);
    offContext.drawImage(img, 0, 0, width, height);
    // 根据第一张图片绘制坐标决定第二张图片的初始坐标
    offContext.drawImage(img2, 0, height, width, height);
    let image = offCanvas.transferToImageBitmap();
    this.context.transferFromImageBitmap(image);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/8RbLVIAMRAW5AkBtXWHWMg/zh-cn_image_0000002628553232.png "点击放大")

离屏绘制的相关代码如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct OffScreenDrawing {
  @State ima: PixelMap | undefined = undefined;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column({ space: 30 }) {
      Button('点击选择图片并进行离屏绘制')
        .onClick(() => {
          this.selectPhoto();
        })
      Image(this.ima)
        .width(200)
        .objectFit(ImageFit.Contain)
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
  }

  async selectPhoto() {
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let photoPickerOptions = new photoAccessHelper.PhotoSelectOptions();
    photoPickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoPickerOptions.maxSelectNumber = 2;
    let photoSelectResult = await photoPicker.select(photoPickerOptions);
    let img: ImageBitmap = new ImageBitmap(photoSelectResult.photoUris[0]);
    let img2: ImageBitmap = new ImageBitmap(photoSelectResult.photoUris[1]);
    let ratio: number = img.height / img.width;
    let offCanvas: OffscreenCanvas = new OffscreenCanvas(800, 800);
    let height: number = 200 * ratio > 300 ? 300 : 300 * ratio;
    let width: number = 200 * ratio > 300 ? 300 / ratio : 300;
    let offContext = offCanvas.getContext('2d', this.settings);
    offContext.drawImage(img, 0, 0, width, height);
    // 根据第一张图片绘制坐标决定第二张图片的初始坐标
    offContext.drawImage(img2, 0, height, width, height);
    // 获取离屏绘制的内容
    this.ima =
      offContext.getPixelMap(0, 0, width, 2 * height);
    let image = offCanvas.transferToImageBitmap();
    this.context.transferFromImageBitmap(image);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/bB9WPtIVS3aKZBkKGnPB9w/zh-cn_image_0000002658912551.png "点击放大")

对于相册图片或沙箱图片，可以在获取图片的ArrayBuffer数据后，创建PixelMap实例绘制长图。参考代码如下：

```ts
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct AlbumImageData {
  @State pixelMap: PixelMap | null = null;
  @State albumPath: string = '';
  @State photoSize: number = 0;

  build() {
    Stack() {
      Image(this.pixelMap)
        .objectFit(ImageFit.Contain)
      Column() {
        Button('点击选择图片并进行拼接')
          .margin({ bottom: 40 })
          .onClick(() => {
            this.selectPhotos();
          })
      }
      .height('100%')
      .justifyContent(FlexAlign.End)
    }
    .width('100%')
    .height('100%')
  }

  async selectPhotos() {
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let photoPickerOptions = new photoAccessHelper.PhotoSelectOptions();
    photoPickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoPickerOptions.maxSelectNumber = 1;
    let photoSelectResult = await photoPicker.select(photoPickerOptions);
    this.albumPath = photoSelectResult.photoUris[0];
    const file = fs.openSync(this.albumPath, fs.OpenMode.READ_ONLY);
    this.photoSize = fs.statSync(file.fd).size;
    let arrayBuffer = new ArrayBuffer(this.photoSize);
    fs.readSync(file.fd, arrayBuffer);
    fs.closeSync(file);
    let imageSource: image.ImageSource = image.createImageSource(arrayBuffer);
    imageSource.getImageInfo((err, value) => {
      if (err) {
        console.error(`getImageInfo error: ${err}`);
        return;
      }
      let imgWidth: number = this.getUIContext().px2vp(value.size.width);
      let imgHeight: number = this.getUIContext().px2vp(value.size.height);
      // 图片距离左右边缘的距离
      let offset: number = 20;
      let opts: image.DecodingOptions =
        { editable: true, desiredSize: { height: value.size.height, width: value.size.width } };
      imageSource.createPixelMap(opts, (err, pixelMap) => {
        if (err) {
          console.error(`Create pixelMap error: ${err.code}`);
          return;
        }
        let offScreenCanvas = new OffscreenCanvas(imgWidth + offset * 2, imgHeight * 2);
        let OffScreenContext = offScreenCanvas.getContext('2d');
        OffScreenContext.drawImage(pixelMap, offset, 0);
        OffScreenContext.drawImage(pixelMap, offset, imgHeight);
        // 获取新的pixelMap，宽为原图的宽度加间距，高为将图片上下拼接后的高度
        this.pixelMap = OffScreenContext.getPixelMap(0, 0, imgWidth + offset * 2, imgHeight * 2);
      });
      // 释放imageSource资源
      imageSource.release().then(() => {
        console.info('Succeeded in releasing the image source instance.');
      }).catch((error: BusinessError) => {
        console.error(`Failed to release the image source instance.code ${error.code}, message is ${error.message}`);
      });
    });
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/xKFuoNhERPCi4a4qy6_eag/zh-cn_image_0000002658792609.png "点击放大")

**方案二**：使用writePixels实现长图绘制。

实现思路如下：

1. 通过获取图片的像素数据ArrayBuffer，创建ImageSource实例并获取图片的宽高信息，通过[InitializationOptions](../harmonyos-references/arkts-apis-image-i.md#initializationoptions8)设置合成后长图图片的透明度、宽高信息（通过比较用于拼接图片的宽高信息决定输出图片的宽高）等。
2. 设置合成图片解码设置[DecodingOptions](../harmonyos-references/arkts-apis-image-i.md#decodingoptions7)，在进行图片拼接之前读取图片的数据，并创建新的PixelMap实例便于对像素数据进行操作。
3. 使用[writePixels](../harmonyos-references/js-apis-sendableimage.md#writepixels)读取指定区域内[PositionArea](../harmonyos-references/arkts-apis-image-i.md#positionarea7)处理后的图像像素数据。

完整示例可参考[官网示例代码](../architecture-guides/image_stitch-0000002287473193.md)。

## 常见FAQ

Q：使用writePixels和Canvas实现绘制效果有什么不同？

A：使用[writePixels](../harmonyos-references/js-apis-sendableimage.md#writepixels)绘制图片时，上层图片会覆盖下层图片，即将上层图片替换下层图片区域。若需要实现实色合并（即图层混合）或是保留图片的透明效果，推荐使用Canvas进行绘制。

Q：可以将多张画布合成为图片吗？

A：HarmonyOS工具中暂未提供直接将画布合成图片的能力，若需合并多张画布上的图片，可以先将画布进行截图操作，将画布转化为图片然后再将图片放入另一个画布中进行拼接。截图操作可以使用[getImageData](../harmonyos-references/ts-components-canvas-common-method.md#getimagedata)或[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)获取Canvas中指定区域的图片，也可以使用[componentSnapshot.getSync](../harmonyos-references/js-apis-arkui-componentsnapshot.md#componentsnapshotgetsync12)实现。

Q：图片数量过多进行绘制时加载速度变慢应该如何解决？

A：可以通过将所需图片包装到一个单例类class并导出，将图片资源都预加载后存入AppStorage中，并在相应页面进行调用，操作方法可参考[官方文档](../harmonyos-guides/arkts-sendable-module.md#使用示例)。

Q：ImageBitmap如何转换为PixelMap？

A：可以通过将ImageBitmap绘制在Canvas画布上，使用[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)获取指定区域的画布数据输出为新的PixelMap对象。需要注意的是，ImageBitmap与PixelMap之间存在单位差异时，在转换时若需保持原图尺寸，需要对图片宽高进行单位转换。

Q：如何实现多张图片叠加合并成一个图层？

A：通过PixelMapDrawableDescriptor创建LayeredDrawableDescriptor，用LayeredDrawableDescriptor()进行图片合成。具体代码参考[官方文档](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

Q：如何在Canvas中渲染网络图片？

A：可以使用ImageKnife三方库实现在Canvas中渲染网络图片的功能。此三方库支持圆角裁剪、圆形裁剪等、图像加载缓存、自定义实现图片获取/网络下载等功能，致力于更高效、更轻便、更简单的功能实现，可以参考[ImageKnife三方库](https://gitcode.com/openharmony-tpc/ImageKnife)。

Q：如何通过Drawing绘制修改PixelMap后生成新的PixelMap？

A：可以通过PixelMap创建画布进行图形绘制，具体代码参考如下：

```ts
import { image } from '@kit.ImageKit';
import { common2D, drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct ImageResize {
  @State ima: PixelMap | undefined = undefined;
  @State imb: PixelMap | undefined = undefined;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(500, 500);
  private img: ImageBitmap = new ImageBitmap('/common/images/img1.png');
  private img2: ImageBitmap = new ImageBitmap('/common/images/img2.png');
  private newWidth: number = 200;
  private newHeight: number = 200;

  build() {
    Column({ space: 20 }) {
      Canvas(this.context)
        .width('90%')
        .height('50%')
        .backgroundColor('#f1f3f5')
        .borderRadius(10)
        .onReady(() => {
          this.draw(this.img, this.img2);
        })

      Button('点击缩放图片')
        .onClick(async () => {
          if (this.ima !== undefined) {
            this.resizeImage(this.ima, this.newWidth, this.newHeight);
          }
        })

      if (this.imb !== undefined) {
        Image(this.imb)
          .width(this.newWidth)
          .height(this.newHeight)
      }
    }
    .width('100%')
    .height('100%')
  }

  draw(img: ImageBitmap | PixelMap, img2: ImageBitmap | PixelMap) {
    let offContext = this.offCanvas.getContext('2d', this.settings);
    let imgWidth = 300;
    let imgHeight = 160;
    let offset = 20;
    offContext.drawImage(img, offset, offset, imgWidth, imgHeight);
    // 根据第一张图片绘制坐标决定第二张图片的初始坐标
    offContext.drawImage(img2, offset, offset * 2 + imgHeight, imgWidth, imgHeight);
    this.ima = offContext.getPixelMap(offset, offset, imgWidth, imgHeight * 2 + offset * 2);
    // 获取离屏绘制的内容
    let image = this.offCanvas.transferToImageBitmap();
    this.context.transferFromImageBitmap(image);
  }

  async resizeImage(bitmap: PixelMap, w: number, h: number): Promise<void> {
    // 获取图像像素信息
    const imageInfo = await bitmap.getImageInfo();
    const width: number = imageInfo.size.width;
    const height: number = imageInfo.size.height;
    const scaleWidth: number = w / width;
    const scaleHeight: number = h / height;
    const pixelMapColor: ArrayBuffer = new ArrayBuffer(w * h * 4);
    const options: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: h, width: w }
    };
    // 采用BGRA_8888格式创建画布PixelMap
    const canvasPixelMap = await image.createPixelMap(pixelMapColor, options);
    // 创建一个以PixelMap作为绘制目标的Canvas对象
    const canvas = new drawing.Canvas(canvasPixelMap);
    // 构造矩阵对象
    const matrix = new drawing.Matrix();
    // 构造画笔对象
    let pen = new drawing.Pen();
    // 绑定画笔到画布上，在画布上进行绘制时，将使用画笔的样式去绘制图形形状的轮廓
    canvas.attachPen(pen);
    // 矩形区域
    let rect: common2D.Rect = {
      left: 0,
      top: 0,
      right: w,
      bottom: h
    };
    // 将图片绘制到画布的指定区域上
    canvas.drawImageRect(bitmap, rect);
    // 将矩阵设置为矩阵右乘围绕轴心点按一定缩放系数缩放后的单位矩阵后得到的矩阵
    matrix.postScale(scaleWidth, scaleHeight, 0, 0);
    // 设置矩阵对象参数
    canvas.setMatrix(matrix);
    // 将画笔与画布解绑
    canvas.detachPen();
    this.imb = canvasPixelMap;
  }
}
```

Q：如何获取合成后的原图base64？

A：可以使用[toDataURL](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md#todataurl)获取原图的base64。

## 总结

对图片进行拼接绘制可以使用Canvas或writePixels进行绘制，两者的适用场景如下：

| 方法 | 适用场景 |
| --- | --- |
| Canvas | 适合图像资源已经加载好后的图像拼接，以及图像拼接后增加更多绘图效果的场景。 |
| writePixels | 适用于简单拼接大量图片的场景以提高性能。 |
