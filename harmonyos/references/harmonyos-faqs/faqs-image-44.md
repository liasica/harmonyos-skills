---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-44
title: ImageBitmap如何加载不同来源的图片
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > ImageBitmap如何加载不同来源的图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f7368bd5780a033c6eda7382b47a496d1ab54af2a89a76c43cd5aa51aaecf9e4
---

## 问题现象

ImageBitmap如何加载不同来源的图片？例如引用资源文件夹的图片$r('app.media.icon')等路径无法正常渲染显示，该如何解决？

## 背景知识

[ImageBitmap](../harmonyos-references/ts-components-canvas-imagebitmap.md)对象可以存储Canvas渲染的像素数据，可用在Canvas上进行高效绘制图像，也可直接用于图像预览，且不同于PixelMap，ImageBitmap支持跨平台兼容。

## 解决方案

ImageBitmap对象仅接受实际文件路径（如“ets/common/test.jpg”），因为/resource资源目录在编译时会被打包进应用中，其中的资源并没有实际路径，所以对于放在/resources资源目录下的图片需要使用resourceManager将图片创建为可操作的PixelMap对象。

* 对于本地路径图片，可直接将图片路径地址传入ImageBitmap中。

  ```ts
  let img: ImageBitmap = new ImageBitmap('common/image/testImage.jpg'); // testImage.jpg仅供参考使用，开发者可替换为实际使用图片
  ```
* 对于资源目录（/resource）下的图片，需要通过图片解码将其转化为新的PixelMap实例再加载到ImageBitmap中。

  ```ts
  getImageBitmapByMediaResource(context: Context, resource: Resource) {
    let fileData: Uint8Array = context.resourceManager.getMediaContentSync(resource.id);
    let imageSource: image.ImageSource = image.createImageSource(fileData.buffer);
    let options: image.DecodingOptions = { editable: true, desiredPixelFormat: image.PixelMapFormat.RGBA_8888 };
    let pixelMap: image.PixelMap = imageSource.createPixelMapSync(options);
    return new ImageBitmap(pixelMap);
  }
  ```
* 对于沙箱路径图片，保存后存放于haps中（如“/data/storage/el2/base/haps/entry/files/img.png”），不能直接用于ImageBitmap渲染处理，需要获取到图片沙箱路径后，使用图片编解码将其转为ImageBitmap对象，使用Canvas加载ImageBitmap：

  ```ts
  getImageBitmapByLocalFile(filePath: string) {
    const imageSource: image.ImageSource = image.createImageSource(filePath);
    const pixelMap: image.PixelMap = imageSource.createPixelMapSync();
    return new ImageBitmap(pixelMap);
  }
  ```
* 对于相册路径图片（如“file://media/Photo/5/IMG\_1750126638\_004/test.jpg”）可以直接使用ImageBitmap加载路径使用。
* 对于网络路径图片，ImageBitmap不支持直接加载，需要通过网络请求下载图片并存放于沙箱中，最后使用沙箱路径渲染加载ImageBitmap的方式实现，参考[下载网络资源文件至应用文件目录](../harmonyos-guides/app-file-upload-download.md#下载网络资源文件至应用文件目录)。

ImageBitmap加载本地路径图片、资源目录图片、沙箱路径图片三种场景的完整示例参考如下：

```ts
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';
import fs from '@ohos.file.fs';
import { resourceManager } from '@kit.LocalizationKit';

@Entry
@Component
struct Index {
  // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  // 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // testImage.jpg需要替换为本地资源文件
  private imageFileName: string = 'testImage.jpg';

  // 将media目录下的图片文件复制到沙箱目录
  mediaImageFileToLocalFile(fileName: Resource) {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    let buff = resourceMgr.getMediaContentSync(fileName.id);
    let localFileUri: string = context.filesDir + '/' + this.imageFileName;
    let file: fs.File | null = null;
    try {
      file = fs.openSync(localFileUri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      fs.writeSync(file.fd, buff.buffer);
      console.info('file path is :', file.path);
    } catch (e) {
      console.error('fs.openSync failed error is : ', JSON.stringify(e));
    } finally {
      if (file !== null) {
        fs.closeSync(file);
      }
    }
  }

  // 将media目录下面的图片转化为ImageBitmap
  getImageBitmapByMediaResource(context: Context, resource: Resource) {
    let fileData: Uint8Array = context.resourceManager.getMediaContentSync(resource.id);
    let imageSource: image.ImageSource = image.createImageSource(fileData.buffer);
    let options: image.DecodingOptions = { editable: true, desiredPixelFormat: image.PixelMapFormat.RGBA_8888 };
    let pixelMap: image.PixelMap = imageSource.createPixelMapSync(options);
    return new ImageBitmap(pixelMap);
  }

  // 将沙箱目录下的图片转化为ImageBitmap
  getImageBitmapByLocalFile(filePath: string) {
    const imageSource: image.ImageSource = image.createImageSource(filePath);
    const pixelMap: image.PixelMap = imageSource.createPixelMapSync();
    return new ImageBitmap(pixelMap);
  }

  aboutToAppear(): void {
    this.mediaImageFileToLocalFile($r('app.media.testImage')); // testImage仅供参考使用，开发者可替换为实际使用图片
  }

  build() {
    Column() {
      Text('ImageBitmap加载三种不同来源的图片')
        .margin({ top: 10 })
        .fontSize(20);
      Canvas(this.context)
        .width('80%')
        .height('100%')
        .onReady(async () => {
          // 加载工程目录ets/common/image下面的图片
          let img: ImageBitmap = new ImageBitmap('common/image/testImage.jpg'); // testImage.jpg仅供参考使用，开发者可替换为实际使用图片
          this.context.font = 'normal normal 60px sans-serif';
          this.context.fillText('common', 120, 15);
          this.context.drawImage(img, 0, 25);
          // 资源目录（/resource）下的图片
          let imageBitmap1 =
            this.getImageBitmapByMediaResource(this.getUIContext().getHostContext() as common.UIAbilityContext,
              $r('app.media.testImage')); // testImage仅供参考使用，开发者可替换为实际使用图片
          this.context.fillText('resource', 120, 130);
          this.context.drawImage(imageBitmap1, 0, 140);
          // 沙箱路径的图片
          let uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let filePath = uiContext.filesDir + '/' + this.imageFileName;
          let imageBitmap2 = this.getImageBitmapByLocalFile(filePath);
          this.context.fillText('沙箱路径', 120, 250);
          this.context.drawImage(imageBitmap2, 0, 260);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 总结

ImageBitmap在跨平台开发环境支持中有着广泛应用，HarmonyOS中常见的图片资源来源有本地资源目录、网络、相册、沙箱等，对于不同来源ImageBitmap要采取对应的措施进行加载。
