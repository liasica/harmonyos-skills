---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-13
title: 如何进行视频压缩
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 如何进行视频压缩
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d2352ab26938299fc5febce980ca9fce992b1db3af627fc79ec288450a991640
---

## 问题现象

视频压缩处理是影音娱乐类应用中的典型场景之一，如上传、发送或保存视频时存在大小限制，需要对视频进行压缩，保证视频质量及大小满足用户需要。

## 解决方案

* **方案一**
  1. 利用三方库videocompressor的视频压缩功能来实现，具体步骤如下：

     ```ts
     static async selectVideo(selectNumber: number): Promise<photoAccessHelper.PhotoSelectResult> {
       let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
       // 设置要选择的媒体文件类型
       photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE;
       // 设置选择文件最大数量
       photoSelectOptions.maxSelectNumber = selectNumber;
       let photoPicker = new photoAccessHelper.PhotoViewPicker();
       // PhotoViewPicker的select方法不需要特殊权限即可读取到图片或者视频文件
       return await photoPicker.select(photoSelectOptions);
     }
     ```

     ```ts
     // 获取视频路径
     async selectAndCompressVideo() {
       let selectResult: photoAccessHelper.PhotoSelectResult = await PictureUtils.selectVideo(1);
       // 得到选中视频的uri
       this.videoPath = selectResult.photoUris[0];
       hilog.info(0x0000, TAG, 'videoCompressor select selectFilePath:' + this.videoPath)
     }
     ```
  2. 调用compressVideo方法并指定相应质量进行压缩。

     ```ts
     compressVideo(quality: CompressQuality, qualityTag: string) {
       this.quantity = qualityTag;
       let videoCompressor = new VideoCompressor();
       // 调用compressVideo方法并指定相应质量进行压缩
       videoCompressor.compressVideo(this.uiContext.getHostContext()!, this.videoPath, quality)
         .then((data) => {
           if (data.code == CompressorResponseCode.SUCCESS) {
             hilog.info(0x0000, TAG,
               'videoCompressor ' + qualityTag + ' message:' + data.message + '--outputPath:' + data.outputPath);
             // 获取存在应用沙箱路径下的压缩后的视频文件，点击保存按钮后将其写入相册
             this.buffer = PictureUtils.compressVideo(data.outputPath);
             hilog.info(0x0000, TAG, `The buffer: ${JSON.stringify(this.buffer)}`);
             this.uiContext.showAlertDialog({ message: '已压缩完成，可执行下载!' });
           } else {
             hilog.info(0x0000, TAG,
               'videoCompressor ' + qualityTag + ' code:' + data.code + '--error message:' + data.message);
           }
         }).catch((err: Error) => {
         hilog.info(0x0000, TAG, 'videoCompressor ' + qualityTag + ' get error message' + err.message);
       })
     }
     ```
  3. 压缩完成后，视频保存至沙箱。

     ```ts
     try {
       let parentDir = this.uiContext.getHostContext()!.filesDir;
       let fileName: string = Date.now() + '-' + this.quantity + '.mp4';
       this.fileDir = parentDir + '/' + fileName;
       let file = await fileIo.open(this.fileDir, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
       // 写入文件
       await fileIo.write(file.fd, this.buffer);
       this.compressedSize = (await fileIo.stat(file.fd)).size;
       // 关闭文件
       await fileIo.close(file.fd);
       this.uiContext.showAlertDialog({ message: '保存成功!' });
     } catch (error) {
       hilog.error(0x0000, TAG, 'error is' + JSON.stringify(error));
       this.uiContext.showAlertDialog({ message: '保存失败!' });
     }
     ```
* **方案二**

  使用AVCodec Kit视频编码功能，将未经压缩的视频数据传输至视频编码器进行编码处理，通过设定所需的编码格式、比特率、帧率等参数，并对编码输出进行控制，从而实现视频文件的压缩目的，编码器参数配置范围请参考：[获取支持的编解码能力](../harmonyos-guides/obtain-supported-codecs.md)。

  ```ts
  int32_t VideoEncoder::Configure(const SampleInfo &sampleInfo) {
      OH_AVFormat *format = OH_AVFormat_Create();
      CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

      OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
      OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
      OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
      OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
      OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, sampleInfo.bitrateMode);
      OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, sampleInfo.bitrate);
      OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, sampleInfo.hevcProfile);
      // Setting HDRVivid-related parameters
      if (sampleInfo.isHDRVivid) {
          OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, sampleInfo.iFrameInterval);
          OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, sampleInfo.rangFlag);
          OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, sampleInfo.primary);
          OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, sampleInfo.transfer);
          OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, sampleInfo.matrix);
      }
      // ...

      // Setting the Encoder
      int ret = OH_VideoEncoder_Configure(encoder_, format);
      OH_AVFormat_Destroy(format);
      format = nullptr;
      CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Config failed, ret: %{public}d", ret);
      return AVCODEC_SAMPLE_ERR_OK;
  }
  ```

  示例代码参考：[基于AVCodec能力的视频编解码](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo)。
* **方案三**

  如果是视频拍摄过程中的场景，可通过AVRecorder设立录像输出流并调整自定义录像参数，从而调控视频文件的比特率与分辨率等特性，进而实现对视频文件大小的有效管理。

  ```ts
  let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
  if (!videoProfilesArray) {
    Logger.error(TAG, 'createOutput videoProfilesArray === null || undefined');
  }
  // ...

  let aVRecorderProfile: media.AVRecorderProfile = {
    // ...
    fileFormat: media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate: 2000000,
    videoCodec: media.CodecMimeType.VIDEO_AVC,
    videoFrameWidth: videoSize.width,
    videoFrameHeight: videoSize.height,
    videoFrameRate: 30
  };

  let aVRecorderConfig: media.AVRecorderConfig = {
    // ...
    videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
    profile: aVRecorderProfile,
    url: this.url,
    rotation: 90,
    // ...
  };
  ```

  示例代码参考：[基于CameraKit通过AVRecorder录像](https://gitcode.com/harmonyos_samples/camera-kit-avrecorder)。

* **方案四**

  ArkTS提供了AVTranscoder接口用于视频转码。视频的码率和分辨率是影响视频画质和文件大小的关键因素，通过AVTranscoder进行视频转码，可以实现节省视频存储空间和提高视频文件的设备兼容性。

  AVTranscoder使用方式及常见问题请参考文档：[视频转码](../harmonyos-guides/using-avtranscoder-for-transcodering.md)。
