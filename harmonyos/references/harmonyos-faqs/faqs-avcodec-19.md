---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-19
title: 视频编码器初始化完成后能否动态修改画面宽高
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 视频编码器初始化完成后能否动态修改画面宽高
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:41df1c40f47a3bef4f56af2bf54ea7787142263652d78b4435385a9d97cd71ea
---

## 问题现象

视频编码器在初次配置完宽高并且启动后，是否还能在编码器编码过程中动态修改配置的画面宽高？

## 解决方案

编码器在编码过程中可以动态修改配置的画面宽高，其中修改方式可以分为以下几种场景。通过[OH\_AVCapability\_IsHardware](../harmonyos-references/capi-native-avcapability-h.md#oh_avcapability_ishardware)函数区分视频编码器是硬件编码器还是软件编码器。

1. 如果视频编码器为硬件编码器且修改后的宽高比初次配置的宽高都要小，则无需重新配置参数，只需要直接传入新的yuv图片即可，输入的图片宽高是多少，输出的宽高就是多少。
2. 如果视频编码器为硬件编码器且修改后的宽或高大于初次配置的宽或高，或者视频编码器为软件编码器，则需要重新配置参数，步骤流程为通过[OH\_VideoEncoder\_Reset](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_reset)函数将[编码器状态机](../harmonyos-guides/video-encoding.md#状态机调用关系)调整为Initialized状态，然后再通过[OH\_VideoEncoder\_Configure](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)函数配置新参数。具体可参考：[视频编码器Surface模式](../harmonyos-guides/video-encoding.md#surface模式)中步骤15：调用OH\_VideoEncoder\_Reset()重置编码器。

## 总结

| 编码器类型 | 新配置宽高变化 | 宽高配置修改方法 |
| --- | --- | --- |
| 硬件编码器 | 新宽 ≤ 旧宽 且 新高 ≤ 旧高 | 无需重新配置，直接传入新图片。 |
| 硬件编码器 | 新宽 > 旧宽 或 新高 > 旧高 | 需要重置编码器后，重新配置宽高参数。 |
| 软件编码器 | 新宽 ≠ 旧宽 或 新高 ≠ 旧高 | 需要重置编码器后，重新配置宽高参数。 |
