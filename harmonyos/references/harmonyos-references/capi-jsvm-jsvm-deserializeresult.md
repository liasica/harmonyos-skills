---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deserializeresult
title: JSVM_DeserializeResult
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_DeserializeResult
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7c5bb8e2b3b100b7158f9981b2f2e1d02f81bdf1f299dd58f7a8a993304809cb
---

```c
typedef struct JSVM_DeserializeResult__* JSVM_DeserializeResult
```

## 概述

与JSVM\_COMPILE\_BACKGROUND\_DESERIALIZE\_RESULT一起传递的后台反序列化结果。

**使用场景：** 用于在JSVM后台编译场景中，传递和存储后台反序列化的结果数据。

**特点：** 轻量级的类型定义，与JSVM\_COMPILE\_BACKGROUND\_DESERIALIZE\_RESULT配合使用。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 24

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
