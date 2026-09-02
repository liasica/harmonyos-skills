---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-change
title: 响应输出设备变更时合理暂停
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 响应输出设备变更时合理暂停
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b10034604270fcc083a44f86d96616841d5d98d9de12415f5b8994a150906c9f
---

开发者可以了解音频流输出设备变更信息，并完成相应适配，比如：应用在播放音乐时发现输出设备下线，为避免打扰用户，应该立即暂停音乐。

开发者可使用AudioRenderer的[on('outputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11)或AudioSessionManager的[on('currentOutputDeviceChanged')](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#oncurrentoutputdevicechanged20)，用于监听音频流输出设备变化及原因。当系统出现音频输出设备的上下线、用户强选、设备抢占或设备选择策略变更等情况，导致音频流输出设备变更时，系统将通过该接口通知应用当前音频流设备变更信息，包含当前音频流输出设备信息和设备变更原因。

## 音频流输出设备信息

在AudioRenderer的[on('outputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11)或AudioSessionManager的[on('currentOutputDeviceChanged')](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#oncurrentoutputdevicechanged20)返回的音频流设备变更信息中，包含当前音频流输出设备信息，以数组形式发送，一般该列表仅包含一个设备信息，具体可参考[AudioDeviceDescriptors](../harmonyos-references/arkts-apis-audio-t.md#audiodevicedescriptors)（设备信息列表）。

## 音频流输出设备变更原因

**说明** 

当发生下述四种情况（[AudioStreamDeviceChangeReason](../harmonyos-references/arkts-apis-audio-e.md#audiostreamdevicechangereason11)）时，系统将向应用发送设备变更回调。

* **REASON\_NEW\_DEVICE\_AVAILABLE**：新设备可用。

  **触发场景：**

  普通蓝牙设备（耳机、眼镜、音箱、车机等）连接、支持佩戴检测的蓝牙设备（耳机、眼镜等）佩戴、有线设备（3.5mm耳机、Type-C耳机、USB耳机、USB音箱等）插入、分布式设备上线等。
* **REASON\_OLD\_DEVICE\_UNAVAILABLE**：旧设备不可用。

  当报告此原因时，应用程序应考虑暂停音频播放。

  **触发场景：**

  普通蓝牙设备（耳机、眼镜、音箱、车机等）断开、支持佩戴检测的蓝牙耳机双耳摘下、支持佩戴检测的蓝牙眼镜摘下、有线设备（3.5mm耳机、Type-C耳机、USB耳机、USB音箱等）拔出、分布式设备下线等。

  针对此场景，常用业务场景的**处理建议**如下：

  + 游戏场景：不暂停
  + 听书场景：暂停
  + 音乐场景：暂停
  + 视频场景：暂停
* **REASON\_OVERRODE**：用户强制选择设备。

  **触发场景：**

  用户从界面选择切换音频流输出设备、从外设选择接听蜂窝或VoIP来电。
* **REASON\_UNKNOWN**：未知原因。

## 参考示例

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRoutingAndVolumeSample)。

### AudioRenderer示例

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioRenderer: audio.AudioRenderer | undefined = undefined;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：语音通话。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};
// ...

  // 创建AudioRenderer实例。
  audio.createAudioRenderer(audioRendererOptions, (err, renderer) => {
    if (!err) {
      console.info('Succeeded in creating audio renderer.');
      // ...
      audioRenderer = renderer;
      // ...
    } else {
      console.info(`Failed to create audio renderer. Code: ${err.code}, message: ${err.message}`);
      // ...
    }
  });
  // ...

  try {
    audioRenderer?.on('outputDeviceChangeWithInfo', (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
      console.info(`Succeeded in using on function. AudioStreamDeviceChangeInfo: ${JSON.stringify(deviceChangeInfo)}`);
      // ...
      switch (deviceChangeInfo.changeReason) {
        case audio.AudioStreamDeviceChangeReason.REASON_OLD_DEVICE_UNAVAILABLE:
          // 响应设备不可用事件，如果应用处于播放状态，应暂停播放，更新UX界面。
          audioRenderer?.pause();
          break;
        case audio.AudioStreamDeviceChangeReason.REASON_NEW_DEVICE_AVAILABLE:
          // 应用根据业务情况响应设备可用事件。
          break;
        case audio.AudioStreamDeviceChangeReason.REASON_OVERRODE:
          // 应用根据业务情况响应设备强选事件。
          break;
        case audio.AudioStreamDeviceChangeReason.REASON_UNKNOWN:
          // 应用根据业务情况响应未知原因事件。
          break;
      }
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```

### AudioSessionManager示例

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioRenderer: audio.AudioRenderer | undefined = undefined;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：语音通话。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioSessionManager = audio.getAudioManager().getSessionManager();
// ...

  // 创建AudioRenderer实例。
  audio.createAudioRenderer(audioRendererOptions, (err, renderer) => {
    if (!err) {
      console.info('Succeeded in creating audio renderer.');
      // ...
      audioRenderer = renderer;
      // ...
    } else {
      console.info(`Failed to create audio renderer. Code: ${err.code}, message: ${err.message}`);
      // ...
    }
  });
  // ...

  // 设置音频会话策略。
  let strategy: audio.AudioSessionStrategy = {
    concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
  };

  // 激活AudioSession。
  audioSessionManager.activateAudioSession(strategy).then(() => {
    console.info('Succeeded in activating audio session.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to activate audio session. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
  // ...

  try {
    // 订阅监听音频流输出设备变化及原因。
    audioSessionManager.on('currentOutputDeviceChanged', async (deviceChangeInfo: audio.CurrentOutputDeviceChangedEvent) => {
      console.info(`Succeeded in using on function. AudioStreamDeviceChangeInfo: ${JSON.stringify(deviceChangeInfo)}`);
      // ...
      switch (deviceChangeInfo.changeReason) {
        case audio.AudioStreamDeviceChangeReason.REASON_OLD_DEVICE_UNAVAILABLE:
          // 响应设备不可用事件，如果应用处于播放状态，应暂停播放，更新UX界面。
          audioRenderer?.pause();
          console.info('REASON_OLD_DEVICE_UNAVAILABLE, pause audio is recommended');
          break;
        case audio.AudioStreamDeviceChangeReason.REASON_NEW_DEVICE_AVAILABLE:
          // 应用根据业务情况响应设备可用事件。
          break;
        case audio.AudioStreamDeviceChangeReason.REASON_OVERRODE:
          // 应用根据业务情况响应设备强选事件。
          break;
        case audio.AudioStreamDeviceChangeReason.REASON_UNKNOWN:
          // 应用根据业务情况响应未知原因事件。
          break;
      }
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```
