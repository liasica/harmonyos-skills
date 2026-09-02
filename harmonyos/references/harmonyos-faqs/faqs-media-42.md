---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-42
title: 屏幕录制如何实时获取原始视频数据与编码视频码流数据
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 屏幕录制如何实时获取原始视频数据与编码视频码流数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b8062047cecd1b269b00491ed959d3223fa6fb3b9444e8d551a17b8d3e262f2d
---

## 问题现象

在屏幕录制的过程中，如何实时获取原始视频数据（RGBA）与编码视频码流（H264、H265）。

## 背景知识

* 开发者可以调用[AVScreenCapture](../harmonyos-references/capi-avscreencapture.md)模块的Native API完成屏幕录制的功能，包括录屏存文件和录屏取码流两套接口。通过录屏取码流接口，可以实时获取屏幕数据，适用于会议共享、直播等场景。
* [VideoEncoder](../harmonyos-references/capi-videoencoder.md)模块提供用于视频编码的接口。开发者可以调用VideoEncoder模块的Native API接口，完成视频编码，将未压缩的视频数据压缩成编码视频码流。视频编码支持[Surface模式](../harmonyos-guides/video-encoding.md#surface模式)和[Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)。Surface模式使用[OHNativeWindow](../harmonyos-references/capi-nativewindow.md)模块来传递输入视频数据，可以与其他模块对接，例如相机、录屏模块。

## 解决方案

AVScreenCapture录屏取码流的通用开发步骤可参考：[AVScreenCapture录屏基础流程](../harmonyos-guides/avscreencapture-c-basic-process.md)。

VideoEncoder视频编码的基础开发流程可参考：[视频编码](../harmonyos-guides/video-encoding.md)。

* 获取原始视频数据：以Buffer模式启动屏幕录制时，可以直接获取当前屏幕的原始视频数据（RGBA格式）。开发者可以根据应用场景将屏幕原始视频数据流转到其他模块处理。可通过如下方式实时获取原始视频数据：
  1. 在启动录屏前，通过[OH\_AVScreenCapture\_SetDataCallback](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setdatacallback)接口设置原始视频数据处理回调方法。

     ```cpp
     OH_AVScreenCapture_SetDataCallback(g_avCapture, OnBufferAvailable, nullptr);
     ```
  2. 通过[OH\_AVScreenCapture\_StartScreenCapture](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapture)接口以Buffer模式启动录屏。

     ```cpp
     // 以Buffer模式启动屏幕录制
     int result = OH_AVScreenCapture_StartScreenCapture(g_avCapture);
     OH_LOG_INFO(LOG_APP, "OH_VideoEncoder_Start Started by buffer mode %{public}d", result);
     if (result != AV_SCREEN_CAPTURE_ERR_OK) {
         OH_LOG_INFO(LOG_APP, "ScreenCapture Started failed %{public}d", result);
         OH_AVScreenCapture_Release(g_avCapture);
     }
     ```
  3. 启动录屏后，通过设置的[OH\_AVScreenCapture\_OnBufferAvailable](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)回调函数来监听是否有视频数据产生并获取屏幕录制的视频数据（RGBA格式）。

     ```cpp
     // 录屏原始数据获取回调
     void CAVScreenCaptureToStream::OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                                      OH_AVScreenCaptureBufferType bufferType, int64_t timestamp,
                                                      void *userData)
     {
         (void)capture;
         (void)userData;
         if (g_isRunning) {
             if (bufferType == OH_SCREEN_CAPTURE_BUFFERTYPE_VIDEO) {
                 // 屏幕录制原始视频数据（RGBA格式）
                 OH_AVCodecBufferAttr attr;
                 OH_AVBuffer_GetBufferAttr(buffer, &attr);
                 OH_LOG_INFO(LOG_APP, "RGBA Buffer: size=%{public}d timestamp=%{public}ld", attr.size, timestamp);

                 OH_AVBuffer_Destroy(buffer);
             }
         }
     }
     ```

* 获取编码视频码流：以Surface模式启动屏幕录制时，需要通过OHNativeWindow与视频编码器对接。此时，无法直接获取屏幕的原始视频数据，视频数据会实时流转到视频编码器模块完成视频编码，最后通过视频编码器输出编码后的视频码流（H264或H265格式）。可通过如下方法获取屏幕编码视频码流：
  1. 创建视频编码器，并通过[OH\_VideoEncoder\_GetSurface](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getsurface)接口获取编码器Surface模式的输入[OHNativeWindow](../harmonyos-references/capi-nativewindow-nativewindow.md)。

     ```cpp
     int32_t VideoEncoder::Create(const std::string &videoCodecMime)
     {
         encoder_ = OH_VideoEncoder_CreateByMime(videoCodecMime.c_str());
         if (encoder_ == nullptr) {
             return -1;
         }
         return 0;
     }
     ```

     ```cpp
     // GetSurface from video encoder
     OH_VideoEncoder_GetSurface(encoder_, &sampleInfo.window); // 视频编码器输入OHNativeWindow
     ```
  2. 通过[OH\_AVScreenCapture\_StartScreenCaptureWithSurface](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreencapturewithsurface)接口以Surface模式启动录屏，传入视频编码器的输入OHNativeWindow对象。

     ```cpp
     // 使用视频编码器输入OHNativeWindow以Surface模式启动屏幕录制
     int result = OH_AVScreenCapture_StartScreenCaptureWithSurface(g_avCapture, sampleInfo_.window);
     OH_LOG_INFO(LOG_APP, "OH_VideoEncoder_Start Started by surface mode %{public}d", result);
     if (result != AV_SCREEN_CAPTURE_ERR_OK) {
         OH_LOG_INFO(LOG_APP, "ScreenCapture Started failed %{public}d", result);
         OH_AVScreenCapture_Release(g_avCapture);
     }
     ```
  3. 屏幕录制的视频数据自动输入视频编码器进行视频编码，可以通过监听视频编码器的输出回调[OH\_AVCodecOnNewOutputBuffer](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconnewoutputbuffer)获取编码视频码流数据（H264或H265格式）。

     ```cpp
     // 视频编码器编码帧输出回调
     void VideoEncoder::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
     {
         (void)codec;
         (void)userData;
         OH_AVCodecBufferAttr attr{};
         OH_AVBuffer_GetBufferAttr(buffer, &attr);
         OH_LOG_INFO(LOG_APP, "H264 Buffer: size=%{public}d flags=%{public}d ", attr.size, attr.flags);
         OH_VideoEncoder_FreeOutputBuffer(codec, index);
     }
     ```

完整代码可参考：

Index.ets:

```ts
import screenCapture from 'libentry.so';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Button('ScreenCapture Buffer Mode')
        .fontSize(20)
        .onClick(() => {
          try {
            let screenWidth = display.getDefaultDisplaySync().width;
            let screenHeight = display.getDefaultDisplaySync().height;
            screenCapture.startBufferMode(screenWidth, screenHeight);
          } catch (err) {
            console.error(`Failed to start screen capture buffer mode, ${JSON.stringify(err)}`);
          }
        });

      Button('ScreenCapture Surface Mode')
        .fontSize(20)
        .onClick(() => {
          try {
            let screenWidth = display.getDefaultDisplaySync().width;
            let screenHeight = display.getDefaultDisplaySync().height;
            screenCapture.startSurfaceMode(screenWidth, screenHeight);
          } catch (err) {
            console.error(`Failed to start screen capture buffer mode, ${JSON.stringify(err)}`);
          }
        });

      Button('Stop ScreenCapture')
        .fontSize(20)
        .onClick(() => {
          screenCapture.stopScreenCapture();
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .justifyContent(FlexAlign.Center);
  }
}
```

SampleInfo.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVCODEC_SAMPLE_INFO_H
#define AVCODEC_SAMPLE_INFO_H

#include "multimedia/player_framework/native_avbuffer.h"
#include "multimedia/player_framework/native_avcodec_base.h"
#include <cstdint>
#include <multimedia/player_framework/native_avcodec_videoencoder.h>
#include <native_buffer/native_buffer.h>
#include <string>

/*
 * Screen recording configuration item
 */
struct SampleInfo {
    std::string videoCodecMime = "";

    int32_t videoWidth = 0;
    int32_t videoHeight = 0;
    OH_AVPixelFormat pixelFormat = AV_PIXEL_FORMAT_NV12;

    OHNativeWindow *window = nullptr;
};

#endif
```

VideoEncoder.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVCODEC_SAMPLE_CALLBACK_H
#define AVCODEC_SAMPLE_CALLBACK_H
#define LOG_DOMAIN 0x3200
#define LOG_TAG "MY_SCNDKDEMO"

#include "SampleInfo.h"
#include <multimedia/player_framework/native_avmuxer.h>
class VideoEncoder {
public:
    int32_t Create(const std::string &videoCodecMime);
    int32_t Config(SampleInfo &sampleInfo);
    int32_t Start();
    int32_t Stop();
    void Release();

private:
    static void OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData);
    static void OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData);
    static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
    static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);

    OH_AVCodec *encoder_ = nullptr;
};
#endif
```

VideoEncoder.cpp:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "VideoEncoder.h"
#include <hilog/log.h>
#include <multimedia/player_framework/native_avcapability.h>

int32_t VideoEncoder::Create(const std::string &videoCodecMime)
{
    encoder_ = OH_VideoEncoder_CreateByMime(videoCodecMime.c_str());
    if (encoder_ == nullptr) {
        return -1;
    }
    return 0;
}

int32_t VideoEncoder::Config(SampleInfo &sampleInfo)
{
    // Configure video encoder
    OH_AVFormat *format = OH_AVFormat_Create();

    OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoWidth);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoHeight);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.pixelFormat);

    int ret = OH_VideoEncoder_Configure(encoder_, format);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Config failed, ret: %{public}d", ret);
    }
    OH_AVFormat_Destroy(format);
    format = nullptr;

    // GetSurface from video encoder
    OH_VideoEncoder_GetSurface(encoder_, &sampleInfo.window); // 视频编码器输入OHNativeWindow

    // SetCallback for video encoder
    OH_VideoEncoder_RegisterCallback(encoder_,
                                     {VideoEncoder::OnCodecError, VideoEncoder::OnCodecFormatChange,
                                      VideoEncoder::OnNeedInputBuffer, VideoEncoder::OnNewOutputBuffer},
                                     nullptr);

    // Prepare video encoder
    OH_VideoEncoder_Prepare(encoder_);

    return 0;
}

