---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager
title: Interface (AudioVolumeGroupManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioVolumeGroupManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:42+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:0d587e7c013bcadb097a93990dc60e30a1a8ae7a838faa14897bb706b2547d19
---

管理音频组音量。

在使用AudioVolumeGroupManager的接口之前，需先通过[getVolumeGroupManager](arkts-apis-audio-audiovolumemanager.md#getvolumegroupmanager9)获取AudioVolumeGroupManager实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## getVolume(deprecated)

PhonePC/2in1TabletTVWearable

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的音量等级。使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通过[getMinVolume](arkts-apis-audio-audiovolumegroupmanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiovolumegroupmanager.md#getmaxvolumedeprecated)获取。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to get volume. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in getting volume. Volume: ${value}.`);
9. });
```

## getVolume(deprecated)

PhonePC/2in1TabletTVWearable

getVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的音量等级。使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](arkts-apis-audio-audiovolumegroupmanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiovolumegroupmanager.md#getmaxvolumedeprecated)获取。 |

**示例：**

```
1. audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
2. console.info(`Succeeded in getting volume. Volume: ${value}.`);
3. });
```

## getVolumeSync(deprecated)

PhonePC/2in1TabletTVWearable

getVolumeSync(volumeType: AudioVolumeType): number

获取指定流的音量等级。同步返回结果。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](arkts-apis-audio-audiovolumegroupmanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiovolumegroupmanager.md#getmaxvolumedeprecated)获取。 |

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
4. let value: number = audioVolumeGroupManager.getVolumeSync(audio.AudioVolumeType.MEDIA);
5. console.info(`Succeeded in getting volume. Volume: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get volume. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getMinVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最小音量等级。使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to get minVolume. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
9. });
```

## getMinVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMinVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最小音量等级。使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回最小音量等级。 |

**示例：**

```
1. audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
2. console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
3. });
```

## getMinVolumeSync(deprecated)

PhonePC/2in1TabletTVWearable

getMinVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最小音量等级。同步返回结果。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回最小音量等级。 |

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
4. let value: number = audioVolumeGroupManager.getMinVolumeSync(audio.AudioVolumeType.MEDIA);
5. console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get minVolume. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getMaxVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最大音量等级。使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to get maxVolume. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
9. });
```

## getMaxVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最大音量等级。使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回最大音量等级。 |

**示例：**

```
1. audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
2. console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
3. });
```

## getMaxVolumeSync(deprecated)

PhonePC/2in1TabletTVWearable

getMaxVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最大音量等级。同步返回结果。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回最大音量等级。 |

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
4. let value: number = audioVolumeGroupManager.getMaxVolumeSync(audio.AudioVolumeType.MEDIA);
5. console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get maxVolume. Code: ${error.code}, message: ${error.message}`);
9. }
```

## isMute(deprecated)

PhonePC/2in1TabletTVWearable

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流静音状态。使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](arkts-apis-audio-audiovolumemanager.md#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音量流静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to use isMute function. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
9. });
```

## isMute(deprecated)

PhonePC/2in1TabletTVWearable

isMute(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流是否被静音。使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](arkts-apis-audio-audiovolumemanager.md#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示静音；返回false表示非静音。 |

**示例：**

```
1. audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
2. console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
3. });
```

## isMuteSync(deprecated)

PhonePC/2in1TabletTVWearable

isMuteSync(volumeType: AudioVolumeType): boolean

获取指定音量流是否被静音。同步返回结果。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](arkts-apis-audio-audiovolumemanager.md#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 流静音状态。返回true表示静音，返回false表示非静音。 |

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
4. let value: boolean = audioVolumeGroupManager.isMuteSync(audio.AudioVolumeType.MEDIA);
5. console.info(`Succeeded in using isMuteSync function. MuteState: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to use isMuteSync function. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getRingerMode9+

PhonePC/2in1TabletTVWearable

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

