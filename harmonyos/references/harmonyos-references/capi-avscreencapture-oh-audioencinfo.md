---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioencinfo
title: OH_AudioEncInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioEncInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:14:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f92ff4def9e7855b5dc4ef13ce47b9bb5b11554874880650e08f75bafe57845
---

```
1. typedef struct OH_AudioEncInfo {...} OH_AudioEncInfo
```

## 概述

PhonePC/2in1TabletTV

音频编码信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t audioBitrate | 音频编码比特率。 |
| [OH\_AudioCodecFormat](capi-native-avscreen-capture-base-h.md#oh_audiocodecformat) audioCodecformat | 音频编码格式。 |
