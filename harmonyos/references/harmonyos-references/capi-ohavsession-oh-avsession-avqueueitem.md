---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avqueueitem
title: OH_AVSession_AVQueueItem
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > OH_AVSession_AVQueueItem
category: harmonyos-references
scraped_at: 2026-04-28T08:12:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:143b4a0c9598fddfdc6ed90e969078038c22fc193109ee56807823d917a6d9b8
---

```
1. typedef struct {...} OH_AVSession_AVQueueItem
```

## 概述

PhonePC/2in1TabletTVWearable

音视频队列元素的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

**所在头文件：** [native\_avqueueitem.h](capi-native-avqueueitem-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t itemId | 资源ID。 |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md) \*description | 媒体项信息。 |
