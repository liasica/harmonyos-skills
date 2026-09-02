---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sleep-h
title: sleep.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > sleep.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4847273f23634c299f1b5ce094ef504af4c580cec76137f04777ae9d8e291f02
---

## 概述

声明[ffrt\_usleep](capi-sleep-h.md#ffrt_usleep)和[ffrt\_yield](capi-sleep-h.md#ffrt_yield)的C接口。

**引用文件：** <ffrt/sleep.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_usleep(uint64\_t usec)](capi-sleep-h.md#ffrt_usleep) | 将调用线程挂起指定的时长。若usec超过支持的最大值则按最大值截断。 |
| [FFRT\_C\_API void ffrt\_yield(void)](capi-sleep-h.md#ffrt_yield) | 将控制权让出给其他任务，使其有机会被执行。 |

## 函数说明

### ffrt\_usleep()

```c
FFRT_C_API int ffrt_usleep(uint64_t usec)
```

**描述**

将调用线程挂起指定的时长。若usec超过支持的最大值则按最大值截断。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t usec | 调用线程被挂起的时长，单位是微秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | ffrt\_success。该函数不会失败。 |

### ffrt\_yield()

```c
FFRT_C_API void ffrt_yield(void)
```

**描述**

将控制权让出给其他任务，使其有机会被执行。

**起始版本：** 10
