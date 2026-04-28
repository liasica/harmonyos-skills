---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager
title: Interface (AudioRoutingManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioRoutingManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5d38a01a2000417226cd3c1432d1071b7e678c8c87f4a3588f92a48ad954bd3c
---

音频路由管理。

在使用AudioRoutingManager的接口之前，需先通过[getRoutingManager](arkts-apis-audio-audiomanager.md#getroutingmanager9)获取AudioRoutingManager实例。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 9开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## getDevices9+

PhonePC/2in1TabletTVWearable

getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void

获取音频设备列表。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-apis-audio-e.md#deviceflag) | 是 | 音频设备类型。 |
| callback | AsyncCallback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数。当获取音频设备列表成功，err为undefined，data为获取到的音频设备列表；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
4. if (err) {
5. console.error(`Failed to get devices. Code: ${err.code}, message: ${err.message}`);
6. } else {
7. console.info(`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
8. }
9. });
```

## getDevices9+

PhonePC/2in1TabletTVWearable

getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>

获取音频设备列表。使用Promise异步回调。

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
4. console.info(`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to get devices. Code: ${err.code}, message: ${err.message}`);
7. });
```

## getDevicesSync10+

PhonePC/2in1TabletTVWearable

getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors

获取音频设备列表。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceFlag | [DeviceFlag](arkts-apis-audio-e.md#deviceflag) | 是 | 音频设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 返回设备列表。 |

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
4. let audioDeviceDescriptors = audioRoutingManager.getDevicesSync(audio.DeviceFlag.OUTPUT_DEVICES_FLAG);
5. console.info(`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to get devices. Code: ${error.code}, message: ${error.message}`);
9. }
```

## isMicBlockDetectionSupported13+

PhonePC/2in1TabletTVWearable

isMicBlockDetectionSupported(): Promise<boolean>

获取当前设备是否支持麦克风状态检测。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持；返回false表示不支持。 |

**示例：**

```
1. audioRoutingManager.isMicBlockDetectionSupported().then((value: boolean) => {
2. console.info(`Query whether microphone block detection is supported on current device result is ${value}.`);
3. });
```

## on('micBlockStatusChanged')13+

PhonePC/2in1TabletTVWearable

on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void

监听麦克风堵塞状态变化事件。使用callback异步回调。

使用此功能前，请查询设备是否支持检测。应用在使用麦克风录音时，若麦克风堵塞状态发生变化，将触发该事件。目前此检测功能仅支持麦克风位于本地设备上。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'micBlockStatusChanged'，当麦克风堵塞状态发生变化时，触发该事件。 |
| callback | Callback<[DeviceBlockStatusInfo](arkts-apis-audio-i.md#deviceblockstatusinfo13)> | 是 | 回调函数，返回麦克风被堵塞状态和设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 在使用此功能之前，应先查询当前设备是否支持检测。
2. audioRoutingManager.isMicBlockDetectionSupported().then((value: boolean) => {
3. console.info(`Query whether microphone block detection is supported on current device result is ${value}.`);
4. if (value) {
5. audioRoutingManager.on('micBlockStatusChanged', (micBlockStatusChanged: audio.DeviceBlockStatusInfo) => {
6. console.info(`block status : ${micBlockStatusChanged.blockStatus} `);
7. });
8. }
9. });
```

## off('micBlockStatusChanged')13+

PhonePC/2in1TabletTVWearable

off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void

取消监听麦克风堵塞状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'micBlockStatusChanged'，当取消监听音频麦克风是否被堵塞变化事件时，触发该事件。 |
| callback | Callback<[DeviceBlockStatusInfo](arkts-apis-audio-i.md#deviceblockstatusinfo13)> | 否 | 回调函数，返回麦克风被堵塞状态和设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRoutingManager.off('micBlockStatusChanged');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let micBlockStatusCallback = (micBlockStatusChanged: audio.DeviceBlockStatusInfo) => {
6. console.info(`block status : ${micBlockStatusChanged.blockStatus} `);
7. };

9. audioRoutingManager.on('micBlockStatusChanged', micBlockStatusCallback);

11. audioRoutingManager.off('micBlockStatusChanged', micBlockStatusCallback);
```

## on('deviceChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'deviceChange', deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void

监听音频设备连接状态变化事件（当音频设备连接状态发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当音频设备连接状态发生变化时，触发该事件。 |
| deviceFlag | [DeviceFlag](arkts-apis-audio-e.md#deviceflag) | 是 | 音频设备类型。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 是 | 回调函数，返回设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (deviceChanged: audio.DeviceChangeAction) => {
2. console.info('device change type : ' + deviceChanged.type);
3. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
4. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
5. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
6. });
```

## off('deviceChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频设备连接状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'deviceChange'，当取消监听音频设备连接变化事件时，触发该事件。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 否 | 回调函数，返回设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRoutingManager.off('deviceChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
6. console.info('device change type : ' + deviceChanged.type);
7. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
8. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
9. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
10. };

12. audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG, deviceChangeCallback);

14. audioRoutingManager.off('deviceChange', deviceChangeCallback);
```

## setCommunicationDevice9+

PhonePC/2in1TabletTVWearable

setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean, callback: AsyncCallback<void>): void

设置通信设备激活状态。使用callback异步回调。

该接口由于功能设计变化，将在后续版本废弃，不建议开发者使用。

推荐使用AVSession提供的[设备切换组件](../harmonyos-guides/using-switch-call-devices.md)，实现通话设备切换。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-apis-audio-e.md#communicationdevicetype9) | 是 | 音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示激活，false表示未激活。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置通信设备激活状态成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRoutingManager.setCommunicationDevice(audio.CommunicationDeviceType.SPEAKER, true, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to set the active status of the device. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the device is set to the active status.');
9. });
```

## getAvailableDevices12+

PhonePC/2in1TabletTVWearable

getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors

获取音频可选设备列表。同步返回结果。

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

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let data: audio.AudioDeviceDescriptors = audioRoutingManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
5. console.info('Succeeded in doing getAvailableDevices.');
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`);
9. }
```

## on('availableDeviceChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当音频可选设备连接状态发生变化时，触发该事件。 |
| deviceUsage | [DeviceUsage](arkts-apis-audio-e.md#deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 是 | 回调函数，返回设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioRoutingManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_OUTPUT_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
2. console.info('device change type : ' + deviceChanged.type);
3. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
4. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
5. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
6. });
```

