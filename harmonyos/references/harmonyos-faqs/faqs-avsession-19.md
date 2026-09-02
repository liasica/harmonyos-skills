---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-19
title: 如何解决音频播放控制通知栏进度状态不更新问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 如何解决音频播放控制通知栏进度状态不更新问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:22+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c2df47bddee59956515e91facc8a197045d773fab5c36f5ffd86647984559752
---

## 问题现象

播放音频时，创建并设置AVSessionManager会话有如下情况：

* 设置播放状态后通知栏进度不会更新；
* 通知栏下拉后更新恢复正常；
* 锁屏后打开恢复正常更新。

## 背景知识

* [AVSession Kit](../harmonyos-guides/avsession-overview.md)：系统提供的音视频管控服务，统一管理系统中所有音视频行为。
* [Background Tasks Kit](../harmonyos-guides/background-task-overview.md)：后台任务管理；应用切到后台后资源会受到严格管控，应当选择合适的后台任务，以满足应用退至后台后继续运行的需求。
* [媒体会话提供方](../harmonyos-guides/using-avsession-developer.md)：音视频应用控制媒体会话控制方的媒体相关信息，及响应媒体会话控制方下发的播控命令。

## 问题定位

1. 对媒体类播放来说，通知栏进度条不生效，首先排查是否申请了AUDIO\_PLAYBACK的长时任务；
2. 排查是否正确设置了资源的时长、播放状态、播放位置、倍速等信息，播控中心将使用这些信息进行进度的展示。

## 分析结论

播控中心的播放状态初始化错误导致播放进度计算失败而不更新，在下拉状态栏或锁屏后重新设置了播放状态后恢复正常。

## 修改建议

1. 申请长时任务，避免进入挂起（Suspend）状态导致播放停止。当应用需要实现后台播放等功能时，需要使用BackgroundTasks Kit的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。对媒体类播放来说，需要申请AUDIO\_PLAYBACK的长时任务。
2. 正确初始化播控中心的播放资源，并在状态变化时更新，防止播放停止或播放进度计算错误。系统的播控中心将根据应用设置的资源。

**说明** 

* 只有当播放媒体的播放状态（state）、播放位置（position）、播放倍速（speed）发生变化的时候，才需要更新会话播放状态（AVPlaybackState），否则系统会发生计算错误。
* 应用在真实播放开始时，上报进度起始播放位置（position）；若播放存在缓冲（buffer）状态，可以先上报播放状态为[AVSessionManager.PlaybackState](../harmonyos-references/arkts-apis-avsession-e.md#playbackstate10).PLAYBACK\_STATE\_BUFFERING来通知系统不刷新进度。

具体可参考：[应用接入AVSession场景介绍-进度条](../harmonyos-guides/avsession-access-scene.md#设置进度条信息)。

## 总结

系统的播控中心播放进度会根据播放状态进行自动计算并刷新，应用只需要在播放的速率、位置等信息发生变化时更新即可。
