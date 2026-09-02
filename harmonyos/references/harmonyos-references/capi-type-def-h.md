---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h
title: type_def.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > type_def.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9ae426104e3204f22b6cd0a744673aa11b1672b163b258963b13c0d4be71cf2d
---

## 概述

定义通用类型。

**引用文件：** <ffrt/type\_def.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 变量

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| int | ffrt\_qos\_t | QoS类型，用于设置任务的QoS等级。 |
| int | ffrt\_timer\_t | 定时器句柄，用于标识已创建的定时器。 |
| using qos = int | - | QoS类型。  **起始版本：** 10 |

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md) | ffrt\_function\_header\_t | 任务执行体，用于定义任务的执行和销毁回调。exec回调在任务被调度时调用，destroy回调在任务完成后被调用以释放任务相关资源。两者共同管理FFRT任务的完整生命周期。 |
| [ffrt\_dependence\_t](capi-ffrt-ffrt-dependence-t.md) | ffrt\_dependence\_t | 依赖数据项结构，用于描述任务间的单个依赖关系。 |
| [ffrt\_deps\_t](capi-ffrt-ffrt-deps-t.md) | ffrt\_deps\_t | 依赖结构体，用于保存任务的依赖列表。 |
| [ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md) | ffrt\_task\_attr\_t | 任务属性结构体，用于存储任务的属性信息。 |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md) | ffrt\_queue\_attr\_t | 队列属性结构体，用于存储队列的属性信息。 |
| [ffrt\_condattr\_t](capi-ffrt-ffrt-condattr-t.md) | ffrt\_condattr\_t | 条件变量属性结构体，用于存储条件变量的属性信息。 |
| [ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md) | ffrt\_mutexattr\_t | 互斥锁属性结构体，用于存储互斥锁的属性信息。 |
| [ffrt\_rwlockattr\_t](capi-ffrt-ffrt-rwlockattr-t.md) | ffrt\_rwlockattr\_t | 读写锁属性结构体，用于存储读写锁的属性信息。 |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md) | ffrt\_mutex\_t | 互斥锁结构体，用于存储互斥锁的内部数据。 |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md) | ffrt\_rwlock\_t | 读写锁结构体，用于存储读写锁的内部数据。 |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md) | ffrt\_cond\_t | 条件变量结构体，用于存储条件变量的内部数据。 |
| [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) | ffrt\_task\_handle\_t | 任务句柄，用于标识不同的任务。 |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md) | ffrt\_fiber\_t | 纤程结构体，用于存储纤程执行上下文。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ffrt\_queue\_priority\_t](capi-type-def-h.md#ffrt_queue_priority_t) | ffrt\_queue\_priority\_t | 并发队列中用于排序任务调度的任务优先级类型枚举。 |
| [ffrt\_qos\_default\_t](capi-type-def-h.md#ffrt_qos_default_t) | ffrt\_qos\_default\_t | 任务QoS类型枚举。 |
| [ffrt\_storage\_size\_t](capi-type-def-h.md#ffrt_storage_size_t) | ffrt\_storage\_size\_t | 多种类型结构体的存储大小定义，单位是字节。 |
| [ffrt\_function\_kind\_t](capi-type-def-h.md#ffrt_function_kind_t) | ffrt\_function\_kind\_t | 任务类型枚举，用于区分通用并发任务和队列调度的任务。 |
| [ffrt\_dependence\_type\_t](capi-type-def-h.md#ffrt_dependence_type_t) | ffrt\_dependence\_type\_t | 依赖类型枚举。用于指定任务间的依赖关系（数据就绪或任务完成）。 |
| [ffrt\_error\_t](capi-type-def-h.md#ffrt_error_t) | ffrt\_error\_t | 错误码枚举，由FFRT接口返回。 |
| [ffrt\_mutex\_type](capi-type-def-h.md#ffrt_mutex_type) | ffrt\_mutex\_type | 互斥锁类型枚举。 |
| [qos\_default](capi-type-def-h.md#qos_default) | - | 任务QoS类型枚举。各枚举值与[ffrt\_qos\_default\_t](capi-type-def-h.md#ffrt_qos_default_t)中对应的枚举值等价。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void(\*ffrt\_function\_t)(void\*)](capi-type-def-h.md#ffrt_function_t) | ffrt\_function\_t | 任务执行函数指针类型。函数指针定义了FFRT任务的入口点。FFRT在调度执行任务时调用该函数，并通过参数传入用户数据指针。 |
| [typedef void (\*ffrt\_poller\_cb)(void\* data, uint32\_t event)](capi-type-def-h.md#ffrt_poller_cb) | ffrt\_poller\_cb | poller回调函数类型。当poller检测到已注册事件时调用该回调。data指针携带注册时传入的用户数据，event值标识触发的事件类型。 |
| [typedef void (\*ffrt\_timer\_cb)(void\* data)](capi-type-def-h.md#ffrt_timer_cb) | ffrt\_timer\_cb | 定时器回调函数类型。当定时器到期时调用该回调。data指针携带定时器注册时传入的用户数据。 |

## 枚举类型说明

### ffrt\_queue\_priority\_t

```c
enum ffrt_queue_priority_t
```

**描述**

并发队列中用于排序任务调度的任务优先级类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_queue\_priority\_immediate = 0 | 最高优先级。任务尽快被调度（句柄时间等于提交时间）；优先于high被调度。 |
| ffrt\_queue\_priority\_high | 高优先级。按句柄时间排序；优先于low被调度。 |
| ffrt\_queue\_priority\_low | 低优先级。按句柄时间排序；优先于idle被调度。 |
| ffrt\_queue\_priority\_idle | 最低优先级。按句柄时间排序；仅在队列中不存在其他优先级任务时才被调度。 |

### ffrt\_qos\_default\_t

```c
enum ffrt_qos_default_t
```

**描述**

任务QoS类型枚举。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_qos\_inherit = -1 | 继承。  继承调用线程的QoS。用于任务需要采用创建者优先级的场景。 |
| ffrt\_qos\_background | 后台任务。  最低优先级。用于用户无感知的工作，例如后台数据同步或日志刷新。 |
| ffrt\_qos\_utility | 实用工具类任务。  用于用户可感知但不主动等待的长时间任务，例如数据加载或内容索引。 |
| ffrt\_qos\_default | 默认类型。  无特殊QoS要求时使用的默认QoS，适用于大多数一般任务。 |
| ffrt\_qos\_user\_initiated | 用户发起的任务。  用于用户主动触发、需要快速响应但不阻塞UI的任务，例如打开文档或执行搜索。 |
| ffrt\_qos\_deadline\_request | 时限请求任务。  用于有明确截止时间的任务，系统优先保障其调度资源。  **起始版本：** 23 |
| ffrt\_qos\_user\_interactive | 用户交互任务。  适用于UI响应等需要立即与用户交互的操作。  **起始版本：** 23 |
| ffrt\_qos\_max = ffrt\_qos\_user\_interactive | 最高QoS等级。  等价于ffrt\_qos\_user\_interactive。  **起始版本：** 23 |

### ffrt\_storage\_size\_t

```c
enum ffrt_storage_size_t
```

**描述**

多种类型结构体的存储大小定义，单位是字节。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_task\_attr\_storage\_size = 128 | 任务属性存储大小，单位是字节。 |
| ffrt\_auto\_managed\_function\_storage\_size = 64 + sizeof(ffrt\_function\_header\_t) | 任务执行体存储大小，单位是字节。 |
| ffrt\_mutex\_storage\_size = 64 | 互斥锁存储大小，单位是字节。 |
| ffrt\_cond\_storage\_size = 64 | 条件变量存储大小，单位是字节。 |
| ffrt\_queue\_attr\_storage\_size = 128 | 队列属性存储大小，单位是字节。 |
| ffrt\_rwlock\_storage\_size = 64 | 读写锁存储大小，单位是字节。  **起始版本：** 18 |
| ffrt\_fiber\_storage\_size | 纤程存储大小，单位是字节。该常量定义纤程存储大小。实际值取决于目标架构：aarch64架构：22字节；arm架构：64字节；x86\_64架构：8字节；其他平台：不支持。  **起始版本：** 20 |

### ffrt\_function\_kind\_t

```c
enum ffrt_function_kind_t
```

**描述**

任务类型枚举，用于区分通用并发任务和队列调度的任务。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_function\_kind\_general | 通用任务。任务可提交到FFRT调度器并发执行。 |
| ffrt\_function\_kind\_queue | 队列任务。任务通过队列按提交顺序依次执行。 |

### ffrt\_dependence\_type\_t

```c
enum ffrt_dependence_type_t
```

**描述**

依赖类型枚举。用于指定任务间的依赖关系（数据就绪或任务完成）。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_dependence\_data | 数据依赖类型。任务仅在所引用的数据就绪后被调度。 |
| ffrt\_dependence\_task | 任务依赖类型。任务仅在所引用的任务完成后被调度。 |

### ffrt\_error\_t

```c
enum ffrt_error_t
```

**描述**

错误码枚举，由FFRT接口返回。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_error = -1 | 通用错误。 |
| ffrt\_success = 0 | 成功。 |
| ffrt\_error\_nomem = ENOMEM | 内存不足错误。 |
| ffrt\_error\_timedout = ETIMEDOUT | 超时错误。 |
| ffrt\_error\_busy = EBUSY | 资源忙碌错误。资源正忙，请稍后重试。 |
| ffrt\_error\_inval = EINVAL | 无效值错误。 |

### ffrt\_mutex\_type

```c
enum ffrt_mutex_type
```

**描述**

互斥锁类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_mutex\_normal = 0 | 普通互斥锁类型。 |
| ffrt\_mutex\_recursive = 2 | 递归互斥锁类型，允许同一线程对同一互斥锁多次加锁。 |
| ffrt\_mutex\_default = ffrt\_mutex\_normal | 默认互斥锁类型，等价于ffrt\_mutex\_normal。 |

### qos\_default

```c
enum qos_default
```

**描述**

任务QoS类型枚举。各枚举值与[ffrt\_qos\_default\_t](capi-type-def-h.md#ffrt_qos_default_t)中对应的枚举值等价。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| qos\_inherit = ffrt\_qos\_inherit | 继承。  继承调用线程的QoS。用于任务需要采用创建者优先级的场景。 |
| qos\_background = ffrt\_qos\_background | 后台任务。  最低优先级。用于用户无感知的工作，例如后台数据同步或日志刷新。 |
| qos\_utility = ffrt\_qos\_utility | 实用工具类任务。  用于用户可感知但不主动等待的长时间任务，例如数据加载或内容索引。 |
| qos\_default = ffrt\_qos\_default | 默认类型。  无特殊QoS要求时使用的默认QoS，适用于大多数一般任务。 |
| qos\_user\_initiated = ffrt\_qos\_user\_initiated | 用户发起的任务。  用于用户主动触发、需要快速响应但不阻塞UI的任务，例如打开文档或执行搜索。 |
| qos\_deadline\_request = ffrt\_qos\_deadline\_request | 时限请求任务。  用于有明确截止时间的任务，系统优先保障其调度资源。  **起始版本：** 23 |
| qos\_user\_interactive = ffrt\_qos\_user\_interactive | 用户交互任务。  适用于UI响应等需要立即与用户交互的操作。  **起始版本：** 23 |
| qos\_max = ffrt\_qos\_user\_interactive | 最高QoS等级。  等价于ffrt\_qos\_user\_interactive。  **起始版本：** 23 |

## 函数说明

### ffrt\_function\_t()

```c
typedef void(*ffrt_function_t)(void*)
```

**描述**

任务执行函数指针类型。函数指针定义了FFRT任务的入口点。FFRT在调度执行任务时调用该函数，并通过参数传入用户数据指针。

**起始版本：** 10

### ffrt\_poller\_cb()

```c
typedef void (*ffrt_poller_cb)(void* data, uint32_t event)
```

**描述**

poller回调函数类型。当poller检测到已注册事件时调用该回调。data指针携带注册时传入的用户数据，event值标识触发的事件类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* data | 指向poller注册时传入的用户数据指针。 |
| uint32\_t event | 触发回调的事件类型。 |

### ffrt\_timer\_cb()

```c
typedef void (*ffrt_timer_cb)(void* data)
```

**描述**

定时器回调函数类型。当定时器到期时调用该回调。data指针携带定时器注册时传入的用户数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* data | 指向定时器注册时传入的用户数据指针。 |
