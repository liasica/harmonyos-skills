---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-transcoding-buffer
title: 基于Buffer模式进行视频转码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码开发实践 > 基于Buffer模式进行视频转码
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:47+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:44df624df7f8cc09244e1a471a4aee178d0c33509962876c2164a2032127ef73
---

## 概述

视频转码是指通过调整编码、比特率、分辨率、帧率、文件格式等参数将视频文件从一种格式转换为另一种格式的过程。Buffer模式是系统提供的一种视频编解码的方式，是媒体子系统的核心能力。在Buffer模式中，编码或解码完成的数据会以共享内存的方式输出，开发者可以获取共享内存的地址和数据信息，适用于视频转码、编辑等场景。

本文主要介绍了视频编解码的基本概念、Buffer模式下的视频编解码原理，并详细介绍了视频转码的实现方案和开发步骤。

## 实现原理

### 基本概念

视频文件格式是视频保存的格式，常见的格式有MP4、AVI等。在视频文件（以MP4文件解码为例）解码时，首先需要将视频进行解封装，解封装会将一个封装好的音视频文件（如MP4、FLV等）中的音频和视频数据流分离出来。然后，从数据流中取出视频的媒体样本sample，通过视频解码器将媒体数据解码成YUV数据，流程如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/y9yoj-mKT0SwOR4j9pzYqQ/zh-cn_image_0000002742123663.png)

在视频文件编码（以MP4文件编码为例）时，首先会通过视频编码器对YUV数据进行编码，将未压缩的视频数据YUV压缩成视频码流H.264，然后，将编码后的媒体数据按一定的格式封装存储到MP4文件里，流程如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ZxX0HR6iSvOf74LOn-7Hvg/zh-cn_image_0000002712244750.png)

关于视频文件编解码支持的格式，详情请参考[AVCodec支持的格式](avcodec-support-formats.md)。

### YUV跨距对齐

YUV是一类真彩色（true-color）颜色空间（color space），Y'UV、YUV等相关专有名词都属于YUV色彩空间范畴。I420、NV12、NV21等是YUV具体的存储格式。I420和YV12属于YUV420P格式，NV12和NV21属于YUV420SP格式。

由于硬件内存访问对齐要求，YUV图像数据在写入内存缓冲区时，其每行数据的存储长度会被硬件或底层驱动自动扩展至规定的对齐粒度（例如16/32/64字节），即YUV跨距对齐。在YUV跨距对齐时，会对每行有效像素数据进行边界填充（Padding），导致Stride值大于图像的有效像素宽度（以字节计算）。

以I420格式为例，其跨距对齐后的格式如下所示。其中，w\_stride是数据填充后的宽跨距，h\_stride是数据填充后的高跨距，height是实际的高度，width是实际的宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/hvntb4L4QSWBWCjCEIdlHg/zh-cn_image_0000002742003703.png)

### 视频编解码原理

视频编解码器的原理和实现机制是一样的，区别是处理的数据有所不同。在编码时，输入数据是原始数据（YUV），输出数据是视频数据（如H.264），解码的过程与编码相反。这里以视频解码的过程进行原理说明。

在视频解码的过程中，主要包含两个部分，分别为输入数据流转和输出数据流转。开发者需要通过输入数据流转将需要解码的数据填充给解码器，解码器再进行解码处理。在输出数据流转中，解码器会将解码完成的数据返回给开发者使用，在开发者使用完毕后，需要通知解码器释放视频数据，从而实现整体的Buffer循环，详细原理流程如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/FIn5C2kyQ4CmcBI6HLmVmQ/zh-cn_image_0000002712404716.png)

输入数据流转的步骤如下所示。

1. 解码器提供空的Buffer地址，该地址用于填充需要解码的视频数据。
2. 将解封装后的视频数据（如H.264）填充到解码器提供的Buffer地址中。
3. 通知解码器，当前Buffer地址已完成视频数据填充。
4. 当解码器收到通知后，会对数据进行解码操作。

输出数据流转的步骤如下所示。

1. 在完成输出数据流转后，解码器会提供已解码的数据。
2. 获取数据后，开发者可以根据实际业务使用视频数据，如送显到屏幕。
3. 使用完毕后，开发者需要将Buffer的使用权移交给解码器。
4. 解码器会循环再利用Buffer地址。Buffer内的视频数据不会被释放或者清零，而是在下一次循环中，将解码好的数据直接覆盖写入到已经空闲的Buffer地址里。

## 视频转码

### 场景描述

