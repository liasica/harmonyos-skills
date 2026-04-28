---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-18
title: 如何在录制采集音频时获取麦克风的音量大小
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何在录制采集音频时获取麦克风的音量大小
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ec2c2a0ea024d1e6ed32bdcbafa431b265a2f64ff65560ee30dfd0ea110cc07c
---

**问题现象**

使用AVRecorder或者AudioCapturer录制音频时，如何实时获取麦克风的音量大小。

**问题根因**

AVRecorder或者AudioCapturer暂不支持监听麦克风音量大小，同时不提供相应API接口。

**解决****措施**

（1）AVRecorder可以通过[getAudioCapturerMaxAmplitude()](../harmonyos-references/arkts-apis-media-avrecorder.md#getaudiocapturermaxamplitude11)接口获取当前音频最大振幅，用以实现振幅UI效果。具体实现可参考[示例代码](https://gitcode.com/HarmonyOS-Cases/cases/tree/master/CommonAppDevelopment/feature/voicerecordynamiceffect)。

（2）还可以使用AudioVolumeGroupManager中的[getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)接口获取输入设备音频流的最大电平值，取值范围为[0, 1]。电平值越大，表示麦克风的音量越大。
