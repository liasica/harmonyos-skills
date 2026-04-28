---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager
title: Interface (AudioManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:372828796a3721d4be181ccc81115b16d2ce1692c7ac405f8b595cfeeacd1670
---

音频音量和设备管理。

在使用AudioManager的接口之前，需先通过[getAudioManager](arkts-apis-audio-f.md#audiogetaudiomanager)获取AudioManager实例。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## getAudioScene8+

PhonePC/2in1TabletTVWearable

getAudioScene(callback: AsyncCallback<AudioScene>): void

获取音频场景模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | 是 | 回调函数。当获取音频场景模式成功，err为undefined，data为获取到的音频场景模式；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getAudioScene((err: BusinessError, value: audio.AudioScene) => {
4. if (err) {
5. console.error(`Failed to obtain the audio scene mode. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the audio scene mode is obtained ${value}.`);
9. });
```

## getAudioScene8+

PhonePC/2in1TabletTVWearable

getAudioScene(): Promise<AudioScene>

获取音频场景模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | Promise对象，返回音频场景模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getAudioScene().then((value: audio.AudioScene) => {
4. console.info(`Promise returned to indicate that the audio scene mode is obtained ${value}.`);
5. }).catch ((err: BusinessError) => {
6. console.error(`Failed to obtain the audio scene mode ${err}`);
7. });
```

## getAudioSceneSync10+

PhonePC/2in1TabletTVWearable

getAudioSceneSync(): AudioScene

获取音频场景模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioScene](arkts-apis-audio-e.md#audioscene8) | 音频场景模式。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let value: audio.AudioScene = audioManager.getAudioSceneSync();
5. console.info(`indicate that the audio scene mode is obtained ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to obtain the audio scene mode ${error}`);
9. }
```

## on('audioSceneChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'audioSceneChange', callback: Callback<AudioScene>): void

监听音频场景变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSceneChange'，当音频场景模式发生变化时，触发该事件。 |
| callback | Callback<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | 是 | 回调函数，返回当前音频场景模式。 |

**示例：**

```
1. audioManager.on('audioSceneChange', (audioScene: audio.AudioScene) => {
2. console.info(`audio scene : ${audioScene}.`);
3. });
```

## off('audioSceneChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void

取消监听音频场景变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSceneChange'，当取消监听当前音频场景变化事件时，触发该事件。 |
| callback | Callback<[AudioScene](arkts-apis-audio-e.md#audioscene8)> | 否 | 回调函数，返回当前音频场景模式。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioManager.off('audioSceneChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let audioSceneChangeCallback = (audioScene: audio.AudioScene) => {
6. console.info(`audio scene : ${audioScene}.`);
7. };

9. audioManager.on('audioSceneChange', audioSceneChangeCallback);

11. audioManager.off('audioSceneChange', audioSceneChangeCallback);
```

## getVolumeManager9+

PhonePC/2in1TabletTVWearable

getVolumeManager(): AudioVolumeManager

获取音频音量管理器。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioVolumeManager](arkts-apis-audio-audiovolumemanager.md) | AudioVolumeManager实例。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
```

## getStreamManager9+

PhonePC/2in1TabletTVWearable

getStreamManager(): AudioStreamManager

获取音频流管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioStreamManager](arkts-apis-audio-audiostreammanager.md) | AudioStreamManager实例。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioStreamManager: audio.AudioStreamManager = audioManager.getStreamManager();
```

## getRoutingManager9+

PhonePC/2in1TabletTVWearable

getRoutingManager(): AudioRoutingManager

获取音频路由管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioRoutingManager](arkts-apis-audio-audioroutingmanager.md) | AudioRoutingManager实例。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioRoutingManager: audio.AudioRoutingManager = audioManager.getRoutingManager();
```

## getSessionManager12+

PhonePC/2in1TabletTVWearable

getSessionManager(): AudioSessionManager

获取音频会话管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioSessionManager](arkts-apis-audio-audiosessionmanager.md) | AudioSessionManager实例。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
```

## getSpatializationManager18+

PhonePC/2in1TabletTV

getSpatializationManager(): AudioSpatializationManager

