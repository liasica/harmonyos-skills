---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-57
title: OHAudio设置数据帧长不生效
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > OHAudio设置数据帧长不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:20a66285168e969c71cb2fb5687ba7ea64db10a550b481fb88ae3f1dba630c19
---

## 问题现象

在OHAudio中可以调用OH\_AudioStreamBuilder\_SetFrameSizeInCallback接口来设置音频数据的帧长。当播放采样率为32000Hz时设置帧长为10ms会显示调用成功但是实际不生效，当采样率为48000Hz时则调用正常。

## 解决方案

[OH\_AudioStreamBuilder\_SetFrameSizeInCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setframesizeincallback)接口在低时延播放时frameSize可设置为5ms、10ms、15ms、20ms音频数据对应的帧长，普通通路播放时frameSize可设置为20ms-100ms音频数据对应的帧长。

当设备支持低时延模式且采样率设置为48000的时候才会开启低时延模式，否则即使设置了低时延模式，系统仍会使用普通模式，详情可以参考[低时延模式限制](../harmonyos-guides/audio-fast-playback.md#低时延模式限制)。

当采样率设置为32000Hz时，由于不满足低时延模式要求，系统会仍然调用普通模式，而普通模式可设置的帧长为20ms-100ms，因此设置帧长为10ms时就不会生效。
