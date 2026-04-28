---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager
title: Interface (AudioSessionManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioSessionManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d2952058d68b38e480a1ef4ad75a13e3f91789c87b0919499d419fe6f6e0030
---

音频会话管理。

在使用AudioSessionManager的接口之前，需先通过[getSessionManager](arkts-apis-audio-audiomanager.md#getsessionmanager12)获取AudioSessionManager实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## activateAudioSession12+

PhonePC/2in1TabletTVWearable

activateAudioSession(strategy: AudioSessionStrategy): Promise<void>

激活音频会话。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-apis-audio-i.md#audiosessionstrategy12) | 是 | 音频会话策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800301 | System error. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let strategy: audio.AudioSessionStrategy = {
4. concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
5. };

7. audioSessionManager.activateAudioSession(strategy).then(() => {
8. console.info('activateAudioSession SUCCESS');
9. }).catch((err: BusinessError) => {
10. console.error(`ERROR: ${err}`);
11. });
```

## deactivateAudioSession12+

PhonePC/2in1TabletTVWearable

deactivateAudioSession(): Promise<void>

停用音频会话。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | System error. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioSessionManager.deactivateAudioSession().then(() => {
4. console.info('deactivateAudioSession SUCCESS');
5. }).catch((err: BusinessError) => {
6. console.error(`ERROR: ${err}`);
7. });
```

## isAudioSessionActivated12+

PhonePC/2in1TabletTVWearable

isAudioSessionActivated(): boolean

检查音频会话是否已激活。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 音频会话是否处于激活状态。true表示已激活，false表示已停用。 |

**示例：**

```
1. let isActivated = audioSessionManager.isAudioSessionActivated();
```

## on('audioSessionDeactivated')12+

PhonePC/2in1TabletTVWearable

on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void

监听音频会话停用事件（当音频会话停用时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionDeactivated'，当音频会话停用时，触发该事件。 |
| callback | Callback<[AudioSessionDeactivatedEvent](arkts-apis-audio-i.md#audiosessiondeactivatedevent12)> | 是 | 回调函数，返回音频会话停用原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioSessionManager.on('audioSessionDeactivated',
2. (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
3. console.info(`reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} `);
4. });
```

## off('audioSessionDeactivated')12+

PhonePC/2in1TabletTVWearable

off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void

取消监听音频会话停用事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionDeactivated'，当取消监听音频会话停用事件时，触发该事件。 |
| callback | Callback<[AudioSessionDeactivatedEvent](arkts-apis-audio-i.md#audiosessiondeactivatedevent12)> | 否 | 回调函数，返回音频会话停用原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioSessionManager.off('audioSessionDeactivated');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let audioSessionDeactivatedCallback = (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
6. console.info(`reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} `);
7. };

9. audioSessionManager.on('audioSessionDeactivated', audioSessionDeactivatedCallback);

11. audioSessionManager.off('audioSessionDeactivated', audioSessionDeactivatedCallback);
```

## setAudioSessionScene20+

PhonePC/2in1TabletTVWearable

setAudioSessionScene(scene: AudioSessionScene): void

设置音频会话场景参数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | [AudioSessionScene](arkts-apis-audio-e.md#audiosessionscene20) | 是 | 音频会话场景。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO_SESSION_SCENE_MEDIA);
```

## on('audioSessionStateChanged')20+

PhonePC/2in1TabletTVWearable

on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void

监听音频会话状态变更事件（当音频会话焦点变更时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | Callback<[AudioSessionStateChangedEvent](arkts-apis-audio-i.md#audiosessionstatechangedevent20)> | 是 | 回调函数，返回音频会话变更提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. audioSessionManager.on('audioSessionStateChanged', (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
2. console.info(`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} `);
3. });
```

## off('audioSessionStateChanged')20+

PhonePC/2in1TabletTVWearable

off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void

取消监听音频会话状态变更事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | Callback<[AudioSessionStateChangedEvent](arkts-apis-audio-i.md#audiosessionstatechangedevent20)> | 否 | 回调函数，返回音频会话变更提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioSessionManager.off('audioSessionStateChanged');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let audioSessionStateChangedCallback = (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
6. console.info(`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} `);
7. };

9. audioSessionManager.on('audioSessionStateChanged', audioSessionStateChangedCallback);

11. audioSessionManager.off('audioSessionStateChanged', audioSessionStateChangedCallback);
```

## setDefaultOutputDevice20+

PhonePC/2in1TabletTVWearable

setDefaultOutputDevice(deviceType: DeviceType): Promise<void>

设置默认发声设备。使用Promise方式进行异步回调。

说明

* 本接口适用于以下情况：当设置的[AudioSessionScene](arkts-apis-audio-e.md#audiosessionscene20)为VoIP场景时，激活AudioSession后立即生效。若[AudioSessionScene](arkts-apis-audio-e.md#audiosessionscene20)为非VoIP场景，激活AudioSession时不会生效，仅在启动播放的[StreamUsage](arkts-apis-audio-e.md#streamusage)为语音消息、VoIP语音通话或VoIP视频通话时才生效。支持听筒、扬声器和系统默认设备。
* 本接口允许在AudioSessionManager创建后随时调用，系统会记录应用设置的默认本机内置发声设备。但只有激活AudioSession后才能生效。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声。否则，系统遵循应用设置的默认本机内置发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

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

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800102 | Allocate memory failed. Return by promise. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
4. console.info('setDefaultOutputDevice Success!');
5. }).catch((err: BusinessError) => {
6. console.error(`setDefaultOutputDevice Fail: ${err}`);
7. });
```

