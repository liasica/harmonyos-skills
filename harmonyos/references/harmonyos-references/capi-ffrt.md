---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt
title: FFRT
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 模块 > FFRT
category: harmonyos-references
scraped_at: 2026-09-02T14:52:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1fba9caa1075ebe04d87211b58bcc72f7a4f8a923ca4368220709aee3dac4172
---

## 概述

提供Function Flow Runtime（FFRT）C接口。FFRT是一种基于任务的并发运行时库，根据任务依赖关系自动调度任务，开发者无需手动管理线程。

**起始版本：** 10

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [condition\_variable.h](capi-condition-variable-h.md) | 声明条件变量的C接口。 |
| [fiber.h](capi-fiber-h.md) | 声明纤程的C接口。  纤程是一种轻量级的用户态线程，用于在用户空间内实现高效的任务调度和上下文切换。 |
| [loop.h](capi-loop-h.md) | 声明事件循环的C接口。 |
| [mutex.h](capi-mutex-h.md) | 声明互斥锁（mutex）的C接口，用于在并发任务间提供互斥访问，保护共享资源免受竞争条件影响。 |
| [queue.h](capi-queue-h.md) | 声明队列的C接口。 |
| [shared\_mutex.h](capi-shared-mutex-h.md) | 声明读写锁（rwlock）的C接口。 |
| [sleep.h](capi-sleep-h.md) | 声明[ffrt\_usleep](capi-sleep-h.md#ffrt_usleep)和[ffrt\_yield](capi-sleep-h.md#ffrt_yield)的C接口。 |
| [task.h](capi-task-h.md) | 声明FFRT任务的C接口，提供任务属性的初始化与销毁、任务QoS设置与获取、任务延迟时间管理、并发队列任务优先级管理、任务栈大小管理、任务提交调度执行、任务句柄引用计数管理以及任务等待等功能。 |
| [timer.h](capi-timer-h.md) | 声明定时器的C接口。  提供基于QoS等级的定时器能力，支持在指定超时时间后执行回调函数，可用于延时任务调度等场景。 |
| [type\_def.h](capi-type-def-h.md) | 定义通用类型。 |