int32_t VideoEncoder::Start()
{
    int ret = OH_VideoEncoder_Start(encoder_);
    return ret;
}

int32_t VideoEncoder::Stop()
{
    int ret = OH_VideoEncoder_Flush(encoder_);
    ret = OH_VideoEncoder_Stop(encoder_);
    return ret;
}

void VideoEncoder::Release()
{
    if (encoder_ != nullptr) {
        OH_VideoEncoder_Destroy(encoder_);
        encoder_ = nullptr;
    }
}

void VideoEncoder::OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData)
{
    (void)codec;
    (void)errorCode;
    (void)userData;
}

void VideoEncoder::OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
{
    (void)codec;
    (void)format;
    (void)userData;
}

void VideoEncoder::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
{
    (void)codec;
    (void)index;
    (void)buffer;
    (void)userData;
}

// 视频编码器编码帧输出回调
void VideoEncoder::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
{
    (void)codec;
    (void)userData;
    OH_AVCodecBufferAttr attr{};
    OH_AVBuffer_GetBufferAttr(buffer, &attr);
    OH_LOG_INFO(LOG_APP, "H264 Buffer: size=%{public}d flags=%{public}d ", attr.size, attr.flags);
    OH_VideoEncoder_FreeOutputBuffer(codec, index);
}
```

CAVScreenCaptureToStream.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVSCREENCAPTURESCREENRECORD_CAVSCREENCAPTURETOSTREAM_H
#define AVSCREENCAPTURESCREENRECORD_CAVSCREENCAPTURETOSTREAM_H

#include "CAVScreenCaptureToStream/SampleInfo.h"
#include "CAVScreenCaptureToStream/VideoEncoder.h"
#include <memory>
#include <multimedia/player_framework/native_avscreen_capture_base.h>
#include <thread>

class CAVScreenCaptureToStream {
private:
    static void StopScreenCaptureRecording(struct OH_AVScreenCapture *capture);
    void InitAVScreenCapture(int32_t videoWidth, int32_t videoHeight);
    void InitEncoder(int32_t videoWidth, int32_t videoHeight);

    static void OnErrorToStream(OH_AVScreenCapture *capture, int32_t errorCode, void *userData);
    static void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                  OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData);

    SampleInfo sampleInfo_;

public:
    CAVScreenCaptureToStream(){};
    ~CAVScreenCaptureToStream();

    static CAVScreenCaptureToStream &GetInstance()
    {
        static CAVScreenCaptureToStream avScreenCapture;
        return avScreenCapture;
    }

    void StartScreenCaptureSurfaceMode(int32_t videoWidth, int32_t videoHeight);
    void StartScreenCaptureBufferMode(int32_t videoWidth, int32_t videoHeight);
    void StopScreenCapture();
};
#endif
```

