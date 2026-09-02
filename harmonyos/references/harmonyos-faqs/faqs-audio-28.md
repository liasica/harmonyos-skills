---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-28
title: 退出视频播放页面后，还有短暂声音残留
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 退出视频播放页面后，还有短暂声音残留
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:817dfb950cc33d1296c55be6eacdb3f136c53b8958d265485390fbc0a06ff767
---

## 问题现象

页面中有正在播放的视频，此时退出页面，仍然有短暂的声音残留。

## 背景知识

[AVPlayer.release()](../harmonyos-references/arkts-apis-media-avplayer.md#release9)是HarmonyOS中用于释放音视频播放资源的一个关键方法。通常在以下场景中调用AVPlayer.release()：

* 页面销毁时（onDestroy()）。
* 应用进入后台时（onBackground()）。
* 用户主动关闭播放功能时。
* 播放完成后，不再需要继续使用播放器时。

## 问题定位

查看应用的代码，搜索release关键词进行定位，查看在页面的相关生命周期（onDestroy()）中是否通过AVPlayer.release()方法销毁播放资源。当应用没有主动调用该方法进行资源的销毁时，视频播放依赖于系统的资源回收机制进行停止和资源释放，这个过程会延迟一个短暂的时间，导致退出页面后，还有短暂的声音残留。

## 分析结论

应用并未在页面的相关生命周期（onDestroy()或onPageHide()）中调用AVPlayer.release()方法销毁播放资源，导致退出播放页面后，仍然有短暂的声音残留。

## 修改建议

建议应用在页面销毁时主动停止并释放视频资源，参考[销毁播放资源](../harmonyos-references/arkts-apis-media-avplayer.md#release9)。
