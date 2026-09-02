---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-44
title: 如何同时录制设备内部音频和麦克风音频，并合成两路音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何同时录制设备内部音频和麦克风音频，并合成两路音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a6bffdb0516bdbb501884ae30e2880a5c9e7d1a0cdec299580cd1e1274069b2
---

## 问题现象

如何实现音频双录，即同时录制系统音频与麦克风音频，并在录制完成后将内录音频与外录音频合成。

## 背景知识

* 音频内录与外录是两种不同的录音方式。音频内录是指直接录制设备系统内部播放的声音，音频外录是指通过麦克风录制外部环境声音。
* 开发者可以通过[AVScreenCapture](../harmonyos-references/capi-native-avscreen-capture-h.md)模块的C API，采集设备内外的音视频数据源。开发者可以设置屏幕录制所需要的音频参数[OH\_AudioInfo](../harmonyos-references/capi-avscreencapture-oh-audioinfo.md)包括内录和麦克风音频[OH\_AudioCaptureInfo](../harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo.md)。
* [AVCodec Kit](../harmonyos-guides/avcodec-kit-intro.md)提供音视频的编解码、媒体文件的解析、封装、媒体数据输入等原子能力。开发者可以调用AVCodec Kit的C API完成[音频编码](../harmonyos-guides/audio-encoding.md)和[媒体数据封装](../harmonyos-guides/audio-video-muxer.md)。
* [@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)是用于编辑音视频文件的三方库，可以调用ffmpeg命令完成音视频文件的编辑，比如通过音频滤镜对多个音频进行混音。
* 当需要使用麦克风时，需要申请[ohos.permission.MICROPHONE](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmicrophone)麦克风权限。申请方式请参考：[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。
* 如果需要持续录制或后台录制，请申请长时任务避免进入挂起（Suspend）状态。[具体参考长时任务开发指导](../harmonyos-guides/continuous-task.md)。

## 解决方案

音频双录场景可以通过AVScreenCapture屏幕录制模块采集设备内外的音频数据，然后将内外音频数据输入[AudioCodec](../harmonyos-references/capi-audiocodec.md)音频编码模块分别编码内录与外录音频流，最后通过[AVMuxer](../harmonyos-references/capi-avmuxer.md)媒体文件封装模块将内录和外录音频流封装到音频文件的不同音频轨道实现。在录制完成后可以通过@ohos/mp4parser(V2.0.7)调用ffmpeg混音命令合成内录和外录的音频轨道完成混音。

具体实现步骤如下：

1. 创建AVScreenCapture实例，配置音频采集参数为同时采集内部和麦克风音频数据。

   ```cpp
   void CAVScreenCaptureToStream::InitAVScreenCapture()
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
       OH_AVScreenCapture_SetStateCallback(g_avCapture, OnSurfaceStateChange, nullptr);

       OH_AVScreenCapture_SetMicrophoneEnabled(g_avCapture, true);
       OH_AVScreenCapture_SetDataCallback(g_avCapture, OnBufferAvailable, audioEncContext_);
       OH_AVScreenCapture_SetCanvasRotation(g_avCapture, true);

       OH_AVScreenCaptureConfig config;
       // 麦克风音频采集参数
       OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_MIC};
       // 内录音频采集参数
       OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
       // 音频输出规格
       OH_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC};
       // 配置音频采集参数
       OH_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};
       // 录屏配置信息
       config = {
           .captureMode = OH_CAPTURE_HOME_SCREEN,
           .dataType = OH_ORIGINAL_STREAM,
           .audioInfo = audioInfo,
       };

       int result = OH_AVScreenCapture_Init(g_avCapture, config);
       if (result != AV_SCREEN_CAPTURE_ERR_OK) {
           OH_LOG_INFO(LOG_APP, "ScreenCapture OH_AVScreenCapture_Init failed %{public}d", result);
       }
       OH_LOG_INFO(LOG_APP, "ScreenCapture OH_AVScreenCapture_Init %{public}d", result);
   }
   ```
2. 创建并配置内录与外录音频编码器。创建媒体文件封装器，并添加内录与外录的音频轨道。

   ```cpp
   void CAVScreenCaptureToStream::InitMuxerAndEncoder(int32_t outputFd)
   {
       sampleInfo_.outputFd = outputFd;

       // 音频编码参数
       sampleInfo_.audioCodecMime = OH_AVCODEC_MIMETYPE_AUDIO_AAC;
       sampleInfo_.audioSampleFormat = OH_BitsPerSample::SAMPLE_S16LE;
       sampleInfo_.audioSampleRate = 48000;
       sampleInfo_.audioChannelCount = 2;
       sampleInfo_.audioBitRate = 96000;
       sampleInfo_.audioChannelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
       sampleInfo_.audioMaxInputSize = sampleInfo_.audioSampleRate * 0.02 * sampleInfo_.audioChannelCount * sizeof(short);
       // 音频编码器
       audioEncoderInner_ = std::make_unique<AudioEncoder>(); // 内录音频编码器
       audioEncoderMic_ = std::make_unique<AudioEncoder>();   // 外录音频编码器
       // 媒体文件封装器
       muxer_ = std::make_unique<Muxer>();
       muxer_->Create(sampleInfo_.outputFd);
       muxer_->Config(sampleInfo_);

       CreateEncoder();
   }
   ```

   ```cpp
   int32_t Muxer::Config(SampleInfo &sampleInfo)
   {
       OH_AVFormat *formatAudio = OH_AVFormat_CreateAudioFormat(sampleInfo.audioCodecMime.data(),
                                                                sampleInfo.audioSampleRate, sampleInfo.audioChannelCount);

       OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_PROFILE, AAC_PROFILE_LC);

       // 内录编码音频轨道
       int32_t ret = OH_AVMuxer_AddTrack(muxer_, &innerTrackId_, formatAudio);
       if (ret != AV_ERR_OK) {
           OH_LOG_ERROR(LOG_APP, "AddTrack failed");
       }
       // 外录音频编码轨道
       ret = OH_AVMuxer_AddTrack(muxer_, &micTrackId_, formatAudio);
       if (ret != AV_ERR_OK) {
           OH_LOG_ERROR(LOG_APP, "AddTrack failed");
       }
       OH_AVFormat_Destroy(formatAudio);

       return ret;
   }
   ```
3. 监听录屏数据获取回调[OH\_AVScreenCapture\_OnBufferAvailable](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)获取设备内部与麦克风采集的原始音频数据。

   ```cpp
   void CAVScreenCaptureToStream::OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                                    OH_AVScreenCaptureBufferType bufferType, int64_t timestamp,
                                                    void *userData)
   {
       (void)capture;
       (void)timestamp;
       if (g_isRunning) {
           CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
           std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
           if (bufferType == OH_AVScreenCaptureBufferType::OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_INNER) {
               // 内录音频原始数据，写入数据缓冲区
               OH_AVCodecBufferAttr attr;
               OH_AVBuffer_GetBufferAttr(buffer, &attr);
               uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
               codecUserData->innerCache.WriteCache(addr, attr.size);
               OH_AVBuffer_Destroy(buffer);
           } else if (bufferType == OH_AVScreenCaptureBufferType::OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_MIC) {
               // 外录音频原始数据，写入数据缓冲区
               OH_AVCodecBufferAttr attr;
               OH_AVBuffer_GetBufferAttr(buffer, &attr);
               uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
               codecUserData->micCache.WriteCache(addr, attr.size);
               OH_AVBuffer_Destroy(buffer);
           }
       }
   }
   ```
4. 将内录与外录的原始音频数据通过内录与外录音频编码器分别编码，并通过媒体文件封装其写入对应的音频轨道。

   ```cpp
   void CAVScreenCaptureToStream::AudioEncInputThread()
   {
       while (g_isRunning) {
           if (!isStarted_) {
               OH_LOG_INFO(LOG_APP, "Audio encoder input thread out");
               break;
           }
           std::unique_lock<std::mutex> lock(audioEncContext_->inputMutex);
           audioEncContext_->inputCond.wait_for(lock, 1s);
           if (!isStarted_) {
               OH_LOG_INFO(LOG_APP, "Audio encoder input thread out");
               break;
           }
           if (audioEncContext_->inputBufferInfoQueue.empty()) {
               OH_LOG_INFO(LOG_APP, "Audio Buffer queue is empty");
               continue;
           }
           CodecBufferInfo bufferInfo = audioEncContext_->inputBufferInfoQueue.front();
           if (bufferInfo.codec == audioEncoderInner_->encoder_) {
               // 从数据缓冲区中读取内录原始音频数据，写入内录音频编码器
               if (audioEncContext_->innerCache.remainLen < sampleInfo_.audioMaxInputSize) {
                   continue;
               }
               audioEncContext_->inputBufferInfoQueue.pop();
               uint8_t *inputBufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
               audioEncContext_->innerCache.ReadCache(inputBufferAddr, sampleInfo_.audioMaxInputSize);
               lock.unlock();
               bufferInfo.attr.size = sampleInfo_.audioMaxInputSize;
               bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
               int32_t ret = audioEncoderInner_->PushInputData(bufferInfo);
               if (ret) {
                   OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
                   break;
               }
           } else {
               // 从数据缓冲区中读取外录原始音频数据，写入外录音频编码器
               if (audioEncContext_->micCache.remainLen < sampleInfo_.audioMaxInputSize) {
                   continue;
               }
               audioEncContext_->inputBufferInfoQueue.pop();
               uint8_t *inputBufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
               audioEncContext_->micCache.ReadCache(inputBufferAddr, sampleInfo_.audioMaxInputSize);
               lock.unlock();
               bufferInfo.attr.size = sampleInfo_.audioMaxInputSize;
               bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
               int32_t ret = audioEncoderMic_->PushInputData(bufferInfo);
               if (ret) {
                   OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
                   break;
               }
           }
       }
   }

   void CAVScreenCaptureToStream::AudioEncOutputThread()
   {
       while (g_isRunning) {
           if (!isStarted_) {
               OH_LOG_INFO(LOG_APP, "Audio encoder output thread out");
               break;
           }
           std::unique_lock<std::mutex> lock(audioEncContext_->outputMutex);
           audioEncContext_->outputCond.wait_for(lock, 1s);

           if (!isStarted_) {
               OH_LOG_INFO(LOG_APP, "Audio encoder output thread out");
               break;
           }

           if (audioEncContext_->outputBufferInfoQueue.empty()) {
               OH_LOG_ERROR(LOG_APP, "Buffer queue is empty");
               continue;
           }

           CodecBufferInfo bufferInfo = audioEncContext_->outputBufferInfoQueue.front();
           audioEncContext_->outputBufferInfoQueue.pop();
           lock.unlock();
           if (bufferInfo.codec == audioEncoderInner_->encoder_) {
               // 内录编码音频写入内录音频轨道
               muxer_->WriteSample(muxer_->GetInnerTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                                   bufferInfo.attr);
               int32_t ret = audioEncoderInner_->FreeOutputData(bufferInfo.bufferIndex);
               if (ret) {
                   OH_LOG_ERROR(LOG_APP, "Encoder output thread out");
                   break;
               }
           } else {
               // 外录编码音频流写入外录音频轨道
               muxer_->WriteSample(muxer_->GetMicTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                                   bufferInfo.attr);
               int32_t ret = audioEncoderMic_->FreeOutputData(bufferInfo.bufferIndex);
               if (ret) {
                   OH_LOG_ERROR(LOG_APP, "Encoder output thread out");
                   break;
               }
           }
       }
   }
   ```
5. 录制完成后，调用ffmpeg指令编辑录制生成的音频文件，混合内录和外录音频轨道，生成内录与外录混合后的音频文件。

   ```ts
   /**
    * 调用ffmpeg指令混合两路音频
    * @param inputFilePath 输入音频文件沙箱路径
    * @param outputFilePath 输出音频文件沙箱路径
    */
   async mixAudioTrack(inputFilePath: string, outputFilePath: string) {
     try {
       if (fileIo.accessSync(outputFilePath)) {
         fileIo.unlinkSync(outputFilePath);
       }
     } catch (error) {
       console.error(`Failed to unlink output file, Cause: ${JSON.stringify(error)}`);
       return;
     }

     let callback: ICallBack = {
       callBackResult: (code: number) => {
         if (code === 0) {
           console.info('Mixed audio succeed');
         } else {
           console.info('Mixed audio failed');
         }
       },
     };
     // 混音命令，将原始音频文件的两路音频轨道合成一路，生成混音后的音频文件。
     let cmd =
       `ffmpeg -i ${inputFilePath} -filter_complex "[0:a:0]volume=0.5[a1];[0:a:1]volume=1.0[a2];[a1][a2]amix=inputs=2:duration=longest" ${outputFilePath}`;
     MP4Parser.ffmpegCmd(cmd, callback);
   }
   ```

完整示例参考如下：

Index.ets:

```ts
import screenCapture from 'libentry.so';
import { Context } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { ICallBack, MP4Parser } from '@ohos/mp4parser';

@Entry
@Component
struct Index {
  filePath: string = '';
  recordFile?: fileIo.File;
  isRecording: boolean = false;

  /**
   * 调用ffmpeg指令混合两路音频
   * @param inputFilePath 输入音频文件沙箱路径
   * @param outputFilePath 输出音频文件沙箱路径
   */
  async mixAudioTrack(inputFilePath: string, outputFilePath: string) {
    try {
      if (fileIo.accessSync(outputFilePath)) {
        fileIo.unlinkSync(outputFilePath);
      }
    } catch (error) {
      console.error(`Failed to unlink output file, Cause: ${JSON.stringify(error)}`);
      return;
    }

    let callback: ICallBack = {
      callBackResult: (code: number) => {
        if (code === 0) {
          console.info('Mixed audio succeed');
        } else {
          console.info('Mixed audio failed');
        }
      },
    };
    // 混音命令，将原始音频文件的两路音频轨道合成一路，生成混音后的音频文件。
    let cmd =
      `ffmpeg -i ${inputFilePath} -filter_complex "[0:a:0]volume=0.5[a1];[0:a:1]volume=1.0[a2];[a1][a2]amix=inputs=2:duration=longest" ${outputFilePath}`;
    MP4Parser.ffmpegCmd(cmd, callback);
  }

  build() {
    Column({ space: 20 }) {
      Button('Start ScreenCapture')
        .fontSize(20)
        .onClick(() => {
          if (this.isRecording) {
            return;
          }
          try {
            let context = this.getUIContext().getHostContext() as Context;
            this.filePath = context.filesDir + `/${new Date().getTime()}.m4a`;
            this.recordFile = fileIo.openSync(this.filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.WRITE_ONLY);
            screenCapture.startScreenCapture(this.recordFile.fd);
            this.isRecording = true;
          } catch (err) {
            console.error(`Failed to start screen capture, ${JSON.stringify(err)}`);
          }
        });

      Button('Stop ScreenCapture')
        .fontSize(20)
        .onClick(() => {
          if (!this.isRecording) {
            return;
          }
          try {
            screenCapture.stopScreenCapture();
            this.isRecording = false;
          } catch (err) {
            console.error(`Failed to stop screen capture, ${JSON.stringify(err)}`);
          } finally {
            if (this.recordFile) {
              fileIo.closeSync(this.recordFile.fd);
            }
          }
        });

      Button('Mix Audio')
        .fontSize(20)
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as Context;
          let outputFilepath = context.filesDir + `/output.m4a`;
          this.mixAudioTrack(this.filePath, outputFilepath);
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

napi\_init.cpp:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "./CAVScreenCaptureToStream/CAVScreenCaptureToStream.h"
#include "napi/native_api.h"

static napi_value StartScreenCaptureToStream(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    int32_t outputFd;
    napi_get_value_int32(env, args[0], &outputFd);
    CAVScreenCaptureToStream::GetInstance().StartScreenCapture(outputFd);

    return nullptr;
}

static napi_value StopScreenCaptureToStream(napi_env env, napi_callback_info info)
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
        {"startScreenCapture", nullptr, StartScreenCaptureToStream, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"stopScreenCapture", nullptr, StopScreenCaptureToStream, nullptr, nullptr, nullptr, napi_default, nullptr},
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

SampleInfo.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVCODEC_SAMPLE_INFO_H
#define AVCODEC_SAMPLE_INFO_H

#include "multimedia/player_framework/native_avbuffer.h"
#include "multimedia/player_framework/native_avcodec_base.h"
#include <condition_variable>
#include <cstdint>
#include <queue>
#include <string>

/*
 * Screen recording configuration item
 */
struct SampleInfo {
    int32_t outputFd = -1;

    std::string audioCodecMime = "";
    int32_t audioSampleFormat = 0;
    int32_t audioSampleRate = 0;
    int32_t audioChannelCount = 0;
    int32_t audioBitRate = 0;
    int64_t audioChannelLayout = 0;
    int32_t audioMaxInputSize = 0;
};

/*
 * Buffer Info
 */
struct CodecBufferInfo {
    OH_AVCodec *codec;
    uint32_t bufferIndex = 0;
    uintptr_t *buffer = nullptr;
    uint8_t *bufferAddr = nullptr;
    OH_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC_BUFFER_FLAGS_NONE};

    CodecBufferInfo(uint32_t argBufferIndex, OH_AVBuffer *argBuffer, OH_AVCodec *codec)
        : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)), codec(codec)
    {
        OH_AVBuffer_GetBufferAttr(argBuffer, &attr);
    };
};

struct BufferCache {
    std::vector<char> cache;
    int32_t remainLen = 0;

    void ClearCache()
    {
        cache.clear();
        remainLen = 0;
    }

    void WriteCache(void *buffer, int32_t bufferLen)
    {
        if (bufferLen + remainLen > cache.size()) {
            cache.resize(remainLen + bufferLen);
        }
        for (int32_t idx = 0; idx < bufferLen; ++idx) {
            cache.data()[remainLen + idx] = ((uint8_t *)buffer)[idx];
        }
        remainLen += bufferLen;
    }

    bool ReadCache(void *buffer, int32_t bufferLen)
    {
        if (remainLen < bufferLen) {
            return false;
        }
        for (int32_t idx = 0; idx < bufferLen; ++idx) {
            ((uint8_t *)buffer)[idx] = cache.data()[idx];
        }
        remainLen = remainLen - bufferLen;
        if (remainLen > 0) {
            for (int32_t idx = 0; idx < remainLen; ++idx) {
                cache.data()[idx] = cache.data()[bufferLen + idx];
            }
        }
        return true;
    }
};

/*
 * Buffer Data
 */
struct CodecUserData {
public:
    std::mutex inputMutex;
    std::condition_variable inputCond;
    std::queue<CodecBufferInfo> inputBufferInfoQueue;

    std::mutex outputMutex;
    std::condition_variable outputCond;
    std::queue<CodecBufferInfo> outputBufferInfoQueue;

    BufferCache innerCache;
    BufferCache micCache;
};

#endif
```

Muxer.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef MUXER_H
#define MUXER_H

#include "SampleInfo.h"
#include "multimedia/player_framework/native_avmuxer.h"

class Muxer {
public:
    Muxer() = default;
    ~Muxer();

    int32_t Create(int32_t fd);
    int32_t Config(SampleInfo &sampleInfo);
    int32_t Start();
    int32_t WriteSample(int32_t trackId, OH_AVBuffer *buffer, OH_AVCodecBufferAttr &attr);
    void Release();
    int32_t GetInnerTrackId();
    int32_t GetMicTrackId();

private:
    OH_AVMuxer *muxer_ = nullptr;
    int32_t innerTrackId_ = -1;
    int32_t micTrackId_ = -1;
    std::mutex writeMutex_;
};

#endif
```

Muxer.cpp:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "Muxer.h"
#include <cstdint>
#include <hilog/log.h>

#undef LOG_TAG
#define LOG_TAG "Muxer"

Muxer::~Muxer() { Release(); }

/*
 * Create an encapsulate instance object and set the encapsulation format to mp4
 */
int32_t Muxer::Create(int32_t fd)
{
    muxer_ = OH_AVMuxer_Create(fd, AV_OUTPUT_FORMAT_M4A);
    if (muxer_ == nullptr) {
        return -1;
    }
    return 0;
}

int32_t Muxer::Config(SampleInfo &sampleInfo)
{
    OH_AVFormat *formatAudio = OH_AVFormat_CreateAudioFormat(sampleInfo.audioCodecMime.data(),
                                                             sampleInfo.audioSampleRate, sampleInfo.audioChannelCount);

    OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_PROFILE, AAC_PROFILE_LC);

    // 内录编码音频轨道
    int32_t ret = OH_AVMuxer_AddTrack(muxer_, &innerTrackId_, formatAudio);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "AddTrack failed");
    }
    // 外录音频编码轨道
    ret = OH_AVMuxer_AddTrack(muxer_, &micTrackId_, formatAudio);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "AddTrack failed");
    }
    OH_AVFormat_Destroy(formatAudio);

    return ret;
}

int32_t Muxer::Start()
{
    int ret = OH_AVMuxer_Start(muxer_);
    return ret;
}

int32_t Muxer::WriteSample(int32_t trackId, OH_AVBuffer *buffer, OH_AVCodecBufferAttr &attr)
{
    std::lock_guard<std::mutex> lock(writeMutex_);

    int32_t ret = OH_AVBuffer_SetBufferAttr(buffer, &attr);

    ret = OH_AVMuxer_WriteSampleBuffer(muxer_, trackId, buffer);
    return ret;
}

void Muxer::Release()
{
    if (muxer_ != nullptr) {
        OH_AVMuxer_Destroy(muxer_);
        muxer_ = nullptr;
    }
}

int32_t Muxer::GetInnerTrackId() { return innerTrackId_; }

int32_t Muxer::GetMicTrackId() { return micTrackId_; }
```

AudioEncoder.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef AVSCREENCAPTURESCREENRECORD_AUDIOENCODER_H
#define AVSCREENCAPTURESCREENRECORD_AUDIOENCODER_H
#include "CAVScreenCaptureToStream/SampleInfo.h"
#include <multimedia/player_framework/native_avmuxer.h>
#include <string>

class AudioEncoder {
public:
    OH_AVCodec *encoder_;
    int32_t Create(const std::string &codecMime);
    int32_t Config(SampleInfo &sampleInfo, CodecUserData *codecUserData);
    void Stop();
    void Release();
    void Start();
    int32_t PushInputData(CodecBufferInfo &info);
    int32_t FreeOutputData(uint32_t bufferIndex);

private:
    static void OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData);
    static void OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData);
    static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
    static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
};
#endif
```

AudioEncoder.cpp:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "AudioEncoder.h"
#include "hilog/log.h"
#include <multimedia/player_framework/native_avcodec_audiocodec.h>
#include <mutex>

#undef LOG_TAG
#define LOG_TAG "AudioEncoder"

int32_t AudioEncoder::Create(const std::string &codecMime)
{
    encoder_ = OH_AudioCodec_CreateByMime(codecMime.c_str(), true);
    return 0;
}

/*
 * Configure audio encoder
 */
int32_t AudioEncoder::Config(SampleInfo &sampleInfo, CodecUserData *codecUserData)
{
    OH_AVFormat *format = OH_AVFormat_Create();
    if (format == nullptr) {
        OH_LOG_ERROR(LOG_APP, "AVFormat create failed");
    }

    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, sampleInfo.audioSampleFormat);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, sampleInfo.audioChannelCount);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleInfo.audioSampleRate);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, sampleInfo.audioBitRate);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, sampleInfo.audioChannelLayout);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_MAX_INPUT_SIZE, sampleInfo.audioMaxInputSize);

    int ret = OH_AudioCodec_Configure(encoder_, format);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Config failed, ret: %{public}d", ret);
    }
    OH_AVFormat_Destroy(format);
    format = nullptr;

    // SetCallback for audio encoder
    OH_AudioCodec_RegisterCallback(encoder_,
                                   {AudioEncoder::OnCodecError, AudioEncoder::OnCodecFormatChange,
                                    AudioEncoder::OnNeedInputBuffer, AudioEncoder::OnNewOutputBuffer},
                                   codecUserData);

    // Prepare audio encoder
    ret = OH_AudioCodec_Prepare(encoder_);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Prepare failed, ret: %{public}d", ret);
    }
    return 0;
}

void AudioEncoder::Start()
{
    int ret = OH_AudioCodec_Start(encoder_);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Start failed, ret: %{public}d", ret);
    }
}

int32_t AudioEncoder::PushInputData(CodecBufferInfo &info)
{
    int32_t ret = OH_AVBuffer_SetBufferAttr(reinterpret_cast<OH_AVBuffer *>(info.buffer), &info.attr);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Set av buffer attr failed");
    }
    ret = OH_AudioCodec_PushInputBuffer(encoder_, info.bufferIndex);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Push input data failed");
    }
    return ret;
}

int32_t AudioEncoder::FreeOutputData(uint32_t bufferIndex)
{
    int32_t ret = OH_AudioCodec_FreeOutputBuffer(encoder_, bufferIndex);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Free output data failed");
    }
    return ret;
}

void AudioEncoder::Stop()
{
    int ret = OH_AudioCodec_Flush(encoder_);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Flush failed, ret: %{public}d", ret);
    }
    ret = OH_AudioCodec_Stop(encoder_);
    if (ret != AV_ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "Stop failed, ret: %{public}d", ret);
    }
}

void AudioEncoder::Release()
{
    if (encoder_ != nullptr) {
        OH_AudioCodec_Flush(encoder_);
        OH_AudioCodec_Stop(encoder_);
        OH_AudioCodec_Destroy(encoder_);
        encoder_ = nullptr;
    }
}

void AudioEncoder::OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData)
{
    (void)codec;
    (void)errorCode;
    (void)userData;
}

void AudioEncoder::OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
{
    (void)codec;
    (void)format;
    (void)userData;
}

void AudioEncoder::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
{
    if (userData == nullptr) {
        return;
    }
    CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
    std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
    (void)lock;

    codecUserData->inputBufferInfoQueue.emplace(index, buffer, codec);
    codecUserData->inputCond.notify_all();
}

void AudioEncoder::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
{
    if (userData == nullptr) {
        return;
    }
    CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
    std::unique_lock<std::mutex> lock(codecUserData->outputMutex);
    (void)lock;

    codecUserData->outputBufferInfoQueue.emplace(index, buffer, codec);
    codecUserData->outputCond.notify_all();
}
```

