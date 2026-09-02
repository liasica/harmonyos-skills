---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativestackframe
title: HiDebug_NativeStackFrame
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_NativeStackFrame
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8e988691c2b7df7691483e5d5177c1ee91af9c617883a60636f8253f9197deff
---

```c
typedef struct HiDebug_NativeStackFrame {...} HiDebug_NativeStackFrame
```

## 概述

native栈帧内容的定义。

**起始版本：** 20

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t relativePc | 相对pc地址。当前pc相对于其所在的映射区域（如可执行文件或共享库）起始地址的偏移量。 |
| uint64\_t funcOffset | 函数偏移量。当前栈帧对应的函数在其所在的映射区域（如可执行文件或共享库）内的偏移量。 |
| const char\* mapName | 映射名称。当前栈帧所属的映射区域的名称。 |
| const char\* functionName | 函数名称。当前栈帧对应的函数的名称。 |
| const char\* buildId | 构建标识符。当前映射区域（如可执行文件或共享库）相关的唯一标识符。在调试和符号解析时，buildId可确保使用的符号文件与实际运行的二进制文件版本一致。 |
| const char\* reserved | 保留字段。为了后续扩展预留的字段。 |
