---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-thumbnail
title: 基于系统能力获取视频缩略图
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于系统能力获取视频缩略图
category: best-practices
scraped_at: 2026-04-29T14:11:38+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:6d7d02d432d1df948420d179befa4346e36c564e70db40eb2c498dec464642e9
---

## 概述

视频缩略图是视频的静态预览图像，是从视频中截取的某一帧画面，经常用作视频的封面。在视频浏览、分享和管理等场景中使用可以帮助用户快速浏览和选择想要的内容，提高用户的使用体验。HarmonyOS提供了对应的模块能力，帮助开发者获取视频文件的缩略图。根据应用获取缩略图策略的不同，可以分为以下两种场景：

* [获取视频默认缩略图](bpta-video-thumbnail.md#section14470163720352)
* [选取视频帧作为缩略图](bpta-video-thumbnail.md#section1848255103812)

## 获取视频默认缩略图

### 实现原理

视频的默认缩略图一般为视频的第一帧，可以通过[PhotoAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md)类的[getThumbnail()](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md#getthumbnail-2)方法获取。这里以获取图库视频缩略图场景为例。

### 开发步骤

1. 通过相册管理模块[@ohos.file.photoAccessHelper](../harmonyos-references/js-apis-photoaccesshelper.md)的[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)选取图库视频，获得视频的URL。

   ```
   1. /**
   2. * Pull up the gallery picker and select a video.
   3. * @returns The url of the selected video.
   4. */
   5. async selectVideo(): Promise<string> {
   6. try {
   7. let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
   8. return photoViewPicker.select({
   9. MIMEType: photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE,
   10. maxSelectNumber: 1
   11. }).then((photoSelectResult: photoAccessHelper.PhotoSelectResult): string => {
   12. if (photoSelectResult.photoUris.length <= 0) {
   13. return '';
   14. }
   15. return photoSelectResult.photoUris[0];
   16. })
   17. } catch (error) {
   18. hilog.error(0x0000, TAG, `selectVideo catch error, code: ${error.code}, message: ${error.message}`);
   19. return '';
   20. }
   21. }
   ```

   [PhotoUtils.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/common/utils/PhotoUtils.ets#L30-L51)
2. 使用[getAssets()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)方法，通过选择的图库视频的URL获取视频资源。

   ```
   1. // Obtain video resources.
   2. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
   3. predicates.equalTo('uri', videoUrl);
   4. let videoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
   5. await this.phAccessHelper.getAssets({
   6. fetchColumns: ['width', 'height', 'orientation'],
   7. predicates: predicates
   8. });
   9. let photoAsset: photoAccessHelper.PhotoAsset = await videoFetchResult.getFirstObject();
   ```

   [PhotoUtils.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/common/utils/PhotoUtils.ets#L61-L69)
3. 根据视频资源的属性配置缩略图的尺寸信息，调用getThumbnail()方法获取PixelMap格式的图片。

   ```
   1. // Configure thumbnail parameters.
   2. let thumbnailSize: Size = { width: 0, height: 0 };
   3. if (photoAsset.get(photoAccessHelper.PhotoKeys.ORIENTATION) === 90 ||
   4. photoAsset.get(photoAccessHelper.PhotoKeys.ORIENTATION) === 270) {
   5. thumbnailSize.width = photoAsset.get(photoAccessHelper.PhotoKeys.HEIGHT) as number;
   6. thumbnailSize.height = photoAsset.get(photoAccessHelper.PhotoKeys.WIDTH) as number;
   7. } else {
   8. thumbnailSize.width = photoAsset.get(photoAccessHelper.PhotoKeys.WIDTH) as number;
   9. thumbnailSize.height = photoAsset.get(photoAccessHelper.PhotoKeys.HEIGHT) as number;
   10. }
   11. return photoAsset.getThumbnail(thumbnailSize);
   ```

   [PhotoUtils.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/common/utils/PhotoUtils.ets#L72-L82)

说明

使用getAsset()和getThumbnail()方法需要申请受限开放权限'[ohos.permission.READ\_IMAGEVIDEO'](../harmonyos-guides/restricted-permissions.md#ohospermissionread_imagevideo)，对于需要克隆、备份或同步图片/视频类文件的应用可申请获取该权限，并通过[getAlbums()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums)方法获取相册资源再调用这两个方法获取缩略图。或者通过picker的方式可以在不获取权限的情况下，使用这两个方法来访问用户指定的图库资源获取缩略图。本文中的示例使用的是第二种picker的方式。

### 实现效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/XxnCh5QKTku5oubOIIc11g/zh-cn_image_0000002229450885.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061134Z&HW-CC-Expire=86400&HW-CC-Sign=D27A3E4D02C6C8B63AB8C4E3A3EBA85AE986A9D54514149FE2B0506738FE799D "点击放大")

## 选取视频帧作为缩略图

### 实现原理

HarmonyOS提供视频缩略图获取类[AVImageGenerator](../harmonyos-references/arkts-apis-media-avimagegenerator.md)用于选取视频指定时间的帧作为缩略图，这里以选取图库视频缩略图场景为例。

### 开发步骤

1. 拉起图库picker，选取视频获取文件资源描述符。

   ```
   1. /**
   2. * Obtain video resources through AVImageGenerator.
   3. */
   4. async imageGeneratorGetThumbnail() {
   5. this.photoUtils.selectVideo().then(async (result: string) => {
   6. // ...
   7. this.fileAlbum = fileIo.openSync(result, fileIo.OpenMode.READ_ONLY);
   8. this.avFileDescriptor = { fd: this.fileAlbum.fd };
   9. // ...
   10. }).catch((error: BusinessError) => {
   11. hilog.error(0x0000, TAG,
   12. `Invoke imageGeneratorGetThumbnail failed!, error code: ${error.code}, message: ${error.message}`);
   13. })
   14. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/pages/Index.ets#L79-L113)
2. 根据文件资源描述符获取视频元数据信息。

   ```
   1. /**
   2. * Get video infos through video file descriptor.
   3. * @param avFileDescriptor AVFileDescriptor of video.
   4. * @returns the size infos of video.
   5. */
   6. async getVideoData(avFileDescriptor: media.AVFileDescriptor): Promise<VideoSizeData> {
   7. let videoSize: VideoSizeData = new VideoSizeData();
   8. try {
   9. let avMetaDataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
   10. avMetaDataExtractor.fdSrc = avFileDescriptor;
   11. let metadata = await avMetaDataExtractor.fetchMetadata();
   12. videoSize.photoSize.width = parseInt(metadata.videoWidth as string);
   13. videoSize.photoSize.height = parseInt(metadata.videoHeight as string);
   14. if (metadata.duration) {
   15. videoSize.totalTime = parseInt(metadata.duration);
   16. }
   17. avMetaDataExtractor.release();
   18. } catch (error) {
   19. hilog.error(0x0000, TAG, `getVideoData catch error, code: ${error.code}, message: ${error.message}`);
   20. }
   21. return videoSize;
   22. }
   ```

   [PhotoUtils.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/common/utils/PhotoUtils.ets#L91-L113)
3. 创建AVImageGenerator。

   ```
   1. this.avImageGenerator = await media.createAVImageGenerator();
   2. if (this.avImageGenerator) {
   3. this.avImageGenerator.fdSrc = this.avFileDescriptor;
   4. } else {
   5. hilog.error(0X0000, TAG, 'Create AVImageGenerator failed!');
   6. return;
   7. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/pages/Index.ets#L99-L105)
4. 使用[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avimagegenerator.md#fetchframebytime12-1)方法来获取指定时间的缩略图，返回PixelMap格式的图片。

   ```
   1. /**
   2. * Obtain a frame at a certain point in time of the video.
   3. * @param time A certain point in time of the video.
   4. */
   5. async fetchFrameByTime(time: number) {
   6. this.pixelMap = await this.avImageGenerator?.fetchFrameByTime(time,
   7. media.AVImageQueryOptions.AV_IMAGE_QUERY_CLOSEST_SYNC, this.videoSize.photoSize).catch((error: BusinessError)=>{
   8. hilog.error(0x0000, TAG, `release catch error, code: ${error.code}, message: ${error.message}`);
   9. return undefined;
   10. });
   11. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/VideoThumbnail/blob/master/entry/src/main/ets/pages/Index.ets#L45-L55)

### 实现效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/maWFcknERlqIbc-V0cc0Qw/zh-cn_image_0000002194010608.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061134Z&HW-CC-Expire=86400&HW-CC-Sign=0EA8803CF8DF94CB03995FAB260E18C0DE4275A309A7A462C93664404E1E7A05 "点击放大")

## 常见问题

### 如何获取网络视频的缩略图

推荐使用系统在API20上的新增接口[setUrlSource()](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#seturlsource20)，在[AVMetadataExtractor](../harmonyos-references/arkts-apis-media-avmetadataextractor.md)实例中调用该接口获取网络视频url地址对应的数据源，再调用[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#fetchframebytime20)接口即可获取网络视频的缩略图。

## 示例代码

* [基于系统能力获取视频缩略图](https://gitcode.com/harmonyos_samples/VideoThumbnail)