CAVScreenCaptureToStream.h:

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#ifndef AVSCREENCAPTURESCREENRECORD_CAVSCREENCAPTURETOSTREAM_H
#define AVSCREENCAPTURESCREENRECORD_CAVSCREENCAPTURETOSTREAM_H
#include "CAVScreenCaptureToStream/AudioEncoder.h"
#include "CAVScreenCaptureToStream/Muxer.h"
#include "CAVScreenCaptureToStream/SampleInfo.h"
#include <memory>
#include <multimedia/player_framework/native_avscreen_capture_base.h>
#include <thread>

class CAVScreenCaptureToStream {
private:
    static void StopScreenCaptureRecording(struct OH_AVScreenCapture *capture);
    void InitAVScreenCapture();

    static void OnErrorToStream(OH_AVScreenCapture *capture, int32_t errorCode, void *userData);
    static void OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                  OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData);
    static void OnSurfaceStateChange(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode,
                                     void *userData);

    void InitMuxerAndEncoder(int32_t outputFd);
    void StartMuxerAndEncoder();
    void CreateEncoder();
    void Release();

    void AudioEncInputThread();
    void AudioEncOutputThread();

    std::unique_ptr<std::thread> audioEncInputThread_ = nullptr;
    std::unique_ptr<std::thread> audioEncOutputThread_ = nullptr;
    std::unique_ptr<Muxer> muxer_ = nullptr;

    SampleInfo sampleInfo_;
    std::atomic<bool> isStarted_{false};
    CodecUserData *audioEncContext_ = nullptr;

