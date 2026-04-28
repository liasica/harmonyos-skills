---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sleep-h
title: sleep.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 头文件 > sleep.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c447017cc5125488b510f2cb8fb7f7e33f474ca4ad7ed845e12ac5333ed2500a
---

## 概述

PhonePC/2in1TabletTVWearable

声明sleep和yield的C接口。

**引用文件：** <ffrt/sleep.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_usleep(uint64\_t usec)](capi-sleep-h.md#ffrt_usleep) | 睡眠调用线程固定的时间。 |
| [FFRT\_C\_API void ffrt\_yield(void)](capi-sleep-h.md#ffrt_yield) | 当前任务主动放权，让其他任务有机会调度执行。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### ffrt\_usleep()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_usleep(uint64_t usec)
```

**描述**

睡眠调用线程固定的时间。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint64\_t usec | 睡眠时间，单位是微秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 执行成功时返回ffrt\_success，  执行失败时返回ffrt\_error。 |

### ffrt\_yield()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_yield(void)
```

**描述**

当前任务主动放权，让其他任务有机会调度执行。

**起始版本：** 10
