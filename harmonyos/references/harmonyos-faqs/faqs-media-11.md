---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-11
title: AVPlayer视频列表反复滑动播放失败问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVPlayer视频列表反复滑动播放失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ef7e9a249ea53232cbb6e32b6d082105ecd0b603eeaaa7364430c02b2d2a6bb
---

## 问题现象

应用视频列表播放功能，视频列表（自动播放）在反复上下滑动后，会出现播放失败问题。

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：提供功能完善一体化播放能力，应用只需要提供流媒体来源，不负责数据解析和解码就可达成播放效果。将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。
* [AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)：AVPlayer的状态机，可通过state属性主动获取当前状态，也可通过监听stateChange事件上报当前状态，状态机之间的切换规则，可参考[音频播放开发指导](../harmonyos-guides/using-avplayer-for-playback.md)。

## 问题定位

复现问题并抓取Hilog日志，查看播放失败时间点应用进程日志和系统日志，关键日志如下：

```txt
07-07 16:07:34.196 25836 25836 I A03D00/JSAPP: 自动播放-onAutoPlay: 82698--isShow:false
07-07 16:07:34.197 25836 25836 I A03D00/JSAPP: 自动播放-onAutoPlay: 24992--isShow:false
07-07 16:07:34.197 25836 25836 I A03D00/JSAPP: 自动播放-onAutoPlay: 93230--isShow:false
07-07 16:07:34.197 25836 25836 I A03D00/JSAPP: 自动播放-onAutoPlay: 65378--isShow:false
07-07 16:07:34.197 25836 25836 I C03906/AceVideo: [(100001:100001:scope)] Video[2336] trigger mediaPlayer stop
07-07 16:07:34.197 25836 25836 I C03900/Ace: [(100001:100001:scope)] Media player start to stop.
07-07 16:07:34.197 25836 26471 I C03906/AceVideo: [(100001:100001:scope)] Video[3738] trigger mediaPlayer play
07-07 16:07:34.197 25836 26471 I C03900/Ace: [(100001:100001:scope)] Media player start to play.
07-07 16:07:34.197 25836 26471 I C02B2B/MonitorClientObject: #30 0x9DCDE0 EnableMonitor
07-07 16:07:34.197  8808  8808 I C02B2B/media_service/PlayerServiceStub: #250 0x4F7700 Stub: OnRemoteRequest task: Player::Stop is received
07-07 16:07:34.197  8808 19652 I C02B2B/media_service/PlayerServiceStub: #250 0xB99700 Stub: OnRemoteRequest task: Player::Play is received
07-07 16:07:34.197  8808 27301 I C02B2B/media_service/AVSessionBackGround: #81 DelListener uid num 1
07-07 16:07:34.197  8808 26467 E C02B2B/media_service/PlayerServer: #674 Can not Stop, currentState is PLAYER_STOPPED
07-07 16:07:34.197  8808 27301 I C02B2B/media_service/AVSessionBackGround: #88 AddListener uid 20020215, player num 26
07-07 16:07:34.197  8808 27301 E C02B2B/media_service/PlayerServer: #540 Can not Play, currentState is PLAYER_STARTED
```

1. 日志分析。应用视频列表在上下滑动过程中，会记录视频播放组件是否在屏幕中显示，当组件在显示时，则更新组件播放状态并自动播放，当组件不在屏幕显示时，则记录isShow，更新播放状态并停止播放。
   * 在停止播放时，系统报如下错误：

     ```txt
     07-07 16:07:34.197  8808 26467 E C02B2B/media_service/PlayerServer: #674 Can not Stop, currentState is PLAYER_STOPPED
     07-07 16:07:55.077  8808 27593 E C02B2B/media_service/PlayerServer: #674 Can not Stop, currentState is PLAYER_STATE_ERROR
     ```
   * 在启动播放时，系统报如下错误：

     ```txt
     07-07 16:07:34.197  8808 27301 E C02B2B/media_service/PlayerServer: #540 Can not Play, currentState is PLAYER_STARTED
     ```
   * 在prepare时，系统报如下错误：

     ```txt
     07-07 16:07:35.695  8808 27301 E C02B2B/media_service/PlayerServer: #450 Can not Prepare, currentState is PLAYER_STARTED
     ```

   上述日志说明在视频列表切换时更新视频播放状态错误，视频在错误状态下停止或启动播放失败。
2. 视频播放状态示意如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/YZdFGJObTNyJIEjSm2scNg/zh-cn_image_0000002658792019.png "点击放大")

   * 当视频状态为stopped时，若需要重新播放视频，则需要将视频状态置为prepared后再播放。
   * 当视频出现error状态时，无法进行继续播放或停止播放，需要调用reset()重置视频状态或调用release()销毁重建。

## 分析结论

1. 在视频状态为error和stopped时进行视频停止播放，导致停止播放错误，无法结束。
2. 在视频状态为playing时进行视频开始播放和prepare()，导致开始播放和prepare错误。

## 修改建议

在进行视频播放状态切换时，要根据当前视频的播放状态按AVPlayer的状态机切换规则进行切换。

1. 可以通过on('error')监听视频是否进入error状态。处于error状态时，播放服务进入不可播控的状态，要求客户端设计容错机制，使用reset()重置或者release()销毁重建。
2. 在视频播放进入stopped状态，可以调用prepare()重新准备，也可以调用reset()重置，或者调用release()彻底销毁。
3. 在视频状态为stopped和initialized调用prepare()使视频进入prepared状态，之后才可开始进行播放。