获取空间音频管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioSpatializationManager](arkts-apis-audio-audiospatializationmanager.md) | AudioSpatializationManager实例。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';
2. let audioSpatializationManager: audio.AudioSpatializationManager = audioManager.getSpatializationManager();
```

## setAudioParameter(deprecated)

PhonePC/2in1TabletTVWearable

setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void

音频参数设置。使用callback异步回调。

接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。

说明

从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MODIFY\_AUDIO\_SETTINGS

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 被设置的音频参数的键。 |
| value | string | 是 | 被设置的音频参数的值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当音频参数设置成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.setAudioParameter('key_example', 'value_example', (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set the audio parameter. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate a successful setting of the audio parameter.');
9. });
```

## setAudioParameter(deprecated)

PhonePC/2in1TabletTVWearable

setAudioParameter(key: string, value: string): Promise<void>

音频参数设置。使用Promise异步回调。

接口根据硬件设备的支持能力扩展音频配置。支持的参数与产品和设备强相关，非通用参数，示例代码内使用样例参数。

说明

从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

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

```
1. audioManager.setAudioParameter('key_example', 'value_example').then(() => {
2. console.info('Promise returned to indicate a successful setting of the audio parameter.');
3. });
```

## getAudioParameter(deprecated)

PhonePC/2in1TabletTVWearable

getAudioParameter(key: string, callback: AsyncCallback<string>): void

获取指定音频参数值。使用callback异步回调。

本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。

说明

从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待获取的音频参数的键。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取指定音频参数值成功，err为undefined，data为获取到的指定音频参数值；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getAudioParameter('key_example', (err: BusinessError, value: string) => {
4. if (err) {
5. console.error(`Failed to obtain the value of the audio parameter. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the value of the audio parameter is obtained ${value}.`);
9. });
```

## getAudioParameter(deprecated)

PhonePC/2in1TabletTVWearable

getAudioParameter(key: string): Promise<string>

获取指定音频参数值。使用Promise异步回调。

本接口的使用场景为：根据硬件设备的支持能力扩展音频配置。在不同的设备平台上，所支持的音频参数会存在差异。示例代码内使用样例参数，实际支持的音频配置参数见具体设备平台的资料描述。

说明

从API version 7开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

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

```
1. audioManager.getAudioParameter('key_example').then((value: string) => {
2. console.info(`Promise returned to indicate that the value of the audio parameter is obtained ${value}.`);
3. });
```

## setVolume(deprecated)

PhonePC/2in1TabletTVWearable

setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void

设置指定流的音量等级。使用callback异步回调。

说明

* 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。
* 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请查看API文档：[音量面板](ohos-multimedia-avvolumepanel.md)。

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set the volume. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate a successful volume setting.');
9. });
```

## setVolume(deprecated)

PhonePC/2in1TabletTVWearable

setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>

设置指定流的音量等级。使用Promise异步回调。

说明

* 从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。
* 应用无法直接调节系统音量，建议通过系统音量面板组件调节音量。具体样例和介绍请查看API文档：[音量面板](ohos-multimedia-avvolumepanel.md)。

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

```
1. audioManager.setVolume(audio.AudioVolumeType.MEDIA, 10).then(() => {
2. console.info('Promise returned to indicate a successful volume setting.');
3. });
```

## getVolume(deprecated)

PhonePC/2in1TabletTVWearable

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的音量等级。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getVolume](arkts-apis-audio-audiovolumegroupmanager.md#getvolumedeprecated)替代；API version 20及以后，建议使用[getVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通过[getMinVolume](arkts-apis-audio-audiomanager.md#getminvolumedeprecated)和[getMaxVolume](arkts-apis-audio-audiomanager.md#getmaxvolumedeprecated)获取。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to obtain the volume. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the volume is obtained.');
9. });
```

## getVolume(deprecated)

PhonePC/2in1TabletTVWearable

getVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的音量等级。使用Promise异步回调。

说明

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

```
1. audioManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
2. console.info(`Promise returned to indicate that the volume is obtained ${value} .`);
3. });
```

## getMinVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最小音量等级。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getMinVolume](arkts-apis-audio-audiovolumegroupmanager.md#getminvolumedeprecated)替代；API version 20及以后，建议使用[getMinVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to obtain the minimum volume. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the minimum volume is obtained. ${value}`);
9. });
```

## getMinVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMinVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最小音量等级。使用Promise异步回调。

说明

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

```
1. audioManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
2. console.info(`Promised returned to indicate that the minimum volume is obtained. ${value}`);
3. });
```

## getMaxVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最大音量等级。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[getMaxVolume](arkts-apis-audio-audiovolumegroupmanager.md#getmaxvolumedeprecated)替代；API version 20及以后，建议使用[getMaxVolumeByStream](arkts-apis-audio-audiovolumemanager.md#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
4. if (err) {
5. console.error(`Failed to obtain the maximum volume. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the maximum volume is obtained. ${value}`);
9. });
```

