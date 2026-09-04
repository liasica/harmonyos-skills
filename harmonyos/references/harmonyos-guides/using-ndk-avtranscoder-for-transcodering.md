---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ndk-avtranscoder-for-transcodering
title: 使用AVTranscoder实现视频转码(C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 视频转码 > 使用AVTranscoder实现视频转码(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7585007da8e1306712cfa72daf299d16a1700109188290b013d13a75f9772f0
---

从API version 20开始支持使用NDK接口（C/C++）实现视频转码。

使用[AVTranscoder](media-kit-intro.md#avtranscoder)可以实现视频转码功能，从API 12开始，转码功能可在手机、平板、2in1设备上作为系统提供的基础能力使用。可以通过调用[canIUse](../harmonyos-references/syscap__ndk_8h.md#caniuse)接口来判断当前设备是否支持AVTranscoder。当canIUse("SystemCapability.Multimedia.Media.AVTranscoder")返回值为true时，表示可以使用转码能力。

本开发指导将以“开始转码-暂停转码-恢复转码-完成转码”的一次完整流程为示例，向开发者讲解AVTranscoder视频转码相关功能。

**图1** 转码状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/9an6yU88SJKtgqOAJRUR8A/zh-cn_image_0000002742003785.png)

状态的详细说明请参考[OH\_AVTranscoder\_State](../harmonyos-references/capi-avtranscoder-base-h.md#oh_avtranscoder_state)。

## 开发步骤及注意事项

在CMake脚本中链接动态库。

```c
target_link_libraries(entry PUBLIC libavtranscoder.so libace_napi.z.so)
```

开发者使用系统日志能力时，需引入如下头文件：

```
#include <hilog/log.h>
```

并需要在CMake脚本中链接如下动态库：

```c
target_link_libraries(sample PUBLIC libhilog_ndk.z.so)
```

开发者通过引入avtranscoder.h和avtranscoder\_base.h头文件，使用转码相关API。

详细的API说明请参考[AVTranscoder](../harmonyos-references/capi-avtranscoder.md)。

1. 创建转码实例：调用OH\_AVTranscoder\_Create()。

   ```
   OH_AVTranscoder *transcoder = OH_AVTranscoder_Create();
   ```
2. 设置回调事件函数：使用OH\_AVTranscoder\_SetStateCallback()、OH\_AVTranscoder\_SetErrorCallback()和OH\_AVTranscoder\_SetProgressUpdateCallback()接口设置回调转码状态、转码错误事件和转码进度更新回调函数，搭配全流程场景使用。支持的回调事件包括：

   | 事件类型 | 说明 |
   | --- | --- |
   | OH\_AVTranscoder\_OnStateChange | 可选事件，回调转码过程中状态。 |
   | OH\_AVTranscoder\_OnError | 可选事件，回调转码错误事件。 |
   | OH\_AVTranscoder\_OnProgressUpdate | 可选事件，回调转码进度更新事件。 |

   应用使用OH\_AVTranscoder\_SetStateCallback()、OH\_AVTranscoder\_SetErrorCallback()和OH\_AVTranscoder\_SetProgressUpdateCallback()接口设置回调转码状态、转码错误事件和转码进度更新回调函数，可以获取更多信息，还可以通过设置userData自定义数据。

   ```
   typedef struct NdkAVTransCoderUser {
      using StateChangeFunc = std::function<void()>;
      NdkAVTransCoderUser();
      NdkAVTransCoderUser(const NdkAVTransCoderUser &other) = delete;
      NdkAVTransCoderUser &operator=(const NdkAVTransCoderUser &other) = delete;
      ~NdkAVTransCoderUser();

      void OnStateChangeCb(OH_AVTranscoder *transcoder, OH_AVTranscoder_State state);
      void OnErrorCb(OH_AVTranscoder *transcoder, int32_t errorCode, const char  *errorMsg);
      void OnProgressUpdateCb(OH_AVTranscoder *transcoder, int progress);
      std::map<uint32_t, StateChangeFunc> stateChangeFuncs_;

      OH_AVTranscoder *transcoder = nullptr;
      int32_t errorCode = AV_ERR_OK;
      OH_AVTranscoder_State transCoderState = AVTRANSCODER_PREPARED;
      int avTranscoderProgress = 0;
      int inStartStateCount = 0;
   } NdkAVTransCoderUser;

   void NdkAVTransCoderUser::OnProgressUpdateCb(OH_AVTranscoder *transcoder, int  progress)
   {
      LOG("NdkAVTransCoderUser OnProgressUpdateCb progress: %{public}d", progress);
      this->avTranscoderProgress = progress;
   }

   void NdkAVTransCoderUser::OnErrorCb(OH_AVTranscoder *transcoder, int32_t  errorCode, const char *errorMsg)
   {
      LOG("NdkAVTransCoderUser OnErrorCb errorCode: %{public}d ,errorMsg: %{public} s", errorCode,
         errorMsg == nullptr ? "unknown" : errorMsg);
      this->errorCode = errorCode;
   }

   void NdkAVTransCoderUser::OnStateChangeCb(OH_AVTranscoder *transcoder,  OH_AVTranscoder_State state)
   {
      this->transCoderState = state;
      if (transcoder == nullptr) {
         return;
      }
      int32_t ret = -1;
      switch (state) {
         case AVTRANSCODER_PREPARED: {
               this->transCoderState = AVTRANSCODER_PREPARED;
               if (this->stateChangeFuncs_.count(AVTRANSCODER_PREPARED) > 0) {
                  this->stateChangeFuncs_[AVTRANSCODER_PREPARED]();
               }
               break;
         }
         case AVTRANSCODER_STARTED: {
               this->transCoderState = AVTRANSCODER_STARTED;
               if (this->stateChangeFuncs_.count(AVTRANSCODER_STARTED) > 0) {
                  this->stateChangeFuncs_[AVTRANSCODER_STARTED]();
               }
               break;
         }
         case AVTRANSCODER_PAUSED: {
               this->transCoderState = AVTRANSCODER_PAUSED;
               if (this->stateChangeFuncs_.count(AVTRANSCODER_PAUSED) > 0) {
                  this->stateChangeFuncs_[AVTRANSCODER_PAUSED]();
               }
               break;
         }
         case AVTRANSCODER_CANCELLED: {
               this->transCoderState = AVTRANSCODER_CANCELLED;
               if (this->stateChangeFuncs_.count(AVTRANSCODER_CANCELLED) > 0) {
                  this->stateChangeFuncs_[AVTRANSCODER_CANCELLED]();
               }
               break;
         }
         case AVTRANSCODER_COMPLETED: {
               this->transCoderState = AVTRANSCODER_COMPLETED;
               if (this->stateChangeFuncs_.count(AVTRANSCODER_COMPLETED) > 0) {
                  this->stateChangeFuncs_[AVTRANSCODER_COMPLETED]();
               }
               break;
         }
         default:
               break;
      }
   }

   static void AvTranscoderStateChangeCbImpl(OH_AVTranscoder *transcoder,  OH_AVTranscoder_State state, void *userData)
   {
      LOG("AvTranscoderStateChangeCbImpl state: %{public}d", state);
      NdkAVTransCoderUser *ndkAVTransCoderUser =  reinterpret_cast<NdkAVTransCoderUser *>(userData);
      if (ndkAVTransCoderUser == nullptr || transcoder == nullptr) {
         LOGE("AvTranscoderStateChangeCbImpl ndkAVTransCoderUser or transcoder is  nullptr");
         return;
      }
      ndkAVTransCoderUser->OnStateChangeCb(transcoder, state);
   }

   static void AvTranscoderErrorCbImpl(OH_AVTranscoder *transcoder, int32_t  errorCode, const char *errorMsg,
                                       void *userData)
   {
      LOG("AvTranscoderErrorCbImpl errorCode: %{public}d, errorMsg: %{public}s",  errorCode,
         errorMsg == nullptr ? "unknown" : errorMsg);
      NdkAVTransCoderUser *ndkAVTransCoderUser =  reinterpret_cast<NdkAVTransCoderUser *>(userData);
      if (ndkAVTransCoderUser == nullptr || transcoder == nullptr) {
         LOGE("AvTranscoderErrorCbImpl ndkAVTransCoderUser or transcoder is  nullptr");
         return;
      }
      ndkAVTransCoderUser->OnErrorCb(transcoder, errorCode, errorMsg);
   }

   static void AvTranscoderProgressUpdateCbImpl(OH_AVTranscoder *transcoder, int  progress, void *userData)
   {
      LOG("AvTranscoderProgressUpdateCbImpl progress: %{public}d", progress);
      NdkAVTransCoderUser *ndkAVTransCoderUser =  reinterpret_cast<NdkAVTransCoderUser *>(userData);
      if (ndkAVTransCoderUser == nullptr || transcoder == nullptr) {
         LOGE("AvTranscoderProgressUpdateCbImpl ndkAVTransCoderUser or transcoder is  nullptr");
         return;
      }
      ndkAVTransCoderUser->OnProgressUpdateCb(transcoder, progress);
   }
   static napi_value OHAvTranscoderNdkPlay(napi_env env, napi_callback_info info)
   {
      OH_AVTranscoder_SetStateCallback(transcoder, AvTranscoderStateChangeCbImpl,  transcoderUser); // 设置状态回调
      OH_AVTranscoder_SetErrorCallback(transcoder, AvTranscoderErrorCbImpl,  transcoderUser); // 设置错误码回调
      OH_AVTranscoder_SetProgressUpdateCallback(transcoder,  AvTranscoderProgressUpdateCbImpl, transcoderUser); // 设置进度值回调
   }
   ```
3. 使用OH\_AVTranscoderConfig\_Create()创建转码配置实例。

   ```
   OH_AVTranscoder_Config *config = OH_AVTranscoderConfig_Create();
   ```
4. 设置转码源视频的文件描述符：调用OH\_AVTranscoderConfig\_SetSrcFD()设置源视频文件信息。

   ```
   OH_AVTranscoderConfig_SetSrcFD(config, srcFd, srcOffset, length); // 设置转码源视频FD
   ```
5. 设置转码输出视频的文件描述符：调用OH\_AVTranscoderConfig\_SetDstFD()设置目标视频文件描述符。

   ```
   OH_AVTranscoderConfig_SetDstFD(config, dstFd); // 设置转码的目标文件描述符dstFd。
   ```
6. （可选）设置转码输出视频的编码格式：调用OH\_AVTranscoderConfig\_SetDstVideoType()设置输出视频的编码格式。

   ```
   OH_AVTranscoderConfig_SetDstVideoType(config, "video/avc"); // 视频编码格式，可选。
   ```
7. （可选）设置转码输出音频的编码格式：调用OH\_AVTranscoderConfig\_SetDstAudioType()设置输出音频的编码格式。

   ```
   OH_AVTranscoderConfig_SetDstAudioType(config, "audio/mp4a-latm"); // 音频编码格式，可选。
   ```
8. 设置转码输出视频文件的封装格式：调用OH\_AVTranscoderConfig\_SetDstFileType()设置输出视频文件的封装格式。

   ```
   OH_AVTranscoderConfig_SetDstFileType(config, AV_OUTPUT_FORMAT_MPEG_4); // 封装格式。
   ```
9. （可选）设置转码输出音频的码率：调用OH\_AVTranscoderConfig\_SetDstAudioBitrate()设置输出音频的码率。

   ```
   const std::int32_t AUDIO_BITRATE = 200000;
   OH_AVTranscoderConfig_SetDstAudioBitrate(config, AUDIO_BITRATE); // 参考avcodec音频编码器码率设置，具体根据实际需要设置。
   ```
10. （可选）设置转码输出视频的码率：调用OH\_AVTranscoderConfig\_SetDstVideoBitrate()设置输出视频的码率。

    ```
    const std::int32_t VIDEO_BITRATE = 3000000;
    OH_AVTranscoderConfig_SetDstVideoBitrate(config, VIDEO_BITRATE); // 视频比特率，可选。
    ```
11. （可选）设置转码输出视频的分辨率：调用OH\_AVTranscoderConfig\_SetDstVideoResolution()设置输出视频的分辨率。

    ```
    const std::int32_t VIDEO_WIDTH = 1280;
    const std::int32_t VIDEO_HEIGHT = 720;
    OH_AVTranscoderConfig_SetDstVideoResolution(config, VIDEO_WIDTH, VIDEO_HEIGHT);
    ```
12. 准备转码：调用OH\_AVTranscoder\_Prepare()成功之后进入AVTRANSCODER\_PREPARED状态。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoder_Prepare(transcoder, config); // 准备转码
    ```
13. 开始转码：调用OH\_AVTranscoder\_Start()成功之后进入AVTRANSCODER\_STARTED状态。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoder_Start(transcoder); // 开始转码
    ```
14. （可选）暂停转码：调用OH\_AVTranscoder\_Pause()成功之后进入AVTRANSCODER\_PAUSED状态。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoder_Pause(transcoder); // 暂停转码
    ```
15. （可选）恢复转码：调用OH\_AVTranscoder\_Resume()成功之后重新进入AVTRANSCODER\_STARTED状态。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoder_Resume(transcoder); // 恢复转码
    ```
16. （可选）取消转码：调用OH\_AVTranscoder\_Cancel()成功之后进入AVTRANSCODER\_CANCELLED状态。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoder_Cancel(transcoder); // 取消转码
    ```
17. 释放转码配置参数：调用OH\_AVTranscoderConfig\_Release()销毁实例，释放资源。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoderConfig_Release(config); // 释放转码配置实例
    ```
18. 释放转码资源：调用OH\_AVTranscoder\_Release()销毁实例，释放资源。

    ```
    OH_AVErrCode errCode = AV_ERR_OK;
    errCode = OH_AVTranscoder_Release(transcoder); // 释放转码实例
    ```

## 运行完整示例

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVTranscoder/AVTranscoderNDK)，并将示例工程的以下资源复制到对应目录。

   ```txt
   AVTranscoderNDK
   entry/src/main/ets/
   └── pages
       └── Index.ets（转码界面）
   entry/src/main/
   ├── cpp
   │   ├── types
   │   │   └── libentry
   │   │       └── Index.d.ts（NDK函数对应的js映射）
   │   ├── CMakeLists.txt（CMake脚本）
   │   └── napi_init.cpp（NDK函数）
   └── resources
       ├── base
       │   └── element
       │       ├── color.json
       │       ├── float.json
       │       └── string.json
       └── rawfile
           └── src.mp4（视频资源）
   ```
2. 编译新建工程并运行。