CAVScreenCaptureToStream.cpp：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "CAVScreenCaptureToStream.h"
#include "SampleInfo.h"
#include "VideoEncoder.h"
#include "hilog/log.h"
#include <multimedia/player_framework/native_avscreen_capture.h>
#include <multimedia/player_framework/native_avscreen_capture_errors.h>
#include <thread>

#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200
#define LOG_TAG "CAVSCREENCAPTURETOSTREAM"

using namespace std;

bool g_isRunning = false;
OH_AVScreenCapture *g_avCapture = nullptr;
std::unique_ptr<VideoEncoder> videoEncoder_ = nullptr;

CAVScreenCaptureToStream::~CAVScreenCaptureToStream() {}

/*
 * Screen recording Error callback
 */
void CAVScreenCaptureToStream::OnErrorToStream(OH_AVScreenCapture *capture, int32_t errorCode, void *userData)
{
    (void)capture;
    (void)userData;
    OH_LOG_ERROR(LOG_APP, "ScreenCapture OnError errorCode is %{public}d", errorCode);
}

// 录屏原始数据获取回调
void CAVScreenCaptureToStream::OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                                 OH_AVScreenCaptureBufferType bufferType, int64_t timestamp,
                                                 void *userData)
{
    (void)capture;
    (void)userData;
    if (g_isRunning) {
        if (bufferType == OH_SCREEN_CAPTURE_BUFFERTYPE_VIDEO) {
            // 屏幕录制原始视频数据（RGBA格式）
            OH_AVCodecBufferAttr attr;
            OH_AVBuffer_GetBufferAttr(buffer, &attr);
            OH_LOG_INFO(LOG_APP, "RGBA Buffer: size=%{public}d timestamp=%{public}ld", attr.size, timestamp);

            OH_AVBuffer_Destroy(buffer);
        }
    }
}

