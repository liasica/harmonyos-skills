---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-callback
title: VideoProcessing_Callback
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > VideoProcessing_Callback
category: harmonyos-references
scraped_at: 2026-04-28T08:14:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:01a2e3eb6116cd375c104b5635dc36bc107bada3ca05b14b819a2241c6582447
---

```
1. typedef struct VideoProcessing_Callback VideoProcessing_Callback
```

## 概述

PhonePC/2in1TabletTV

视频处理回调对象类型。

定义一个VideoProcessing\_Callback空指针，调用[OH\_VideoProcessingCallback\_Create](capi-video-processing-h.md#oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。

**起始版本：** 12

**相关模块：** [VideoProcessing](capi-videoprocessing.md)

**所在头文件：** [video\_processing\_types.h](capi-video-processing-types-h.md)