不同的设备和平台支持视频格式各有不同，通过转码可以将视频转化成设备或平台适配的格式，从而确保视频能够正确地播放与观看，提高视频的兼容性和可播放性。例如，部分平台仅支持特定的视频格式。在相同的视频格式下，其分辨率、帧率、比特率等参数也各有不同，通过改变相应的参数，可以缩小视频文件的大小，从而节省视频的存储空间。

在ArkTS侧，系统提供了转码的相关接口AVTranscoder，可以实现简单的视频转码操作。而在复杂的场景下，如视频裁剪等场景，则需要调用系统的视频编解码的相关能力进行实现。在Buffer模式下的视频转码，可以对视频数据进行读写操作，能够满足更加灵活多变的场景需求。

### 开发步骤

在视频转码的场景中，视频文件会经历解封装、视频解码、视频编码和视频封装的步骤，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/2a1RUBitT5m_MHS9bQDfHg/zh-cn_image_0000002742123665.png)

其主要包含三个大步骤。

**1. 视频编解码环境初始化**：为后续视频编码、解码提前创建好对应的实例，并设置编解码所需要的参数。

**2. 视频文件解码**：视频文件解码包含了视频解封装、视频解码的操作，最后生成解码后的视频数据。

**3. 视频文件编码**：将解码后的数据进行拷贝处理，并通过编码器进行编码，最后封装到对应的视频文件中。

**视频编解码环境初始化**开发步骤如下所示。

1. 创建与配置解封装器。
2. 创建与配置解码器，并注册解码器的回调函数。其中，回调函数OnNeedInputBuffer()提供了解码空Buffer地址，回调函数OnNewOutputBuffer()提供了解码后的视频数据。
3. 创建与配置封装器。
4. 创建与配置编码器，并注册编码器的回调函数，回调函数需要配置的内容与解码器相同。

在视频文件解码中，主要包含两个步骤，输入缓存处理、输出缓存处理。在OnNeedInputBuffer()回调函数中，维护了一个空Buffer的缓存队列，在实现输入缓存处理时，需要解封装、填充视频数据。在OnNewOutputBuffer()回调函数中，维护了一个已解码视频数据的缓存队列，在实现输出缓存处理时，需要处理视频数据，其调用顺序如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/IIAzKkIUSRyayZOock2WZw/zh-cn_image_0000002712244752.png)

**视频文件解码**开发步骤如下所示。

1. 通过inputBufferInfoQueue获取视频缓存空地址。
2. 通过Demuxer读取媒体数据，即视频码流数据及其格式。
3. 在OH\_VideoDecoder\_PushInputBuffer()中设置对应的视频缓存数据。
4. 在解码完成后，通过outputBufferInfoQueue获取视频缓存数据。
5. 处理缓存数据，最后通过OH\_VideoDecoder\_FreeOutputBuffer()刷新缓存，将缓存资源返回给解码器。

**视频文件编码**开发步骤如下所示。在视频文件编码中，大致的处理流程与视频文件解码类似，而编码的输入缓存的数据来源于解码的输出缓存，所以，可以在解码的输出缓存处理子线程中同步处理编码的输入缓存数据。

1. 通过inputBufferInfoQueue获取视频缓存地址。
2. 将解码的输出缓存数据拷贝到编码的输入缓存中。
3. 通过OH\_VideoEncoder\_PushInputBuffer()将已填充的输入缓存提交给编码器。
4. 在编码完成后，通过outputBufferInfoQueue获取视频缓存数据。
5. 通过Muxer将编码完成的视频数据写入到视频文件中

### 代码实现

