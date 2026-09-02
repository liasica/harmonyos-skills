---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-13
title: PC设备视频暂停后恢复播放报错
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > PC设备视频暂停后恢复播放报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:83b6f8d2c61cc469538ac2cd20ad93fa5d278b05fe8a724c5c779c4bc862b72b
---

## 问题现象

PC设备视频正常播放时，点击暂停后，再点击播放报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/A4KRnMxyR1G091HhkWnVgQ/zh-cn_image_0000002628552644.png "点击放大")

## 背景知识

[AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)可以播放音视频，播控流程需要符合状态机逻辑，播放状态变化示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/6z4Cy1f1S1-C13L5_9lNzQ/zh-cn_image_0000002658911963.png "点击放大")

## 问题定位

过滤Hilog日志中media\_service媒体服务的日志信息，查看播放器流程是否正常，如果播放器状态变化与实际显示不符，说明播放器状态机回调处理时出现问题。

```shell
// 媒体服务日志显示播放器状态切换为inited状态
06-10 08:24:22.977  1737 64160 I C02B2B/media_service/PlayerServer: #1798 instance: 0xDB4240 change state to inited_state
```

```shell
// Callback State change说明播放器状态机回调变更，currentState is PLAYER_STATE_ERROR说明状态机切换发生错误
06-10 08:24:22.977  1737 64160 I C02B2B/media_service/PlayerServerTaskMgr: #212 0xDB43C0 task[preparing->prepared done] end
06-10 08:24:22.978  1737 64160 I C02B2B/media_service/PlayerServerState: #153 0xEEA6D8 Callback State change, currentState is PLAYER_STATE_ERROR
```

```shell
// 播放器状态机回调错误，返回unsupport interface错误信息
06-10 08:24:22.978  1737 64160 E C02B2B/media_service/HiPlayerCallbackLooper: (DoReportError(), 252): Report error, error type: 0 error value: 331350544
06-10 08:24:22.978  1737 64160 E C02B2B/media_service/PlayerListenerProxy: #91 player callback onError, errorCode: 331350544, errorMsg: unsupport interface
```

## 分析结论

界面截图显示暂停按钮状态，然而播放器实际状态没有进入paused状态，而是initialized状态，此时点击播放按钮，无法直接从inited状态变化到playing状态，从而导致播放器错误，日志信息中体现的当前状态为PLAYER\_STATE\_ERROR，说明在状态变化时发生了错误。

## 修改建议

[参考demo](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSVideo/entry/src/main/ets/pages/Index.ets)中setAVPlayerCallback方法对于状态机逻辑的监听变化，避免状态的异常导致播放器报错。
