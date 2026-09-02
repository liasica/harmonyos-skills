---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcapability
title: AVCapability
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 模块 > AVCapability
category: harmonyos-references
scraped_at: 2026-09-02T14:52:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44d29cfc1c2ee95a5ba58314437da0021699aab52dc641822fa8e1006ca9c25a
---

## 概述

AVCapability模块提供用于编解码能力查询的函数。开发者通过本模块可以在运行时获取系统支持的编解码器信息，包括编解码器的基本信息、支持的参数范围、档次与级别组合以及可选编解码特性等，从而动态选择合适的编解码器并正确配置参数。

本模块提供的主要能力包括：

* **获取编解码器能力实例**：根据MIME类型或编解码器类型查询系统支持的编解码器能力，支持按硬件/软件类别筛选。
* **查询编解码器基本信息**：获取编解码器名称、MIME类型、最大实例数，区分硬件/软件编解码器、安全/非安全解码器。
* **查询编码器参数范围**：获取编码器支持的码率范围、质量范围、复杂度范围，检查码率模式支持情况。
* **查询音频编解码器能力**：获取采样率列表、采样率范围、声道数范围等音频相关参数。
* **查询视频编解码器能力**：获取分辨率对齐值、分辨率范围、帧率范围、像素格式、NativeBuffer格式等视频相关参数，支持检查特定分辨率和帧率组合的支持情况。
* **查询档次与级别**：获取编解码器支持的档次列表、指定档次下的级别列表，检查特定档次与级别组合的支持情况。
* **查询编解码特性**：检查编解码器是否支持时域可分层、B帧、低时延、长期参考帧、编码前处理降采样/裁剪等可选特性，获取特性属性。

适用场景包括：创建编解码器前查询系统是否支持指定格式、区分硬件与软件编解码器、获取参数范围用于配置编解码会话、查询档次级别与可选特性的支持情况。

对应的开发指南及样例可参考[获取支持的编解码能力](../harmonyos-guides/obtain-supported-codecs.md)。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [native\_avcapability.h](capi-native-avcapability-h.md) | 声明用于编解码能力查询到的Native API。 |
