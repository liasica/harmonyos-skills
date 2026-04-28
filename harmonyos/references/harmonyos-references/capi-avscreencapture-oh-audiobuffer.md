---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiobuffer
title: OH_AudioBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioBuffer
category: harmonyos-references
scraped_at: 2026-04-28T08:14:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a42b42fe2d1c964ea93b535cd112b6247ad91d386a37b2ddad48a349cb82cd9f
---

```
1. typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

## 概述

PhonePC/2in1TabletTV

定义了音频数据的大小、类型、时间戳等配置信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* buf | 音频buffer内存。 |
| int32\_t size | 音频buffer内存大小。 |
| int64\_t timestamp | 音频buffer时间戳。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频录制源类型。 |
