---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct8h
title: JSVM_CallbackStruct*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CallbackStruct*
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dfc78972834afa69000f4a8f03dd2b2ab73eed50e04d71c27224db9814f76857
---

```c
typedef JSVM_CallbackStruct* JSVM_Callback
```

## 概述

用户提供的native函数的函数指针类型，这些函数通过JSVM-API接口暴露给JavaScript。

**使用场景：** 在Native层实现JavaScript可调用的函数时使用，适用于JSVM扩展开发场景。

**解决的问题：** 定义标准化的函数指针类型，便于将C/C++函数暴露给JavaScript环境。

**功能特点：** 提供类型安全的函数指针定义，支持Native与JavaScript的交互。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
