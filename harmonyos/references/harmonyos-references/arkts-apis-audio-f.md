---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-f
title: Functions
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:11:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:791efc0ec174eb9a73fe3bd079bbcb657d27533e74264140509149d43fe29b50
---

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## audio.getAudioManager

PhonePC/2in1TabletTVWearable

getAudioManager(): AudioManager

获取音频管理器。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioManager](arkts-apis-audio-audiomanager.md) | 音频管理器对象。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioManager = audio.getAudioManager();
```

## audio.createAudioRenderer8+

PhonePC/2in1TabletTVWearable

createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void

获取音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-apis-audio-i.md#audiorendereroptions8) | 是 | 配置渲染器。 |
| callback | AsyncCallback<[AudioRenderer](arkts-apis-audio-audiorenderer.md)> | 是 | 回调函数。当获取音频渲染器成功，err为undefined，data为获取到的音频渲染器对象；否则为错误对象。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioStreamInfo: audio.AudioStreamInfo = {
4. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
5. channels: audio.AudioChannel.CHANNEL_2, // 通道。
6. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
7. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
8. };

10. let audioRendererInfo: audio.AudioRendererInfo = {
11. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
12. rendererFlags: 0 // 音频渲染器标志。
13. };

15. let audioRendererOptions: audio.AudioRendererOptions = {
16. streamInfo: audioStreamInfo,
17. rendererInfo: audioRendererInfo
18. };

20. let audioRenderer: audio.AudioRenderer;

22. audio.createAudioRenderer(audioRendererOptions,(err, data) => {
23. if (err) {
24. console.error(`AudioRenderer Created: Error: ${err}`);
25. } else {
26. console.info('AudioRenderer Created: SUCCESS');
27. audioRenderer = data;
28. }
29. });
```

## audio.createAudioRenderer8+

PhonePC/2in1TabletTVWearable

createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>

获取音频渲染器。使用Promise异步回调。

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

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let audioStreamInfo: audio.AudioStreamInfo = {
5. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
6. channels: audio.AudioChannel.CHANNEL_2, // 通道。
7. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
8. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
9. };

11. let audioRendererInfo: audio.AudioRendererInfo = {
12. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
13. rendererFlags: 0 // 音频渲染器标志。
14. };

16. let audioRendererOptions: audio.AudioRendererOptions = {
17. streamInfo: audioStreamInfo,
18. rendererInfo: audioRendererInfo
19. };

21. let audioRenderer: audio.AudioRenderer;

23. audio.createAudioRenderer(audioRendererOptions).then((data) => {
24. audioRenderer = data;
25. console.info('AudioFrameworkRenderLog: AudioRenderer Created : SUCCESS');
26. }).catch((err: BusinessError) => {
27. console.error(`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}`);
28. });
```

## audio.createAudioCapturer8+

PhonePC/2in1TabletTVWearable

createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void

获取音频采集器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

当设置Mic音频源（即[SourceType](arkts-apis-audio-e.md#sourcetype8)为SOURCE\_TYPE\_MIC、SOURCE\_TYPE\_VOICE\_RECOGNITION、SOURCE\_TYPE\_VOICE\_COMMUNICATION、SOURCE\_TYPE\_VOICE\_MESSAGE、SOURCE\_TYPE\_CAMCORDER）时需要该权限。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioCapturerOptions](arkts-apis-audio-i.md#audiocaptureroptions8) | 是 | 配置音频采集器。 |
| callback | AsyncCallback<[AudioCapturer](arkts-apis-audio-audiocapturer.md)> | 是 | 回调函数。当获取音频采集器成功，err为undefined，data为获取到的音频采集器对象；否则为错误对象。异常将返回error对象：  错误码6800301：表示参数校验异常、权限校验异常或系统处理异常（具体错误查看系统日志）。  错误码6800101：表示必选参数为空或参数类型错误。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioStreamInfo: audio.AudioStreamInfo = {
4. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
5. channels: audio.AudioChannel.CHANNEL_2, // 通道。
6. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
7. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
8. };

10. let audioCapturerInfo: audio.AudioCapturerInfo = {
11. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
12. capturerFlags: 0 // 音频采集器标志。
13. };

15. let audioCapturerOptions: audio.AudioCapturerOptions = {
16. streamInfo: audioStreamInfo,
17. capturerInfo: audioCapturerInfo
18. };

20. let audioCapturer: audio.AudioCapturer;

22. audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
23. if (err) {
24. console.error(`AudioCapturer Created : Error: ${err}`);
25. } else {
26. console.info('AudioCapturer Created : SUCCESS');
27. audioCapturer = data;
28. }
29. });
```

## audio.createAudioCapturer8+

PhonePC/2in1TabletTVWearable

createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>

获取音频采集器。使用Promise异步回调。

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
| Promise<[AudioCapturer](arkts-apis-audio-audiocapturer.md)> | Promise对象，成功将返回音频采集器对象，异常将返回error对象：  错误码6800301：表示参数校验异常、权限校验异常或系统处理异常（具体错误查看系统日志）。  错误码6800101：表示必选参数为空或参数类型错误。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let audioStreamInfo: audio.AudioStreamInfo = {
5. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
6. channels: audio.AudioChannel.CHANNEL_2, // 通道。
7. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
8. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
9. };

11. let audioCapturerInfo: audio.AudioCapturerInfo = {
12. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
13. capturerFlags: 0 // 音频采集器标志。
14. };

16. let audioCapturerOptions:audio.AudioCapturerOptions = {
17. streamInfo: audioStreamInfo,
18. capturerInfo: audioCapturerInfo
19. };

21. let audioCapturer: audio.AudioCapturer;

23. audio.createAudioCapturer(audioCapturerOptions).then((data) => {
24. audioCapturer = data;
25. console.info('AudioCapturer Created : SUCCESS');
26. }).catch((err: BusinessError) => {
27. console.error(`AudioCapturer Created : ERROR : ${err}`);
28. });
```

## audio.createAudioLoopback20+

PhonePC/2in1TabletTVWearable

createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>

创建音频返听器。使用Promise异步回调。

在使用createAudioLoopback接口之前，需先通过[isAudioLoopbackSupported](arkts-apis-audio-audiostreammanager.md#isaudioloopbacksupported20)查询系统返听能力。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

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
| 201 | Permission denied. |
| 801 | Unsupported API. |
| 6800101 | Parameter verification failed. |
| 6800104 | Loopback mode is unsupported. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let audioLoopback: audio.AudioLoopback;

6. audio.createAudioLoopback(audio.AudioLoopbackMode.HARDWARE).then((data) => {
7. audioLoopback = data;
8. console.info('AudioLoopback Created : SUCCESS');
9. }).catch((err: BusinessError) => {
10. console.error(`AudioLoopback Created : ERROR : ${err}`);
11. });
```
