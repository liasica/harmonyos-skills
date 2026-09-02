---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-fast-playback
title: 低时延音频播放(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 低时延音频播放(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:be0638393da76857c1feb4891a154552fb9a3ed8c3c41699a8ee36bea9696384
---

从API version 10开始支持低时延音频播放。

低时延音频播放是一种通过软硬芯协同设计实现的音频渲染方案。其核心机制是通过减少buffer大小、优化读写数据架构，使该模式下音频播放具有更低的时延。

## 使用前提

* 支持低时延模式的音频输出设备。
* 可通过[OH\_AudioRenderer\_GetFastStatus()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_getfaststatus)验证当前设备是否支持低时延模式。

## 开发指导

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRendererSampleC)。

### 简介

为使用低时延模式，开发者需要参考[推荐使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)进行音频开发。

当前OHAudio支持两种模式：普通模式（AUDIOSTREAM\_LATENCY\_MODE\_NORMAL）和低时延模式（AUDIOSTREAM\_LATENCY\_MODE\_FAST）。

### 设置低时延模式

开发者通过调用[OH\_AudioStreamBuilder\_SetLatencyMode()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setlatencymode)，设置[OH\_AudioStream\_LatencyMode](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_latencymode)来决定音频流使用的模式。

设置低时延模式开发示例：

```
OH_AudioStream_LatencyMode latencyMode = AUDIOSTREAM_LATENCY_MODE_FAST;
OH_AudioStreamBuilder_SetLatencyMode(builder, latencyMode);
```

针对OHAudio开发音频播放，有以下相关实例可供参考：

* [OHAudio录制和播放](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/OHAudio)。

## 注意事项

### 低时延模式限制

在以下场景中，即使设置了低时延模式，系统仍会使用普通模式。

* 当前设备不支持低时延模式。
* 当前流格式不支持低时延模式。
* 系统低时延资源已被全部占用。
* 当前系统中存在更高优先级流（如：蜂窝通话）。

从API version 20开始，支持低时延相关查询接口。

* 可通过[OH\_AudioRenderer\_GetFastStatus()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_getfaststatus)来获取音频播放流是否正在低时延状态下工作。
* 在部分特殊场景（如：存在更高优先级流、当前连接设备不支持等）下，开发者可以通过调用[OH\_AudioRenderer\_OnFastStatusChange()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_onfaststatuschange)来获取低时延状态改变事件。

**注意** 

低时延模式下，不支持调整播放速度。

### 使用低时延流的场景

* 游戏、K歌、直播等对时延要求较高的场景，建议使用低时延模式。
* 视频播放、音乐播放等对时延要求不敏感的场景，不建议使用低时延模式。

### 确保数据及时提供

低时延模式下，应用提供数据的频次比普通播放模式高，如果传送数据不及时可能导致杂音等问题。开发者应避免在数据回调线程中做耗时操作，确保数据回调线程可以及时返回。

### 数据回调线程

播放的音频数据需要通过回调接口写入。开发者要实现回调接口，使用[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)设置写入音频数据的回调函数，在设置音频回调函数时，回调函数[OH\_AudioRenderer\_OnWriteDataCallback](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)（从API version 12开始支持）用于写入音频数据。

开发音频播放功能的示例代码请参考：[推荐使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)。

设置数据回调函数示例：

```
// 自定义写入数据函数。
static OH_AudioData_Callback_Result MyOnWriteData_New(
    OH_AudioRenderer* renderer,
    void* userData,
    void* audioData,
    int32_t audioDataSize)
{
    // 将待播放的数据，按audioDataSize长度写入audioData。
    // 如果开发者不希望播放某段audioData，返回AUDIO_DATA_CALLBACK_RESULT_INVALID即可。
    size_t readCount = fread(audioData, audioDataSize, 1, g_fp);
    if (readCount == 0) {
        return AUDIO_DATA_CALLBACK_RESULT_INVALID;
    }
    if (feof(g_fp)) {
        fseek(g_fp, 0, SEEK_SET);
    }
    return AUDIO_DATA_CALLBACK_RESULT_VALID;
}
// ...
    // 配置写入音频数据回调函数。
    OH_AudioRenderer_OnWriteDataCallback writeDataCb = MyOnWriteData_New;
    OH_AudioStreamBuilder_SetRendererWriteDataCallback(builder, writeDataCb, nullptr);
```

* 为避免音频卡顿，禁止在回调函数OH\_AudioRenderer\_OnWriteDataCallback中执行耗时操作。
* 为保证OH\_AudioRenderer\_OnWriteDataCallback与流状态控制逻辑独立正常运行，禁止在OH\_AudioRenderer\_OnWriteDataCallback回调函数中调用音频流控制接口。

  | 音频流控制接口 | 说明 |
  | --- | --- |
  | OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer) | 开始播放。 |
  | OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer) | 暂停播放。 |
  | OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer) | 停止播放。 |
  | OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer) | 释放缓存数据。 |
  | OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer) | 释放播放实例。 |

  **注意** 

  音频流控制接口执行存在耗时（例如OH\_AudioRenderer\_Stop接口需要播完缓存，单次执行普遍超过50ms），应避免在主线程中直接调用，以免造成界面显示卡顿。
