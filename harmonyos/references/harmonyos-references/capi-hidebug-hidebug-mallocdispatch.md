---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-mallocdispatch
title: HiDebug_MallocDispatch
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_MallocDispatch
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f69ad914b81d311e3ba4a5ca01d21050586327946cffbe6fc12e7244c21995be
---

```c
typedef struct HiDebug_MallocDispatch {...} HiDebug_MallocDispatch
```

## 概述

应用程序进程可替换/恢复的HiDebug\_MallocDispatch表结构类型定义。通过该结构体，开发者可以自定义内存管理函数指针，实现对进程内存分配和释放的监控与定制。主要特点包括：支持动态替换和恢复内存管理函数、提供全面的内存操作接口（malloc、calloc、realloc、free、mmap、munmap）、不影响系统默认内存管理行为。使用场景包括：内存泄漏检测、内存使用性能分析、自定义内存分配策略、内存安全监控等。能够帮助开发者及时发现和解决内存问题，提升应用稳定性和性能。

**起始版本：** 20

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [void\* (\*malloc)(size\_t)](capi-hidebug-hidebug-mallocdispatch.md#malloc) | 开发者自定义malloc函数指针。用于替代系统默认的内存分配函数，在分配内存时记录分配信息或执行自定义逻辑，可用于内存泄漏追踪和性能监控。 |
| [void\* (\*calloc)(size\_t, size\_t)](capi-hidebug-hidebug-mallocdispatch.md#calloc) | 开发者自定义calloc函数指针。用于替代系统默认的calloc函数，在分配并初始化零内存时记录分配信息或执行自定义逻辑，可用于追踪大块内存分配和内存初始化监控。 |
| [void\* (\*realloc)(void\*, size\_t)](capi-hidebug-hidebug-mallocdispatch.md#realloc) | 开发者自定义realloc函数指针。用于替代系统默认的realloc函数，在调整已分配内存大小时记录操作信息或执行自定义逻辑，可用于监控内存重分配行为和内存碎片分析。 |
| [void (\*free)(void\*)](capi-hidebug-hidebug-mallocdispatch.md#free) | 开发者自定义free函数指针。用于替代系统默认的free函数，在释放内存时记录释放信息，或执行自定义处理逻辑。使用时需确保传入的指针有效，避免重复释放或释放野指针。 |
| [void\* (\*mmap)(void\*, size\_t, int, int, int, off\_t)](capi-hidebug-hidebug-mallocdispatch.md#mmap) | 开发者自定义mmap函数指针。用于替代系统默认的mmap函数，在内存映射时记录映射信息或执行自定义逻辑，可用于监控大块内存映射操作和共享内存使用情况。 |
| [int (\*munmap)(void\*, size\_t)](capi-hidebug-hidebug-mallocdispatch.md#munmap) | 开发者自定义munmap函数指针。用于替代系统默认的munmap函数，在取消内存映射时记录操作信息或执行自定义逻辑，可配合mmap函数进行映射内存的生命周期管理。 |

## 成员函数说明

### malloc()

```c
void* (*malloc)(size_t)
```

**描述**

开发者自定义malloc函数指针。用于替代系统默认的内存分配函数，在分配内存时记录分配信息或执行自定义逻辑，可用于内存泄漏追踪和性能监控。

### calloc()

```c
void* (*calloc)(size_t, size_t)
```

**描述**

开发者自定义calloc函数指针。用于替代系统默认的calloc函数，在分配并初始化零内存时记录分配信息或执行自定义逻辑，可用于追踪大块内存分配和内存初始化监控。

### realloc()

```c
void* (*realloc)(void*, size_t)
```

**描述**

开发者自定义realloc函数指针。用于替代系统默认的realloc函数，在调整已分配内存大小时记录操作信息或执行自定义逻辑，可用于监控内存重分配行为和内存碎片分析。

### free()

```c
void (*free)(void*)
```

**描述**

开发者自定义free函数指针。用于替代系统默认的free函数，在释放内存时记录释放信息，或执行自定义处理逻辑。使用时需确保传入的指针有效，避免重复释放或释放野指针。

### mmap()

```c
void* (*mmap)(void*, size_t, int, int, int, off_t)
```

**描述**

开发者自定义mmap函数指针。用于替代系统默认的mmap函数，在内存映射时记录映射信息或执行自定义逻辑，可用于监控大块内存映射操作和共享内存使用情况。

### munmap()

```c
int (*munmap)(void*, size_t)
```

**描述**

开发者自定义munmap函数指针。用于替代系统默认的munmap函数，在取消内存映射时记录操作信息或执行自定义逻辑，可配合mmap函数进行映射内存的生命周期管理。
