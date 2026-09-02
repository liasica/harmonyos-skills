---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsinkbase-oh-avsamplesbuffer
title: OH_AVSamplesBuffer
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVSamplesBuffer
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:22a4468860b6431ca5e422d33799afc988f6510594ec86fb7c662e8a3ef6c09a
---

```c
typedef struct OH_AVSamplesBuffer OH_AVSamplesBuffer
```

## 概述

LowPowerAVSink输入数据的结构体。应用在收到DataNeeded回调后需要将数据打包装进OH\_AVSamplesBuffer实例中送给对应的lowpower\_avsink。

**起始版本：** 20

**相关模块：** [AVSinkBase](capi-avsinkbase.md)

**所在头文件：** [lowpower\_avsink\_base.h](capi-lowpower-avsink-base-h.md)
