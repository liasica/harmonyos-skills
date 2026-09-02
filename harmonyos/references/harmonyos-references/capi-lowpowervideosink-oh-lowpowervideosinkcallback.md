---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpowervideosink-oh-lowpowervideosinkcallback
title: OH_LowPowerVideoSinkCallback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_LowPowerVideoSinkCallback
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea75222d2f5d17e6805f58acad700e86a9c5037b98b6fa8a251673a650a08d07
---

```c
typedef struct OH_LowPowerVideoSinkCallback OH_LowPowerVideoSinkCallback;
```

## 概述

包含了OH\_LowPowerVideoSink回调函数指针的集合。

应用需注册此实例结构体到[OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)实例中，并对回调上报的信息进行处理，保证OH\_LowPowerVideoSink的正常运行。

**起始版本：** 20

**相关模块：** [LowPowerVideoSink](capi-lowpowervideosink.md)

**所在头文件：** [lowpower\_video\_sink\_base.h](capi-lowpower-video-sink-base-h.md)
