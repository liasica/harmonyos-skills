---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-25
title: 播控中心通知栏显示问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 播控中心通知栏显示问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:118e2ba59983c6dc15aebc9b665f51e0f1bc27a84480a558b5c319a5c0b4cdc0
---

## 问题现象

播控中心通知栏的触发条件，显示效果，删除效果，以及常见问题说明。

## 背景知识

* [媒体播放状态](../harmonyos-guides/using-avsession-developer.md#基本概念)（AVPlaybackState）：用于描述媒体播放状态的相关属性，包含当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。
* [注册控制命令](../harmonyos-guides/avsession-access-scene.md#控制命令的处理)：应用接入AVSession，可以通过注册不同的控制命令来实现播控中心界面上的控制操作，即通过on接口注册不同的控制命令参数，即可实现对应的功能。具体的接口参考[接口注册](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10)。
* [AVSession Kit](../harmonyos-guides/avsession-overview.md)：AVSession Kit（Audio & Video Session Kit，音视频播控服务）是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。音视频应用在实现音视频功能的同时，需要接入媒体会话即AVSession Kit，参考[应用接入AVSession场景介绍](../harmonyos-guides/avsession-access-scene.md)。
* [播控中心](../design-guides/broadcasting-control-0000001957017133.md)：媒体播控用于显示当前设备正在播放的音视频媒体信息，以及帮助用户高效快捷地管理媒体内容的播放。其中，通知中心、锁屏与锁屏（沉浸模式）场景的播控页随接入播控中心的特定类型音频流启动而启动。且当手动删除通知中心播控页时，会通过播控中心对音频流进行暂停控制，待下次音频流启动时通知中心播控页恢复，同时锁屏与\*\*锁屏（沉浸模式）\*\*播控页恢复。

## 解决方案

1. 通知栏播控显示方式。
   * 正确接入AVSession。
     + 对于媒体类应用[接入AVSession](../harmonyos-guides/avsession-access-scene.md)，创建AVSession时需要选择会话类型（[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)）为'audio'或者'video'。
     + 在创建完成AVSession后，还必须要设元数据（AVMetadata），并至少注册一个控制命令（播放、暂停等），播控中心才能正常显示。
   * 通知栏播控显示条件。

     正确接入AVSession后，通知栏播控页会随音频流启动时，通过AVSession发通知，此时可以正常显示通知栏播控。若通知栏播控消失，则下次应用内音频流启动时恢复。
   * 通知栏播控自动删除。

     当播控中心状态为暂停状态时，会启动10min的计时，若持续10min均为暂停状态，通知栏播控将会自动删除。
2. 通知栏播控删除时的回调监听。
   * 删除通知栏播控时，播控中心将发出pause命令，若已[激活AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)，可以通过[on('pause')](../harmonyos-references/arkts-apis-avsession-avsession.md#onpause10)监听到播控中心发出的pause命令。
   * 通过监听长时任务取消。HarmonyOS6.0前，后台接入长时任务时，若删除通知栏播控，对应的长时任务将会被同步删除。HarmonyOS6.0后，删除通知栏播控后，将会发送长时任务通知，继续删除长时任务通知才会取消对应的长时任务。
3. 通知栏播控显示效果。

   参考[播控中心](../design-guides/broadcasting-control-0000001957017133.md)和[实况窗](../design-guides/system-features-live-view-0000001955186861.md)，播控中心是一种系统设计的实况窗。通知栏播控包括通知中心、锁屏页的播控展示。