## getMaxVolume(deprecated)

PhonePC/2in1TabletTVWearable

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最大音量等级。使用Promise异步回调。

说明

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

```
1. audioManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((data: number) => {
2. console.info('Promised returned to indicate that the maximum volume is obtained.');
3. });
```

## mute(deprecated)

PhonePC/2in1TabletTVWearable

mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void

设置指定音量流静音。使用callback异步回调。

当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| mute | boolean | 是 | 是否设置指定音量流为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置指定音量流静音成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.mute(audio.AudioVolumeType.MEDIA, true, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to mute the stream. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the stream is muted.');
9. });
```

## mute(deprecated)

PhonePC/2in1TabletTVWearable

mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>

设置指定音量流静音。使用Promise异步回调。

当该音量流可设置的最小音量不能为0时，不支持静音操作。例如：闹钟和通话。

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

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

```
1. audioManager.mute(audio.AudioVolumeType.MEDIA, true).then(() => {
2. console.info('Promise returned to indicate that the stream is muted.');
3. });
```

## isMute(deprecated)

PhonePC/2in1TabletTVWearable

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流的静音状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[isMute](arkts-apis-audio-audiovolumegroupmanager.md#ismutedeprecated)替代；API version 20及以后，建议使用[isSystemMutedForStream](arkts-apis-audio-audiovolumemanager.md#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音量流的静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to obtain the mute status. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the mute status of the stream is obtained. ${value}`);
9. });
```

## isMute(deprecated)

PhonePC/2in1TabletTVWearable

isMute(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流的静音状态。使用Promise异步回调。

说明

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

```
1. audioManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
2. console.info(`Promise returned to indicate that the mute status of the stream is obtained ${value}.`);
3. });
```

## isActive(deprecated)

PhonePC/2in1TabletTVWearable

isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流的活跃状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。在API version 9-19建议使用[isActive](arkts-apis-audio-audiostreammanager.md#isactivedeprecated)替代；API version 20及以后，建议使用[isStreamActive](arkts-apis-audio-audiostreammanager.md#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音量流的活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
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

获取指定音量流的活跃状态。使用Promise异步回调。

说明

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

```
1. audioManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
2. console.info(`Promise returned to indicate that the active status of the stream is obtained ${value}.`);
3. });
```

## setRingerMode(deprecated)

PhonePC/2in1TabletTVWearable

setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void

设置铃声模式。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.ACCESS\_NOTIFICATION\_POLICY

仅在静音和非静音状态切换时需要该权限。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AudioRingMode](arkts-apis-audio-e.md#audioringmode) | 是 | 音频铃声模式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置铃声模式成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set the ringer mode. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate a successful setting of the ringer mode.');
9. });
```

## setRingerMode(deprecated)

PhonePC/2in1TabletTVWearable

setRingerMode(mode: AudioRingMode): Promise<void>

设置铃声模式。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

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

```
1. audioManager.setRingerMode(audio.AudioRingMode.RINGER_MODE_NORMAL).then(() => {
2. console.info('Promise returned to indicate a successful setting of the ringer mode.');
3. });
```

## getRingerMode(deprecated)

PhonePC/2in1TabletTVWearable

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