1. 视频编解码环境初始化。

   * 初始化视频解码环境。

     ```
     int32_t Transcoding::InitDecoder() {
         CHECK_AND_RETURN_RET_LOG(!isStarted_, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
         CHECK_AND_RETURN_RET_LOG(demuxer_ == nullptr && videoDecoder_ == nullptr,
                                  AVCODEC_SAMPLE_ERR_ERROR, "Already started.");

         videoDecoder_ = std::make_unique<VideoDecoder>();
         demuxer_ = std::make_unique<Demuxer>();

         isReleased_ = false;
         int32_t ret = demuxer_->Create(sampleInfo_);

         if (ret == AVCODEC_SAMPLE_ERR_OK) {
             ret = CreateVideoDecoder();
         } else {
             AVCODEC_SAMPLE_LOGE("Create audio decoder failed");
         }
         return ret;
     }
     ```
   * 创建解封装器。在创建解封装器时，需要根据需要解码的视频文件fd创建对应的OH\_AVSource对象，再根据该对象创建对应的解码器。

     ```
     int32_t Demuxer::Create(SampleInfo &info) {
         source_ = OH_AVSource_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
         CHECK_AND_RETURN_RET_LOG(source_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR,
                                  "Create demuxer source failed, fd: %{public}d, offset: %{public}" PRId64
                                  ", file size: %{public}" PRId64,
                                  info.inputFd, info.inputFileOffset, info.inputFileSize);
         demuxer_ = OH_AVDemuxer_CreateWithSource(source_);
         CHECK_AND_RETURN_RET_LOG(demuxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create demuxer failed");

         auto sourceFormat = std::shared_ptr<OH_AVFormat>(OH_AVSource_GetSourceFormat(source_), OH_AVFormat_Destroy);
         CHECK_AND_RETURN_RET_LOG(sourceFormat != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Get source format failed");

         int32_t ret = GetTrackInfo(sourceFormat, info);
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Get video track info failed");

         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 创建完解封装器后，可以通过解封装器获取视频对应的参数，如视频的宽高、帧率等信息。

     ```
     int32_t Demuxer::GetTrackInfo(std::shared_ptr<OH_AVFormat> sourceFormat, SampleInfo &info) {
         int32_t trackCount = 0;
         OH_AVFormat_GetIntValue(sourceFormat.get(), OH_MD_KEY_TRACK_COUNT, &trackCount);
         for (int32_t index = 0; index < trackCount; index++) {
             int trackType = -1;
             auto trackFormat =
                 std::shared_ptr<OH_AVFormat>(OH_AVSource_GetTrackFormat(source_, index), OH_AVFormat_Destroy);
             OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_TRACK_TYPE, &trackType);
             if (trackType == MEDIA_TYPE_VID) {
                 OH_AVDemuxer_SelectTrackByID(demuxer_, index);
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_WIDTH, &info.videoWidth);
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_HEIGHT, &info.videoHeight);
                 OH_AVFormat_GetDoubleValue(trackFormat.get(), OH_MD_KEY_FRAME_RATE, &info.frameRate);
                 OH_AVFormat_GetLongValue(trackFormat.get(), OH_MD_KEY_BITRATE, &info.bitrate);
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_ROTATION, &info.rotation);
                 char *videoCodecMime;
                 OH_AVFormat_GetStringValue(trackFormat.get(), OH_MD_KEY_CODEC_MIME,
                                            const_cast<char const **>(&videoCodecMime));
                 info.videoCodecMime = videoCodecMime;
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_PROFILE, &info.hevcProfile);
                 videoTrackId_ = index;

                 AVCODEC_SAMPLE_LOGI("====== Demuxer Video config ======");
                 AVCODEC_SAMPLE_LOGI("Mime: %{public}s", videoCodecMime);
                 AVCODEC_SAMPLE_LOGI("%{public}d*%{public}d, %{public}.1ffps, %{public}" PRId64 "kbps", info.videoWidth,
                                     info.videoHeight, info.frameRate, info.bitrate / 1024);
                 AVCODEC_SAMPLE_LOGI("====== Demuxer Video config ======");
             } else if (trackType == MEDIA_TYPE_AUD) {
                 OH_AVDemuxer_SelectTrackByID(demuxer_, index);
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUDIO_SAMPLE_FORMAT, &info.audioSampleForamt);
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUD_CHANNEL_COUNT, &info.audioChannelCount);
                 OH_AVFormat_GetLongValue(trackFormat.get(), OH_MD_KEY_CHANNEL_LAYOUT, &info.audioChannelLayout);
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUD_SAMPLE_RATE, &info.audioSampleRate);
                 char *audioCodecMime;
                 OH_AVFormat_GetStringValue(trackFormat.get(), OH_MD_KEY_CODEC_MIME,
                                            const_cast<char const **>(&audioCodecMime));
                 uint8_t *codecConfig = nullptr;
                 OH_AVFormat_GetBuffer(trackFormat.get(), OH_MD_KEY_CODEC_CONFIG, &codecConfig, &info.codecConfigLen);
                 if (info.codecConfigLen > 0 && info.codecConfigLen < sizeof(info.codecConfig)) {
                     memcpy(info.codecConfig, codecConfig, info.codecConfigLen);
                     AVCODEC_SAMPLE_LOGI(
                         "codecConfig:%{public}p, len:%{public}i, 0:0x%{public}02x 1:0x:%{public}02x, bufLen:%{public}u",
                         info.codecConfig, (int)info.codecConfigLen, info.codecConfig[0], info.codecConfig[1],
                         sizeof(info.codecConfig));
                 }
                 OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AAC_IS_ADTS, &info.aacAdts);
                 
                 info.audioCodecMime = audioCodecMime;
                 audioTrackId_ = index;

                 AVCODEC_SAMPLE_LOGI("====== Demuxer Audio config ======");
                 AVCODEC_SAMPLE_LOGI(
                     "audioMime:%{public}s sampleForamt:%{public}d "
                     "sampleRate:%{public}d channelCount:%{public}d channelLayout:%{public}d adts:%{public}i",
                     info.audioCodecMime.c_str(), info.audioSampleForamt, info.audioSampleRate, info.audioChannelCount,
                     info.audioChannelLayout, info.aacAdts);
                 AVCODEC_SAMPLE_LOGI("====== Demuxer Audio config ======");
             }
         }

         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 创建视频解码器。

     ```
     int32_t Transcoding::CreateVideoDecoder() {
         AVCODEC_SAMPLE_LOGW("video mime:%{public}s", sampleInfo_.videoCodecMime.c_str());
         int32_t ret = videoDecoder_->Create(sampleInfo_.videoCodecMime);
         if (ret != AVCODEC_SAMPLE_ERR_OK) {
             AVCODEC_SAMPLE_LOGW("Create video decoder failed, mime:%{public}s", sampleInfo_.videoCodecMime.c_str());
         } else {
             videoDecContext_ = new CodecUserData;
             ret = videoDecoder_->Config(sampleInfo_, videoDecContext_);
             CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Video Decoder config failed");
         }
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 配置视频解码器，包括视频的宽、高、分辨率等基础信息和解码器的回调函数。

     ```
     int32_t VideoDecoder::SetCallback(CodecUserData *codecUserData) {
         int32_t ret = AV_ERR_OK;
         ret = OH_VideoDecoder_RegisterCallback(decoder_,
                                                {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
                                                 SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},
                                                codecUserData);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Set callback failed, ret: %{public}d", ret);

         return AVCODEC_SAMPLE_ERR_OK;
     }

     int32_t VideoDecoder::Configure(const SampleInfo &sampleInfo) {
         OH_AVFormat *format = OH_AVFormat_Create();
         CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

         OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
         OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.frameRate);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_ROTATION, sampleInfo.rotation);

         AVCODEC_SAMPLE_LOGI("====== VideoDecoder config ======");
         AVCODEC_SAMPLE_LOGI("%{public}d*%{public}d, %{public}.1ffps", sampleInfo.videoWidth, sampleInfo.videoHeight,
                             sampleInfo.frameRate);
         AVCODEC_SAMPLE_LOGI("====== VideoDecoder config ======");
         int ret = OH_VideoDecoder_Configure(decoder_, format);
         OH_AVFormat_Destroy(format);
         format = nullptr;
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Config failed, ret: %{public}d", ret);
         return AVCODEC_SAMPLE_ERR_OK;
     }

     int32_t VideoDecoder::Config(const SampleInfo &sampleInfo, CodecUserData *codecUserData) {
         CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");
         CHECK_AND_RETURN_RET_LOG(codecUserData != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Invalid param: codecUserData");

         int32_t ret = Configure(sampleInfo);
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Configure failed");
         
         ret = SetCallback(codecUserData);
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR,
                                  "Set callback failed, ret: %{public}d", ret);

         ret = OH_VideoDecoder_Prepare(decoder_);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Prepare failed, ret: %{public}d", ret);

         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 初始化视频编码环境，包括创建配置视频编码器、视频封装器。

     **说明** 

     + 系统支持的封装格式有限，支持的格式列表请参考[AVCodec支持的格式](avcodec-support-formats.md)。
     + 常规视频转码、录制、播放场景均包含音、视频双路流。本示例仅聚焦视频流处理，相关能力请参考[音视频编解码](audio-video-codec.md)。

     ```
     int32_t Transcoding::InitEncoder() {
         CHECK_AND_RETURN_RET_LOG(!isStarted_, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
         CHECK_AND_RETURN_RET_LOG(muxer_ == nullptr && videoEncoder_ == nullptr,
                                  AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
         
         videoEncoder_ = std::make_unique<VideoEncoder>();
         muxer_ = std::make_unique<Muxer>();
         
         int32_t ret = muxer_->Create(sampleInfo_.outputFd);
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create muxer with fd(%{public}d) failed",
                                  sampleInfo_.outputFd);
         ret = muxer_->Config(sampleInfo_);
         
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create audio encoder failed");

         ret = CreateVideoEncoder();
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create video encoder failed");
         
         AVCODEC_SAMPLE_LOGI("Succeed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 创建视频编码器。

     ```
     int32_t VideoEncoder::Create(const std::string &videoCodecMime) {
         encoder_ = OH_VideoEncoder_CreateByMime(videoCodecMime.c_str());
         CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create failed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 配置视频编码器。

     ```
     int32_t VideoEncoder::Config(SampleInfo &sampleInfo, CodecUserData *codecUserData) {
         CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Encoder is null");
         CHECK_AND_RETURN_RET_LOG(codecUserData != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Invalid param: codecUserData");

         int32_t ret = Configure(sampleInfo);
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Configure failed");

         ret = SetCallback(codecUserData);
         CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR,
                                  "Set callback failed, ret: %{public}d", ret);

         ret = OH_VideoEncoder_Prepare(encoder_);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Prepare failed, ret: %{public}d", ret);

         return AVCODEC_SAMPLE_ERR_OK;
     }

     // ...

     int32_t VideoEncoder::Configure(const SampleInfo &sampleInfo) {
         OH_AVFormat *format = OH_AVFormat_Create();
         CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

         OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
         OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.outputFrameRate);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, sampleInfo.bitrateMode);
         OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, sampleInfo.outputBitrate);
         OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, sampleInfo.hevcProfile);
         if (sampleInfo.isHDRVivid) {
             OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, sampleInfo.iFrameInterval);
             OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, sampleInfo.rangFlag);
             OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, sampleInfo.primary);
             OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, sampleInfo.transfer);
             OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, sampleInfo.matrix);
         }
         AVCODEC_SAMPLE_LOGI("====== VideoEncoder config ======");
         AVCODEC_SAMPLE_LOGI("%{public}d*%{public}d, %{public}.1ffps", sampleInfo.videoWidth, sampleInfo.videoHeight,
                             sampleInfo.frameRate);
         AVCODEC_SAMPLE_LOGI("BitRate Mode: %{public}d, BitRate: %{public}" PRId64 "kbps", sampleInfo.bitrateMode,
                             sampleInfo.bitrate / 1024);
         AVCODEC_SAMPLE_LOGI("====== VideoEncoder config ======");
         
         int ret = OH_VideoEncoder_Configure(encoder_, format);
         OH_AVFormat_Destroy(format);
         format = nullptr;
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Config failed, ret: %{public}d", ret);
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 配置视频封装器。在配置视频封装器时，需要设置视频封装的格式，包括视频宽高、帧率、编码格式等。

     ```
     int32_t Muxer::Config(SampleInfo &sampleInfo) {
         CHECK_AND_RETURN_RET_LOG(muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Muxer is null");
         OH_AVFormat *formatAudio = OH_AVFormat_CreateAudioFormat(sampleInfo.audioCodecMime.data(),
                                                                  sampleInfo.audioSampleRate, sampleInfo.audioChannelCount);
         CHECK_AND_RETURN_RET_LOG(formatAudio != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create audio format failed");
         OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_PROFILE, AAC_PROFILE_LC);
         int32_t ret = OH_AVMuxer_AddTrack(muxer_, &audioTrackId_, formatAudio);
         OH_AVFormat_Destroy(formatAudio);
         
         OH_AVFormat *formatVideo =
             OH_AVFormat_CreateVideoFormat(sampleInfo.outputVideoCodecMime.data(), sampleInfo.videoWidth, sampleInfo.videoHeight);
         CHECK_AND_RETURN_RET_LOG(formatVideo != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create video format failed");

         OH_AVFormat_SetDoubleValue(formatVideo, OH_MD_KEY_FRAME_RATE, sampleInfo.outputFrameRate);
         OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
         OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
         OH_AVFormat_SetStringValue(formatVideo, OH_MD_KEY_CODEC_MIME, sampleInfo.outputVideoCodecMime.data());
         if (sampleInfo.isHDRVivid) {
             OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_VIDEO_IS_HDR_VIVID, 1);
             OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_RANGE_FLAG, sampleInfo.rangFlag);
             OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_COLOR_PRIMARIES, sampleInfo.primary);
             OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_TRANSFER_CHARACTERISTICS, sampleInfo.transfer);
             OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_MATRIX_COEFFICIENTS, sampleInfo.matrix);
         }

         ret = OH_AVMuxer_AddTrack(muxer_, &videoTrackId_, formatVideo);
         OH_AVFormat_Destroy(formatVideo);
         formatVideo = nullptr;
         OH_AVMuxer_SetRotation(muxer_, sampleInfo.rotation);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "AddTrack failed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
