---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencaptureconfig
title: OH_AVScreenCaptureConfig
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCaptureConfig
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:666adada85efee12a06b48679bbedc5773c07e32f4e20ee9ebbd1a9c59219621
---

```c
typedef struct OH_AVScreenCaptureConfig {...} OH_AVScreenCaptureConfig
```

## 概述

屏幕录制配置参数。

用于配置屏幕录制的模式、数据格式、音频参数、视频参数及录制文件参数等，适用于需要自定义屏幕录制行为（如选择录制模式、指定数据输出格式、设置音视频编码参数等）的场景。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_CaptureMode](capi-native-avscreen-capture-base-h.md#oh_capturemode) captureMode | 屏幕录制的模式，用于指定屏幕录制的捕获方式。不同的captureMode值决定录制内容的范围和交互方式，开发者应根据需要录制的屏幕区域和交互需求选择合适的模式。可取值包括OH\_CAPTURE\_HOME\_SCREEN（录制主屏幕）和OH\_CAPTURE\_SPECIFIED\_WINDOW（录制指定窗口）等，具体枚举值见[OH\_CaptureMode](capi-native-avscreen-capture-base-h.md#oh_capturemode)。 |
| [OH\_DataType](capi-native-avscreen-capture-base-h.md#oh_datatype) dataType | 屏幕录制流的数据格式，例如需要实时处理录制流数据时可选择流数据格式，需要保存为文件时可选择文件数据格式。取值原则参考[OH\_DataType](capi-native-avscreen-capture-base-h.md#oh_datatype)枚举定义。当数据格式为OH\_CAPTURE\_FILE时，必须设置[OH\_RecorderInfo](capi-avscreencapture-oh-recorderinfo.md)。 |
| [OH\_AudioInfo](capi-avscreencapture-oh-audioinfo.md) audioInfo | 音频录制参数，用于配置录制的音频相关属性。包含音频编码格式、采样率、声道数等配置项，具体属性见[OH\_AudioInfo](capi-avscreencapture-oh-audioinfo.md)。 |
| [OH\_VideoInfo](capi-avscreencapture-oh-videoinfo.md) videoInfo | 视频录制参数，用于配置录制的视频相关属性。包含视频编码格式、分辨率、帧率等配置项，具体属性见[OH\_VideoInfo](capi-avscreencapture-oh-videoinfo.md)。 |
| [OH\_RecorderInfo](capi-avscreencapture-oh-recorderinfo.md) recorderInfo | 录制文件参数，当数据格式为OH\_CAPTURE\_FILE时必须设置，未设置时录制无法正常启动。 |
