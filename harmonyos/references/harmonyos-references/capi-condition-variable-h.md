---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-condition-variable-h
title: condition_variable.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > condition_variable.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bdcfcd71c396f5083d2540f07fed5ce0c3a825fd52fa2844567a3510d82a78a0
---

## 概述

声明条件变量的C接口。

**引用文件：** <ffrt/condition\_variable.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_cond\_init(ffrt\_cond\_t\* cond, const ffrt\_condattr\_t\* attr)](capi-condition-variable-h.md#ffrt_cond_init) | 初始化条件变量。该条件变量不再使用时，必须通过[ffrt\_cond\_destroy](capi-condition-variable-h.md#ffrt_cond_destroy)销毁。 |
| [FFRT\_C\_API int ffrt\_cond\_signal(ffrt\_cond\_t\* cond)](capi-condition-variable-h.md#ffrt_cond_signal) | 唤醒至少一个阻塞在条件变量上的线程。 |
| [FFRT\_C\_API int ffrt\_cond\_broadcast(ffrt\_cond\_t\* cond)](capi-condition-variable-h.md#ffrt_cond_broadcast) | 唤醒当前阻塞在条件变量上的所有线程。 |
| [FFRT\_C\_API int ffrt\_cond\_wait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex)](capi-condition-variable-h.md#ffrt_cond_wait) | 将调用线程阻塞在条件变量上。调用线程在进入时必须持有该mutex。阻塞期间会原子地释放该mutex，并在函数返回前重新获取，因此调用方在唤醒时重新获得mutex的所有权。线程由另一个线程调用[ffrt\_cond\_signal](capi-condition-variable-h.md#ffrt_cond_signal)或[ffrt\_cond\_broadcast](capi-condition-variable-h.md#ffrt_cond_broadcast)唤醒。调用方需在唤醒后重新检查谓词，以防止虚假唤醒。 |
| [FFRT\_C\_API int ffrt\_cond\_timedwait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex, const struct timespec\* time\_point)](capi-condition-variable-h.md#ffrt_cond_timedwait) | 将调用线程阻塞至给定的时间点。如果在到达time\_point前没有调用[ffrt\_cond\_signal](capi-condition-variable-h.md#ffrt_cond_signal)或[ffrt\_cond\_broadcast](capi-condition-variable-h.md#ffrt_cond_broadcast)来唤醒线程，线程会被自动唤醒。 |
| [FFRT\_C\_API int ffrt\_cond\_destroy(ffrt\_cond\_t\* cond)](capi-condition-variable-h.md#ffrt_cond_destroy) | 销毁条件变量。该条件变量必须已通过[ffrt\_cond\_init](capi-condition-variable-h.md#ffrt_cond_init)初始化，且在调用本接口时不得被任何线程引用。 |

## 函数说明

### ffrt\_cond\_init()

```c
FFRT_C_API int ffrt_cond_init(ffrt_cond_t* cond, const ffrt_condattr_t* attr)
```

**描述**

初始化条件变量。该条件变量不再使用时，必须通过[ffrt\_cond\_destroy](capi-condition-variable-h.md#ffrt_cond_destroy)销毁。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md)\* cond | 指向条件变量的指针。 |
| [const ffrt\_condattr\_t](capi-ffrt-ffrt-condattr-t.md)\* attr | 指向条件变量属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 条件变量初始化成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

### ffrt\_cond\_signal()

```c
FFRT_C_API int ffrt_cond_signal(ffrt_cond_t* cond)
```

**描述**

唤醒至少一个阻塞在条件变量上的线程。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md)\* cond | 指向条件变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 线程被唤醒时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_cond\_wait](capi-condition-variable-h.md#ffrt_cond_wait)

### ffrt\_cond\_broadcast()

```c
FFRT_C_API int ffrt_cond_broadcast(ffrt_cond_t* cond)
```

**描述**

唤醒当前阻塞在条件变量上的所有线程。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md)\* cond | 指向条件变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 线程被唤醒时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_cond\_wait](capi-condition-variable-h.md#ffrt_cond_wait)

### ffrt\_cond\_wait()

```c
FFRT_C_API int ffrt_cond_wait(ffrt_cond_t* cond, ffrt_mutex_t* mutex)
```

**描述**

将调用线程阻塞在条件变量上。调用线程在进入时必须持有该mutex。阻塞期间会原子地释放该mutex，并在函数返回前重新获取，因此调用方在唤醒时重新获得mutex的所有权。线程由另一个线程调用[ffrt\_cond\_signal](capi-condition-variable-h.md#ffrt_cond_signal)或[ffrt\_cond\_broadcast](capi-condition-variable-h.md#ffrt_cond_broadcast)唤醒。调用方需在唤醒后重新检查谓词，以防止虚假唤醒。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md)\* cond | 指向条件变量的指针。 |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向调用线程持有的mutex的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 阻塞后被成功唤醒时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_cond\_timedwait](capi-condition-variable-h.md#ffrt_cond_timedwait)

[ffrt\_cond\_signal](capi-condition-variable-h.md#ffrt_cond_signal)

[ffrt\_cond\_broadcast](capi-condition-variable-h.md#ffrt_cond_broadcast)

### ffrt\_cond\_timedwait()

```c
FFRT_C_API int ffrt_cond_timedwait(ffrt_cond_t* cond, ffrt_mutex_t* mutex, const struct timespec* time_point)
```

**描述**

将调用线程阻塞至给定的时间点。如果在到达time\_point前没有调用[ffrt\_cond\_signal](capi-condition-variable-h.md#ffrt_cond_signal)或[ffrt\_cond\_broadcast](capi-condition-variable-h.md#ffrt_cond_broadcast)来唤醒线程，线程会被自动唤醒。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md)\* cond | 指向条件变量的指针。 |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向mutex的指针。 |
| const struct timespec\* time\_point | 等待到期的绝对时间点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 阻塞后被成功唤醒时返回ffrt\_success；  未被唤醒且到达time\_point时返回ffrt\_error\_timedout；  cond、mutex或time\_point任一为null时返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_cond\_wait](capi-condition-variable-h.md#ffrt_cond_wait)

[ffrt\_cond\_signal](capi-condition-variable-h.md#ffrt_cond_signal)

[ffrt\_cond\_broadcast](capi-condition-variable-h.md#ffrt_cond_broadcast)

### ffrt\_cond\_destroy()

```c
FFRT_C_API int ffrt_cond_destroy(ffrt_cond_t* cond)
```

**描述**

销毁条件变量。该条件变量必须已通过[ffrt\_cond\_init](capi-condition-variable-h.md#ffrt_cond_init)初始化，且在调用本接口时不得被任何线程引用。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_cond\_t](capi-ffrt-ffrt-cond-t.md)\* cond | 指向条件变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 条件变量销毁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |
