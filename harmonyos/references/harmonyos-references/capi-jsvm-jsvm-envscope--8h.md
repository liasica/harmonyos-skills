---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-envscope--8h
title: JSVM_EnvScope__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_EnvScope__*
category: harmonyos-references
scraped_at: 2026-09-02T14:53:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:63a11083d327f77d72a942a06f27e8ccd9c2c51bb568328332a2ef51d1d32601
---

```c
typedef struct JSVM_EnvScope__* JSVM_EnvScope
```

## 概述

表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH\_JSVM\_OpenEnvScope进入该环境的JSVM\_EnvScope后，该环境才对线程的虚拟机实例可用。

**使用场景：** 在多线程环境下需要访问和操作JavaScript环境时，用于管理和切换环境作用域。

**解决的问题：** 解决多线程环境下对同一虚拟机实例的环境访问和隔离问题。

**带来的收益：** 为开发者提供线程安全的环境管理机制，确保多线程访问的正确性和隔离性。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
