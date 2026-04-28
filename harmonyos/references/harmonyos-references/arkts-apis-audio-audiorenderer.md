---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer
title: Interface (AudioRenderer)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioRenderer)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf8e031aa2874f322b6f38ed97e44cc1d04bf4d7a6d9b9ea1913bc91becaf28e
---

提供音频渲染的相关接口。

在使用AudioRenderer的接口之前，需先通过[createAudioRenderer](arkts-apis-audio-f.md#audiocreateaudiorenderer8)获取AudioRenderer实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 8开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state8+ | [AudioState](arkts-apis-audio-e.md#audiostate8) | 是 | 否 | 音频渲染器的状态。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let state: audio.AudioState = audioRenderer.state;
```

## getRendererInfo8+

PhonePC/2in1TabletTVWearable

getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void

获取当前创建的音频渲染器信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8)> | 是 | 回调函数。当获取音频渲染器的信息成功，err为undefined，data为获取到的音频渲染器的信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getRendererInfo((err: BusinessError, audioRendererInfo: audio.AudioRendererInfo) => {
4. if (err) {
5. console.error(`Failed to get renderer info. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
8. }
9. });
```

## getRendererInfo8+

PhonePC/2in1TabletTVWearable

getRendererInfo(): Promise<AudioRendererInfo>

获取当前创建的音频渲染器信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8)> | Promise对象，返回音频渲染器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getRendererInfo().then((audioRendererInfo: audio.AudioRendererInfo) => {
4. console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get renderer info. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getRendererInfoSync10+

PhonePC/2in1TabletTVWearable

getRendererInfoSync(): AudioRendererInfo

获取当前创建的音频渲染器信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 返回音频渲染器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioRendererInfo = audioRenderer.getRendererInfoSync();
5. console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get renderer info. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getStreamInfo8+

PhonePC/2in1TabletTVWearable

getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void

获取音频流信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8)> | 是 | 回调函数。当获取音频流信息成功，err为undefined，data为获取到的音频流信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
4. console.info('Renderer GetStreamInfo:');
5. console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
6. console.info(`Renderer channel: ${streamInfo.channels}`);
7. console.info(`Renderer format: ${streamInfo.sampleFormat}`);
8. console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
9. });
```

## getStreamInfo8+

PhonePC/2in1TabletTVWearable

getStreamInfo(): Promise<AudioStreamInfo>

获取音频流信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8)> | Promise对象，返回音频流信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getStreamInfo().then((streamInfo: audio.AudioStreamInfo) => {
4. console.info('Renderer GetStreamInfo:');
5. console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
6. console.info(`Renderer channel: ${streamInfo.channels}`);
7. console.info(`Renderer format: ${streamInfo.sampleFormat}`);
8. console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
9. }).catch((err: BusinessError) => {
10. console.error(`ERROR: ${err}`);
11. });
```

## getStreamInfoSync10+

PhonePC/2in1TabletTVWearable

getStreamInfoSync(): AudioStreamInfo

获取音频流信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8) | 返回音频流信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let streamInfo: audio.AudioStreamInfo = audioRenderer.getStreamInfoSync();
5. console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
6. console.info(`Renderer channel: ${streamInfo.channels}`);
7. console.info(`Renderer format: ${streamInfo.sampleFormat}`);
8. console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
9. } catch (err) {
10. let error = err as BusinessError;
11. console.error(`ERROR: ${error}`);
12. }
```

## getAudioStreamId9+

PhonePC/2in1TabletTVWearable

getAudioStreamId(callback: AsyncCallback<number>): void

获取音频流id。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音频流id成功，err为undefined，data为获取到的音频流id；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioStreamId((err: BusinessError, streamId: number) => {
4. console.info(`Renderer GetStreamId: ${streamId}`);
5. });
```

## getAudioStreamId9+

PhonePC/2in1TabletTVWearable

getAudioStreamId(): Promise<number>

获取音频流id。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流id。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioStreamId().then((streamId: number) => {
4. console.info(`Renderer getAudioStreamId: ${streamId}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioStreamIdSync10+

PhonePC/2in1TabletTVWearable

getAudioStreamIdSync(): number

获取音频流id。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频流id。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let streamId: number = audioRenderer.getAudioStreamIdSync();
5. console.info(`Renderer getAudioStreamIdSync: ${streamId}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`ERROR: ${error}`);
9. }
```

## setAudioEffectMode10+

PhonePC/2in1TabletTVWearable

setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void

设置当前音效模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioEffectMode](arkts-apis-audio-e.md#audioeffectmode10) | 是 | 音效模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置当前音效模式成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT_DEFAULT, (err: BusinessError) => {
4. if (err) {
5. console.error('Failed to set params');
6. } else {
7. console.info('Callback invoked to indicate a successful audio effect mode setting.');
8. }
9. });
```

## setAudioEffectMode10+

PhonePC/2in1TabletTVWearable

setAudioEffectMode(mode: AudioEffectMode): Promise<void>

设置当前音效模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioEffectMode](arkts-apis-audio-e.md#audioeffectmode10) | 是 | 音效模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT_DEFAULT).then(() => {
4. console.info('setAudioEffectMode SUCCESS');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioEffectMode10+

PhonePC/2in1TabletTVWearable

getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void

获取当前音效模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioEffectMode](arkts-apis-audio-e.md#audioeffectmode10)> | 是 | 回调函数。当获取当前音效模式成功，err为undefined，data为获取到的当前音效模式；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioEffectMode((err: BusinessError, effectMode: audio.AudioEffectMode) => {
4. if (err) {
5. console.error('Failed to get params');
6. } else {
7. console.info(`getAudioEffectMode: ${effectMode}`);
8. }
9. });
```

## getAudioEffectMode10+

