---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-18
title: 如何在录制采集音频时获取麦克风的音量大小
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何在录制采集音频时获取麦克风的音量大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bafa9022ce22e5e2812d2a8b08edaab07e87f57742f59a90b9d7400596e95a71
---

## 问题现象

使用AVRecorder或者AudioCapturer录制音频时，如何实时获取麦克风的音量大小。

## 问题根因

AVRecorder或者AudioCapturer暂不支持监听麦克风音量大小，同时不提供相应API接口。

## 解决措施

1. AVRecorder可以通过[getAudioCapturerMaxAmplitude()](../harmonyos-references/arkts-apis-media-avrecorder.md#getaudiocapturermaxamplitude11)接口获取当前音频最大振幅，用以实现振幅UI效果。具体实现可参考[示例代码](https://gitcode.com/HarmonyOS-Cases/cases/tree/master/CommonAppDevelopment/feature/voicerecordynamiceffect)。
2. 还可以使用AudioVolumeGroupManager中的[getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)接口获取输入设备音频流的最大电平值，取值范围为[0, 1]。电平值越大，表示麦克风的音量越大。
