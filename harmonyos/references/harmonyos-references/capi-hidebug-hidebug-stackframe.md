---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe
title: HiDebug_StackFrame
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_StackFrame
category: harmonyos-references
scraped_at: 2026-11-12T09:56:16+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dfb9e2783a6ba6dfdd04b39766e6bcb425d9c69dcdf7c55039fb07731d9866a5
---

```c
typedef struct HiDebug_StackFrame {...} HiDebug_StackFrame
```

## 概述

栈帧内容的定义。该结构体用于表示调试时的栈帧信息，支持获取当前栈的类型以及对应的js栈帧或Native栈帧内容，帮助开发者进行问题定位和调试分析。

**起始版本：** 20

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| HiDebug\_StackFrameType type | 当前栈的类型。 |
| frame.js | 由[HiDebug\_JsStackFrame](capi-hidebug-hidebug-jsstackframe.md)定义的js栈帧内容。 |
| frame.native | 由[HiDebug\_NativeStackFrame](capi-hidebug-hidebug-nativestackframe.md)定义的native栈帧内容。 |
