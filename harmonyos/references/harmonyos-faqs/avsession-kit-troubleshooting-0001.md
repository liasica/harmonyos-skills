---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/avsession-kit-troubleshooting-0001
title: 音视频播控（AVSession）问题定位
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 故障排查 > 音视频播控（AVSession）问题定位
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:43+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:19653b64aec1e4087688207e737968decb66b121d5f731d46e4f413380303228
---

## 无线投屏时不能切换声音输出

### 问题现象

在使用系统无线投屏时，部分音频流无法投屏。

### 定位过程

使用正则表达式搜索：audio\_server.\*usage:，查看应用使用的音频流类型。

```txt
01-29 15:49:35.406   810   985 W C02B8B/audio_server/AudioPolicyService: [GetPreferredOutputDeviceDescInner]Invalid usage[0], return current device.
```

可见，应用的音频流类型：streamUsage:0，进一步查看[音频流使用类型的枚举](../harmonyos-references/arkts-apis-audio-e.md#streamusage)。根据枚举类型查阅，STREAM\_USAGE\_UNKNOWN的值是0，属于未知类型的音频流。可见应用使用的音频流类型为未知类型。

### 分析结论

应用使用了未知类型的音频流，投屏场景下，未知类型的音频流无法选择分布式设备播放，只能选择默认的扬声器设备。

### 修改建议

建议应用根据业务场景选用合适的音频流类型，目前在分布式设备上投播可支持的常见音频流类型包括：

* STREAM\_USAGE\_MOVIE
* STREAM\_USAGE\_AUDIOBOOK
* STREAM\_USAGE\_GAME
* STREAM\_USAGE\_MUSIC
* STREAM\_USAGE\_NAVIGATION
* STREAM\_USAGE\_ACCESSIBILITY
* STREAM\_USAGE\_VOICE\_ASSISTANT

## 如何解决音频播放控制通知栏进度状态不更新问题

### 问题现象

播放音频时，创建并设置AVSessionManager会话有如下情况：

* 设置播放状态后通知栏进度不会更新。
* 通知栏下拉后更新恢复正常。
* 锁屏后打开恢复正常更新。

### 定位过程

1. 对媒体类播放来说，通知栏进度条不生效，首先排查是否申请了AUDIO\_PLAYBACK的长时任务。
2. 排查是否正确设置了资源的时长、播放状态、播放位置、倍速等信息，播控中心将使用这些信息进行进度的展示。

### 分析结论

播控中心的播放状态初始化错误导致播放进度计算失败而不更新，在下拉状态栏或锁屏后重新设置了播放状态后恢复正常。

### 修改建议

1. 申请长时任务，避免进入挂起状态导致播放停止。当应用需要实现后台播放等功能时，需要使用BackgroundTasks Kit的能力，申请对应的长时任务，避免进入挂起状态。对媒体类播放来说，需要申请AUDIO\_PLAYBACK的长时任务。
2. 正确初始化播控中心的播放资源，并在状态变化时更新，防止播放停止或播放进度计算错误。系统的播控中心将根据应用设置的资源。

**说明** 

* 只有当播放媒体的播放状态、播放位置、播放倍速发生变化的时候，才需要更新会话播放状态（AVPlaybackState），否则系统会发生计算错误。
* 应用在真实播放开始时，上报进度起始播放位置；若播放存在缓冲状态，可以先上报播放状态为[AVSessionManager.PlaybackState](../harmonyos-references/arkts-apis-avsession-e.md#playbackstate10).PLAYBACK\_STATE\_BUFFERING来通知系统不刷新进度。
