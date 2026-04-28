---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-shapeinfo
title: OH_AI_ShapeInfo
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 结构体 > OH_AI_ShapeInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:19:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:66a4029db7f36560d550b05e00229aeb0d8903fbec09fb3aad3bb1220165805c
---

```
1. typedef struct OH_AI_ShapeInfo {...} OH_AI_ShapeInfo
```

## 概述

PhonePC/2in1TabletTVWearable

形状维度大小，预留最大维度是32，当前实际支持的最大维度是8。

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

**所在头文件：** [model.h](capi-model-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| size\_t shape\_num | 维度数组长度。 |
| int64\_t shape[OH\_AI\_MAX\_SHAPE\_NUM] | 维度数组。 |
