---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-avscreencapture
title: 基于AVScreenCapture录制音频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频录制系列开发实践 > 基于AVScreenCapture录制音频
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:bb7201954bdac54d36294b40dff7b36f0654ef3e26b7c1e21f8a1f1431f3be57
---

## 概述

AVScreenCapture具备采集设备内部音频和麦克风音频的能力，可以录制设备内播放的音频或者麦克风的音频。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了如何基于AVScreenCapture录制音频，指导开发者实现基础录制。

基于AVScreenCapture录制音频实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/b4MBG8ctS5yqxA5ij9QuSg/zh-cn_image_0000002524061076.gif "点击放大")

本文的主要内容如下：

[基础录制](bpta-audio-record-base-on-avscreencapture.md#section20569101215108)：介绍在C/C++侧基于AVScreenCapture录制音频，包括开始录制、结束录制。

## 基础录制

### 实现原理

开发者可以调用C/C++侧屏幕录制[AVScreenCapture](../harmonyos-guides/media-kit-intro.md#avscreencapture)模块的接口，完成屏幕录制，采集设备内部和麦克风等音视频源数据。通过AVScreenCapture可以实现单独录制音频文件的功能，在录制音频文件时，支持录制m4a的音频格式，关键流程包括开始录制、停止录制、释放资源等。

### 开发步骤

1.在CMake脚本中链接动态库libnative\_avscreen\_capture.so、libnative\_media\_core.so等。

```screen
target_link_libraries(entry PUBLIC libace_napi.z.so libace_ndk.z.so libjsvm.so libhilog_ndk.z.so libnative_avscreen_capture.so libuv.so libnative_media_core.so)
```

2.配置音频录制相关参数。

* 设置视频录制相关参数OH\_VideoInfo，包括OH\_VideoCaptureInfo和OH\_VideoEncInfo。

**说明** 

AVScreenCapture用于实现屏幕录制。当OH\_VideoCaptureInfo的videoFrameWidth和videoFrameHeight设置为0时，AVScreenCapture会忽略视频相关参数，不录制屏幕数据。

* 设置音频相关参数OH\_AudioInfo，包括音频采集信息OH\_AudioCaptureInfo、音频编码信息OH\_AudioEncInfo。

```cpp
// Configuration parameters
void AVScreenCapture::SetConfig(OH_AVScreenCaptureConfig &config) {
    OH_RecorderInfo recorderInfo;
    recorderInfo.fileFormat = OH_ContainerFormatType::CFT_MPEG_4A;
    // Config VideoCaptureInfo
    OH_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = 0, .videoFrameHeight = 0, .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA};
    // Config VideoEncInfo
    OH_VideoEncInfo videoEncInfo = {
        .videoCodec = OH_VideoCodecFormat::OH_H264, .videoBitrate = 2000000, .videoFrameRate = 30};
    // Config VideoInfo
    OH_VideoInfo videoInfo = {.videoCapInfo = videoCapInfo, .videoEncInfo = videoEncInfo};

    // Config Mic Capture Info
    OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_MIC};
    // Config inner Capture Info
    OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
    // Config Audio Encoder Info
    OH_AudioEncInfo audioEncInfo = {.audioBitrate = 96000, .audioCodecformat = OH_AudioCodecFormat::OH_AAC_LC};
    // Config Audio Info
    OH_AudioInfo audioInfo = {.micCapInfo = micCapInfo, .innerCapInfo = innerCapInfo, .audioEncInfo = audioEncInfo};

    config.captureMode = OH_CAPTURE_HOME_SCREEN; // screen capture mode
    config.dataType = OH_CAPTURE_FILE; // data type
    config.audioInfo = audioInfo; // audio info
    config.videoInfo = videoInfo; // video info
    config.recorderInfo = recorderInfo; // recorder info
}
```

3.启动音频录制。

* 在调用[OH\_AVScreenCapture\_Create()](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_create)创建录制对象后，通过环境配置OH\_AVScreenCaptureConfig初始化该对象。
* 然后，调用OH\_AVScreenCapture\_StartScreenRecording()启动音频录制。

```cpp
OH_AVSCREEN_CAPTURE_ErrCode AVScreenCapture::StartScreenCaptureToFile(int32_t outputFd) {
    if (avScreenCapture != nullptr) {
        StopScreenCaptureRecording(avScreenCapture);
        OH_AVScreenCapture_Release(avScreenCapture);
    }
    avScreenCapture = OH_AVScreenCapture_Create();
    if (avScreenCapture == nullptr) {
        OH_LOG_ERROR(LOG_APP, "AVScreenCapture create screen capture failed");
    }
    OH_AVScreenCaptureConfig config_;
    SetConfig(config_);
    std::string fileUrl = "fd://" + std::to_string(outputFd);
    config_.recorderInfo.url = const_cast<char *>(fileUrl.c_str());

    OH_AVScreenCapture_SetMicrophoneEnabled(avScreenCapture, true);
    OH_AVScreenCapture_SetErrorCallback(avScreenCapture, OnErrorSaveFile, nullptr);
    OH_AVScreenCapture_SetStateCallback(avScreenCapture, OnStateChangeSaveFile, nullptr);

    OH_AVSCREEN_CAPTURE_ErrCode result = OH_AVScreenCapture_Init(avScreenCapture, config_);

    if (result != AV_SCREEN_CAPTURE_ERR_OK) {
        OH_LOG_INFO(LOG_APP, "AVScreenCapture ScreenCapture OH_AVScreenCapture_Init failed %{public}d", result);
    }
    OH_LOG_INFO(LOG_APP, "AVScreenCapture ScreenCapture OH_AVScreenCapture_Init succ %{public}d", result);

    result = OH_AVScreenCapture_StartScreenRecording(avScreenCapture);
    if (result != AV_SCREEN_CAPTURE_ERR_OK) {
        OH_LOG_INFO(LOG_APP, "AVScreenCapture ScreenCapture Started failed %{public}d", result);
        OH_AVScreenCapture_Release(avScreenCapture);
    }
    OH_LOG_INFO(LOG_APP, "AVScreenCapture ScreenCapture Started succ %{public}d", result);
    isRunning = true;
    return result;
}
```

4.停止音频录制。

```cpp
OH_AVSCREEN_CAPTURE_ErrCode AVScreenCapture::StopScreenCaptureToFile() {
    OH_AVSCREEN_CAPTURE_ErrCode result = AV_SCREEN_CAPTURE_ERR_OPERATE_NOT_PERMIT;

    if (isRunning && avScreenCapture != nullptr) {
        OH_LOG_INFO(LOG_APP, "AVScreenCapture ScreenCapture File Stop");
        result = OH_AVScreenCapture_StopScreenRecording(avScreenCapture);
        if (result != AV_SCREEN_CAPTURE_ERR_BASE) {
            OH_LOG_ERROR(LOG_APP,
                         "AVScreenCapture StopScreenCapture OH_AVScreenCapture_StopScreenRecording Result: %{public}d",
                         result);
        } else {
            OH_LOG_INFO(LOG_APP, "AVScreenCapture StopScreenCapture OH_AVScreenCapture_StopScreenRecording");
        }
        result = OH_AVScreenCapture_Release(avScreenCapture);
        if (result != AV_SCREEN_CAPTURE_ERR_BASE) {
            OH_LOG_ERROR(LOG_APP, "AVScreenCapture StopScreenCapture OH_AVScreenCapture_Release: %{public}d", result);
        } else {
            OH_LOG_INFO(LOG_APP, "AVScreenCapture OH_AVScreenCapture_Release success");
        }
        isRunning = false;
        avScreenCapture = nullptr;
    }
    return result;
}
```

5.释放音频录制资源。

```cpp
void AVScreenCapture::ReleaseAVScreenCapture(struct OH_AVScreenCapture *capture) {
    StopScreenCaptureRecording(capture);
    if (capture != nullptr) {
        OH_LOG_INFO(LOG_APP, "AVScreenCapture ScreenCapture ReleaseSCInstanceWorker S");
        OH_AVScreenCapture_Release(capture);
        isRunning = false;
        avScreenCapture = nullptr;
    }
}
```

## 示例代码

* [基于AVScreenCapture录制音频（C++）](https://gitcode.com/HarmonyOS_Samples/avscreen-capture-record-system-audio-arkts)
