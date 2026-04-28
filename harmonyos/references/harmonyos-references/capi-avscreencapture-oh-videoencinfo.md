---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo
title: OH_VideoEncInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_VideoEncInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:14:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4b504571d7e052e4b03ea1451a5d620dc944efe8184ffa334d17c2f281b7dd19
---

```
1. typedef struct OH_VideoEncInfo {...} OH_VideoEncInfo
```

## 概述

PhonePC/2in1TabletTV

视频编码参数。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_VideoCodecFormat](capi-native-avscreen-capture-base-h.md#oh_videocodecformat) videoCodec | 视频采集编码格式。 |
| int32\_t videoBitrate | 视频采集比特率。 |
| int32\_t videoFrameRate | 视频采集帧率。 |
