---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-image-super-resolution
title: 图像超分
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 图像超分
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:70858eaa9abfe81aa8ff38ba3490b42a4c4ed629c6a0665a645ca9fb995c70e7
---

## 适用场景

从26.0.0版本开始，新增支持对输入的低分辨率图像进行超分辨率重建，使图像更加清晰。适用于提升图片质量、修复老照片等场景。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/PcN8esRSRMOQOhxiOiHbFg/zh-cn_image_0000002736434523.png "点击放大")

## 开发步骤

1. 在使用图像超分时，将实现图像超分相关的类添加至工程。

   ```typescript
   import { imageSuperResolution, visionBase } from '@kit.CoreVisionKit'
   import { image } from '@kit.ImageKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 在aboutToAppear中调用[ImageSRAnalyzer.create()](../harmonyos-references/core-vision-image-super-resolution-api.md#imagesranalyzercreate)创建图像超分分析器实例，并且在aboutToDisappear中调用[ImageSRAnalyzer.destroy()](../harmonyos-references/core-vision-image-super-resolution-api.md#imagesranalyzerdestroy)释放资源。

   ```typescript
   private analyzer: imageSuperResolution.ImageSRAnalyzer | null = null;

   async aboutToAppear(): Promise<void> {
     this.analyzer = await imageSuperResolution.ImageSRAnalyzer.create();
     hilog.info(0x0000, 'ImageSRSample', 'ImageSRAnalyzer created');
   }

   async aboutToDisappear(): Promise<void> {
     if (this.analyzer) {
       await this.analyzer.destroy();
       hilog.info(0x0000, 'ImageSRSample', 'ImageSRAnalyzer released successfully');
     }
   }
   ```
3. 通过photoAccessHelper.PhotoViewPicker拉起图库选择图片，并且使用fileIo与image模块将URI转换为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，为后续超分接口准备输入数据。

   ```typescript
   Button('选择图片')
     .type(ButtonType.Capsule)
     .fontColor(Color.White)
     .alignSelf(ItemAlign.Center)
     .width('80%')
     .margin(10)
     .onClick(() => {
       // 拉起图库，获取图片资源
       void this.selectImage();
     })
   ```

   选择图片与解码图片的方法实现如下：

   ```typescript
   private async selectImage() {
     let uri = await this.openPhoto();
     if (!uri) {
       hilog.error(0x0000, 'ImageSRSample', 'Failed to get uri.');
       return;
     }
     this.loadImage(uri);
   }

   private async openPhoto(): Promise<string> {
     return new Promise<string>((resolve) => {
       let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
       photoPicker.select({
         MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
         maxSelectNumber: 1
       }).then(res => {
         resolve(res.photoUris[0]);
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'ImageSRSample', `Failed to get photo image uri.code: ${err.code}, message: ${err.message}`);
         resolve('');
       });
     });
   }

   private loadImage(name: string) {
     setTimeout(async () => {
       let imageSource: image.ImageSource | undefined = undefined;
       let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
       imageSource = image.createImageSource(fileSource.fd);
       this.inputImage = await imageSource.createPixelMap();
       this.dataValues = '';
       await fileIo.close(fileSource);
     }, 100);
   }
   ```
4. 构造[Request](../harmonyos-references/core-vision-image-super-resolution-api.md#imagesranalyzerprocess)对象并传入待处理图片的PixelMap，调用[ImageSRAnalyzer.process](../harmonyos-references/core-vision-image-super-resolution-api.md#imagesranalyzerprocess)方法，获取超分处理结果并展示在界面上。

   ```typescript
   Button('图像超分')
     .type(ButtonType.Capsule)
     .fontColor(Color.White)
     .alignSelf(ItemAlign.Center)
     .width('80%')
     .margin(10)
     .onClick(() => {
       if (!this.inputImage || !this.analyzer) {
         hilog.error(0x0000, 'ImageSRSample', 'Failed to process image super resolution.');
         return;
       }
       // 调用图像超分接口
       let imageData: visionBase.ImageData = {
         pixelMap: this.inputImage
       }
       let request: visionBase.Request = {
         inputData: imageData
       };
       request.inputData = imageData
       this.analyzer.process(request)
         .then((response: imageSuperResolution.ISPResponse) => {
           hilog.info(0x0000, 'ImageSRSample', 'Super resolution completed');
           this.outputImage = response.pixelMap;
         })
         .catch((error: BusinessError) => {
           hilog.error(0x0000, 'ImageSRSample', `Image super resolution failed. Code: ${error.code}, message: ${error.message}`);
           this.dataValues = `Error: ${error.message}`;
         });
     })
   ```

## 开发实例

### Index.ets

```typescript
import { imageSuperResolution, visionBase } from '@kit.CoreVisionKit'
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct Index {
  @State inputImage: PixelMap | undefined = undefined;
  @State outputImage: PixelMap | undefined = undefined;
  @State dataValues: string = '';
  private analyzer: imageSuperResolution.ImageSRAnalyzer | null = null;

  async aboutToAppear(): Promise<void> {
    this.analyzer = await imageSuperResolution.ImageSRAnalyzer.create();
    hilog.info(0x0000, 'ImageSRSample', 'ImageSRAnalyzer created');
  }

  async aboutToDisappear(): Promise<void> {
    if (this.analyzer) {
      await this.analyzer.destroy();
      hilog.info(0x0000, 'ImageSRSample', 'ImageSRAnalyzer released successfully');
    }
  }

  build() {
    Column() {
      Text('Input Image')
        .fontSize(16)
        .margin(5)
      Image(this.inputImage)
        .objectFit(ImageFit.Fill)
        .height('25%')
      Text('Output Image')
        .fontSize(16)
        .margin(5)
      Image(this.outputImage)
        .objectFit(ImageFit.Fill)
        .height('25%')
      Text(this.dataValues)
        .copyOption(CopyOptions.LocalDevice)
        .height('10%')
        .margin(10)
        .width('60%')
      Button('选择图片')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          // 拉起图库
          void this.selectImage();
        })
      Button('图像超分')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          if (!this.inputImage || !this.analyzer) {
            hilog.error(0x0000, 'ImageSRSample', 'Failed to process image super resolution.');
            return;
          }
          // 调用图像超分接口
          let imageData: visionBase.ImageData = {
            pixelMap: this.inputImage
          }
          let request: visionBase.Request = {
            inputData: imageData
          };
          request.inputData = imageData
          this.analyzer.process(request)
            .then((response: imageSuperResolution.ISPResponse) => {
              hilog.info(0x0000, 'ImageSRSample', 'Super resolution completed');
              this.outputImage = response.pixelMap;
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'ImageSRSample', `Image super resolution failed. Code: ${error.code}, message: ${error.message}`);
              this.dataValues = `Error: ${error.message}`;
            });
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    let uri = await this.openPhoto();
    if (!uri) {
      hilog.error(0x0000, 'ImageSRSample', 'Failed to get uri.');
      return;
    }
    this.loadImage(uri);
  }

  private async openPhoto(): Promise<string> {
    return new Promise<string>((resolve) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
        maxSelectNumber: 1
      }).then(res => {
        resolve(res.photoUris[0]);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'ImageSRSample', `Failed to get photo image uri.code: ${err.code}, message: ${err.message}`);
        resolve('');
      });
    });
  }

  private loadImage(name: string) {
    setTimeout(async () => {
      let imageSource: image.ImageSource | undefined = undefined;
      let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
      imageSource = image.createImageSource(fileSource.fd);
      this.inputImage = await imageSource.createPixelMap();
      this.dataValues = '';
      this.outputImage = undefined;
      await fileIo.close(fileSource);
    }, 100);
  }
}
```
