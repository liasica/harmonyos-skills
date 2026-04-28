---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/volume-management
title: 播放音量管理
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 播放音量管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:476d93e2d07b4bd5637fa147f0db6629f94e57e4cd8eefe409869a9eb365a871
---

本模块提供播放音量管理能力，包括对**系统音量**、**应用音量**和**音频流音量**的管理。

**系统音量**是由HarmonyOS系统全局管理的音量设置，适用于所有应用程序和设备。HarmonyOS系统将音频分为不同的流类型，每种流类型有独立的系统音量控制。

说明

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

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

## 系统音量

管理系统音量的接口由AudioVolumeManager提供，在使用之前，需要使用[getVolumeManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

通过AudioVolumeManager只能获取音量信息及监听音量变化，不能主动调节系统音量。如果应用需要调节系统音量，可以[使用音量面板调节系统音量](volume-management.md#使用音量面板调节系统音量)。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. let audioManager = audio.getAudioManager();
4. let audioVolumeManager = audioManager.getVolumeManager();
```

### 获取音量信息

管理系统音量的接口由AudioVolumeManager提供，在使用之前，需要使用[getVolumeManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. let audioManager = audio.getAudioManager();
4. let audioVolumeManager = audioManager.getVolumeManager();
```

使用[AudioVolumeManager](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md)获取指定流类型的音量信息。

示例代码如下所示：

```
1. import { audio } from '@kit.AudioKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // ...
4. // 获取指定流的音量。
5. audioVolumeManager.getVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
6. // ...
7. // 获取指定流的最小音量。
8. audioVolumeManager.getMinVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);

10. // 获取指定流的最大音量。
11. audioVolumeManager.getMaxVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
```

### 监听系统音量变化

通过设置监听事件，可以监听系统音量的变化：

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC,
4. (streamVolumeEvent: audio.StreamVolumeEvent) => {
5. console.info(`StreamUsagem: ${streamVolumeEvent.streamUsage} `);
6. console.info(`Volume level: ${streamVolumeEvent.volume} `);
7. console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
8. // ...
9. });
```

### 使用音量面板调节系统音量

应用无法直接调节系统音量，可以通过系统音量面板，让用户通过界面操作来调节音量。当用户通过应用内音量面板调节音量时，系统会展示音量提示界面，显性地提示用户系统音量发生改变。

系统提供了ArkTS组件AVVolumePanel（音量面板），应用可以创建该组件，具体样例和介绍请查看参考文档：[avVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)。

## 应用音量

管理应用音量的接口由AudioVolumeManager提供，在使用之前，需要使用[getVolumeManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getvolumemanager9)获取AudioVolumeManager实例。

当[音量模式](../harmonyos-references/arkts-apis-audio-e.md#audiovolumemode19)设置为APP\_INDIVIDUAL时，可通过下面示例接口设置、查询应用音量。

### 调节应用音量

```
1. import { audio } from '@kit.AudioKit';
2. // ...
3. let audioManager = audio.getAudioManager();
4. let audioVolumeManager = audioManager.getVolumeManager();
5. // ...
6. // 设置应用的音量（范围为0到100）。
7. audioVolumeManager.setAppVolumePercentage(20).then(() => {
8. console.info(`set app volume success.`);
9. // ...
10. });

12. // 查询应用音量。
13. audioVolumeManager.getAppVolumePercentage().then((value: number) => {
14. console.info(`app volume is ${value}.`);
15. // ...
16. });

18. // 监听应用音量变化，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
19. let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
20. console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
21. console.info(`Volume level: ${volumeEvent.volume} `);
22. console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
23. // ...
24. };
25. audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);
26. audioVolumeManager.off('appVolumeChange', appVolumeChangeCallback);
```

## 音频流音量

管理音频流音量的接口是AVPlayer或AudioRenderer的setVolume()方法，使用[AVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)设置音频流音量的示例代码如下：

```
1. let volume = 1.0;  // 指定的音量大小，取值范围为[0.00-1.00]，1表示最大音量。
2. avPlayer.setVolume(volume);
```

使用[AudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)的[setVolume](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)和[getVolume](../harmonyos-references/arkts-apis-audio-audiorenderer.md#getvolume12)接口分别完成音频流音量的设置和获取。

示例代码如下所示：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // ...
3. // 设置音频流音量。
4. audioRenderer.setVolume(0.5).then(() => {  // 音量范围为[0.0-1.0]。
5. console.info('Invoke setVolume succeeded.');
6. // ...
7. }).catch((err: BusinessError) => {
8. console.error(`Invoke setVolume failed, code is ${err.code}, message is ${err.message}`);
9. // ...
10. });

12. // 获取音频流音量。
13. try {
14. let value: number = audioRenderer.getVolume();
15. console.info(`Indicate that the volume is obtained ${value}.`);
16. // ...
17. } catch (err) {
18. let error = err as BusinessError;
19. console.error(`Failed to obtain the volume, error ${error}.`);
20. // ...
21. }
```
