---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-queue-h
title: queue.h
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 头文件 > queue.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b76ecef736c475d1ff04f4519cbeaa4f0b844eb648f268689155565e057d515a
---

## 概述

声明队列的C接口。

**引用文件：** <ffrt/queue.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 队列句柄。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ffrt\_queue\_type\_t](capi-queue-h.md#ffrt_queue_type_t) | ffrt\_queue\_type\_t | 枚举队列类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FFRT\_C\_API int ffrt\_queue\_attr\_init(ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_init) | 初始化队列属性。该队列属性不再使用时，必须通过[ffrt\_queue\_attr\_destroy](capi-queue-h.md#ffrt_queue_attr_destroy)销毁。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_destroy(ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_destroy) | 销毁队列属性。该队列属性必须已通过[ffrt\_queue\_attr\_init](capi-queue-h.md#ffrt_queue_attr_init)初始化。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_qos(ffrt\_queue\_attr\_t\* attr, ffrt\_qos\_t qos)](capi-queue-h.md#ffrt_queue_attr_set_qos) | 设置队列属性的QoS。 |
| [FFRT\_C\_API ffrt\_qos\_t ffrt\_queue\_attr\_get\_qos(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_qos) | 获取队列属性的QoS。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_timeout(ffrt\_queue\_attr\_t\* attr, uint64\_t timeout\_us)](capi-queue-h.md#ffrt_queue_attr_set_timeout) | 设置队列属性的任务执行超时时长。 |
| [FFRT\_C\_API uint64\_t ffrt\_queue\_attr\_get\_timeout(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_timeout) | 获取队列属性的任务执行超时时长。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_callback(ffrt\_queue\_attr\_t\* attr, ffrt\_function\_header\_t\* f)](capi-queue-h.md#ffrt_queue_attr_set_callback) | 设置队列属性的超时回调函数。当队列中的任务执行时间超过通过[ffrt\_queue\_attr\_set\_timeout](capi-queue-h.md#ffrt_queue_attr_set_timeout)设置的超时时长时触发该回调。 |
| [FFRT\_C\_API ffrt\_function\_header\_t\* ffrt\_queue\_attr\_get\_callback(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_callback) | 获取队列属性的超时回调函数。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_max\_concurrency(ffrt\_queue\_attr\_t\* attr, const int max\_concurrency)](capi-queue-h.md#ffrt_queue_attr_set_max_concurrency) | 设置并发队列属性的最大并发度。 |
| [FFRT\_C\_API int ffrt\_queue\_attr\_get\_max\_concurrency(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_max_concurrency) | 获取并发队列属性的最大并发度。 |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_thread\_mode(ffrt\_queue\_attr\_t\* attr, bool mode)](capi-queue-h.md#ffrt_queue_attr_set_thread_mode) | 设置队列属性的执行模式。该接口指定队列中的任务是以协程模式还是线程模式执行。默认以协程模式执行。将mode设为true时启用基于线程的执行。 |
| [FFRT\_C\_API bool ffrt\_queue\_attr\_get\_thread\_mode(const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_attr_get_thread_mode) | 获取队列属性的执行模式。 |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_queue\_create(ffrt\_queue\_type\_t type, const char\* name, const ffrt\_queue\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_create) | 创建队列。该队列不再使用时，必须通过[ffrt\_queue\_destroy](capi-queue-h.md#ffrt_queue_destroy)销毁。 |
| [FFRT\_C\_API void ffrt\_queue\_destroy(ffrt\_queue\_t queue)](capi-queue-h.md#ffrt_queue_destroy) | 销毁队列。该队列必须已通过[ffrt\_queue\_create](capi-queue-h.md#ffrt_queue_create)创建。销毁时会取消尚未开始执行的任务，并阻塞等待正在执行的任务完成。 |
| [FFRT\_C\_API void ffrt\_queue\_submit(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit) | 提交任务到队列。 |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit_h) | 提交任务到队列，并获取任务句柄。 |
| [FFRT\_C\_API void ffrt\_queue\_submit\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit_f) | 提交任务到队列，是[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)接口的简化形式。该接口将给定的任务函数及其参数包装为用于队列提交的任务包装器（ffrt\_function\_kind\_queue）。其中用于处理执行后清理的任务销毁回调（after\_func）会被设为NULL，因而省略任何额外清理动作。生成的任务包装器随后通过[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)接口被提交到指定队列。 |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)](capi-queue-h.md#ffrt_queue_submit_h_f) | 提交任务到队列并获取任务句柄，是[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)接口的简化形式。该接口将给定的任务函数及其参数包装为用于队列提交的任务包装器（ffrt\_function\_kind\_queue）。其中用于处理执行后清理的任务销毁回调（after\_func）会被设为NULL，因而省略任何额外清理动作。生成的任务包装器随后通过[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)接口被提交到指定队列。 |
| [FFRT\_C\_API void ffrt\_queue\_wait(ffrt\_task\_handle\_t handle)](capi-queue-h.md#ffrt_queue_wait) | 等待队列中的任务执行完成。 |
| [FFRT\_C\_API int ffrt\_queue\_cancel(ffrt\_task\_handle\_t handle)](capi-queue-h.md#ffrt_queue_cancel) | 取消队列中的任务。已开始执行的任务无法被取消。 |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_main\_queue(void)](capi-queue-h.md#ffrt_get_main_queue) | 获取应用主线程队列。 |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_current\_queue(void)](capi-queue-h.md#ffrt_get_current_queue) | 获取应用Worker（ArkTS）线程队列。 |

## 枚举类型说明

### ffrt\_queue\_type\_t

```c
enum ffrt_queue_type_t
```

**描述**

枚举队列类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ffrt\_queue\_serial | 串行队列。 |
| ffrt\_queue\_concurrent | 并发队列。 |
| ffrt\_queue\_max | 最大有效队列类型值，作为哨兵使用（例如用于迭代）。 |

## 函数说明

### ffrt\_queue\_attr\_init()

```c
FFRT_C_API int ffrt_queue_attr_init(ffrt_queue_attr_t* attr)
```

**描述**

初始化队列属性。该队列属性不再使用时，必须通过[ffrt\_queue\_attr\_destroy](capi-queue-h.md#ffrt_queue_attr_destroy)销毁。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 队列属性初始化成功时返回0；  否则返回-1。 |

### ffrt\_queue\_attr\_destroy()

```c
FFRT_C_API void ffrt_queue_attr_destroy(ffrt_queue_attr_t* attr)
```

**描述**

销毁队列属性。该队列属性必须已通过[ffrt\_queue\_attr\_init](capi-queue-h.md#ffrt_queue_attr_init)初始化。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

### ffrt\_queue\_attr\_set\_qos()

```c
FFRT_C_API void ffrt_queue_attr_set_qos(ffrt_queue_attr_t* attr, ffrt_qos_t qos)
```

**描述**

设置队列属性的QoS。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |
| [ffrt\_qos\_t](capi-type-def-h.md#变量) qos | QoS等级，取值范围参见[ffrt\_qos\_t](capi-type-def-h.md#变量)枚举定义。 |

### ffrt\_queue\_attr\_get\_qos()

```c
FFRT_C_API ffrt_qos_t ffrt_queue_attr_get_qos(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列属性的QoS。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_qos\_t](capi-type-def-h.md#变量) | QoS等级，取值范围参见[ffrt\_qos\_t](capi-type-def-h.md#变量)枚举定义。 |

### ffrt\_queue\_attr\_set\_timeout()

```c
FFRT_C_API void ffrt_queue_attr_set_timeout(ffrt_queue_attr_t* attr, uint64_t timeout_us)
```

**描述**

设置队列属性的任务执行超时时长。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |
| uint64\_t timeout\_us | 队列任务执行超时时长，单位是微秒。下限为1000微秒（1毫秒），低于1000的值会被强制设为1000。 |

### ffrt\_queue\_attr\_get\_timeout()

```c
FFRT_C_API uint64_t ffrt_queue_attr_get_timeout(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列属性的任务执行超时时长。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API uint64\_t | 队列任务执行超时时长，单位是微秒。 |

### ffrt\_queue\_attr\_set\_callback()

```c
FFRT_C_API void ffrt_queue_attr_set_callback(ffrt_queue_attr_t* attr, ffrt_function_header_t* f)
```

**描述**

设置队列属性的超时回调函数。当队列中的任务执行时间超过通过[ffrt\_queue\_attr\_set\_timeout](capi-queue-h.md#ffrt_queue_attr_set_timeout)设置的超时时长时触发该回调。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* f | 队列超时回调函数。 |

### ffrt\_queue\_attr\_get\_callback()

```c
FFRT_C_API ffrt_function_header_t* ffrt_queue_attr_get_callback(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列属性的超时回调函数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* | 队列任务超时回调函数。 |

### ffrt\_queue\_attr\_set\_max\_concurrency()

```c
FFRT_C_API void ffrt_queue_attr_set_max_concurrency(ffrt_queue_attr_t* attr, const int max_concurrency)
```

**描述**

设置并发队列属性的最大并发度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |
| const int max\_concurrency | 队列可并发执行的最大任务数。 |

### ffrt\_queue\_attr\_get\_max\_concurrency()

```c
FFRT_C_API int ffrt_queue_attr_get_max_concurrency(const ffrt_queue_attr_t* attr)
```

**描述**

获取并发队列属性的最大并发度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 队列的最大并发度。 |

### ffrt\_queue\_attr\_set\_thread\_mode()

```c
FFRT_C_API void ffrt_queue_attr_set_thread_mode(ffrt_queue_attr_t* attr, bool mode)
```

**描述**

设置队列属性的执行模式。该接口指定队列中的任务是以协程模式还是线程模式执行。默认以协程模式执行。将mode设为true时启用基于线程的执行。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |
| bool mode | 是否启用基于线程的执行模式。- true：任务以原生线程执行（线程模式）。- false：任务以协程执行（默认）。 |

### ffrt\_queue\_attr\_get\_thread\_mode()

```c
FFRT_C_API bool ffrt_queue_attr_get_thread_mode(const ffrt_queue_attr_t* attr)
```

**描述**

获取队列属性的执行模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API bool | 任务以原生线程执行（线程模式）时返回true；  任务以协程执行（默认）时返回false。 |

### ffrt\_queue\_create()

```c
FFRT_C_API ffrt_queue_t ffrt_queue_create(ffrt_queue_type_t type, const char* name, const ffrt_queue_attr_t* attr)
```

**描述**

创建队列。该队列不再使用时，必须通过[ffrt\_queue\_destroy](capi-queue-h.md#ffrt_queue_destroy)销毁。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_type\_t](capi-queue-h.md#ffrt_queue_type_t) type | 队列类型。ffrt\_queue\_serial适用于任务需按顺序执行的场景；ffrt\_queue\_concurrent适用于任务可并发执行以提高吞吐量的场景。 |
| const char\* name | 指向队列名称的指针。 |
| [const ffrt\_queue\_attr\_t](capi-ffrt-ffrt-queue-attr-t.md)\* attr | 指向队列属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 队列创建成功时返回非空的队列句柄；  否则返回空指针。 |

### ffrt\_queue\_destroy()

```c
FFRT_C_API void ffrt_queue_destroy(ffrt_queue_t queue)
```

**描述**

销毁队列。该队列必须已通过[ffrt\_queue\_create](capi-queue-h.md#ffrt_queue_create)创建。销毁时会取消尚未开始执行的任务，并阻塞等待正在执行的任务完成。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |

### ffrt\_queue\_submit()

```c
FFRT_C_API void ffrt_queue_submit(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)
```

**描述**

提交任务到队列。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* f | 指向任务执行体的指针。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 指向任务属性的指针。 |

**参考：**

[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)

### ffrt\_queue\_submit\_h()

```c
FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h(ffrt_queue_t queue, ffrt_function_header_t* f, const ffrt_task_attr_t* attr)
```

**描述**

提交任务到队列，并获取任务句柄。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_header\_t](capi-ffrt-ffrt-function-header-t.md)\* f | 指向任务执行体的指针。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 指向任务属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) | 任务提交成功时返回非空的任务句柄；  否则返回空指针。 |

**参考：**

[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)

### ffrt\_queue\_submit\_f()

```c
FFRT_C_API void ffrt_queue_submit_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)
```

**描述**

提交任务到队列，是[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)接口的简化形式。该接口将给定的任务函数及其参数包装为用于队列提交的任务包装器（ffrt\_function\_kind\_queue）。其中用于处理执行后清理的任务销毁回调（after\_func）会被设为NULL，因而省略任何额外清理动作。生成的任务包装器随后通过[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)接口被提交到指定队列。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) func | 要执行的任务函数。 |
| void\* arg | 指向传递给任务函数的参数或闭包数据的指针。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 指向任务属性的指针。 |

**参考：**

[ffrt\_queue\_submit](capi-queue-h.md#ffrt_queue_submit)

### ffrt\_queue\_submit\_h\_f()

```c
FFRT_C_API ffrt_task_handle_t ffrt_queue_submit_h_f(ffrt_queue_t queue, ffrt_function_t func, void* arg, const ffrt_task_attr_t* attr)
```

**描述**

提交任务到队列并获取任务句柄，是[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)接口的简化形式。该接口将给定的任务函数及其参数包装为用于队列提交的任务包装器（ffrt\_function\_kind\_queue）。其中用于处理执行后清理的任务销毁回调（after\_func）会被设为NULL，因而省略任何额外清理动作。生成的任务包装器随后通过[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)接口被提交到指定队列。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) queue | 队列句柄。 |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) func | 要执行的任务函数。 |
| void\* arg | 指向传递给任务函数的参数或闭包数据的指针。 |
| [const ffrt\_task\_attr\_t](capi-ffrt-ffrt-task-attr-t.md)\* attr | 指向任务属性的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) | 任务提交成功时返回非空的任务句柄；  否则返回空指针。 |

**参考：**

[ffrt\_queue\_submit\_h](capi-queue-h.md#ffrt_queue_submit_h)

### ffrt\_queue\_wait()

```c
FFRT_C_API void ffrt_queue_wait(ffrt_task_handle_t handle)
```

**描述**

等待队列中的任务执行完成。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) handle | 任务句柄。 |

### ffrt\_queue\_cancel()

```c
FFRT_C_API int ffrt_queue_cancel(ffrt_task_handle_t handle)
```

**描述**

取消队列中的任务。已开始执行的任务无法被取消。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ffrt\_task\_handle\_t](capi-ffrt-ffrt-task-handle-t.md) handle | 任务句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API int | 任务取消成功时返回0；  任务已执行完毕或已从队列中移除时返回1；  handle为空时返回-1。 |

### ffrt\_get\_main\_queue()

```c
FFRT_C_API ffrt_queue_t ffrt_get_main_queue(void)
```

**描述**

获取应用主线程队列。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 应用主线程队列。 |

### ffrt\_get\_current\_queue()

```c
FFRT_C_API ffrt_queue_t ffrt_get_current_queue(void)
```

**描述**

获取应用Worker（ArkTS）线程队列。

**起始版本：** 12

**废弃版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| FFRT\_C\_API [ffrt\_queue\_t](capi-ffrt-ffrt-queue-t.md) | 应用Worker（ArkTS）线程队列。 |
