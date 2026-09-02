---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-23
title: 如何实现动态照片压缩
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何实现动态照片压缩
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a06c54cf7846dfa674f550b07d5b73a132f2b7bd6a9e2ff872ed1d04f7cb3c84
---

## 问题现象

使用系统相机拍摄的动态图片，使用packToFile编码压缩后会变成静态图片。如何压缩动态图片并维持其动态特性？

## 背景知识

* [动态照片](../harmonyos-guides/photoaccesshelper-movingphoto.md)：是一种结合了图片和视频的照片形式，可以显示一小段时间的动态画面和声音。图片格式为JPG，视频格式为MP4。
* [packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)：指定编码参数对图片进行编码压缩。
* [AVTranscoder](../harmonyos-references/arkts-apis-media-avtranscoder.md)：视频转码管理，可用于视频压缩。
* [MovingPhotoView](../harmonyos-guides/movingphotoview-guidelines.md)：用于播放动态照片的组件。

## 解决方案

1. 获取媒体库动态照片对象，将动态照片的图片内容和视频内容分别保存在沙箱文件中。具体可参考：[获取媒体库动态照片对象](../harmonyos-guides/photoaccesshelper-movingphoto.md#获取媒体库动态照片对象)。

   ```ts
   async function pickMovingPhoto(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
     try {
       // picker选择动态照片uri。
       let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
       photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.MOVING_PHOTO_IMAGE_TYPE;
       photoSelectOptions.maxSelectNumber = 9;
       let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
       let photoSelectResult = await photoViewPicker.select(photoSelectOptions);
       let uris = photoSelectResult.photoUris;
       for (let i = 0; i < uris.length; i++) {
         // 获取uri对应的PhotoAsset资产。
         let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
         predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uris[i]);
         let fetchOption: photoAccessHelper.FetchOptions = {
           fetchColumns: [],
           predicates: predicates,
         };
         let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
           await phAccessHelper.getAssets(fetchOption);
         let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
         // 获取PhotoAsset对应的动态照片对象。
         await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, photoAsset, {
           deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
         }, {
           async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
             // 保存动态图片图片部分的沙箱文件地址
             let imageFileUri = 'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image.jpg';
             // 保存动态图片视频部分的沙箱文件地址
             let videoFileUri = 'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video.mp4';
             let imageFile: fileIo.File | undefined;
             let videoFile: fileIo.File | undefined;
             if (movingPhoto !== undefined) {
               console.info(`request moving photo successfully, uri: ${movingPhoto.getUri()}`);
               try {
                 fileIo.openSync(imageFileUri, fileIo.OpenMode.CREATE);
                 fileIo.openSync(videoFileUri, fileIo.OpenMode.CREATE);
                 await movingPhoto.requestContent(imageFileUri, videoFileUri);
               } catch (err) {
                 console.error(`failed to moving photo`);
               } finally {
                 if (imageFile) {
                   fileIo.closeSync(imageFile);
                 }
                 if (videoFile) {
                   fileIo.closeSync(videoFile);
                 }
               }
             }
           },
         });
       }
     } catch (err) {
       console.error(`request moving photo failed with error: ${err.code}, ${err.message}`);
     }
   }
   ```
2. 使用[ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)类的[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)接口压缩动态照片的图片内容。具体可参考：[图片编码进文件](../harmonyos-guides/image-encoding.md)。

   ```ts
   Button('Pack Image')
     .width('100%')
     .onClick(async () => {
       // 保存动态照片图片内容的沙箱文件地址
       let imageFileUri =
         'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image.jpg';
       // 保存压缩后的图片文件的沙箱文件地址
       let packFileUri =
         'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image_packed.jpg';
       let imageFile: fileIo.File | undefined;
       let packFile: fileIo.File | undefined;
       try {
         imageFile = fileIo.openSync(imageFileUri, fileIo.OpenMode.READ_WRITE);
         packFile = fileIo.openSync(packFileUri, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         let imageSource = image.createImageSource(imageFile.fd);
         let imagePacker = image.createImagePacker();
         let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 50 };
         await imagePacker.packToFile(imageSource, packFile.fd, packOpts);
       } catch (err) {
         console.error(`failed to pack image file: ${JSON.stringify(err)}`);
       } finally {
         if (imageFile) {
           fileIo.closeSync(imageFile);
         }
         if (packFileUri) {
           fileIo.closeSync(packFile);
         }
       }
     });
   ```
3. 使用[AVTranscoder](../harmonyos-references/arkts-apis-media-avtranscoder.md)对动态照片的视频内容进行编码转换压缩。具体可参考：[使用AVTranscoder实现视频转码](../harmonyos-guides/using-avtranscoder-for-transcodering.md)。

   ```ts
   Button('Pack Video')
     .width('100%')
     .onClick(async () => {
       // 保存动态照片视频内容的沙箱文件地址
       let videoFileUri =
         'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video.mp4';
       // 保存压缩后的视频文件的沙箱文件地址
       let packFileUri =
         'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video_packed.mp4';
       let videoFile: fileIo.File | undefined;
       let packFile: fileIo.File | undefined;
       try {
         videoFile = fileIo.openSync(videoFileUri, fileIo.OpenMode.READ_WRITE);
         packFile = fileIo.openSync(packFileUri, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         let videoFileSize = fileIo.statSync(videoFile.fd).size;
         this.avTranscoder!.fdSrc = { fd: videoFile.fd, offset: 0, length: videoFileSize };
         this.avTranscoder!.fdDst = packFile.fd;
         let config: media.AVTranscoderConfig = {
           audioCodec: media.CodecMimeType.AUDIO_AAC,
           videoCodec: media.CodecMimeType.VIDEO_HEVC,
           fileFormat: media.ContainerFormatType.CFT_MPEG_4,
           audioBitrate: 20000,
           videoBitrate: 10000000,
         };
         await this.avTranscoder!.prepare(config);
         await this.avTranscoder!.start();
       } catch (err) {
         console.error(`failed to pack video file: ${JSON.stringify(err)}`);
       } finally {
         if (videoFile) {
           fileIo.closeSync(videoFile);
         }
         if (packFile) {
           fileIo.closeSync(packFile);
         }
       }
     });
   ```
4. 根据压缩后的图片和视频文件重新加载成MovingPhoto对象。具体可参考：[获取应用沙箱动态照片对象](../harmonyos-guides/photoaccesshelper-movingphoto.md#获取应用沙箱动态照片对象)。

   ```ts
   Button('Load Moving Photo')
     .width('100%')
     .onClick(async () => {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       try {
         // 压缩后的图片文件的沙箱地址
         let imageFileUri =
           'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image_packed.jpg';
         // 压缩后的视频文件的沙箱地址
         let videoFileUri =
           'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video_packed.mp4';
         this.src =
           await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
         console.info(`Load moving photo successfully`);
       } catch (err) {
         console.error(`Load Moving photo failed: ${JSON.stringify(err)}`);
       }
     });
   ```
5. 根据压缩后的图片和视频文件保存动态照片对象到系统图库。具体可参考：[保存动态照片资源](../harmonyos-guides/photoaccesshelper-movingphoto.md#保存动态照片资源)。

   ```ts
   SaveButton({
     icon: SaveIconStyle.FULL_FILLED,
     text: SaveDescription.SAVE_IMAGE,
     buttonType: ButtonType.Capsule,
   }) // 创建安全控件按钮。
     .onClick(async (_event, result: SaveButtonOnClickResult) => {
       if (result === SaveButtonOnClickResult.SUCCESS) {
         try {
           let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
           let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
           // 压缩后的图片文件的沙箱地址
           let imageFileUri =
             'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image_packed.jpg';
           // 压缩后的视频文件的沙箱地址
           let videoFileUri =
             'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video_packed.mp4';
           let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
             photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context,
               photoAccessHelper.PhotoType.IMAGE, 'jpg', {
                 title: 'moving_photo',
                 subtype: photoAccessHelper.PhotoSubtype.MOVING_PHOTO,
               });
           assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, imageFileUri);
           assetChangeRequest.addResource(photoAccessHelper.ResourceType.VIDEO_RESOURCE, videoFileUri);
           await phAccessHelper.applyChanges(assetChangeRequest);
           console.info(`create moving photo successfully, uri: ${assetChangeRequest.getAsset().uri}`);
         } catch (err) {
           console.error(`create moving photo failed with error: ${err.code}, ${err.message}`);
         }
       } else {
         console.error('SaveButtonOnClickResult create moving photo failed');
       }
     });
   ```

完整代码如下：

```ts
import {
  MovingPhotoView,
  MovingPhotoViewController,
  photoAccessHelper,
} from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
import image from '@ohos.multimedia.image';
import { fileIo } from '@kit.CoreFileKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { dataSharePredicates } from '@kit.ArkData';

async function pickMovingPhoto(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  try {
    // picker选择动态照片uri。
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.MOVING_PHOTO_IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 9;
    let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult = await photoViewPicker.select(photoSelectOptions);
    let uris = photoSelectResult.photoUris;
    for (let i = 0; i < uris.length; i++) {
      // 获取uri对应的PhotoAsset资产。
      let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
      predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uris[i]);
      let fetchOption: photoAccessHelper.FetchOptions = {
        fetchColumns: [],
        predicates: predicates,
      };
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await phAccessHelper.getAssets(fetchOption);
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      // 获取PhotoAsset对应的动态照片对象。
      await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, photoAsset, {
        deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
      }, {
        async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
          // 保存动态图片图片部分的沙箱文件地址
          let imageFileUri = 'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image.jpg';
          // 保存动态图片视频部分的沙箱文件地址
          let videoFileUri = 'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video.mp4';
          let imageFile: fileIo.File | undefined;
          let videoFile: fileIo.File | undefined;
          if (movingPhoto !== undefined) {
            console.info(`request moving photo successfully, uri: ${movingPhoto.getUri()}`);
            try {
              fileIo.openSync(imageFileUri, fileIo.OpenMode.CREATE);
              fileIo.openSync(videoFileUri, fileIo.OpenMode.CREATE);
              await movingPhoto.requestContent(imageFileUri, videoFileUri);
            } catch (err) {
              console.error(`failed to moving photo`);
            } finally {
              if (imageFile) {
                fileIo.closeSync(imageFile);
              }
              if (videoFile) {
                fileIo.closeSync(videoFile);
              }
            }
          }
        },
      });
    }
  } catch (err) {
    console.error(`request moving photo failed with error: ${err.code}, ${err.message}`);
  }
}

@Entry
@Component
struct Index {
  @State src: photoAccessHelper.MovingPhoto | undefined = undefined;
  controller: MovingPhotoViewController = new MovingPhotoViewController();
  avTranscoder: media.AVTranscoder | undefined = undefined;

  async aboutToAppear(): Promise<void> {
    try {
      this.avTranscoder = await media.createAVTranscoder();
    } catch (err) {
      console.error(`failed to create AVTranscoder: ${JSON.stringify(err)}`);
      return;
    }
    this.avTranscoder.on('complete', async () => {
      console.info(`AVTranscoder completed`);
    });
    this.avTranscoder.on('error', (err: BusinessError) => {
      console.error(`AVTranscoder failed: ${JSON.stringify(err)}`);
    });
    this.avTranscoder.on('progressUpdate', (progress: number) => {
      console.info(`AVTrancoder progress update: ${progress}`);
    });
  }

  build() {
    Column({ space: 20 }) {
      Column() {
        MovingPhotoView({
          movingPhoto: this.src,
          controller: this.controller,
        });
      }
      .width('50%')
      .aspectRatio(1);

      Row() {
        Button('Start Play')
          .margin(5)
          .onClick(() => {
            this.controller.startPlayback();
          });
        Button('Stop Play')
          .margin(5)
          .onClick(() => {
            this.controller.stopPlayback();
          });
      }
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('10%');

      Button('Pick Moving Photo').onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
        pickMovingPhoto(phAccessHelper, context);
      }).width('100%');

      Button('Pack Image')
        .width('100%')
        .onClick(async () => {
          // 保存动态照片图片内容的沙箱文件地址
          let imageFileUri =
            'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image.jpg';
          // 保存压缩后的图片文件的沙箱文件地址
          let packFileUri =
            'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image_packed.jpg';
          let imageFile: fileIo.File | undefined;
          let packFile: fileIo.File | undefined;
          try {
            imageFile = fileIo.openSync(imageFileUri, fileIo.OpenMode.READ_WRITE);
            packFile = fileIo.openSync(packFileUri, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
            let imageSource = image.createImageSource(imageFile.fd);
            let imagePacker = image.createImagePacker();
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 50 };
            await imagePacker.packToFile(imageSource, packFile.fd, packOpts);
          } catch (err) {
            console.error(`failed to pack image file: ${JSON.stringify(err)}`);
          } finally {
            if (imageFile) {
              fileIo.closeSync(imageFile);
            }
            if (packFileUri) {
              fileIo.closeSync(packFile);
            }
          }
        });

      Button('Pack Video')
        .width('100%')
        .onClick(async () => {
          // 保存动态照片视频内容的沙箱文件地址
          let videoFileUri =
            'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video.mp4';
          // 保存压缩后的视频文件的沙箱文件地址
          let packFileUri =
            'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video_packed.mp4';
          let videoFile: fileIo.File | undefined;
          let packFile: fileIo.File | undefined;
          try {
            videoFile = fileIo.openSync(videoFileUri, fileIo.OpenMode.READ_WRITE);
            packFile = fileIo.openSync(packFileUri, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
            let videoFileSize = fileIo.statSync(videoFile.fd).size;
            this.avTranscoder!.fdSrc = { fd: videoFile.fd, offset: 0, length: videoFileSize };
            this.avTranscoder!.fdDst = packFile.fd;
            let config: media.AVTranscoderConfig = {
              audioCodec: media.CodecMimeType.AUDIO_AAC,
              videoCodec: media.CodecMimeType.VIDEO_HEVC,
              fileFormat: media.ContainerFormatType.CFT_MPEG_4,
              audioBitrate: 20000,
              videoBitrate: 10000000,
            };
            await this.avTranscoder!.prepare(config);
            await this.avTranscoder!.start();
          } catch (err) {
            console.error(`failed to pack video file: ${JSON.stringify(err)}`);
          } finally {
            if (videoFile) {
              fileIo.closeSync(videoFile);
            }
            if (packFile) {
              fileIo.closeSync(packFile);
            }
          }
        });

      Button('Load Moving Photo')
        .width('100%')
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          try {
            // 压缩后的图片文件的沙箱地址
            let imageFileUri =
              'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image_packed.jpg';
            // 压缩后的视频文件的沙箱地址
            let videoFileUri =
              'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video_packed.mp4';
            this.src =
              await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
            console.info(`Load moving photo successfully`);
          } catch (err) {
            console.error(`Load Moving photo failed: ${JSON.stringify(err)}`);
          }
        });

      SaveButton({
        icon: SaveIconStyle.FULL_FILLED,
        text: SaveDescription.SAVE_IMAGE,
        buttonType: ButtonType.Capsule,
      }) // 创建安全控件按钮。
        .onClick(async (_event, result: SaveButtonOnClickResult) => {
          if (result === SaveButtonOnClickResult.SUCCESS) {
            try {
              let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
              // 压缩后的图片文件的沙箱地址
              let imageFileUri =
                'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_image_packed.jpg';
              // 压缩后的视频文件的沙箱地址
              let videoFileUri =
                'file://com.huawei.myapplication/data/storage/el2/base/haps/entry/files/moving_video_packed.mp4';
              let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
                photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context,
                  photoAccessHelper.PhotoType.IMAGE, 'jpg', {
                    title: 'moving_photo',
                    subtype: photoAccessHelper.PhotoSubtype.MOVING_PHOTO,
                  });
              assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, imageFileUri);
              assetChangeRequest.addResource(photoAccessHelper.ResourceType.VIDEO_RESOURCE, videoFileUri);
              await phAccessHelper.applyChanges(assetChangeRequest);
              console.info(`create moving photo successfully, uri: ${assetChangeRequest.getAsset().uri}`);
            } catch (err) {
              console.error(`create moving photo failed with error: ${err.code}, ${err.message}`);
            }
          } else {
            console.error('SaveButtonOnClickResult create moving photo failed');
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