PhonePC/2in1TabletTVWearable

getAudioEffectMode(): Promise<AudioEffectMode>

获取当前音效模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioEffectMode](arkts-apis-audio-e.md#audioeffectmode10)> | Promise对象，返回当前音效模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioEffectMode().then((effectMode: audio.AudioEffectMode) => {
4. console.info(`getAudioEffectMode: ${effectMode}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## start8+

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

启动音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动音频渲染器成功，err为undefined，否则为错误对象。异常将返回error对象：  错误码6800301：表示包含状态检查异常、焦点抢占失败、系统处理异常（具体错误查看系统日志）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.start((err: BusinessError) => {
4. if (err) {
5. console.error('Renderer start failed.');
6. } else {
7. console.info('Renderer start success.');
8. }
9. });
```

## start8+

PhonePC/2in1TabletTVWearable

start(): Promise<void>

启动音频渲染器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，成功表示启动音频渲染器成功。异常将返回error对象：  错误码6800301：表示包含状态检查异常、焦点抢占失败、系统处理异常（具体错误查看系统日志）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.start().then(() => {
4. console.info('Renderer started');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## pause8+

PhonePC/2in1TabletTVWearable

pause(callback: AsyncCallback<void>): void

暂停音频渲染。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当暂停渲染成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.pause((err: BusinessError) => {
4. if (err) {
5. console.error('Renderer pause failed');
6. } else {
7. console.info('Renderer paused.');
8. }
9. });
```

## pause8+

PhonePC/2in1TabletTVWearable

pause(): Promise<void>

暂停音频渲染。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.pause().then(() => {
4. console.info('Renderer paused');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## drain8+

PhonePC/2in1TabletTVWearable

drain(callback: AsyncCallback<void>): void

检查缓冲区是否已被耗尽。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当检查缓冲区是否已被耗尽成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.drain((err: BusinessError) => {
4. if (err) {
5. console.error('Renderer drain failed');
6. } else {
7. console.info('Renderer drained.');
8. }
9. });
```

## drain8+

PhonePC/2in1TabletTVWearable

drain(): Promise<void>

检查缓冲区是否已被耗尽。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.drain().then(() => {
4. console.info('Renderer drained successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## flush11+

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

清空缓冲区（[AudioState](arkts-apis-audio-e.md#audiostate8)为STATE\_RUNNING、STATE\_PAUSED、STATE\_STOPPED状态下可用）。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permit at current state. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.flush().then(() => {
4. console.info('Renderer flushed successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## stop8+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止音频渲染。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止渲染成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.stop((err: BusinessError) => {
4. if (err) {
5. console.error('Renderer stop failed');
6. } else {
7. console.info('Renderer stopped.');
8. }
9. });
```

## stop8+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止音频渲染。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.stop().then(() => {
4. console.info('Renderer stopped successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## release8+

PhonePC/2in1TabletTVWearable

release(callback: AsyncCallback<void>): void

释放音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放音频渲染器成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.release((err: BusinessError) => {
4. if (err) {
5. console.error('Renderer release failed');
6. } else {
7. console.info('Renderer released.');
8. }
9. });
```

## release8+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放音频渲染器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.release().then(() => {
4. console.info('Renderer released successfully');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioTime8+

PhonePC/2in1TabletTVWearable

getAudioTime(callback: AsyncCallback<number>): void

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取时间戳成功，err为undefined，data为获取到的时间戳；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioTime((err: BusinessError, timestamp: number) => {
4. console.info(`Current timestamp: ${timestamp}`);
5. });
```

## getAudioTime8+

PhonePC/2in1TabletTVWearable

getAudioTime(): Promise<number>

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回时间戳。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioTime().then((timestamp: number) => {
4. console.info(`Current timestamp: ${timestamp}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioTimeSync10+

PhonePC/2in1TabletTVWearable

getAudioTimeSync(): number

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回时间戳。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let timestamp: number = audioRenderer.getAudioTimeSync();
5. console.info(`Current timestamp: ${timestamp}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`ERROR: ${error}`);
9. }
```

## getAudioTimestampInfo19+

PhonePC/2in1TabletTVWearable

getAudioTimestampInfo(): Promise<AudioTimestampInfo>

获取输出音频流时间戳和位置信息，适配倍速接口。使用Promise异步回调。

获取输出音频流时间戳和位置信息，通常用于进行音画同步对齐。

注意，当实际播放位置（framePosition）为0时，时间戳（timestamp）是固定值，直到流真正跑起来时才会更新。当调用Flush接口时实际播放位置也会被重置。

当音频流路由（route）变化时，例如设备变化或者输出类型变化时，播放位置也会被重置，但此时时间戳仍会持续增长。推荐当实际播放位置和时间戳的变化稳定后再使用该接口获取的值。该接口适配倍速接口，例如当播放速度设置为2倍时，播放位置的增长速度也会返回为正常的2倍。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioTimestampInfo](arkts-apis-audio-i.md#audiotimestampinfo19)> | Promise对象，返回音频流时间戳和当前数据帧位置信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permit at current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
4. console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getAudioTimestampInfoSync19+

PhonePC/2in1TabletTVWearable

getAudioTimestampInfoSync(): AudioTimestampInfo

获取音频流时间戳和当前数据帧位置信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioTimestampInfo](arkts-apis-audio-i.md#audiotimestampinfo19) | 返回音频流时间戳和当前数据帧位置信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Operation not permit at current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioTimestampInfo: audio.AudioTimestampInfo = audioRenderer.getAudioTimestampInfoSync();
5. console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`ERROR: ${error}`);
9. }
```

## getLatency23+

PhonePC/2in1TabletTVWearable

getLatency(type: AudioLatencyType): number

获取当前音频路由的预估时延。

说明

* 无线连接的音频设备，时延估算会存在误差，结果仅供参考。
* 由于时延未计入实时缓冲区，建议仅在音频播放开始时获取，避免频繁调用，否则可能因路由切换而阻塞该接口调用。
* 音频输出到硬件后的音画同步建议使用[getAudioTimestampInfo](arkts-apis-audio-audiorenderer.md#getaudiotimestampinfo19)或[getAudioTimestampInfoSync](arkts-apis-audio-audiorenderer.md#getaudiotimestampinfosync19)完成。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AudioLatencyType](arkts-apis-audio-e.md#audiolatencytype23) | 是 | 获取的时延类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频时延，单位为毫秒。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permitted in release state. |
| 6800301 | System internal error, like audio service error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. const latency: number = audioRenderer.getLatency(audio.AudioLatencyType.LATENCY_TYPE_ALL);
5. console.info(`Current audio latency: ${latency}ms`);
6. } catch (err) {
7. const error = err as BusinessError;
8. console.error(`Failed to get latency. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getBufferSize8+

PhonePC/2in1TabletTVWearable

getBufferSize(callback: AsyncCallback<number>): void

获取音频渲染器的最小缓冲区大小。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音频渲染器的最小缓冲区大小成功，err为undefined，data为获取到的最小缓冲区大小；否则为错误对象。  单位为字节。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let bufferSize: number;

5. audioRenderer.getBufferSize((err: BusinessError, data: number) => {
6. if (err) {
7. console.error('getBufferSize error');
8. } else {
9. console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
10. bufferSize = data;
11. }
12. });
```

## getBufferSize8+

PhonePC/2in1TabletTVWearable

getBufferSize(): Promise<number>

获取音频渲染器的最小缓冲区大小。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回缓冲区大小。  单位为字节。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let bufferSize: number;

5. audioRenderer.getBufferSize().then((data: number) => {
6. console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
7. bufferSize = data;
8. }).catch((err: BusinessError) => {
9. console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
10. });
```

## getBufferSizeSync10+

PhonePC/2in1TabletTVWearable

getBufferSizeSync(): number

获取音频渲染器的最小缓冲区大小。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回缓冲区大小，单位为字节。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let bufferSize: number = 0;

5. try {
6. bufferSize = audioRenderer.getBufferSizeSync();
7. console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${bufferSize}`);
8. } catch (err) {
9. let error = err as BusinessError;
10. console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${error}`);
11. }
```

## setSpeed11+

PhonePC/2in1TabletTVWearable

setSpeed(speed: number): void

设置播放倍速。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 设置播放的倍速值，倍速范围为[0.25, 4.0]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioRenderer.setSpeed(1.5);
```

## getSpeed11+

PhonePC/2in1TabletTVWearable

getSpeed(): number

获取播放倍速。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回播放的倍速值，倍速范围为[0.25, 4.0]。 |

**示例：**

```
1. let speed = audioRenderer.getSpeed();
```

## setInterruptMode9+

PhonePC/2in1TabletTVWearable

setInterruptMode(mode: InterruptMode): Promise<void>

设置应用的焦点模型。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-apis-audio-e.md#interruptmode9) | 是 | 焦点模型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let mode = 0;

5. audioRenderer.setInterruptMode(mode).then(() => {
6. console.info('setInterruptMode Success!');
7. }).catch((err: BusinessError) => {
8. console.error(`setInterruptMode Fail: ${err}`);
9. });
```

## setInterruptMode9+

PhonePC/2in1TabletTVWearable

setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void

设置应用的焦点模型。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-apis-audio-e.md#interruptmode9) | 是 | 焦点模型。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置应用的焦点模型成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let mode = 1;

5. audioRenderer.setInterruptMode(mode, (err: BusinessError) => {
6. if(err){
7. console.error(`setInterruptMode Fail: ${err}`);
8. }
9. console.info('setInterruptMode Success!');
10. });
```

## setInterruptModeSync10+

PhonePC/2in1TabletTVWearable

setInterruptModeSync(mode: InterruptMode): void

设置应用的焦点模型。同步设置。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [InterruptMode](arkts-apis-audio-e.md#interruptmode9) | 是 | 焦点模型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. audioRenderer.setInterruptModeSync(0);
5. console.info('setInterruptMode Success!');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`setInterruptMode Fail: ${error}`);
9. }
```

## setVolume9+

PhonePC/2in1TabletTVWearable

setVolume(volume: number): Promise<void>

设置音频流的音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 音量值范围为[0.0, 1.0]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.setVolume(0.5).then(() => {
4. console.info('setVolume Success!');
5. }).catch((err: BusinessError) => {
6. console.error(`setVolume Fail: ${err}`);
7. });
```

## setVolume9+

PhonePC/2in1TabletTVWearable

setVolume(volume: number, callback: AsyncCallback<void>): void

设置音频流的音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 音量值范围为[0.0, 1.0]。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置应用的音量成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.setVolume(0.5, (err: BusinessError) => {
4. if(err){
5. console.error(`setVolume Fail: ${err}`);
6. return;
7. }
8. console.info('setVolume Success!');
9. });
```

## getVolume12+

PhonePC/2in1TabletTVWearable

getVolume(): number

获取音频流的音量。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音量大小，音量值范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: number = audioRenderer.getVolume();
5. console.info(`Indicate that the volume is obtained ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to obtain the volume, error ${error}.`);
9. }
```

## getMinStreamVolume10+

PhonePC/2in1TabletTVWearable

getMinStreamVolume(callback: AsyncCallback<number>): void

获取音频流的最小音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音频流的最小音量成功，err为undefined，data为获取到的应用基于音频流的最小音量；否则为错误对象。  音量范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getMinStreamVolume((err: BusinessError, minVolume: number) => {
4. if (err) {
5. console.error(`getMinStreamVolume error: ${err}`);
6. } else {
7. console.info(`getMinStreamVolume Success! ${minVolume}`);
8. }
9. });
```

## getMinStreamVolume10+

PhonePC/2in1TabletTVWearable

getMinStreamVolume(): Promise<number>

获取音频流的最小音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流最小音量。  音量范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getMinStreamVolume().then((value: number) => {
4. console.info(`Get min stream volume Success! ${value}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Get min stream volume Fail: ${err}`);
7. });
```

## getMinStreamVolumeSync10+

PhonePC/2in1TabletTVWearable

getMinStreamVolumeSync(): number

获取音频流的最小音量。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频流最小音量，音量范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: number = audioRenderer.getMinStreamVolumeSync();
5. console.info(`Get min stream volume Success! ${value}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Get min stream volume Fail: ${error}`);
9. }
```

## getMaxStreamVolume10+

PhonePC/2in1TabletTVWearable

getMaxStreamVolume(callback: AsyncCallback<number>): void

获取音频流的最大音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音频流的最大音量成功，err为undefined，data为获取到的应用基于音频流的最大音量；否则为错误对象。  音量范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getMaxStreamVolume((err: BusinessError, maxVolume: number) => {
4. if (err) {
5. console.error(`getMaxStreamVolume Fail: ${err}`);
6. } else {
7. console.info(`getMaxStreamVolume Success! ${maxVolume}`);
8. }
9. });
```

## getMaxStreamVolume10+

PhonePC/2in1TabletTVWearable

getMaxStreamVolume(): Promise<number>

获取音频流的最大音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流最大音量。  音量范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getMaxStreamVolume().then((value: number) => {
4. console.info(`Get max stream volume Success! ${value}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Get max stream volume Fail: ${err}`);
7. });
```

## getMaxStreamVolumeSync10+

PhonePC/2in1TabletTVWearable

getMaxStreamVolumeSync(): number

获取音频流的最大音量。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频流最大音量，音量范围为[0.0, 1.0]。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: number = audioRenderer.getMaxStreamVolumeSync();
5. console.info(`Get max stream volume Success! ${value}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Get max stream volume Fail: ${error}`);
9. }
```

## getUnderflowCount10+

PhonePC/2in1TabletTVWearable

getUnderflowCount(callback: AsyncCallback<number>): void

获取当前播放音频流的欠载音频帧数量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取当前播放音频流的欠载音频帧数量成功，err为undefined，data为获取到的当前播放音频流的欠载音频帧数量；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getUnderflowCount((err: BusinessError, underflowCount: number) => {
4. if (err) {
5. console.error(`getUnderflowCount Fail: ${err}`);
6. } else {
7. console.info(`getUnderflowCount Success! ${underflowCount}`);
8. }
9. });
```

## getUnderflowCount10+

PhonePC/2in1TabletTVWearable

getUnderflowCount(): Promise<number>

获取当前播放音频流的欠载音频帧数量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回音频流的欠载音频帧数量。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getUnderflowCount().then((value: number) => {
4. console.info(`Get underflow count Success! ${value}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Get underflow count Fail: ${err}`);
7. });
```

## getUnderflowCountSync10+

PhonePC/2in1TabletTVWearable

getUnderflowCountSync(): number

获取当前播放音频流的欠载音频帧数量，同步返回数据。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回音频流的欠载音频帧数量。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: number = audioRenderer.getUnderflowCountSync();
5. console.info(`Get underflow count Success! ${value}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Get underflow count Fail: ${error}`);
9. }
```

## getCurrentOutputDevices10+

PhonePC/2in1TabletTVWearable

getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void

获取音频流输出设备信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数。当获取音频流输出设备信息成功，err为undefined，data为获取到的音频流输出设备信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getCurrentOutputDevices((err: BusinessError, deviceInfo: audio.AudioDeviceDescriptors) => {
4. if (err) {
5. console.error(`getCurrentOutputDevices Fail: ${err}`);
6. } else {
7. for (let i = 0; i < deviceInfo.length; i++) {
8. console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
9. console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
10. console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
11. console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
12. console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
13. console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
14. console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
15. console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
16. }
17. }
18. });
```

## getCurrentOutputDevices10+

PhonePC/2in1TabletTVWearable

getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>

获取音频流输出设备信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | Promise对象，返回音频流的输出设备信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getCurrentOutputDevices().then((deviceInfo: audio.AudioDeviceDescriptors) => {
4. for (let i = 0; i < deviceInfo.length; i++) {
5. console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
6. console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
7. console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
8. console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
9. console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
10. console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
11. console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
12. console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
13. }
14. }).catch((err: BusinessError) => {
15. console.error(`Get current output devices Fail: ${err}`);
16. });
```

## getCurrentOutputDevicesSync10+

PhonePC/2in1TabletTVWearable

getCurrentOutputDevicesSync(): AudioDeviceDescriptors

获取音频流输出设备信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 返回音频流的输出设备信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let deviceInfo: audio.AudioDeviceDescriptors = audioRenderer.getCurrentOutputDevicesSync();
5. for (let i = 0; i < deviceInfo.length; i++) {
6. console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
7. console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
8. console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
9. console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
10. console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
11. console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
12. console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
13. console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
14. }
15. } catch (err) {
16. let error = err as BusinessError;
17. console.error(`Get current output devices Fail: ${error}`);
18. }
```

## setChannelBlendMode11+

PhonePC/2in1TabletTVWearable

setChannelBlendMode(mode: ChannelBlendMode): void

设置单双声道混合模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ChannelBlendMode](arkts-apis-audio-e.md#channelblendmode11) | 是 | 声道混合模式类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |

**示例：**

```
1. let mode = audio.ChannelBlendMode.MODE_DEFAULT;

3. audioRenderer.setChannelBlendMode(mode);
4. console.info(`BlendMode: ${mode}`);
```

## setVolumeWithRamp11+

PhonePC/2in1TabletTVWearable

setVolumeWithRamp(volume: number, duration: number): void

在指定时间范围内设置音量渐变模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 渐变目标音量值，音量范围为[0.0, 1.0]。 |
| duration | number | 是 | 渐变持续时间，单位为ms。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. let volume = 0.5;
2. let duration = 1000;

4. audioRenderer.setVolumeWithRamp(volume, duration);
5. console.info(`setVolumeWithRamp: ${volume}`);
```

## setSilentModeAndMixWithOthers12+

PhonePC/2in1TabletTVWearable

setSilentModeAndMixWithOthers(on: boolean): void

设置静音并发播放模式。

当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其他音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | boolean | 是 | 打开/关闭静音并发播放模式。true表示设置当前播放的音频流静音播放，并且不会打断其它音频流播放。false表示取消当前播放的音频流静音播放，音频流可根据系统焦点策略抢占焦点。 |

**示例：**

```
1. audioRenderer.setSilentModeAndMixWithOthers(true);
```

## getSilentModeAndMixWithOthers12+

PhonePC/2in1TabletTVWearable

getSilentModeAndMixWithOthers(): boolean

获取静音并发播放模式。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 静音并发播放模式状态。返回true表示打开，返回false表示关闭。 |

**示例：**

```
1. let on = audioRenderer.getSilentModeAndMixWithOthers();
```

## setDefaultOutputDevice12+

PhonePC/2in1TabletTVWearable

setDefaultOutputDevice(deviceType: DeviceType): Promise<void>

设置默认发声设备。使用Promise异步回调。

说明

* 本接口仅适用于[StreamUsage](arkts-apis-audio-e.md#streamusage)为语音消息、VoIP语音通话或者VoIP视频通话的场景，支持听筒、扬声器和系统默认设备。
* 本接口允许在AudioRenderer创建后随时调用，系统会记录应用设置的默认本机内置发声设备。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声；否则，系统遵循应用设置的默认本机内置发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**设备行为差异：** 当该接口在无听筒的设备上设置默认发声设备为听筒时，将继续从扬声器发声。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [DeviceType](arkts-apis-audio-e.md#devicetype) | 是 | 设备类型。  仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 本接口允许在AudioRenderer创建以后的任何时间被调用。
4. // 未播放时调用，系统会记录应用设置的默认本机内置发声设备，当应用启动播放时从设置的默认本机内置发声设备发声。
5. // 正在播放时调用，在没有外接设备如蓝牙耳机/有线耳机，系统会立即切换到设置的默认本机内置发声设备发声；否则系统会先记录应用设置的默认本机内置发声设备，等外接设备移除后再切换到设置的默认本机内置发声设备发声。
6. audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
7. console.info('setDefaultOutputDevice Success!');
8. }).catch((err: BusinessError) => {
9. console.error(`setDefaultOutputDevice Fail: ${err}`);
10. });
```

## on('audioInterrupt')9+

PhonePC/2in1TabletTVWearable

on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

AudioRenderer对象在start事件时获取焦点，在pause、stop等事件时释放焦点，无需开发者主动申请。

调用此方法后，如果AudioRenderer对象获取焦点失败或发生中断事件（如被其他音频打断等），会收到[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)。建议应用根据InterruptEvent的信息进行进一步处理。更多信息请参阅文档[音频焦点介绍](../harmonyos-guides/audio-playback-concurrency.md)。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当音频焦点状态发生变化时，触发该事件。 |
| callback | Callback<[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 是 | 回调函数，返回中断事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let isPlaying: boolean = false; // 标识符，表示是否正在渲染。
4. let isDucked: boolean = false; // 标识符，表示是否被降低音量。

6. audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
7. // 在发生音频打断事件时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
8. // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
9. // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
10. // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
11. if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
12. // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
13. switch (interruptEvent.hintType) {
14. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
15. // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
16. console.info('Force paused. Update playing status and stop writing');
17. isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
18. break;
19. case audio.InterruptHint.INTERRUPT_HINT_STOP:
20. // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
21. console.info('Force stopped. Update playing status and stop writing');
22. isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
23. break;
24. case audio.InterruptHint.INTERRUPT_HINT_DUCK:
25. // 音频流已被降低音量渲染。
26. console.info('Force ducked. Update volume status');
27. isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
28. break;
29. case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
30. // 音频流已被恢复正常音量渲染。
31. console.info('Force unducked. Update volume status');
32. isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
33. break;
34. default:
35. console.info('Invalid interruptEvent');
36. break;
37. }
38. } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
39. // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
40. switch (interruptEvent.hintType) {
41. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
42. // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
43. // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
44. console.info('Resume force paused renderer or ignore');
45. // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
46. break;
47. default:
48. console.info('Invalid interruptEvent');
49. break;
50. }
51. }
52. });
```

## off('audioInterrupt')18+

PhonePC/2in1TabletTVWearable

off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void

取消监听音频中断事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当取消监听音频中断事件时，触发该事件。 |
| callback | Callback<[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 否 | 回调函数，返回中断事件信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('audioInterrupt');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let isPlaying: boolean; // 标识符，表示是否正在渲染。
6. let isDucked: boolean; // 标识符，表示是否被降低音量。

8. let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
9. // 在发生音频打断事件时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
10. // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
11. // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
12. // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
13. if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
14. // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
15. switch (interruptEvent.hintType) {
16. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
17. // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
18. console.info('Force paused. Update playing status and stop writing');
19. isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
20. break;
21. case audio.InterruptHint.INTERRUPT_HINT_STOP:
22. // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
23. console.info('Force stopped. Update playing status and stop writing');
24. isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
25. break;
26. case audio.InterruptHint.INTERRUPT_HINT_DUCK:
27. // 音频流已被降低音量渲染。
28. console.info('Force ducked. Update volume status');
29. isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
30. break;
31. case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
32. // 音频流已被恢复正常音量渲染。
33. console.info('Force unducked. Update volume status');
34. isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
35. break;
36. default:
37. console.info('Invalid interruptEvent');
38. break;
39. }
40. } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
41. // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
42. switch (interruptEvent.hintType) {
43. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
44. // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
45. // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
46. console.info('Resume force paused renderer or ignore');
47. // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
48. break;
49. default:
50. console.info('Invalid interruptEvent');
51. break;
52. }
53. }
54. };

56. audioRenderer.on('audioInterrupt', audioInterruptCallback);

58. audioRenderer.off('audioInterrupt', audioInterruptCallback);
```

