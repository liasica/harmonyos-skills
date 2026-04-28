---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/public-audio-spatialization-management
title: 空间音频能力查询和状态订阅
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 空间音频能力查询和状态订阅
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:233baf50a7d16a2bfbb858e322c81bc09903588ab33f972085e5da8424a9470f
---

从API version 18开始，支持空间音频能力查询和状态订阅。

空间音频是一种能够将传统立体声体验扩展到三维空间的音频技术，在单声道、立体声、环绕声的基础上，增加高度感知，营造全方位的听音体验。空间音频为用户提供沉浸的、有互动的、有空间感的“声”临其境的音频体验。

Audio Vivid是基于AI技术的音频编解码标准，由世界超高清视频产业联盟（UWA）与数字音视频编解码技术标准工作组（AVS）联合制定，共同发布。包含音频PCM数据以及元数据的音频格式，相比传统立体声音源，Audio Vivid包含音频内容源的元数据信息，能够还原物理和感知世界中的真实听感，打造极致的沉浸式听觉体验。

空间音频支持播放多声道、立体声、Audio Vivid等格式音源，并在耳机实现双耳空间音频渲染重放。搭配Audio Vivid格式音源的空间音频渲染，能够将音乐中的人声和各种乐器作为独立的声音对象，重新定义各种声音对象的位置、移动轨迹和声音大小、远近等要素，实现声音在听众四周及上方全面萦绕，实现更佳的空间音频沉浸式体验，获得影院、音乐厅等的临场感与艺术体验。当设备支持空间音频且空间音频开关被打开时，下发Audio Vivid格式音源可以得到更加沉浸的音频体验。关于如何播放Audio Vivid音源，可参考[播放Audio Vivid格式音源](using-ohaudio-for-playback.md#播放audio-vivid格式音源)。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

## 使用说明

对于播放音频类的应用，开发者可以查询到设备是否有支持空间音频的能力，以及当前设备空间音频的开关状态。

### 创建空间音频示例

应用开发者在使用AudioSpatializationManager的接口前，需要先调用[getSpatializationManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getspatializationmanager18)创建AudioSpatializationManager实例。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. let audioManager = audio.getAudioManager();
4. // ...
5. let audioSpatializationManager = audioManager.getSpatializationManager();
```

### 查询设备是否支持空间音频渲染能力

应用开发者可以使用[AudioDeviceDescriptor](../harmonyos-references/arkts-apis-audio-i.md#audiodevicedescriptor)的spatializationSupported属性获取指定设备是否具有空间音频渲染的能力，需要通过音频框架中其他接口来获取当前已连接设备或当前发声设备的AudioDeviceDescriptor。例如，可以使用[getRoutingManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getroutingmanager9)创建的AudioRoutingManager实例的[getDevicesSync](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevicessync10)接口获取。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. let audioRoutingManager = audioManager.getRoutingManager();
4. // ...
5. let deviceDescriptors = audioRoutingManager.getDevicesSync(audio.DeviceFlag.OUTPUT_DEVICES_FLAG);
6. console.info(`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(deviceDescriptors)}.`);
```

### 查询当前发声设备的空间音频渲染效果开关状态

应用开发者可以通过[isSpatializationEnabledForCurrentDevice](../harmonyos-references/arkts-apis-audio-audiospatializationmanager.md#isspatializationenabledforcurrentdevice18)接口查询当前设备的空间音频渲染效果开关状态。

* 该接口返回true表示当前设备空间音频渲染开启，返回false表示当前设备空间音频渲染关闭。
* 该状态仅为开关状态，实际是否生效还需依赖当前设备是否支持空间音频渲染。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. let isSpatializationEnabledForCurrentDevice = audioSpatializationManager.isSpatializationEnabledForCurrentDevice();
4. console.info(`Succeeded in using isSpatializationEnabledForCurrentDevice function,
5. IsSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}.`);
```

**订阅当前发声设备空间音频渲染效果的开关状态变化事件**

应用开发者可以通过[on('spatializationEnabledChangeForCurrentDevice')](../harmonyos-references/arkts-apis-audio-audiospatializationmanager.md#onspatializationenabledchangeforcurrentdevice18)接口订阅当前空间音频渲染效果的开关状态变化事件。

该接口返回true表示空间音频渲染被开启，返回false表示空间音频渲染被关闭。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. audioSpatializationManager.on('spatializationEnabledChangeForCurrentDevice',
4. (isSpatializationEnabledForCurrentDevice: boolean) => {
5. console.info(`Succeeded in using on function, IsSpatializationEnabledForCurrentDevice:
6. ${isSpatializationEnabledForCurrentDevice}.`);
7. // ...
8. });
```

**取消订阅当前发声设备空间音频渲染效果的开关状态变化事件**

应用开发者可以通过[off('spatializationEnabledChangeForCurrentDevice')](../harmonyos-references/arkts-apis-audio-audiospatializationmanager.md#offspatializationenabledchangeforcurrentdevice18)接口取消订阅空间音频渲染效果的开关状态变化事件。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. audioSpatializationManager.off('spatializationEnabledChangeForCurrentDevice');
```
