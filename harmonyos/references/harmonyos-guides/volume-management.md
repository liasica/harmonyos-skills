---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/volume-management
title: 播放音量管理
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 播放音量管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9ba53426688da9b3f36a38f7897cea63432e459fd6aad481aebf436e22051f89
---

本模块提供播放音量管理能力，包括对**系统音量**、**应用音量**和**音频流音量**的管理。

**系统音量**是由HarmonyOS系统全局管理的音量设置，适用于所有应用程序和设备。HarmonyOS系统将音频分为不同的流类型，每种流类型有独立的系统音量控制。

**说明** 

系统音量可以通过物理音量按键或系统设置界面调节。在设置界面中，用户可以单独调整上述每种系统音量的大小。

常见的流类型以及对应的系统音量如下所示。

* 媒体音量：用于音乐、视频、游戏等媒体播放。
* 通话音量：用于语音通话。
* 铃声音量：用于来电铃声。
* 闹钟音量：用于闹钟提醒。

**应用音量**是HarmonyOS提供给三方应用用来控制该应用下所有音频流音量的一种音量类型。三方应用设置应用音量之后，该应用中起的所有音频流默认使用该音量大小。另外具有系统应用权限的应用可以通过UID单独调整指定应用的音量。

**音频流音量**是由应用独立控制的音量设置，仅影响该应用中指定的音频流输出音量大小。例如：媒体播放器可以独立控制其播放音量，而不影响系统音量以及该应用中的其他类型流音量。

系统音量、应用音量和音频流音量的关系如下所示。

* 层级关系：系统音量是全局的，应用音量和音频流音量是局部的。

  应用音量和音频流音量的调整范围受系统音量的限制。例如：系统媒体音量设置为50%，应用音量设置为100%，应用程序的最终输出音量只能达到50%（50% \* 100%）。

  音频流音量是对应用音量的更精细化控制。设置了应用音量的三方应用，还可以继续通过音频流音量对指定的音频流进行更加精细化的控制。
* 协同关系：应用最终的输出音量是由系统音量、应用音量和音频流音量共同决定的。例如：系统媒体音量设置为50%，应用音量设置为50%，应用程序中对媒体音频流设置音频流音量为100%，则该音频流最终输出的音量为25%（50% \* 50% \* 100%）。

HarmonyOS通过系统音量，应用音量和音频流音量协同的方式实现应用对音量的精确控制。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRoutingAndVolumeSample)。

## 系统音量

管理系统音量的接口由AudioVolumeManager提供，在使用之前，需要使用[getVolumeManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

通过AudioVolumeManager只能获取音量信息及监听音量变化，不能主动调节系统音量。如果应用需要调节系统音量，可以[使用音量面板调节系统音量](volume-management.md#使用音量面板调节系统音量)。

```typescript
import { audio } from '@kit.AudioKit';
// ...

let audioManager = audio.getAudioManager();
let audioVolumeManager = audioManager.getVolumeManager();
```

### 获取音量信息

使用[AudioVolumeManager](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md)获取指定流类型的音量信息。

示例代码如下所示：

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  try {
    // 获取指定音频流的音量。
    let volume = audioVolumeManager.getVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
    console.info(`Succeeded in getting volume by stream. Volume: ${volume}`);
    // ...
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to get volume by stream. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  try {
    // 获取指定音频流的最小音量。
    let volume = audioVolumeManager.getMinVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
    console.info(`Succeeded in getting min volume by stream. Volume: ${volume}`);
    // ...
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to get min volume by stream. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  try {
    // 获取指定音频流的最大音量。
    let volume = audioVolumeManager.getMaxVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
    console.info(`Succeeded in getting max volume by stream. Volume: ${volume}`);
    // ...
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to get max volume by stream. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```

### 监听系统音量变化

通过设置监听事件，可以监听系统音量的变化：

**说明** 

不同输出设备的系统音量相互独立。当音频流的输出设备发生变更时，当前设备上该流类型的系统音量可能与原设备不同，应用可[监听最高优先级输出设备变化](audio-output-device-management.md#监听最高优先级输出设备变化)，在设备变化后通过系统音量查询接口[getVolumeByStream](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#getvolumebystream20)重新获取音量值，以更新应用侧维护的音量状态。

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  try {
    audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
      console.info(`Succeeded in using on function. StreamVolumeEvent: ${JSON.stringify(streamVolumeEvent)}`);
      // ...
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```

### 使用音量面板调节系统音量

应用无法直接调节系统音量，可以通过系统音量面板，让用户通过界面操作来调节音量。当用户通过应用内音量面板调节音量时，系统会展示音量提示界面，显性地提示用户系统音量发生改变。

系统提供了ArkTS组件AVVolumePanel（音量面板），应用可以创建该组件，具体样例和介绍请查看参考文档：[avVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)。

## 应用音量

管理应用音量的接口由AudioVolumeManager提供，在使用之前，需要使用[getVolumeManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

当[音量模式](../harmonyos-references/arkts-apis-audio-e.md#audiovolumemode19)设置为APP\_INDIVIDUAL时，可通过下面示例接口设置、查询应用音量。

### 调节应用音量

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioManager = audio.getAudioManager();
let audioVolumeManager = audioManager.getVolumeManager();

let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`Succeeded in using on function. VolumeEvent: ${JSON.stringify(volumeEvent)}`);
  // ...
};
// ...

  try {
    // 监听应用音量变化。
    audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  // 设置应用的音量（范围为0到100）。
  audioVolumeManager.setAppVolumePercentage(20).then(() => {
    console.info('Succeeded in setting app volume percentage.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to set app volume percentage. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
  // ...

  // 查询应用音量。
  audioVolumeManager.getAppVolumePercentage().then((volume: number) => {
    console.info(`Succeeded in getting app volume percentage. Volume: ${volume}`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to get app volume percentage. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

## 音频流音量

应用可使用[AVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)的[setVolume](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)或[AudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)的[setVolume](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)设置音频流音量。

使用[AudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)的[setVolume](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)和[getVolume](../harmonyos-references/arkts-apis-audio-audiorenderer.md#getvolume12)接口分别完成音频流音量的设置和获取。

示例代码如下所示：

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

    // 设置音频流音量，音量范围为[0.0-1.0]。
    audioRenderer.setVolume(0.1).then(() => {
      console.info('Succeeded in setting volume.');
      // ...
    }).catch((err: BusinessError) => {
      console.error(`Failed to set volume. Code: ${err.code}, message: ${err.message}`);
      // ...
    });
    // ...

    try {
      // 获取音频流音量。
      let volume: number = audioRenderer.getVolume();
      console.info(`Succeeded in getting volume. Volume: ${volume}`);
      // ...
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to get volume. Code: ${error.code}, message: ${error.message}`);
      // ...
    }
```
