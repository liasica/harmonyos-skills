---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avqueueitem
title: OH_AVSession_AVQueueItem
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > OH_AVSession_AVQueueItem
category: harmonyos-references
scraped_at: 2026-09-02T15:02:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:adcb2ce44dfd1c1f451a732ca19640d6cbd6a79f1d0ef9e9e6267465c54c1865
---

```c
typedef struct OH_AVSession_AVQueueItem {...} OH_AVSession_AVQueueItem
```

## 概述

音视频队列元素的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

**所在头文件：** [native\_avqueueitem.h](capi-native-avqueueitem-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t itemId | 资源ID。 |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md) \*description | 媒体项信息。 |
