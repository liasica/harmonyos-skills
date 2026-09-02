---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-f
title: Functions
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Functions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2c3c968b89d39eca4c6a83055479b5c03d18b12ef8dfd80bcfef4cc6d9d7b448
---

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

## audio.getAudioManager

getAudioManager(): AudioManager

获取音频管理器。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioManager](arkts-apis-audio-audiomanager.md) | 音频管理器对象。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
```

## audio.createAudioRenderer8+

createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void

创建音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-apis-audio-i.md#audiorendereroptions8) | 是 | 配置渲染器。 |
| callback | AsyncCallback<[AudioRenderer](arkts-apis-audio-audiorenderer.md)> | 是 | 回调函数。当创建音频渲染器成功，err为undefined，data为创建的音频渲染器对象；否则为错误对象。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

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

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions,(err, data) => {
  if (err) {
    console.error(`AudioRenderer Created: Error: ${err}`);
  } else {
    console.info('AudioRenderer Created: SUCCESS');
    audioRenderer = data;
  }
});
```

## audio.createAudioRenderer8+

createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>

创建音频渲染器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-apis-audio-i.md#audiorendereroptions8) | 是 | 配置渲染器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRenderer](arkts-apis-audio-audiorenderer.md)> | Promise对象，返回音频渲染器对象。 |

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

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions).then((data) => {
  audioRenderer = data;
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}`);
});
```

## audio.createAudioCapturer8+

createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void

创建音频采集器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

当设置Mic音频源（即[SourceType](arkts-apis-audio-e.md#sourcetype8)为SOURCE\_TYPE\_MIC、SOURCE\_TYPE\_VOICE\_RECOGNITION、SOURCE\_TYPE\_VOICE\_COMMUNICATION、SOURCE\_TYPE\_VOICE\_MESSAGE、SOURCE\_TYPE\_CAMCORDER）时需要该权限。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioCapturerOptions](arkts-apis-audio-i.md#audiocaptureroptions8) | 是 | 配置音频采集器。 |
| callback | AsyncCallback<[AudioCapturer](arkts-apis-audio-audiocapturer.md)> | 是 | 回调函数。当创建音频采集器成功，err为undefined，data为创建的音频采集器对象；否则为错误对象。  异常将返回error对象：  返回错误码6800301：表示参数校验异常、权限校验异常或系统处理异常（具体错误查看系统日志）。  返回错误码6800101：表示必选参数为空或参数类型错误。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

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

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
  if (err) {
    console.error(`AudioCapturer Created : Error: ${err}`);
  } else {
    console.info('AudioCapturer Created : SUCCESS');
    audioCapturer = data;
  }
});
```

## audio.createAudioCapturer8+

createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>

创建音频采集器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

当设置Mic音频源（即[SourceType](arkts-apis-audio-e.md#sourcetype8)为SOURCE\_TYPE\_MIC、SOURCE\_TYPE\_VOICE\_RECOGNITION、SOURCE\_TYPE\_VOICE\_COMMUNICATION、SOURCE\_TYPE\_VOICE\_MESSAGE、SOURCE\_TYPE\_CAMCORDER）时需要该权限。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioCapturerOptions](arkts-apis-audio-i.md#audiocaptureroptions8) | 是 | 配置音频采集器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioCapturer](arkts-apis-audio-audiocapturer.md)> | Promise对象，成功将返回音频采集器对象，异常将返回error对象。  返回错误码6800301：表示参数校验异常、权限校验异常或系统处理异常（具体错误查看系统日志）。  返回错误码6800101：表示必选参数为空或参数类型错误。 |

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

let audioCapturerOptions:audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions).then((data) => {
  audioCapturer = data;
  console.info('AudioCapturer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioCapturer Created : ERROR : ${err}`);
});
```

## audio.createAudioLoopback20+

createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>

创建音频返听器。使用Promise异步回调。

在使用createAudioLoopback接口之前，需先通过[isAudioLoopbackSupported](arkts-apis-audio-audiostreammanager.md#isaudioloopbacksupported20)查询系统返听能力。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

* API version 20-24，需要申请权限才可以使用本接口。
* 从API版本26.0.0开始，无需申请权限可以直接使用本接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-apis-audio-e.md#audioloopbackmode20) | 是 | 音频返听模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioLoopback](arkts-apis-audio-audioloopback.md)> | Promise对象，成功将返回音频返听器对象，异常将返回error对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied.  适用版本：20-24 |
| 801 | Unsupported API.  适用版本：20-24 |
| 6800101 | Parameter verification failed. |
| 6800104 | Loopback mode is unsupported. |

**示例：**

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioLoopback: audio.AudioLoopback;

audio.createAudioLoopback(audio.AudioLoopbackMode.HARDWARE).then((data) => {
  audioLoopback = data;
  console.info('AudioLoopback Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioLoopback Created : ERROR : ${err}`);
});
```
