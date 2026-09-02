---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe
title: HiDebug_StackFrame
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_StackFrame
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ccfe32929518fd0fd9eb35ce9d8622e4be50c9e58c2ed653189f279bff726071
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
| [HiDebug\_StackFrameType](capi-hidebug-type-h.md#hidebug_stackframetype) type | 当前栈的类型。 |
| struct [HiDebug\_JsStackFrame](capi-hidebug-hidebug-jsstackframe.md) js | 由[HiDebug\_JsStackFrame](capi-hidebug-hidebug-jsstackframe.md)定义的js栈帧内容。 |
| struct [HiDebug\_NativeStackFrame](capi-hidebug-hidebug-nativestackframe.md) native | 由[HiDebug\_NativeStackFrame](capi-hidebug-hidebug-nativestackframe.md)定义的native栈帧内容。 |
