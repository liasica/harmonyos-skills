---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-17
title: 应用中播放多个视频后有多个音频同时播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 应用中播放多个视频后有多个音频同时播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:ea21823a5e107e543257e930b524642fb1da1f1866b92deb4488c9168f56c3ab
---

## 问题现象

应用点击某个视频播放后退出，视频声音依然在播放，点击多个视频播放后，会有多个音频同时混合着播放。

## 背景知识

1. [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：可以实现端到端播放原始媒体资源，播放的全流程包含：创建AVPlayer，设置播放资源，设置播放参数（音量/倍速/焦点模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。
2. [AudioSession](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)：音频会话支持自定义本应用音频流的焦点策略，预设了以下四种音频并发模式：
   * 默认模式（CONCURRENCY\_DEFAULT）：即系统默认的[音频焦点策略](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)。
   * 并发模式（CONCURRENCY\_MIX\_WITH\_OTHERS）：和其他音频流并发。
   * 降低音量模式（CONCURRENCY\_DUCK\_OTHERS）：和其他音频流并发，并且降低其他音频流的音量。
   * 暂停模式（CONCURRENCY\_PAUSE\_OTHERS）：暂停其他音频流，待释放焦点后通知其他音频流恢复。

## 问题定位

1. 应用中全局搜索AudioSession音频会话，查看是否配置了CONCURRENCY\_MIX\_WITH\_OTHERS并发模式或者CONCURRENCY\_DUCK\_OTHERS降低音量模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/zx2T_578SLyDJKu0LUIhsg/zh-cn_image_0000002628392754.png)
2. 应用中排查视频播放返回首页后，应用有无调用AVPlayer实例的stop接口，停止播放音视频资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uq1HdYuLRKeRd45uV_J4dg/zh-cn_image_0000002658792025.png)

## 分析结论

应用中使用了音频会话策略，并设置模式为CONCURRENCY\_MIX\_WITH\_OTHERS并发模式，允许多个音频流并发播放；应用在播放视频返回首页后，未主动调用AVPlayer实例的stop接口，停止当前音频流的播放，导致并发播放的音频越来越多。

## 修改建议

1. 应用中修改音频会话的模式为默认模式（CONCURRENCY\_DEFAULT），系统会按照默认的音频焦点策略处理音频的播放，如应用当前正在播放音乐，后面又重启了一个音乐播放，这时默认的处理策略是后播音乐正常播放，先播音乐停止播放，这点可以参考官网[典型场景](../harmonyos-guides/audio-playback-concurrency.md#典型场景)。
2. 应用中在播放视频返回首页后，主动调用AVPlayer实例的[stop](../harmonyos-references/arkts-apis-media-avplayer.md#stop9)接口，停止当前音频流的播放，避免多个音频同时播放场景的发生。
