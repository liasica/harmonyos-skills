---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-mallocdispatch
title: HiDebug_MallocDispatch
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_MallocDispatch
category: harmonyos-references
scraped_at: 2026-04-28T08:11:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eb7a6038fa1a2d21a1e3dd5a814eb55acf6eb9ffcd2df4bf925e4547cb7a8677
---

```
1. typedef struct HiDebug_MallocDispatch {...} HiDebug_MallocDispatch
```

## 概述

PhonePC/2in1TabletTVWearable

应用程序进程可替换/恢复的HiDebug\_MallocDispatch表结构类型定义。

**起始版本：** 20

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void\* (\*malloc)(size\_t)](capi-hidebug-hidebug-mallocdispatch.md#malloc) | 开发者自定义malloc函数指针。 |
| [void\* (\*calloc)(size\_t, size\_t)](capi-hidebug-hidebug-mallocdispatch.md#calloc) | 开发者自定义calloc函数指针。 |
| [void\* (\*realloc)(void\*, size\_t)](capi-hidebug-hidebug-mallocdispatch.md#realloc) | 开发者自定义realloc函数指针。 |
| [void (\*free)(void\*)](capi-hidebug-hidebug-mallocdispatch.md#free) | 开发者自定义free函数指针。 |
| [void\* (\*mmap)(void\*, size\_t, int, int, int, off\_t)](capi-hidebug-hidebug-mallocdispatch.md#mmap) | 开发者自定义mmap函数指针。 |
| [int (\*munmap)(void\*, size\_t)](capi-hidebug-hidebug-mallocdispatch.md#munmap) | 开发者自定义munmap函数指针。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### malloc()

PhonePC/2in1TabletTVWearable

```
1. void* (*malloc)(size_t)
```

**描述**

开发者自定义malloc函数指针。

### calloc()

PhonePC/2in1TabletTVWearable

```
1. void* (*calloc)(size_t, size_t)
```

**描述**

开发者自定义calloc函数指针。

### realloc()

PhonePC/2in1TabletTVWearable

```
1. void* (*realloc)(void*, size_t)
```

**描述**

开发者自定义realloc函数指针。

### free()

PhonePC/2in1TabletTVWearable

```
1. void (*free)(void*)
```

**描述**

开发者自定义free函数指针。

### mmap()

PhonePC/2in1TabletTVWearable

```
1. void* (*mmap)(void*, size_t, int, int, int, off_t)
```

**描述**

开发者自定义mmap函数指针。

### munmap()

PhonePC/2in1TabletTVWearable

```
1. int (*munmap)(void*, size_t)
```

**描述**

开发者自定义munmap函数指针。
