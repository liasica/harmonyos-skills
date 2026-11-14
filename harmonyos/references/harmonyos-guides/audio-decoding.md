---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-decoding
title: 音频解码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 音频解码
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:32d356514e42bdd745d35403dacad86a41608eed2785399ea9d0d808e4b81077
---

开发者可以调用本模块的Native API接口，完成音频解码，即将媒体数据解码为PCM码流。

当前支持的解码能力请参考[AVCodec支持的格式](avcodec-support-formats.md#音频解码)。

**适用场景**

* 音频播放

  在播放音频之前，需要先解码音频，再将数据输送到硬件扬声器播放。
* 音频渲染

  在对音频文件进行音效处理之前，需要先解码再由音频处理模块进行音频渲染。
* 音频编辑

  音频编辑（如调整单个声道的播放倍速等）需要基于PCM码流进行，所以需要先将音频文件解码。

**说明** 

通过MP3音频编码流程生成的码流无法直接通过MP3音频解码流程进行解码。建议通过（PCM码流->MP3音频编码->封装->解封装->MP3音频解码）流程进行。

## 开发指导

详细的API说明请参考[native\_avcodec\_audiocodec.h](../harmonyos-references/capi-native-avcodec-audiocodec-h.md)。

参考以下示例代码，完成音频解码的全流程，包括：创建解码器、设置解码参数（采样率/码率/声道数等）、开始、刷新、重置、销毁资源。

示例代码引用了示例工程中自定义的工具宏与数据结构（如CHECK\_AND\_RETURN\_RET\_LOG、AVCODEC\_SAMPLE\_ERR\_\*、AVCODEC\_SAMPLE\_LOG\*、CodecUserData、CodecBufferInfo、SampleInfo等），不属于SDK的接口，完整定义请参见示例工程，移植时需自行实现或替换。

在应用开发过程中，开发者应按一定顺序调用方法，执行对应操作，否则系统可能会抛出异常或产生其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

如下为音频解码调用关系图：

* 虚线表示可选。
* 实线表示必选。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Bd6CC4m9S8yUHHjKoHEQwQ/zh-cn_image_0000002788467534.png?HW-CC-KV=V1&HW-CC-Date=20261114T004753Z&HW-CC-Expire=31536000000&HW-CC-Sign=197393247A8FE1A88CB292057014B5F99BA8A2CBEC7CB29F4D01FCF12A46E163)

### 在 CMake 脚本中链接动态库

```cmake
target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
target_link_libraries(sample PUBLIC libnative_media_core.so)
target_link_libraries(sample PUBLIC libnative_media_acodec.so)
```

**说明** 

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加所需的头文件。

   ```cpp
   #include <multimedia/player_framework/native_avcodec_audiocodec.h>
   #include <multimedia/native_audio_channel_layout.h>
   #include <multimedia/player_framework/native_avcapability.h>
   #include <multimedia/player_framework/native_avcodec_base.h>
   #include <multimedia/player_framework/native_avformat.h>
   #include <multimedia/player_framework/native_avbuffer.h>
   ```
