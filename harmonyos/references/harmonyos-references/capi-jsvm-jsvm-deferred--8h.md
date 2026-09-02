---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deferred--8h
title: JSVM_Deferred__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_Deferred__*
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:257711788f32c1196011f3b1972e00af5ef3b4dc859c85bb242af2949d6d4961
---

```c
typedef struct JSVM_Deferred__* JSVM_Deferred
```

## 概述

表示Promise延迟对象。

**使用场景：** 在JSVM Native模块中需要创建Promise对象并延迟处理异步操作结果时，需要在Native层手动控制Promise的resolve或reject时机的场景，将Native层的异步操作结果封装为Promise返回给JavaScript层。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
