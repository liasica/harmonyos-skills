---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-49
title: setDefaultOutputDevice切换听筒扬声器耗时较长
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > setDefaultOutputDevice切换听筒扬声器耗时较长
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ecf221d70c50c9bf1851076189456c582409f614794f6a3d6a50937757c4818e
---

## 问题现象

使用setDefaultOutputDevice接口切换扬声器听筒时，耗时较长，中断时间较长，什么原因？

## 背景知识

AudioRenderer的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)支持应用切换听筒和扬声器设备。

## 问题定位

* 根据hilog日志，搜索[SetDefaultOutputDevice]set to找到切换设备的地方。
* 日志中发现有6条音频输出流，并且有4条是usage等于17-VoIP视频通话流，音频流类型可查看[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)。

  ```txt
  I C02B8B/audio_server/AudioCoreService: [comm][DeviceFetchStart] by SetDefaultOutputDevice for 6 output streams
  ```
* 输出设备切换时，会对每个音频输出流做静音操作，避免切换时的杂音，可查看到日志中存在多条静音与取消静音操作日志，音频流切换时间是累计的，共耗时约1.1s，有明显的中断。

  ```txt
  I C02B89/audio_server/AudioRenderSink: [SetSinkMuteForSwitchDevice]set primary mute 1 // 静音操作
  ...
  I C02B89/audio_server/AudioRenderSink: [SetSinkMuteForSwitchDevice]set voip mute 0 // 取消静音操作
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Evt4nCtiQpu3snbrUrEIGw/zh-cn_image_0000002658792059.png "点击放大")

## 分析结论

应用起了多条音频输出流，切换设备时每条音频流会有静音和取消静音操作，操作耗时会累计，出现明显中断现象。

## 修改建议

应用侧排查，不使用的音频流及时[release释放](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)掉，避免切换耗时。