## on('markReach')8+

PhonePC/2in1TabletTVWearable

on(type: 'markReach', frame: number, callback: Callback<number>): void

监听标记到达事件（当渲染的帧数到达frame参数的值时触发，仅调用一次）。使用callback异步回调。

如果将frame设置为100，当渲染帧数到达第100帧时，系统将上报信息。

**系统能力:** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'markReach'，当渲染的帧数到达frame参数的值时，触发该事件。 |
| frame | number | 是 | 触发事件的帧数。该值必须大于0。 |
| callback | Callback<number> | 是 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. audioRenderer.on('markReach', 1000, (position: number) => {
2. if (position == 1000) {
3. console.info('ON Triggered successfully');
4. }
5. });
```

## off('markReach')8+

PhonePC/2in1TabletTVWearable

off(type: 'markReach', callback?: Callback<number>): void

取消监听标记到达事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'markReach'，当取消监听标记到达事件时，触发该事件。 |
| callback18+ | Callback<number> | 否 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('markReach');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let markReachCallback = (position: number) => {
6. if (position == 1000) {
7. console.info('ON Triggered successfully');
8. }
9. };

11. audioRenderer.on('markReach', 1000, markReachCallback);

13. audioRenderer.off('markReach', markReachCallback);
```

## on('periodReach')8+

