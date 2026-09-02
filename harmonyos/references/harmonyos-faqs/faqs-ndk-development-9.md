---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-9
title: NDK中实现AVScreenCapture在Surface模式下回调编码数据到ArkTS侧
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NDK中实现AVScreenCapture在Surface模式下回调编码数据到ArkTS侧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:184b78d6611f4849b0e07d0c6c1cb633bd9aa9daf74e362eeaee9258f0aa33fd
---

## 问题现象

如何在NDK开发中使用AVScreenCapture实时录制屏幕，并将Surface模式实时编码数据一帧一帧的回调到ArkTS侧？

## 背景知识

* [AVScreenCapture录屏取码流](../harmonyos-guides/using-avscreencapture-for-buffer.md)主要应用于屏幕录制、会议共享、直播等场景。根据录屏码流的获取方式，可分为buffer和Surface模式。buffer模式获取音视频原始码流，然后通过流的方式流转到其他模块处理。Surface对接NativeImage作为消费者端，提供Surface关联OpenGL外部纹理。
* [线程安全函数](../harmonyos-guides/use-napi-thread-safety.md)是Node-API接口之一，用于创建一个线程安全的JavaScript函数。主要用于在多个线程之间共享和调用，而不会出现竞争条件或死锁。

## 解决方案

1. 实现录屏和回调函数。

   ```screen
   /*
    * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
    */
   #include "napi/native_api.h"
   #include "sample_info.h"
   #include "Recorder.h"

   #include <multimedia/player_framework/native_avcodec_base.h>
   #include <multimedia/player_framework/native_avscreen_capture.h>
   #include <multimedia/player_framework/native_avscreen_capture_base.h>
   #include <multimedia/player_framework/native_avbuffer.h>
   #include <multimedia/player_framework/native_avcodec_videoencoder.h>
   #include <multimedia/player_framework/native_avcapability.h>
   #include <multimedia/player_framework/native_avcodec_videoencoder.h>

     // 错误事件发生回调函数OnError()。
     void OnError(OH_AVScreenCapture *capture, int32_t errorCode, void *userData) {
     (void)capture;
     // 应用根据错误码进行事件处理。
     (void)errorCode;
     (void)userData;
   }

   // 状态变更事件处理函数OnStateChange()。
   void OnStateChange(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData) {
     (void)capture;
     if (stateCode == OH_AVScreenCaptureStateCode::OH_SCREEN_CAPTURE_STATE_CANCELED) { // 按照所需状态自行修改填写。
       // 处理录屏状态变更。
     }
     (void)userData;
   }

   // 获取并处理音视频原始码流数据回调函数OnBufferAvailable()。
   void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType,
   int64_t timestamp, void *userData) {
     // 处于录屏取码流状态。
   }

   // 执行回调ArkTS函数，将编码后视频帧回调ArkTS
   static void callJS(napi_env env, napi_value js_cb, void *context, void *data) {
     SampleInfo *sampleInfo = reinterpret_cast<SampleInfo *>(data);
     napi_value buffer;
     napi_create_buffer(env, sizeof(sampleInfo->buf), reinterpret_cast<void **>(&sampleInfo->buf), &buffer);
     napi_value callFunc = nullptr;
     napi_get_reference_value(env, sampleInfo->tsRef, &callFunc);
     napi_call_function(env, nullptr, callFunc, 1, &buffer, nullptr);
   }

   // 开始录屏
   static napi_value ScreenCapture(napi_env env, napi_callback_info info) {
     // 获取ArkTS侧传递的回调函数
     size_t argc = 1;
     napi_value args[1] = {nullptr};
     napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

     // 录屏相关配置
     OH_AVScreenCapture *capture = OH_AVScreenCapture_Create();
     // 设置回调。
     OH_AVScreenCapture_SetErrorCallback(capture, OnError, nullptr);
     OH_AVScreenCapture_SetStateCallback(capture, OnStateChange, nullptr);
     // 回调音视频原始码流
     OH_AVScreenCapture_SetDataCallback(capture, OnBufferAvailable, nullptr);
     // OH_AVScreenRecorderConfig配置录屏视频宽高，音频通道数等
     OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 16000, .audioChannels = 2, .audioSource = OH_MIC};
     OH_VideoCaptureInfo videoCapInfo = {
       .videoFrameWidth = 768, .videoFrameHeight = 1280, .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA};
     OH_AudioInfo audioInfo = {
       .micCapInfo = micCapInfo,
     };
     OH_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo};
     OH_AVScreenCaptureConfig config = {.dataType = OH_ORIGINAL_STREAM, .audioInfo = audioInfo, .videoInfo = videoInfo};
     OH_AVScreenCapture_Init(capture, config);

     // 编码器相关配置
     SampleInfo sampleInfo;
     sampleInfo.videoCodecMime = "video/avc";
     sampleInfo.videoWidth = 768;
     sampleInfo.videoHeight = 1280;
     sampleInfo.frameRate = 30;
     sampleInfo.bitrate = 10000000;
     sampleInfo.audioCodecMime = OH_AVCODEC_MIMETYPE_AUDIO_AAC;
     sampleInfo.audioSampleForamt = OH_BitsPerSample::SAMPLE_S16LE;
     sampleInfo.audioSampleRate = 48000;
     sampleInfo.audioChannelCount = 2;
     sampleInfo.audioBitRate = 96000;
     sampleInfo.audioChannelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
     sampleInfo.audioMaxInputSize = sampleInfo.audioSampleRate * 0.02 * sampleInfo.audioChannelCount * sizeof(short);
     sampleInfo.pixelFormat = AV_PIXEL_FORMAT_RGBA;

     // 保存ArkTS传递的回调函数，在合适时机调用
     napi_create_reference(env, args[0], 1, &sampleInfo.tsRef);
     // 创建线程安全函数
     napi_value workName = nullptr;
     napi_create_string_utf8(env, "ScreenCaptureThreadSafeFunc", NAPI_AUTO_LENGTH, &workName);
     napi_threadsafe_function tsfn;
     napi_create_threadsafe_function(env, args[0], nullptr, workName, 0, 1, nullptr, nullptr, nullptr, callJS, &tsfn);
     sampleInfo.tsfn = tsfn;

     // init编码器相关配置
     Recorder::GetInstance().Init(sampleInfo);
     // 指定surface开始录屏。
     int32_t retStart = OH_AVScreenCapture_StartScreenCaptureWithSurface(capture, sampleInfo.window);

     if (retStart != AV_ERR_OK) {
       return nullptr;
     }
     Recorder::GetInstance().Start();
     // 开始录屏。
     OH_AVScreenCapture_SetMicrophoneEnabled(capture, true);
     return nullptr;
   }

   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports) {
     napi_property_descriptor desc[] = {{"screenCapture", nullptr, ScreenCapture, nullptr, nullptr, nullptr, napi_default, nullptr}};
   napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   return exports;
   }
   EXTERN_C_END

   static napi_module demoModule = {
     .nm_version = 1,
     .nm_flags = 0,
     .nm_filename = nullptr,
     .nm_register_func = Init,
     .nm_modname = "entry",
     .nm_priv = ((void *)0),
     .reserved = {0},
   };

   extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
2. OnNewOutputBuffer调用线程安全函数，避免死锁。

   ```screen
   /*
    * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
    */

   #include "sample_callback.h"
   #include "av_codec_sample_log.h"

   namespace {
     constexpr int LIMIT_LOGD_FREQUENCY = 50;
     constexpr int32_t BYTES_PER_SAMPLE_2 = 2;
   } // namespace

   // 自定义写入数据函数
   int32_t SampleCallback::OnRenderWriteData(OH_AudioRenderer *renderer, void *userData, void *buffer, int32_t length)
   {
     (void)renderer;
     (void)length;
     CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);

     // 将待播放的数据，按length长度写入buffer
     uint8_t *dest = (uint8_t *)buffer;
     size_t index = 0;
     std::unique_lock<std::mutex> lock(codecUserData->outputMutex);
     // 从队列中取出需要播放的长度为length的数据
     while (!codecUserData->renderQueue.empty() && index < length) {
       dest[index++] = codecUserData->renderQueue.front();
       codecUserData->renderQueue.pop();
     }
     AVCODEC_SAMPLE_LOGD("render BufferLength:%{public}d Out buffer count: %{public}u, renderQueue.size: %{public}u "
     "renderReadSize: %{public}u",
     length, codecUserData->outputFrameCount, codecUserData->renderQueue.size(), index);

     codecUserData->frameWrittenForSpeed +=
     length / codecUserData->speed / codecUserData->sampleInfo->audioChannelCount / BYTES_PER_SAMPLE_2;
     codecUserData->currentPosAudioBufferPts =
       codecUserData->endPosAudioBufferPts - codecUserData->renderQueue.size() /
         codecUserData->sampleInfo->audioSampleRate /
         codecUserData->sampleInfo->audioChannelCount / BYTES_PER_SAMPLE_2;

     if (codecUserData->renderQueue.size() < length) {
       codecUserData->renderCond.notify_all();
     }
     return 0;
   }
   // 自定义音频流事件函数
   int32_t SampleCallback::OnRenderStreamEvent(OH_AudioRenderer *renderer, void *userData, OH_AudioStream_Event event)
   {
     (void)renderer;
     (void)userData;
     (void)event;
     // 根据event表示的音频流事件信息，更新播放器状态和界面
     return 0;
   }
   // 自定义音频中断事件函数
   int32_t SampleCallback::OnRenderInterruptEvent(OH_AudioRenderer *renderer, void *userData,
     OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)
   {
     (void)renderer;
     (void)userData;
     (void)type;
     (void)hint;
     // 根据type和hint表示的音频中断信息，更新播放器状态和界面
     return 0;
   }
   // 自定义异常回调函数
   int32_t SampleCallback::OnRenderError(OH_AudioRenderer *renderer, void *userData, OH_AudioStream_Result error)
   {
     (void)renderer;
     (void)userData;
     (void)error;
     AVCODEC_SAMPLE_LOGE("OnRenderError");
     // 根据error表示的音频异常信息，做出相应的处理
     return 0;
   }

   void SampleCallback::OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData)
   {
     (void)codec;
     (void)errorCode;
     (void)userData;
     AVCODEC_SAMPLE_LOGE("On codec error, error code: %{public}d", errorCode);
   }

   void SampleCallback::OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
   {
     AVCODEC_SAMPLE_LOGI("On codec format change");
   }

   void SampleCallback::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
     if (userData == nullptr) {
       return;
     }
     (void)codec;
     CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
     std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
     if (codecUserData->isEncFirstFrame) {
       OH_AVFormat *format = OH_VideoEncoder_GetInputDescription(codec);
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &codecUserData->width);
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &codecUserData->height);
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_STRIDE, &codecUserData->widthStride);
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_SLICE_HEIGHT, &codecUserData->heightStride);
       OH_AVFormat_Destroy(format);
       codecUserData->isEncFirstFrame = false;
     }
     codecUserData->inputBufferInfoQueue.emplace(index, buffer);
     codecUserData->inputCond.notify_all();
   }

   void SampleCallback::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
     if (userData == nullptr) {
       return;
     }
     (void)codec;
     CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
     std::unique_lock<std::mutex> lock(codecUserData->outputMutex);
     codecUserData->outputBufferInfoQueue.emplace(index, buffer);

     // 回调arkts
     SampleInfo *sampleInfo = codecUserData->sampleInfo;
     if (sampleInfo) {
       uint8_t *buf = OH_AVBuffer_GetAddr(buffer);
       if (buf) {
         sampleInfo->buf = buf;
         // 调用线程安全函数
         napi_acquire_threadsafe_function(sampleInfo->tsfn);
         napi_call_threadsafe_function(sampleInfo->tsfn, (void *)sampleInfo, napi_tsfn_blocking);
       }
     }
     codecUserData->outputCond.notify_all();
     AVCODEC_SAMPLE_LOGI("output buffer");
   }
   ```
3. 导出Native方法提供ArkTS使用。

   ```screen
   export const screenCapture: (cb:(buffer: ArrayBuffer)=>void) => void;
   ```
4. ArkTS侧调用录屏方法。

   ```screen
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'libentry.so';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message = 'Welcome';
               testNapi.screenCapture((buffer: ArrayBuffer) => {
                 hilog.info(100, 'capture buffer ===', buffer.byteLength.toString());
               });
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
