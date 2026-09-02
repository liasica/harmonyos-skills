---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-46
title: 如何将录屏码流数据从Native侧传递到ArkTS侧
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何将录屏码流数据从Native侧传递到ArkTS侧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:41a92fc1b10fbf2e1d51a77e99f76ca844dd2cfcc39bea0b5f60b1e49286f6e1
---

## 问题现象

屏幕录制实时获取码流的过程中，如何将Native侧获取的码流数据按帧传递到ArkTS侧函数处理。

## 背景知识

* 屏幕录制功能支持开发者获取屏幕数据，开发者可通过调用[AVScreenCapture](../harmonyos-guides/media-kit-intro.md#avscreencapture)模块的C API，采集设备内外的音视频数据源。
* [AVCodec Kit](../harmonyos-guides/avcodec-kit-intro.md)提供音视频的编解码、媒体文件的解析、封装、媒体数据输入等原子能力。开发者可以调用AVCodec Kit的C API完成[视频编码](../harmonyos-guides/video-encoding.md)。
* [napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)是Node-API接口之一，用于创建一个线程安全的JavaScript函数。该函数主要用于在多个线程之间共享和调用，避免竞争条件和死锁。具体可参考：[使用Node-API接口进行线程安全开发](../harmonyos-guides/use-napi-thread-safety.md)。
* 如果需要持续录制或后台录制，请申请长时任务避免进入挂起（Suspend）状态。具体参考[长时任务开发指导](../harmonyos-guides/continuous-task.md)。

## 解决方案

在录屏获取码流数据的场景中，为了避免阻塞主线程，处理视频编码输出通常在单独的子线程中实现。为了将Native侧的编码数据传递到ArkTS侧进行处理，可以创建一个线程安全的函数，通过线程安全函数调用ArkTS侧的回调函数。在编码码流数据到达后，在Native侧调用线程安全函数，将Native侧获取的编码码流数据，按帧传递到ArkTS侧的回调函数中处理。

具体实现步骤如下：

1. 在ArkTS侧，启动屏幕录制，并将回调函数传递到Native侧。

   ```ts
   export const startScreenCapture: (width: number, height: number, callback: (buffer: ArrayBuffer) => void) => void;
   ```

   ```ts
     let callback: (buffer: ArrayBuffer) => void = (buffer: ArrayBuffer) => {
       if (this.file) {
         try {
           fileIo.writeSync(this.file.fd, buffer);
         } catch (error) {
           console.error(`Failed to write file. Cause: ${JSON.stringify(error)}`);
         }
       }
     };
     screenCapture.startScreenCapture(screenWidth, screenHeight, callback);
   } catch (err) {
     console.error(`Failed to start screen capture buffer mode, ${JSON.stringify(err)}`);
   }
   ```
2. 在Native侧，通过ArkTS侧传递的回调函数创建线程安全函数，并启动屏幕录制。

   ```cpp
   static napi_value StartScreenCapture(napi_env env, napi_callback_info info)
   {
       size_t argc = 3;
       napi_value args[3] = {nullptr};
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       int32_t videoWidth, videoHeight;
       napi_get_value_int32(env, args[0], &videoWidth);
       napi_get_value_int32(env, args[1], &videoHeight);
       // 注册回调函数
       CAVScreenCaptureToStream::GetInstance().RegisterDataCallback(env, info, args[2]);
       // 启动屏幕录制
       CAVScreenCaptureToStream::GetInstance().StartScreenCapture(videoWidth, videoHeight);

       return nullptr;
   }
   ```

   ```cpp
   void CAVScreenCaptureToStream::RegisterDataCallback(napi_env &env, napi_callback_info &info, napi_value &callback)
   {
       (void)info;
       napi_value resource = nullptr;
       napi_create_string_utf8(env, "DataCallback", NAPI_AUTO_LENGTH, &resource);
       napi_create_threadsafe_function(env, callback, nullptr, resource, 0, 1, nullptr, nullptr, nullptr, CallJs,
                                       &sampleInfo_.func);
   }
   ```
3. 码流数据到达时，调用线程安全函数，将码流数据作为参数传递到ArkTS侧处理。

   ```cpp
   void CAVScreenCaptureToStream::CallJs(napi_env env, napi_value jsCb, void *context, void *data)
   {
       (void)context;
       OH_AVBuffer *avBuffer = reinterpret_cast<OH_AVBuffer *>(data);
       OH_AVCodecBufferAttr attr{};
       OH_AVBuffer_GetBufferAttr(avBuffer, &attr);
       // 创建ArrayBuffer
       uint8_t *buffer = nullptr;
       napi_value argv = nullptr;
       napi_create_arraybuffer(env, attr.size, (void **)&buffer, &argv);
       if (buffer != nullptr) {
           uint8_t *addr = OH_AVBuffer_GetAddr(avBuffer);
           for (size_t i = 0; i < attr.size; ++i) {
               buffer[i] = addr[i];
           }
       } else {
           OH_LOG_ERROR(LOG_APP, "napi_create_arraybuffer failed");
           return;
       }
       // 调用JS侧回调函数
       napi_value result = nullptr;
       napi_value undefined = nullptr;
       napi_get_undefined(env, &undefined);
       napi_call_function(env, undefined, jsCb, 1, &argv, &result);
   }
   ```

   ```cpp
   // 视频编码器编码帧输出回调
   void VideoEncoder::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   {
       (void)codec;
       SampleInfo *info = reinterpret_cast<SampleInfo *>(userData);
       // 调用线程安全函数
       napi_call_threadsafe_function(info->func, buffer, napi_tsfn_nonblocking);
       OH_VideoEncoder_FreeOutputBuffer(codec, index);
   }
   ```

完整参考代码如下：

CMakeLists.txt：

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

index.d.ts:

```ts
export const startScreenCapture: (width: number, height: number, callback: (buffer: ArrayBuffer) => void) => void;
export const stopScreenCapture: () => void;
```

napi\_init.cpp：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "napi/native_api.h"
#include "./CAVScreenCaptureToStream/CAVScreenCaptureToStream.h"

static napi_value StartScreenCapture(napi_env env, napi_callback_info info)
{
    size_t argc = 3;
    napi_value args[3] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t videoWidth, videoHeight;
    napi_get_value_int32(env, args[0], &videoWidth);
    napi_get_value_int32(env, args[1], &videoHeight);
    // 注册回调函数
    CAVScreenCaptureToStream::GetInstance().RegisterDataCallback(env, info, args[2]);
    // 启动屏幕录制
    CAVScreenCaptureToStream::GetInstance().StartScreenCapture(videoWidth, videoHeight);

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
        {"startScreenCapture", nullptr, StartScreenCapture, nullptr, nullptr, nullptr, napi_default, nullptr},
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

SampleInfo.h：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVCODEC_SAMPLE_INFO_H
#define AVCODEC_SAMPLE_INFO_H

#include "napi/native_api.h"
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
    int32_t videoWidth = 0;
    int32_t videoHeight = 0;
    std::string videoCodecMime = "";
    OH_AVPixelFormat pixelFormat = AV_PIXEL_FORMAT_NV12;

    OHNativeWindow *window = nullptr;

    napi_threadsafe_function func;
};

#endif
```

VideoEncoder.h：

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

VideoEncoder.cpp：

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

    OH_VideoEncoder_GetSurface(encoder_, &sampleInfo.window); // 视频编码器输入OHNativeWindow

    OH_VideoEncoder_RegisterCallback(encoder_,
                                     {VideoEncoder::OnCodecError, VideoEncoder::OnCodecFormatChange,
                                      VideoEncoder::OnNeedInputBuffer, VideoEncoder::OnNewOutputBuffer},
                                     &sampleInfo);

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
    SampleInfo *info = reinterpret_cast<SampleInfo *>(userData);
    // 调用线程安全函数
    napi_call_threadsafe_function(info->func, buffer, napi_tsfn_nonblocking);
    OH_VideoEncoder_FreeOutputBuffer(codec, index);
}
```

CAVScreenCaptureToStream.h：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVSCREENCAPTURESCREENRECORD_CAVSCREENCAPTURETOSTREAM_H
#define AVSCREENCAPTURESCREENRECORD_CAVSCREENCAPTURETOSTREAM_H

#include "napi/native_api.h"
#include "CAVScreenCaptureToStream/SampleInfo.h"
#include "CAVScreenCaptureToStream/VideoEncoder.h"
#include <multimedia/player_framework/native_avscreen_capture_base.h>

class CAVScreenCaptureToStream {
private:
    void InitAVScreenCapture(int32_t videoWidth, int32_t videoHeight);
    void InitEncoder(int32_t videoWidth, int32_t videoHeight);

    static void OnErrorToStream(OH_AVScreenCapture *capture, int32_t errorCode, void *userData);
    static void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                  OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData);

    static void StopScreenCaptureRecording(struct OH_AVScreenCapture *capture);
    static void CallJs(napi_env env, napi_value jsCb, void *context, void *data);

    SampleInfo sampleInfo_;

public:
    CAVScreenCaptureToStream(){};
    ~CAVScreenCaptureToStream();

    static CAVScreenCaptureToStream &GetInstance()
    {
        static CAVScreenCaptureToStream avScreenCapture;
        return avScreenCapture;
    }

    void RegisterDataCallback(napi_env &env, napi_callback_info &info, napi_value &callback);
    void StartScreenCapture(int32_t videoWidth, int32_t videoHeight);
    void StopScreenCapture();
};
#endif
```

CAVScreenCaptureToStream.cpp:

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

void CAVScreenCaptureToStream::CallJs(napi_env env, napi_value jsCb, void *context, void *data)
{
    (void)context;
    OH_AVBuffer *avBuffer = reinterpret_cast<OH_AVBuffer *>(data);
    OH_AVCodecBufferAttr attr{};
    OH_AVBuffer_GetBufferAttr(avBuffer, &attr);
    // 创建ArrayBuffer
    uint8_t *buffer = nullptr;
    napi_value argv = nullptr;
    napi_create_arraybuffer(env, attr.size, (void **)&buffer, &argv);
    if (buffer != nullptr) {
        uint8_t *addr = OH_AVBuffer_GetAddr(avBuffer);
        for (size_t i = 0; i < attr.size; ++i) {
            buffer[i] = addr[i];
        }
    } else {
        OH_LOG_ERROR(LOG_APP, "napi_create_arraybuffer failed");
        return;
    }
    // 调用JS侧回调函数
    napi_value result = nullptr;
    napi_value undefined = nullptr;
    napi_get_undefined(env, &undefined);
    napi_call_function(env, undefined, jsCb, 1, &argv, &result);
}

void CAVScreenCaptureToStream::RegisterDataCallback(napi_env &env, napi_callback_info &info, napi_value &callback)
{
    (void)info;
    napi_value resource = nullptr;
    napi_create_string_utf8(env, "DataCallback", NAPI_AUTO_LENGTH, &resource);
    napi_create_threadsafe_function(env, callback, nullptr, resource, 0, 1, nullptr, nullptr, nullptr, CallJs,
                                    &sampleInfo_.func);
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

void CAVScreenCaptureToStream::StartScreenCapture(int32_t videoWidth, int32_t videoHeight)
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

        napi_release_threadsafe_function(sampleInfo_.func, napi_tsfn_release);

        OH_LOG_INFO(LOG_APP, "Release successful");
    }
}
```

Index.ets:

```ts
import screenCapture from 'libentry.so';
import { display } from '@kit.ArkUI';
import { fileIo } from '@kit.CoreFileKit';
import { Context } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  private file: fileIo.File | undefined;

  aboutToDisappear(): void {
    if (this.file) {
      try {
        fileIo.closeSync(this.file);
        this.file = undefined;
      } catch (error) {
        console.error(`Failed to close file ${this.file?.path}. Cause: ${JSON.stringify(error)}`);
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('Start ScreenCapture')
        .fontSize(20)
        .onClick(() => {
          if (this.file) {
            try {
              fileIo.closeSync(this.file);
              this.file = undefined;
            } catch (error) {
              console.error(`Failed to close file ${this.file?.path}. Cause: ${JSON.stringify(error)}`);
            }
          }
          try {
            let context = this.getUIContext().getHostContext() as Context;
            let filePath = context.filesDir + `/${util.generateRandomUUID()}`;
            this.file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
          } catch (error) {
            console.error(`Failed to create file. Cause: ${JSON.stringify(error)}`);
          }
          try {
            let screenWidth = display.getDefaultDisplaySync().width;
            let screenHeight = display.getDefaultDisplaySync().height;
            let callback: (buffer: ArrayBuffer) => void = (buffer: ArrayBuffer) => {
              if (this.file) {
                try {
                  fileIo.writeSync(this.file.fd, buffer);
                } catch (error) {
                  console.error(`Failed to write file. Cause: ${JSON.stringify(error)}`);
                }
              }
            };
            screenCapture.startScreenCapture(screenWidth, screenHeight, callback);
          } catch (err) {
            console.error(`Failed to start screen capture buffer mode, ${JSON.stringify(err)}`);
          }
        });

      Button('Stop ScreenCapture')
        .fontSize(20)
        .onClick(() => {
          screenCapture.stopScreenCapture();
          if (this.file) {
            try {
              fileIo.closeSync(this.file);
              this.file = undefined;
            } catch (error) {
              console.error(`Failed to close file ${this.file?.path}. Cause: ${JSON.stringify(error)}`);
            }
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .justifyContent(FlexAlign.Center);
  }
}
```