/*
 * Configure screen recording parameters
 */
void CAVScreenCaptureToStream::InitAVScreenCapture(int32_t videoWidth, int32_t videoHeight)
{
    if (g_avCapture != nullptr) {
        StopScreenCaptureRecording(g_avCapture);
    }

    g_avCapture = OH_AVScreenCapture_Create();
    if (g_avCapture == nullptr) {
        OH_LOG_ERROR(LOG_APP, "create screen capture failed");
    }
    OH_LOG_INFO(LOG_APP, "ScreenCapture after create sc");

    // Set callback
    OH_AVScreenCapture_SetErrorCallback(g_avCapture, OnErrorToStream, nullptr);
    OH_AVScreenCapture_SetDataCallback(g_avCapture, OnBufferAvailable, nullptr);

    OH_AVScreenCapture_SetCanvasRotation(g_avCapture, true);

    // Initialize configuration information
    OH_AVScreenCaptureConfig config;
    OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_SOURCE_DEFAULT};
    OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
    OH_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC};
    OH_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};

    OH_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = videoWidth, .videoFrameHeight = videoHeight, .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA};

    OH_VideoEncInfo videoEncInfo = {
        .videoCodec = OH_VideoCodecFormat::OH_H264, .videoBitrate = 10000000, .videoFrameRate = 30};

    OH_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo, .videoEncInfo = videoEncInfo};

    config = {
        .captureMode = OH_CAPTURE_HOME_SCREEN,
        .dataType = OH_ORIGINAL_STREAM,
        .audioInfo = audioInfo,
        .videoInfo = videoInfo,
    };

    int result = OH_AVScreenCapture_Init(g_avCapture, config);
    if (result != AV_SCREEN_CAPTURE_ERR_OK) {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OH_AVScreenCapture_Init failed %{public}d", result);
    }
    OH_LOG_INFO(LOG_APP, "ScreenCapture OH_AVScreenCapture_Init %{public}d", result);
}

