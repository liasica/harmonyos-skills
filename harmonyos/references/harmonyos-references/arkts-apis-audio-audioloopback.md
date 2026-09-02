---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback
title: Interface (AudioLoopback)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioLoopback)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0e6e5348a2d3f2130d4750525a860ab28b600fe34a4e9996d691faacca3b6104
---

提供音频返听的相关接口。

在使用AudioLoopback的接口之前，需先通过[audio.createAudioLoopback](arkts-apis-audio-f.md#audiocreateaudioloopback20)获取AudioLoopback实例。

当启用音频返听时，系统会创建低时延渲染器与低时延采集器，实现低时延耳返功能。采集的音频直接通过内部路由返回到渲染器。对于渲染器，其音频焦点策略与[STREAM\_USAGE\_MUSIC](arkts-apis-audio-e.md#streamusage)相匹配。对于采集器，其音频焦点策略与[SOURCE\_TYPE\_MIC](arkts-apis-audio-e.md#sourcetype8)相匹配。

输入/输出设备由系统自动选择。如果当前输入/输出不支持低时延，则音频返听无法启用。在运行过程中，如果音频焦点被另一个音频流抢占，输入/输出设备切换到不支持低时延的设备，系统会自动禁用音频返听。

**说明** 

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

## getStatus20+

getStatus(): Promise<AudioLoopbackStatus>

获取音频返听状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AudioLoopbackStatus](arkts-apis-audio-e.md#audioloopbackstatus20)> | Promise对象，返回音频返听状态。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioLoopback.getStatus().then((status: audio.AudioLoopbackStatus) => {
  console.info(`AudioLoopback: Status: ${status}`);
}).catch((err: BusinessError) => {
  console.error(`AudioLoopback: Status :ERROR: ${err}`);
})
```

## setVolume20+

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
| 6800101 | Parameter verification failed, from 0.0 to 1.0. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioLoopback.setVolume(0.5).then(() => {
  console.info('setVolume Success!');
}).catch((err: BusinessError) => {
  console.error(`setVolume Fail: ${err}`);
});
```

## getVolume

getVolume(): number

获取音频返听输出音量。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前音频返听输出音量，范围为[0.0, 1.0]。 |

**示例：**

```ts
let volume = audioLoopback.getVolume();
console.info(`Current loopback volume is ${volume}.`);
```

## on('statusChange')20+

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

```ts
audioLoopback.on('statusChange', (status: audio.AudioLoopbackStatus) => {
  if (status == audio.AudioLoopbackStatus.UNAVAILABLE_DEVICE) {
    console.info('audio loopback status is: UNAVAILABLE_DEVICE');
  } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE_SCENE) {
    console.info('audio loopback status is: UNAVAILABLE_SCENE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
    console.info('audio loopback status is: AVAILABLE_IDLE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
    console.info('audio loopback status is: AVAILABLE_RUNNING');
  }
});
```

## off('statusChange')20+

off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void

取消监听音频返听状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'statusChange'。 |
| callback | Callback<[AudioLoopbackStatus](arkts-apis-audio-e.md#audioloopbackstatus20)> | 否 | 回调函数，返回当前音频返听的状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 取消该事件的所有监听。
audioLoopback.off('statusChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let statusChangeCallback = (status: audio.AudioLoopbackStatus) => {
  if (status == audio.AudioLoopbackStatus.UNAVAILABLE_DEVICE) {
    console.info('audio loopback status is: UNAVAILABLE_DEVICE');
  } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE_SCENE) {
    console.info('audio loopback status is: UNAVAILABLE_SCENE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
    console.info('audio loopback status is: AVAILABLE_IDLE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
    console.info('audio loopback status is: AVAILABLE_RUNNING');
  }
};

audioLoopback.on('statusChange', statusChangeCallback);

audioLoopback.off('statusChange', statusChangeCallback);
```

## getSupportedDevicePairs

getSupportedDevicePairs(): Array<AudioDevicePair>

获取当前设备连接状态下支持返听的音频输入输出设备组合。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[AudioDevicePair](arkts-apis-audio-i.md#audiodevicepair)> | 返回支持返听的音频输入输出设备数组。  如果没有可用的输入输出设备组合，则返回空数组。 |

**示例：**

```ts
let supportedPairs = audioLoopback.getSupportedDevicePairs();
if (supportedPairs.length === 0) {
  console.info('No supported loopback device pair found.');
}
```

## getPreferredDevicePair

getPreferredDevicePair(): AudioDevicePair | null

获取当前设备连接状态下系统推荐的返听音频输入输出设备组合。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDevicePair](arkts-apis-audio-i.md#audiodevicepair) | null | 返回系统推荐的音频输入输出设备组合。  如果没有可用的输入输出设备组合，则返回null。 |

**示例：**

```ts
let preferredPair = audioLoopback.getPreferredDevicePair();
if (preferredPair === null) {
  console.info('No preferred loopback device pair found.');
}
```

## enable20+

enable(enable: boolean): Promise<boolean>

启用或禁用音频返听器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 表示是否启用音频返听器。true表示启用，false表示禁用。 |

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioLoopback.enable(true).then((isSuccess) => {
  if (isSuccess) {
    console.info('audio loopback enable success');
  } else {
    console.info('audio loopback enable fail');
  }
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## setReverbPreset21+

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

```ts
  audioLoopback.setReverbPreset(audio.AudioLoopbackReverbPreset.THEATER);
```

## getReverbPreset21+

getReverbPreset(): AudioLoopbackReverbPreset

获取当前音频返听器的混响模式。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioLoopbackReverbPreset](arkts-apis-audio-e.md#audioloopbackreverbpreset21) | 返回当前音频返听器的混响模式。  在没有被修改的情况下，默认的混响模式是THEATER。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let reverbPreset = audioLoopback.getReverbPreset();
} catch (err) {
  console.error(`getReverbPreset:ERROR: ${err}`);
}
```

## setEqualizerPreset21+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';
try {
  audioLoopback.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
} catch (err) {
  console.error(`setEqualizerPreset :ERROR: ${err}`);
}
```

## getEqualizerPreset21+

getEqualizerPreset(): AudioLoopbackEqualizerPreset

获取当前音频返听器的均衡器类型。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioLoopbackEqualizerPreset](arkts-apis-audio-e.md#audioloopbackequalizerpreset21) | 返回当前音频返听器的均衡器类型。  在没有被修改的情况下，默认的均衡器类型是FULL。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let equalizerPreset = audioLoopback.getEqualizerPreset();
} catch (err) {
  console.error(`getEqualizerPreset:ERROR: ${err}`);
}
```