public:
    CAVScreenCaptureToStream(){};
    ~CAVScreenCaptureToStream();

    static CAVScreenCaptureToStream &GetInstance()
    {
        static CAVScreenCaptureToStream avScreenCapture;
        return avScreenCapture;
    }

    void StartScreenCapture(int32_t outputFd);
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
#include "CAVScreenCaptureToStream/Muxer.h"
#include "SampleInfo.h"
#include "hilog/log.h"
#include <multimedia/player_framework/native_avcapability.h>
#include <multimedia/player_framework/native_avcodec_base.h>
#include <multimedia/player_framework/native_avcodec_videoencoder.h>
#include <multimedia/player_framework/native_avscreen_capture.h>
#include <multimedia/player_framework/native_avscreen_capture_errors.h>
#include <multimedia/native_audio_channel_layout.h>
#include <thread>

#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200
#define LOG_TAG "CAVSCREENCAPTURETOSTREAM"

using namespace std;

bool g_isRunning = false;

OH_AVScreenCapture *g_avCapture = nullptr;
std::unique_ptr<AudioEncoder> audioEncoderInner_ = nullptr;
std::unique_ptr<AudioEncoder> audioEncoderMic_ = nullptr;

CAVScreenCaptureToStream::~CAVScreenCaptureToStream() { Release(); }

