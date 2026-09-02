---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-scriptorigin
title: JSVM_ScriptOrigin
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_ScriptOrigin
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b92fdf51e28652e99f8459b503d8af6926b1339e040200fa90f6040bb268e80f
---

```c
typedef struct {...} JSVM_ScriptOrigin
```

## 概述

某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* sourceMapUrl | Sourcemap 路径。 |
| const char\* resourceName | 源文件名。 |
| size\_t resourceLineOffset | 这段代码在源文件中的起始行号。 |
| size\_t resourceColumnOffset | 这段代码在源文件中的起始列号。 |
