---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fiber-h
title: fiber.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 头文件 > fiber.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a392e02703a4db514b110bcf3469a6722121f0d2d09f4bcc5b5655e02f22d490
---

## 概述

PhonePC/2in1TabletTVWearable

纤程是一种轻量级的用户态线程，用于在用户空间内实现高效的任务调度和上下文切换，此为声明纤程的C接口。

**引用文件：** <ffrt/fiber.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 20

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_fiber\_init(ffrt\_fiber\_t\* fiber, void(\*func)(void\*), void\* arg, void\* stack, size\_t stack\_size)](capi-fiber-h.md#ffrt_fiber_init) | 纤程初始化函数，此函数初始化纤程实例，该实例可以存储上下文。 |
| [FFRT\_C\_API void ffrt\_fiber\_switch(ffrt\_fiber\_t\* from, ffrt\_fiber\_t\* to)](capi-fiber-h.md#ffrt_fiber_switch) | 纤程切换函数，调用该函数的线程会暂停当前任务的执行，并将当前上下文保存到from纤程中，同时恢复to纤程中的上下文。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### ffrt\_fiber\_init()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_fiber_init(ffrt_fiber_t* fiber, void(*func)(void*), void* arg, void* stack, size_t stack_size)
```

**描述**

纤程初始化函数，此函数初始化纤程实例，该实例可以存储上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| fiber | 指向要初始化的纤程的指针, 具体可参考[ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md)。 |
| func | 纤程切换后所要执行的方法。 |
| void\* arg | 纤程切换后所要执行方法的入参。 |
| void\* stack | 纤程堆栈内存指针。 |
| size\_t stack\_size | 纤程堆栈大小, 具体可参考[ffrt\_storage\_size\_t](capi-type-def-h.md#ffrt_storage_size_t)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 初始化成功返回ffrt\_success，否则返回ffrt\_error。 |

### ffrt\_fiber\_switch()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_fiber_switch(ffrt_fiber_t* from, ffrt_fiber_t* to)
```

**描述**

纤程切换函数，调用该函数的线程会暂停当前任务的执行，并将当前上下文保存到from纤程中，同时恢复to纤程中的上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md)\* from | 将要保存的纤程指针。 |
| [ffrt\_fiber\_t](capi-ffrt-ffrt-fiber-t.md)\* to | 将要恢复的纤程指针。 |
