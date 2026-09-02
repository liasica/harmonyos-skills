---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-skeleton-detection
title: 骨骼点检测
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 骨骼点检测
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab5e52b8d7ec0ae30cf7bd39e5d839ba2a450b26a42f204e60fd4b868be40468
---

## 适用场景

人体骨骼关键点检测，主要检测人体的一些关键点，通过关键点描述人体骨骼信息。具体应用主要集中在智能视频监控，病人监护系统，人机交互，虚拟现实，人体动画，智能家居，智能安防，运动员辅助训练等等。

支持17个关键点的识别，具体为鼻子，左右眼，左右耳，左右肩，左右肘、左右手腕、左右髋、左右膝、左右脚踝。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/7ZIWua-uQ5q8G9ihet8Axw/zh-cn_image_0000002706675436.png)

## 开发步骤

1. 在使用骨骼点检测时，将实现骨骼点检测相关的类添加至工程。

   ```typescript
   import { image } from '@kit.ImageKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 通过photoAccessHelper.PhotoViewPicker拉起图库选择图片，使用fileIo与image模块将URI转换为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，为后续检测接口准备输入数据。

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
       hilog.error(0x0000, 'skeletonDetectSample', 'Failed to define uri.');
       return;
     }
     this.loadImage(uri);
   }

   private async openPhoto(): Promise<string> {
     return new Promise<string>((resolve, reject) => {
       let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
       photoPicker.select({
         MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
         maxSelectNumber: 1
       }).then(res => {
         resolve(res.photoUris[0]);
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
         reject(err);
       });
     });
   }

   private loadImage(name: string) {
     setTimeout(async () => {
       let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
       this.imageSource = image.createImageSource(fileSource.fd);
       this.chooseImage = await this.imageSource.createPixelMap();
       await fileIo.close(fileSource);
     }, 100);
   }
   ```
3. 实例化visionBase.Request对象，将PixelMap封装为输入参数；调用[SkeletonDetector.create()](../harmonyos-references/core-vision-skeleton-detection-api.md#create)创建检测器实例，再调用其[process](../harmonyos-references/core-vision-skeleton-detection-api.md#process)方法，获取图片中人体的17个关键点信息，并将结果展示在界面上。

   ```typescript
   Button('开始骨骼点识别')
     .type(ButtonType.Capsule)
     .fontColor(Color.White)
     .alignSelf(ItemAlign.Center)
     .width('80%')
     .margin(10)
     .onClick(() => {
       // 调用封装的异步处理函数
       void this.handleSkeletonDetection();
     })
   ```

   骨骼点识别的方法实现如下：

   ```typescript
   private async handleSkeletonDetection() {
     try {
       if (!this.chooseImage) {
         hilog.error(0x0000, 'skeletonDetectSample', 'Failed to choose image.');
         return;
       }
       // 调用骨骼点识别接口
       let request: visionBase.Request = {
         inputData: { pixelMap: this.chooseImage }
       };
       let detector = await skeletonDetection.SkeletonDetector.create();
       let data: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);
       await detector.destroy();
       let poseJson = JSON.stringify(data);
       hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in skeleton detection: ${poseJson}`);
       this.dataValues = poseJson;
     } catch (err) {
       const error = err as BusinessError;
       hilog.error(0x0000, 'skeletonDetectSample', `Skeleton detection error. Code: ${error.code}, message: ${error.message}`);
     }
   }
   ```

## 开发实例

### Index.ets

```typescript
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct Index {
  private imageSource: image.ImageSource | undefined = undefined;
  @State chooseImage: PixelMap | undefined = undefined;
  @State dataValues: string = '';

  build() {
    Column() {
      Image(this.chooseImage)
        .objectFit(ImageFit.Fill)
        .height('60%')

      Text(this.dataValues)
        .copyOption(CopyOptions.LocalDevice)
        .height('15%')
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

      Button('开始骨骼点识别')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          // 调用封装的异步处理函数
          void this.handleSkeletonDetection();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 封装骨骼点识别的异步逻辑
  private async handleSkeletonDetection() {
    try {
      if (!this.chooseImage) {
        hilog.error(0x0000, 'skeletonDetectSample', 'Failed to choose image.');
        return;
      }
      // 调用骨骼点识别接口
      let request: visionBase.Request = {
        inputData: { pixelMap: this.chooseImage }
      };
      let detector = await skeletonDetection.SkeletonDetector.create();
      let data: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);
      await detector.destroy();
      if (!data) {
        hilog.error(0x0000, 'skeletonDetectSample', 'Invalid skeleton detection result');
        return;
      }
      let poseJson = JSON.stringify(data);
      hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in skeleton detection: ${poseJson}`);
      this.dataValues = poseJson;
    } catch (err) {
      const error = err as BusinessError;
      hilog.error(0x0000, 'skeletonDetectSample', `Skeleton detection error. Code: ${error.code}, message: ${error.message}`);
    }
  }

  private async selectImage() {
    let uri = await this.openPhoto();
    if (!uri) {
      hilog.error(0x0000, 'skeletonDetectSample', 'Failed to define uri.');
      return;
    }
    this.loadImage(uri);
  }

  private async openPhoto(): Promise<string> {
    return new Promise<string>((resolve, reject) => {
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select({
        MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
        maxSelectNumber: 1
      }).then(res => {
        resolve(res.photoUris[0]);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
        reject(err);
      });
    });
  }

  private loadImage(name: string) {
    setTimeout(async () => {
      let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
      this.imageSource = image.createImageSource(fileSource.fd);
      this.chooseImage = await this.imageSource.createPixelMap();
      await fileIo.close(fileSource);
    }, 100);
  }
}
```
