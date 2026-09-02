---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-callback
title: VideoProcessing_Callback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > VideoProcessing_Callback
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75735d8351b07971a5c9e34bfd1aff4957e403e9112c8f652615770eded61548
---

```c
typedef struct VideoProcessing_Callback VideoProcessing_Callback
```

## 概述

视频处理回调对象类型。

定义一个VideoProcessing\_Callback空指针，调用[OH\_VideoProcessingCallback\_Create](capi-video-processing-h.md#oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。

**起始版本：** 12

**相关模块：** [VideoProcessing](capi-videoprocessing.md)

**所在头文件：** [video\_processing\_types.h](capi-video-processing-types-h.md)
