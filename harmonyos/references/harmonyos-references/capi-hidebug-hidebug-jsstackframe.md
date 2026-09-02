---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-jsstackframe
title: HiDebug_JsStackFrame
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_JsStackFrame
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9e4639e8e013f1daffbac74d531b4409c7c2c66a583c04c73b9e522105075e42
---

```c
typedef struct HiDebug_JsStackFrame {...} HiDebug_JsStackFrame
```

## 概述

js栈帧内容的定义。用于在性能分析和调试场景中，记录js调用栈的帧信息，包括代码位置、函数名称、映射区域等关键信息。

**起始版本：** 20

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t relativePc | 相对pc地址。当前pc相对于其所在的映射区域（如可执行文件或共享库）起始地址的偏移量。 |
| int32\_t line | 代码所在的行号。当前栈帧对应的代码位于文件的具体行位置。 |
| int32\_t column | 代码所在的列号。当前栈帧对应的代码在指定行的具体列位置。 |
| const char\* mapName | 映射名称。当前栈帧所属的映射区域的名称。 |
| const char\* functionName | 函数名称。当前栈帧对应的函数的名称。 |
| const char\* url | URL地址。当前栈帧对应代码的文件的URL，无论是本地文件路径还是远程服务器上的文件地址，通过该URL能找到对应的代码文件。 |
| const char\* packageName | 包名。当前栈帧对应的代码所属包的名称。 |