PhonePC/2in1TabletTVWearable

on(type: 'periodReach', frame: number, callback: Callback<number>): void

监听标记到达事件（每当渲染的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。

如果将frame设置为10，每渲染10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'periodReach'，当渲染的帧数达到frame参数的值时，触发该事件。 |
| frame | number | 是 | 触发事件的帧数。该值必须大于 0。 |
| callback | Callback<number> | 是 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. audioRenderer.on('periodReach', 1000, (position: number) => {
2. if (position == 1000) {
3. console.info('ON Triggered successfully');
4. }
5. });
```

## off('periodReach')8+

PhonePC/2in1TabletTVWearable

off(type: 'periodReach', callback?: Callback<number>): void

取消监听标记到达事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'periodReach'，当取消监听标记到达事件时，触发该事件。 |
| callback18+ | Callback<number> | 否 | 回调函数，返回frame参数的值。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('periodReach');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let periodReachCallback = (position: number) => {
6. if (position == 1000) {
7. console.info('ON Triggered successfully');
8. }
9. };

11. audioRenderer.on('periodReach', 1000, periodReachCallback);

13. audioRenderer.off('periodReach', periodReachCallback);
```

## on('stateChange')8+

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: Callback<AudioState>): void

监听状态变化事件（当AudioRenderer的状态发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当AudioRenderer的状态发生变化时，触发该事件。 |
| callback | Callback<[AudioState](arkts-apis-audio-e.md#audiostate8)> | 是 | 回调函数，返回当前音频的状态。 |

**示例：**

```
1. audioRenderer.on('stateChange', (state: audio.AudioState) => {
2. if (state == 1) {
3. console.info('audio renderer state is: STATE_PREPARED');
4. }
5. if (state == 2) {
6. console.info('audio renderer state is: STATE_RUNNING');
7. }
8. });
```

## off('stateChange')18+

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: Callback<AudioState>): void

