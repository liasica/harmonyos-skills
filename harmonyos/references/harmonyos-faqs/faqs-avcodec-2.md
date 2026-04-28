---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-2
title: 音视频文件的封装协议与编码格式有哪些
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 音视频文件的封装协议与编码格式有哪些
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:44+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:78754a0f7001084739f6bb994376f16ce3621564af41afcd89791d0a5b8032ad
---

* 音视频文件的封装支持mp4和m4a容器格式。mp4封装视频、音频、字幕和元数据等媒体元素，适用于网上电影、电视剧和用户拍摄的视频等内容。m4a主要存储音频媒体元素。这两种格式在多媒体内容的编辑、存储和分享中发挥重要作用。
* 视频编解码支持H.264（AVC）和H.265（HEVC）的硬件加速编解码。H.264和H.265是视频标准编码技术，H.265的视频压缩率高于H.264。例如，在录制相同视频文件时，H.265生成的MP4文件大小显著减小，更利于节省存储空间。
* [音频编码](../harmonyos-guides/audio-encoding.md)支持AAC，FLAC；[音频解码](../harmonyos-guides/audio-decoding.md)支持AAC，MPEG(MP3)，FLAC，Vorbis。

**参考链接**

[媒体数据封装](../harmonyos-guides/audio-video-muxer.md)
