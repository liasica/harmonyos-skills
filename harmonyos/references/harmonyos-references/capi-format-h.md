---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-format-h
title: format.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > format.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:57f85b6ebd7834efdea16e1aae287a6292734bd662a99d88c63de9efda91950f
---

## 概述

PhonePC/2in1TabletTVWearable

提供张量数据的排列格式。

**引用文件：** <mindspore/format.h>

**库：** libmindspore\_lite\_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AI\_Format](capi-format-h.md#oh_ai_format) | OH\_AI\_Format | MSTensor保存的数据支持的排列格式。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_Format

PhonePC/2in1TabletTVWearable

```
1. enum OH_AI_Format
```

**描述**

MSTensor保存的数据支持的排列格式。

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| OH\_AI\_FORMAT\_NCHW = 0 | 按批次N、通道C、高度H和宽度W的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_NHWC = 1 | 按批次N、高度H、宽度W和通道C的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_NHWC4 = 2 | 按批次N、高度H、宽度W和通道C的顺序存储张量数据，其中C轴是4字节对齐格式。 |
| OH\_AI\_FORMAT\_HWKC = 3 | 按高度H、宽度W、核数K和通道C的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_HWCK = 4 | 按高度H、宽度W、通道C和核数K的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_KCHW = 5 | 按核数K、通道C、高度H和宽度W的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_CKHW = 6 | 按通道C、核数K、高度H和宽度W的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_KHWC = 7 | 按核数K、高度H、宽度W和通道C的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_CHWK = 8 | 按通道C、高度H、宽度W和核数K的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_HW = 9 | 按高度H和宽度W的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_HW4 = 10 | 按高度H和宽度W的顺序存储张量数据，其中W轴是4字节对齐格式。 |
| OH\_AI\_FORMAT\_NC = 11 | 按批次N和通道C的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_NC4 = 12 | 按批次N和通道C的顺序存储张量数据，其中C轴是4字节对齐格式。 |
| OH\_AI\_FORMAT\_NC4HW4 = 13 | 按批次N、通道C、高度H和宽度W的顺序存储张量数据，其中C轴和W轴是4字节对齐格式。 |
| OH\_AI\_FORMAT\_NCDHW = 15 | 按批次N、通道C、深度D、高度H和宽度W的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_NWC = 16 | 按批次N、宽度W和通道C的顺序存储张量数据。 |
| OH\_AI\_FORMAT\_NCW = 17 | 按批次N、通道C和宽度W的顺序存储张量数据。 |
