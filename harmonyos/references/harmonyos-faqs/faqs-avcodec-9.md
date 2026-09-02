---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-9
title: 应用内选择某个音频文件后无法播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 应用内选择某个音频文件后无法播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d17a265e662fdc60d399882c037312e75d31c82d79d5f0f10e4cb4d6dd09fbff
---

## 问题现象

音频播放格式中，表明支持APE格式，但是打开该格式的音频无法播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/V8r-crDFT0qM_EluvTeJZw/zh-cn_image_0000002628552686.png "点击放大")

## 背景知识

根据[Media Kit支持的格式与协议](../harmonyos-guides/media-kit-intro.md#支持的格式与协议)的内容，音频播放支持以下音频格式：

| 音频容器规格 | 规格描述 |
| --- | --- |
| m4a | 音频格式：AAC |
| aac | 音频格式：AAC |
| mp3 | 音频格式：MP3 |
| ogg | 音频格式：VORBIS |
| wav | 音频格式：PCM |
| amr | 音频格式：AMR |

[AVCodec Kit](../harmonyos-guides/avcodec-kit-intro.md)是媒体系统中的音视频的编解码、媒体文件的解析、封装、媒体数据输入等原子能力，适合需要自定义编解码逻辑的场景。

## 问题定位

1. 使用ArkUI Inspector确认其音频播放组件为AVPlayer。
2. 检查代码中是否具备APE格式的解码能力，可通过全局搜索AVCodec Kit中的相关接口，确认是否支持。

## 分析结论

AVPlayer不具备内置APE解码能力。因此，当使用AVPlayer播放.APE文件时，无法找到合适的解码器，导致播放失败。

## 修改建议

对于APE格式的应用，可通过集成三方解码库或者使用AVCodec Kit来实现，具体可参考：[音频解码](../harmonyos-guides/audio-decoding.md)。
