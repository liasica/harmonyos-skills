---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsinkbase-oh-avsamplesbuffer
title: OH_AVSamplesBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVSamplesBuffer
category: harmonyos-references
scraped_at: 2026-11-04T08:36:21+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:748c31311737626e4cda24f0e823e8c377a2268a5db8d878807785fbfd679776
---

```c
typedef struct OH_AVSamplesBuffer OH_AVSamplesBuffer
```

## 概述

LowPowerAVSink输入数据的结构体。应用在收到DataNeeded回调后需要将数据打包装进OH\_AVSamplesBuffer实例中送给对应的LowPowerAVSink。

**起始版本：** 20

**相关模块：** [AVSinkBase](capi-avsinkbase.md)

**所在头文件：** [lowpower\_avsink\_base.h](capi-lowpower-avsink-base-h.md)
