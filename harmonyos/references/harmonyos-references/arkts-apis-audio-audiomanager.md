---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager
title: Interface (AudioManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioManager)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a38cae85f582fd4eaa7570cd22b7afff279d90c74ef014633a2da783aede22be
---

AudioManager是音频系统的核心管理模块。本模块提供音频系统管理能力，包括音频场景模式获取、音量控制、音频流管理、设备路由、会话管理、空间音频管理、录音管理等。开发者可通过AudioManager获取各个子管理器的实例以完成具体的音频管理任务。

在使用AudioManager的接口之前，需先通过[getAudioManager](arkts-apis-audio-f.md#audiogetaudiomanager)获取AudioManager实例。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

## getAudioScene8+

getAudioScene(callback: AsyncCallback<AudioScene>): void

获取音频场景模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | 是 | 回调函数。当获取音频场景模式成功，err为undefined，data为获取到的音频场景模式；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioScene((err: BusinessError, value: audio.AudioScene) => {
  if (err) {
    console.error(`Failed to obtain the audio scene mode. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the audio scene mode, audioScene: ${value}.`);
});
```

## getAudioScene8+

getAudioScene(): Promise<AudioScene>

获取音频场景模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | Promise对象，返回音频场景模式。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioScene().then((value: audio.AudioScene) => {
  console.info(`Succeeded in obtaining the audio scene mode, audioScene: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the audio scene mode. Code: ${err.code}, message: ${err.message}`);
});
```

## getAudioSceneSync10+

getAudioSceneSync(): AudioScene

获取音频场景模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioScene](arkts-apis-audio-e.md#audioscene8) | 音频场景模式。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioScene = audioManager.getAudioSceneSync();
  console.info(`Succeeded in obtaining the audio scene mode, audioScene: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the audio scene mode. Code: ${error.code}, message: ${error.message}`);
}
```

## on('audioSceneChange')20+

on(type: 'audioSceneChange', callback: Callback<AudioScene>): void

监听音频场景变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSceneChange'，当音频场景模式发生变化时，触发该事件。 |
| callback | Callback<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | 是 | 回调函数，返回当前音频场景模式。 |

**示例：**

```ts
audioManager.on('audioSceneChange', (audioScene: audio.AudioScene) => {
  console.info(`Audio scene changed, audioScene: ${audioScene}.`);
});
```

## off('audioSceneChange')20+

off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void

取消监听音频场景变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSceneChange'。 |
| callback | Callback<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('audioSceneChange')](arkts-apis-audio-audiomanager.md#onaudioscenechange20)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**示例：**

```ts
// 取消该事件的所有监听。
audioManager.off('audioSceneChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSceneChangeCallback = (audioScene: audio.AudioScene) => {
  console.info(`Audio scene changed, audioScene: ${audioScene}.`);
};

audioManager.on('audioSceneChange', audioSceneChangeCallback);

audioManager.off('audioSceneChange', audioSceneChangeCallback);
```

## getVolumeManager9+

getVolumeManager(): AudioVolumeManager

获取音频音量管理器。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioVolumeManager](arkts-apis-audio-audiovolumemanager.md) | 返回AudioVolumeManager实例。 |

**示例：**

```ts
let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
```

## getStreamManager9+

getStreamManager(): AudioStreamManager

获取音频流管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioStreamManager](arkts-apis-audio-audiostreammanager.md) | 返回AudioStreamManager实例。 |

**示例：**

```ts
let audioStreamManager: audio.AudioStreamManager = audioManager.getStreamManager();
```

## getRoutingManager9+

getRoutingManager(): AudioRoutingManager

获取音频路由管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRoutingManager](arkts-apis-audio-audioroutingmanager.md) | 返回AudioRoutingManager实例。 |

**示例：**

```ts
let audioRoutingManager: audio.AudioRoutingManager = audioManager.getRoutingManager();
```

## getSessionManager12+

getSessionManager(): AudioSessionManager

获取音频会话管理器。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioSessionManager](arkts-apis-audio-audiosessionmanager.md) | 返回AudioSessionManager实例。 |

**示例：**

```ts
let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
```

## getSpatializationManager18+

getSpatializationManager(): AudioSpatializationManager

获取空间音频管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioSpatializationManager](arkts-apis-audio-audiospatializationmanager.md) | 返回AudioSpatializationManager实例。 |

**示例：**

```ts
let audioSpatializationManager: audio.AudioSpatializationManager = audioManager.getSpatializationManager();
```

## getDeviceEnhanceManager()

getDeviceEnhanceManager(): AudioDeviceEnhanceManager

获取音频设备增强管理器。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceEnhanceManager](arkts-apis-audio-audiodeviceenhancemanager.md) | 返回AudioDeviceEnhanceManager实例。 |

**示例：**

```ts
let audioDeviceEnhanceManager: audio.AudioDeviceEnhanceManager = audioManager.getDeviceEnhanceManager();
```

## getDebuggingManager

getDebuggingManager(): AudioDebuggingManager

获取音频调试管理器实例。该实例为单例，获取后可重复使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDebuggingManager](arkts-apis-audio-audiodebuggingmanager.md) | 返回AudioDebuggingManager实例。 |

**示例：**

```ts
let debugManager: audio.AudioDebuggingManager = audioManager.getDebuggingManager();
```

## getRecordingManager

getRecordingManager(): AudioRecordingManager

获取录音策略管理器。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRecordingManager](arkts-apis-audio-audiorecordingmanager.md) | 返回AudioRecordingManager实例。 |

**示例：**

```ts
let audioRecordingManager: audio.AudioRecordingManager = audioManager.getRecordingManager();
```

## setAudioParameter(deprecated)

setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void

音频参数设置。使用callback异步回调。

接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。

**说明** 

从API version 7开始支持，从API version 11开始废弃。

**需要权限：** ohos.permission.MODIFY\_AUDIO\_SETTINGS

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 被设置的音频参数的键。 |
| value | string | 是 | 被设置的音频参数的值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频参数设置成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setAudioParameter('key_example', 'value_example', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the audio parameter. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the audio parameter.');
});
```

## setAudioParameter(deprecated)

setAudioParameter(key: string, value: string): Promise<void>

音频参数设置。使用Promise异步回调。

接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。

**说明** 

从API version 7开始支持，从API version 11开始废弃。

**需要权限：** ohos.permission.MODIFY\_AUDIO\_SETTINGS

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 被设置的音频参数的键。 |
| value | string | 是 | 被设置的音频参数的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setAudioParameter('key_example', 'value_example').then(() => {
  console.info('Succeeded in setting the audio parameter.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the audio parameter. Code: ${err.code}, message: ${err.message}`);
});
```

## getAudioParameter(deprecated)

getAudioParameter(key: string, callback: AsyncCallback<string>): void

获取指定音频参数值。使用callback异步回调。

本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。

**说明** 

从API version 7开始支持，从API version 11开始废弃。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待获取的音频参数的键。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取指定音频参数值成功，err为undefined，data为获取到的指定音频参数值；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioParameter('key_example', (err: BusinessError, value: string) => {
  if (err) {
    console.error(`Failed to obtain the audio parameter. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the audio parameter, value: ${value}.`);
});
```

## getAudioParameter(deprecated)

getAudioParameter(key: string): Promise<string>

获取指定音频参数值。使用Promise异步回调。

本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。

**说明** 

从API version 7开始支持，从API version 11开始废弃。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待获取的音频参数的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回获取的音频参数值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getAudioParameter('key_example').then((value: string) => {
  console.info(`Succeeded in obtaining the audio parameter, value: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the audio parameter. Code: ${err.code}, message: ${err.message}`);
});
```

## setVolume(deprecated)

setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void

设置指定流的音量等级。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[AVVolumePanel](ohos-multimedia-avvolumepanel.md#avvolumepanel)替代。

**需要权限：** ohos.permission.ACCESS\_NOTIFICATION\_POLICY

仅设置铃声（即volumeType为AudioVolumeType.RINGTONE）在静音和非静音状态切换时需要该权限。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| volume | number | 是 | 音量等级，可设置范围通过[getMinVolume](arkts-apis-audio-audiomanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiomanager.md#getmaxvolumedeprecated)获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置指定流的音量成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the volume.');
});
```

## setVolume(deprecated)

setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>

设置指定流的音量等级。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[AVVolumePanel](ohos-multimedia-avvolumepanel.md#avvolumepanel)替代。

**需要权限：** ohos.permission.ACCESS\_NOTIFICATION\_POLICY

仅设置铃声（即volumeType为AudioVolumeType.RINGTONE）在静音和非静音状态切换时需要该权限。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| volume | number | 是 | 音量等级，可设置范围通过[getMinVolume](arkts-apis-audio-audiomanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiomanager.md#getmaxvolumedeprecated)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Succeeded in setting the volume.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the volume. Code: ${err.code}, message: ${err.message}`);
});
```

## getVolume(deprecated)

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的音量等级。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getVolume](arkts-apis-audio-audiovolumegroupmanager.md#getvolumedeprecated)替代；API version 20及以后，建议使用[getVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通过[getMinVolume](arkts-apis-audio-audiomanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiomanager.md#getmaxvolumedeprecated)获取。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the volume, volume: ${value}.`);
});
```

## getVolume(deprecated)

getVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的音量等级。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getVolume](arkts-apis-audio-audiovolumegroupmanager.md#getvolumedeprecated)替代；API version 20及以后，建议使用[getVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](arkts-apis-audio-audiomanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiomanager.md#getmaxvolumedeprecated)获取。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in obtaining the volume, volume: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the volume. Code: ${err.code}, message: ${err.message}`);
});
```

## getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最小音量等级。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getMinVolume](arkts-apis-audio-audiovolumegroupmanager.md#getminvolumedeprecated)替代；API version 20及以后，建议使用[getMinVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the minimum volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the minimum volume, minVolume: ${value}.`);
});
```

## getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最小音量等级。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getMinVolume](arkts-apis-audio-audiovolumegroupmanager.md#getminvolumedeprecated)替代；API version 20及以后，建议使用[getMinVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)替代。

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in obtaining the minimum volume, minVolume: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the minimum volume. Code: ${err.code}, message: ${err.message}`);
});
```

## getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最大音量等级。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getMaxVolume](arkts-apis-audio-audiovolumegroupmanager.md#getmaxvolumedeprecated)替代；API version 20及以后，建议使用[getMaxVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the maximum volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the maximum volume, maxVolume: ${value}.`);
});
```

## getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最大音量等级。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getMaxVolume](arkts-apis-audio-audiovolumegroupmanager.md#getmaxvolumedeprecated)替代；API version 20及以后，建议使用[getMaxVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)替代。

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((data: number) => {
  console.info(`Succeeded in obtaining the maximum volume, maxVolume: ${data}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the maximum volume. Code: ${err.code}, message: ${err.message}`);
});
```