取消监听状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当取消监听状态变化事件时，触发该事件。 |
| callback | Callback<[AudioState](arkts-apis-audio-e.md#audiostate8)> | 否 | 回调函数，返回当前音频的状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('stateChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let stateChangeCallback = (state: audio.AudioState) => {
6. if (state == 1) {
7. console.info('audio renderer state is: STATE_PREPARED');
8. }
9. if (state == 2) {
10. console.info('audio renderer state is: STATE_RUNNING');
11. }
12. };

14. audioRenderer.on('stateChange', stateChangeCallback);

16. audioRenderer.off('stateChange', stateChangeCallback);
```

## on('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void

监听音频输出设备变化事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'outputDeviceChange'，当音频输出设备发生变化时，触发该事件。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数，返回当前音频流的输出设备描述信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioRenderer.on('outputDeviceChange', (deviceInfo: audio.AudioDeviceDescriptors) => {
2. console.info(`DeviceInfo id: ${deviceInfo[0].id}`);
3. console.info(`DeviceInfo name: ${deviceInfo[0].name}`);
4. console.info(`DeviceInfo address: ${deviceInfo[0].address}`);
5. });
```

## off('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void

取消监听音频输出设备变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'outputDeviceChange'，当取消监听音频输出设备变化事件时，触发该事件。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 否 | 回调函数，返回当前音频流的输出设备描述信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('outputDeviceChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let outputDeviceChangeCallback = (deviceInfo: audio.AudioDeviceDescriptors) => {
6. console.info(`DeviceInfo id: ${deviceInfo[0].id}`);
7. console.info(`DeviceInfo name: ${deviceInfo[0].name}`);
8. console.info(`DeviceInfo address: ${deviceInfo[0].address}`);
9. };

