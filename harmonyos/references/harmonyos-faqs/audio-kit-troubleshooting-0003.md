---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/audio-kit-troubleshooting-0003
title: 音视频播放音量不同步与被打断后状态异常问题定位
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 故障排查 > 音视频播放音量不同步与被打断后状态异常问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:14+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:ab040a435120d5d2b385485fec2da5a1ff24f3fe632d4520decaab77b79be96d
---

## 视频音量与系统音量不同步

### 问题现象

在视频页面调节音量大小，和系统的音量不同步。

### 定位过程

打开视频页，分别通过手势和系统按键调节音量，二者的调节结果不同，初步判断是视频音量和系统音量的控制之间没有添加连接。检查代码，发现应用视频加载使用的是AVPlayer接口，通过setVolume()方法实现的音量调节功能：

```ts
this.avPlayer.setVolume(this.playerModel.volume);
```

全局搜索AudioVolumeManager发现并没有监听系统音量变化的代码，手势调节只是控制视频音量大小，并没有通知系统音量变化，从而导致视频与系统的音量不同步。

### 分析结论

应用只通过setVolume()方法进行了视频音量的调节，没有通知系统音量同步变化。

### 修改建议

* 使用系统按键调节音量时，通过[on('streamVolumeChange')](../harmonyos-references/arkts-apis-audio-audiovolumemanager.md#onstreamvolumechange20)监听系统的音量变化，将变化值通过[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)方法同步给视频。
* 使用[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)手势调节视频音量时，通过调用音量面板组件，将调节的结果同步给系统音量。

## 播放视频时被打断导致播放状态异常

### 问题现象

应用在播放过程中，若播放的媒体数据涉及音频，存在会被其他应用打断后，该应用内与播控中心的播放状态显示异常的现象，以下图为例，播放视频时被语音助手小艺打断后，需连续点击2次后才继续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/eMQ8sz5_Sd6zOw430xqPFA/zh-cn_image_0000002793692187.png "点击放大")

### 定位过程

检查是否通过[on('audioInterrupt')](../harmonyos-references/js-apis-audiohaptic.md#onaudiointerrupt)对音频打断事件[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)进行监听，并根据音频打断类型[InterruptForceType](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)和中断提示[InterruptHint](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)正确管理视频播放状态。

1. 检查是否更新AVPlayer播放器的状态。如，对于打断类型为INTERRUPT\_FORCE（强制中断），中断提示为INTERRUPT\_HINT\_PAUSE（音频暂停）的打断事件，主动调用AVPlayer的[pause](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)接口来保证状态一致。
2. 当接入了媒体会话管理AVSession时，检查是否调用[setAVPlaybackState](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)同步播控中心的播放状态。接入详情可参考[应用接入AVSession场景介绍](../harmonyos-guides/avsession-access-scene.md)。
3. 处理音频打断事件时，也需检查UI组件播放状态的同步逻辑是否完善，避免视频播放的UI组件状态异常。

### 分析结论

在视频播放被打断的场景中，可能导致播放状态异常（或者不符合当前场景）的情形包括以下三种：

1. 未更新AVPlayer播放器的状态，导致不满足相应场景，如先暂停后恢复的场景，没有实现视频继续播放。
2. 未更新AVSession播放状态，导致播控中心状态和实际视频状态不一致。
3. 未更新UI组件播放状态，导致视觉呈现和实际视频状态不一致。

### 修改建议

在处理音视频打断事件时，需保持AVPlayer、AVSession和页面UI播放状态一致。以应用处理音视频播放被打断后，先暂停后恢复的场景为例（音频流状态交互可参考[音频焦点抢占流程](../best-practices/bpta-audio-focus-management.md#section1747213761316)）：

1. 当后台应用音频开始播放时，视频应用会监听到音频打断类型[InterruptForceType](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)为INTERRUPT\_FORCE（强制打断），中断提示[InterruptHint](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)为INTERRUPT\_HINT\_PAUSE（音频暂停）事件，此时系统内部会自动暂停视频播放，但AVPlayer播放器的状态不会自动变为暂停，应用需要主动调用AVPlayer的暂停接口来保证状态一致。
2. 当后台应用音频结束后，视频应用会监听到打断类型为INTERRUPT\_SHARE（共享打断），中断提示为INTERRUPT\_HINT\_RESUME（音频恢复）事件，应用需要在相应的事件中主动调用AVPlayer的播放接口完成恢复。

完整示例可以参考[使用AVPlayer播放视频完整示例](../harmonyos-guides/video-playback.md#运行完整示例)。
