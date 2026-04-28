---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-queue-h
title: queue.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 头文件 > queue.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7ae35bdda3cde1f02fbcf26f6a65be12687af998250501cb5ad67daf9246f7ea
---

## 概述

PhonePC/2in1TabletTVWearable

声明队列的C接口。

**引用文件：** <ffrt/queue.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 队列句柄。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ffrt\_queue\_type\_t](capi-queue-h.md#ffrt_queue_type_t) | ffrt\_queue\_type\_t | 队列类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_queue\_attr\_init(ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_init) | 初始化队列属性。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_destroy(ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_destroy) | 销毁队列属性。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_qos(ffrt\_queue\_attr\_t\* attr, ffrt\_qos\_t qos)](capi-queue-h.md#ffrt_queue_attr_set_qos) | 设置队列QoS属性。 |
| [FFRT\_C\_API ffrt\_qos\_t ffrt\_queue\_attr\_get\_qos(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_qos) | 获取队列QoS属性。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_timeout(ffrt\_queue\_attr\_t\* attr, uint64\_t timeout\_us)](capi-queue-h.md#ffrt_queue_attr_set_timeout) | 设置串行队列timeout属性。超时时间的最小值是1ms，如果设置的值小于1ms，那么超时时间被设置为1ms。 |
| [FFRT\_C\_API uint64\_t ffrt\_queue\_attr\_get\_timeout(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_timeout) | 获取串行队列任务执行的timeout时间。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_callback(ffrt\_queue\_attr\_t\* attr, ffrt\_function\_header\_t\* f)](capi-queue-h.md#ffrt_queue_attr_set_callback) | 设置串行队列超时回调方法。  不建议在f中调用exit函数，可能导致未定义行为。 |
| [FFRT\_C\_API ffrt\_function\_header\_t\* ffrt\_queue\_attr\_get\_callback(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_callback) | 获取串行队列超时回调方法。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_max\_concurrency(ffrt\_queue\_attr\_t\* attr, const int max\_concurrency)](capi-queue-h.md#ffrt_queue_attr_set_max_concurrency) | 设置并行队列最大并发度。 |
| [FFRT\_C\_API int ffrt\_queue\_attr\_get\_max\_concurrency(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_max_concurrency) | 获取并行队列最大并发度。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_thread\_mode(ffrt\_queue\_attr\_t\* attr, bool mode)](capi-queue-h.md#ffrt_queue_attr_set_thread_mode) | 设置队列中的任务是以协程模式还是以线程模式运行。默认以协程模式运行。 |
| [FFRT\_C\_API bool ffrt\_queue\_attr\_get\_thread\_mode(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_thread_mode) | 获取队列中的任务是以协程模式还是以线程模式运行。 |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_queue\_create(ffrt\_queue\_type\_t type, const char\* name, const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_create) | 创建队列。 |
| [FFRT\_C\_API void ffrt\_queue\_destroy(ffrt\_queue\_t queue)](capi-queue-h.md#ffrt_queue_destroy) | 销毁队列。 |
| [FFRT\_C\_API void ffrt\_queue\_submit(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit) | 提交一个任务到队列中调度执行。 |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit_h) | 提交一个任务到队列中调度执行，并返回任务句柄。 |
| [FFRT\_C\_API void ffrt\_queue\_submit\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit_f) | 提交一个任务到队列中调度执行，是ffrt\_queue\_submit接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt\_queue\_submit接口。 |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit_h_f) | 提交一个任务到队列中调度执行，并返回任务句柄，是ffrt\_queue\_submit\_h接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt\_queue\_submit\_h接口。 |
| [FFRT\_C\_API void ffrt\_queue\_wait(ffrt\_task\_handle\_t handle)](capi-queue-h.md#ffrt_queue_wait) | 等待队列中一个任务执行完成。 |
| [FFRT\_C\_API int ffrt\_queue\_cancel(ffrt\_task\_handle\_t handle)](capi-queue-h.md#ffrt_queue_cancel) | 取消队列中一个任务。 |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_main\_queue(void)](capi-queue-h.md#ffrt_get_main_queue) | 获取主线程队列。 |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_current\_queue(void)](capi-queue-h.md#ffrt_get_current_queue) | 获取应用Worker(ArkTs)线程队列。(API18废弃) |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ffrt\_queue\_type\_t

PhonePC/2in1TabletTVWearable

```
1. enum ffrt_queue_type_t
```

**描述**

队列类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_queue\_serial | 串行队列 |
| ffrt\_queue\_concurrent | 并行队列 |
| ffrt\_queue\_max | 无效队列类型 |

## 函数说明

PhonePC/2in1TabletTVWearable

### ffrt\_queue\_attr\_init()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_queue_attr_init(ffrt_queue_attr_t* attr)
```

**描述**

初始化队列属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 执行成功时返回0，  执行失败时返回-1。 |

### ffrt\_queue\_attr\_destroy()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_attr_destroy(ffrt_queue_attr_t* attr)
```

**描述**

销毁队列属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |

### ffrt\_queue\_attr\_set\_qos()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_attr_set_qos(ffrt_queue_attr_t* attr, ffrt_qos_t qos)
```

**描述**

设置队列QoS属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |
| [ffrt\_qos\_t](capi-type-def-h.md#变量) qos | QoS属性值。 |

### ffrt\_queue\_attr\_get\_qos()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_qos_t ffrt_queue_attr_get_qos(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列QoS属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_qos\_t](capi-type-def-h.md#变量) | 返回队列的QoS属性。 |

### ffrt\_queue\_attr\_set\_timeout()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_attr_set_timeout(ffrt_queue_attr_t* attr, uint64_t timeout_us)
```

**描述**

设置串行队列timeout属性。超时时间的最小值是1ms，如果设置的值小于1ms，那么超时时间被设置为1ms。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 串行队列属性指针。 |
| uint64\_t timeout\_us | 串行队列任务执行的timeout时间(微秒)。 |

### ffrt\_queue\_attr\_get\_timeout()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API uint64_t ffrt_queue_attr_get_timeout(const ffrt_queue_attr_t* attr)
```

**描述**

获取串行队列任务执行的timeout时间。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 串行队列属性指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API uint64\_t | 返回串行队列任务执行的timeout时间。 |

### ffrt\_queue\_attr\_set\_callback()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_attr_set_callback(ffrt_queue_attr_t* attr, ffrt_function_header_t* f)
```

**描述**

设置串行队列超时回调方法。

不建议在f中调用exit函数，可能导致未定义行为。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 串行队列属性指针。 |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* f | 超时回调方法执行体。 |

### ffrt\_queue\_attr\_get\_callback()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_function_header_t* ffrt_queue_attr_get_callback(const ffrt_queue_attr_t* attr)
```

**描述**

获取串行队列超时回调方法。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 串行队列属性指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* | 返回串行队列超时回调方法。 |

### ffrt\_queue\_attr\_set\_max\_concurrency()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_attr_set_max_concurrency(ffrt_queue_attr_t* attr, const int max_concurrency)
```

**描述**

设置并行队列最大并发度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |
| const int max\_concurrency | 最大并发度。 |

### ffrt\_queue\_attr\_get\_max\_concurrency()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_queue_attr_get_max_concurrency(const ffrt_queue_attr_t* attr)
```

**描述**

获取并行队列最大并发度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 返回最大并发度。 |

### ffrt\_queue\_attr\_set\_thread\_mode()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_attr_set_thread_mode(ffrt_queue_attr_t* attr, bool mode)
```

**描述**

设置队列中的任务是以协程模式还是以线程模式运行。默认以协程模式运行。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |
| bool mode | 设置队列任务运行方式。true表示以线程模式运行, false表示以协程方式运行。 |

### ffrt\_queue\_attr\_get\_thread\_mode()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API bool ffrt_queue_attr_get_thread_mode(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列中的任务是以协程模式还是以线程模式运行。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API bool | true表示以线程模式运行，false表示以协程模式运行。 |

### ffrt\_queue\_create()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_queue_t ffrt_queue_create(ffrt_queue_type_t type, const char* name, const ffrt_queue_attr_t* attr)
```

**描述**

创建队列。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_type\_t](capi-queue-h.md#ffrt_queue_type_t) type | 队列类型。 |
| const char\* name | 队列名字。 |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 队列属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 创建队列成功返回非空队列句柄，  创建队列失败返回空指针。 |

### ffrt\_queue\_destroy()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_destroy(ffrt_queue_t queue)
```

**描述**

销毁队列。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |

### ffrt\_queue\_submit()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_submit(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* f | 任务的执行体。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 任务属性。 |

### ffrt\_queue\_submit\_h()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行，并返回任务句柄。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* f | 任务的执行体。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 任务属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) | 提交成功返回非空任务句柄，  提交失败返回空指针。 |

### ffrt\_queue\_submit\_f()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_submit_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行，是ffrt\_queue\_submit接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt\_queue\_submit接口。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) func | 指定的任务函数。 |
| void\* arg | 传递给任务函数的参数。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 任务属性。 |

**参考：**

[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)

### ffrt\_queue\_submit\_h\_f()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)
```

**描述**

提交一个任务到队列中调度执行，并返回任务句柄，是ffrt\_queue\_submit\_h接口的简化包装形式。该接口假定任务不需要销毁回调函数，给定的任务函数和参数被包装为队列任务结构，并将封装后的任务结构和其他参数传递给ffrt\_queue\_submit\_h接口。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) func | 指定的任务函数。 |
| void\* arg | 传递给任务函数的参数。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 任务属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) | 提交成功返回非空任务句柄，  提交失败返回空指针。 |

**参考：**

[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)

### ffrt\_queue\_wait()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API void ffrt_queue_wait(ffrt_task_handle_t handle)
```

**描述**

等待队列中一个任务执行完成。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) handle | 任务句柄。 |

### ffrt\_queue\_cancel()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API int ffrt_queue_cancel(ffrt_task_handle_t handle)
```

**描述**

取消队列中一个任务。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) handle | 任务句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 取消任务成功返回0，  取消任务失败返回-1。 |

### ffrt\_get\_main\_queue()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_queue_t ffrt_get_main_queue(void)
```

**描述**

获取主线程队列。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 返回主线程队列句柄。 |

### ffrt\_get\_current\_queue()

PhonePC/2in1TabletTVWearable

```
1. FFRT_C_API ffrt_queue_t ffrt_get_current_queue(void)
```

**描述**

获取应用Worker(ArkTs)线程队列。

**起始版本：** 12

**废弃版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API ffrt\_queue\_t | 返回当前线程队列句柄。 |