## getDefaultOutputDevice20+

PhonePC/2in1TabletTVWearable

getDefaultOutputDevice(): DeviceType

获取通过[setDefaultOutputDevice](arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)设置的默认发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DeviceType | 设备类型。  仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. Return by promise. |

**示例：**

```
1. let deviceType = audioSessionManager.getDefaultOutputDevice();
```

## on('currentOutputDeviceChanged')20+

PhonePC/2in1TabletTVWearable

on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void

监听当前输出设备变化事件（当前输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备变更时触发。 |
| callback | Callback<[CurrentOutputDeviceChangedEvent](arkts-apis-audio-i.md#currentoutputdevicechangedevent20)> | 是 | 回调函数，返回当前输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
4. console.info(`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `);
5. };

7. audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
```

## off('currentOutputDeviceChanged')20+

PhonePC/2in1TabletTVWearable

off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void

取消监听当前输出设备的变化事件，并使用callback进行异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备发生变化时，触发该事件。 |
| callback | Callback<[CurrentOutputDeviceChangedEvent](arkts-apis-audio-i.md#currentoutputdevicechangedevent20)> | 否 | 回调函数，用于返回当前输出设备变化的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioSessionManager.off('currentOutputDeviceChanged');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
6. console.info(`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `);
7. };

9. audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

11. audioSessionManager.off('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
```

## getAvailableDevices21+

PhonePC/2in1TabletTVWearable

getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors

获取音频可选设备列表。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-apis-audio-e.md#deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 返回设备列表。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
5. console.info('Succeeded in doing getAvailableDevices.');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`);
9. }
```

## on('availableDeviceChange')21+

PhonePC/2in1TabletTVWearable

on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当音频可选设备连接状态发生变化时，触发该事件。 |
| deviceUsage | [DeviceUsage](arkts-apis-audio-e.md#deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 是 | 回调函数，返回设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_INPUT_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
2. console.info('device change type : ' + deviceChanged.type);
3. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
4. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
5. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
6. });
```

## off('availableDeviceChange')21+

PhonePC/2in1TabletTVWearable

off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频可选设备连接状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当取消监听音频可选设备连接变化事件时，触发该事件。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 否 | 回调函数，返回可选设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioSessionManager.off('availableDeviceChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
6. console.info('device change type : ' + deviceChanged.type);
7. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
8. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
9. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
10. };

12. audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_INPUT_DEVICES, availableDeviceChangeCallback);

14. audioSessionManager.off('availableDeviceChange', availableDeviceChangeCallback);
```

## selectMediaInputDevice21+

PhonePC/2in1TabletTVWearable

selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>

设置媒体输入设备。使用Promise异步回调。

说明