获取铃声模式。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getRingerMode](arkts-apis-audio-audiovolumegroupmanager.md#getringermode9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | 是 | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
4. if (err) {
5. console.error(`Failed to obtain the ringer mode. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the ringer mode is obtained ${value}.`);
9. });
```

## getRingerMode(deprecated)

PhonePC/2in1TabletTVWearable

getRingerMode(): Promise<AudioRingMode>

获取铃声模式。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getRingerMode](arkts-apis-audio-audiovolumegroupmanager.md#getringermode9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioRingMode](arkts-apis-audio-e.md#audioringmode)> | Promise对象，返回系统的铃声模式。 |

**示例：**

```
1. audioManager.getRingerMode().then((value: audio.AudioRingMode) => {
2. console.info(`Promise returned to indicate that the ringer mode is obtained ${value}.`);
3. });
```

## getDevices(deprecated)

PhonePC/2in1TabletTVWearable

getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void

获取音频设备列表。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getDevices](arkts-apis-audio-audioroutingmanager.md#getdevices9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-apis-audio-e.md#deviceflag) | 是 | 音频设备类型。 |
| callback | AsyncCallback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数。当获取音频设备列表成功，err为undefined，data为获取到的音频设备列表；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (err: BusinessError, value: audio.AudioDeviceDescriptors) => {
4. if (err) {
5. console.error(`Failed to obtain the device list. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the device list is obtained.');
9. });
```

## getDevices(deprecated)

PhonePC/2in1TabletTVWearable

getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>

获取音频设备列表。使用Promise异步回调。

说明

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

```
1. audioManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((data: audio.AudioDeviceDescriptors) => {
2. console.info('Promise returned to indicate that the device list is obtained.');
3. });
```

## setDeviceActive(deprecated)

PhonePC/2in1TabletTVWearable

setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void

设置设备激活状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[setCommunicationDevice](arkts-apis-audio-audioroutingmanager.md#setcommunicationdevice9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-apis-audio-e.md#activedevicetypedeprecated) | 是 | 活跃音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示已激活，false表示未激活。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置设备激活状态成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set the active status of the device. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the device is set to the active status.');
9. });
```

## setDeviceActive(deprecated)

PhonePC/2in1TabletTVWearable

setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>

设置设备激活状态。使用Promise异步回调。

说明

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

```
1. audioManager.setDeviceActive(audio.ActiveDeviceType.SPEAKER, true).then(() => {
2. console.info('Promise returned to indicate that the device is set to the active status.');
3. });
```

## isDeviceActive(deprecated)

PhonePC/2in1TabletTVWearable

isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void

获取指定设备的激活状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[isCommunicationDeviceActive](arkts-apis-audio-audioroutingmanager.md#iscommunicationdeviceactive9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [ActiveDeviceType](arkts-apis-audio-e.md#activedevicetypedeprecated) | 是 | 活跃音频设备类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定设备的激活状态成功，err为undefined，data为true表示激活，false表示未激活；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER, (err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to obtain the active status of the device. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the active status of the device is obtained.');
9. });
```

## isDeviceActive(deprecated)

PhonePC/2in1TabletTVWearable

isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>

获取指定设备的激活状态。使用Promise异步回调。

说明

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

```
1. audioManager.isDeviceActive(audio.ActiveDeviceType.SPEAKER).then((value: boolean) => {
2. console.info(`Promise returned to indicate that the active status of the device is obtained ${value}.`);
3. });
```

## setMicrophoneMute(deprecated)

PhonePC/2in1TabletTVWearable

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

设置麦克风静音状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.setMicrophoneMute(true, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to mute the microphone. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the microphone is muted.');
9. });
```

## setMicrophoneMute(deprecated)

PhonePC/2in1TabletTVWearable

setMicrophoneMute(mute: boolean): Promise<void>

设置麦克风静音状态。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅面向系统应用开放。

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

```
1. audioManager.setMicrophoneMute(true).then(() => {
2. console.info('Promise returned to indicate that the microphone is muted.');
3. });
```

## isMicrophoneMute(deprecated)

PhonePC/2in1TabletTVWearable

isMicrophoneMute(callback: AsyncCallback<boolean>): void

