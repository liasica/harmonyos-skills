---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-27
title: 应用拉起麦克风导致播放中的音频中断
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 应用拉起麦克风导致播放中的音频中断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:93080b823b4c83080df5163e249fb074eb80a15e099ffdb8d5306cea0fcaeb22
---

## 问题现象

用户在应用中正在播放一段音频作为背景音乐，当用户点击应用中某个功能时。应用会拉起麦克风监听环境音，导致打断了当前正在播放的音频。

## 背景知识

* [Audio Kit简介](../harmonyos-guides/audio-kit-intro.md)：Audio Kit（音频服务）旨在提供场景化的音频播放和录制接口，助力开发者快速构建音频高清采集及沉浸式播放能力。
* [AVSession Kit简介](../harmonyos-guides/avsession-overview.md)：AVSession Kit（Audio & Video Session Kit，音视频播控服务）是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。
* [音频焦点和音频会话介绍](../harmonyos-guides/audio-playback-concurrency.md)：在应用播放或录制声音时，常出现与其他音频流的并发或中断情况，这对用户体验造成显著影响。系统预设的默认音频焦点策略，主要依据音频流类型（即播放流的StreamUsage和录制流的SourceType）及音频流启动的顺序进行决策。若默认的音频焦点策略无法满足特定场景的需求，应用程序可利用音频会话（AudioSession），调整本应用音频流所采用的音频焦点策略。
* [焦点模式](../harmonyos-guides/audio-playback-concurrency.md#焦点模式)：针对同一应用创建的多个音频流，应用可通过设置焦点模式（InterruptMode），选择由应用自主管控，或由系统统一管理。
* [音频会话（AudioSession）使用流程](../harmonyos-guides/audio-playback-concurrency-audio-session-overview.md#音频会话使用场景概述)。
* [使用AudioSession管理应用音频焦点(ArkTS)](../harmonyos-guides/audio-session-management.md)：对于涉及多个音频流并发播放的场景，系统已预设了默认的音频焦点策略，该策略将对所有音频流（包括播放和录制）实施统一的焦点管理。

## 问题定位

根据Hilog日志来排查问题：

1. 在日志中检索关键字"AVSession"，或者可以直接通过AVSession关键字来进行过滤。如下日志信息：

   ```txt
   07-03 09:36:31.157   3163-8927     C02B91/com.hua...ice/AVSession  com.huawe...aservice  I     [HandleEventWithThreadSafe]event:1|num:1|state:2
   07-03 09:36:31.157   3231-3231     A01C04/com.ohos.sceneboard/MC   com.ohos.sceneboard   I     CardMediaController_debug --> playstate change showing avsession callback : {"state":2,"speed":1,"position":{"elapsedTime":2439,"updateTime":1751506591156},"isFavorite":false,"duration":184064}, locale
   ```

   根据以上信息可以看到，AVSession在更新音频播放的元数据，如播放状态，进度位置，播放倍速，缓存的时间、播放时长等信息。
2. 继续在之后的日志中进行检索关键字“destroy”，如下日志信息：

   ```txt
   07-03 09:36:31.308   33144-33144   C02B8A/anco_au...ncoAudioProxy  anco_audio            I     [AncoAvSessionDestroy]AncoAvSessionDestroy
   07-03 09:36:31.308   33144-33144   C02B8A/anco_au...ncoAudioProxy  anco_audio            I     [Destroy]AvSession destroy
   07-03 09:36:31.308   33144-33144   C02B91/anco_audio/AVSession     anco_audio            I     [Destroy]enter
   07-03 09:36:31.309   1698-58913    C02B91/av_session/AVSession     av_session            I     [Destroy]AVSessionItem check service destroy event with service, check serviceCallback exist
   07-03 09:36:31.309   1698-58913    C02B91/av_session/AVSession     av_session            I     [Destroy]AVSessionItem send service destroy event to service
   07-03 09:36:31.309   1698-58913    C02B91/av_session/AVSession     av_session            I     [operator()]Start handle session release event
   0
   ```

   根据上述日志信息，可以看到此时触发了AVSession的destroy。对应于，用户点击功能后，应用拉起了麦克风功能。
3. 继续往下检查日志，如下日志信息：

   ```txt
   07-03 09:36:31.316   1698-18949    C02B91/av_session/AVSession     av_session            I     [~AVSessionItem]destroy with activate session, try deactivate it
   07-03 09:36:31.316   1698-18949    C02B91/av_session/AVSession     av_session            I     [Deactivate]Deactivate in
   07-03 09:36:31.316   1698-58913    C02B91/av_session/AVSession     av_session            I     [GetAllSessionDescriptors]GetAllSessionDescriptors with size=1, topSession:io.moreless.tide.next
   07-03 09:36:31.316   1698-18949    C02B91/av_session/AVSession     av_session            I     [Deactivate]Deactivate done
   ```

   可以看到这里进行音频播放的AVSession被终止，音频播放停止。

## 分析结论

由于拉起了麦克风功能，音频焦点变化未做相应处理，系统默认停止了当前的AVSession，导致播放的音频停止。

## 修改建议

根据[音频焦点管理解决方案](../best-practices/bpta-audio-focus-management.md)，不同应用间音频流焦点相互抢占情况，例如后播短视频会打断先播的后台音乐，按照系统默认焦点策略，后台音乐会停止播放，且短视频暂停或者播放结束后也不会恢复播放。

建议应用监听音频焦点事件，并在焦点发生变化时，根据InterruptEvent做出必要的响应。

参考监听音频焦点事件[处理音频焦点变化](../harmonyos-guides/audio-playback-concurrency.md#处理音频焦点变化)。
