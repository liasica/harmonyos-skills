---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager
title: Interface (AudioStreamManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioStreamManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:41+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:53b60779f93790246fc3443e65c93e1c5fcba804d50e9ae05631edbdcc8502a3
---

音频流管理。

在使用AudioStreamManager的接口之前，需先通过[getStreamManager](arkts-apis-audio-audiomanager.md#getstreammanager9)获取AudioStreamManager实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## getCurrentAudioRendererInfoArray9+

PhonePC/2in1TabletTVWearable

getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void

获取当前音频渲染器的信息。使用callback异步回调。

说明

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力**: SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioRendererChangeInfoArray](arkts-apis-audio-t.md#audiorendererchangeinfoarray9)> | 是 | 回调函数。当获取当前音频渲染器的信息成功，err为undefined，data为获取到的当前音频渲染器的信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.getCurrentAudioRendererInfoArray((err: BusinessError, audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
4. if (err) {
5. console.error(`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
8. }
9. });
```

## getCurrentAudioRendererInfoArray9+

PhonePC/2in1TabletTVWearable

getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>

获取当前音频渲染器的信息。使用Promise异步回调。

说明

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRendererChangeInfoArray](arkts-apis-audio-t.md#audiorendererchangeinfoarray9)> | Promise对象，返回当前音频渲染器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.getCurrentAudioRendererInfoArray().then((audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
4. console.info(`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getCurrentAudioRendererInfoArraySync10+

PhonePC/2in1TabletTVWearable

getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray

获取当前音频渲染器的信息。同步返回结果。

说明

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRendererChangeInfoArray](arkts-apis-audio-t.md#audiorendererchangeinfoarray9) | 返回当前音频渲染器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray = audioStreamManager.getCurrentAudioRendererInfoArraySync();
5. console.info(`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get current audio renderer info array. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getCurrentAudioCapturerInfoArray9+

PhonePC/2in1TabletTVWearable

getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void

获取当前音频采集器的信息。使用callback异步回调。

说明

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioCapturerChangeInfoArray](arkts-apis-audio-t.md#audiocapturerchangeinfoarray9)> | 是 | 回调函数。当获取当前音频采集器的信息成功，err为undefined，data为获取到的当前音频采集器的信息；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.getCurrentAudioCapturerInfoArray((err: BusinessError, audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
4. if (err) {
5. console.error(`Failed to get current audio capturer info array. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
8. }
9. });
```

## getCurrentAudioCapturerInfoArray9+

PhonePC/2in1TabletTVWearable

getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>

获取当前音频采集器的信息。使用Promise异步回调。

说明

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioCapturerChangeInfoArray](arkts-apis-audio-t.md#audiocapturerchangeinfoarray9)> | Promise对象，返回当前音频采集器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.getCurrentAudioCapturerInfoArray().then((audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
4. console.info(`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get current audio capturer info array. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getCurrentAudioCapturerInfoArraySync10+

PhonePC/2in1TabletTVWearable

getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray

获取当前音频采集器的信息。同步返回结果。

说明

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioCapturerChangeInfoArray](arkts-apis-audio-t.md#audiocapturerchangeinfoarray9) | 返回当前音频采集器信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let audioCapturerChangeInfoArray = audioStreamManager.getCurrentAudioCapturerInfoArraySync();
5. console.info(`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get current audio capturer info array. Code: ${error.code}, message: ${error.message}`);
9. }
```

## on('audioRendererChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void

监听音频渲染器更改事件（当音频播放流状态变化或设备变化时触发）。使用callback异步回调。

说明

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioRendererChange'，当音频播放流状态变化或设备变化时，触发该事件。 |
| callback | Callback<[AudioRendererChangeInfoArray](arkts-apis-audio-t.md#audiorendererchangeinfoarray9)> | 是 | 回调函数，返回当前音频渲染器信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioStreamManager.on('audioRendererChange',  (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
2. console.info(`Succeeded in using on function, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
3. });
```

## off('audioRendererChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void

取消监听音频渲染器更改事件。使用callback异步回调。

说明

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioRendererChange'，当取消监听音频渲染器更改事件时，触发该事件。 |
| callback18+ | Callback<[AudioRendererChangeInfoArray](arkts-apis-audio-t.md#audiorendererchangeinfoarray9)> | 否 | 回调函数，返回当前音频渲染器信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
2. // 当订阅了多个该事件的监听时，可通过 audioStreamManager.off('audioRendererChange'); 取消该事件的所有监听。
3. let audioRendererChangeCallback = (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
4. console.info(`Succeeded in using on or off function, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
5. };

7. audioStreamManager.on('audioRendererChange', audioRendererChangeCallback);

9. audioStreamManager.off('audioRendererChange', audioRendererChangeCallback);
```

## on('audioCapturerChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void

监听音频采集器更改事件（当音频录制流状态变化或设备变化时触发）。使用callback异步回调。

说明

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioCapturerChange'，当音频录制流状态变化或设备变化时，触发该事件。 |
| callback | Callback<[AudioCapturerChangeInfoArray](arkts-apis-audio-t.md#audiocapturerchangeinfoarray9)> | 是 | 回调函数，返回当前音频采集器信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioStreamManager.on('audioCapturerChange', (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
2. console.info(`Succeeded in using on function, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
3. });
```

## off('audioCapturerChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void

取消监听音频采集器更改事件。使用callback异步回调。

说明

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioCapturerChange'，当取消监听音频采集器更改事件时，触发该事件。 |
| callback18+ | Callback<[AudioCapturerChangeInfoArray](arkts-apis-audio-t.md#audiocapturerchangeinfoarray9)> | 否 | 回调函数，返回当前音频采集器信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
2. // 当订阅了多个该事件的监听时，可通过 audioStreamManager.off('audioCapturerChange'); 取消该事件的所有监听。
3. let audioCapturerChangeCallback = (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
4. console.info(`Succeeded in using on or off function, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
5. };

7. audioStreamManager.on('audioCapturerChange', audioCapturerChangeCallback);

9. audioStreamManager.off('audioCapturerChange', audioCapturerChangeCallback);
```

## isActive(deprecated)

PhonePC/2in1TabletTVWearable

isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音频流活跃状态。使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[isStreamActive](arkts-apis-audio-audiostreammanager.md#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频流类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音频流活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to obtain the active status of the stream. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the active status of the stream is obtained ${value}.`);
9. });
```

## isActive(deprecated)

PhonePC/2in1TabletTVWearable

isActive(volumeType: AudioVolumeType): Promise<boolean>

获取指定音频流是否为活跃状态。使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[isStreamActive](arkts-apis-audio-audiostreammanager.md#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频流类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示流状态为活跃；返回false表示流状态不活跃。 |

**示例：**

```
1. audioStreamManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
2. console.info(`Promise returned to indicate that the active status of the stream is obtained ${value}.`);
3. });
```

## isActiveSync(deprecated)

PhonePC/2in1TabletTVWearable

isActiveSync(volumeType: AudioVolumeType): boolean

获取指定音频流是否为活跃状态。同步返回结果。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[isStreamActive](arkts-apis-audio-audiostreammanager.md#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频流类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 流的活跃状态。返回true表示活跃，返回false表示不活跃。 |

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
4. let value: boolean = audioStreamManager.isActiveSync(audio.AudioVolumeType.MEDIA);
5. console.info(`Indicate that the active status of the stream is obtained ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to obtain the active status of the stream ${error}.`);
9. }
```

## isStreamActive20+

PhonePC/2in1TabletTVWearable

isStreamActive(streamUsage: StreamUsage): boolean

获取指定音频流是否为活跃状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流使用类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 流是否处于活跃状态。返回true表示活跃，返回false表示不活跃。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isStreamActive = audioStreamManager.isStreamActive(audio.StreamUsage.STREAM_USAGE_MUSIC);
5. console.info(`Succeeded in using isStreamActive function, IsStreamActive: ${isStreamActive}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to use isStreamActive function. code: ${error.code}, message: ${error.message}`);
9. }
```

## getAudioEffectInfoArray10+

PhonePC/2in1TabletTVWearable

getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void

获取当前音效模式的信息。使用callback异步回调。

**系统能力**: SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| usage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流使用类型。 |
| callback | AsyncCallback<[AudioEffectInfoArray](arkts-apis-audio-audiostreammanager.md#getaudioeffectinfoarray10)> | 是 | 回调函数。当获取当前音效模式的信息成功，err为undefined，data为获取到的当前音效模式的信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.getAudioEffectInfoArray(audio.StreamUsage.STREAM_USAGE_MUSIC, (err: BusinessError, audioEffectInfoArray: audio.AudioEffectInfoArray) => {
4. if (err) {
5. console.error(`Failed to get audio effect info array. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.`);
8. }
9. });
```

## getAudioEffectInfoArray10+

PhonePC/2in1TabletTVWearable

getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>

获取当前音效模式的信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| usage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流使用类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioEffectInfoArray](arkts-apis-audio-audiostreammanager.md#getaudioeffectinfoarray10)> | Promise对象，返回当前音效模式的信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioStreamManager.getAudioEffectInfoArray(audio.StreamUsage.STREAM_USAGE_MUSIC).then((audioEffectInfoArray: audio.AudioEffectInfoArray) => {
4. console.info(`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get audio effect info array. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getAudioEffectInfoArraySync10+

PhonePC/2in1TabletTVWearable

getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray

获取当前音效模式的信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| usage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流使用类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioEffectInfoArray](arkts-apis-audio-audiostreammanager.md#getaudioeffectinfoarray10) | 返回当前音效模式的信息。 |

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
4. let audioEffectInfoArray = audioStreamManager.getAudioEffectInfoArraySync(audio.StreamUsage.STREAM_USAGE_MUSIC);
5. console.info(`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get audio effect info array. Code: ${error.code}, message: ${error.message}`);
9. }
```

## isAcousticEchoCancelerSupported20+

PhonePC/2in1TabletTVWearable

isAcousticEchoCancelerSupported(sourceType: SourceType): boolean

查询指定的source type是否支持回声消除。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceType | [SourceType](arkts-apis-audio-e.md#sourcetype8) | 是 | 音源类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持回声消除。true表示支持回声消除，false表示不支持回声消除。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isAcousticEchoCancelerSupported = audioStreamManager.isAcousticEchoCancelerSupported(audio.SourceType.SOURCE_TYPE_LIVE);
5. console.info(`Succeeded in using isAcousticEchoCancelerSupported function, IsAcousticEchoCancelerSupported: ${isAcousticEchoCancelerSupported}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to use isAcousticEchoCancelerSupported function. code: ${error.code}, message: ${error.message}`);
9. }
```

## isAudioLoopbackSupported20+

PhonePC/2in1TabletTVWearable

isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean

查询当前系统是否支持指定的音频返听模式。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-apis-audio-e.md#audioloopbackmode20) | 是 | 音频返听模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持指定的音频返听模式。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isAudioLoopbackSupported = audioStreamManager.isAudioLoopbackSupported(audio.AudioLoopbackMode.HARDWARE);
5. console.info(`Succeeded in using isAudioLoopbackSupported function, IsAudioLoopbackSupported: ${isAudioLoopbackSupported}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to use isAudioLoopbackSupported function. code: ${error.code}, message: ${error.message}`);
9. }
```

## isRecordingAvailable20+

PhonePC/2in1TabletTVWearable

isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean

检查传入的音频采集器信息中音源类型的录制是否可以启动成功。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 是 | 音频采集器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 代表录制是否可以启动成功。true表示成功，false表示失败。  仅检测是否可以获取音频采集器信息中音源类型的焦点。通常在音频录制启动前调用，否则已存在的录制流可能会拒绝其启动。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let audioStreamInfo: audio.AudioStreamInfo = {
4. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
5. channels: audio.AudioChannel.CHANNEL_2,
6. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
7. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
8. };

10. let audioCapturerInfo: audio.AudioCapturerInfo = {
11. source: audio.SourceType.SOURCE_TYPE_MIC,
12. capturerFlags: 0
13. };

15. let audioCapturerOptions: audio.AudioCapturerOptions = {
16. streamInfo: audioStreamInfo,
17. capturerInfo: audioCapturerInfo
18. };

20. audio.createAudioCapturer(audioCapturerOptions, (err: BusinessError, audioCapturer: audio.AudioCapturer) => {
21. if (err) {
22. console.error(`Failed to create AudioCapturer. Code: ${err.code}, message: ${err.message}`);
23. } else {
24. console.info('Succeeded in creating AudioCapturer.');
25. try {
26. let isRecordingAvailable = audioStreamManager.isRecordingAvailable(audioCapturerInfo);
27. console.info(`Succeeded in using isRecordingAvailable function, IsRecordingAvailable: ${isRecordingAvailable}.`);
28. } catch (err) {
29. let error = err as BusinessError;
30. console.error(`Failed to use isRecordingAvailable function. code: ${error.code}, message: ${error.message}`);
31. }
32. }
33. });
```

## isIntelligentNoiseReductionEnabledForCurrentDevice21+

PhonePC/2in1TabletTVWearable

isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean

查询指定的音源类型智能降噪开关是否打开。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceType | [SourceType](arkts-apis-audio-e.md#sourcetype8) | 是 | 表示音源类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 智能降噪开关的状态。true表示打开，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let isSupport = audioStreamManager.isIntelligentNoiseReductionEnabledForCurrentDevice(audio.SourceType.SOURCE_TYPE_LIVE);
5. console.info(`SourceType: ${audio.SourceType.SOURCE_TYPE_LIVE} intelligent noise reduction enabled is: ${isSupport}`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`isIntelligentNoiseReductionEnabledForCurrentDevice ERROR: ${error}`);
9. }
```
