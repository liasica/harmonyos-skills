---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-env--8h
title: JSVM_Env__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_Env__*
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:12000362d4553e7374297dc2f09b1f6979dd806b1858aee7bdfc992420e87e90
---

```c
typedef struct JSVM_Env__* JSVM_Env
```

## 概述

表示虚拟机特定状态的上下文环境，需要在调用native函数时作为参数传递，并且传递给后续任何的JSVM-API嵌套调用。

**使用场景：** 在Native模块中调用JSVM-API时，用于保存和传递虚拟机状态，在多实例环境下，区分不同的虚拟机环境实例。

**功能特点：** 提供虚拟机实例级别的状态隔离，支持跨函数调用的状态传递。

**解决的问题：** 解决Native代码与JavaScript引擎交互时的状态管理问题，支持在多个虚拟机实例间进行状态隔离。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
