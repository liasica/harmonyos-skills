---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiospatializationmanager
title: Interface (AudioSpatializationManager)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interface (AudioSpatializationManager)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dd50cf6f6e97da9e54061ca08960fd3e04be8c3260afed91e2ed45962bff5264
---

AudioSpatializationManager是音频系统中的空间音频管理模块。本模块提供空间音频渲染能力，包括开启或关闭当前设备的空间音频渲染、监听空间音频渲染开关状态变化等。当开发者需要使用空间音频技术增强音频体验时，使用本模块接口完成相关操作，适用于音视频播放、游戏等场景。

在使用AudioSpatializationManager的接口之前，需先通过[getSpatializationManager](arkts-apis-audio-audiomanager.md#getspatializationmanager18)获取AudioSpatializationManager实例。

**说明** 

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 18开始支持。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

## isSpatializationEnabledForCurrentDevice18+

isSpatializationEnabledForCurrentDevice(): boolean

获取当前设备空间音频渲染是否开启。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备空间音频渲染是否开启。true表示开启，false表示未开启。 |

**示例：**

```ts
let isSpatializationEnabledForCurrentDevice: boolean = audioSpatializationManager.isSpatializationEnabledForCurrentDevice();

console.info(`Succeeded in checking whether spatialization is enabled for the current device, isSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}.`);
```

## on('spatializationEnabledChangeForCurrentDevice')18+

on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void

监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'spatializationEnabledChangeForCurrentDevice'，当空间音频渲染开关状态变化时，触发该事件。 |
| callback | Callback<boolean> | 是 | 回调函数。参数为true表示打开空间音频渲染状态；参数为false表示关闭空间音频渲染状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
audioSpatializationManager.on('spatializationEnabledChangeForCurrentDevice', (isSpatializationEnabledForCurrentDevice: boolean) => {
  console.info(`Spatialization enabled for current device changed, isSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}.`);
});
```

## off('spatializationEnabledChangeForCurrentDevice')18+

off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void

取消监听当前设备空间音频渲染开关状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'spatializationEnabledChangeForCurrentDevice'。 |
| callback | Callback<boolean> | 否 | 回调函数。传入回调函数时，仅取消该回调对应的监听事件，需与[on('spatializationEnabledChangeForCurrentDevice')](arkts-apis-audio-audiospatializationmanager.md#onspatializationenabledchangeforcurrentdevice18)绑定同一回调函数；不传参数时，取消此事件类型下所有已订阅的监听事件。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](errorcode-audio.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 取消该事件的所有监听。
audioSpatializationManager.off('spatializationEnabledChangeForCurrentDevice');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let spatializationEnabledChangeForCurrentDeviceCallback = (enabled: boolean) => {
  console.info(`Spatialization enabled for current device changed, enabled: ${enabled}.`);
};

audioSpatializationManager.on('spatializationEnabledChangeForCurrentDevice', spatializationEnabledChangeForCurrentDeviceCallback);

audioSpatializationManager.off('spatializationEnabledChangeForCurrentDevice', spatializationEnabledChangeForCurrentDeviceCallback);
```
