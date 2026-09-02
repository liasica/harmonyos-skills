---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcapability-oh-avrange
title: OH_AVRange
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVRange
category: harmonyos-references
scraped_at: 2026-09-02T15:02:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9da22bffb3cfc899679397257e1192ae00616ef33d946c6416931dfc751fdf4f
---

```c
typedef struct OH_AVRange {...} OH_AVRange
```

## 概述

范围包含最小值和最大值。

**起始版本：** 10

**相关模块：** [AVCapability](capi-avcapability.md)

**所在头文件：** [native\_avcapability.h](capi-native-avcapability-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t minVal | 最小值。 |
| int32\_t maxVal | 最大值。 |
