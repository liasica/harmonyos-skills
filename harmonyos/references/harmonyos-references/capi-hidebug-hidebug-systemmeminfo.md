---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-systemmeminfo
title: HiDebug_SystemMemInfo
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_SystemMemInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:40c6ae65d8fddf8d4d9bbf3e0953126b5927dc710992a0a738f20b47d9139dda
---

```c
typedef struct HiDebug_SystemMemInfo {...} HiDebug_SystemMemInfo
```

## 概述

系统内存信息结构类型定义。用于获取系统内存的总量、空闲量、可用量等关键信息，适用于系统性能分析、内存监控、故障诊断等场景，帮助开发者了解系统内存使用状况，优化内存管理策略。

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t totalMem | 系统总的内存，以KB为单位。 |
| uint32\_t freeMem | 系统空闲的内存，以KB为单位。 |
| uint32\_t availableMem | 系统可用的内存，以KB为单位。 |
