---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiobuffer
title: OH_AudioBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioBuffer
category: harmonyos-references
scraped_at: 2026-09-05T06:20:25+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:e5caae72ac2501bd207cb3c18f1cee0aee210e34b532a14c85520c7d20492fab
---

```c
typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

## 概述

定义了音频缓冲区数据及其大小、类型、时间戳等属性信息。

在屏幕录制过程中，该结构体由系统通过音频数据回调填充，开发者可从中读取录制的音频帧数据及其时间戳，用于后续音频处理或编码。适用于需要获取屏幕录制音频帧数据的场景。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*buf | 指向音频缓冲区内存的指针。由系统分配和释放，开发者无需手动管理。音频缓冲区用于存储录制的音频采样数据，数据格式为PCM原始字节流，需配合size字段确定数据长度。 |
| int32\_t size | 音频缓冲区内存大小，单位为字节（Byte），表示buf指针所指音频数据的字节长度。取值范围大于等于0，由系统填充，值为负数时将报错。 |
| int64\_t timestamp | 音频缓冲区时间戳，表示该音频帧的时间位置。单位为纳秒（ns）。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频录制源类型。其值由OH\_AudioCaptureInfo中配置的[OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype)决定。 |
