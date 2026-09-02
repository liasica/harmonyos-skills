---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fiber-h
title: fiber.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > fiber.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:18be0a40ed99a429812b98e180f46418ca00f91320c01fd489e31b0e90a32442
---

## 概述

声明纤程的C接口。纤程是一种轻量级的用户态线程，用于在用户空间内实现高效的任务调度和上下文切换。

**引用文件：** <ffrt/fiber.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 20

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_fiber\_init(ffrt\_fiber\_t\* fiber, void(\*func)(void\*), void\* arg, void\* stack, size\_t stack\_size)](capi-fiber-h.md#ffrt_fiber_init) | 初始化纤程。初始化纤程结构，使其准备好被执行。调用者需负责分配stack指向的栈内存，并保证该内存在纤程整个生命周期内有效。 |
| [FFRT\_C\_API void ffrt\_fiber\_switch(ffrt\_fiber\_t\* from, ffrt\_fiber\_t\* to)](capi-fiber-h.md#ffrt_fiber_switch) | 在两个纤程间切换执行上下文。将当前执行上下文保存到from指定的纤程中，并从to指定的纤程恢复执行上下文。from和to都必须指向已通过[ffrt\_fiber\_init](capi-fiber-h.md#ffrt_fiber_init)初始化的纤程实例；否则行为未定义。 |

## 函数说明

### ffrt\_fiber\_init()

```c
FFRT_C_API int ffrt_fiber_init(ffrt_fiber_t* fiber, void(*func)(void*), void* arg, void* stack, size_t stack_size)
```

**描述**

初始化纤程。初始化纤程结构，使其准备好被执行。调用者需负责分配stack指向的栈内存，并保证该内存在纤程整个生命周期内有效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md)\* fiber | 指向待初始化的纤程结构的指针。 |
| void(\*func)(void\*) | 纤程将执行的入口函数。 |
| void\* arg | 传递给入口函数的参数。 |
| void\* stack | 指向纤程栈所用内存区域的指针。 |
| size\_t stack\_size | 栈的大小，单位是字节。必须足以容纳纤程上下文。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 纤程初始化成功时返回ffrt\_success；  stack\_size过小（不足以容纳纤程上下文）时返回ffrt\_error\_inval。 |

### ffrt\_fiber\_switch()

```c
FFRT_C_API void ffrt_fiber_switch(ffrt_fiber_t* from, ffrt_fiber_t* to)
```

**描述**

在两个纤程间切换执行上下文。将当前执行上下文保存到from指定的纤程中，并从to指定的纤程恢复执行上下文。from和to都必须指向已通过[ffrt\_fiber\_init](capi-fiber-h.md#ffrt_fiber_init)初始化的纤程实例；否则行为未定义。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md)\* from | 指向用于保存当前上下文的纤程的指针。 |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md)\* to | 指向用于恢复执行上下文的纤程的指针。 |

**参考：**

[ffrt\_fiber\_init](capi-fiber-h.md#ffrt_fiber_init)