获取麦克风静音状态。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[isMicrophoneMute](arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to obtain the mute status of the microphone. ${err}`);
6. return;
7. }
8. console.info(`Callback invoked to indicate that the mute status of the microphone is obtained ${value}.`);
9. });
```

## isMicrophoneMute(deprecated)

PhonePC/2in1TabletTVWearable

isMicrophoneMute(): Promise<boolean>

获取麦克风静音状态。使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[isMicrophoneMute](arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |

**示例：**

```
1. audioManager.isMicrophoneMute().then((value: boolean) => {
2. console.info(`Promise returned to indicate that the mute status of the microphone is obtained ${value}.`);
3. });
```

## on('deviceChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void

监听音频设备连接变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[on('deviceChange')](arkts-apis-audio-audioroutingmanager.md#ondevicechange9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当音频设备连接状态发生变化时，触发该事件。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 是 | 回调函数，返回设备更新详情。 |

**示例：**

```
1. audioManager.on('deviceChange', (deviceChanged: audio.DeviceChangeAction) => {
2. console.info(`device change type : ${deviceChanged.type} `);
3. console.info(`device descriptor size : ${deviceChanged.deviceDescriptors.length} `);
4. console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceRole} `);
5. console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceType} `);
6. });
```

## off('deviceChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频设备连接变化事件。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[off('deviceChange')](arkts-apis-audio-audioroutingmanager.md#offdevicechange9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当取消监听音频设备连接变化事件时，触发该事件。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 否 | 回调函数，返回设备更新详情。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioManager.off('deviceChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
6. console.info(`device change type : ${deviceChanged.type} `);
7. console.info(`device descriptor size : ${deviceChanged.deviceDescriptors.length} `);
8. console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceRole} `);
9. console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceType} `);
10. };

12. audioManager.on('deviceChange', deviceChangeCallback);

14. audioManager.off('deviceChange', deviceChangeCallback);
```

## on('interrupt')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void

监听音频打断事件（当音频焦点发生变化时触发）。使用callback异步回调。

与[on('audioInterrupt')](arkts-apis-audio-audiorenderer.md#onaudiointerrupt9)作用一致，均用于监听焦点变化。为无音频流的场景（未曾创建AudioRenderer对象），比如FM、语音唤醒等提供焦点变化监听功能。

说明

从API version 7开始支持，从API version 11开始废弃，建议使用[on('audioInterrupt')](arkts-apis-audio-audiocapturer.md#onaudiointerrupt10)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'interrupt'，当音频焦点状态发生变化时，触发该事件。 |
| interrupt | [AudioInterrupt](arkts-apis-audio-i.md#audiointerruptdeprecated) | 是 | 音频打断事件类型的参数。 |
| callback | Callback<[InterruptAction](arkts-apis-audio-i.md#interruptactiondeprecated)> | 是 | 回调函数，返回打断事件信息。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let interAudioInterrupt: audio.AudioInterrupt = {
4. streamUsage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
5. contentType: audio.ContentType.CONTENT_TYPE_UNKNOWN,
6. pauseWhenDucked: true
7. };

9. audioManager.on('interrupt', interAudioInterrupt, (interruptAction: audio.InterruptAction) => {
10. if (interruptAction.actionType === 0) {
11. console.info('An event to gain the audio focus starts.');
12. console.info(`Focus hint: ${interruptAction.hint} `);
13. }
14. if (interruptAction.actionType === 1) {
15. console.info('An audio interruption event starts.');
16. console.info(`Audio interruption hint: ${interruptAction.hint} `);
17. }
18. });
```

## off('interrupt')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void

取消监听音频打断事件。使用callback异步回调。

说明

从API version 7开始支持，从API version 11开始废弃，建议使用[off('audioInterrupt')](arkts-apis-audio-audiocapturer.md#offaudiointerrupt10)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'interrupt'，当取消监听音频打断事件时，触发该事件。 |
| interrupt | [AudioInterrupt](arkts-apis-audio-i.md#audiointerruptdeprecated) | 是 | 音频打断事件类型的参数。 |
| callback | Callback<[InterruptAction](arkts-apis-audio-i.md#interruptactiondeprecated)> | 否 | 回调函数，返回打断事件信息。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let interAudioInterrupt: audio.AudioInterrupt = {
4. streamUsage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
5. contentType: audio.ContentType.CONTENT_TYPE_UNKNOWN,
6. pauseWhenDucked: true
7. };

9. // 取消该事件的所有监听。
10. audioManager.off('interrupt', interAudioInterrupt);

12. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
13. let interruptCallback = (interruptAction: audio.InterruptAction) => {
14. if (interruptAction.actionType === 0) {
15. console.info('An event to gain the audio focus starts.');
16. console.info(`Focus hint: ${interruptAction.hint} `);
17. }
18. if (interruptAction.actionType === 1) {
19. console.info('An audio interruption event starts.');
20. console.info(`Audio interruption hint: ${interruptAction.hint} `);
21. }
22. };

24. audioManager.on('interrupt', interAudioInterrupt, interruptCallback);

26. audioManager.off('interrupt', interAudioInterrupt, interruptCallback);
```