## off('availableDeviceChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频可选设备连接状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当取消监听音频可选设备连接变化事件时，触发该事件。 |
| callback | Callback<[DeviceChangeAction](arkts-apis-audio-i.md#devicechangeaction)> | 否 | 回调函数，返回可选设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioRoutingManager.off('availableDeviceChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
6. console.info('device change type : ' + deviceChanged.type);
7. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
8. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
9. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
10. };

12. audioRoutingManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_OUTPUT_DEVICES, availableDeviceChangeCallback);

14. audioRoutingManager.off('availableDeviceChange', availableDeviceChangeCallback);
```

## setCommunicationDevice9+

PhonePC/2in1TabletTVWearable

setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean): Promise<void>

设置通信设备激活状态。使用Promise异步回调。

该接口由于功能设计变化，将在后续版本废弃，不建议开发者使用。

推荐开发者使用AVSession提供的[设备切换组件](../harmonyos-guides/using-switch-call-devices.md)，实现通话设备切换。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-apis-audio-e.md#communicationdevicetype9) | 是 | 活跃音频设备类型。 |
| active | boolean | 是 | 是否设置设备为激活状态。true表示激活，false表示未激活。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. audioRoutingManager.setCommunicationDevice(audio.CommunicationDeviceType.SPEAKER, true).then(() => {
2. console.info('Promise returned to indicate that the device is set to the active status.');
3. });
```

## isCommunicationDeviceActive9+

PhonePC/2in1TabletTVWearable

isCommunicationDeviceActive(deviceType: CommunicationDeviceType, callback: AsyncCallback<boolean>): void

