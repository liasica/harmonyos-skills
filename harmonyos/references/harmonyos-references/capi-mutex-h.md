---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mutex-h
title: mutex.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > mutex.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:78c30a89f4819fd1f6f2da3d1dfb9e38085106f517fe0ac7cb3a527cfe3037a0
---

## 概述

声明互斥锁（mutex）的C接口，用于在并发任务间提供互斥访问，保护共享资源免受竞争条件影响。

**引用文件：** <ffrt/mutex.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_mutexattr\_init(ffrt\_mutexattr\_t\* attr)](capi-mutex-h.md#ffrt_mutexattr_init) | 初始化mutex属性。初始化成功后，mutex属性被设置为默认值。该mutex属性不再使用时，必须通过[ffrt\_mutexattr\_destroy](capi-mutex-h.md#ffrt_mutexattr_destroy)销毁。 |
| [FFRT\_C\_API int ffrt\_mutexattr\_settype(ffrt\_mutexattr\_t\* attr, int type)](capi-mutex-h.md#ffrt_mutexattr_settype) | 设置mutex属性的类型。类型可以是ffrt\_mutex\_normal（普通互斥锁）或ffrt\_mutex\_recursive（递归互斥锁，允许同一任务多次获取该锁）。 |
| [FFRT\_C\_API int ffrt\_mutexattr\_gettype(ffrt\_mutexattr\_t\* attr, int\* type)](capi-mutex-h.md#ffrt_mutexattr_gettype) | 获取mutex属性的类型。调用成功后，类型值通过出参type返回。 |
| [FFRT\_C\_API int ffrt\_mutexattr\_destroy(ffrt\_mutexattr\_t\* attr)](capi-mutex-h.md#ffrt_mutexattr_destroy) | 销毁mutex属性。该mutex属性必须已通过[ffrt\_mutexattr\_init](capi-mutex-h.md#ffrt_mutexattr_init)初始化。 |
| [FFRT\_C\_API int ffrt\_mutex\_init(ffrt\_mutex\_t\* mutex, const ffrt\_mutexattr\_t\* attr)](capi-mutex-h.md#ffrt_mutex_init) | 初始化mutex。该mutex不再使用时，必须通过[ffrt\_mutex\_destroy](capi-mutex-h.md#ffrt_mutex_destroy)销毁。通过attr传入已配置的mutex属性，或传入空指针使用默认值。 |
| [FFRT\_C\_API int ffrt\_mutex\_lock(ffrt\_mutex\_t\* mutex)](capi-mutex-h.md#ffrt_mutex_lock) | 加锁mutex。若mutex已被其他线程持有，则阻塞当前线程直到mutex可用。成功时，调用线程持有该mutex，直至通过[ffrt\_mutex\_unlock](capi-mutex-h.md#ffrt_mutex_unlock)释放。 |
| [FFRT\_C\_API int ffrt\_mutex\_unlock(ffrt\_mutex\_t\* mutex)](capi-mutex-h.md#ffrt_mutex_unlock) | 解锁mutex。调用线程必须已持有该mutex，且该锁之前由[ffrt\_mutex\_lock](capi-mutex-h.md#ffrt_mutex_lock)或[ffrt\_mutex\_trylock](capi-mutex-h.md#ffrt_mutex_trylock)获取。 |
| [FFRT\_C\_API int ffrt\_mutex\_trylock(ffrt\_mutex\_t\* mutex)](capi-mutex-h.md#ffrt_mutex_trylock) | 尝试加锁mutex。该接口为非阻塞操作：若mutex已被其他线程持有，则立即返回错误码。成功时，调用线程持有该mutex，直至通过[ffrt\_mutex\_unlock](capi-mutex-h.md#ffrt_mutex_unlock)释放。 |
| [FFRT\_C\_API int ffrt\_mutex\_destroy(ffrt\_mutex\_t\* mutex)](capi-mutex-h.md#ffrt_mutex_destroy) | 销毁mutex。调用成功后，mutex占用的资源被释放，该mutex对象不可再使用。该mutex必须已通过[ffrt\_mutex\_init](capi-mutex-h.md#ffrt_mutex_init)初始化，且在调用本接口时不得被任何线程持有。 |

## 函数说明

### ffrt\_mutexattr\_init()

```c
FFRT_C_API int ffrt_mutexattr_init(ffrt_mutexattr_t* attr)
```

**描述**

初始化mutex属性。初始化成功后，mutex属性被设置为默认值。该mutex属性不再使用时，必须通过[ffrt\_mutexattr\_destroy](capi-mutex-h.md#ffrt_mutexattr_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md)\* attr | 指向mutex属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex属性初始化成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

### ffrt\_mutexattr\_settype()

```c
FFRT_C_API int ffrt_mutexattr_settype(ffrt_mutexattr_t* attr, int type)
```

**描述**

设置mutex属性的类型。类型可以是ffrt\_mutex\_normal（普通互斥锁）或ffrt\_mutex\_recursive（递归互斥锁，允许同一任务多次获取该锁）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md)\* attr | 指向mutex属性的指针。 |
| int type | mutex类型，取值为ffrt\_mutex\_normal、ffrt\_mutex\_recursive或ffrt\_mutex\_default（等价于ffrt\_mutex\_normal）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex属性类型设置成功时返回ffrt\_success；  当attr为空指针，或mutex属性类型既不是ffrt\_mutex\_normal也不是ffrt\_mutex\_recursive时  返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_mutex\_type](capi-type-def-h.md#ffrt_mutex_type)

### ffrt\_mutexattr\_gettype()

```c
FFRT_C_API int ffrt_mutexattr_gettype(ffrt_mutexattr_t* attr, int* type)
```

**描述**

获取mutex属性的类型。调用成功后，类型值通过出参type返回。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md)\* attr | 指向mutex属性的指针。 |
| int\* type | 指向mutex类型的指针，用于接收获取的类型值（ffrt\_mutex\_normal或ffrt\_mutex\_recursive）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex属性类型获取成功时返回ffrt\_success；  attr或type为空指针时返回ffrt\_error\_inval。 |

### ffrt\_mutexattr\_destroy()

```c
FFRT_C_API int ffrt_mutexattr_destroy(ffrt_mutexattr_t* attr)
```

**描述**

销毁mutex属性。该mutex属性必须已通过[ffrt\_mutexattr\_init](capi-mutex-h.md#ffrt_mutexattr_init)初始化。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md)\* attr | 指向mutex属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex属性销毁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

### ffrt\_mutex\_init()

```c
FFRT_C_API int ffrt_mutex_init(ffrt_mutex_t* mutex, const ffrt_mutexattr_t* attr)
```

**描述**

初始化mutex。该mutex不再使用时，必须通过[ffrt\_mutex\_destroy](capi-mutex-h.md#ffrt_mutex_destroy)销毁。通过attr传入已配置的mutex属性，或传入空指针使用默认值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向mutex的指针。 |
| [const ffrt\_mutexattr\_t](capi-ffrt-ffrt-mutexattr-t.md)\* attr | 指向mutex属性的指针，或传入空指针使用默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex初始化成功时返回ffrt\_success；  mutex为空，或attr非空但未指定合法的mutex类型时返回ffrt\_error\_inval。 |

### ffrt\_mutex\_lock()

```c
FFRT_C_API int ffrt_mutex_lock(ffrt_mutex_t* mutex)
```

**描述**

加锁mutex。若mutex已被其他线程持有，则阻塞当前线程直到mutex可用。成功时，调用线程持有该mutex，直至通过[ffrt\_mutex\_unlock](capi-mutex-h.md#ffrt_mutex_unlock)释放。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向mutex的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex加锁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_mutex\_trylock](capi-mutex-h.md#ffrt_mutex_trylock)

### ffrt\_mutex\_unlock()

```c
FFRT_C_API int ffrt_mutex_unlock(ffrt_mutex_t* mutex)
```

**描述**

解锁mutex。调用线程必须已持有该mutex，且该锁之前由[ffrt\_mutex\_lock](capi-mutex-h.md#ffrt_mutex_lock)或[ffrt\_mutex\_trylock](capi-mutex-h.md#ffrt_mutex_trylock)获取。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向mutex的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex解锁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

### ffrt\_mutex\_trylock()

```c
FFRT_C_API int ffrt_mutex_trylock(ffrt_mutex_t* mutex)
```

**描述**

尝试加锁mutex。该接口为非阻塞操作：若mutex已被其他线程持有，则立即返回错误码。成功时，调用线程持有该mutex，直至通过[ffrt\_mutex\_unlock](capi-mutex-h.md#ffrt_mutex_unlock)释放。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向mutex的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex加锁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval或ffrt\_error\_busy。 |

**参考：**

[ffrt\_mutex\_lock](capi-mutex-h.md#ffrt_mutex_lock)

### ffrt\_mutex\_destroy()

```c
FFRT_C_API int ffrt_mutex_destroy(ffrt_mutex_t* mutex)
```

**描述**

销毁mutex。调用成功后，mutex占用的资源被释放，该mutex对象不可再使用。该mutex必须已通过[ffrt\_mutex\_init](capi-mutex-h.md#ffrt_mutex_init)初始化，且在调用本接口时不得被任何线程持有。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_mutex\_t](capi-ffrt-ffrt-mutex-t.md)\* mutex | 指向mutex的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | mutex销毁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |
