---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-46
title: 播放视频时被打断导致播放状态异常
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 播放视频时被打断导致播放状态异常
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3ade0f79731bc8bd96fa304a2cd01ecd312835a4733472be737494cb7aac05f6
---

## 问题现象

应用在播放过程中，若播放的媒体数据涉及音频，存在会被其他应用打断后，该应用内与播控中心的播放状态显示异常的现象，以下图为例，播放视频时被语音助手小艺打断后，需连续点击2次后才继续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/AcPuZcsSS3i0FbAfSJAShg/zh-cn_image_0000002658911951.png "点击放大")

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：AVPlayer主要工作是将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放（[Interface (AVPlayer)](../harmonyos-references/arkts-apis-media-avplayer.md)）。
* [AVSession Kit（音视频播控服务）](../harmonyos-guides/avsession-overview.md)：AVSession Kit是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力（[AVSession相关API](../harmonyos-references/js-apis-avsession.md)）。
* [音频焦点和音频会话](../harmonyos-guides/audio-playback-concurrency.md)：在应用播放或录制声音时，常出现与其他音频流的并发或中断情况，系统预设了默认的[音频焦点策略](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)，同时也提供了[音频会话管理](../harmonyos-guides/audio-session-management.md)，允许应用自定义其音频流的焦点策略。
* 应用在播放音频（含视频）的过程中，若有其他音频流申请音频焦点（如用户唤起小艺、打开其他应用播放音视频等），系统会根据[音频焦点策略](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)进行焦点处理。如果系统判定应用音频流的焦点有变化，会自动执行一些必要的操作，如：执行暂停、继续、降低音量、恢复音量等操作，并通过音频打断事件（[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)）通知到应用。以中断提示为音频暂停为例：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/FzKKHGAcSS2sqOnmsNKa5A/zh-cn_image_0000002628392740.png)
* [on('audioInterrupt')](../harmonyos-references/js-apis-audiohaptic.md#onaudiointerrupt)：监听音频中断事件（当音频焦点发生变化时触发）。当收到音频打断事件（[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)）时，应用根据其音频打断类型（[InterruptForceType](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)）和中断提示（[InterruptHint](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)）做出相应的处理策略。

  **须知** 

  如果使用了AVPlayer播放视频，audioRendererInfo会被默认设置成Movie，应用无需处理。

  使用on('audioInterrupt')监听音频打断时，要注意使用的视频资源必须有音频流，否则无法触发音频打断事件。

## 问题定位

检查是否通过[on('audioInterrupt')](../harmonyos-references/js-apis-audiohaptic.md#onaudiointerrupt)对音频打断事件[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)进行监听，并根据音频打断类型[InterruptForceType](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)和中断提示[InterruptHint](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)正确管理视频播放状态。

1. 检查是否更新AVPlayer播放器的状态。如，对于打断类型为INTERRUPT\_FORCE（强制中断），中断提示为INTERRUPT\_HINT\_PAUSE（音频暂停）的打断事件，主动调用AVPlayer的[pause](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)接口来保证状态一致。
2. 当接入了媒体会话管理AVSession时，检查是否调用[setAVPlaybackState](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)同步播控中心的播放状态。接入详情可参考[应用接入AVSession场景介绍](../harmonyos-guides/avsession-access-scene.md)。
3. 处理音频打断事件时，也需检查UI组件播放状态的同步逻辑是否完善，避免视频播放的UI组件状态异常。

## 分析结论

在视频播放被打断的场景中，可能导致播放状态异常（或者不符合当前场景）的情形包括以下三种：

1. 未更新AVPlayer播放器的状态，导致不满足相应场景，如先暂停后恢复的场景，没有实现视频继续播放。
2. 未更新AVSession播放状态，导致播控中心状态和实际视频状态不一致。
3. 未更新UI组件播放状态，导致视觉呈现和实际视频状态不一致。

## 修改建议

在处理音视频打断事件时，需保持AVPlayer、AVSession和页面UI播放状态一致。以应用处理音视频播放被打断后，先暂停后恢复的场景为例（音频流状态交互可参考[音频焦点抢占流程](../best-practices/bpta-audio-focus-management.md#section1747213761316)）：

1. 当后台应用音频开始播放时，视频应用会监听到音频打断类型[InterruptForceType](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)为INTERRUPT\_FORCE（强制打断），中断提示[InterruptHint](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)为INTERRUPT\_HINT\_PAUSE（音频暂停）事件，此时系统内部会自动暂停视频播放，但AVPlayer播放器的状态不会自动变为暂停，应用需要主动调用AVPlayer的暂停接口来保证状态一致。
2. 当后台应用音频结束后，视频应用会监听到打断类型为INTERRUPT\_SHARE（共享打断），中断提示为INTERRUPT\_HINT\_RESUME（音频恢复）事件，应用需要在相应的事件中主动调用AVPlayer的播放接口完成恢复。

完整示例可以参考[使用AVPlayer播放视频完整示例](../harmonyos-guides/video-playback.md#运行完整示例)。
