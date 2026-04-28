---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-lowpoweraudiosink-oh-lowpoweraudiosinkcallback
title: OH_LowPowerAudioSinkCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_LowPowerAudioSinkCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:14:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c6a740407302d124d3e4de62285cb74dae74af36a96aa61612f5a615b715383c
---

```
1. typedef struct OH_LowPowerAudioSinkCallback OH_LowPowerAudioSinkCallback
```

## 概述

PhonePC/2in1Tablet

包含了LowPowerAudioSink回调函数指针的集合。

应用需注册此实例结构体到[OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)实例中，并对回调上报的信息进行处理，保证LowPowerAudioSink的正常运行。

**起始版本：** 20

**相关模块：** [LowPowerAudioSink](capi-lowpoweraudiosink.md)

**所在头文件：** [lowpower\_audio\_sink\_base.h](capi-lowpower-audio-sink-base-h.md)
