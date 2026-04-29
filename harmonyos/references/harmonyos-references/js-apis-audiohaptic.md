---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic
title: @ohos.multimedia.audioHaptic (音振协同)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audioHaptic (音振协同)
category: harmonyos-references
scraped_at: 2026-04-29T14:02:23+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:751f79b54f10fdf065299a254376f0b992030f1d3f7c547c3112623fe99f554a
---

音振协同，表示在播放声音时，可同步发起振动。可用于来电通知、消息提醒等场景。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**设备行为差异：** 若设备无振动器件，将不会产生振动效果。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audioHaptic } from '@kit.AudioKit';
```

## audioHaptic.getAudioHapticManager

PhonePC/2in1TabletTVWearable

getAudioHapticManager(): AudioHapticManager

获取音振管理器。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioHapticManager](js-apis-audiohaptic.md#audiohapticmanager) | 音振管理器。 |

**示例：**

```
1. let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();
```

## AudioLatencyMode

PhonePC/2in1TabletTVWearable

枚举，音频时延模式。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_LATENCY\_MODE\_NORMAL | 0 | 普通时延模式。 |
| AUDIO\_LATENCY\_MODE\_FAST | 1 | 低时延模式。当音频文件过长时可能被截断，该特性与[SoundPool](js-apis-inner-multimedia-soundpool.md#soundpool)一致。 |

## AudioHapticPlayerOptions

PhonePC/2in1TabletTVWearable

音振播放器选项。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| muteAudio | boolean | 否 | 是 | 是否将音频静音，true表示将音频静音，false表示正常播放声音。若不填该参数，则默认为false。 |
| muteHaptics | boolean | 否 | 是 | 是否禁止振动，true表示将禁止振动，false表示正常振动。若不填该参数，则默认为false。 |

## AudioHapticFileDescriptor20+

PhonePC/2in1TabletTVWearable

描述音振文件描述符。

注意

开发者需要确保fd是可用的文件描述符，且offset和length的值都是正确的。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 否 | 否 | 音振资源文件的文件描述符，通常大于等于0。 |
| offset | number | 否 | 是 | 文件中数据读取的偏移量，单位为字节。默认情况下，偏移量为0。 |
| length | number | 否 | 是 | 读取数据的字节长度。默认情况下，长度为文件中从偏移量位置开始的剩余字节数。 |

## AudioHapticManager

PhonePC/2in1TabletTVWearable

管理音振协同功能。在调用AudioHapticManager的接口前，需要先通过[getAudioHapticManager](js-apis-audiohaptic.md#audiohapticgetaudiohapticmanager)创建实例。

### registerSource

PhonePC/2in1TabletTVWearable

registerSource(audioUri: string, hapticUri: string): Promise<number>

通过Uri注册音频和振动资源。使用Promise异步回调。

注意

单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| audioUri | string | 是 | 音频资源的Uri。  - 对普通时延模式，音频资源格式和路径格式的支持可参考[AVPlayer](arkts-apis-media-avplayer.md)。  - 对低时延模式，音频资源格式支持可参考[SoundPool](js-apis-inner-multimedia-soundpool.md#soundpool)，路径格式需满足[fileIo.open](js-apis-file-fs.md#fileioopen)的要求。  - 对两种时延模式，均建议传入文件的绝对路径。 |
| hapticUri | string | 是 | 振动资源的Uri。  振动资源格式支持可参考[HapticFileDescriptor](js-apis-vibrator.md#hapticfiledescriptor10)，路径格式需满足[fileIo.open](js-apis-file-fs.md#fileioopen)的要求。  建议传入文件的绝对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回注册的资源ID。  正常情况下返回注册的资源ID为非负数。若返回注册的资源ID为负数，则表示注册失败，需检查注册资源数量是否超过上限。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let audioUri = 'data/audioTest.wav'; // 需更改为目标音频资源的Uri。
4. let hapticUri = 'data/hapticTest.json'; // 需更改为目标振动资源的Uri。
5. let id = 0;
6. // 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。
7. audioHapticManagerInstance.registerSource(audioUri, hapticUri).then((value: number) => {
8. console.info(`Succeeded in registering source. ID: ${value}.`);
9. id = value;
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to register source. Code: ${err.code}, message: ${err.message}`);
12. });
```

### registerSourceFromFd20+

PhonePC/2in1TabletTVWearable

registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>

通过文件描述符注册音频和振动资源。使用Promise异步回调。

注意

单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| audioFd | [AudioHapticFileDescriptor](js-apis-audiohaptic.md#audiohapticfiledescriptor20) | 是 | 已打开的有效文件描述符对象，用于描述音频文件。配套的offset和length需符合实际文件长度。 |
| hapticFd | [AudioHapticFileDescriptor](js-apis-audiohaptic.md#audiohapticfiledescriptor20) | 是 | 已打开的有效文件描述符对象，用于描述振动文件。配套的offset和length必须符合实际文件长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回注册的资源ID。  正常情况下返回注册的资源ID为非负数。若返回注册的资源ID为负数，则表示注册失败，需检查注册资源数量是否超过上限。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

7. let audioFile = context.resourceManager.getRawFdSync('audioTest.ogg'); // 需要改成rawfile目录下的对应文件。
8. let audioFd: audioHaptic.AudioHapticFileDescriptor = {
9. fd: audioFile.fd,
10. offset: audioFile.offset,
11. length: audioFile.length,
12. };

14. let hapticFile = context.resourceManager.getRawFdSync('hapticTest.json'); // 需要改成rawfile目录下的对应文件。
15. let hapticFd: audioHaptic.AudioHapticFileDescriptor = {
16. fd: hapticFile.fd,
17. offset: hapticFile.offset,
18. length: hapticFile.length,
19. };
20. let id = 0;
21. // 单个应用最多支持同时注册128个资源，超过之后将会注册失败（返回注册的资源ID为负数）。推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。
22. audioHapticManagerInstance.registerSourceFromFd(audioFd, hapticFd).then((value: number) => {
23. console.info(`Succeeded in registering source from fd. ID: ${value}.`);
24. id = value;
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to register source from fd. Code: ${err.code}, message: ${err.message}`);
27. });
```

### unregisterSource

PhonePC/2in1TabletTVWearable

unregisterSource(id: number): Promise<void>

取消注册音频和振动资源。使用Promise异步回调。

注意

对于不再需要使用的资源，建议应用及时取消注册，避免出现资源泄漏或资源数量超上限等问题。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 已注册资源的source id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let id = 0; // 需要通过registerSource方法获取。

5. audioHapticManagerInstance.unregisterSource(id).then(() => {
6. console.info('Succeeded in unregistering source.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to unregister source. Code: ${err.code}, message: ${err.message}`);
9. });
```

### setAudioLatencyMode

PhonePC/2in1TabletTVWearable

setAudioLatencyMode(id:number, latencyMode: AudioLatencyMode): void

设置音频时延模式。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 已注册资源的source id。 |
| latencyMode | [AudioLatencyMode](js-apis-audiohaptic.md#audiolatencymode) | 是 | 音频时延模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let id = 0; // 需要通过registerSource方法获取。

5. let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_FAST;

7. audioHapticManagerInstance.setAudioLatencyMode(id, latencyMode);
```

