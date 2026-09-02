---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-26
title: 视频音量与系统音量不同步
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 视频音量与系统音量不同步
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f22a67265e9d0ed34c2277e91b064c7cbe4d3eeb677475837b9e0c35a2f4e6f7
---

## 问题现象

在视频页面调节音量大小，和系统的音量不同步。

## 背景知识

通过手势调节音量是视频开发中的常见功能。在HarmonyOS中，系统提供了[Video组件](../harmonyos-guides/arkts-common-components-video-player.md)以及[AVPlayer接口](../harmonyos-references/arkts-apis-media-avplayer.md)供开发者进行视频开发，同时提供了如下调节音量的方法：

* 通过添加[音量面板组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md)来调节系统音量。
* 系统音量接口[AudioVolumeManager](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md)，可以和音量面板组合使用调节系统音量。
* 通过AVPlayer接口中的[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)方法实现管理音频流音量。

## 问题定位

打开视频页，分别通过手势和系统按键调节音量，二者的调节结果不同，初步判断是视频音量和系统音量的控制之间没有添加连接。检查代码，发现应用视频加载使用的是AVPlayer接口，通过setVolume()方法实现的音量调节功能：

```screen
this.avPlayer.setVolume(this.playerModel.volume);
```

全局搜索AudioVolumeManager发现并没有监听系统音量变化的代码，手势调节只是控制视频音量大小，并没有通知系统音量变化，从而导致视频与系统的音量不同步。

## 分析结论

应用只通过setVolume()方法进行了视频音量的调节，没有通知系统音量同步变化。

## 修改建议

* 使用系统按键调节音量时，通过[on('streamVolumeChange')](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#onstreamvolumechange20)监听系统的音量变化，将变化值通过[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)方法同步给视频。
* 使用[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)手势调节视频音量时，通过调用音量面板组件，将调节的结果同步给系统音量。

## 常见FAQ

Q：是否有控制系统音量进度条的位置或者显示隐藏的API？

A：目前没有控制系统音量进度条位置或显隐的API，可以给页面增加[音量面板组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md)并使用[Position](../harmonyos-references/ts-types.md#position)属性将面板移出屏幕外，以实现系统音量进度条和音量面板的隐藏效果。
