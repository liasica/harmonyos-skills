---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcapability-oh-avrange
title: OH_AVRange
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVRange
category: harmonyos-references
scraped_at: 2026-10-01T07:39:18+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:dcc4ac94147903d25b092cf7e51f70bcce6d11b01de20f1cbbee6580499ebd50
---

```c
typedef struct OH_AVRange {...} OH_AVRange
```

## 概述

范围包含最小值和最大值。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**相关模块：** [AVCapability](capi-avcapability.md)

**所在头文件：** [native\_avcapability.h](capi-native-avcapability-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t minVal | 最小值。 |
| int32\_t maxVal | 最大值。 |