### setStreamUsage

PhonePC/2in1TabletTVWearable

setStreamUsage(id: number, usage: audio.StreamUsage): void

设置音频流使用类型。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 已注册资源的source id。 |
| usage | [audio.StreamUsage](arkts-apis-audio-e.md#streamusage) | 是 | 音频流使用类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 5400102 | Operation not allowed. |

**示例：**

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let id = 0; // 需要通过registerSource方法获取。

6. let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;

8. audioHapticManagerInstance.setStreamUsage(id, usage);
```

### createPlayer

PhonePC/2in1TabletTVWearable

createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>

创建音振播放器。使用Promise异步回调。

**需要权限：** ohos.permission.VIBRATE

如果应用创建的AudioHapticPlayer需要触发振动，则需要校验应用是否拥有该权限。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 已注册资源的source id。 |
| options | [AudioHapticPlayerOptions](js-apis-audiohaptic.md#audiohapticplayeroptions) | 否 | 音振播放器选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioHapticPlayer](js-apis-audiohaptic.md#audiohapticplayer)> | Promise对象，返回创建的音振播放器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400106 | Unsupport format. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let id = 0; // 需要通过registerSource方法获取。

5. let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
6. let audioHapticPlayerInstance: audioHaptic.AudioHapticPlayer | undefined = undefined;

8. audioHapticManagerInstance.createPlayer(id, options).then((value: audioHaptic.AudioHapticPlayer) => {
9. audioHapticPlayerInstance = value;
10. console.info('Succeeded in creating player.');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to create player. Code: ${err.code}, message: ${err.message}`);
13. });
```

## AudioHapticType

PhonePC/2in1TabletTVWearable

枚举，音振类型。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_HAPTIC\_TYPE\_AUDIO | 0 | 音频。 |
| AUDIO\_HAPTIC\_TYPE\_HAPTIC | 1 | 振动。 |

## AudioHapticPlayer

PhonePC/2in1TabletTVWearable

音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过[createPlayer](js-apis-audiohaptic.md#createplayer)创建实例。

### isMuted

PhonePC/2in1TabletTVWearable

isMuted(type: AudioHapticType): boolean

查询该音振类型是否被静音。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AudioHapticType](js-apis-audiohaptic.md#audiohaptictype) | 是 | 音振类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示查询的音振类型是否被静音。true表示静音，false表示非静音。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Parameter verification failed. |

**示例：**

```
1. let audioHapticType: audioHaptic.AudioHapticType = audioHaptic.AudioHapticType.AUDIO_HAPTIC_TYPE_AUDIO;

