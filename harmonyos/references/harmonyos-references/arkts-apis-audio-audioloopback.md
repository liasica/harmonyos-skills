---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback
title: Interface (AudioLoopback)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioLoopback)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4a7b4045aea2b3f007819607a7228654dae82c9558bb6e79c78cb3e3571dc839
---

提供音频返听的相关接口。

在使用AudioLoopback的接口之前，需先通过[audio.createAudioLoopback](arkts-apis-audio-f.md#audiocreateaudioloopback20)获取AudioLoopback实例。

当启用音频返听时，系统会创建低时延渲染器与低时延采集器，实现低时延耳返功能。采集的音频直接通过内部路由返回到渲染器。对于渲染器，其音频焦点策略与[STREAM\_USAGE\_MUSIC](arkts-apis-audio-e.md#streamusage)相匹配。对于采集器，其音频焦点策略与[SOURCE\_TYPE\_MIC](arkts-apis-audio-e.md#sourcetype8)相匹配。

输入\输出设备由系统自动选择。如果当前输入\输出不支持低时延，则音频返听无法启用。在运行过程中，如果音频焦点被另一个音频流抢占，输入\输出设备切换到不支持低时延的设备，系统会自动禁用音频返听。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { audio } from '@kit.AudioKit';
```

## getStatus20+

PhonePC/2in1TabletTVWearable

getStatus(): Promise<AudioLoopbackStatus>

获取音频返听状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioLoopbackStatus](arkts-apis-audio-e.md#audioloopbackstatus20)> | Promise对象，返回音频返听状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioLoopback.getStatus().then((status: audio.AudioLoopbackStatus) => {
4. console.info(`AudioLoopback: Status: ${status}`);
5. }).catch((err: BusinessError) => {
6. console.error(`AudioLoopback: Status :ERROR: ${err}`);
7. })
```

## setVolume20+

PhonePC/2in1TabletTVWearable

setVolume(volume: number): Promise<void>

设置音频返听的音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 音量值范围为[0.0, 1.0]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed, form 0.0 to 1.0. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioLoopback.setVolume(0.5).then(() => {
4. console.info('setVolume Success!');
5. }).catch((err: BusinessError) => {
6. console.error(`setVolume Fail: ${err}`);
7. });
```

## on('statusChange')20+

PhonePC/2in1TabletTVWearable

on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void

监听返听状态变化事件（当AudioLoopback的状态发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'statusChange'，当AudioLoopback的状态发生变化时，触发该事件。 |
| callback | Callback<[AudioLoopbackStatus](arkts-apis-audio-e.md#audioloopbackstatus20)> | 是 | 回调函数，返回当前音频返听的状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. audioLoopback.on('statusChange', (status: audio.AudioLoopbackStatus) => {
2. if (status == audio.AudioLoopbackStatus.UNAVAILABLE_DEVICE) {
3. console.info('audio loopback status is: UNAVAILABLE_DEVICE');
4. } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE_SCENE) {
5. console.info('audio loopback status is: UNAVAILABLE_SCENE');
6. } else if (status == audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
7. console.info('audio loopback status is: AVAILABLE_IDLE');
8. } else if (status == audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
9. console.info('audio loopback status is: AVAILABLE_RUNNING');
10. }
11. });
```

## off('statusChange')20+

PhonePC/2in1TabletTVWearable

off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void

取消监听音频状态事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'statusChange'，当取消监听音频状态事件时，触发该事件。 |
| callback | Callback<[AudioLoopbackStatus](arkts-apis-audio-e.md#audioloopbackstatus20)> | 否 | 回调函数，返回当前音频返听的状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. // 取消该事件的所有监听。
2. audioLoopback.off('statusChange');

4. // 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
5. let statusChangeCallback = (status: audio.AudioLoopbackStatus) => {
6. if (status == audio.AudioLoopbackStatus.UNAVAILABLE_DEVICE) {
7. console.info('audio loopback status is: UNAVAILABLE_DEVICE');
8. } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE_SCENE) {
9. console.info('audio loopback status is: UNAVAILABLE_SCENE');
10. } else if (status == audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
11. console.info('audio loopback status is: AVAILABLE_IDLE');
12. } else if (status == audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
13. console.info('audio loopback status is: AVAILABLE_RUNNING');
14. }
15. };

17. audioLoopback.on('statusChange', statusChangeCallback);

19. audioLoopback.off('statusChange', statusChangeCallback);
```

## enable20+

PhonePC/2in1TabletTVWearable

enable(enable: boolean): Promise<boolean>

启用或禁用音频返听器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否启用音频返听器。true表示启用，false表示不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示功能执行成功；返回false表示功能执行失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. audioLoopback.enable(true).then((isSuccess) => {
4. if (isSuccess) {
5. console.info('audio loopback enable success');
6. } else {
7. console.info('audio loopback enable fail');
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`ERROR: ${err}`);
11. });
```

## setReverbPreset21+

PhonePC/2in1TabletTVWearable

setReverbPreset(preset: AudioLoopbackReverbPreset): boolean

设置音频返听器的混响模式。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preset | [AudioLoopbackReverbPreset](arkts-apis-audio-e.md#audioloopbackreverbpreset21) | 是 | 混响模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回混响模式是否设置成功。true表示成功，false表示不成功。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. audioLoopback.setReverbPreset(audio.AudioLoopbackReverbPreset.THEATER);
4. } catch (err) {
5. console.error(`setReverbPreset :ERROR: ${err}`);
6. }
```

## getReverbPreset21+

PhonePC/2in1TabletTVWearable

getReverbPreset(): AudioLoopbackReverbPreset

获取当前音频返听器的混响模式。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioLoopbackReverbPreset](arkts-apis-audio-e.md#audioloopbackreverbpreset21) | 返回当前音频返听器的混响模式。  在没有被修改的情况下，默认的混响模式是THEATER。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let reverbPreset = audioLoopback.getReverbPreset();
4. } catch (err) {
5. console.error(`getReverbPreset:ERROR: ${err}`);
6. }
```

## setEqualizerPreset21+

PhonePC/2in1TabletTVWearable

setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean

设置音频返听器的均衡器类型。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preset | [AudioLoopbackEqualizerPreset](arkts-apis-audio-e.md#audioloopbackequalizerpreset21) | 是 | 均衡器类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回均衡器类型是否设置成功。true表示成功，false表示不成功。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. audioLoopback.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
4. } catch (err) {
5. console.error(`setEqualizerPreset :ERROR: ${err}`);
6. }
```

## getEqualizerPreset21+

PhonePC/2in1TabletTVWearable

getEqualizerPreset(): AudioLoopbackEqualizerPreset

获取当前音频返听器的均衡器类型。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioLoopbackEqualizerPreset](arkts-apis-audio-e.md#audioloopbackequalizerpreset21) | 返回当前音频返听器的均衡器类型。  在没有被修改的情况下，默认的均衡器类型是FULL。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let reverbPreset = audioLoopback.getEqualizerPreset();
4. } catch (err) {
5. console.error(`getEqualizerPreset:ERROR: ${err}`);
6. }
```
