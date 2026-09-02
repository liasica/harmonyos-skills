---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avdemuxer
title: AVDemuxer
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 模块 > AVDemuxer
category: harmonyos-references
scraped_at: 2026-09-02T14:52:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:02b15c8cff162228ebb0163186ffae1fad157d0cf36802bb13b7dfef487c704f
---

## 概述

AVDemuxer模块提供从媒体文件码流中提取[sample](../harmonyos-guides/audio-video-demuxer.md)的接口。

本模块提供的主要能力包括：

* **解封装器创建与销毁**：通过媒体源（OH\_AVSource）创建解封装器实例，销毁解封装器实例释放资源。
* **轨道选择**：选择或取消选择需要读取数据的轨道，支持多轨道选择。
* **帧数据读取**：从选中的轨道读取压缩帧数据（sample），获取帧的相关信息（时间戳、大小、标志位等）。
* **跳转功能**：根据时间戳跳转到指定位置，支持前向跳转、后向跳转、就近跳转等模式。
* **DRM信息处理**：设置DRM信息回调，获取受DRM保护的媒体内容的解密信息。

适用场景包括：媒体播放器开发、视频编辑、音视频数据分析、媒体文件解析、受DRM保护的媒体内容解封装等需要从媒体文件中提取压缩数据的场景。

本模块通常与AVSource模块配合使用，先通过AVSource创建媒体源，再通过AVDemuxer进行解封装。解封装后的压缩数据可送入视频/音频解码器进行解码。

对应的开发指南及样例可参考[媒体数据解析](../harmonyos-guides/audio-video-demuxer.md)。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [native\_avdemuxer.h](capi-native-avdemuxer-h.md) | 声明用于音视频媒体数据解析的接口。 |
