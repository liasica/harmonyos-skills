---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-45
title: AVPlayer播放音视频报错5400106
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVPlayer播放音视频报错5400106
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1687d52a4b732df25df2a1ff74b2a5c939223c74f11ada6565503902b046e615
---

## 问题现象

使用[AVPlayer](../harmonyos-guides/video-playback.md)播放音视频媒体资源，在设置媒体资源后，调用[prepare](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)准备播放时报错5400106，不支持的规格。本文介绍该类错误的排查思路。

## 背景知识

* [AVPlayer](../harmonyos-guides/video-playback.md)的主要工作是将音视频媒体资源转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。应用只需要提供流媒体来源，不负责数据解析和解码就可达成播放效果。
* [5400106-不支持的规格](../harmonyos-references/errorcode-media.md#section5400106-不支持的规格)：当前播放的媒体资源的格式规格不支持，用户需要切换为支持的规格。

## 问题定位

[AVPlayer](../harmonyos-guides/video-playback.md)只支持主流的容器格式与音视频编码规格。如果播放的媒体资源的规格格式不在AVPlayer支持的范围内，调用[prepare](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)准备播放时会报错5400106。常见的导致5400106报错的原因可按如下步骤排查：

1. 不支持的封装与编码格式。

   ```txt
   02-14 10:32:09.094   52681-52746   C02B2B/com.hua...layerCallback  com.huawe...lication  E     #785 OnErrorCb:errorCode 5400106, errorMsg Unsupported Format: unsupport interface, unsupport container format type
   ```

   从错误日志信息中可以看到“Unsupported Format: unsupport interface，unsupport container format type”，说明当前播放的媒体资源的音视频封装编码格式不在AVPlayer支持的范围内，导致播放出错。

   可以通过工具（如：ffprobe、mediaInfo等）查看媒体资源的封装格式与音视频轨道的编码格式，并检查是否为AVPlayer支持的格式。若当前设置的媒体资源的封装编码格式为不支持的格式，需要更换媒体资源。AVPlayer支持的音视频格式可参考：[支持的格式与协议](../harmonyos-guides/media-kit-intro.md#支持的格式与协议)。
2. 不支持的视频分辨率。

   ```txt
   02-14 11:21:46.572   20787-20886   C02B2B/com.hua...layerCallback  com.huawe...lication  E     #785 OnErrorCb:errorCode 5400106, errorMsg Unsupported Format: unsupport interface, unsupport video source type
   ```

   从错误日志信息中可以看到“Unsupported Format: unsupport interface, unsupport video source type”，说明当前媒体资源的视频轨道解码失败，常见的情况是视频分辨率不在支持的范围内。

   当前AVPlayer支持主流的视频分辨率（如4K/1080P/720P/480P/270P），超过该范围会导致AVPlayer播放失败。可以通过工具（如：ffprobe、mediaInfo等）查看媒体资源的视频分辨率，然后通过视频解码模块的[OH\_AVCapability\_IsVideoSizeSupported](../harmonyos-references/capi-native-avcapability-h.md#oh_avcapability_isvideosizesupported)判断视频解码器是否支持该视频分辨率大小。具体可参考：[设置正确的视频宽高](../harmonyos-guides/obtain-supported-codecs.md#设置正确的视频宽高)。
3. 不支持的音频采样率。

   ```txt
   02-14 11:39:06.684   30698-32139   C02B2B/com.hua...layerCallback  com.huawe...lication  E     #785 OnErrorCb:errorCode 5400106, errorMsg Unsupported Format: unsupport interface, unsupport audio sample rate
   ```

   从错误日志信息中可以看到：“Unsupported Format: unsupport interface, unsupport audio sample rate”，说明当前媒体资源的音频采样率不在支持的范围内。

   AVPlayer解码音频数据后会输出到音频服务（Audio Framework），由音频服务输出至音频驱动渲染，实现音频播放功能。因此AVPlayer播放的媒体资源的音频采样率必须满足音频服务对采样率的限制。音频采样率限制可参考：[支持的音频格式](../harmonyos-guides/audio-kit-intro.md#支持的音频格式)。

## 分析结论

AVPlayer在设置媒体资源后，调用[prepare](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)准备播放时报错5400106，是因为当前设置的媒体资源使用了AVPlayer不支持的格式规格。常见的不支持原因有：封装和编码格式不支持，视频分辨率不支持以及音频采样率不支持，需要根据日志信息具体定位分析。

## 修改建议

对于5400106，不支持的规格问题，需要用户切换为支持规格的媒体资源后使用AVPlayer播放。
