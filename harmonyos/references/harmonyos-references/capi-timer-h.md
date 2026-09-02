---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h
title: timer.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > timer.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e123c6eabb8c2c228f3b68da5a9ea54bc7363bca01688b66ff7cebda446a3977
---

## 概述

声明定时器的C接口。提供基于QoS等级的定时器能力，支持在指定超时时间后执行回调函数，可用于延时任务调度等场景。

**引用文件：** <ffrt/timer.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 12

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API ffrt\_timer\_t ffrt\_timer\_start(ffrt\_qos\_t qos, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)](capi-timer-h.md#ffrt_timer_start) | 在FFRT工作线程上启动定时器。避免在cb中调用exit或[ffrt\_timer\_stop](capi-timer-h.md#ffrt_timer_stop)，以防止未定义行为或死锁。 |
| [FFRT\_C\_API int ffrt\_timer\_stop(ffrt\_qos\_t qos, ffrt\_timer\_t handle)](capi-timer-h.md#ffrt_timer_stop) | 停止FFRT工作线程上的定时器。该接口为阻塞接口。请避免在回调函数内调用该接口，以防止死锁或同步问题。当handle对应的回调正在执行时，该函数会等待回调完成后再返回。 |

## 函数说明

### ffrt\_timer\_start()

```c
FFRT_C_API ffrt_timer_t ffrt_timer_start(ffrt_qos_t qos, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```

**描述**

在FFRT工作线程上启动定时器。避免在cb中调用exit或[ffrt\_timer\_stop](capi-timer-h.md#ffrt_timer_stop)，以防止未定义行为或死锁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_qos\_t](capi-type-def-h.md#变量) qos | 运行定时器的工作线程的QoS等级。 |
| uint64\_t timeout | 超时时间，单位是毫秒。 |
| void\* data | 传递给cb的用户数据。 |
| [ffrt\_timer\_cb](capi-type-def-h.md#ffrt_timer_cb) cb | 超时后执行的用户回调函数。 |
| bool repeat | 是否重复执行该定时器。true表示重复，false表示只执行一次。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_timer\_t](capi-type-def-h.md#变量) | 定时器句柄；若回调函数为空指针或QoS映射未注册则返回-1。 |

**参考：**

[ffrt\_timer\_stop](capi-timer-h.md#ffrt_timer_stop)

### ffrt\_timer\_stop()

```c
FFRT_C_API int ffrt_timer_stop(ffrt_qos_t qos, ffrt_timer_t handle)
```

**描述**

停止FFRT工作线程上的定时器。该接口为阻塞接口。请避免在回调函数内调用该接口，以防止死锁或同步问题。当handle对应的回调正在执行时，该函数会等待回调完成后再返回。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_qos\_t](capi-type-def-h.md#变量) qos | 运行定时器的工作线程的QoS等级。必须与[ffrt\_timer\_start](capi-timer-h.md#ffrt_timer_start)中使用的QoS等级一致。 |
| [ffrt\_timer\_t](capi-type-def-h.md#变量) handle | 目标定时器句柄，由[ffrt\_timer\_start](capi-timer-h.md#ffrt_timer_start)返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 操作成功时返回0；  否则返回-1。 |

**参考：**

[ffrt\_timer\_start](capi-timer-h.md#ffrt_timer_start)
