---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager
title: Interface (AudioVolumeManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioVolumeManager)
category: harmonyos-references
scraped_at: 2026-04-29T14:02:21+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6e361450409eb10c68bd630d0284ff19d8496a87dad0382cae0b968f3cb8744d
---

音量管理。

在使用AudioVolumeManager的接口之前，需先通过[getVolumeManager](arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## getVolumeGroupManager9+

PhonePC/2in1TabletTVWearable

getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void

获取音频组音量管理器实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | number | 是 | 音量组id，默认使用DEFAULT\_VOLUME\_GROUP\_ID。 |
| callback | AsyncCallback<[AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md)> | 是 | 回调函数。当获取音频组音量管理器实例成功，err为undefined，data为获取到的音频组音量管理器实例；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;
4. let audioVolumeGroupManager: audio.AudioVolumeGroupManager;

6. audioVolumeManager.getVolumeGroupManager(groupId, (err: BusinessError, value: audio.AudioVolumeGroupManager) => {
7. if (err) {
8. console.error(`Failed to get volume group manager. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in getting volume group manager.');
12. audioVolumeGroupManager = value;
13. });
```

## getVolumeGroupManager9+

PhonePC/2in1TabletTVWearable

getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>

获取音频组音量管理器实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | number | 是 | 音量组id，默认使用DEFAULT\_VOLUME\_GROUP\_ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise< [AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md) > | Promise对象，返回音频组音量管理器实例。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;
5. let audioVolumeGroupManager: audio.AudioVolumeGroupManager;

7. audioVolumeManager.getVolumeGroupManager(groupId).then((value: audio.AudioVolumeGroupManager) => {
8. console.info('Succeeded in getting volume group manager.');
9. audioVolumeGroupManager = value;
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to get volume group manager. Code: ${err.code}, message: ${err.message}`);
12. });
```

## getVolumeGroupManagerSync10+

PhonePC/2in1TabletTVWearable

getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager

获取音频组音量管理器实例。同步返回结果。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | number | 是 | 音量组id，默认使用DEFAULT\_VOLUME\_GROUP\_ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md) | 音频组音量管理器实例。 |

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
4. let audioVolumeGroupManager: audio.AudioVolumeGroupManager = audioVolumeManager.getVolumeGroupManagerSync(audio.DEFAULT_VOLUME_GROUP_ID);
5. console.info('Succeeded in getting volume group manager.');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get volume group manager. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getAppVolumePercentage19+

PhonePC/2in1TabletTVWearable

getAppVolumePercentage(): Promise<number>

获取应用的音量（范围为[0, 100]）。使用Promise异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回应用的音量。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. audioVolumeManager.getAppVolumePercentage().then((value: number) => {
4. console.info(`app volume is ${value}.`);
5. });
```

## setAppVolumePercentage19+

PhonePC/2in1TabletTVWearable

setAppVolumePercentage(volume: number): Promise<void>

设置应用的音量（范围为[0, 100]）。使用Promise异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 要设置的音量值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Crash or blocking occurs in system process. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. audioVolumeManager.setAppVolumePercentage(20).then(() => {
4. console.info(`set app volume success.`);
5. });
```

## on('volumeChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'volumeChange', callback: Callback<VolumeEvent>): void

监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[on('streamVolumeChange')](arkts-apis-audio-audiovolumemanager.md#onstreamvolumechange20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'volumeChange'，当系统音量发生变化时，触发该事件。 |
| callback | Callback<[VolumeEvent](arkts-apis-audio-i.md#volumeevent9)> | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioVolumeManager.on('volumeChange', (volumeEvent: audio.VolumeEvent) => {
2. console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
3. console.info(`Volume level: ${volumeEvent.volume} `);
4. console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
5. });
```

## off('volumeChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void

取消监听系统音量变化事件。使用callback异步回调。

说明

从API version 12开始支持，从API version 20开始废弃，建议使用[off('streamVolumeChange')](arkts-apis-audio-audiovolumemanager.md#offstreamvolumechange20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'volumeChange'，当取消监听系统音量变化事件时，触发该事件。 |
| callback | Callback<[VolumeEvent](arkts-apis-audio-i.md#volumeevent9)> | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioVolumeManager.off('volumeChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let volumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
6. console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
7. console.info(`Volume level: ${volumeEvent.volume} `);
8. console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
9. };

11. audioVolumeManager.on('volumeChange', volumeChangeCallback);

13. audioVolumeManager.off('volumeChange', volumeChangeCallback);
```

## on('appVolumeChange')19+

PhonePC/2in1TabletTVWearable

on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void

监听当前应用的应用级音量变化事件（当应用级音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'appVolumeChange'，当应用级音量发生变化时，触发该事件。 |
| callback | Callback<[VolumeEvent](arkts-apis-audio-i.md#volumeevent9)> | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioVolumeManager.on('appVolumeChange', (volumeEvent: audio.VolumeEvent) => {
2. console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
3. console.info(`Volume level: ${volumeEvent.volume} `);
4. console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
5. });
```

## off('appVolumeChange')19+

PhonePC/2in1TabletTVWearable

off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void

取消监听当前应用的应用级音量变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'appVolumeChange'，当取消监听当前应用的应用级音量变化事件时，触发该事件。 |
| callback | Callback<[VolumeEvent](arkts-apis-audio-i.md#volumeevent9)> | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioVolumeManager.off('appVolumeChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
6. console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
7. console.info(`Volume level: ${volumeEvent.volume} `);
8. console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
9. };

11. audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);

13. audioVolumeManager.off('appVolumeChange', appVolumeChangeCallback);
```

## getVolumeByStream20+

PhonePC/2in1TabletTVWearable

getVolumeByStream(streamUsage: StreamUsage): number

获取指定音频流的音量。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 需要获取音量值的音频流。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 音量值。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 获取指定音频流的音量值。
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { audio } from '@kit.AudioKit'

5. try {
6. let volume : number = audio.getAudioManager().getVolumeManager().getVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
7. console.info(`Obtains the volume of a stream success.`);
8. } catch (err) {
9. let error = err as BusinessError;
10. console.error(`Failed to obtains the volume of a stream, error: ${error}`);
11. }
```

## getMinVolumeByStream20+

PhonePC/2in1TabletTVWearable

getMinVolumeByStream(streamUsage: StreamUsage): number

获取指定音频流的最小音量。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 需要获取的最小音量值的音频流。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 音量值。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 获取指定音频流的最小音量。
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { audio } from '@kit.AudioKit'

5. try {
6. let volume : number = audio.getAudioManager().getVolumeManager().getMinVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
7. console.info(`Obtains the minimum volume allowed for a stream success.`);
8. } catch (err) {
9. let error = err as BusinessError;
10. console.error(`Failed to obtains the minimum volume allowed for a stream, error: ${error}`);
11. }
```

## getMaxVolumeByStream20+

PhonePC/2in1TabletTVWearable

getMaxVolumeByStream(streamUsage: StreamUsage): number

获取指定音频流的最大音量。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 需要获取的最大音量值的音频流。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 音量值。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 获取指定音频流的最大音量。
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { audio } from '@kit.AudioKit'

5. try {
6. let volume : number = audio.getAudioManager().getVolumeManager().getMaxVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
7. console.info(`Obtains the maximum volume allowed for a stream success.`);
8. } catch (err) {
9. let error = err as BusinessError;
10. console.error(`Failed to obtains the maximum volume allowed for a stream, error: ${error}`);
11. }
```

## isSystemMutedForStream20+

PhonePC/2in1TabletTVWearable

isSystemMutedForStream(streamUsage: StreamUsage): boolean

检查指定音频流是否静音。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 检查是否为静音的音频流。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 音频流是否为静音状态，true表示音频流已静音，false表示音频流未静音。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 检查指定音频流是否静音。
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { audio } from '@kit.AudioKit'

5. try {
6. let isMuted : boolean = audio.getAudioManager().getVolumeManager().isSystemMutedForStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
7. console.info(`Checks whether the system is muted based on the stream success.`);
8. } catch (err) {
9. let error = err as BusinessError;
10. console.error(`Failed to checks whether the system is muted based on the stream, error: ${error}`);
11. }
```

## getVolumeInUnitOfDbByStream20+

PhonePC/2in1TabletTVWearable

getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number

获取系统通过音频流、音量等级和设备类型计算出的音量dB值。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](arkts-apis-audio-e.md#devicetype) | 是 | 设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 音频流的音量dB值。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 获取系统通过音频流、音量等级和设备类型计算出的音量dB值。
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { audio } from '@kit.AudioKit'

5. try {
6. let volumeInDb : number = audio.getAudioManager().getVolumeManager().getVolumeInUnitOfDbByStream(audio.StreamUsage.STREAM_USAGE_MUSIC, 5, audio.DeviceType.SPEAKER);
7. console.info(`Gets the volume db value that system calculate by volume stream, volume level and device type.
8. success.`);
9. } catch (err) {
10. let error = err as BusinessError;
11. console.error(`Failed to gets the volume db value that system calculate by volume stream, volume level and device type., error: ${error}`);
12. }
```

## on('streamVolumeChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void

监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'streamVolumeChange'，当系统音量发生变化时，触发该事件。 |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流使用类型。 |
| callback | Callback<[StreamVolumeEvent](arkts-apis-audio-i.md#streamvolumeevent20)> | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
2. console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
3. console.info(`Volume level: ${streamVolumeEvent.volume} `);
4. console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
5. });
```

## off('streamVolumeChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void

取消监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'streamVolumeChange'，当取消监听系统音量变化事件时，触发该事件。 |
| callback | Callback<[StreamVolumeEvent](arkts-apis-audio-i.md#streamvolumeevent20)> | 否 | 回调函数，返回变化后的音量信息。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioVolumeManager.off('streamVolumeChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let streamVolumeChangeCallback = (streamVolumeEvent: audio.StreamVolumeEvent) => {
6. console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
7. console.info(`Volume level: ${streamVolumeEvent.volume} `);
8. console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
9. };

11. audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, streamVolumeChangeCallback);

13. audioVolumeManager.off('streamVolumeChange', streamVolumeChangeCallback);
```