11. audioRenderer.on('outputDeviceChange', outputDeviceChangeCallback);

13. audioRenderer.off('outputDeviceChange', outputDeviceChangeCallback);
```

## on('outputDeviceChangeWithInfo')11+

PhonePC/2in1TabletTVWearable

on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void

监听音频流输出设备变化及原因事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'outputDeviceChangeWithInfo'，当音频输出设备发生变化时，触发该事件。 |
| callback | Callback<[AudioStreamDeviceChangeInfo](arkts-apis-audio-i.md#audiostreamdevicechangeinfo11)> | 是 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioRenderer.on('outputDeviceChangeWithInfo', (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
2. console.info(`DeviceInfo id: ${deviceChangeInfo.devices[0].id}`);
3. console.info(`DeviceInfo name: ${deviceChangeInfo.devices[0].name}`);
4. console.info(`DeviceInfo address: ${deviceChangeInfo.devices[0].address}`);
5. console.info(`Device change reason: ${deviceChangeInfo.changeReason}`);
6. });
```

## off('outputDeviceChangeWithInfo')11+

PhonePC/2in1TabletTVWearable

off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void

取消监听音频流输出设备变化及原因事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'outputDeviceChangeWithInfo'，当取消监听音频流输出设备变化及原因事件时，触发该事件。 |
| callback | Callback<[AudioStreamDeviceChangeInfo](arkts-apis-audio-i.md#audiostreamdevicechangeinfo11)> | 否 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('outputDeviceChangeWithInfo');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let outputDeviceChangeWithInfoCallback = (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
6. console.info(`DeviceInfo id: ${deviceChangeInfo.devices[0].id}`);
7. console.info(`DeviceInfo name: ${deviceChangeInfo.devices[0].name}`);
8. console.info(`DeviceInfo address: ${deviceChangeInfo.devices[0].address}`);
9. console.info(`Device change reason: ${deviceChangeInfo.changeReason}`);
10. };