void CAVScreenCaptureToStream::StopScreenCaptureRecording(struct OH_AVScreenCapture *capture)
{
    if (g_isRunning && capture != nullptr) {
        OH_AVScreenCapture_StopScreenCapture(capture);
        g_isRunning = false;
        OH_LOG_INFO(LOG_APP, "CAVScreenCaptureToStream ScreenCapture StopScreenCapture");
    }
}

/*
 * Initialize configuration information
 */
void CAVScreenCaptureToStream::InitEncoder(int32_t videoWidth, int32_t videoHeight)
{
    // Video encoding configuration
    sampleInfo_.videoWidth = videoWidth;
    sampleInfo_.videoHeight = videoHeight;
    sampleInfo_.videoCodecMime = "video/avc";

    videoEncoder_ = std::make_unique<VideoEncoder>();

    videoEncoder_->Create(sampleInfo_.videoCodecMime);
    videoEncoder_->Config(sampleInfo_);
}

void CAVScreenCaptureToStream::StartScreenCaptureSurfaceMode(int32_t videoWidth, int32_t videoHeight)
{
    InitEncoder(videoWidth, videoHeight);

    InitAVScreenCapture(videoWidth, videoHeight);

    g_isRunning = true;

    videoEncoder_->Start();

    // 使用视频编码器输入OHNativeWindow以Surface模式启动屏幕录制
    int result = OH_AVScreenCapture_StartScreenCaptureWithSurface(g_avCapture, sampleInfo_.window);
    OH_LOG_INFO(LOG_APP, "OH_VideoEncoder_Start Started by surface mode %{public}d", result);
    if (result != AV_SCREEN_CAPTURE_ERR_OK) {
        OH_LOG_INFO(LOG_APP, "ScreenCapture Started failed %{public}d", result);
        OH_AVScreenCapture_Release(g_avCapture);
    }
}

void CAVScreenCaptureToStream::StartScreenCaptureBufferMode(int32_t videoWidth, int32_t videoHeight)
{

    InitAVScreenCapture(videoWidth, videoHeight);

    g_isRunning = true;

    // 以Buffer模式启动屏幕录制
    int result = OH_AVScreenCapture_StartScreenCapture(g_avCapture);
    OH_LOG_INFO(LOG_APP, "OH_VideoEncoder_Start Started by buffer mode %{public}d", result);
    if (result != AV_SCREEN_CAPTURE_ERR_OK) {
        OH_LOG_INFO(LOG_APP, "ScreenCapture Started failed %{public}d", result);
        OH_AVScreenCapture_Release(g_avCapture);
    }
}