## mute(deprecated)

mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void

设置指定音量流静音。使用callback异步回调。

当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[AVVolumePanel](ohos-multimedia-avvolumepanel.md#avvolumepanel)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| mute | boolean | 是 | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置指定音量流静音成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.mute(audio.AudioVolumeType.MEDIA, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the stream. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in muting the stream.');
});
```

## mute(deprecated)

mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>

设置指定音量流静音。使用Promise异步回调。

当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[AVVolumePanel](ohos-multimedia-avvolumepanel.md#avvolumepanel)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| mute | boolean | 是 | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.mute(audio.AudioVolumeType.MEDIA, true).then(() => {
  console.info('Succeeded in muting the stream.');
}).catch((err: BusinessError) => {
  console.error(`Failed to mute the stream. Code: ${err.code}, message: ${err.message}`);
});
```

## isMute(deprecated)

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流的静音状态。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[isMute](arkts-apis-audio-audiovolumegroupmanager.md#ismutedeprecated)替代；API version 20及以后，建议使用[isSystemMutedForStream](arkts-apis-audio-audiovolumemanager.md#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音量流的静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to check whether the stream is muted. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in checking whether the stream is muted, isMuted: ${value}.`);
});
```

## isMute(deprecated)

isMute(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流的静音状态。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[isMute](arkts-apis-audio-audiovolumegroupmanager.md#ismutedeprecated)替代；API version 20及以后，建议使用[isSystemMutedForStream](arkts-apis-audio-audiovolumemanager.md#issystemmutedforstream20)替代。

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Succeeded in checking whether the stream is muted, isMuted: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the stream is muted. Code: ${err.code}, message: ${err.message}`);
});
```

## isActive(deprecated)

isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流的活跃状态。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[isActive](arkts-apis-audio-audiostreammanager.md#isactivedeprecated)替代；API version 20及以后，建议使用[isStreamActive](arkts-apis-audio-audiostreammanager.md#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音量流的活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to check whether the stream is active. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in checking whether the stream is active, isActive: ${value}.`);
});
```

## isActive(deprecated)

isActive(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流的活跃状态。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[isActive](arkts-apis-audio-audiostreammanager.md#isactivedeprecated)替代；API version 20及以后，建议使用[isStreamActive](arkts-apis-audio-audiostreammanager.md#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示流状态为活跃；返回false表示流状态不活跃。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Succeeded in checking whether the stream is active, isActive: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the stream is active. Code: ${err.code}, message: ${err.message}`);
});
```

## setRingerMode(deprecated)

setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void

设置铃声模式。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.ACCESS\_NOTIFICATION\_POLICY

仅在静音和非静音状态切换时需要该权限。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioRingMode](arkts-apis-audio-e.md#audioringmode) | 是 | 音频铃声模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置铃声模式成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the ringer mode. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the ringer mode.');
});
```

