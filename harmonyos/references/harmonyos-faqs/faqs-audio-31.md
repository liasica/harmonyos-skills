---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-31
title: 应用打开时中断了听书功能
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 应用打开时中断了听书功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d2d8137b381e42c26e5c16435ff9cedd23ce16a95ce586a7771ddce8f80010b8
---

## 问题现象

用户在使用听书功能的情况下，打开应用在广告页面时，听书功能被中断掉，进入应用后也没恢复。

## 背景知识

1. 为解决多音频流播放冲突问题，系统采用了音频焦点机制，即只有获得音频焦点的音频流可以正常播放，失去音频焦点的音频流则不能播放，系统[音频焦点管理](../harmonyos-guides/audio-playback-concurrency.md#音频焦点)机制提供了四类音频中断策略：
   * 终止策略(Stop)：停止先播音频流，使其永久失焦，待后播音频流结束后，先播音频流不恢复播放。
   * 暂停策略(Pause)：暂停先播音频流，使其暂时失焦，待后播音频流结束后，先播音频流恢复播放。
   * 降音策略(Duck)：与先播音频流并发播放，并且降低先播音频流的音量，待后播音频流结束后，先播音频流恢复音量。
   * 并发策略(Mix)：与先播音频流并发播放。

2. 若系统[音频焦点策略](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)无法满足用户的音频播放体验需求，系统提供了音频会话([AudioSession](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略))，以便应用精细化管理和自定义调整中断策略。
3. [AudioConcurrencyMode](../harmonyos-references/arkts-apis-audio-e.md#audioconcurrencymode12)：代表音频会话支持的默认、并发、降低音量、暂停四种音频并发模式。

## 问题定位

1. 应用中搜索AudioRenderer或者AVPlayer相关接口，查看应用是否有播放音频的功能，简单示例如下：

   ```ts
   audioRenderer.start((err: BusinessError) => {
     if (err) {
       console.error(`Renderer start failed, code is ${err.code}, message is ${err.message}`);
     } else {
       console.info('Renderer start success.');
     }
   });
   ```

   ```ts
   avPlayer.play((err: BusinessError) => {
     if (err) {
       console.error(`Failed to play,error message is ${err.message}`);
     } else {
       console.info('Succeeded in playing');
     }
   });
   ```
2. 应用中搜索AudioConcurrencyMode并发模式，查看应用有无使用音频会话，自定义音频中断策略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/kunEZIaKRg6Vb3Pjltrfhw/zh-cn_image_0000002658911833.png)

## 分析结论

1. 应用中未采用音频会话[AudioSession](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)自定义音频中断策略，应用会按照系统默认焦点策略处理多个音频流之间的并发播放；
2. 先播听书音频流类型是电子书，后播音乐音频流类型是音乐时，按照[音频焦点策略](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)，会停止先播听书音频流，使其永久失焦，即使后播音频流结束，先播的听书音频流也不会恢复播放。

## 修改建议

1. 在使用系统默认焦点策略的情况下，先播音乐的音频流类型是电子书，可调整后播音乐的音频流类型。
   * 调整后播音乐的音频流类型为游戏，这时的默认焦点策略是先播和后播的两个音频流并发播放，不会中断先播的听书功能，可通过调整音频流使用类型[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为STREAM\_USAGE\_GAME实现。
   * 调整后播音乐的音频流类型为闹钟或者语音信息，这时的默认焦点策略是暂停先播的听书功能，待后播音频流结束后，先播的听书功能会恢复播放，可通过调整音频流使用类型[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为STREAM\_USAGE\_ALARM或者STREAM\_USAGE\_VOICE\_MESSAGE实现。

2. 应用中采用音频会话[AudioSession](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)自定义音频中断策略，AudioSession将在系统默认策略的基础上，进行适当的策略调整。
   * 应用设置音频会话为并发模式[CONCURRENCY\_MIX\_WITH\_OTHERS](../harmonyos-guides/audio-session-management.md#音频会话策略)，系统将直接采取并发策略，允许先播电子书和后播音频并发播放。
   * 应用设置音频会话为暂停模式[CONCURRENCY\_PAUSE\_OTHERS](../harmonyos-guides/audio-session-management.md#音频会话策略)，先播电子书和后播音频的系统默认焦点策略是停止先播电子书，设置的AudioSession会话策略为Pause模式，其优先级低于默认策略Stop模式，满足AudioSession调整原则，最终系统按照暂停策略(Pause)先暂停先播音频电子书，待后播音频结束后，先播电子书会恢复播放。