12. audioRenderer.on('outputDeviceChangeWithInfo', outputDeviceChangeWithInfoCallback);

14. audioRenderer.off('outputDeviceChangeWithInfo', outputDeviceChangeWithInfoCallback);
```

## on('writeData')11+

PhonePC/2in1TabletTVWearable

on(type: 'writeData', callback: AudioRendererWriteDataCallback): void

监听音频数据写入回调事件（当需要写入音频数据时触发），使用 callback 方式返回结果。

回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'writeData'，当需要写入音频数据时，触发该事件。 |
| callback | [AudioRendererWriteDataCallback](arkts-apis-audio-t.md#audiorendererwritedatacallback12) | 是 | 回调函数，入参代表应用接收待写入的数据缓冲区。  API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果[AudioDataCallbackResult](arkts-apis-audio-e.md#audiodatacallbackresult12)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import {fileIo as fs} from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. class Options {
6. offset?: number;
7. length?: number;
8. }

10. let bufferSize: number = 0;
11. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
12. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. let path = context.cacheDir;
14. // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
15. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
16. let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
17. let writeDataCallback = (buffer: ArrayBuffer) => {
18. let options: Options = {
19. offset: bufferSize,
20. length: buffer.byteLength
21. };

23. try {
24. fs.readSync(file.fd, buffer, options);
25. bufferSize += buffer.byteLength;
26. // API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果。
27. return audio.AudioDataCallbackResult.VALID;
28. } catch (error) {
29. console.error('Error reading file:', error);
30. // API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果。
31. return audio.AudioDataCallbackResult.INVALID;
32. }
33. };

35. audioRenderer.on('writeData', writeDataCallback);
36. audioRenderer.start().then(() => {
37. console.info('Renderer started');
38. }).catch((err: BusinessError) => {
39. console.error(`ERROR: ${err}`);
40. });
```

## off('writeData')11+

PhonePC/2in1TabletTVWearable

off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void

取消监听音频数据写入回调事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'writeData'，当取消监听音频数据写入回调事件时，触发该事件。 |
| callback | [AudioRendererWriteDataCallback](arkts-apis-audio-t.md#audiorendererwritedatacallback12) | 否 | 回调函数，入参代表应用接收待写入的数据缓冲区。  API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果[AudioDataCallbackResult](arkts-apis-audio-e.md#audiodatacallbackresult12)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRenderer.off('writeData');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let writeDataCallback = (data: ArrayBuffer) => {
6. console.info(`write data: ${data}`);
7. };

9. audioRenderer.on('writeData', writeDataCallback);

11. audioRenderer.off('writeData', writeDataCallback);
```

## write(deprecated)

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void

写入缓冲区。使用callback异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[on('writeData')](arkts-apis-audio-audiorenderer.md#onwritedata11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 要写入缓冲区的数据。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当写入缓冲区成功，err为undefined，data为获取到的写入的字节数；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. let bufferSize: number;
6. class Options {
7. offset?: number;
8. length?: number;
9. }
10. audioRenderer.getBufferSize().then((data: number)=> {
11. console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
12. bufferSize = data;
13. console.info(`Buffer size: ${bufferSize}`);
14. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. let path = context.cacheDir;
17. // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
18. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
19. let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
20. fs.stat(filePath).then(async (stat: fs.Stat) => {
21. let buf = new ArrayBuffer(bufferSize);
22. let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
23. for (let i = 0;i < len; i++) {
24. let options: Options = {
25. offset: i * bufferSize,
26. length: bufferSize
27. };
28. await fs.read(file.fd, buf, options);
29. await new Promise((resolve,reject)=>{
30. audioRenderer.write(buf,(err: BusinessError, writeSize: number)=>{
31. if(err){
32. reject(err)
33. }else{
34. resolve(writeSize)
35. }
36. })
37. })
38. }
39. });
40. }).catch((err: BusinessError) => {
41. console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
42. });
```