/*
 * Screen recording Error callback
 */
void CAVScreenCaptureToStream::OnErrorToStream(OH_AVScreenCapture *capture, int32_t errorCode, void *userData)
{
    (void)capture;
    (void)userData;
    OH_LOG_ERROR(LOG_APP, "ScreenCapture OnError errorCode is %{public}d", errorCode);
}

void CAVScreenCaptureToStream::OnBufferAvailable(OH_AVScreenCapture *capture, OH_AVBuffer *buffer,
                                                 OH_AVScreenCaptureBufferType bufferType, int64_t timestamp,
                                                 void *userData)
{
    (void)capture;
    (void)timestamp;
    if (g_isRunning) {
        CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
        std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
        if (bufferType == OH_AVScreenCaptureBufferType::OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_INNER) {
            // 内录音频原始数据，写入数据缓冲区
            OH_AVCodecBufferAttr attr;
            OH_AVBuffer_GetBufferAttr(buffer, &attr);
            uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
            codecUserData->innerCache.WriteCache(addr, attr.size);
            OH_AVBuffer_Destroy(buffer);
        } else if (bufferType == OH_AVScreenCaptureBufferType::OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_MIC) {
            // 外录音频原始数据，写入数据缓冲区
            OH_AVCodecBufferAttr attr;
            OH_AVBuffer_GetBufferAttr(buffer, &attr);
            uint8_t *addr = OH_AVBuffer_GetAddr(buffer);
            codecUserData->micCache.WriteCache(addr, attr.size);
            OH_AVBuffer_Destroy(buffer);
        }
    }
}

