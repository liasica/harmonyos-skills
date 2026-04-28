---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media
title: 模块描述
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T08:13:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:30b8563fc9b019eb18c5eb227092a39dabac6e6e77306346f646fbcd92c4bfc9
---

媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

媒体子系统包含了音视频相关媒体业务，提供以下常用功能：

* 音视频播放（[AVPlayer](arkts-apis-media-avplayer.md)9+）
* 音视频录制（[AVRecorder](arkts-apis-media-avrecorder.md)9+）
* 视频转码（[AVTranscoder](arkts-apis-media-avtranscoder.md)12+）
* 获取音视频元数据（[AVMetadataExtractor](arkts-apis-media-avmetadataextractor.md)11+）
* 获取视频缩略图（[AVImageGenerator](arkts-apis-media-avimagegenerator.md)12+）
* 屏幕录制（[AVScreenCaptureRecorder](arkts-apis-media-avscreencapturerecorder.md)12+）

## 导入模块

```
1. import { media } from '@kit.MediaKit';
```
