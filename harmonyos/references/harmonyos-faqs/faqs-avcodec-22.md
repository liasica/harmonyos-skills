---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-22
title: 如何实现视频压缩
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 如何实现视频压缩
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e423e2ce85245a9c8d6a48bff42419d3b73d7f13db4b7d0861d34da126171b94
---

## 问题现象

当视频文件体积过大，需要减小其容量以利于存储或传输，那么如何通过视频压缩技术来实现呢？

## 背景知识

* videoCompressor核心功能是压缩视频体积或转换视频格式，要实现压缩或转换，必须依赖两个关键步骤：
  1. 解封装（Demux）：拆开视频文件，提取内部的视频流等。
  2. 编解码（Codec）：对视频流进行解码（解压）和重新编码（压缩）。关系总结：解封装是第一步，编解码是第二步，最后再封装成新文件。
* [AVCodec Kit](../harmonyos-guides/avcodec-kit-intro.md)是媒体系统中视频的编解码、媒体文件的解析、封装、媒体数据输入等原子能力，开发者可以调用视频编码模块的Native API接口，通过调用Native侧的编码器完成视频编码，即将未压缩的视频数据压缩成视频码流。
* [AVTranscoder](../harmonyos-guides/media-kit-intro.md#avtranscoder)主要用于将已压缩编码的视频文件按照指定参数转换为另一种格式的视频。支持修改源视频文件的编码参数（格式、码率）和封装格式，以达到修改视频大小的目的。
* 容器格式和编码标准的关系：
  + 容器格式（MP4、MPEG-TS）：决定文件如何“打包”。例如：MP4可以装H.264或H.265编码的视频，就像快递盒可以装纸质书或电子书。
  + 编码标准（H.264、H.265）：决定视频内容如何“压缩”。例如：H.265比H.264压缩率更高，但需要更强的硬件支持。

  | 术语 | 类型 | 作用 |
  | --- | --- | --- |
  | MP4 | 容器格式 | 封装视频流、字幕等。 |
  | MPEG-TS | 容器格式 | 专为流媒体设计的封装格式（如直播、电视）。 |
  | AVC/H.264 | 视频编码标准 | 高效压缩视频的规则（通用性强）。 |
  | HEVC/H.265 | 视频编码标准 | 更高效的压缩规则（体积更小，画质更好）。 |

## 解决方案

可通过videoCompressor压缩视频质量，或者通过AVCodec Kit、AVTranscoder转码或者改变源视频文件的编码参数（格式、码率）达到缩小视频大小的目的。

* **方案一**：可以使用[videoCompressor](https://gitee.com/openharmony-sig/ohos_videocompressor)压缩视频质量实现视频压缩。视频压缩实现思路参考[videoCompressor实现视频压缩功能](../architecture-guides/video_compress_demo-0000002248722292.md)。
* **方案二**：AVCodec Kit视频编码功能能够将未经压缩的视频数据传输至视频编码器进行编码处理。应用程序可以设定所需的编码格式、比特率、帧率等参数，并对编码输出进行控制，从而实现视频文件的压缩目的，编码器参数可参考[设置正确的音频编解码参数](../harmonyos-guides/obtain-supported-codecs.md#设置正确的音频编解码参数)。详细demo请参考：[AVCodecSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec#avcodecsample)。
* **方案三**：采用AVTranscoder实现视频转码功能，支持通过减少比特率和分辨率等方式来实现视频的压缩。详细demo请参考：[UseAVTranscoderVideo](https://gitcode.com/HarmonyOS_Samples/UseAVTranscoderVideo)。

## 常见FAQ

Q：通过videoCompressor压缩视频是否可以指定压缩分辨率？

A：压缩质量支持COMPRESS\_QUALITY\_HIGH、COMPRESS\_QUALITY\_MEDIUM、COMPRESS\_QUALITY\_LOW参数，V1.0.6版本无法指定压缩分辨率。

## 总结

三种方案的适用场景及其对应的编码和封装格式如下表所示：

| 方案 | 适用场景 | 编码格式 | 封装格式 | 解封装格式 |
| --- | --- | --- | --- | --- |
| 方案一： videoCompressor | 指定视频压缩质量CompressQuality，无需设置编码参数。 | AVC(H.264)、 HEVC(H.265) | MP4 | MP4、MPEG-TS |
| 方案二： AVCodec Kit | 未经压缩的视频数据传输至视频编码器，进行编码参数设置。 | AVC(H.264)、 HEVC(H.265) | MP4 | MP4、MPEG-TS、FMP4、FLV、MKV、AVI、MPEG-PS |
| 方案三： AVTranscoder | 将已压缩编码的视频文件按照指定参数转换为另一种格式的视频。 | AVC(H.264)、 HEVC(H.265) | MP4 | MP4、MPEG-TS、FMP4、FLV、MKV、AVI、MPEG-PS |
