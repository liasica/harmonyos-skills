---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileprofile
title: JSVM_CompileProfile
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CompileProfile
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a40e644f8f01ee1c8946099c337d00d09024bb7495d5d53c31b916470cb0868f
---

```c
typedef const struct {...} JSVM_CompileProfile
```

## 概述

与JSVM\_COMPILE\_COMPILE\_PROFILE一起传递的编译采样文件。

**使用场景：** 用于应用二次启动时的预编译优化，可提升应用启动速度和运行性能。适用于需要优化启动性能的应用场景。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int \*profile | 编译采样文件的指针。 |
| size\_t length | 编译采样文件的大小。 |
