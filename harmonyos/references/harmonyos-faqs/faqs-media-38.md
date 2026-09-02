---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-38
title: AVPlayer播放直播流报错，错误码801，不支持loop
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVPlayer播放直播流报错，错误码801，不支持loop
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:15478e741095094aef3b32f02ffe27a08635fa23a6af7a72cd03c0392c46172c
---

## 问题现象

设置[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)为非循环播放，使用AVPlayer播放直播流音频失败，错误码为801，错误信息为：直播流不支持loop。

## 背景知识

[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)将音视频媒体资源转码为可供渲染的图像和可听到的音频模拟信号，并通过输出设备进行播放，应用只需要提供媒体来源，不负责数据解析和解码就可实现播放效果。AVPlayer支持网络直播，支持hls/http-flv协议的直播流，具体可参考：[支持的格式与协议](../harmonyos-guides/media-kit-intro.md#支持的格式与协议)。

## 问题定位

使用AVPlayer播放直播流，错误日志信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/yf7yXXMgTuuq_mW74j81Yg/zh-cn_image_0000002628392786.png "点击放大")

根据错误日志信息可以知道，当前媒体流为直播流，直播流不支持循环播放。

查看代码，发现在AVPlayer的prepared状态下设置了[属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)中的loop属性为false，而AVPlayer在直播场景下不支持设置loop属性，无论是设置loop属性为false还是true，都不支持。

## 分析结论

AVPlayer在直播场景下不支持设置loop属性，在直播场景下，无论是设置loop属性为false还是true，AVPlayer都会播放失败。

## 修改建议

在播放直播流时，不要设置loop属性。在直播场景下，除了不支持设置loop属性外，同样不支持[seek](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)、[setSpeed](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)、[setPlaybackRate](../harmonyos-references/arkts-apis-media-avplayer.md#setplaybackrate20)，如果在直播场景进行这些操作，AVPlayer会报错，错误码为801。
