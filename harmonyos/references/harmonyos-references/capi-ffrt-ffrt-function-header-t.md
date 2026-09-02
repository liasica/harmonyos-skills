---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-function-header-t
title: ffrt_function_header_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_function_header_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:52096b0293db7d72fa8e3b2618ebe9a7d45848aa85d26591debc51fb34ca1347
---

```c
typedef struct {...} ffrt_function_header_t
```

## 概述

任务执行体，用于定义任务的执行和销毁回调。exec回调在任务被调度时调用，destroy回调在任务完成后被调用以释放任务相关资源。两者共同管理FFRT任务的完整生命周期。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) exec | 执行任务的函数。在任务被调度时由框架调用。 |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) destroy | 销毁任务的函数。在任务执行完毕后由框架调用以释放资源。 |
| uint64\_t reserve[2] | 保留字段。需设置为0。 |
