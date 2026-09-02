---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager
title: Interface (AudioVolumeManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioVolumeManager)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2ad7b13318463206ea1ad3b56ca7f6e4405b5fe3558b0ff71103c55d3c666dfd
---

AudioVolumeManager是音频系统中的音量管理模块。本模块提供音频音量管理能力，包括获取和设置应用级音量、获取音频流音量及音量范围、监听系统和应用级音量变化等。当需要精确控制应用音量或响应系统音量变化时，使用本模块接口完成相关操作。

在使用AudioVolumeManager的接口之前，需先通过[getVolumeManager](arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

**说明** 

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

## getVolumeGroupManager9+

getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void

获取音频组音量管理器实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | number | 是 | 音量组ID，默认使用DEFAULT\_VOLUME\_GROUP\_ID。 |
| callback | AsyncCallback<[AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md)> | 是 | 回调函数。当获取音频组音量管理器实例成功，err为undefined，data为获取到的音频组音量管理器实例；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;
let audioVolumeGroupManager: audio.AudioVolumeGroupManager;

audioVolumeManager.getVolumeGroupManager(groupId, (err: BusinessError, value: audio.AudioVolumeGroupManager) => {
  if (err) {
    console.error(`Failed to obtain the volume group manager. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  audioVolumeGroupManager = value;
  console.info('Succeeded in obtaining the volume group manager.');
});
```

## getVolumeGroupManager9+

getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>

获取音频组音量管理器实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | number | 是 | 音量组ID，默认使用DEFAULT\_VOLUME\_GROUP\_ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise< [AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md) > | Promise对象，返回音频组音量管理器实例。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;
let audioVolumeGroupManager: audio.AudioVolumeGroupManager;

audioVolumeManager.getVolumeGroupManager(groupId).then((value: audio.AudioVolumeGroupManager) => {
  audioVolumeGroupManager = value;
  console.info('Succeeded in obtaining the volume group manager.');
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the volume group manager. Code: ${err.code}, message: ${err.message}`);
});
```

## getVolumeGroupManagerSync10+

getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager

获取音频组音量管理器实例。同步返回结果。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | number | 是 | 音量组ID，默认使用DEFAULT\_VOLUME\_GROUP\_ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md) | 音频组音量管理器实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioVolumeGroupManager: audio.AudioVolumeGroupManager = audioVolumeManager.getVolumeGroupManagerSync(audio.DEFAULT_VOLUME_GROUP_ID);
  console.info('Succeeded in obtaining the volume group manager.');
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume group manager. Code: ${error.code}, message: ${error.message}`);
}
```

## getAppVolumePercentage19+

getAppVolumePercentage(): Promise<number>

获取应用的音量（范围为[0, 100]）。使用Promise异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回应用的音量。  取值范围为[0, 100]，单位为百分号（%）。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeManager.getAppVolumePercentage().then((value: number) => {
  console.info(`Succeeded in obtaining the app volume percentage, appVolumePercentage: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the app volume percentage. Code: ${err.code}, message: ${err.message}`);
});
```

## setAppVolumePercentage19+

setAppVolumePercentage(volume: number): Promise<void>

设置应用的音量（范围为[0, 100]）。使用Promise异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 要设置的音量值。  取值范围为[0, 100]，单位为百分号（%）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Crash or blocking occurs in system process. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeManager.setAppVolumePercentage(20).then(() => {
  console.info('Succeeded in setting the app volume percentage.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the app volume percentage. Code: ${err.code}, message: ${err.message}`);
});
```

## on('volumeChange')(deprecated)

on(type: 'volumeChange', callback: Callback<VolumeEvent>): void

监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。

**说明** 

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

```ts
audioVolumeManager.on('volumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(`Volume changed, volumeEvent: ${JSON.stringify(volumeEvent)}.`);
});
```

## off('volumeChange')(deprecated)

off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void

取消监听系统音量变化事件。

**说明** 

从API version 12开始支持，从API version 20开始废弃，建议使用[off('streamVolumeChange')](arkts-apis-audio-audiovolumemanager.md#offstreamvolumechange20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'volumeChange'。 |
| callback | Callback<[VolumeEvent](arkts-apis-audio-i.md#volumeevent9)> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('volumeChange')](arkts-apis-audio-audiovolumemanager.md#onvolumechangedeprecated)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 取消该事件的所有监听。
audioVolumeManager.off('volumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let volumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`Volume changed, volumeEvent: ${JSON.stringify(volumeEvent)}.`);
};

audioVolumeManager.on('volumeChange', volumeChangeCallback);

audioVolumeManager.off('volumeChange', volumeChangeCallback);
```

## on('appVolumeChange')19+

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

```ts
audioVolumeManager.on('appVolumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(`App volume changed, appVolumeEvent: ${JSON.stringify(volumeEvent)}.`);
});
```

## off('appVolumeChange')19+

off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void

取消监听当前应用的应用级音量变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'appVolumeChange'。 |
| callback | Callback<[VolumeEvent](arkts-apis-audio-i.md#volumeevent9)> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('appVolumeChange')](arkts-apis-audio-audiovolumemanager.md#onappvolumechange19)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 取消该事件的所有监听。
audioVolumeManager.off('appVolumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`App volume changed, appVolumeEvent: ${JSON.stringify(volumeEvent)}.`);
};

audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);

audioVolumeManager.off('appVolumeChange', appVolumeChangeCallback);
```

## getVolumeByStream20+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取指定音频流的音量值。
try {
  let volume: number = audio.getAudioManager().getVolumeManager().getVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Succeeded in obtaining the volume by stream, volume: ${volume}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume by stream. Code: ${error.code}, message: ${error.message}`);
}
```

## getMinVolumeByStream20+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取指定音频流的最小音量。
try {
  let volume: number = audio.getAudioManager().getVolumeManager().getMinVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Succeeded in obtaining the minimum volume by stream, minVolume: ${volume}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the minimum volume by stream. Code: ${error.code}, message: ${error.message}`);
}
```

## getMaxVolumeByStream20+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取指定音频流的最大音量。
try {
  let volume: number = audio.getAudioManager().getVolumeManager().getMaxVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Succeeded in obtaining the maximum volume by stream, maxVolume: ${volume}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the maximum volume by stream. Code: ${error.code}, message: ${error.message}`);
}
```

## isSystemMutedForStream20+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 检查指定音频流是否静音。
try {
  let isMuted: boolean = audio.getAudioManager().getVolumeManager().isSystemMutedForStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Succeeded in checking whether the system is muted for the stream, isMuted: ${isMuted}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to check whether the system is muted for the stream. Code: ${error.code}, message: ${error.message}`);
}
```

## getVolumeInUnitOfDbByStream20+

getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number

获取系统通过音频流、音量等级和设备类型计算出的音量dB值。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流类型。 |
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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 获取系统通过音频流、音量等级和设备类型计算出的音量dB值。
try {
  let volumeInDb: number = audio.getAudioManager().getVolumeManager().getVolumeInUnitOfDbByStream(audio.StreamUsage.STREAM_USAGE_MUSIC, 5, audio.DeviceType.SPEAKER);
  console.info(`Succeeded in obtaining the volume in dB by stream, volumeInDb: ${volumeInDb}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume in dB by stream. Code: ${error.code}, message: ${error.message}`);
}
```

## on('streamVolumeChange')20+

on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void

监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'streamVolumeChange'，当系统音量发生变化时，触发该事件。 |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 需要监听音量变化的音频流类型。 |
| callback | Callback<[StreamVolumeEvent](arkts-apis-audio-i.md#streamvolumeevent20)> | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(`Stream volume changed, streamVolumeEvent: ${JSON.stringify(streamVolumeEvent)}.`);
});
```

## off('streamVolumeChange')20+

off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void

取消监听系统音频流音量变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'streamVolumeChange'。 |
| callback | Callback<[StreamVolumeEvent](arkts-apis-audio-i.md#streamvolumeevent20)> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('streamVolumeChange')](arkts-apis-audio-audiovolumemanager.md#onstreamvolumechange20)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**示例：**

```ts
// 取消该事件的所有监听。
audioVolumeManager.off('streamVolumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let streamVolumeChangeCallback = (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(`Stream volume changed, streamVolumeEvent: ${JSON.stringify(streamVolumeEvent)}.`);
};

audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, streamVolumeChangeCallback);

audioVolumeManager.off('streamVolumeChange', streamVolumeChangeCallback);
```