2. 创建解码器实例对象，OH\_AVCodec \*为解码器实例指针。

   应用可以通过媒体类型或编解码器名称创建解码器。

   * 方法一：通过mime type创建解码器。

   ```
   int32_t AudioDecoder::Create(const std::string &codecMime)
   {
       // 设置判定是否为编码。false表示当前是解码。
       constexpr bool isEncoder = false;
       // 通过mime type创建解码器。此处传入的mime type以实际解码格式为准。
       decoder_ = OH_AudioCodec_CreateByMime(codecMime.c_str(), isEncoder);
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create failed");
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```

   * 方法二：通过codec name创建解码器。

   ```
   int32_t AudioDecoder::CreateByName(const std::string &codecMime)
   {
       // 通过codec name创建解码器。
       OH_AVCapability *capability = OH_AVCodec_GetCapability(codecMime.c_str(), false);
       CHECK_AND_RETURN_RET_LOG(capability != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "GetCapability failed");
       const char *name = OH_AVCapability_GetName(capability);
       decoder_ = OH_AudioCodec_CreateByName(name);
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "CreateByName failed");
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
3. 调用OH\_AudioCodec\_RegisterCallback()注册回调函数。

   注册回调函数指针集合OH\_AVCodecCallback，包括：

   * OH\_AVCodecOnError：解码器运行错误。
   * OH\_AVCodecOnStreamChanged：码流信息变化回调，包括采样率变化、声道数变化、音频采样格式变化，支持检测此变化的解码格式有：Audio Vivid，AAC，FLAC，MP3，VORBIS。(API version 15开始支持)
   * OH\_AVCodecOnNeedInputBuffer：运行过程中需要新的输入数据，即解码器已准备好，可以输入数据。
   * OH\_AVCodecOnNewOutputBuffer：运行过程中产生了新的输出数据，即解码完成。

   开发者可以通过处理该回调报告的信息，确保解码器正常运转。

   示例中的CodecUserData为应用自定义的透传数据结构，用于在回调线程与消费线程之间传递buffer队列。

   **注意** 

   请勿在回调中调用解码器的相关接口或进行耗时操作。

   ```
   void SampleCallback::OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   {
       (void)codec;
       auto *codecUserData = static_cast<CodecUserData *>(userData);
       if (codecUserData != nullptr && !codecUserData->isDestroyed.load()) {
           codecUserData->SignalError();
       }
       AVCODEC_SAMPLE_LOGE("On codec error, error code: %{public}d", errorCode);
   }
   ```

   ```
   void SampleCallback::OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   {
       (void)codec;
       AVCODEC_SAMPLE_LOGI("On codec format change");
       auto *codecUserData = static_cast<CodecUserData *>(userData);
       if (codecUserData == nullptr || codecUserData->isDestroyed.load() || format == nullptr) {
           return;
       }
       // 音频码流信息变化：采样率/声道数/采样格式。应用可据此判断变化并做对应处理。
       int32_t sampleRate = 0;
       int32_t channelCount = 0;
       int32_t sampleFormat = 0;
       if (OH_AVFormat_GetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, &sampleRate)) {
           AVCODEC_SAMPLE_LOGI("Audio sample rate changed: %{public}d", sampleRate);
       }
       if (OH_AVFormat_GetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, &channelCount)) {
           AVCODEC_SAMPLE_LOGI("Audio channel count changed: %{public}d", channelCount);
       }
       if (OH_AVFormat_GetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, &sampleFormat)) {
           AVCODEC_SAMPLE_LOGI("Audio sample format changed: %{public}d", sampleFormat);
       }
       std::unique_lock<std::shared_mutex> codecLock(codecUserData->codecMutex);
       // 可通过format获取到变化后的视频宽、高、跨距等。
       UpdateVideoOutputInfo(format, codecUserData);
       const int32_t pixelFormat = static_cast<int32_t>(codecUserData->outputPixelFormat);
       AVCODEC_SAMPLE_LOGI("Format changed: %{public}d*%{public}d, stride: %{public}d*%{public}d, "
           "pixel format: %{public}d",
           codecUserData->width, codecUserData->height,
           codecUserData->widthStride, codecUserData->heightStride, pixelFormat);
   }
   ```

   示例函数同时服务于音视频编解码，其中UpdateVideoOutputInfo()为视频宽高、像素格式等信息的更新逻辑；OnNeedInputBuffer()中的UpdateEncoderFirstInputDescription()为视频编码首帧的信息获取逻辑（内部调用OH\_VideoEncoder\_GetInputDescription()）。音频解码场景均不会生效，可忽略。

   ```
   void SampleCallback::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
       auto *codecUserData = static_cast<CodecUserData *>(userData);
       if (codecUserData == nullptr || codecUserData->isDestroyed.load()) {
           return;
       }
       if (codec == nullptr || buffer == nullptr) {
           AVCODEC_SAMPLE_LOGE("Invalid codec input callback argument");
           codecUserData->SignalError();
           return;
       }
       UpdateEncoderFirstInputDescription(codec, codecUserData);
       // 输入帧的数据buffer和对应的index送入inputBufferQueue队列。
       codecUserData->inputBufferQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));
   }
   ```

   ```
   void SampleCallback::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
       auto *codecUserData = static_cast<CodecUserData *>(userData);
       if (codecUserData == nullptr || codecUserData->isDestroyed.load()) {
           return;
       }
       if (codec == nullptr || buffer == nullptr) {
           AVCODEC_SAMPLE_LOGE("Invalid codec output callback argument");
           codecUserData->SignalError();
           return;
       }
       if (codecUserData->isDecFirstFrame) {
           OH_AVFormat *format = OH_VideoDecoder_GetOutputDescription(codec);
           if (format != nullptr) {
               UpdateVideoOutputInfo(format, codecUserData);
               OH_AVFormat_Destroy(format);
           }
           codecUserData->isDecFirstFrame = false;
       }
       // 输出帧的数据buffer和对应的index送入outputBufferQueue队列。
       codecUserData->outputBufferQueue.Enqueue(std::make_shared<CodecBufferInfo>(index, buffer));

       // 从AVBuffer中获取时域层级信息。
       int32_t layerID = GetTemporalLayerID(buffer);
       if (layerID >= 0 && index % LIMIT_LOGD_FREQUENCY == 0) {
           AVCODEC_SAMPLE_LOGD("Temporal layer ID: %{public}d", layerID);
       }
   }
   ```

   **说明** 

   isDecFirstFrame分支内部调用OH\_VideoDecoder\_GetOutputDescription()，该接口声明于native\_avcodec\_videodecoder.h，属于视频解码库。示例中isDecFirstFrame分支与时域层级信息的获取（GetTemporalLayerID()）为视频解码场景的扩展逻辑，音频解码场景不会生效，可忽略。

   配置回调：

   ```
   int32_t AudioDecoder::SetCallback(CodecUserData *codecUserData)
   {
       // 异步模式下回调由codec内部线程触发并访问传入的userData；须先停止解码器再销毁该上下文，避免回调访问已释放的对象。
       int32_t ret = AV_ERR_OK;
       ret = OH_AudioCodec_RegisterCallback(decoder_,
                                            {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
                                             SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},
                                            codecUserData);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Set callback failed, ret: %{public}d", ret);

       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
4. （可选）OH\_AudioCodec\_SetDecryptionConfig设置解密配置。

   当获取到DRM信息(参考[音视频解封装](audio-video-demuxer.md)开发步骤第4步)后，通过此接口进行解密配置。

   DRM相关接口详见[DRM API文档](../harmonyos-references/capi-drm.md)。

   此接口需在Prepare前调用。

   添加头文件:

   ```
   #include <multimedia/drm_framework/native_mediakeysystem.h>
   #include <multimedia/drm_framework/native_mediakeysession.h>
   #include <multimedia/drm_framework/native_drm_err.h>
   #include <multimedia/drm_framework/native_drm_common.h>
   ```

   在 CMake 脚本中链接动态库:

   ```cmake
   target_link_libraries(sample PUBLIC libnative_drm.so)
   ```

   使用示例:

   ```
   // 根据DRM信息创建指定的DRM系统, 以创建"com.wiseplay.drm"为例。
   MediaKeySystem *system = nullptr;
   int32_t ret = OH_MediaKeySystem_Create("com.wiseplay.drm", &system);
   if (system == nullptr) {
       printf("create media key system failed");
       return;
   }

   // 创建解密会话。
   MediaKeySession *session = nullptr;
   DRM_ContentProtectionLevel contentProtectionLevel = CONTENT_PROTECTION_LEVEL_SW_CRYPTO;
   ret = OH_MediaKeySystem_CreateMediaKeySession(system, &contentProtectionLevel, &session);
   if (ret != DRM_ERR_OK) {
       // 如创建失败，请查看DRM接口文档及日志信息。
       printf("create media key session failed.");
       return;
   }
   if (session == nullptr) {
       printf("media key session is nullptr.");
       return;
   }
   // 获取许可证请求、设置许可证响应等。
   // 设置解密配置, 即将解密会话、安全通路标志(当前音频解密不支持安全通路，应设置为false)设置到解码器中。
   bool secureAudio = false;
   ret = OH_AudioCodec_SetDecryptionConfig(audioDec_, session, secureAudio);
   ```
5. 调用OH\_AudioCodec\_Configure()配置解码器。

   配置选项key值说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/joBnnYlEQM6C6H-JY9yInQ/zh-cn_image_0000002788467536.png?HW-CC-KV=V1&HW-CC-Date=20261114T004753Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE23CD70790434F578723C37AE6D3C3898C3DF7133E0824449F1271B3EAC759F)

   各音频解码类型参数范围说明：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/70vaHK-DQfOeJy5NsXpz0Q/zh-cn_image_0000002817507025.png?HW-CC-KV=V1&HW-CC-Date=20261114T004753Z&HW-CC-Expire=31536000000&HW-CC-Sign=17B6B3AD7A9FC7452DD8D3F61089502B76AE105E60C3D0C994314278E22E6DB1)

   从API version 20开始，支持通过[OH\_AVCapability\_GetAudioSupportedSampleRateRanges](../harmonyos-references/capi-native-avcapability-h.md#oh_avcapability_getaudiosupportedsamplerateranges)接口进行采样率范围能力查询，以下几种音频解码类型支持对范围内的任意采样率进行解码：

   | 音频解码类型 | 采样率(Hz) |
   | --- | --- |
   | Flac | 8000 ~ 384000 |
   | Vorbis | 8000 ~ 192000 |
   | APE | 1 ~ 2147483647 |

   ```
   int32_t AudioDecoder::Configure(const SampleInfo &sampleInfo)
   {
       // 解码能力表可能未完整列出部分容器编码格式的采样率/声道信息。
       // 解码器Configure调用的返回值才是最终判定依据，此处仅将能力查询结果作为参考日志。
       if (!CodecCapability::ValidateAudioConfiguration(sampleInfo, false)) {
           AVCODEC_SAMPLE_LOGW("Audio capability query did not fully describe mime: %{public}s; "
               "continue with decoder configure", sampleInfo.audio.audioCodecMime.c_str());
       }
       // format仅用于本次Configure；所有失败路径和成功路径都要在返回前销毁。
       OH_AVFormat *format = OH_AVFormat_Create();
       CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

       // 必选：采样格式、声道数、声道布局、采样率。
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S16LE);
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, sampleInfo.audio.audioChannelCount);
       OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, sampleInfo.audio.audioChannelLayout);
       OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleInfo.audio.audioSampleRate);
       // 可选：同步模式，按需设置。
       if (sampleInfo.codec.codecSyncMode) {
           OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_SYNC_MODE, sampleInfo.codec.codecSyncMode);
       }

       // 可选：编解码器特定数据（codec config），由解封装获取，没有则不设置。
       if (sampleInfo.audio.codecConfigLen > 0 &&
           sampleInfo.audio.codecConfig.size() >= sampleInfo.audio.codecConfigLen) {
           OH_AVFormat_SetBuffer(format, OH_MD_KEY_CODEC_CONFIG, sampleInfo.audio.codecConfig.data(),
               sampleInfo.audio.codecConfigLen);
       }

       // 配置解码器。
       int ret = OH_AudioCodec_Configure(decoder_, format);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Config failed, ret: %{public}d", ret);
       OH_AVFormat_Destroy(format);
       format = nullptr;

       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
6. 调用OH\_AudioCodec\_Prepare()，解码器就绪。

   示例工程将OH\_AudioCodec\_Prepare()封装在Config()函数中调用：在Config()函数中先完成Configure()配置与回调注册，之后再调用OH\_AudioCodec\_Prepare()使解码器就绪。以下为其中Prepare部分的代码：

   ```
   {
       // 解码器就绪。
       int ret = OH_AudioCodec_Prepare(decoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Prepare failed, ret: %{public}d", ret);
   }
   ```
7. 调用OH\_AudioCodec\_Start()启动解码器，进入运行态。

   ```
   int32_t AudioDecoder::Start()
   {
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");

       int ret = OH_AudioCodec_Start(decoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Start failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
8. （可选）调用OH\_AVCencInfo\_SetAVBuffer()，设置cencInfo。

   若当前播放的节目是DRM加密节目，且由上层应用做[媒体解封装](audio-video-demuxer.md)，则须调用OH\_AVCencInfo\_SetAVBuffer()将cencInfo设置给AVBuffer，以实现AVBuffer中媒体数据的解密。

   添加头文件：

   ```
   #include <multimedia/player_framework/native_cencinfo.h>
   ```

   在 CMake 脚本中链接动态库：

   ```cmake
   target_link_libraries(sample PUBLIC libnative_media_avcencinfo.so)
   ```

   使用示例：

   ```
   OH_AVBuffer *buffer = ...; // 待解密的输入buffer，获取方式可参考步骤9。
   uint32_t keyIdLen = DRM_KEY_ID_SIZE;
   uint8_t keyId[] = {
       0xd4, 0xb2, 0x01, 0xe4, 0x61, 0xc8, 0x98, 0x96,
       0xcf, 0x05, 0x22, 0x39, 0x8d, 0x09, 0xe6, 0x28};
   uint32_t ivLen = DRM_KEY_IV_SIZE;
   uint8_t iv[] = {
       0xbf, 0x77, 0xed, 0x51, 0x81, 0xde, 0x36, 0x3e,
       0x52, 0xf7, 0x20, 0x4f, 0x72, 0x14, 0xa3, 0x95};
   uint32_t encryptedBlockCount = 0;
   uint32_t skippedBlockCount = 0;
   uint32_t firstEncryptedOffset = 0;
   uint32_t subsampleCount = 1;
   DrmSubsample subsamples[1] = { { .clearHeaderLen = 0x10, .payLoadLen = 0x16 } };
   // 创建CencInfo实例。
   OH_AVCencInfo *cencInfo = OH_AVCencInfo_Create();
   if (cencInfo == nullptr) {
       // 异常处理。
   }
   // 设置解密算法。
   OH_AVErrCode errNo = OH_AVCencInfo_SetAlgorithm(cencInfo, DRM_ALG_CENC_AES_CTR);
   if (errNo != AV_ERR_OK) {
       // 异常处理。
   }
   // 设置KeyId和Iv。
   errNo = OH_AVCencInfo_SetKeyIdAndIv(cencInfo, keyId, keyIdLen, iv, ivLen);
   if (errNo != AV_ERR_OK) {
       // 异常处理。
   }
   // 设置Sample信息。
   errNo = OH_AVCencInfo_SetSubsampleInfo(cencInfo, encryptedBlockCount, skippedBlockCount, firstEncryptedOffset,
       subsampleCount, subsamples);
   if (errNo != AV_ERR_OK) {
       // 异常处理。
   }
   // 设置模式：KeyId、Iv和SubSamples已被设置。
   errNo = OH_AVCencInfo_SetMode(cencInfo, DRM_CENC_INFO_KEY_IV_SUBSAMPLES_SET);
   if (errNo != AV_ERR_OK) {
       // 异常处理。
   }
   // 将CencInfo设置到AVBuffer中。
   errNo = OH_AVCencInfo_SetAVBuffer(cencInfo, buffer);
   if (errNo != AV_ERR_OK) {
       // 异常处理。
   }
   // 销毁CencInfo实例。
   errNo = OH_AVCencInfo_Destroy(cencInfo);
   if (errNo != AV_ERR_OK) {
       // 异常处理。
   }
   cencInfo = nullptr;
   ```
9. 调用OH\_AudioCodec\_PushInputBuffer()，写入待解码的数据。

   需开发者填充完整的输入数据后调用。

   结束时需要将flags标识为AVCODEC\_BUFFER\_FLAGS\_EOS。

   ```
   int32_t AudioDecoder::PushInputBuffer(CodecBufferInfo &info)
   {
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");
       CHECK_AND_RETURN_RET_LOG(info.buffer != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Input buffer is null");
       int32_t ret = OH_AVBuffer_SetBufferAttr(info.buffer, &info.attr);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Set avbuffer attr failed");
       ret = OH_AudioCodec_PushInputBuffer(decoder_, info.bufferIndex);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Push input data failed");
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```

   示例中待解码的数据从解封装模块读取，pts、size、flags由OH\_AVDemuxer\_ReadSampleBuffer写入buffer属性，输入线程消费示例如下：

   ```
   void Player::AudioDecInputThread()
   {
       while (isStarted_ && audioWorkerRunning_) {
           WaitIfPaused(true);
           CHECK_AND_BREAK_LOG(isStarted_ && audioWorkerRunning_, "Decoder input thread out");
           std::shared_ptr<CodecBufferInfo> bufferInfo = audioDecContext_->inputBufferQueue.Dequeue();
           std::shared_lock<std::shared_mutex> codecLock(audioDecContext_->codecMutex);
           CHECK_AND_BREAK_LOG(isStarted_ && audioWorkerRunning_, "Work done, thread out");
           CHECK_AND_CONTINUE_LOG(bufferInfo != nullptr, "Buffer queue is empty, continue");
           audioDecContext_->inputFrameCount++;
           int32_t ret = demuxer_->ReadSample(demuxer_->GetAudioTrackId(), bufferInfo->buffer, bufferInfo->attr);
           if (ret != AVCODEC_SAMPLE_ERR_OK) {
               AVCODEC_SAMPLE_LOGE("Read audio sample failed");
               playbackFailed_ = true;
               isStarted_ = false;
               break;
           }
           ret = audioDecoder_->PushInputBuffer(*bufferInfo);
           if (ret != AVCODEC_SAMPLE_ERR_OK) {
               playbackFailed_ = true;
               isStarted_ = false;
               break;
           }
           CHECK_AND_BREAK_LOG(!(bufferInfo->attr.flags & AVCODEC_BUFFER_FLAGS_EOS), "Catch EOS, thread out");
       }
   }
   ```
10. 调用OH\_AudioCodec\_FreeOutputBuffer()，释放解码后的数据。

    在获取解码PCM码流后，应及时调用OH\_AudioCodec\_FreeOutputBuffer()进行释放。

    ```
    int32_t AudioDecoder::FreeOutputBuffer(uint32_t bufferIndex, bool render)
    {
        CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");

        int32_t ret = AVCODEC_SAMPLE_ERR_OK;
        ret = OH_AudioCodec_FreeOutputBuffer(decoder_, bufferIndex);
        CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Free output data failed");
        return AVCODEC_SAMPLE_ERR_OK;
    }
    ```

    输出线程从输出buffer队列中取出解码完成的数据，取走PCM数据后及时释放，输出消费示例如下：

    ```
    bool AudioOutputPump::ProcessAsyncOutput()
    {
        CHECK_AND_RETURN_RET_LOG(running_, false, "Audio decoder output thread out");
        std::shared_ptr<CodecBufferInfo> bufferInfo = context_.outputBufferQueue.Dequeue();
        std::shared_lock<std::shared_mutex> codecLock(context_.codecMutex);
        if (bufferInfo == nullptr) {
            AVCODEC_SAMPLE_LOGW("Buffer queue is empty, continue");
            return true;
        }
        if (!running_) {
            (void)ReleaseOutputBuffer(*bufferInfo, "audio output worker stopped");
            return false;
        }
        if (bufferInfo->attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
            (void)ReleaseOutputBuffer(*bufferInfo, "audio output EOS");
            AVCODEC_SAMPLE_LOGI("Catch EOS, audio output thread out");
            return false;
        }
        return HandleOutputBuffer(*bufferInfo, true);
    }
    ```

从API version 11开始，Audio Vivid新增获取元数据。

```
uint32_t index = signal_->outQueue_.front();
OH_AVBuffer *data = signal_->outBufferQueue_.front();
// 获取buffer attributes。
OH_AVCodecBufferAttr attr = {0};
int32_t ret = OH_AVBuffer_GetBufferAttr(data, &attr);
if (ret != AV_ERR_OK) {
    // 异常处理。
}
// 将解码完成数据data写入到对应输出文件中。
outFile_.write(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(data)), attr.size);

// API version 11开始提供 获取audio vivid 元数据。
OH_AVFormat *format = OH_AVBuffer_GetParameter(data);
uint8_t *metadata = nullptr;
size_t metaSize;
OH_AVFormat_GetBuffer(format, OH_MD_KEY_AUDIO_VIVID_METADATA, &metadata, &metaSize);

ret = OH_AudioCodec_FreeOutputBuffer(audioDec_, index);
if (ret != AV_ERR_OK) {
    // 异常处理。
}
if (attr.flags == AVCODEC_BUFFER_FLAGS_EOS) {
    // 结束。
}
```

1. （可选）调用OH\_AudioCodec\_Flush()刷新解码器。

   调用OH\_AudioCodec\_Flush()后，解码器仍处于运行态，但会将当前队列清空，将已解码的数据释放。

   此时需要调用OH\_AudioCodec\_Start()重新开始解码。

   使用情况：

   * 在解码输出buffer属性为AVCODEC\_BUFFER\_FLAGS\_EOS后，若想重新使用相同配置进行解码时，需要调用刷新。
   * 在执行过程中遇到可继续执行的错误时（即OH\_AudioCodec\_IsValid()为true）可以调用刷新，然后调用OH\_AudioCodec\_Start()重新开始解码。

   ```
   int32_t AudioDecoder::Flush()
   {
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");

       // 刷新解码器，清空当前队列，之后需要调用Start()重新开始解码。
       int32_t ret = OH_AudioCodec_Flush(decoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Flush failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
2. （可选）调用OH\_AudioCodec\_Reset()重置解码器。

   调用OH\_AudioCodec\_Reset()后，解码器回到初始化状态，重置前获取到的输入/输出buffer都无法继续使用，需先调用OH\_AudioCodec\_Configure()重新配置，再调用OH\_AudioCodec\_Start()重新开始解码。启动后重新获取输入/输出buffer。

   ```
   int32_t AudioDecoder::Reset()
   {
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");

       // 重置解码器，之后需要重新调用Configure()配置、Start()启动。
       int32_t ret = OH_AudioCodec_Reset(decoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Reset failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
3. 调用OH\_AudioCodec\_Stop()停止解码器。

   停止后，可以通过调用OH\_AudioCodec\_Start()重新进入已启动状态（started）。停止前获取到的输入/输出buffer都无法继续使用，需要在启动后重新获取输入/输出buffer。

   ```
   int32_t AudioDecoder::Stop()
   {
       CHECK_AND_RETURN_RET_LOG(decoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");

       int32_t ret = OH_AudioCodec_Stop(decoder_);
       CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Stop failed, ret: %{public}d", ret);
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
4. 调用OH\_AudioCodec\_Destroy()销毁解码器实例，释放资源。

   **说明** 

   禁止重复销毁解码器。

   ```
   int32_t AudioDecoder::Release()
   {
       if (decoder_ != nullptr) {
           // 销毁前刷新并停止解码器，不可重复destroy。
           Flush();
           Stop();
           OH_AudioCodec_Destroy(decoder_);
           decoder_ = nullptr;
       }
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