## write(deprecated)

PhonePC/2in1TabletTVWearable

write(buffer: ArrayBuffer): Promise<number>

写入缓冲区。使用Promise异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[on('writeData')](arkts-apis-audio-audiorenderer.md#onwritedata11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 要写入缓冲区的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回写入的字节数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. let bufferSize: number;
6. class Options {
7. offset?: number;
8. length?: number;
9. }
10. audioRenderer.getBufferSize().then((data: number) => {
11. console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
12. bufferSize = data;
13. console.info(`BufferSize: ${bufferSize}`);
14. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. let path = context.cacheDir;
17. // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
18. let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
19. let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
20. fs.stat(filePath).then(async (stat: fs.Stat) => {
21. let buf = new ArrayBuffer(bufferSize);
22. let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
23. for (let i = 0;i < len; i++) {
24. let options: Options = {
25. offset: i * bufferSize,
26. length: bufferSize
27. };
28. await fs.read(file.fd, buf, options);
29. try{
30. await audioRenderer.write(buf);
31. } catch(err) {
32. let error = err as BusinessError;
33. console.error(`audioRenderer.write err: ${error}`);
34. }
35. }
36. });
37. }).catch((err: BusinessError) => {
38. console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
39. });
```

## setRenderRate(deprecated)

PhonePC/2in1TabletTVWearable

setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void

设置音频渲染速率。使用callback异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[setSpeed](arkts-apis-audio-audiorenderer.md#setspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | [AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8) | 是 | 渲染的速率。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置音频渲染速率成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER_RATE_NORMAL, (err: BusinessError) => {
4. if (err) {
5. console.error('Failed to set params');
6. } else {
7. console.info('Callback invoked to indicate a successful render rate setting.');
8. }
9. });
```

## setRenderRate(deprecated)

PhonePC/2in1TabletTVWearable

setRenderRate(rate: AudioRendererRate): Promise<void>

设置音频渲染速率。使用Promise异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[setSpeed](arkts-apis-audio-audiorenderer.md#setspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | [AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8) | 是 | 渲染的速率。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER_RATE_NORMAL).then(() => {
4. console.info('setRenderRate SUCCESS');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getRenderRate(deprecated)

PhonePC/2in1TabletTVWearable

getRenderRate(callback: AsyncCallback<AudioRendererRate>): void

获取音频渲染速率。使用callback异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[getSpeed](arkts-apis-audio-audiorenderer.md#getspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8)> | 是 | 回调函数。当获取当前渲染速率成功，err为undefined，data为获取到的当前渲染速率；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getRenderRate((err: BusinessError, renderRate: audio.AudioRendererRate) => {
4. console.info(`getRenderRate: ${renderRate}`);
5. });
```

## getRenderRate(deprecated)

PhonePC/2in1TabletTVWearable

getRenderRate(): Promise<AudioRendererRate>

获取音频渲染速率。使用Promise异步回调。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[getSpeed](arkts-apis-audio-audiorenderer.md#getspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8)> | Promise对象，返回渲染速率。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRenderer.getRenderRate().then((renderRate: audio.AudioRendererRate) => {
4. console.info(`getRenderRate: ${renderRate}`);
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## getRenderRateSync(deprecated)

PhonePC/2in1TabletTVWearable

getRenderRateSync(): AudioRendererRate

获取音频渲染速率。同步返回结果。

说明

从API version 10开始支持，从API version 11开始废弃，建议使用[getSpeed](arkts-apis-audio-audiorenderer.md#getspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRendererRate](arkts-apis-audio-e.md#audiorendererrate8) | 返回渲染速率。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let renderRate: audio.AudioRendererRate = audioRenderer.getRenderRateSync();
5. console.info(`getRenderRate: ${renderRate}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`ERROR: ${error}`);
9. }
```

## setLoudnessGain20+

PhonePC/2in1TabletTVWearable

setLoudnessGain(loudnessGain: number): Promise<void>

设置播放响度。使用Promise异步回调。

说明

* 该接口仅支持类型为[STREAM\_USAGE\_MUSIC](arkts-apis-audio-e.md#streamusage)、[STREAM\_USAGE\_MOVIE](arkts-apis-audio-e.md#streamusage)或[STREAM\_USAGE\_AUDIOBOOK](arkts-apis-audio-e.md#streamusage)的音频流。
* 该接口不支持高清通路的响度设置。
* 由于音频框架与硬件之间存在缓冲区，响度调节实际生效存在延迟，时长取决于缓冲区长度。
* 建议在不同音频开始播放前预先设置响度，以实现最佳均衡效果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loudnessGain | number | 是 | 设置播放的响度值，单位为dB，响度范围为[-90.0, 24.0]。默认值为0.0dB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800104 | Operation is not supported on this renderer, e.g. the stream usage of this renderer is not one of [STREAM\_USAGE\_MUSIC](arkts-apis-audio-e.md#streamusage),  [STREAM\_USAGE\_MOVIE](arkts-apis-audio-e.md#streamusage), or [STREAM\_USAGE\_AUDIOBOOK](arkts-apis-audio-e.md#streamusage), or this renderer is routed through the high-resolution playback path. |

**示例：**

```
1. audioRenderer.setLoudnessGain(1.0);
```

## getLoudnessGain20+

PhonePC/2in1TabletTVWearable

getLoudnessGain(): number

获取播放响度。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回播放的响度值，单位为分贝。 |

**示例：**

```
1. let loudnessGain = audioRenderer.getLoudnessGain();
```
