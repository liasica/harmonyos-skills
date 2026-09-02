---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm
title: Multimedia_Drm
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 模块 > Multimedia_Drm
category: harmonyos-references
scraped_at: 2026-09-02T14:52:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7ec45330ee89c6cbd538f1d5f7c31f78267b03f7a672ab8100474920480ed3c3
---

## 概述

该功能使第三方应用程序可以自行实现媒体解封装和解复用功能，而不是使用系统提供的。

在创建DRM实例和会话后，可以调用DRM提供的解密接口进行解密。解密参数结构定义了解密参数的传输格式。

对应的开发指南及样例可参考[媒体数据解析](../harmonyos-guides/audio-video-demuxer.md)。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [native\_cencinfo.h](capi-native-cencinfo-h.md) | 声明用于设置解密参数的Native API。 |
