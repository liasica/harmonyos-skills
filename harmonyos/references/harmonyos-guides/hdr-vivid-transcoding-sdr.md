---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-vivid-transcoding-sdr
title: HDR Vivid视频转码SDR视频开发实践
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码开发实践 > HDR Vivid视频转码SDR视频开发实践
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:47+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:e35b9a905bab9ddc2939e7cd12fb6901606ba502cffdc3b50928e45005f0ca0a
---

## 概述

随着视频技术的发展，HDR（高动态范围）视频逐渐成为主流，其中HDR Vivid作为一种先进的HDR标准，能够提供更丰富的色彩和更广泛的亮度范围。然而，许多设备和平台仍然只支持SDR（标准动态范围）视频。因此，将HDR Vivid视频转码为SDR视频，以确保内容在更多设备上能够正常播放。将HDR Vivid视频转码成SDR视频是一个涉及多个技术要点的复杂过程。通过合理的转码处理，可以确保视频内容在不同设备上都能呈现出更佳的效果，不仅优化了视频的播放体验，还能满足更广泛受众的需求，因此很多场景下需要将HDR Vivid视频转码为SDR视频。

目前系统只支持从HDR Vivid类型转码为SDR视频，其他诸如HDR HLG或HDR 10类型的视频，要通过系统色彩空间转换能力将其转换为HDR Vivid类型后，才可进而转码为SDR类型视频。

