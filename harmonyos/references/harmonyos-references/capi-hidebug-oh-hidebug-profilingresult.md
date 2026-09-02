---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-profilingresult
title: OH_HiDebug_ProfilingResult
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > OH_HiDebug_ProfilingResult
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a3cd747f24f4f3861fff68d0c3b70cdedfb3e0a055adc0eb7cf13c195e090d4
---

```c
typedef struct OH_HiDebug_ProfilingResult {...} OH_HiDebug_ProfilingResult
```

## 概述

封装单次资源采集的结果。

**起始版本：** 24

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_HiDebug\_ResourceType](capi-hidebug-type-h.md#oh_hidebug_resourcetype) resourceType | 资源采集类型。  **起始版本：** 24 |
| const char\* filePath | 资源采集结果文件路径。如果采集失败则为空值。  **起始版本：** 24 |