/*
 * Screen recording state change callback
 */
void CAVScreenCaptureToStream::OnSurfaceStateChange(struct OH_AVScreenCapture *capture,
                                                    OH_AVScreenCaptureStateCode stateCode, void *userData)
{
    (void)userData;
    switch (stateCode) {
    case OH_SCREEN_CAPTURE_STATE_STOPPED_BY_USER: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OnStateChange OH_SCREEN_CAPTURE_STATE_STOPPED_BY_USER");
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_CANCELED: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OnStateChange OH_SCREEN_CAPTURE_STATE_CANCELED ");
        StopScreenCaptureRecording(capture);
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_STARTED: {
        int ret = OH_AVScreenCapture_SetMaxVideoFrameRate(g_avCapture, 30);
        OH_LOG_INFO(LOG_APP, "OH_AVScreenCapture_SetMaxVideoFrameRate result: %{public}d", ret);
        OH_LOG_INFO(LOG_APP, "ScreenCapture OnStateChange started OH_SCREEN_CAPTURE_STATE_STARTED");
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_STOPPED_BY_CALL: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OH_SCREEN_CAPTURE_STATE_STOPPED_BY_CALL");
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OH_SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER");
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_MIC_UNMUTED_BY_USER: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OH_SCREEN_CAPTURE_STATE_MIC_MUTED_BY_USER");
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OnStateChange OH_SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE");
        break;
    }
    case OH_SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE: {
        OH_LOG_INFO(LOG_APP, "ScreenCapture OH_SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE");
        break;
    }
    default:
        break;
    }
}