## setRingerMode(deprecated)

setRingerMode(mode: AudioRingMode): Promise<void>

设置铃声模式。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.ACCESS\_NOTIFICATION\_POLICY

仅在静音和非静音状态切换时需要该权限。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioRingMode](arkts-apis-audio-e.md#audioringmode) | 是 | 音频铃声模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL).then(() => {
  console.info('Succeeded in setting the ringer mode.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the ringer mode. Code: ${err.code}, message: ${err.message}`);
});
```

## getRingerMode(deprecated)

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

获取铃声模式。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[getRingerMode](arkts-apis-audio-audiovolumegroupmanager.md#getringermode9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | 是 | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(`Failed to obtain the ringer mode. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the ringer mode, ringerMode: ${value}.`);
});
```

## getRingerMode(deprecated)

getRingerMode(): Promise<AudioRingMode>

获取铃声模式。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[getRingerMode](arkts-apis-audio-audiovolumegroupmanager.md#getringermode9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | Promise对象，返回系统的铃声模式。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(`Succeeded in obtaining the ringer mode, ringerMode: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the ringer mode. Code: ${err.code}, message: ${err.message}`);
});
```

## getDevices(deprecated)

getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void

获取音频设备列表。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[getDevices](arkts-apis-audio-audioroutingmanager.md#getdevices9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-apis-audio-e.md#deviceflag) | 是 | 音频设备类型。 |
| callback | AsyncCallback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数。当获取音频设备列表成功，err为undefined，data为获取到的音频设备列表；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (err: BusinessError, value: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(`Failed to obtain the device list. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the device list, devices: ${JSON.stringify(value)}.`);
});
```

