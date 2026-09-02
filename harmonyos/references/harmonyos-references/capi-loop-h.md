---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h
title: loop.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > loop.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:45cf3d5eb8c949bad365513381f1c9c23fddf0e3e465998202019da5076be2d4
---

## 概述

声明事件循环的C接口。

**引用文件：** <ffrt/loop.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 12

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) | loop句柄，用于标识不同的loop。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API ffrt\_loop\_t ffrt\_loop\_create(ffrt\_queue\_t queue)](capi-loop-h.md#ffrt_loop_create) | 在指定的队列上创建loop，用于运行事件循环。 |
| [FFRT\_C\_API int ffrt\_loop\_destroy(ffrt\_loop\_t loop)](capi-loop-h.md#ffrt_loop_destroy) | 销毁loop。调用该接口可释放与loop关联的资源。 |
| [FFRT\_C\_API int ffrt\_loop\_run(ffrt\_loop\_t loop)](capi-loop-h.md#ffrt_loop_run) | 启动一次loop循环。该函数会独占调用线程，在当前调用线程中同步运行事件循环，直到调用[ffrt\_loop\_stop](capi-loop-h.md#ffrt_loop_stop)后才会返回。 |
| [FFRT\_C\_API void ffrt\_loop\_stop(ffrt\_loop\_t loop)](capi-loop-h.md#ffrt_loop_stop) | 停止loop循环。调用后，正在执行[ffrt\_loop\_run](capi-loop-h.md#ffrt_loop_run)的线程将停止循环并返回。 |
| [FFRT\_C\_API int ffrt\_loop\_epoll\_ctl(ffrt\_loop\_t loop, int op, int fd, uint32\_t events, void \*data, ffrt\_poller\_cb cb)](capi-loop-h.md#ffrt_loop_epoll_ctl) | 在ffrt loop上控制epoll文件描述符。在目标文件描述符上添加、修改或删除监听的事件。 |
| [FFRT\_C\_API ffrt\_timer\_t ffrt\_loop\_timer\_start(ffrt\_loop\_t loop, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)](capi-loop-h.md#ffrt_loop_timer_start) | 在ffrt loop上启动定时器。超时后调用回调函数；若repeat为true，则周期性重复触发。 |
| [FFRT\_C\_API int ffrt\_loop\_timer\_stop(ffrt\_loop\_t loop, ffrt\_timer\_t handle)](capi-loop-h.md#ffrt_loop_timer_stop) | 在ffrt loop上停止定时器。调用后，该定时器不再触发。 |

## 函数说明

### ffrt\_loop\_create()

```c
FFRT_C_API ffrt_loop_t ffrt_loop_create(ffrt_queue_t queue)
```

**描述**

在指定的队列上创建loop，用于运行事件循环。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) | loop创建成功时返回非空的loop句柄；  否则返回空指针。 |

### ffrt\_loop\_destroy()

```c
FFRT_C_API int ffrt_loop_destroy(ffrt_loop_t loop)
```

**描述**

销毁loop。调用该接口可释放与loop关联的资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | loop销毁成功时返回0；  否则返回-1。 |

### ffrt\_loop\_run()

```c
FFRT_C_API int ffrt_loop_run(ffrt_loop_t loop)
```

**描述**

启动一次loop循环。该函数会独占调用线程，在当前调用线程中同步运行事件循环，直到调用[ffrt\_loop\_stop](capi-loop-h.md#ffrt_loop_stop)后才会返回。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | loop运行成功时返回0；  否则返回-1。 |

**参考：**

[ffrt\_loop\_stop](capi-loop-h.md#ffrt_loop_stop)

### ffrt\_loop\_stop()

```c
FFRT_C_API void ffrt_loop_stop(ffrt_loop_t loop)
```

**描述**

停止loop循环。调用后，正在执行[ffrt\_loop\_run](capi-loop-h.md#ffrt_loop_run)的线程将停止循环并返回。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop句柄。 |

**参考：**

[ffrt\_loop\_run](capi-loop-h.md#ffrt_loop_run)

### ffrt\_loop\_epoll\_ctl()

```c
FFRT_C_API int ffrt_loop_epoll_ctl(ffrt_loop_t loop, int op, int fd, uint32_t events, void *data, ffrt_poller_cb cb)
```

**描述**

在ffrt loop上控制epoll文件描述符。在目标文件描述符上添加、修改或删除监听的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop句柄。 |
| int op | 在目标文件描述符上执行的操作类型，如添加、修改或删除。 |
| int fd | 执行操作的目标文件描述符。 |
| uint32\_t events | 监听的事件类型（如可读、可写等），支持按位或组合。 |
| void \*data | 传递给cb的用户数据。 |
| [ffrt\_poller\_cb](capi-type-def-h.md#ffrt_poller_cb) cb | 当目标fd被轮询到时执行的用户回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 操作成功时返回0；  否则返回-1。 |

### ffrt\_loop\_timer\_start()

```c
FFRT_C_API ffrt_timer_t ffrt_loop_timer_start(ffrt_loop_t loop, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```

**描述**

在ffrt loop上启动定时器。超时后调用回调函数；若repeat为true，则周期性重复触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop句柄。 |
| uint64\_t timeout | 超时时间，单位是毫秒，取值范围为[0, +∞)。 |
| void\* data | 传递给cb的用户数据。 |
| [ffrt\_timer\_cb](capi-type-def-h.md#ffrt_timer_cb) cb | 超时后执行的用户回调函数。 |
| bool repeat | 是否重复执行该定时器。true表示重复，false表示只执行一次。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_timer\_t](capi-type-def-h.md#变量) | 定时器句柄；若loop或cb为空则返回-1。 |

**参考：**

[ffrt\_loop\_timer\_stop](capi-loop-h.md#ffrt_loop_timer_stop)

### ffrt\_loop\_timer\_stop()

```c
FFRT_C_API int ffrt_loop_timer_stop(ffrt_loop_t loop, ffrt_timer_t handle)
```

**描述**

在ffrt loop上停止定时器。调用后，该定时器不再触发。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_loop\_t](capi-ffrt-ffrt-loop-t.md) loop | loop句柄。 |
| [ffrt\_timer\_t](capi-type-def-h.md#变量) handle | 定时器句柄，由[ffrt\_loop\_timer\_start](capi-loop-h.md#ffrt_loop_timer_start)返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 操作成功时返回0；  否则返回-1。 |

**参考：**

[ffrt\_loop\_timer\_start](capi-loop-h.md#ffrt_loop_timer_start)
