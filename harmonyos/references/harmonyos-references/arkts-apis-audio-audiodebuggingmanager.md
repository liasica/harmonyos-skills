---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiodebuggingmanager
title: Interface (AudioDebuggingManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioDebuggingManager)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:786e93eda64f16ab628c7aa4c20d549869ad6cb85816043cf5d65c271d9a184b
---

音频调试管理器，用于音频运行时调试，包括获取快照信息等功能，用于定位音频播放、录音、耳返、会话等场景中的异常问题。

**起始版本：** 26.0.0

**说明** 

快照信息的内容和格式后续会根据开发者使用情况和反馈建议优化调整，随版本迭代可能发生变化，所以仅供人工调试参考，不建议开发者依据快照信息开发功能逻辑。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

## printAppInfo

printAppInfo(fd: number): void

打印当前应用进程的完整音频运行时快照。快照包含所有播放流、录音流和音频会话信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符，指定快照信息的写入位置。小于0或不可写时，快照信息将输出到运行日志；否则输出到fd指向的文件。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let debugManager = audioManager.getDebuggingManager();

// 输出到日志。
debugManager.printAppInfo(-1);
```

## printRendererInfo

printRendererInfo(renderer: AudioRenderer, fd: number): void

打印指定音频播放实例的完整音频运行时快照。快照包含流信息、通路信息、音量和设备信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| renderer | [AudioRenderer](arkts-apis-audio-audiorenderer.md) | 是 | 目标音频播放实例。 |
| fd | number | 是 | 文件描述符，指定快照信息的写入位置。小于0或不可写时，快照信息将输出到运行日志；否则输出到fd指向的文件。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioManager = audio.getAudioManager();
let debugManager = audioManager.getDebuggingManager();

audio.createAudioRenderer(audioRendererOptions).then((data) => {
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : SUCCESS');
  let audioRenderer = data;
  // 输出到日志。
  debugManager.printRendererInfo(audioRenderer, -1);
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}`);
});
```

## printCapturerInfo

printCapturerInfo(capturer: AudioCapturer, fd: number): void

打印指定录音实例的完整音频运行时快照。快照包含流信息、通路信息、音量和设备信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capturer | [AudioCapturer](arkts-apis-audio-audiocapturer.md) | 是 | 目标录音实例。 |
| fd | number | 是 | 文件描述符，指定快照信息的写入位置。小于0或不可写时，快照信息将输出到运行日志；否则输出到fd指向的文件。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioManager = audio.getAudioManager();
let debugManager = audioManager.getDebuggingManager();

audio.createAudioCapturer(audioCapturerOptions).then((data) => {
  console.info('AudioCapturer Created : SUCCESS');
  let audioCapturer = data;
  // 输出到日志。
  debugManager.printCapturerInfo(audioCapturer, -1);
}).catch((err: BusinessError) => {
  console.error(`AudioCapturer Created : ERROR : ${err}`);
});
```

## printLoopbackInfo

printLoopbackInfo(loopback: AudioLoopback, fd: number): void

打印指定耳返实例的完整音频运行时快照。快照包含耳返状态、设备和音效信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loopback | [AudioLoopback](arkts-apis-audio-audioloopback.md) | 是 | 目标耳返实例。 |
| fd | number | 是 | 文件描述符，指定快照信息的写入位置。小于0或不可写时，快照信息将输出到运行日志；否则输出到fd指向的文件。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioManager = audio.getAudioManager();
let debugManager = audioManager.getDebuggingManager();

audio.createAudioLoopback(audio.AudioLoopbackMode.HARDWARE).then((data) => {
  console.info('AudioLoopback Created : SUCCESS');
  let audioLoopback = data;
  // 输出到日志。
  debugManager.printLoopbackInfo(audioLoopback, -1);
}).catch((err: BusinessError) => {
  console.error(`AudioLoopback Created : ERROR : ${err}`);
});
```

## printSessionInfo

printSessionInfo(session: AudioSessionManager, fd: number): void

打印指定会话管理器实例的完整音频运行时快照。快照包含会话状态、场景、策略和设备信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| session | [AudioSessionManager](arkts-apis-audio-audiosessionmanager.md) | 是 | 目标会话管理器实例。 |
| fd | number | 是 | 文件描述符，指定快照信息的写入位置。小于0或不可写时，快照信息将输出到运行日志；否则输出到fd指向的文件。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
let debugManager = audioManager.getDebuggingManager();

// 输出到日志。
debugManager.printSessionInfo(audioSessionManager, -1);
```
