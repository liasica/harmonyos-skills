---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink-oh-lowpoweraudiosinkcallback
title: OH_LowPowerAudioSinkCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_LowPowerAudioSinkCallback
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a27dfb1d486a46e156a7367d5b88cbcf3649c03ad2f0e755870693e672e4934
---

```c
typedef struct OH_LowPowerAudioSinkCallback OH_LowPowerAudioSinkCallback;
```

## 概述

包含了OH\_LowPowerAudioSink回调函数指针的集合。

应用需注册此实例结构体到[OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)实例中，并对回调上报的信息进行处理，保证OH\_LowPowerAudioSink的正常运行。

**起始版本：** 20

**相关模块：** [LowPowerAudioSink](capi-lowpoweraudiosink.md)

**所在头文件：** [lowpower\_audio\_sink\_base.h](capi-lowpower-audio-sink-base-h.md)
