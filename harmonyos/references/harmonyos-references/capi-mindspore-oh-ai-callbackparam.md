---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-callbackparam
title: OH_AI_CallBackParam
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 结构体 > OH_AI_CallBackParam
category: harmonyos-references
scraped_at: 2026-04-28T08:19:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94087c0de0265543a8d13187d9f60f7432d2761d6e197b9a338712da2876d6a1
---

```
1. typedef struct OH_AI_CallBackParam {...} OH_AI_CallBackParam
```

## 概述

PhonePC/2in1TabletTVWearable

回调函数中传入的算子信息。

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

**所在头文件：** [model.h](capi-model-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* node\_name | 算子名称。 |
| char\* node\_type | 算子类型。 |