## getDevices(deprecated)

getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>

获取音频设备列表。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[getDevices](arkts-apis-audio-audioroutingmanager.md#getdevices9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-apis-audio-e.md#deviceflag) | 是 | 音频设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | Promise对象，返回设备列表。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((data: audio.AudioDeviceDescriptors) => {
  console.info(`Succeeded in obtaining the device list, devices: ${JSON.stringify(data)}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the device list. Code: ${err.code}, message: ${err.message}`);
});
```

## setDeviceActive(deprecated)

setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void

设置设备激活状态。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[setCommunicationDevice](arkts-apis-audio-audioroutingmanager.md#setcommunicationdevice9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-apis-audio-e.md#activedevicetypedeprecated) | 是 | 活跃音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置设备激活状态成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set the active status of the device. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the active status of the device.');
});
```

## setDeviceActive(deprecated)

setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>

设置设备激活状态。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[setCommunicationDevice](arkts-apis-audio-audioroutingmanager.md#setcommunicationdevice9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-apis-audio-e.md#activedevicetypedeprecated) | 是 | 活跃音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true).then(() => {
  console.info('Succeeded in setting the active status of the device.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set the active status of the device. Code: ${err.code}, message: ${err.message}`);
});
```

## isDeviceActive(deprecated)

isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void

获取指定设备的激活状态。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[isCommunicationDeviceActive](arkts-apis-audio-audioroutingmanager.md#iscommunicationdeviceactive9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-apis-audio-e.md#activedevicetypedeprecated) | 是 | 活跃音频设备类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定设备的激活状态成功，err为undefined，data为true表示激活，false表示未激活；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to check whether the device is active. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in checking whether the device is active, isActive: ${value}.`);
});
```

## isDeviceActive(deprecated)

isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>

获取指定设备的激活状态。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[isCommunicationDeviceActive](arkts-apis-audio-audioroutingmanager.md#iscommunicationdeviceactive9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-apis-audio-e.md#activedevicetypedeprecated) | 是 | 活跃音频设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示设备已激活；返回false表示设备未激活。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER).then((value: boolean) => {
  console.info(`Succeeded in checking whether the device is active, isActive: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the device is active. Code: ${err.code}, message: ${err.message}`);
});
```

## setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