* 本接口不适用于VoIP通话录音，即[SourceType](arkts-apis-audio-e.md#sourcetype8)为SOURCE\_TYPE\_VOICE\_COMMUNICATION的场景不适用。
* 本接口调用前需要先调用[getAvailableDevices](arkts-apis-audio-audiosessionmanager.md#getavailabledevices21)接口查询到当前可用输入设备列表，从列表中选择输入设备。
* 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。
* 应用程序可以监听[currentInputDeviceChanged](arkts-apis-audio-audiosessionmanager.md#oncurrentinputdevicechanged21)事件来获得实际的输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputAudioDevice | [AudioDeviceDescriptor](arkts-apis-audio-i.md#audiodevicedescriptor) | 是 | 媒体输入设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed, for example, the selected device does not exist. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
5. console.info('Succeeded in doing getAvailableDevices.');

7. if (data[0]) {
8. audioSessionManager.selectMediaInputDevice(data[0]).then(() => {
9. console.info('Succeeded in doing selectMediaInputDevice.');
10. }).catch((selectErr: BusinessError) => {
11. console.error(`Failed to selectMediaInputDevice. Code: ${selectErr.code}, message: ${selectErr.message}`);
12. });
13. }
14. } catch (err) {
15. let error = err as BusinessError;
16. console.error(`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`);
17. }
```

## getSelectedMediaInputDevice21+

PhonePC/2in1TabletTVWearable

getSelectedMediaInputDevice(): AudioDeviceDescriptor

获得通过[selectMediaInputDevice](arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)设置的媒体输入设备。如果没有设置，返回一个deviceType属性为INVALID的设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptor](arkts-apis-audio-i.md#audiodevicedescriptor) | 媒体输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let device: audio.AudioDeviceDescriptor = audioSessionManager.getSelectedMediaInputDevice();
5. console.info('Succeeded in doing getSelectedMediaInputDevice.');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to getSelectedMediaInputDevice. Code: ${error.code}, message: ${error.message}`);
9. }
```

## clearSelectedMediaInputDevice21+

PhonePC/2in1TabletTVWearable

clearSelectedMediaInputDevice(): Promise<void>

清空通过[selectMediaInputDevice](arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)设置的媒体输入设备。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioSessionManager.clearSelectedMediaInputDevice().then(() => {
4. console.info('Succeeded in doing clearSelectedMediaInputDevice.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to clearSelectedMediaInputDevice. Code: ${err.code}, message: ${err.message}`);
7. });
```

## setBluetoothAndNearlinkPreferredRecordCategory21+

PhonePC/2in1TabletTVWearable

setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>

设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。使用Promise异步回调。

说明

* 应用程序可以在蓝牙或星闪连接之前设置此分类，系统将在设备连接时优先使用蓝牙或星闪进行录音。
* 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。
* 应用程序可以监听[currentInputDeviceChanged](arkts-apis-audio-audiosessionmanager.md#oncurrentinputdevicechanged21)事件来获得实际的输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](arkts-apis-audio-e.md#bluetoothandnearlinkpreferredrecordcategory21) | 是 | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const category = audio.BluetoothAndNearlinkPreferredRecordCategory.PREFERRED_LOW_LATENCY;
4. audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category).then(() => {
5. console.info('Succeeded in doing setBluetoothAndNearlinkPreferredRecordCategory.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to setBluetoothAndNearlinkPreferredRecordCategory. Code: ${err.code}, message: ${err.message}`);
8. });
```

## getBluetoothAndNearlinkPreferredRecordCategory21+

PhonePC/2in1TabletTVWearable

getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory

获取通过[setBluetoothAndNearlinkPreferredRecordCategory](arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)设置的在使用蓝牙或星闪进行录音时的设备偏好分类。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothAndNearlinkPreferredRecordCategory](arkts-apis-audio-e.md#bluetoothandnearlinkpreferredrecordcategory21) | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let category: audio.BluetoothAndNearlinkPreferredRecordCategory = audioSessionManager.getBluetoothAndNearlinkPreferredRecordCategory();
5. console.info('Succeeded in doing getBluetoothAndNearlinkPreferredRecordCategory.');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to getBluetoothAndNearlinkPreferredRecordCategory. Code: ${error.code}, message: ${error.message}`);
9. }
```

## on('currentInputDeviceChanged')21+

PhonePC/2in1TabletTVWearable

on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void

监听当前输入设备变化事件（当前输入设备发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | Callback<[CurrentInputDeviceChangedEvent](arkts-apis-audio-i.md#currentinputdevicechangedevent21)> | 是 | 回调函数，返回当前输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
4. console.info(`reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `);
5. };

7. audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);
```

## off('currentInputDeviceChanged')21+

PhonePC/2in1TabletTVWearable

off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void

取消监听当前输入设备的变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | Callback<[CurrentInputDeviceChangedEvent](arkts-apis-audio-i.md#currentinputdevicechangedevent21)> | 否 | 回调函数，用于返回当前输入设备变化的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioSessionManager.off('currentInputDeviceChanged');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
6. console.info(`reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `);
7. };

9. audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);

11. audioSessionManager.off('currentInputDeviceChanged', currentInputDeviceChangedCallback);
```

## enableMuteSuggestionWhenMixWithOthers23+

PhonePC/2in1TabletTVWearable

enableMuteSuggestionWhenMixWithOthers(enable: boolean): void

启用混音播放下接收静音播放建议通知功能。

通常，当使用混音模式时，如果其他应用同时播放音频，会和其他应用进行混音播放。但在某些场景下（如游戏或广播），应用自身会通过静音自身的音频以给用户提供更好的体验。

如果启用此功能，当订阅音频会话状态更改事件后静音建议和取消静音建议提示将通过[AudioSessionStateChangedEvent](arkts-apis-audio-i.md#audiosessionstatechangedevent20)回调发送。收到静音建议表示其他应用程序开始播放音频，且播放的音频和本应用的音频不能混音。

此功能仅支持已设置[AudioSessionScene](arkts-apis-audio-e.md#audiosessionscene20)并激活模式模式为CONCURRENCY\_MIX\_WITH\_OTHERS的音频会话使用。并且仅在激活音频会话期间生效一次，每次激活音频会话前都必须重新启用。

详细说明请参考[启用混音播放下静音建议通知](../harmonyos-guides/audio-session-management.md#启用混音播放下静音建议通知)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用混音播放下接收静音播放建议通知功能。true表示启用，false表示不启用。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Function is called without setting [AudioSessionScene](arkts-apis-audio-e.md#audiosessionscene20) or called after audio session activation. |
| 6800301 | Audio client call audio service error, system internal error. |

**示例：**

```
1. audio.getAudioManager().getSessionManager().enableMuteSuggestionWhenMixWithOthers(true);
```

## isOtherMediaPlaying23+

PhonePC/2in1TabletTVWearable

isOtherMediaPlaying(): boolean

检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否有其他应用正在播放媒体类型的音频。true表示有，false表示没有。 |

**示例：**

```
1. let isExistence = audioSessionManager.isOtherMediaPlaying();
```
