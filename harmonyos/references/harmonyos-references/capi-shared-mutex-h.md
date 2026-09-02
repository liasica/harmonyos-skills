---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-shared-mutex-h
title: shared_mutex.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > shared_mutex.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d5fa7da4bb423795cd03ea440d549aece446ccfabd31f44aa0e95c9c9bdc643d
---

## 概述

声明读写锁（rwlock）的C接口。

**引用文件：** <ffrt/shared\_mutex.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 18

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_rwlock\_init(ffrt\_rwlock\_t\* rwlock, const ffrt\_rwlockattr\_t\* attr)](capi-shared-mutex-h.md#ffrt_rwlock_init) | 初始化rwlock。该rwlock不再使用时，必须通过[ffrt\_rwlock\_destroy](capi-shared-mutex-h.md#ffrt_rwlock_destroy)销毁。 |
| [FFRT\_C\_API int ffrt\_rwlock\_wrlock(ffrt\_rwlock\_t\* rwlock)](capi-shared-mutex-h.md#ffrt_rwlock_wrlock) | 加写锁。锁不可用时阻塞当前线程。成功时，调用线程持有排他写锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。写锁具有排他性，不允许与任何读锁同时持有。 |
| [FFRT\_C\_API int ffrt\_rwlock\_trywrlock(ffrt\_rwlock\_t\* rwlock)](capi-shared-mutex-h.md#ffrt_rwlock_trywrlock) | 尝试加写锁。不会阻塞当前线程。成功时，调用线程持有排他写锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。 |
| [FFRT\_C\_API int ffrt\_rwlock\_rdlock(ffrt\_rwlock\_t\* rwlock)](capi-shared-mutex-h.md#ffrt_rwlock_rdlock) | 加读锁。锁不可用时阻塞当前线程。成功时，调用线程持有读锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。多个读者可同时持有该锁，但不允许与写锁同时持有。 |
| [FFRT\_C\_API int ffrt\_rwlock\_tryrdlock(ffrt\_rwlock\_t\* rwlock)](capi-shared-mutex-h.md#ffrt_rwlock_tryrdlock) | 尝试加读锁。不会阻塞当前线程。成功时，调用线程持有读锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。 |
| [FFRT\_C\_API int ffrt\_rwlock\_unlock(ffrt\_rwlock\_t\* rwlock)](capi-shared-mutex-h.md#ffrt_rwlock_unlock) | 解锁rwlock。调用线程必须已持有该rwlock，且该锁之前由[ffrt\_rwlock\_rdlock](capi-shared-mutex-h.md#ffrt_rwlock_rdlock)、[ffrt\_rwlock\_tryrdlock](capi-shared-mutex-h.md#ffrt_rwlock_tryrdlock)、[ffrt\_rwlock\_wrlock](capi-shared-mutex-h.md#ffrt_rwlock_wrlock)或[ffrt\_rwlock\_trywrlock](capi-shared-mutex-h.md#ffrt_rwlock_trywrlock)获取。 |
| [FFRT\_C\_API int ffrt\_rwlock\_destroy(ffrt\_rwlock\_t\* rwlock)](capi-shared-mutex-h.md#ffrt_rwlock_destroy) | 销毁rwlock。该rwlock必须已通过[ffrt\_rwlock\_init](capi-shared-mutex-h.md#ffrt_rwlock_init)初始化，且在调用本接口时不得被任何线程以读锁或写锁持有。 |

## 函数说明

### ffrt\_rwlock\_init()

```c
FFRT_C_API int ffrt_rwlock_init(ffrt_rwlock_t* rwlock, const ffrt_rwlockattr_t* attr)
```

**描述**

初始化rwlock。该rwlock不再使用时，必须通过[ffrt\_rwlock\_destroy](capi-shared-mutex-h.md#ffrt_rwlock_destroy)销毁。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |
| [const ffrt\_rwlockattr\_t](capi-ffrt-ffrt-rwlockattr-t.md)\* attr | 指向rwlock属性的指针。当前仅支持默认模式，需设置为空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock初始化成功且attr为空指针时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

### ffrt\_rwlock\_wrlock()

```c
FFRT_C_API int ffrt_rwlock_wrlock(ffrt_rwlock_t* rwlock)
```

**描述**

加写锁。锁不可用时阻塞当前线程。成功时，调用线程持有排他写锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。写锁具有排他性，不允许与任何读锁同时持有。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock加锁成功时返回ffrt\_success；  rwlock为空指针时返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_rwlock\_rdlock](capi-shared-mutex-h.md#ffrt_rwlock_rdlock)

[ffrt\_rwlock\_trywrlock](capi-shared-mutex-h.md#ffrt_rwlock_trywrlock)

### ffrt\_rwlock\_trywrlock()

```c
FFRT_C_API int ffrt_rwlock_trywrlock(ffrt_rwlock_t* rwlock)
```

**描述**

尝试加写锁。不会阻塞当前线程。成功时，调用线程持有排他写锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock加锁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval或ffrt\_error\_busy。 |

**参考：**

[ffrt\_rwlock\_wrlock](capi-shared-mutex-h.md#ffrt_rwlock_wrlock)

### ffrt\_rwlock\_rdlock()

```c
FFRT_C_API int ffrt_rwlock_rdlock(ffrt_rwlock_t* rwlock)
```

**描述**

加读锁。锁不可用时阻塞当前线程。成功时，调用线程持有读锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。多个读者可同时持有该锁，但不允许与写锁同时持有。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock加锁成功时返回ffrt\_success；  rwlock为空指针时返回ffrt\_error\_inval。 |

**参考：**

[ffrt\_rwlock\_wrlock](capi-shared-mutex-h.md#ffrt_rwlock_wrlock)

[ffrt\_rwlock\_tryrdlock](capi-shared-mutex-h.md#ffrt_rwlock_tryrdlock)

### ffrt\_rwlock\_tryrdlock()

```c
FFRT_C_API int ffrt_rwlock_tryrdlock(ffrt_rwlock_t* rwlock)
```

**描述**

尝试加读锁。不会阻塞当前线程。成功时，调用线程持有读锁，直至通过[ffrt\_rwlock\_unlock](capi-shared-mutex-h.md#ffrt_rwlock_unlock)释放。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock加锁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval或ffrt\_error\_busy。 |

**参考：**

[ffrt\_rwlock\_rdlock](capi-shared-mutex-h.md#ffrt_rwlock_rdlock)

### ffrt\_rwlock\_unlock()

```c
FFRT_C_API int ffrt_rwlock_unlock(ffrt_rwlock_t* rwlock)
```

**描述**

解锁rwlock。调用线程必须已持有该rwlock，且该锁之前由[ffrt\_rwlock\_rdlock](capi-shared-mutex-h.md#ffrt_rwlock_rdlock)、[ffrt\_rwlock\_tryrdlock](capi-shared-mutex-h.md#ffrt_rwlock_tryrdlock)、[ffrt\_rwlock\_wrlock](capi-shared-mutex-h.md#ffrt_rwlock_wrlock)或[ffrt\_rwlock\_trywrlock](capi-shared-mutex-h.md#ffrt_rwlock_trywrlock)获取。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock解锁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |

### ffrt\_rwlock\_destroy()

```c
FFRT_C_API int ffrt_rwlock_destroy(ffrt_rwlock_t* rwlock)
```

**描述**

销毁rwlock。该rwlock必须已通过[ffrt\_rwlock\_init](capi-shared-mutex-h.md#ffrt_rwlock_init)初始化，且在调用本接口时不得被任何线程以读锁或写锁持有。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_rwlock\_t](capi-ffrt-ffrt-rwlock-t.md)\* rwlock | 指向rwlock的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | rwlock销毁成功时返回ffrt\_success；  否则返回ffrt\_error\_inval。 |