/*
 * Configure screen recording parameters
 */
void CAVScreenCaptureToStream::InitAVScreenCapture()
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
    OH_AVScreenCapture_SetStateCallback(g_avCapture, OnSurfaceStateChange, nullptr);

    OH_AVScreenCapture_SetMicrophoneEnabled(g_avCapture, true);
    OH_AVScreenCapture_SetDataCallback(g_avCapture, OnBufferAvailable, audioEncContext_);
    OH_AVScreenCapture_SetCanvasRotation(g_avCapture, true);

    OH_AVScreenCaptureConfig config;
    // 麦克风音频采集参数
    OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_MIC};
    // 内录音频采集参数
    OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
    // 音频输出规格
    OH_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC};
    // 配置音频采集参数
    OH_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};
    // 录屏配置信息
    config = {
        .captureMode = OH_CAPTURE_HOME_SCREEN,
        .dataType = OH_ORIGINAL_STREAM,
        .audioInfo = audioInfo,
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
 * Create audio and video encoder
 */
void CAVScreenCaptureToStream::CreateEncoder()
{
    audioEncContext_ = new CodecUserData;
    audioEncoderInner_->Create(sampleInfo_.audioCodecMime);
    audioEncoderInner_->Config(sampleInfo_, audioEncContext_);
    audioEncoderMic_->Create(sampleInfo_.audioCodecMime);
    audioEncoderMic_->Config(sampleInfo_, audioEncContext_);
}

/*
 * Initialize configuration information
 */
void CAVScreenCaptureToStream::InitMuxerAndEncoder(int32_t outputFd)
{
    sampleInfo_.outputFd = outputFd;

    // 音频编码参数
    sampleInfo_.audioCodecMime = OH_AVCODEC_MIMETYPE_AUDIO_AAC;
    sampleInfo_.audioSampleFormat = OH_BitsPerSample::SAMPLE_S16LE;
    sampleInfo_.audioSampleRate = 48000;
    sampleInfo_.audioChannelCount = 2;
    sampleInfo_.audioBitRate = 96000;
    sampleInfo_.audioChannelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
    sampleInfo_.audioMaxInputSize = sampleInfo_.audioSampleRate * 0.02 * sampleInfo_.audioChannelCount * sizeof(short);
    // 音频编码器
    audioEncoderInner_ = std::make_unique<AudioEncoder>(); // 内录音频编码器
    audioEncoderMic_ = std::make_unique<AudioEncoder>();   // 外录音频编码器
    // 媒体文件封装器
    muxer_ = std::make_unique<Muxer>();
    muxer_->Create(sampleInfo_.outputFd);
    muxer_->Config(sampleInfo_);

    CreateEncoder();
}

void CAVScreenCaptureToStream::StartMuxerAndEncoder()
{
    // Start muxer
    muxer_->Start();

    isStarted_ = true;

    if (audioEncContext_) {
        // Start audio Encoder
        audioEncoderInner_->Start();
        audioEncoderMic_->Start();
        isStarted_ = true;
        // Start the audio input and output threads
        audioEncInputThread_ = std::make_unique<std::thread>(&CAVScreenCaptureToStream::AudioEncInputThread, this);
        audioEncOutputThread_ = std::make_unique<std::thread>(&CAVScreenCaptureToStream::AudioEncOutputThread, this);
        if (audioEncInputThread_ == nullptr || audioEncOutputThread_ == nullptr) {
            Release();
            return;
        }

        // Empty the playback cache queue
        if (audioEncContext_ != nullptr) {
            audioEncContext_->innerCache.ClearCache();
            audioEncContext_->micCache.ClearCache();
        }
    }
}

void CAVScreenCaptureToStream::StartScreenCapture(int32_t outputFd)
{
    if (g_isRunning) {
        OH_LOG_ERROR(LOG_APP, "Screen Capture is running");
        return;
    }

    InitMuxerAndEncoder(outputFd);

    InitAVScreenCapture();

    g_isRunning = true;

    StartMuxerAndEncoder();

    int result = OH_AVScreenCapture_StartScreenCapture(g_avCapture);
    OH_LOG_INFO(LOG_APP, "OH_VideoEncoder_Start Started %{public}d", result);
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
        Release();
    }
}

/*
 * Release
 */
void CAVScreenCaptureToStream::Release()
{
    isStarted_ = false;
    if (audioEncInputThread_ && audioEncInputThread_->joinable()) {
        audioEncContext_->inputCond.notify_all();
        audioEncInputThread_->join();
        audioEncInputThread_.reset();
    }
    if (audioEncOutputThread_ && audioEncOutputThread_->joinable()) {
        audioEncContext_->outputCond.notify_all();
        audioEncOutputThread_->join();
        audioEncOutputThread_.reset();
    }
    if (muxer_ != nullptr) {
        muxer_->Release();
        muxer_.reset();
        OH_LOG_INFO(LOG_APP, "Muxer release successful");
    }
    if (audioEncoderMic_ != nullptr) {
        audioEncoderMic_->Stop();
        audioEncoderMic_->Release();
        audioEncoderMic_.reset();
        OH_LOG_INFO(LOG_APP, "Audio encoder release successful");
    }
    if (audioEncoderInner_ != nullptr) {
        audioEncoderInner_->Stop();
        audioEncoderInner_->Release();
        audioEncoderInner_.reset();
        OH_LOG_INFO(LOG_APP, "Audio encoder release successful");
    }
    if (audioEncContext_ != nullptr) {
        delete audioEncContext_;
        audioEncContext_ = nullptr;
    }
    OH_LOG_INFO(LOG_APP, "Release successful");
}

