---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo
title: OH_VideoEncInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_VideoEncInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b53b2b913728b15e15be300dd59b58a9a643c046e0037015427e514ca5643ef4
---

```c
typedef struct OH_VideoEncInfo {...} OH_VideoEncInfo
```

## 概述

视频编码参数。

用于配置屏幕录制的视频编码参数，支持设置编码格式、比特率和帧率。videoCodec指定编码格式（如H.264、H.265等），videoBitrate影响视频清晰度和文件大小，videoFrameRate影响视频流畅度。通常在调用屏幕录制接口前设置这些参数。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_VideoCodecFormat](capi-native-avscreen-capture-base-h.md#oh_videocodecformat) videoCodec | 视频编码格式。不同编码格式影响视频的压缩效率与兼容性，具体各格式效果参见[OH\_VideoCodecFormat](capi-native-avscreen-capture-base-h.md#oh_videocodecformat)枚举说明。 |
| int32\_t videoBitrate | 视频编码比特率，单位为比特每秒（bit/s）。取值范围需根据编码格式和实际需求确定，默认取值为10000000，值越大画质越好但文件也越大。 |
| int32\_t videoFrameRate | 视频编码帧率，单位为帧每秒（FPS）。常见取值范围为15~60 FPS。 |
