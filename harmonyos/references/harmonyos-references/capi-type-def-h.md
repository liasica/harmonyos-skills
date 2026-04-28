---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h
title: type_def.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 头文件 > type_def.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:01f5ac774ac4826cb60d64209bce0f44c9fc30eec805009fed5b27c4843f197c
---

## 概述

PhonePC/2in1TabletTVWearable

定义通用类型。

**引用文件：** <ffrt/type\_def.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| int | ffrt\_timer\_t | 定时器句柄。 |
| int | ffrt\_qos\_t | QoS类型。 |
| using qos = int | - | QoS类型。  **起始版本：** 10 |

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md) | ffrt\_function\_header\_t | 任务执行体。 |
| [ffrt\_dependence\_t](capi-ffrt-ffrt-dependence-t.md) | ffrt\_dependence\_t | 依赖数据结构。 |
| [ffrt\_deps\_t](capi-ffrt-ffrt-deps-t.md) | ffrt\_deps\_t | 依赖结构定义。 |
| [ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md) | ffrt\_task\_attr\_t | 并行任务属性结构。 |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md) | ffrt\_queue\_attr\_t | 串行队列属性结构。 |
| [ffrt\_condattr\_t](capi-ffrt-ffrt-condattr-t.md) | ffrt\_condattr\_t | FFRT条件变量属性结构。 |
| [ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md) | ffrt\_mutexattr\_t | FFRT锁属性结构。 |
| [ffrt\_rwlockattr\_t](capi-ffrt-ffrt-rwlockattr-t.md) | ffrt\_rwlockattr\_t | FFRT读写锁属性结构。 |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md) | ffrt\_mutex\_t | FFRT互斥锁结构。 |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md) | ffrt\_rwlock\_t | FFRT读写锁结构。 |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md) | ffrt\_cond\_t | FFRT条件变量结构。 |
| void\* | [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) | 并行任务句柄。 |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md) | ffrt\_fiber\_t | 纤程结构。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ffrt\_queue\_priority\_t](capi-type-def-h.md#ffrt_queue_priority_t) | ffrt\_queue\_priority\_t | 任务的优先级类型。 |
| [ffrt\_qos\_default\_t](capi-type-def-h.md#ffrt_qos_default_t) | ffrt\_qos\_default\_t | 任务的QoS类型。 |
| [ffrt\_storage\_size\_t](capi-type-def-h.md#ffrt_storage_size_t) | ffrt\_storage\_size\_t | 多种类型数据结构分配大小定义。 |
| [ffrt\_function\_kind\_t](capi-type-def-h.md#ffrt_function_kind_t) | ffrt\_function\_kind\_t | 任务类型。 |
| [ffrt\_dependence\_type\_t](capi-type-def-h.md#ffrt_dependence_type_t) | ffrt\_dependence\_type\_t | 依赖类型。 |
| [ffrt\_error\_t](capi-type-def-h.md#ffrt_error_t) | ffrt\_error\_t | FFRT错误码。 |
| [ffrt\_mutex\_type](capi-type-def-h.md#ffrt_mutex_type) | ffrt\_mutex\_type | 互斥锁类型枚举。描述互斥类型，ffrt\_mutex\_normal是普通互斥锁；ffrt\_mutex\_recursive是递归互斥锁，ffrt\_mutex\_default是普通互斥锁。 |
| [qos\_default](capi-type-def-h.md#qos_default) | - | 任务QoS类型枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void(\*ffrt\_function\_t)(void\*)](capi-type-def-h.md#ffrt_function_t) | ffrt\_function\_t | 任务执行函数指针类型。 |
| [typedef void (\*ffrt\_poller\_cb)(void\* data, uint32\_t event)](capi-type-def-h.md#ffrt_poller_cb) | ffrt\_poller\_cb | poller回调函数定义。 |
| [typedef void (\*ffrt\_timer\_cb)(void\* data)](capi-type-def-h.md#ffrt_timer_cb) | ffrt\_timer\_cb | timer回调函数定义。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ffrt\_queue\_priority\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_queue_priority_t
```

**描述**

任务的优先级类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_queue\_priority\_immediate = 0 | immediate 优先级 |
| ffrt\_queue\_priority\_high | high 优先级 |
| ffrt\_queue\_priority\_low | low 优先级 |
| ffrt\_queue\_priority\_idle | lowest 优先级 |

### ffrt\_qos\_default\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_qos_default_t
```

**描述**

任务的QoS类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_qos\_inherit = -1 | 继承当前任务QoS属性 |
| ffrt\_qos\_background | 后台任务 |
| ffrt\_qos\_utility | 实时工具 |
| ffrt\_qos\_default | 默认类型 |
| ffrt\_qos\_user\_initiated | 用户期望 |
| ffrt\_qos\_deadline\_request | 时限请求  **起始版本：** 23 |
| ffrt\_qos\_user\_interactive | 用户交互  **起始版本：** 23 |
| ffrt\_qos\_max = ffrt\_qos\_user\_interactive | 最高QoS等级  **起始版本：** 23 |

### ffrt\_storage\_size\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_storage_size_t
```

**描述**

多种类型数据结构分配大小定义。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_task\_attr\_storage\_size = 128 | 任务属性 |
| ffrt\_auto\_managed\_function\_storage\_size = 64 + sizeof(ffrt\_function\_header\_t) | 任务执行体 |
| ffrt\_mutex\_storage\_size = 64 | 互斥锁 |
| ffrt\_cond\_storage\_size = 64 | 条件变量 |
| ffrt\_queue\_attr\_storage\_size = 128 | 队列属性 |
| ffrt\_rwlock\_storage\_size = 64 | 读写锁  **起始版本：** 18 |
| ffrt\_fiber\_storage\_size | 纤程在不同平台所占大小，单位：Byte。（平台相关）aarch64架构：22字节；arm架构：64字节；x86\_64架构：8字节；其他平台：不支持。  **起始版本：** 20 |

### ffrt\_function\_kind\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_function_kind_t
```

**描述**

任务类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_function\_kind\_general | 通用任务类型 |
| ffrt\_function\_kind\_queue | 队列任务类型 |

### ffrt\_dependence\_type\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_dependence_type_t
```

**描述**

依赖类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_dependence\_data | 数据依赖类型 |
| ffrt\_dependence\_task | 任务依赖类型 |

### ffrt\_error\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_error_t
```

**描述**

FFRT错误码。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_error = -1 | 失败 |
| ffrt\_success = 0 | 成功 |
| ffrt\_error\_nomem = ENOMEM | 内存不足 |
| ffrt\_error\_timedout = ETIMEDOUT | 超时 |
| ffrt\_error\_busy = EBUSY | 重新尝试 |
| ffrt\_error\_inval = EINVAL | 值无效 |

### ffrt\_mutex\_type

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_mutex_type
```

**描述**

互斥锁类型枚举。描述互斥类型，ffrt\_mutex\_normal是普通互斥锁；ffrt\_mutex\_recursive是递归互斥锁，ffrt\_mutex\_default是普通互斥锁。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_mutex\_normal = 0 | 普通互斥锁 |
| ffrt\_mutex\_recursive = 2 | 递归互斥锁 |
| ffrt\_mutex\_default = ffrt\_mutex\_normal | 默认互斥锁 |

### qos\_default

PhonePC/2in1TabletTVWearable

```
1. enum qos_default
```

**描述**

任务QoS类型枚举。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| qos\_inherit = ffrt\_qos\_inherit | 继承当前任务的QoS类型 |
| qos\_background = ffrt\_qos\_background | 后台任务 |
| qos\_utility = ffrt\_qos\_utility | 实时工具 |
| qos\_default = ffrt\_qos\_default | 默认类型 |
| qos\_user\_initiated = ffrt\_qos\_user\_initiated | 用户期望 |
| qos\_deadline\_request = ffrt\_qos\_deadline\_request | 时限请求  **起始版本：** 23 |
| qos\_user\_interactive = ffrt\_qos\_user\_interactive | 用户交互  **起始版本：** 23 |
| qos\_max = ffrt\_qos\_user\_interactive | 最高QoS等级  **起始版本：** 23 |

## 函数说明

PhonePC/2in1TabletTVWearable

### ffrt\_function\_t()

PhonePC/2in1TabletTVWearable

```
1. typedef void(*ffrt_function_t)(void*)
```

**描述**

任务执行函数指针类型。

**起始版本：** 10

### ffrt\_poller\_cb()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*ffrt_poller_cb)(void* data, uint32_t event)
```

**描述**

poller回调函数定义。

**起始版本：** 12

### ffrt\_timer\_cb()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*ffrt_timer_cb)(void* data)
```

**描述**

timer回调函数定义。

**起始版本：** 12