void CAVScreenCaptureToStream::AudioEncInputThread()
{
    while (g_isRunning) {
        if (!isStarted_) {
            OH_LOG_INFO(LOG_APP, "Audio encoder input thread out");
            break;
        }
        std::unique_lock<std::mutex> lock(audioEncContext_->inputMutex);
        audioEncContext_->inputCond.wait_for(lock, 1s);
        if (!isStarted_) {
            OH_LOG_INFO(LOG_APP, "Audio encoder input thread out");
            break;
        }
        if (audioEncContext_->inputBufferInfoQueue.empty()) {
            OH_LOG_INFO(LOG_APP, "Audio Buffer queue is empty");
            continue;
        }
        CodecBufferInfo bufferInfo = audioEncContext_->inputBufferInfoQueue.front();
        if (bufferInfo.codec == audioEncoderInner_->encoder_) {
            // 从数据缓冲区中读取内录原始音频数据，写入内录音频编码器
            if (audioEncContext_->innerCache.remainLen < sampleInfo_.audioMaxInputSize) {
                continue;
            }
            audioEncContext_->inputBufferInfoQueue.pop();
            uint8_t *inputBufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
            audioEncContext_->innerCache.ReadCache(inputBufferAddr, sampleInfo_.audioMaxInputSize);
            lock.unlock();
            bufferInfo.attr.size = sampleInfo_.audioMaxInputSize;
            bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
            int32_t ret = audioEncoderInner_->PushInputData(bufferInfo);
            if (ret) {
                OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
                break;
            }
        } else {
            // 从数据缓冲区中读取外录原始音频数据，写入外录音频编码器
            if (audioEncContext_->micCache.remainLen < sampleInfo_.audioMaxInputSize) {
                continue;
            }
            audioEncContext_->inputBufferInfoQueue.pop();
            uint8_t *inputBufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
            audioEncContext_->micCache.ReadCache(inputBufferAddr, sampleInfo_.audioMaxInputSize);
            lock.unlock();
            bufferInfo.attr.size = sampleInfo_.audioMaxInputSize;
            bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
            int32_t ret = audioEncoderMic_->PushInputData(bufferInfo);
            if (ret) {
                OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
                break;
            }
        }
    }
}

void CAVScreenCaptureToStream::AudioEncOutputThread()
{
    while (g_isRunning) {
        if (!isStarted_) {
            OH_LOG_INFO(LOG_APP, "Audio encoder output thread out");
            break;
        }
        std::unique_lock<std::mutex> lock(audioEncContext_->outputMutex);
        audioEncContext_->outputCond.wait_for(lock, 1s);

        if (!isStarted_) {
            OH_LOG_INFO(LOG_APP, "Audio encoder output thread out");
            break;
        }

        if (audioEncContext_->outputBufferInfoQueue.empty()) {
            OH_LOG_ERROR(LOG_APP, "Buffer queue is empty");
            continue;
        }

        CodecBufferInfo bufferInfo = audioEncContext_->outputBufferInfoQueue.front();
        audioEncContext_->outputBufferInfoQueue.pop();
        lock.unlock();
        if (bufferInfo.codec == audioEncoderInner_->encoder_) {
            // 内录编码音频写入内录音频轨道
            muxer_->WriteSample(muxer_->GetInnerTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                                bufferInfo.attr);
            int32_t ret = audioEncoderInner_->FreeOutputData(bufferInfo.bufferIndex);
            if (ret) {
                OH_LOG_ERROR(LOG_APP, "Encoder output thread out");
                break;
            }
        } else {
            // 外录编码音频流写入外录音频轨道
            muxer_->WriteSample(muxer_->GetMicTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
                                bufferInfo.attr);
            int32_t ret = audioEncoderMic_->FreeOutputData(bufferInfo.bufferIndex);
            if (ret) {
                OH_LOG_ERROR(LOG_APP, "Encoder output thread out");
                break;
            }
        }
    }
}
```
