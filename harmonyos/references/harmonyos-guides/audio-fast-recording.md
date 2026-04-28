---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-fast-recording
title: 低时延音频录制(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 低时延音频录制(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a471e83ab7b0789998640c6bbe7b85e09b469e9a380f1dc29e0f7b61bb68497f
---

从API version 10开始支持低时延音频录制。

低时延音频录制是一种通过软硬芯协同设计实现的音频渲染方案。其核心机制是通过减少buffer大小、优化读写数据架构，使该模式下音频录制具有更低的时延。

## 使用前提

* 支持低时延模式的音频输入设备。
* 可通过[OH\_AudioCapturer\_GetFastStatus()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_getfaststatus)验证当前设备是否支持低时延模式。

## 开发指导

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioCapturerSampleC)。

### 简介

为使用低时延模式，开发者需要参考[推荐使用OHAudio开发音频录制功能(C/C++)](using-ohaudio-for-recording.md)进行音频开发。

当前OHAudio支持两种模式：普通模式（AUDIOSTREAM\_LATENCY\_MODE\_NORMAL）和低时延模式（AUDIOSTREAM\_LATENCY\_MODE\_FAST）。

### 设置低时延模式

开发者通过调用[OH\_AudioStreamBuilder\_SetLatencyMode()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setlatencymode)，设置[OH\_AudioStream\_LatencyMode](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_latencymode)来决定音频流使用的模式。

设置低时延模式开发示例：

```
1. OH_AudioStream_LatencyMode latencyMode = AUDIOSTREAM_LATENCY_MODE_FAST;
2. OH_AudioStreamBuilder_SetLatencyMode(builder, latencyMode);
```

针对OHAudio开发音频录制，有以下相关实例可供参考：

* [OHAudio录制和播放](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/OHAudio)。

## 注意事项

### 低时延模式限制

在以下场景中，即使设置了低时延模式，系统仍会使用普通模式。

* 当前设备不支持低时延模式。
* 当前流格式不支持低时延模式。
* 系统低时延资源已被全部占用。
* 当前系统中存在更高优先级流（如：VOIP通话）。

从API version 20开始，支持低时延相关查询接口。

* 开发者通过调用[OH\_AudioCapturer\_GetFastStatus()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_getfaststatus)来获取音频录制流是否正在低时延状态下工作。
* 在部分特殊场景（如：存在更高优先级流、当前连接设备不支持等）下，开发者可以通过调用[OH\_AudioCapturer\_OnFastStatusChange()](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_onfaststatuschange)来获取低时延状态改变事件。

### 使用低时延流的场景

* k歌、直播等对时延要求较高的场景，建议使用低时延模式。
* 普通录音、录像、录屏等没有实时要求的场景，不建议使用低时延模式。

### 确保数据及时读入

低时延模式下，应用读取数据的频次比普通录制模式高，如果获取数据不及时可能导致杂音等问题。开发者应避免在数据回调线程中做耗时操作，确保数据回调线程可以及时返回。

### 数据回调线程

音频录制的音频数据需要通过回调接口读入。开发者要实现回调接口，使用[OH\_AudioStreamBuilder\_SetCapturerReadDataCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerreaddatacallback)设置回调函数，在设置音频回调函数时，回调函数[OH\_AudioCapturer\_OnReadDataCallback](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_onreaddatacallback)（从API version 12开始支持）用于读取音频数据。

开发音频录制功能的示例代码请参考：[推荐使用OHAudio开发音频录制功能(C/C++)](using-ohaudio-for-recording.md)。

设置数据回调函数示例：

```
1. int32_t MyOnReadData_Legacy(
2. OH_AudioCapturer* capturer,
3. void* userData,
4. void* buffer,
5. int32_t length)
6. {
7. // 从buffer中取出length长度的录音数据。
8. return 0;
9. }
10. // ...
11. // 配置读入音频数据回调函数。
12. OH_AudioCapturer_OnReadDataCallback readDataCb = MyOnReadData_NewAPI;
13. OH_AudioStreamBuilder_SetCapturerReadDataCallback(builder, readDataCb, nullptr);
```

* 为避免音频卡顿，禁止在回调方法OH\_AudioCapturer\_OnReadData中执行耗时操作。
* 为保证OH\_AudioCapturer\_OnReadData与流状态控制逻辑独立正常运行，禁止在OH\_AudioCapturer\_OnReadData回调方法中调用音频流控制接口。

  | 音频流控制接口 | 说明 |
  | --- | --- |
  | OH\_AudioStream\_Result OH\_AudioCapturer\_Start(OH\_AudioCapturer\* capturer) | 开始录制。 |
  | OH\_AudioStream\_Result OH\_AudioCapturer\_Pause(OH\_AudioCapturer\* capturer) | 暂停录制。 |
  | OH\_AudioStream\_Result OH\_AudioCapturer\_Stop(OH\_AudioCapturer\* capturer) | 停止录制。 |
  | OH\_AudioStream\_Result OH\_AudioCapturer\_Flush(OH\_AudioCapturer\* capturer) | 释放缓存数据。 |
  | OH\_AudioStream\_Result OH\_AudioCapturer\_Release(OH\_AudioCapturer\* capturer) | 释放录制实例。 |

  注意

  音频流控制接口执行会有耗时（例如OH\_AudioCapturer\_Stop接口单次执行普遍超过50ms），应避免在主线程中直接调用，以免造成界面显示卡顿。