2. 视频文件解码。

   * 启动视频转码，包括视频解码输入缓存处理线程、输出缓存处理线程、编码输出缓存处理线程。

     ```
     int32_t Transcoding::Start() {
         std::unique_lock<std::mutex> lock(mutex_);
         int32_t ret;
         CHECK_AND_RETURN_RET_LOG(!isStarted_, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
         CHECK_AND_RETURN_RET_LOG(demuxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
         if (videoDecContext_) {
             ret = videoDecoder_->Start();
             if (ret != AVCODEC_SAMPLE_ERR_OK) {
                 AVCODEC_SAMPLE_LOGE("Video Decoder start failed");
                 lock.unlock();
                 StartRelease();
                 return AVCODEC_SAMPLE_ERR_ERROR;
             }
             isStarted_ = true;
             videoDecInputThread_ = std::make_unique<std::thread>(&Transcoding::VideoDecInputThread, this);
             videoDecOutputThread_ = std::make_unique<std::thread>(&Transcoding::VideoDecOutputThread, this);

             if (videoDecInputThread_ == nullptr || videoDecOutputThread_ == nullptr) {
                 AVCODEC_SAMPLE_LOGE("Create thread failed");
                 lock.unlock();
                 StartRelease();
                 return AVCODEC_SAMPLE_ERR_ERROR;
             }
         }

         if (videoEncContext_) {
             CHECK_AND_RETURN_RET_LOG(videoEncoder_ != nullptr && muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR,
                                      "Already started.");
             int32_t ret = muxer_->Start();
             CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Muxer start failed");
             ret = videoEncoder_->Start();
             CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Encoder start failed");
             videoEncOutputThread_ = std::make_unique<std::thread>(&Transcoding::VideoEncOutputThread, this);
             if (videoEncOutputThread_ == nullptr) {
                 AVCODEC_SAMPLE_LOGE("Create thread failed");
                 StartRelease();
                 return AVCODEC_SAMPLE_ERR_ERROR;
             }
         }
         
         audioThread_ = std::make_unique<std::thread>(&Transcoding::AudioTranscoderThread, this);
         AVCODEC_SAMPLE_LOGI("Succeed");
         doneCond_.notify_all();
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 视频解码输入缓存处理。

     ```
     void Transcoding::VideoDecInputThread() {
         while (true) {
             CHECK_AND_BREAK_LOG(isStarted_, "Decoder input thread out");
             std::unique_lock<std::mutex> lock(videoDecContext_->inputMutex);
             bool condRet = videoDecContext_->inputCond.wait_for(
                 lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->inputBufferInfoQueue.empty(); });
             CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
             CHECK_AND_CONTINUE_LOG(!videoDecContext_->inputBufferInfoQueue.empty(),
                                    "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

             CodecBufferInfo bufferInfo = videoDecContext_->inputBufferInfoQueue.front();
             videoDecContext_->inputBufferInfoQueue.pop();
             videoDecContext_->inputFrameCount++;
             lock.unlock();

             demuxer_->ReadSample(demuxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                                  bufferInfo.attr);

             int32_t ret = videoDecoder_->PushInputBuffer(bufferInfo);
             CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Push data failed, thread out");

             CHECK_AND_BREAK_LOG(!(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS),
                                 "VideoDecInputThread Catch EOS, thread out");
         }
     }
     ```
   * 视频解码输出缓存处理。

     ```
     void Transcoding::VideoDecOutputThread() {
         sampleInfo_.frameInterval = MICROSECOND / sampleInfo_.frameRate;
         while (true) {
             CHECK_AND_BREAK_LOG(isStarted_, "Decoder output thread out");
             std::unique_lock<std::mutex> lock(videoDecContext_->outputMutex);
             bool condRet = videoDecContext_->outputCond.wait_for(lock, 5s, [this]() {
                 return !isStarted_ ||
                        !(videoDecContext_->outputBufferInfoQueue.empty() && videoEncContext_->inputBufferInfoQueue.empty());
             });
             CHECK_AND_BREAK_LOG(isStarted_, "Decoder output thread out");
             CHECK_AND_CONTINUE_LOG(!videoDecContext_->outputBufferInfoQueue.empty(),
                                    "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
             CHECK_AND_CONTINUE_LOG(!videoEncContext_->inputBufferInfoQueue.empty(),
                                    "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

             CodecBufferInfo bufferInfo = videoDecContext_->outputBufferInfoQueue.front();
             videoDecContext_->outputBufferInfoQueue.pop();
             videoDecContext_->outputFrameCount++;
             AVCODEC_SAMPLE_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
                                 videoDecContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                                 bufferInfo.attr.pts);
             lock.unlock();

             CodecBufferInfo encBufferInfo = videoEncContext_->inputBufferInfoQueue.front();
             videoEncContext_->inputBufferInfoQueue.pop();
             videoEncContext_->inputFrameCount++;
             
             AVCODEC_SAMPLE_LOGW(
                 "Out bufferInfo flags: %{public}u, offset: %{public}d, pts: %{public}u, size: %{public}" PRId64,
                 bufferInfo.attr.flags, bufferInfo.attr.offset, bufferInfo.attr.pts, bufferInfo.attr.size);

             encBufferInfo.bufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(encBufferInfo.buffer));
             bufferInfo.bufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
             CopyStrideYUV420SP(encBufferInfo, bufferInfo);

             AVCODEC_SAMPLE_LOGW(
                 "Out encBufferInfo flags: %{public}u, offset: %{public}d, pts: %{public}u, size: %{public}d" PRId64,
                 encBufferInfo.attr.flags, encBufferInfo.attr.offset, encBufferInfo.attr.pts, encBufferInfo.attr.size);

             OH_AVBuffer_SetBufferAttr(reinterpret_cast<OH_AVBuffer *>(encBufferInfo.buffer), &encBufferInfo.attr);

             int32_t ret = videoDecoder_->FreeOutputBuffer(bufferInfo.bufferIndex, false);
             CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Decoder output thread out");

             videoEncoder_->PushInputBuffer(encBufferInfo);

             if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
                 AVCODEC_SAMPLE_LOGW("VideoDecOutputThread Catch EOS, thread out" PRId64);
                 break;
             }
         }
     }
     ```
3. 视频文件编码。

   * 在解码输出缓存子线程中，将解码输出缓存同步拷贝AVBuffer。同时，需要注意的是解码的数据中会进行YUV跨距对齐，需要专门处理对应的跨距，偏移填充的数据，才能正确的进行视频编码。若解码过程中发生分辨率、帧率变更，需开发者自行适配处理。系统提供了超分、下采样及丢帧能力，详情可参考[视频缩放](generate-super-resolution-video.md)、[编码支持前处理](video-encoding-preproc.md)。当前系统未提供自动插帧功能，插帧逻辑需由开发者自主实现。

     ```
     void Transcoding::CopyStrideYUV420SP(CodecBufferInfo &encBufferInfo, CodecBufferInfo &bufferInfo) {
         int32_t videoWidth = videoDecContext_->width;
         int32_t &stride = videoDecContext_->widthStride;
         int32_t size = 0;
         uint8_t *tempBufferAddr = encBufferInfo.bufferAddr;

         size += videoDecContext_->height * videoWidth * 3 / 2;
         if (videoWidth == videoDecContext_->widthStride && videoDecContext_->heightStride == videoDecContext_->height) {
             std::memcpy(tempBufferAddr, bufferInfo.bufferAddr, size);
         } else {
             for (int32_t row = 0; row < videoDecContext_->height; row++) {
                 std::memcpy(tempBufferAddr, bufferInfo.bufferAddr, videoWidth);
                 tempBufferAddr += videoWidth;
                 bufferInfo.bufferAddr += stride;
             }
             bufferInfo.bufferAddr += (videoDecContext_->heightStride - videoDecContext_->height) * stride;

             for (int32_t row = 0; row < (videoDecContext_->height / 2); row++) {
                 std::memcpy(tempBufferAddr, bufferInfo.bufferAddr, videoWidth);
                 tempBufferAddr += videoWidth;
                 bufferInfo.bufferAddr += stride;
             }
         }
         
         encBufferInfo.attr.size = size;
         encBufferInfo.attr.flags = bufferInfo.attr.flags;
         encBufferInfo.attr.offset = bufferInfo.attr.offset;
         encBufferInfo.attr.pts = bufferInfo.attr.pts;

         tempBufferAddr = nullptr;
         delete tempBufferAddr;
     }
     ```
   * 同时，拷贝的AVBuffer内存需要通过OH\_AVBuffer\_SetBufferAttr()设置对应的属性，其中，size属性为当前数据的大小，是实际AVBuffer的数据大小。最后，通过OH\_VideoEncoder\_PushInputBuffer()将填充的输入缓存数据提交给编码器。

     ```
     int32_t VideoEncoder::PushInputBuffer(CodecBufferInfo &info) {
         CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");
         int32_t ret = OH_VideoEncoder_PushInputBuffer(encoder_, info.bufferIndex);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Push input data failed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 在编码输出处理中，获取已编码的视频数据。

     ```
     void Transcoding::VideoEncOutputThread() {
         while (true) {
             std::unique_lock<std::mutex> lock(videoEncContext_->outputMutex);
             bool condRet = videoEncContext_->outputCond.wait_for(
                 lock, 5s, [this]() { return !isStarted_ || !videoEncContext_->outputBufferInfoQueue.empty(); });
             CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
             CHECK_AND_CONTINUE_LOG(!videoEncContext_->outputBufferInfoQueue.empty(),
                                    "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

             CodecBufferInfo bufferInfo = videoEncContext_->outputBufferInfoQueue.front();
             videoEncContext_->outputBufferInfoQueue.pop();
             CHECK_AND_BREAK_LOG(!(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS),
                                 "VideoEncOutputThread  Catch EOS, thread out");
             lock.unlock();
             if ((bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_SYNC_FRAME) ||
                 (bufferInfo.attr.flags == AVCODEC_BUFFER_FLAGS_NONE)) {
                 videoEncContext_->outputFrameCount++;
                 bufferInfo.attr.pts = videoEncContext_->outputFrameCount * MICROSECOND / sampleInfo_.frameRate;
             } else {
                 bufferInfo.attr.pts = 0;
             }
             AVCODEC_SAMPLE_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
                                 videoEncContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
                                 bufferInfo.attr.pts);

             muxer_->WriteSample(muxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                                 bufferInfo.attr);
             int32_t ret = videoEncoder_->FreeOutputBuffer(bufferInfo.bufferIndex);
             CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Encoder output thread out");
         }
         AVCODEC_SAMPLE_LOGI("Exit, frame count: %{public}u", videoEncContext_->outputFrameCount);
         StartRelease();
     }
     ```
   * 通过OH\_AVMuxer\_WriteSampleBuffer方法，将编码完成的数据写入到视频文件中，从而完成视频转码。

     ```
     int32_t Muxer::WriteSample(int32_t trackId, OH_AVBuffer *buffer, OH_AVCodecBufferAttr &attr){
         std::lock_guard<std::mutex> lock(writeMutex_);

         CHECK_AND_RETURN_RET_LOG(muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Muxer is null");
         CHECK_AND_RETURN_RET_LOG(buffer != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Get a empty buffer");

         int32_t ret = OH_AVBuffer_SetBufferAttr(buffer, &attr);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "SetBufferAttr failed");

         ret = OH_AVMuxer_WriteSampleBuffer(muxer_, trackId, buffer);
         CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Write sample failed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```

## 常见问题

### 通过Buffer模式进行编解码，视频出现花屏或者绿边

可能的原因是在视频编解码的过程中没有考虑YUV跨距的问题，需要注意宽高对齐，处理对应的跨距，关于跨距的原理，请参考[YUV跨距对齐](video-transcoding-buffer.md#yuv跨距对齐)。在视频编码时，跨距可以在编码的回调函数EncOnNeedInputBuffer()中进行获取，其中，OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH和OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT分别是视频图片的宽和高，OH\_MD\_KEY\_VIDEO\_STRIDE和OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT分别是字节填充后的宽和高。在视频解码时，跨距可以在解码的回调函数OnNewOutputBuffer()中进行获取，参考代码如下。

```
void SampleCallback::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
    if (userData == nullptr) {
        return;
    }
    CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
    if(codecUserData->isDecFirstFrame) {
        OH_AVFormat *format = OH_VideoDecoder_GetOutputDescription(codec);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &codecUserData->width);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &codecUserData->height);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_STRIDE, &codecUserData->widthStride);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_SLICE_HEIGHT, &codecUserData->heightStride);
        OH_AVFormat_Destroy(format);
        codecUserData->isDecFirstFrame = false;
    }
    std::unique_lock<std::mutex> lock(codecUserData->outputMutex);
    codecUserData->outputBufferInfoQueue.emplace(index, buffer);
    codecUserData->outputCond.notify_all();
}

void SampleCallback::EncOnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
    if (userData == nullptr) {
        return;
    }
    CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
    if (codecUserData->isEncFirstFrame) {
        OH_AVFormat *format = OH_VideoDecoder_GetOutputDescription(codec);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &codecUserData->width);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &codecUserData->height);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_STRIDE, &codecUserData->widthStride);
        OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_SLICE_HEIGHT, &codecUserData->heightStride);
        OH_AVFormat_Destroy(format);
        codecUserData->isEncFirstFrame = false;
    }
    std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
    codecUserData->inputBufferInfoQueue.emplace(index, buffer);
    codecUserData->inputCond.notify_all();
}
```

**说明** 

在处理跨距时，需要注意size属性的计算与设置，如果size的大小和设置buffer的大小不一致，视频编解码时会出现buffer数据丢失。

### 在视频编解码中，Surface模式和Buffer模式的区别是什么

视频编解码包含两种方式，分别是Surface模式和Buffer模式。在Surface模式下，会通过window对象对接其他模块，如相机、屏幕录制等模块。相对于Surface模式，Buffer模式对于视频数据处理更加灵活，也更为复杂。关于Surface模式和Buffer模式的区别可以参考[视频编码](video-encoding.md)。

## 示例代码

* [基于Buffer模式进行视频转码](https://gitcode.com/harmonyos_samples/avcodec-buffer-mode)
