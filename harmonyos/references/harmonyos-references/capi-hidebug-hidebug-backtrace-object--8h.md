---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-backtrace-object--8h
title: HiDebug_Backtrace_Object__*
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_Backtrace_Object__*
category: harmonyos-references
scraped_at: 2026-09-02T14:52:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3cc5cb6f5faf52ddeaa42883e7cf2660af647d69f51b1ec7c43324d0f5b1e387
---

```c
typedef struct HiDebug_Backtrace_Object__* HiDebug_Backtrace_Object
```

## 概述

用于栈回溯及栈解析的对象。该对象封装了栈回溯所需的上下文信息，包括调用栈地址、线程状态等数据，通过相关接口可获取详细的栈帧信息和符号解析结果。该对象通过HiDebug相关接口创建，使用后需要调用对应的销毁接口释放资源。

**起始版本：** 20

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)
