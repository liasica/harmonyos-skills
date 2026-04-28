---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h
title: loop.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 头文件 > loop.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6ad4532b14f94037dc61370f626d7713a1b778a0f15f3db6041c2144d417e77c
---

## 概述

PhonePC/2in1TabletTVWearable

声明循环的C接口。

**引用文件：** <ffrt/loop.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 12

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) | loop句柄。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API ffrt\_loop\_t ffrt\_loop\_create(ffrt\_queue\_t queue)](capi-loop-h.md#ffrt_loop_create) | 创建loop对象。 |
| [FFRT\_C\_API int ffrt\_loop\_destroy(ffrt\_loop\_t loop)](capi-loop-h.md#ffrt_loop_destroy) | 销毁loop对象。 |
| [FFRT\_C\_API int ffrt\_loop\_run(ffrt\_loop\_t loop)](capi-loop-h.md#ffrt_loop_run) | 开启loop循环。 |
| [FFRT\_C\_API void ffrt\_loop\_stop(ffrt\_loop\_t loop)](capi-loop-h.md#ffrt_loop_stop) | 停止loop循环。 |
| [FFRT\_C\_API int ffrt\_loop\_epoll\_ctl(ffrt\_loop\_t loop, int op, int fd, uint32\_t events, void \*data, ffrt\_poller\_cb cb)](capi-loop-h.md#ffrt_loop_epoll_ctl) | 管理loop上的监听事件。  不建议在cb中调用exit函数，可能导致未定义行为。 |
| [FFRT\_C\_API ffrt\_timer\_t ffrt\_loop\_timer\_start(ffrt\_loop\_t loop, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)](capi-loop-h.md#ffrt_loop_timer_start) | 在ffrt loop上启动定时器。  不建议在cb中调用exit函数，可能导致未定义行为。 |
| [FFRT\_C\_API int ffrt\_loop\_timer\_stop(ffrt\_loop\_t loop, ffrt\_timer\_t handle)](capi-loop-h.md#ffrt_loop_timer_stop) | 停止ffrt loop定时器。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### ffrt\_loop\_create()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_loop_t ffrt_loop_create(ffrt_queue_t queue)
```

**描述**

创建loop对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 并发队列。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) | 创建成功返回ffrt\_loop\_t对象，  创建失败返回空指针。 |

### ffrt\_loop\_destroy()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_loop_destroy(ffrt_loop_t loop)
```

**描述**

销毁loop对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 销毁成功返回0，  销毁失败返回-1。 |

### ffrt\_loop\_run()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_loop_run(ffrt_loop_t loop)
```

**描述**

开启loop循环。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | loop循环失败返回-1，  loop循环成功返回0。 |

### ffrt\_loop\_stop()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_loop_stop(ffrt_loop_t loop)
```

**描述**

停止loop循环。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop对象。 |

### ffrt\_loop\_epoll\_ctl()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_loop_epoll_ctl(ffrt_loop_t loop, int op, int fd, uint32_t events, void *data, ffrt_poller_cb cb)
```

**描述**

管理loop上的监听事件。

不建议在cb中调用exit函数，可能导致未定义行为。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop对象。 |
| int op | fd操作符。 |
| int fd | 事件描述符。 |
| uint32\_t events | 事件。 |
| void \*data | 事件变化时触发的回调函数的入参。 |
| [ffrt\_poller\_cb](capi-type-def-h.md#ffrt_poller_cb) cb | 事件变化时触发的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 成功返回0，  失败返回-1。 |

### ffrt\_loop\_timer\_start()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_timer_t ffrt_loop_timer_start(ffrt_loop_t loop, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```

**描述**

在ffrt loop上启动定时器。

不建议在cb中调用exit函数，可能导致未定义行为。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop对象。 |
| uint64\_t timeout | 超时时间(毫秒)。 |
| void\* data | 事件变化时触发的回调函数的入参。 |
| [ffrt\_timer\_cb](capi-type-def-h.md#ffrt_timer_cb) cb | 事件变化时触发的回调函数。 |
| bool repeat | 是否重复执行该定时器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_timer\_t](capi-type-def-h.md#变量) | 返回定时器句柄。 |

### ffrt\_loop\_timer\_stop()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_loop_timer_stop(ffrt_loop_t loop, ffrt_timer_t handle)
```

**描述**

停止ffrt loop定时器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ffrt\_loop\_t loop | loop对象。 |
| ffrt\_timer\_t handle | timer对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 成功返回0，  失败返回-1。 |
