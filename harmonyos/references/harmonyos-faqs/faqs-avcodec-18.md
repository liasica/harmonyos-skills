---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-18
title: 部分视频边缓存边播放失败
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 部分视频边缓存边播放失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ef3690fdcc885637b1fed0de71ee34053c2a2b408404b2703ca9ebec2630361
---

## 问题现象

使用AVPlayer实现视频的播放，使用OhosVideoCache视频缓存库部分视频无法边缓存边播放，必须完全缓存完成才可以播放，如何排查？

## 背景知识

* [AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)是一个功能较完善的音视频播放API，集成了流媒体和本地资源解析，媒体资源解封装，视频解码和渲染功能，可直接播放mp4、mkv等格式的视频文件。
* [OhosVideoCache](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/blob/master/OhosVideoCache/README_zh.md#ohosvideocache)是一个支持边播放边缓存的库，只需要将音视频的url传递给OhosVideoCache处理之后再设置给播放器，OhosVideoCache就可以一边下载音视频数据并保存在本地，一边读取本地缓存返回给播放器，使用者无需进行其他操作。

## 问题定位

1. mp4文件是由多个“盒子”（Box）组成的，这些盒子可以嵌套，形成一个层次结构。每个盒子都有一个4字节的标识符（通常是4个ASCII字符，如ftyp、moov），以及指明盒子大小和类型的信息。
   * ftyp：用于说明当前媒体文件的类型、版本号及兼容的协议类型。它是mp4文件的第一个盒子，且只能有一个。
   * moov：用于存储文件的元数据，包括创建时间、修改时间、整体播放时长等全局信息，以及音视频流的具体信息（如轨道信息、编码格式等）。它也是一个容器盒子，可以包含多个子盒子。
   * mdat：用于存储实际的音视频数据。一个mp4文件可以有一个或多个mdat盒子，也可以没有（当媒体数据全部引用其他文件时）。媒体数据的结构由metadata进行描述。
2. 对无法播放的视频文件进行结构解析，发现moov信息排在最后面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/DoJcmmADR2aB2vADCYfGaA/zh-cn_image_0000002658911571.png "点击放大")

## 分析结论

视频数据中moov信息排在后面的不支持边下载边播放。moov中存放了视频的相关信息，比如时长、分辨率、帧率，mdat中存放的是媒体数据，只有加载完moov信息之后才能开始播放，所以想要提升播放加载速度，必须要将moov信息排在mdat前面。如果视频的moov信息在最后面，需要下载完成后才能播放。

## 修改建议

* 对无法播放的视频文件重新排列文件结构，把moov信息移到mdat前面。
* 实现mp4文件moov信息前置，技术实现方案可参考[音视频编解码服务](../harmonyos-references/avcodec-api.md)。

## 常见FAQ

Q：ijkPlayer播放视频，调用seekTo后进度条出现卡顿或跳动现象。

A：该问题是由于视频资源的moov信息在视频的结构末尾导致，可以在服务端将moov信息移到前面解决。