获取指定通信设备的激活状态。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-apis-audio-e.md#communicationdevicetype9) | 是 | 活跃音频设备类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定通信设备的激活状态成功，err为undefined，data为true表示激活，false表示未激活；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioRoutingManager.isCommunicationDeviceActive(audio.CommunicationDeviceType.SPEAKER, (err: BusinessError, value: boolean) => {
4. if (err) {
5. console.error(`Failed to obtain the active status of the device. ${err}`);
6. return;
7. }
8. console.info('Callback invoked to indicate that the active status of the device is obtained.');
9. });
```

## isCommunicationDeviceActive9+

PhonePC/2in1TabletTVWearable

isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Promise<boolean>

获取指定通信设备的激活状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-apis-audio-e.md#communicationdevicetype9) | 是 | 活跃音频设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示设备已激活；返回false表示设备未激活。 |

**示例：**

```
1. audioRoutingManager.isCommunicationDeviceActive(audio.CommunicationDeviceType.SPEAKER).then((value: boolean) => {
2. console.info(`Promise returned to indicate that the active status of the device is obtained ${value}.`);
3. });
```

## isCommunicationDeviceActiveSync10+

PhonePC/2in1TabletTVWearable

isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean

获取指定通信设备的激活状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-apis-audio-e.md#communicationdevicetype9) | 是 | 活跃音频设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设备是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。 |

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
4. let value: boolean = audioRoutingManager.isCommunicationDeviceActiveSync(audio.CommunicationDeviceType.SPEAKER);
5. console.info(`Indicate that the active status of the device is obtained ${value}.`);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`Failed to obtain the active status of the device ${error}.`);
9. }
```

## getPreferOutputDeviceForRendererInfo10+

PhonePC/2in1TabletTVWearable

getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void

根据音频信息，返回优先级最高的输出设备。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 音频渲染器信息。 |
| callback | AsyncCallback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数。当获取优先级最高的输出设备成功，err为undefined，data为获取到的优先级最高的输出设备信息；否则为错误对象。 |

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

3. let rendererInfo: audio.AudioRendererInfo = {
4. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
5. rendererFlags: 0 // 音频渲染器标志。
6. };