获取铃声模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | 是 | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
4. if (err) {
5. console.error(`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
9. });
```

## getRingerMode9+

PhonePC/2in1TabletTVWearable

getRingerMode(): Promise<AudioRingMode>

获取铃声模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | Promise对象，返回系统的铃声模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getRingerMode().then((value: audio.AudioRingMode) => {
4. console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getRingerModeSync10+

PhonePC/2in1TabletTVWearable

getRingerModeSync(): AudioRingMode

获取铃声模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRingMode](arkts-apis-audio-e.md#audioringmode) | 返回系统的铃声模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: audio.AudioRingMode = audioVolumeGroupManager.getRingerModeSync();
5. console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get ringerMode. Code: ${error.code}, message: ${error.message}`);
9. }
```

## on('ringerModeChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void

监听铃声模式变化事件（当[AudioRingMode](arkts-apis-audio-e.md#audioringmode)发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'ringerModeChange'，当铃声模式发生变化时，触发该事件。 |
| callback | Callback<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | 是 | 回调函数，返回变化后的铃音模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioVolumeGroupManager.on('ringerModeChange', (ringerMode: audio.AudioRingMode) => {
2. console.info(`Succeeded in using on function. AudioRingMode: ${ringerMode}.`);
3. });
```

## off('ringerModeChange')18+

PhonePC/2in1TabletTVWearable

off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void

取消监听铃声模式变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'ringerModeChange'，当取消监听铃声模式变化事件时，触发该事件。 |
| callback | Callback<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | 否 | 回调函数，返回变化后的铃音模式。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioVolumeGroupManager.off('ringerModeChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let ringerModeChangeCallback = (ringerMode: audio.AudioRingMode) => {
6. console.info(`Succeeded in using on or off function. AudioRingMode: ${ringerMode}.`);
7. };

9. audioVolumeGroupManager.on('ringerModeChange', ringerModeChangeCallback);

11. audioVolumeGroupManager.off('ringerModeChange', ringerModeChangeCallback);
```

## isMicrophoneMute9+

PhonePC/2in1TabletTVWearable

isMicrophoneMute(callback: AsyncCallback<boolean>): void

获取麦克风静音状态。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in using isMicrophoneMute function. MuteState: ${value}.`);
9. });
```

## isMicrophoneMute9+

PhonePC/2in1TabletTVWearable

isMicrophoneMute(): Promise<boolean>

获取麦克风静音状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
4. console.info(`Succeeded in using isMicrophoneMute function. MuteState: ${value}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`);
7. });
```

## isMicrophoneMuteSync10+

PhonePC/2in1TabletTVWearable

isMicrophoneMuteSync(): boolean

获取麦克风静音状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 系统麦克风静音状态。返回true表示静音，返回false表示非静音。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: boolean = audioVolumeGroupManager.isMicrophoneMuteSync();
5. console.info(`Succeeded in using isMicrophoneMuteSync function. MuteState: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to use isMicrophoneMuteSync function. Code: ${error.code}, message: ${error.message}`);
9. }
```

## on('micStateChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void

监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发）。使用callback异步回调。

目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅）。因此，推荐使用单一AudioManager实例进行开发。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'micStateChange'，当检测到系统麦克风状态发生改变时，触发该事件。 |
| callback | Callback<[MicStateChangeEvent](arkts-apis-audio-i.md#micstatechangeevent9)> | 是 | 回调函数，返回变更后的麦克风状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
2. console.info(`Succeeded in using on function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.`);
3. });
```

## off('micStateChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void

取消监听系统麦克风状态更改事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'micStateChange'，当取消监听系统麦克风状态更改事件时，触发该事件。 |
| callback | Callback<[MicStateChangeEvent](arkts-apis-audio-i.md#micstatechangeevent9)> | 否 | 回调函数，返回变更后的麦克风状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioVolumeGroupManager.off('micStateChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let micStateChangeCallback = (micStateChange: audio.MicStateChangeEvent) => {
6. console.info(`Succeeded in using on or off function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.`);
7. };

9. audioVolumeGroupManager.on('micStateChange', micStateChangeCallback);

11. audioVolumeGroupManager.off('micStateChange', micStateChangeCallback);
```

## isVolumeUnadjustable10+

PhonePC/2in1TabletTVWearable

isVolumeUnadjustable(): boolean

获取固定音量模式开关状态，打开时进入固定音量模式，此时音量固定无法被调节。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 固定音量模式开关状态。返回true表示固定音量模式，返回false表示非固定音量模式。 |

**示例：**

```
1. let volumeAdjustSwitch: boolean = audioVolumeGroupManager.isVolumeUnadjustable();
2. console.info(`Succeeded in using isVolumeUnadjustable function. VolumeUnadjustable: ${volumeAdjustSwitch}.`);
```

## getSystemVolumeInDb(deprecated)

PhonePC/2in1TabletTVWearable

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void

获取音量增益dB值。使用callback异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](arkts-apis-audio-audiovolumemanager.md#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](arkts-apis-audio-e.md#devicetype) | 是 | 设备类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音量增益dB值成功，err为undefined，data为获取到的音量增益dB值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |
| 6800301 | System error. Return by callback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
8. }
9. });
```

## getSystemVolumeInDb(deprecated)

PhonePC/2in1TabletTVWearable

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>

获取音量增益dB值。使用Promise异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](arkts-apis-audio-audiovolumemanager.md#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](arkts-apis-audio-e.md#devicetype) | 是 | 设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回对应的音量增益dB值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER).then((value: number) => {
4. console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getSystemVolumeInDbSync(deprecated)

PhonePC/2in1TabletTVWearable

getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number

获取音量增益dB值。同步返回结果。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](arkts-apis-audio-audiovolumemanager.md#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](arkts-apis-audio-e.md#devicetype) | 是 | 设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回对应的音量增益dB值。 |

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
4. let value: number = audioVolumeGroupManager.getSystemVolumeInDbSync(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER);
5. console.info(`Succeeded in getting system volume in db sync. DB: ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get system volume in db sync. Code: ${error.code}, message: ${error.message}`);
9. }
```

