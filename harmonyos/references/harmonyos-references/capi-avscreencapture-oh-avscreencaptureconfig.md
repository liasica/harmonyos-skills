---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencaptureconfig
title: OH_AVScreenCaptureConfig
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCaptureConfig
category: harmonyos-references
scraped_at: 2026-04-28T08:14:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0d54db0c755c8b004e667a7f350d1ae54d06ae1c2657f08865ae67a0a47f6018
---

```
1. typedef struct OH_AVScreenCaptureConfig {...} OH_AVScreenCaptureConfig
```

## 概述

PhonePC/2in1TabletTV

屏幕录制配置参数。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_CaptureMode](capi-native-avscreen-capture-base-h.md#oh_capturemode) captureMode | 屏幕录制的模式。 |
| [OH\_DataType](capi-native-avscreen-capture-base-h.md#oh_datatype) dataType | 屏幕录制流的数据格式。 |
| [OH\_AudioInfo](capi-avscreencapture-oh-audioinfo.md) audioInfo | 音频录制参数。 |
| [OH\_VideoInfo](capi-avscreencapture-oh-videoinfo.md) videoInfo | 视频录制参数。 |
| [OH\_RecorderInfo](capi-avscreencapture-oh-recorderinfo.md) recorderInfo | 录制文件参数，当数据格式为OH\_CAPTURE\_FILE时必须设置。 |