/*
 * Stop screen recording
 */
void CAVScreenCaptureToStream::StopScreenCapture()
{
    if (g_isRunning) {
        int32_t ret = OH_AVScreenCapture_StopScreenCapture(g_avCapture);
        if (ret != AV_SCREEN_CAPTURE_ERR_BASE) {
            OH_LOG_ERROR(LOG_APP, "StopScreenCapture OH_AVScreenCapture_StopScreenCapture Result: %{public}d", ret);
        } else {
            OH_LOG_INFO(LOG_APP, "StopScreenCapture OH_AVScreenCapture_StopScreenCapture");
        }
        ret = OH_AVScreenCapture_Release(g_avCapture);
        if (ret != AV_SCREEN_CAPTURE_ERR_BASE) {
            OH_LOG_ERROR(LOG_APP, "StopScreenCapture OH_AVScreenCapture_Release: %{public}d", ret);
        } else {
            OH_LOG_INFO(LOG_APP, "OH_AVScreenCapture_Release success");
        }
        g_isRunning = false;
        g_avCapture = nullptr;

        if (videoEncoder_ != nullptr) {
            videoEncoder_->Stop();
            if (sampleInfo_.window != nullptr) {
                OH_NativeWindow_DestroyNativeWindow(sampleInfo_.window);
                sampleInfo_.window = nullptr;
            }
            videoEncoder_->Release();
            videoEncoder_.reset();
            OH_LOG_INFO(LOG_APP, "Video encoder release successful");
        }
        OH_LOG_INFO(LOG_APP, "Release successful");
    }
}
```

napi\_init.cpp:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "napi/native_api.h"
#include "./CAVScreenCaptureToStream/CAVScreenCaptureToStream.h"

static napi_value StartBufferMode(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t videoWidth, videoHeight;
    napi_get_value_int32(env, args[0], &videoWidth);
    napi_get_value_int32(env, args[1], &videoHeight);
    CAVScreenCaptureToStream::GetInstance().StartScreenCaptureBufferMode(videoWidth, videoHeight);

    return nullptr;
}

static napi_value StartSurfaceMode(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t outputFd, videoWidth, videoHeight;
    napi_get_value_int32(env, args[0], &videoWidth);
    napi_get_value_int32(env, args[1], &videoHeight);
    CAVScreenCaptureToStream::GetInstance().StartScreenCaptureSurfaceMode(videoWidth, videoHeight);

    return nullptr;
}

static napi_value StopScreenCapture(napi_env env, napi_callback_info info)
{
    (void)env;
    (void)info;
    CAVScreenCaptureToStream::GetInstance().StopScreenCapture();
    return nullptr;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"startBufferMode", nullptr, StartBufferMode, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"startSurfaceMode", nullptr, StartSurfaceMode, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"stopScreenCapture", nullptr, StopScreenCapture, nullptr, nullptr, nullptr, napi_default, nullptr},
    };
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

CMakeLists.txt:

```cmake
# the minimum version of CMake.
cmake_minimum_required(VERSION 3.5.0)
project(AVScreenCapturerStream)

set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

if(DEFINED PACKAGE_FIND_FILE)
    include(${PACKAGE_FIND_FILE})
endif()

include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)

add_library(entry SHARED napi_init.cpp CAVScreenCaptureToStream/CAVScreenCaptureToStream.cpp
                                       CAVScreenCaptureToStream/VideoEncoder.cpp)

target_link_libraries(entry PUBLIC libace_napi.z.so libEGL.so libGLESv3.so libace_ndk.z.so libuv.so libhilog_ndk.z.so
                                       libnative_media_codecbase.so libnative_media_core.so libnative_media_vdec.so libnative_window.so
                                       libnative_media_venc.so libnative_media_acodec.so libnative_media_avdemuxer.so libnative_media_avsource.so libnative_media_avmuxer.so
                                       libohaudio.so libnative_avscreen_capture.so)
```
