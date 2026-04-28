---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-playing-short-audio-based-soundpool
title: 基于SoundPool播放短音频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频播放系列开发实践 > 基于SoundPool播放短音频
category: best-practices
scraped_at: 2026-04-28T08:20:38+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a97741bf48419d99eb9e2dc2420db424680ed8803716ee5eb9dcdf19b3c8e534
---

## 概述

SoundPool提供短音频的播放能力，当需要播放一些急促简短的音效（如应用启动音、消息通知音等）时，建议调用SoundPool，应用只需要提供音频资源来源，不负责数据解析和解码就可达成播放效果。指导开发者使用SoundPool开发播放短音频功能，主要涉及基础播放、倍速播放、循环播放、音量调节等开发场景。

本文是音频播放系列文章的第5篇，实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/h3rJ1uK_QEODhmloe2yhyw/zh-cn_image_0000002555337527.png?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=B1975B490F69DF459DA721567FD449C5D665F33AD7FA62E28970382EF6CFA26F "点击放大")

## 规格与限制

* 支持的文件大小：

  SoundPool当前支持播放解码后1MB以下的音频资源，解码后大小超过1MB的长音频将截取前面的1MB大小数据进行播放。

* 支持的协议如下：

| 协议类型 | 协议描述 |
| --- | --- |
| 本地点播 | 协议格式：支持file descriptor，禁止file path。 |

* 支持的音频播放格式如下：

| 音频容器规格 | 编码规格描述 |
| --- | --- |
| m4a | 音频格式：AAC |
| aac | 音频格式：AAC |
| mp3 | 音频格式：MP3 |
| ogg | 音频格式：VORBIS |
| wav | 音频格式：PCM |

* SoundPool实例数量限制：
  + API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
  + API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

## 实现原理

通过创建SoundPool实例，加载和播放对应的音频资源。支持设置音频流的播放速率、音量、循环模式等播放参数。

说明

使用SoundPool播放短音频，且[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)指定为Music、Movie、AudioBook等类型时，其申请焦点时默认为并发模式，不会影响其他音频，若开发过程中涉及焦点管理的问题，请参考[音频焦点管理解决方案](bpta-audio-focus-management.md#section8811136185118)。

## 开发步骤

1. 创建SoundPool实例。

```
1. // The parameter 'usage' in audioRenderInfo takes the values of STREAM_USAGE_UNKNOWN, STREAM_USAGE_MUSIC, and STREAM_USAGE_MOVIE.
2. // When STREAM_USAGE_AUDIOBOOK is used, the SoundPool plays short sounds in the mixing mode and will not interrupt the playback of other audio.
3. let audioRendererInfo: audio.AudioRendererInfo = {
4. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // The type of audio stream used: Music. Configure according to the business scenario and refer to StreamUsage.
5. rendererFlags: 1 // Set rendererFlags to 1 for low-latency path playback
6. };
7. // Create an instance of soundPool.
8. this.soundPool = await media.createSoundPool(14, audioRendererInfo);
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L39-L46)

2. 设置[on('loadComplete')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onloadcomplete)回调，用于监听“资源加载完成”的状态。开发者应在监听到“资源加载完成”的状态后，方可执行后续的播放操作，否则系统会抛出异常。

```
1. // Loading completion callback.
2. async loadCallback() {
3. if (!this.soundPool) {
4. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
5. return;
6. }
7. this.soundPool.on('loadComplete', (soundId: number) => {
8. this.soundId = soundId;
9. hilog.info(0xFF00, 'SoundPool', `load soundPool soundId: ${this.soundId}`);
10. })
11. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L64-L75)

3. 设置[on('playFinished')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onplayfinished)或者[on('playFinishedWithStreamId')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onplayfinishedwithstreamid18)回调，用于监听“播放完成”，以便于在播放后处理对应的业务。

```
1. setPlayFinishedCallback() {
2. if (!this.soundPool) {
3. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
4. return;
5. }
6. this.soundPool.on('playFinished', () => {
7. hilog.info(0xFF00, 'SoundPool', `Succeeded in playFinished`);
8. })
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L79-L87)

4. 设置[on('error')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onerror)回调，进行错误类型的监听，以便遇到播放问题后，进行快速定位。

```
1. // Set error type listening.
2. setErrorCallback() {
3. if (!this.soundPool) {
4. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
5. return;
6. }
7. this.soundPool.on('error', (error: BusinessError) => {
8. hilog.error(0xFF00, 'SoundPool',
9. `error happened, error code is :' ${error.code}, error message is ${error.message}`);
10. })
11. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L91-L101)

5. 调用[load()](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load)方法，加载音频资源。

```
1. // Load audio resources.
2. let context = this.getUIContext().getHostContext();
3. let fileDescriptor = await context!.resourceManager.getRawFd('test.ogg');
4. this.soundId = await this.soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L53-L56)

6. 调用[play()](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#play)方法，播放音频资源。

```
1. async playSoundPool() {
2. if (!this.soundPool) {
3. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
4. return;
5. }
6. this.soundPool.setPriority(this.soundId, 999);
7. // Please perform the 'play' operation only after the audio resource is fully loaded, that is, after receiving the 'loadComplete' callback.
8. this.streamId = await this.soundPool.play(this.soundId);
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L105-L113)

7. 开发者可以通过配置播放参数PlayParameters实现不同的播放效果，也可以通过单独调用[setLoop](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#setloop)、[setPriority](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#setpriority)、[setvolume](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#setvolume)、[setRate](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#setrate-1)等函数来实现不同的播放效果。下面以设置短音频的循环模式为例，其他设置方法的调用方式相同。

```
1. if (!this.soundPool) {
2. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
3. return;
4. }
5. // ...
6. await this.soundPool.setLoop(this.streamId, 2);
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L225-L232)

8. 停止播放，取消监听，释放SoundPool实例。

```
1. async setOffCallback() {
2. if (!this.soundPool) {
3. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
4. return;
5. }
6. this.soundPool.off('loadComplete');
7. this.soundPool.off('playFinished');
8. this.soundPool.off('error');
9. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L135-L143)

```
1. async release() {
2. if (!this.soundPool) {
3. hilog.error(0xFF00, 'SoundPool', `soundPool is undefined`);
4. return;
5. }
6. // Terminate the playback of the specified stream.
7. await this.soundPool.stop(this.streamId);
8. // Uninstall audio resources.
9. await this.soundPool.unload(this.soundId);
10. // Turn off the monitoring.
11. this.setOffCallback();
12. // Release SoundPool.
13. await this.soundPool.release();
14. this.streamId = 0;
15. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio/blob/master/entry/src/main/ets/pages/Index.ets#L117-L131)

## 示例代码

* [基于SoundPool播放短音频](https://gitcode.com/HarmonyOS_Samples/soundpool-play-short-audio)
