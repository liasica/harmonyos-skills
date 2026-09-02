---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-shapeinfo
title: OH_AI_ShapeInfo
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 结构体 > OH_AI_ShapeInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:03:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:024a75b1f00b88d0cc76de8355ef810868acb2681f6cb59a5c148f60ee6c8f70
---

```c
typedef struct OH_AI_ShapeInfo {...} OH_AI_ShapeInfo
```

## 概述

形状维度大小，预留最大维度是32，当前实际支持的最大维度是8。

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

**所在头文件：** [model.h](capi-model-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t shape\_num | 维度数组长度。 |
| int64\_t shape[OH\_AI\_MAX\_SHAPE\_NUM] | 维度数组。 |