8. audioRoutingManager.getPreferOutputDeviceForRendererInfo(rendererInfo, (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
9. if (err) {
10. console.error(`Failed to get prefer output device for renderer info. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. console.info(`Succeeded in getting prefer output device for renderer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
13. }
14. });
```

## getPreferOutputDeviceForRendererInfo10+

PhonePC/2in1TabletTVWearable

getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>

根据音频信息，返回优先级最高的输出设备。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 音频渲染器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | Promise对象，返回优先级最高的输出设备信息。 |

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

8. audioRoutingManager.getPreferOutputDeviceForRendererInfo(rendererInfo).then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
9. console.info(`Succeeded in getting prefer output device for renderer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to get prefer output device for renderer info. Code: ${err.code}, message: ${err.message}`);
12. })
```

## getPreferredOutputDeviceForRendererInfoSync10+

PhonePC/2in1TabletTVWearable

getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors

根据音频信息，返回优先级最高的输出设备。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 音频渲染器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 返回优先级最高的输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let rendererInfo: audio.AudioRendererInfo = {
4. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
5. rendererFlags: 0 // 音频渲染器标志。
6. };

8. try {
9. let audioDeviceDescriptors = audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(rendererInfo);
10. console.info(`Succeeded in getting prefer output device for renderer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
11. } catch (err) {
12. let error = err as BusinessError;
13. console.error(`Failed to get prefer output device for renderer info. Code: ${error.code}, message: ${error.message}`);
14. }
```

## on('preferOutputDeviceChangeForRendererInfo')10+

PhonePC/2in1TabletTVWearable

on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void

监听最高优先级输出设备变化事件（当最高优先级输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'preferOutputDeviceChangeForRendererInfo'，当最高优先级输出设备发生变化时，触发该事件。 |
| rendererInfo | [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 音频渲染器信息。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数，返回优先级最高的输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. let rendererInfo: audio.AudioRendererInfo = {
2. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
3. rendererFlags: 0 // 音频渲染器标志。
4. };

6. audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', rendererInfo, (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
7. console.info(`Succeeded in using on function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
8. });
```

## off('preferOutputDeviceChangeForRendererInfo')10+

PhonePC/2in1TabletTVWearable

off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void

取消监听最高优先级输出音频设备变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'preferOutputDeviceChangeForRendererInfo'，当取消监听最高优先级输出音频设备变化事件时，触发该事件。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 否 | 回调函数，返回优先级最高的输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
2. // 当订阅了多个该事件的监听时，可通过 audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo'); 取消该事件的所有监听。
3. let preferOutputDeviceChangeForRendererInfoCallback = (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
4. console.info(`Succeeded in using on or off function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
5. };
6. let rendererInfo: audio.AudioRendererInfo = {
7. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
8. rendererFlags: 0 // 音频渲染器标志。
9. };

11. audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', rendererInfo, preferOutputDeviceChangeForRendererInfoCallback);

13. audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo', preferOutputDeviceChangeForRendererInfoCallback);
```

## getPreferredInputDeviceForCapturerInfo10+

PhonePC/2in1TabletTVWearable

getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void

根据音频信息，返回优先级最高的输入设备。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 是 | 音频采集器信息。 |
| callback | AsyncCallback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数。当获取优先级最高的输入设备成功，err为undefined，data为获取到的优先级最高的输入设备信息；否则为错误对象。 |

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

3. let capturerInfo: audio.AudioCapturerInfo = {
4. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
5. capturerFlags: 0 // 音频采集器标志。
6. };

8. audioRoutingManager.getPreferredInputDeviceForCapturerInfo(capturerInfo, (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
9. if (err) {
10. console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. console.info(`Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
13. }
14. });
```

## getPreferredInputDeviceForCapturerInfo10+

PhonePC/2in1TabletTVWearable

getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>

根据音频信息，返回优先级最高的输入设备。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 是 | 音频采集器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | Promise对象，返回优先级最高的输入设备信息。 |

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

8. audioRoutingManager.getPreferredInputDeviceForCapturerInfo(capturerInfo).then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
9. console.info(`Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
12. });
```

## getPreferredInputDeviceForCapturerInfoSync10+

PhonePC/2in1TabletTVWearable

getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors

根据音频信息，返回优先级最高的输入设备。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 是 | 音频采集器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 返回优先级最高的输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let capturerInfo: audio.AudioCapturerInfo = {
4. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
5. capturerFlags: 0 // 音频采集器标志。
6. };

8. try {
9. let audioDeviceDescriptors = audioRoutingManager.getPreferredInputDeviceForCapturerInfoSync(capturerInfo);
10. console.info(`Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
11. } catch (err) {
12. let error = err as BusinessError;
13. console.error(`Failed to get preferred input device for capturer info. Code: ${error.code}, message: ${error.message}`);
14. }
```

## on('preferredInputDeviceChangeForCapturerInfo')10+

PhonePC/2in1TabletTVWearable

on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void

监听最高优先级输入设备变化事件（当最高优先级输入设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'preferredInputDeviceChangeForCapturerInfo'，当最高优先级输入设备发生变化时，触发该事件。 |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 是 | 音频采集器信息。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 是 | 回调函数，返回优先级最高的输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. let capturerInfo: audio.AudioCapturerInfo = {
2. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
3. capturerFlags: 0 // 音频采集器标志。
4. };

6. audioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo', capturerInfo, (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
7. console.info(`Succeeded in using on function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
8. });
```

## off('preferredInputDeviceChangeForCapturerInfo')10+

PhonePC/2in1TabletTVWearable

off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void

取消监听最高优先级输入音频设备变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'preferredInputDeviceChangeForCapturerInfo'，当取消监听最高优先级输入音频设备变化事件时，触发该事件。 |
| callback | Callback<[AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors)> | 否 | 回调函数，返回优先级最高的输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
2. // 当订阅了多个该事件的监听时，可通过 audioRoutingManager.off('preferredInputDeviceChangeForCapturerInfo'); 取消该事件的所有监听。
3. let preferredInputDeviceChangeForCapturerInfoCallback = (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
4. console.info(`Succeeded in using on or off function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
5. };
6. let capturerInfo: audio.AudioCapturerInfo = {
7. source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
8. capturerFlags: 0 // 音频采集器标志。
9. };

11. audioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo', capturerInfo, preferredInputDeviceChangeForCapturerInfoCallback);

13. audioRoutingManager.off('preferredInputDeviceChangeForCapturerInfo', preferredInputDeviceChangeForCapturerInfoCallback);
```
