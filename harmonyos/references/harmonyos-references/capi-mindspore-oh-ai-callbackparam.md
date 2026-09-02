---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-callbackparam
title: OH_AI_CallBackParam
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 结构体 > OH_AI_CallBackParam
category: harmonyos-references
scraped_at: 2026-09-02T15:03:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eec4d7e68260321ea4986fd87be833b0feaf702765cc3672abc28ba5efc822a7
---

```c
typedef struct OH_AI_CallBackParam {...} OH_AI_CallBackParam
```

## 概述

回调函数中传入的算子信息。

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

**所在头文件：** [model.h](capi-model-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* node\_name | 算子名称。 |
| char\* node\_type | 算子类型。 |
