---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-thumbnail-system
title: 基于系统能力获取视频缩略图
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 媒体开发实践 > 基于系统能力获取视频缩略图
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:10eeb76e0ec7ba1ec47678323351a9829441259ae21697d236bac0b1a6f6d9e1
---

## 概述

视频缩略图是视频的静态预览图像，是从视频中截取的某一帧画面，经常用作视频的封面。在视频浏览、分享和管理等场景中使用可以帮助用户快速浏览和选择想要的内容，提高用户的使用体验。HarmonyOS提供了对应的模块能力，帮助开发者获取视频文件的缩略图。根据应用获取缩略图策略的不同，可以分为以下两种场景：

* [获取视频默认缩略图](video-thumbnail-system.md#获取视频默认缩略图)
* [选取视频帧作为缩略图](video-thumbnail-system.md#选取视频帧作为缩略图)

## 获取视频默认缩略图

### 实现原理

视频的默认缩略图一般为视频的第一帧，可以通过[PhotoAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md)类的[getThumbnail()](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md#getthumbnail-2)方法获取。这里以获取图库视频缩略图场景为例。

### 开发步骤

1. 通过相册管理模块[@ohos.file.photoAccessHelper](../harmonyos-references/js-apis-photoaccesshelper.md)的[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)选取图库视频，获得视频的URL。

   ```typescript
   async selectVideo(): Promise<string> {
     try {
       let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
       return photoViewPicker.select({
         MIMEType: photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE,
         maxSelectNumber: 1
       }).then((photoSelectResult: photoAccessHelper.PhotoSelectResult): string => {
         if (photoSelectResult.photoUris.length <= 0) {
           return '';
         }
         return photoSelectResult.photoUris[0];
       })
     } catch (error) {
       hilog.error(0x0000, TAG, `selectVideo catch error, code: ${error.code}, message: ${error.message}`);
       return '';
     }
   }
   ```
2. 使用[getAssets()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)方法，通过选择的图库视频的URL获取视频资源。

   ```typescript
   let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
   predicates.equalTo('uri', videoUrl);
   let videoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
     await this.phAccessHelper.getAssets({
       fetchColumns: ['width', 'height', 'orientation'],
       predicates: predicates
     });
   let photoAsset: photoAccessHelper.PhotoAsset = await videoFetchResult.getFirstObject();
   ```
3. 根据视频资源的属性配置缩略图的尺寸信息，调用getThumbnail()方法获取PixelMap格式的图片。

   ```typescript
   let thumbnailSize: Size = { width: 0, height: 0 };
   if (photoAsset.get(photoAccessHelper.PhotoKeys.ORIENTATION) === 90 ||
     photoAsset.get(photoAccessHelper.PhotoKeys.ORIENTATION) === 270) {
     thumbnailSize.width = photoAsset.get(photoAccessHelper.PhotoKeys.HEIGHT) as number;
     thumbnailSize.height = photoAsset.get(photoAccessHelper.PhotoKeys.WIDTH) as number;
   } else {
     thumbnailSize.width = photoAsset.get(photoAccessHelper.PhotoKeys.WIDTH) as number;
     thumbnailSize.height = photoAsset.get(photoAccessHelper.PhotoKeys.HEIGHT) as number;
   }
   return photoAsset.getThumbnail(thumbnailSize);
   ```

**说明** 

使用getAsset()和getThumbnail()方法需要申请受限开放权限'[ohos.permission.READ\_IMAGEVIDEO'](restricted-permissions.md#ohospermissionread_imagevideo)，对于需要克隆、备份或同步图片/视频类文件的应用可申请获取该权限，并通过[getAlbums()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums)方法获取相册资源再调用这两个方法获取缩略图。或者通过picker的方式可以在不获取权限的情况下，使用这两个方法来访问用户指定的图库资源获取缩略图。本文中的示例使用的是第二种picker的方式。

### 实现效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/ti_SSUCHQY-Y0cBUYsHbRA/zh-cn_image_0000002736433741.gif)

## 选取视频帧作为缩略图

### 实现原理

HarmonyOS提供视频缩略图获取类[AVImageGenerator](../harmonyos-references/arkts-apis-media-avimagegenerator.md)用于选取视频指定时间的帧作为缩略图，这里以选取图库视频缩略图场景为例。

### 开发步骤

1. 拉起图库picker，选取视频获取文件资源描述符。

   ```typescript
   async imageGeneratorGetThumbnail() {
     this.photoUtils.selectVideo().then(async (result: string) => {
       // ...
       this.fileAlbum = fileIo.openSync(result, fileIo.OpenMode.READ_ONLY);
       this.avFileDescriptor = { fd: this.fileAlbum.fd };
       // ...
     }).catch((error: BusinessError) => {
       hilog.error(0x0000, TAG,
         `Invoke imageGeneratorGetThumbnail failed!, error code: ${error.code}, message: ${error.message}`);
     })
   }
   ```
2. 根据文件资源描述符获取视频元数据信息。

   ```typescript
   async getVideoData(avFileDescriptor: media.AVFileDescriptor): Promise<VideoSizeData> {
     let videoSize: VideoSizeData = new VideoSizeData();
     try {
       let avMetaDataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
       avMetaDataExtractor.fdSrc = avFileDescriptor;
       let metadata = await avMetaDataExtractor.fetchMetadata();
       videoSize.photoSize.width = parseInt(metadata.videoWidth as string);
       videoSize.photoSize.height = parseInt(metadata.videoHeight as string);
       if (metadata.duration) {
         videoSize.totalTime = parseInt(metadata.duration);
       }
       avMetaDataExtractor.release();
     } catch (error) {
       hilog.error(0x0000, TAG, `getVideoData catch error, code: ${error.code}, message: ${error.message}`);
     }
     return videoSize;
   }
   ```
3. 创建AVImageGenerator。

   ```typescript
   this.avImageGenerator = await media.createAVImageGenerator();
   if (this.avImageGenerator) {
     this.avImageGenerator.fdSrc = this.avFileDescriptor;
   } else {
     hilog.error(0X0000, TAG, 'Create AVImageGenerator failed!');
     return;
   }
   ```
4. 使用[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avimagegenerator.md#fetchframebytime12-1)方法来获取指定时间的缩略图，返回PixelMap格式的图片。

   ```typescript
   async fetchFrameByTime(time: number) {
     this.pixelMap = await this.avImageGenerator?.fetchFrameByTime(time,
       media.AVImageQueryOptions.AV_IMAGE_QUERY_CLOSEST_SYNC, this.videoSize.photoSize).catch((error: BusinessError)=>{
       hilog.error(0x0000, TAG, `release catch error, code: ${error.code}, message: ${error.message}`);
       return undefined;
     });
   }
   ```

### 实现效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/IflZwzAaTLWn4vcVCm-GXg/zh-cn_image_0000002706834590.gif)

## 常见问题

### 如何获取网络视频的缩略图

推荐使用系统在API20上的新增接口[setUrlSource()](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#seturlsource20)，在[AVMetadataExtractor](../harmonyos-references/arkts-apis-media-avmetadataextractor.md)实例中调用该接口获取网络视频url地址对应的数据源，再调用[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#fetchframebytime20)接口即可获取网络视频的缩略图。

## 示例代码

* [基于系统能力获取视频缩略图](https://gitcode.com/harmonyos_samples/VideoThumbnail)
