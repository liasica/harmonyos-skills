---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h
title: timer.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 头文件 > timer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:92dde4474bcf99302d3278d8007612b7b19995a309de74e43c0fd3cf1226b642
---

## 概述

PhonePC/2in1TabletTVWearable

声明定时器的C接口。

**引用文件：** <ffrt/timer.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 12

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API ffrt\_timer\_t ffrt\_timer\_start(ffrt\_qos\_t qos, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)](capi-timer-h.md#ffrt_timer_start) | 启动计时器。 |
| [FFRT\_C\_API int ffrt\_timer\_stop(ffrt\_qos\_t qos, ffrt\_timer\_t handle)](capi-timer-h.md#ffrt_timer_stop) | 关闭计时器。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### ffrt\_timer\_start()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_timer_t ffrt_timer_start(ffrt_qos_t qos, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```

**描述**

启动计时器。

不建议在cb中调用exit函数，可能导致未定义行为。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_qos\_t](capi-type-def-h.md#变量) qos | QoS等级。 |
| uint64\_t timeout | 超时时间(毫秒)。 |
| void\* data | 超时后回调函数的入参。 |
| [ffrt\_timer\_cb](capi-type-def-h.md#ffrt_timer_cb) cb | 超时执行的回调函数。 |
| bool repeat | 是否重复执行该定时器（该功能暂未支持）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_timer\_t](capi-type-def-h.md#变量) | 返回定时器句柄。 |

### ffrt\_timer\_stop()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_timer_stop(ffrt_qos_t qos, ffrt_timer_t handle)
```

**描述**

关闭计时器。

说明

为阻塞接口，请避免在回调函数callback内使用，防止死锁或同步问题。

当传入的handle对应的callback正在执行时，该函数会等待callback完成后再继续执行。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ffrt\_qos\_t qos | QoS等级。 |
| ffrt\_timer\_t handle | 定时器句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 关闭成功返回0，  关闭失败返回-1。 |