3. let result: boolean = audioHapticPlayerInstance.isMuted(audioHapticType);
```

### start

PhonePC/2in1TabletTVWearable

start(): Promise<void>

开始播放。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. |
| 5400103 | IO error. |
| 5400105 | Service died. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioHapticPlayerInstance.start().then(() => {
4. console.info('Succeeded in starting.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to start. Code: ${err.code}, message: ${err.message}`);
7. });
```

### stop

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止播放。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit. |
| 5400105 | Service died. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioHapticPlayerInstance.stop().then(() => {
4. console.info('Succeeded in stopping.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to stop Code: ${err.code}, message: ${err.message}`);
7. });
```

### release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放音振播放器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioHapticPlayerInstance.release().then(() => {
4. console.info('Succeeded in releasing.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to release. Code: ${err.code}, message: ${err.message}`);
7. });
```

### setVolume20+

PhonePC/2in1TabletTVWearable

setVolume(volume: number): Promise<void>

设置音振播放器的音量。使用Promise异步回调。

注意

该方法需在音振播放器释放前调用。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 取值范围为[0.00, 1.00]，其中1.00表示最大音量（100%）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Service died. |
| 5400102 | Operate not permit in current state. |
| 5400108 | Parameter out of range. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioHapticPlayerInstance.setVolume(0.5).then(() => {
4. console.info('Succeeded in setting volume.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to set volume. Code: ${err.code}, message: ${err.message}`);
7. });
```

### setLoop20+

PhonePC/2in1TabletTVWearable

setLoop(loop: boolean): Promise<void>

设置音振播放器循环播放。使用Promise异步回调。

注意

该方法需在音振播放器销毁前调用。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loop | boolean | 是 | 是否循环播放。true表示循环播放，false表示不循环播放。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operate not permit in current state. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioHapticPlayerInstance.setLoop(true).then(() => {
4. console.info('Succeeded in setting loop.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to set loop. Code: ${err.code}, message: ${err.message}`);
7. });
```

### on('endOfStream')

PhonePC/2in1TabletTVWearable

on(type: 'endOfStream', callback: Callback<void>): void

监听流结束事件（音频流播放结束时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'endOfStream'，当音频流播放结束时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**示例：**

```
1. audioHapticPlayerInstance.on('endOfStream', () => {
2. console.info('Succeeded in using on function.');
3. });
```

### off('endOfStream')

PhonePC/2in1TabletTVWearable

off(type: 'endOfStream', callback?: Callback<void>): void

取消监听流结束事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'endOfStream'，当取消监听流结束事件时，触发该事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果。 |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioHapticPlayerInstance.off('endOfStream');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let endOfStreamCallback = () => {
6. console.info('Succeeded in using on or off function.');
7. };

9. audioHapticPlayerInstance.on('endOfStream', endOfStreamCallback);

11. audioHapticPlayerInstance.off('endOfStream', endOfStreamCallback);
```

### on('audioInterrupt')

PhonePC/2in1TabletTVWearable

on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当音频焦点状态发生变化时，触发该事件。 |
| callback | Callback<[audio.InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 是 | 回调函数，返回中断事件信息。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. let isPlaying: boolean; // 标识符，表示是否正在渲染。
4. let isDucked: boolean; // 标识符，表示是否被降低音量。

6. audioHapticPlayerInstance.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
7. // 在发生音频打断事件时，audioHapticPlayerInstance收到interruptEvent回调，此处根据其内容做相应处理。
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
35. break;
36. }
37. } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
38. // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
39. switch (interruptEvent.hintType) {
40. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
41. // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
42. // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
43. console.info('Resume force paused renderer or ignore');
44. // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
45. break;
46. default:
47. break;
48. }
49. }
50. });
```

### off('audioInterrupt')

PhonePC/2in1TabletTVWearable

off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void

取消监听音频中断事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioInterrupt'，当取消监听音频中断事件时，触发该事件。 |
| callback | Callback<[audio.InterruptEvent](arkts-apis-audio-i.md#interruptevent9)> | 否 | 回调函数，返回中断事件信息。 |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. // 取消该事件的所有监听。
4. audioHapticPlayerInstance.off('audioInterrupt');

6. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
7. let isPlaying: boolean; // 标识符，表示是否正在渲染。
8. let isDucked: boolean; // 标识符，表示是否被降低音量。
9. let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
10. // 在发生音频打断事件时，audioHapticPlayerInstance收到interruptEvent回调，此处根据其内容做相应处理。
11. // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
12. // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
13. // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
14. if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
15. // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
16. switch (interruptEvent.hintType) {
17. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
18. // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
19. console.info('Force paused. Update playing status and stop writing');
20. isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
21. break;
22. case audio.InterruptHint.INTERRUPT_HINT_STOP:
23. // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
24. console.info('Force stopped. Update playing status and stop writing');
25. isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
26. break;
27. case audio.InterruptHint.INTERRUPT_HINT_DUCK:
28. // 音频流已被降低音量渲染。
29. console.info('Force ducked. Update volume status');
30. isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
31. break;
32. case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
33. // 音频流已被恢复正常音量渲染。
34. console.info('Force unducked. Update volume status');
35. isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
36. break;
37. default:
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
50. break;
51. }
52. }
53. };

55. audioHapticPlayerInstance.on('audioInterrupt', audioInterruptCallback);

57. audioHapticPlayerInstance.off('audioInterrupt', audioInterruptCallback);
```