## getMaxAmplitudeForInputDevice12+

PhonePC/2in1TabletTVWearable

getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>

获取输入设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](arkts-apis-audio-i.md#audiodevicedescriptor) | 是 | 获取最大电平值的设备信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回对应设备的电平值，大小在[0, 1]之间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let capturerInfo: audio.AudioCapturerInfo = {
4. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
5. capturerFlags: 0 // 音频采集器标志。
6. };

8. audio.getAudioManager().getRoutingManager().getPreferredInputDeviceForCapturerInfo(capturerInfo).then((data) => {
9. audioVolumeGroupManager.getMaxAmplitudeForInputDevice(data[0]).then((value) => {
10. console.info(`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`);
13. })
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
16. })
```

## getMaxAmplitudeForOutputDevice12+

PhonePC/2in1TabletTVWearable

getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>

获取输出设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outputDevice | [AudioDeviceDescriptor](arkts-apis-audio-i.md#audiodevicedescriptor) | 是 | 获取最大电平值的设备信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回对应设备的电平值，大小在[0, 1]之间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let rendererInfo: audio.AudioRendererInfo = {
4. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
5. rendererFlags: 0 // 音频渲染器标志。
6. };

8. audio.getAudioManager().getRoutingManager().getPreferOutputDeviceForRendererInfo(rendererInfo).then((data) => {
9. audioVolumeGroupManager.getMaxAmplitudeForOutputDevice(data[0]).then((value) => {
10. console.info(`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`);
13. })
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
16. })
```

## setMicrophoneMute(deprecated)

PhonePC/2in1TabletTVWearable

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

设置麦克风静音状态。使用callback异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_AUDIO\_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioVolumeGroupManager.setMicrophoneMute(true, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set microphone mute. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in setting microphone mute.');
9. });
```

## setMicrophoneMute(deprecated)

PhonePC/2in1TabletTVWearable

setMicrophoneMute(mute: boolean): Promise<void>

设置麦克风静音状态。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_AUDIO\_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. audioVolumeGroupManager.setMicrophoneMute(true).then(() => {
2. console.info('Succeeded in setting microphone mute.');
3. });
```
