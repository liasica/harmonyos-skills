---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-ref--8h
title: JSVM_Ref__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_Ref__*
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6a5b4f362874345ac075ee732c6c2466742e3529bfd76f912e9fbc5598403e4e
---

```c
typedef struct JSVM_Ref__* JSVM_Ref
```

## 概述

表示JavaScript值的引用。

**使用场景：** 在Native与JavaScript交互场景中，需要持有JavaScript对象引用时使用。

**功能特点：** 提供对JavaScript值的稳定引用，防止被垃圾回收。支持跨函数、跨作用域传递JavaScript值。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