设置麦克风静音状态。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the microphone. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in muting the microphone.');
});
```

## setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean): Promise<void>

设置麦克风静音状态。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.setMicrophoneMute(true).then(() => {
  console.info('Succeeded in muting the microphone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to mute the microphone. Code: ${err.code}, message: ${err.message}`);
});
```

## isMicrophoneMute(deprecated)

isMicrophoneMute(callback: AsyncCallback<boolean>): void

获取麦克风静音状态。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[isMicrophoneMute](arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to check whether the microphone is muted. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in checking whether the microphone is muted, isMuted: ${value}.`);
});
```

## isMicrophoneMute(deprecated)

isMicrophoneMute(): Promise<boolean>

获取麦克风静音状态。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[isMicrophoneMute](arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioManager.isMicrophoneMute().then((value: boolean) => {
  console.info(`Succeeded in checking whether the microphone is muted, isMuted: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to check whether the microphone is muted. Code: ${err.code}, message: ${err.message}`);
});
```

## on('deviceChange')(deprecated)

on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void

监听音频设备连接变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[on('deviceChange')](arkts-apis-audio-audioroutingmanager.md#ondevicechange9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当音频设备连接状态发生变化时，触发该事件。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 是 | 回调函数，返回设备更新详情。 |

**示例：**

```ts
audioManager.on('deviceChange', (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`Device changed, deviceChanged: ${JSON.stringify(deviceChanged)}.`);
});
```

## off('deviceChange')(deprecated)

off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频设备连接变化事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[off('deviceChange')](arkts-apis-audio-audioroutingmanager.md#offdevicechange9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('deviceChange')](arkts-apis-audio-audiomanager.md#ondevicechangedeprecated)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**示例：**

```ts
// 取消该事件的所有监听。
audioManager.off('deviceChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`Device changed, deviceChanged: ${JSON.stringify(deviceChanged)}.`);
};

audioManager.on('deviceChange', deviceChangeCallback);

audioManager.off('deviceChange', deviceChangeCallback);
```

## on('interrupt')(deprecated)

on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void

监听音频打断事件（当音频焦点发生变化时触发）。使用callback异步回调。

与[on('audioInterrupt')](arkts-apis-audio-audiorenderer.md#onaudiointerrupt9)作用一致，均用于监听焦点变化。为无音频流的场景（未曾创建AudioRenderer对象），比如FM、语音唤醒等提供焦点变化监听功能。

**说明** 

从API version 7开始支持，从API version 11开始废弃，建议使用[on('audioInterrupt')](arkts-apis-audio-audiocapturer.md#onaudiointerrupt10)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'interrupt'，当音频焦点状态发生变化时，触发该事件。 |
| interrupt | [AudioInterrupt](arkts-apis-audio-i.md#audiointerruptdeprecated) | 是 | 音频打断事件类型的参数。 |
| callback | Callback<[InterruptAction](arkts-apis-audio-i.md#interruptactiondeprecated)> | 是 | 回调函数，返回打断事件信息。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

let interAudioInterrupt: audio.AudioInterrupt = {
  streamUsage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
  contentType: audio.ContentType.CONTENT_TYPE_UNKNOWN,
  pauseWhenDucked: true
};

audioManager.on('interrupt', interAudioInterrupt, (interruptAction: audio.InterruptAction) => {
  console.info(`Interrupt changed, interruptAction: ${JSON.stringify(interruptAction)}.`);
});
```

## off('interrupt')(deprecated)

off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void

取消监听音频打断事件。

**说明** 

从API version 7开始支持，从API version 11开始废弃，建议使用[off('audioInterrupt')](arkts-apis-audio-audiocapturer.md#offaudiointerrupt10)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'interrupt'。 |
| interrupt | [AudioInterrupt](arkts-apis-audio-i.md#audiointerruptdeprecated) | 是 | 音频打断事件类型的参数。 |
| callback | Callback<[InterruptAction](arkts-apis-audio-i.md#interruptactiondeprecated)> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('interrupt')](arkts-apis-audio-audiomanager.md#oninterruptdeprecated)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

let interAudioInterrupt: audio.AudioInterrupt = {
  streamUsage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
  contentType: audio.ContentType.CONTENT_TYPE_UNKNOWN,
  pauseWhenDucked: true
};

// 取消该事件的所有监听。
audioManager.off('interrupt', interAudioInterrupt);

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let interruptCallback = (interruptAction: audio.InterruptAction) => {
  console.info(`Interrupt changed, interruptAction: ${JSON.stringify(interruptAction)}.`);
};

audioManager.on('interrupt', interAudioInterrupt, interruptCallback);

audioManager.off('interrupt', interAudioInterrupt, interruptCallback);
```
