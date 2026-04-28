---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-13
title: 如何进行视频压缩
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 如何进行视频压缩
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:45+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:82dc4835f55fa996b9c85f2fc094de038a520c8df9148a8b8a056cdcd2eaf558
---

**问题现象**

视频压缩处理是影音娱乐类应用中的典型场景之一，如上传、发送或保存视频时存在大小限制，需要对视频进行压缩，保证视频质量及大小满足用户需要。

**解决方案**

**方案一**

1. 利用三方库videocompressor的视频压缩功能来实现，具体步骤如下：

   ```
   1. static async selectVideo(selectNumber: number): Promise<photoAccessHelper.PhotoSelectResult> {
   2. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   3. // 设置要选择的媒体文件类型
   4. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE;
   5. // 设置选择文件最大数量
   6. photoSelectOptions.maxSelectNumber = selectNumber;
   7. let photoPicker = new photoAccessHelper.PhotoViewPicker();
   8. // PhotoViewPicker的select方法不需要特殊权限即可读取到图片或者视频文件
   9. return await photoPicker.select(photoSelectOptions);
   10. }
   ```

   [PictureUtils.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/common/PictureUtils.ets#L25-L34)

   ```
   1. // 获取视频路径
   2. async selectAndCompressVideo() {
   3. let selectResult: photoAccessHelper.PhotoSelectResult = await PictureUtils.selectVideo(1);
   4. // 得到选中视频的uri
   5. this.videoPath = selectResult.photoUris[0];
   6. hilog.info(0x0000, TAG, 'videoCompressor select selectFilePath:' + this.videoPath)
   7. }
   ```

   [VideoCompression.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/VideoCompression.ets#L46-L53)
2. 调用compressVideo方法并指定相应质量进行压缩。

   ```
   1. compressVideo(quality: CompressQuality, qualityTag: string) {
   2. this.quantity = qualityTag;
   3. let videoCompressor = new VideoCompressor();
   4. // 调用compressVideo方法并指定相应质量进行压缩
   5. videoCompressor.compressVideo(this.uiContext.getHostContext()!, this.videoPath, quality)
   6. .then((data) => {
   7. if (data.code == CompressorResponseCode.SUCCESS) {
   8. hilog.info(0x0000, TAG,
   9. 'videoCompressor ' + qualityTag + ' message:' + data.message + '--outputPath:' + data.outputPath);
   10. // 获取存在应用沙箱路径下的压缩后的视频文件，点击保存按钮后将其写入相册
   11. this.buffer = PictureUtils.compressVideo(data.outputPath);
   12. hilog.info(0x0000, TAG, `The buffer: ${JSON.stringify(this.buffer)}`);
   13. this.uiContext.showAlertDialog({ message: '已压缩完成，可执行下载!' });
   14. } else {
   15. hilog.info(0x0000, TAG,
   16. 'videoCompressor ' + qualityTag + ' code:' + data.code + '--error message:' + data.message);
   17. }
   18. }).catch((err: Error) => {
   19. hilog.info(0x0000, TAG, 'videoCompressor ' + qualityTag + ' get error message' + err.message);
   20. })
   21. }
   ```

   [VideoCompression.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/VideoCompression.ets#L57-L78)
3. 压缩完成后，视频保存至沙箱。

   ```
   1. try {
   2. let parentDir = this.uiContext.getHostContext()!.filesDir;
   3. let fileName: string = Date.now() + '-' + this.quantity + '.mp4';
   4. this.fileDir = parentDir + '/' + fileName;
   5. let file = await fileIo.open(this.fileDir, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   6. // 写入文件
   7. await fileIo.write(file.fd, this.buffer);
   8. this.compressedSize = (await fileIo.stat(file.fd)).size;
   9. // 关闭文件
   10. await fileIo.close(file.fd);
   11. this.uiContext.showAlertDialog({ message: '保存成功!' });
   12. } catch (error) {
   13. hilog.error(0x0000, TAG, 'error is' + JSON.stringify(error));
   14. this.uiContext.showAlertDialog({ message: '保存失败!' });
   15. }
   ```

   [VideoCompression.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/VideoCompression.ets#L134-L148)

**方案二**

使用AVCodec Kit视频编码功能，将未经压缩的视频数据传输至视频编码器进行编码处理，通过设定所需的编码格式、比特率、帧率等参数，并对编码输出进行控制，从而实现视频文件的压缩目的，编码器参数配置范围请参考：[获取支持的编解码能力](../harmonyos-guides/obtain-supported-codecs.md)。

```
1. int32_t VideoEncoder::Configure(const SampleInfo &sampleInfo) {
2. OH_AVFormat *format = OH_AVFormat_Create();
3. CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
7. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, sampleInfo.bitrateMode);
10. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, sampleInfo.bitrate);
11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, sampleInfo.hevcProfile);
12. // Setting HDRVivid-related parameters
13. if (sampleInfo.isHDRVivid) {
14. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, sampleInfo.iFrameInterval);
15. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, sampleInfo.rangFlag);
16. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, sampleInfo.primary);
17. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, sampleInfo.transfer);
18. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, sampleInfo.matrix);
19. }
20. // ...

22. // Setting the Encoder
23. int ret = OH_VideoEncoder_Configure(encoder_, format);
24. OH_AVFormat_Destroy(format);
25. format = nullptr;
26. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Config failed, ret: %{public}d", ret);
27. return AVCODEC_SAMPLE_ERR_OK;
28. }
```

[VideoEncoder.cpp](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/VideoEncoder.cpp#L118-L159)

示例代码参考：[基于AVCodec能力的视频编解码](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo)。

**方案三**

如果是视频拍摄过程中的场景，可通过AVRecorder设立录像输出流并调整自定义录像参数，从而调控视频文件的比特率与分辨率等特性，进而实现对视频文件大小的有效管理。

```
1. let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
2. if (!videoProfilesArray) {
3. Logger.error(TAG, 'createOutput videoProfilesArray === null || undefined');
4. }
5. // ...

7. let aVRecorderProfile: media.AVRecorderProfile = {
8. // ...
9. fileFormat: media.ContainerFormatType.CFT_MPEG_4,
10. videoBitrate: 2000000,
11. videoCodec: media.CodecMimeType.VIDEO_AVC,
12. videoFrameWidth: videoSize.width,
13. videoFrameHeight: videoSize.height,
14. videoFrameRate: 30
15. };

17. let aVRecorderConfig: media.AVRecorderConfig = {
18. // ...
19. videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
20. profile: aVRecorderProfile,
21. url: this.url,
22. rotation: 90,
23. // ...
24. };
```

[Record.ets](https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder/blob/master/entry/src/main/ets/pages/Record.ets#L167-L225)

示例代码参考：[基于CameraKit通过AVRecorder录像](https://gitcode.com/harmonyos_samples/camera-kit-avrecorder)。

**方案四**

ArkTS提供了AVTranscoder接口用于视频转码。视频的码率和分辨率是影响视频画质和文件大小的关键因素，通过AVTranscoder进行视频转码，可以实现节省视频存储空间和提高视频文件的设备兼容性。

AVTranscoder使用方式及常见问题请参考文档：[视频转码](../harmonyos-guides/using-avtranscoder-for-transcodering.md)。