在开始之前，建议已了解视频解码的[Surface模式](video-decoding.md#surface模式)、[视频色彩空间转换](video-csc.md)。

本文提供如下开发场景，以帮助开发者解决HDR视频转码SDR视频的问题：

* [基于AVTranscoder模块实现HDR Vivid视频到SDR视频转码](hdr-vivid-transcoding-sdr.md#基于avtranscoder模块实现hdr-vivid视频到sdr视频转码)
* [基于AVCodec模块实现HDR Vivid视频到SDR视频的色彩空间转换](hdr-vivid-transcoding-sdr.md#基于avcodec模块实现hdr-vivid视频到sdr视频的色彩空间转换)
* [基于VideoProcessing模块实现HDR Vivid视频到SDR视频的色彩空间转换](hdr-vivid-transcoding-sdr.md#基于videoprocessing模块实现hdr-vivid视频到sdr视频的色彩空间转换)
* [基于VideoProcessing模块转换HDR色彩空间](hdr-vivid-transcoding-sdr.md#基于videoprocessing模块转换hdr色彩空间)

## 基于AVTranscoder模块实现HDR Vivid视频到SDR视频转码

### 实现原理

使用[AVTranscoder](media-kit-intro.md#avtranscoder)可以实现视频转码功能，从API version 20开始支持视频转码的C/C++开发，转码功能可在手机、平板、PC/2in1等设备上作为系统提供的基础能力使用。可以通过调用[canIUse()](../harmonyos-references/js-apis-syscap.md#caniuse)接口来判断当前设备是否支持AVTranscoder，当canIUse("SystemCapability.Multimedia.Media.AVTranscoder")的返回值为true时，表示可以使用转码能力。转码步骤如下：初始化与准备阶段，调用[OH\_AVTranscoder\_Create()](../harmonyos-references/capi-avtranscoder-h.md#oh_avtranscoder_create)创建`OH\_AVTranscoder` 对象；启动与运行阶段，调用OH\_AVTranscoder\_Start()启动转码任务，此时可调用[OH\_AVTranscoder\_Pause()](../harmonyos-references/capi-avtranscoder-h.md#oh_avtranscoder_pause)暂停任务。在暂停状态下，可调用[OH\_AVTranscoder\_Resume()](../harmonyos-references/capi-avtranscoder-h.md#oh_avtranscoder_resume)恢复任务；任务进行时，若想取消该任务，可调用[OH\_AVTranscoder\_Cancel()](../harmonyos-references/capi-avtranscoder-h.md#oh_avtranscoder_cancel)终止转码任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/YpeAy3mmTEOdAxCCOySxxw/zh-cn_image_0000002712404714.png)

### 开发步骤

具体开发步骤，可参考[使用AVTranscoder实现视频转码(C/C++)](using-ndk-avtranscoder-for-transcodering.md)。

关键点：调用[OH\_AVTranscoderConfig\_SetDstVideoType()](../harmonyos-references/capi-avtranscoder-h.md#oh_avtranscoderconfig_setdstvideotype)设置输出视频的编码格式为“video/avc”。

```
OH_AVTranscoderConfig_SetDstVideoType(config, "video/avc");
```

1. 创建默认AVTranscoder配置，并设置输出视频的编码格式为“video/avc”。

   ```
   void AVTranscoder::CreateDefaultTransCoderConfig(int32_t dstFd) {
       config = OH_AVTranscoderConfig_Create();
       OH_AVTranscoderConfig_SetDstFD(config, dstFd);
       OH_AVTranscoderConfig_SetDstFileType(config, AV_OUTPUT_FORMAT_MPEG_4);
       OH_AVTranscoderConfig_SetDstVideoType(config, "video/avc");
       OH_AVTranscoderConfig_SetDstAudioType(config, "audio/mp4a-latm");
       OH_AVTranscoderConfig_SetDstAudioBitrate(config, 200000);
       OH_AVTranscoderConfig_SetDstVideoBitrate(config, 3000000);
   }
   ```
2. 进行AVTranscoder转码，并返回转码结果。

   ```
   int32_t AVTranscoder::StartAVTranscoder(const SampleInfo &sampleInfo) {
       result = 0;
       sampleInfo_ = sampleInfo;
       transcoder = OH_AVTranscoder_Create();
       CreateDefaultTransCoderConfig(sampleInfo.outputFd);
       OH_AVTranscoder_SetStateCallback(transcoder, AvTranscoderStateChangeCb, nullptr);
       OH_AVTranscoder_SetErrorCallback(transcoder, OnErrorCb, nullptr);
       OH_AVErrCode result =
           OH_AVTranscoderConfig_SetSrcFD(config, sampleInfo.inputFd, 0, sampleInfo.inputFileSize);
       if (result != AV_ERR_OK) {
           AVCODEC_SAMPLE_LOGI("Transcoder setSrcFD failed, ret %{public}d", result);
       }
       result = OH_AVTranscoder_Prepare(transcoder, config);
       if (result != AV_ERR_OK) {
           AVCODEC_SAMPLE_LOGI("Transcoder prepare failed, ret %{public}d", result);
       }
       result = OH_AVTranscoder_Start(transcoder);
       return result;
   }
   ```
3. 定义AVTranscoder状态改变函数，当状态为“AVTRANSCODER\_COMPLETED”时，释放AVTranscoder。

   ```
   void AVTranscoder::AvTranscoderStateChangeCb(OH_AVTranscoder *transcoder, OH_AVTranscoder_State state, void *userData) {
       if (transcoder == nullptr) {
           return;
       }
       switch (state) {
       case AVTRANSCODER_COMPLETED: {
           AVTranscoder::GetInstance().result = 1;
           AVTranscoder::GetInstance().ReleaseAVTranscoder();
           break;
       }
       default:
           break;
       }
   }
   ```
4. 在[OH\_AVTranscoder\_SetStateCallback()](../harmonyos-references/capi-avtranscoder-h.md#oh_avtranscoder_setstatecallback)中设置AvTranscoder状态改变监听。

   ```
   OH_AVTranscoder_SetStateCallback(transcoder, AvTranscoderStateChangeCb, nullptr);
   ```
5. 转码成功后，释放AVTranscoder。

   ```
   int32_t AVTranscoder::ReleaseAVTranscoder() {
       int ret = 0;
       AVCODEC_SAMPLE_LOGI("OH_AVTranscoder_Release ret:%{public}d", ret);
       if (transcoder != nullptr) {
           ret = OH_AVTranscoder_Release(transcoder);
           AVCODEC_SAMPLE_LOGI("OH_AVTranscoder_Release ret:%{public}d", ret);
           transcoder = nullptr;
       }
       if (config != nullptr) {
           ret = OH_AVTranscoderConfig_Release(config);
           AVCODEC_SAMPLE_LOGI("OH_AVTranscoderConfig_Release ret:%{public}d", ret);
           config = nullptr;
       }
       return ret;
   }
   ```

## 基于AVCodec模块实现HDR Vivid视频到SDR视频的色彩空间转换

### 实现原理

在视频分享或者编辑场景时，开发者有时需要将HDR Vivid视频转换为SDR视频，可以调用AVCodec能力实现该功能。

### 开发步骤

使用AVCodec色彩空间转换能力，主要的开发步骤为（详细开发步骤可参考[视频解码支持HDRVivid2SDR](hdrvivid2sdr.md)）：

1. 创建解码器实例，查询系统支持的解码器能力，根据查询结果基于name创建硬解码器。

   ```
   class VideoDecoder {
   // ...
   private:
       // ...
       OH_AVCodec *decoder_ = nullptr;
   };
   ```

   ```
   int32_t VideoDecoder::Create(SampleInfo &sampleInfo) {
       // ...
           OH_AVCapability *capability =
               OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_HEVC, false, HARDWARE);
           CHECK_AND_RETURN_RET_LOG(capability != nullptr, AVCODEC_SAMPLE_ERROR,
                                    "OH_AVCodec_GetCapabilityByCategory failed");
           const char *name = OH_AVCapability_GetName(capability);
           decoder_ = OH_VideoDecoder_CreateByName(name);
           // ...
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERROR, "Create VideoDecoder failed");
       return AVCODEC_SAMPLE_OK;
   }
   ```
2. 调用[OH\_VideoDecoder\_RegisterCallback()](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_registercallback)设置回调函数。

   ```
   int32_t VideoDecoder::SetCallback(CodecUserData *codecUserData) {
       int32_t ret =
           OH_VideoDecoder_RegisterCallback(decoder_,
                                            {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
                                             SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},
                                            codecUserData);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERROR, "Create SetCallback failed");
       return AVCODEC_SAMPLE_OK;
   }
   ```
3. 调用[OH\_VideoDecoder\_Configure()](../harmonyos-references/capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)配置解码器。必选配置项有：视频帧宽度、视频帧高度、视频像素格式、指定输出为SDR。

   ```
   int32_t VideoDecoder::Configure(const SampleInfo &sampleInfo) {
       OH_AVFormat *format = OH_AVFormat_Create();
       CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERROR, "Create AVFormat failed");
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
       OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_ROTATION, sampleInfo.rotation);
       // ...
           OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_DECODER_OUTPUT_COLOR_SPACE, OH_COLORSPACE_BT709_LIMIT);
           OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENABLE_LOW_LATENCY, 1);
           // ...
       int ret = OH_VideoDecoder_Configure(decoder_, format);
       OH_AVFormat_Destroy(format);
       format = nullptr;
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERROR, "VideoDecoder Configure failed");
       return AVCODEC_SAMPLE_OK;
   }
   ```
4. 目前仅Surface模式支持该能力，后续步骤具体可参考：视频解码的[Surface模式](video-decoding.md#surface模式)。

## 基于VideoProcessing模块实现HDR Vivid视频到SDR视频的色彩空间转换

### 实现原理

开发者可以调用[VideoProcessing](../harmonyos-references/capi-videoprocessing.md)模块提供的C API接口，实现HDR2SDR的色彩空间转换。支持的格式转换范围如下：

| 输入ColorSpace | 输入MetadataType | 输入pixelFormat | 输出ColorSpace | 输出MetadataType | 输出pixelFormat |
| --- | --- | --- | --- | --- | --- |
| OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | OH\_COLORSPACE\_BT709\_LIMIT | OH\_VIDEO\_NONE | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
| OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | OH\_COLORSPACE\_BT709\_LIMIT | OH\_VIDEO\_NONE | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |

### 开发步骤

HarmonyOS提供了Native侧的[VideoProcessing](../harmonyos-references/capi-videoprocessing.md)模块，可以将HDR Vivid视频转码成SDR视频，主要的开发步骤为（详细开发步骤可参考[视频色彩空间转换](video-csc.md)）：

1. 调用[OH\_VideoProcessing\_Create()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_create)创建视频处理实例。

   ```
   void VideoProcessing::SetProcessingSurface(SampleInfo &sampleInfo) {
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Create(&processor, VIDEO_PROCESSING_TYPE_COLOR_SPACE_CONVERSION);
       ret = OH_VideoProcessing_GetSurface(processor, &sampleInfo.inWindow);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_GetSurface failed");
   }
   ```

   调用[OH\_VideoProcessing\_GetSurface()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_getsurface)在视频处理启动之前创建输入surface。

   ```
   int32_t VideoEncoder::GetSurface(SampleInfo &sampleInfo) {
       int32_t ret;
       if (sampleInfo.processType > 1) {
           ret = OH_VideoEncoder_GetSurface(encoder_, &sampleInfo.outWindow);
       } else {
           ret = OH_VideoEncoder_GetSurface(encoder_, &sampleInfo.window);
       }
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERROR, "Get surface failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_OK;
   }
   ```
2. 调用[OH\_VideoProcessing\_SetSurface()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_setsurface)设置surface。

   ```
   int32_t err = 0;
   err = OH_NativeWindow_SetMetadataValue(sampleInfo.outWindow, OH_HDR_METADATA_TYPE, sizeof(uint8_t),
                                          (uint8_t *)&sampleInfo.outputFormat.metadataType);
   CHECK_AND_RETURN_LOG(err == 0, "SetMetadataValue BT2020_PQ_LIMIT failed");
   err = OH_NativeWindow_NativeWindowHandleOpt(sampleInfo.outWindow, SET_FORMAT, sampleInfo.outputFormat.pixelFormat);
   CHECK_AND_RETURN_LOG(err == 0, "NativeWindowHandleOpt BT2020_PQ_LIMIT failed");
   err = OH_NativeWindow_SetColorSpace(sampleInfo.outWindow,
                                       OH_NativeBuffer_ColorSpace(sampleInfo.outputFormat.colorSpace));
   CHECK_AND_RETURN_LOG(err == 0, "SetColorSpace failed");

   ret = OH_VideoProcessing_SetSurface(processor, sampleInfo.outWindow);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "SetSurface failed");
   ```
3. 调用[OH\_VideoProcessing\_RegisterCallback()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_registercallback)等函数创建并绑定回调函数。

   ```
   ret = OH_VideoProcessingCallback_Create(&callback);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_Create failed");
   ret = OH_VideoProcessingCallback_BindOnError(callback, OnError);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_BindOnError failed");
   ret = OH_VideoProcessingCallback_BindOnState(callback, OnState);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_BindOnState failed");
   ret = OH_VideoProcessingCallback_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_BindOnNewOutputBuffer failed");
   ret = OH_VideoProcessing_RegisterCallback(processor, callback, nullptr);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_RegisterCallback failed");
   ```
4. 调用[OH\_VideoProcessing\_Start()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_start)启动色彩空间转换处理。

   ```
   void VideoProcessing::StartProcessing() {
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Start(processor);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_Start failed");
   }
   ```
5. 调用[OH\_VideoProcessing\_Stop()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_stop)停止色彩空间转换处理。

   ```
   void VideoProcessing::StopProcessing() {
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Stop(processor);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_Stop failed");
       DestroyProcessing();
   }
   ```
6. 调用[OH\_VideoProcessing\_Destroy()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_destroy)及[OH\_VideoProcessing\_DeinitializeEnvironment()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_deinitializeenvironment)释放处理实例和资源。

   ```
   void VideoProcessing::DestroyProcessing() {
       CHECK_AND_RETURN_LOG(processor != nullptr, "processor is nullptr");
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_TAG, "start DestroyProcessing");
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Destroy(processor);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_Destroy failed");
       processor = nullptr;
       CHECK_AND_RETURN_LOG(callback != nullptr, "callback is nullptr");
       ret = OH_VideoProcessingCallback_Destroy(callback);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_Destroy failed");
       callback = nullptr;
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_TAG, "Destroy And Callback_Destroy succeed");
       OH_VideoProcessing_DeinitializeEnvironment();
   }
   ```

## 基于VideoProcessing模块转换HDR色彩空间

### 实现原理

开发者可以调用[VideoProcessing](../harmonyos-references/capi-videoprocessing.md)模块提供的C API接口，实现HDR2HDR的色彩空间转换。支持的转码范围如下：

| 输入ColorSpace | 输入MetadataType | 输入pixelFormat | 输出ColorSpace | 输出MetadataType | 输出pixelFormat |
| --- | --- | --- | --- | --- | --- |
| OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
| OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_VIDEO\_HDR\_HLG | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_VIDEO\_HDR\_HDR10 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
| OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_VIDEO\_HDR\_HLG | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
| OH\_COLORSPACE\_BT2020\_PQ\_HLG\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | OH\_COLORSPACE\_BT2020\_PQ\_HLG\_LIMIT | OH\_VIDEO\_HDR\_VIVID | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010, NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010, NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |

### 开发步骤

具体开发步骤，可参考[视频色彩空间转换](video-csc.md)。

1. 初始化环境并查询是否支持视频颜色空间转换。

   ```
   bool VideoProcessing::IsColorSpaceConversionSupported(SampleInfo &sampleInfo) {
       OH_VideoProcessing_InitializeEnvironment();
       return OH_VideoProcessing_IsColorSpaceConversionSupported(&sampleInfo.inputFormat, &sampleInfo.outputFormat);
   }
   ```
2. 设置输入输出的值。

   ```
   sampleInfo.inputFormat.metadataType = OH_VIDEO_HDR_VIVID;
   sampleInfo.inputFormat.colorSpace = OH_COLORSPACE_BT2020_HLG_LIMIT;
   sampleInfo.inputFormat.pixelFormat = NATIVEBUFFER_PIXEL_FMT_YCRCB_P010;
   sampleInfo.outputFormat.metadataType = OH_VIDEO_NONE;
   sampleInfo.outputFormat.colorSpace = OH_COLORSPACE_BT709_LIMIT;
   sampleInfo.outputFormat.pixelFormat = NATIVEBUFFER_PIXEL_FMT_YCBCR_420_SP;
   ```
3. 创建色彩空间转换模块，并获取Surface。

   ```
   void VideoProcessing::SetProcessingSurface(SampleInfo &sampleInfo) {
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Create(&processor, VIDEO_PROCESSING_TYPE_COLOR_SPACE_CONVERSION);
       ret = OH_VideoProcessing_GetSurface(processor, &sampleInfo.inWindow);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_GetSurface failed");
   }
   ```
4. 配置异步回调函数。

   ```
   void OnError(OH_VideoProcessing *videoProcessor, VideoProcessing_ErrorCode error, void *userData) {
       (void)videoProcessor;
       (void)error;
       (void)userData;
       OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, LOG_TAG, "OnError: %{public}d", error);
   }

   void OnState(OH_VideoProcessing *videoProcessor, VideoProcessing_State state, void *userData) {
       (void)videoProcessor;
       (void)state;
       (void)userData;
   }

   void OnNewOutputBuffer(OH_VideoProcessing *videoProcessor, uint32_t index, void *userData) {

       OH_VideoProcessing_RenderOutputBuffer(videoProcessor, index);
       (void)userData;
   }
   ```

   ```
   ret = OH_VideoProcessingCallback_Create(&callback);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_Create failed");
   ret = OH_VideoProcessingCallback_BindOnError(callback, OnError);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_BindOnError failed");
   ret = OH_VideoProcessingCallback_BindOnState(callback, OnState);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_BindOnState failed");
   ret = OH_VideoProcessingCallback_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_BindOnNewOutputBuffer failed");
   ret = OH_VideoProcessing_RegisterCallback(processor, callback, nullptr);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_RegisterCallback failed");
   ```
5. 设置Surface。

   ```
   int32_t err = 0;
   err = OH_NativeWindow_SetMetadataValue(sampleInfo.outWindow, OH_HDR_METADATA_TYPE, sizeof(uint8_t),
                                          (uint8_t *)&sampleInfo.outputFormat.metadataType);
   CHECK_AND_RETURN_LOG(err == 0, "SetMetadataValue BT2020_PQ_LIMIT failed");
   err = OH_NativeWindow_NativeWindowHandleOpt(sampleInfo.outWindow, SET_FORMAT, sampleInfo.outputFormat.pixelFormat);
   CHECK_AND_RETURN_LOG(err == 0, "NativeWindowHandleOpt BT2020_PQ_LIMIT failed");
   err = OH_NativeWindow_SetColorSpace(sampleInfo.outWindow,
                                       OH_NativeBuffer_ColorSpace(sampleInfo.outputFormat.colorSpace));
   CHECK_AND_RETURN_LOG(err == 0, "SetColorSpace failed");

   ret = OH_VideoProcessing_SetSurface(processor, sampleInfo.outWindow);
   CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "SetSurface failed");
   ```
6. 调用[OH\_VideoProcessing\_Start()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_start)启动色彩空间转换处理。

   ```
   void VideoProcessing::StartProcessing() {
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Start(processor);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_Start failed");
   }
   ```
7. 调用[OH\_VideoProcessing\_Stop()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_stop)停止色彩空间转换处理。

   ```
   void VideoProcessing::StopProcessing() {
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Stop(processor);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_Stop failed");
       DestroyProcessing();
   }
   ```

   调用[OH\_VideoProcessing\_Destroy()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_destroy)销毁视频处理实例。

   ```
   void VideoProcessing::DestroyProcessing() {
       CHECK_AND_RETURN_LOG(processor != nullptr, "processor is nullptr");
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_TAG, "start DestroyProcessing");
       VideoProcessing_ErrorCode ret = OH_VideoProcessing_Destroy(processor);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessing_Destroy failed");
       processor = nullptr;
       CHECK_AND_RETURN_LOG(callback != nullptr, "callback is nullptr");
       ret = OH_VideoProcessingCallback_Destroy(callback);
       CHECK_AND_RETURN_LOG(ret == VIDEO_PROCESSING_SUCCESS, "OH_VideoProcessingCallback_Destroy failed");
       callback = nullptr;
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_TAG, "Destroy And Callback_Destroy succeed");
       OH_VideoProcessing_DeinitializeEnvironment();
   }
   ```

## 示例代码

* [实现HDR视频转码SDR视频功能](https://gitcode.com/harmonyos_samples/hdr2sdr/tree/master/)
