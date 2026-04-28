---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-data-types-interfaces
title: Node-API支持的数据类型和接口
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API支持的数据类型和接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28f7216cb0c9f7c16eed1be579a1efb9a427b2f424bc03d2c7a6a2d589f2a245
---

## Node-API的数据类型

### napi\_status

是一个枚举数据类型，表示Node-API接口返回的状态信息。

每当调用一个Node-API函数，都会返回该值，表示操作成功与否的相关信息。

```
1. typedef enum {
2. napi_ok,
3. napi_invalid_arg,
4. napi_object_expected,
5. napi_string_expected,
6. napi_name_expected,
7. napi_function_expected,
8. napi_number_expected,
9. napi_boolean_expected,
10. napi_array_expected,
11. napi_generic_failure,
12. napi_pending_exception,
13. napi_cancelled,
14. napi_escape_called_twice,
15. napi_handle_scope_mismatch,
16. napi_callback_scope_mismatch,
17. napi_queue_full,
18. napi_closing,
19. napi_bigint_expected,
20. napi_date_expected,
21. napi_arraybuffer_expected,
22. napi_detachable_arraybuffer_expected,
23. napi_would_deadlock, /* unused */
24. napi_no_external_buffers_allowed,
25. napi_cannot_run_js
26. } napi_status;
```

### napi\_extended\_error\_info

一个结构体，在调用Node-API接口不成功时存储了较为详细的错误信息。

```
1. typedef struct {
2. const char *error_message;
3. void *engine_reserved;
4. uint32_t engine_error_code;
5. napi_status error_code;
6. } napi_extended_error_info;
```

### napi\_value

napi\_value是一个C的结构体指针，表示一个ArkTS/JS对象的引用。napi\_value持有了ArkTS/JS对象，同时，napi\_value受[napi\_handle\_scope](napi-data-types-interfaces.md#内存管理类型)管理，scope中napi\_value持有的JS对象不会被释放；出scope后，napi\_value将失效，不再持有对应的ArkTS/JS对象。

### napi\_env

* 用于表示Node-API执行时的上下文，Native侧函数入参，并传递给函数中的Node-API接口。
* napi\_env与ArkTS/JS线程的上下文环境绑定，每一个napi\_env都持有独立的运行时上下文环境，当ArkTS/JS线程退出之后，相应的napi\_env将不再有效。
* 禁止缓存napi\_env，禁止在不同线程间传递napi\_env。

### napi\_threadsafe\_function

[napi\_threadsafe\_function](use-napi-thread-safety.md)用来创建一个线程安全的ArkTS/JS函数，可以在不同的线程中调用。可以用于将异步操作的结果传递给ArkTS/JS环境，例如从另一个线程中读取数据或执行计算密集型操作。线程安全函数回调的执行仅在创建线程安全函数的ArkTS线程中执行。通过使用napi\_threadsafe\_function，可以实现ArkTS/JS和C++之间的高效通信，同时保持线程安全性。

### napi\_threadsafe\_function\_release\_mode

该枚举类型定义了两个常量，用于指定以哪一种方式来释放线程安全函数。

```
1. typedef enum {
2. napi_tsfn_release,
3. napi_tsfn_abort
4. } napi_threadsafe_function_release_mode;
```

该值会传给napi\_release\_threadsafe\_function。

```
1. napi_release_threadsafe_function(napi_threadsafe_function func,
2. napi_threadsafe_function_release_mode mode);
```

* mode值为napi\_tsfn\_release时：表示将tsfn中持有的线程数减一，当线程数减到0时，线程安全函数tsfn将被销毁。
* mode值为napi\_tsfn\_abort时：该tsfn关闭，不能再调用此tsfn。

  如果设置为napi\_tsfn\_abort，利用napi\_call\_threadsafe\_function接口调用此tsfn时，该行为可能导致UAF问题————当napi\_tsfn\_abort被设置时，tsfn立刻关闭，不能再被调用。如果此时调用napi\_call\_threadsafe\_function，系统可能会返回napi\_closing状态，表示tsfn正在关闭，但是传递给tsfn的data并未被放入队列中，这意味着data可能未被正确处理。如果data指向的内存已经被释放（例如，tsfn的资源被释放），但调用者仍然尝试访问或使用data，就会出现UAF(Use-After-Free)问题。

### napi\_threadsafe\_function\_call\_mode

该枚举类型定义了两个常量，用于指定线程安全函数的调用模式。

数据结构如下所示：

```
1. typedef enum {
2. napi_tsfn_nonblocking,
3. napi_tsfn_blocking
4. } napi_threadsafe_function_call_mode;
```

* napi\_tsfn\_nonblocking：napi\_call\_threadsafe\_function是非阻塞的，如果队列已满，则返回napi\_queue\_full，从而阻止数据添加到队列中。
* napi\_tsfn\_blocking：napi\_call\_threadsafe\_function是阻塞的，直至队列中有空间可用。

### 内存管理类型

Node-API包含以下内存管理类型：

**napi\_handle\_scope**

napi\_handle\_scope数据类型是用来管理ArkTS/JS对象的生命周期的。它允许ArkTS/JS对象在一定范围内保持活动状态，以便在ArkTS/JS代码中使用。在创建napi\_handle\_scope时，所有在该范围内创建的ArkTS/JS对象都会保持活动状态，直到scope被关闭。这样可以做到ArkTS/JS对象生命周期最小化，[避免发生内存泄漏问题](napi-guidelines.md#生命周期管理)。同时，napi\_handle\_scope也可参考[生命周期类问题注意事项](../best-practices/bpta-scenario-stability-cppcrash.md#section1662118147417)

**napi\_escapable\_handle\_scope**

* 由napi\_open\_escapable\_handle\_scope接口创建，由napi\_close\_escapable\_handle\_scope接口关闭。
* 表示一种特殊类型的句柄范围，用于将在escapable\_handle\_scope范围内创建的值返回给父scope。
* 用于napi\_escape\_handle接口，将ArkTS/JS对象逃逸到父scope，以便在外部作用域使用。

**napi\_ref**

指向napi\_value，允许用户管理ArkTS/JS值的生命周期。

**napi\_type\_tag**

该结构体定义了一个包含两个无符号64位整数的类型标签，用于标识一个Node-API值的类型信息。

```
1. typedef struct {
2. uint64_t lower;
3. uint64_t upper;
4. } napi_type_tag;
```

* 存储了两个无符号64位整数的128位值，用它来标记ArkTS/JS对象，确保它们属于某种类型。
* 比napi\_instanceof更强的类型检查，如果对象的原型被操纵，napi\_instanceof可能会存在误报。
* type\_tag与napi\_wrap结合非常有用，因为它确保从包装对象检索的指针可以安全地转换为与先前应用于JavaScript对象的类型标记相对应的Native类型。

**napi\_async\_cleanup\_hook\_handle**

napi\_async\_cleanup\_hook\_handle是Node-API中用于管理异步资源生命周期的一种机制。它允许注册一个清理钩子（cleanup hook），该钩子仅在当前napi\_env环境生命周期结束时被调用。通过使用 napi\_async\_cleanup\_hook\_handle，可以确保某些异步资源在环境销毁前得到妥善释放，从而避免资源泄漏。此外，在Node-API实现中，只要该结构未被释放，会延迟整个 napi\_env 环境的销毁。在HarmonyOS中，该接口的行为基本等同于env生命周期相关的清理钩子，除了支持重复注册相同的上下文数据（data）外，其余行为与标准的env清理钩子一致。

**napi\_critical\_scope（扩展能力）**

napi\_critical\_scope是Node-API中，用于创建临界接口执行环境的机制。它由napi\_open\_critical\_scope接口创建，由napi\_close\_critical\_scope接口关闭。

临界接口：需要在临界区作用域内执行的接口，通常接口名中含有critical关键字。

**napi\_strong\_ref（扩展能力）**

指向napi\_value，允许用户管理ArkTS对象的生命周期。

**提示：** napi\_strong\_ref与napi\_ref相比，具有更高的创建效率，但支持的功能受限（如：不支持强弱引用转换等）。

**napi\_sendable\_ref（扩展能力）**

指向napi\_value，允许调用者管理Sendable ArkTS对象的生命周期，并支持跨ArkTS线程操作napi\_sendable\_ref。

**提示：** 与napi\_ref相比，napi\_sendable\_ref支持跨ArkTS线程操作（例如，在A线程创建napi\_sendable\_ref，B线程通过napi\_sendable\_ref获取napi\_value，C线程删除napi\_sendable\_ref。调用者需保证调用时序。），但功能上有以下限制：被引用napi\_value必须是Sendable的，不支持强弱引用转换。

### 回调类型

Node-API包含以下回调类型：

**napi\_callback\_info**

Native侧获取JS侧参数信息，传递给napi\_get\_cb\_info，用于获取JS侧入参信息。

**napi\_callback**

表示用户定义的Native函数，暴露给ArkTS/JS，即ArkTS/JS侧调用的接口；一般不需要在callback中创建handle或者callback scope。

基本用法如下：

```
1. typedef napi_value (*napi_callback)(napi_env, napi_callback_info);
```

**napi\_finalize**

函数指针，用于传入napi\_create\_threadsafe\_function、napi\_set\_instance\_data、napi\_wrap、napi\_add\_finalizer等接口。napi\_finalize在对象被回收时会被调用。

**napi\_async\_execute\_callback**

函数指针，用于napi\_create\_async\_work接口。

* 异步执行的Native函数，从工作池线程调用，可与事件循环线程并行执行。
* 函数实现中必须避免调用非线程安全的Node-API。
* Node-API调用可以在napi\_async\_complete\_callback中执行。

**napi\_async\_complete\_callback**

napi\_async\_complete\_callback用于异步操作完成后的回调。当需要进行异步操作时，可以使用napi\_create\_async\_work函数创建一个异步操作任务，并指定一个napi\_async\_complete\_callback回调函数，在异步操作完成后会自动调用该回调函数，以便进行后续的处理。该回调函数的参数包括当前异步操作任务的状态和返回值等信息，可以根据这些信息进行相应的处理。

**napi\_threadsafe\_function\_call\_js**

函数指针，在事件循环线程中执行，可与ArkTS/JS交互，从而实现更加复杂的功能，用于napi\_create\_threadsafe\_function(napi\_env env,…,napi\_threadsafe\_function\_call\_js call\_js\_cb,...)接口。

**napi\_cleanup\_hook**

函数指针，用于napi\_add\_env\_cleanup\_hook接口，当环境销毁时会被执行。

**napi\_async\_cleanup\_hook**

函数指针，用于napi\_add\_async\_cleanup\_hook接口，当环境销毁时会被执行。

### 调度优先级

QoS决定了线程调度的优先级，等级定义如下：

```
1. typedef enum {
2. napi_qos_background = 0,
3. napi_qos_utility = 1,
4. napi_qos_default = 2,
5. napi_qos_user_initiated = 3,
6. } napi_qos_t;
```

| QoS等级 | 适用场景 |
| --- | --- |
| napi\_qos\_background | 低等级，用户不可见任务，例如数据同步、备份。 |
| napi\_qos\_utility | 中低等级，不需要立即看到响应效果的任务，例如下载或导入数据。 |
| napi\_qos\_default | 默认。 |
| napi\_qos\_user\_initiated | 高等级，用户触发并且可见进展，例如打开文档。 |

### 事件循环模式

napi提供了运行底层事件循环的两种模式, 其定义如下：

```
1. typedef enum {
2. napi_event_mode_default = 0,
3. napi_event_mode_nowait = 1,
4. } napi_event_mode;
```

| 事件循环运行模式 | 解释说明 |
| --- | --- |
| napi\_event\_mode\_default | 阻塞式的运行底层事件循环，直到循环中没有或活跃的uv\_handle句柄时退出事件循环。 |
| napi\_event\_mode\_nowait | 非阻塞式的运行底层事件循环，尝试去处理一个任务，处理完之后退出事件循环；如果事件循环中没有任务，立刻退出事件循环。 |

### 线程安全任务优先级

napi提供了线程安全任务的优先级, 底层任务队列中的任务会根据其优先级被依次执行, 优先级的定义如下：

```
1. typedef enum {
2. napi_priority_immediate = 0,
3. napi_priority_high = 1,
4. napi_priority_low = 2,
5. napi_priority_idle = 3,
6. } napi_task_priority;
```

| 任务优先级 | 解释说明 |
| --- | --- |
| napi\_priority\_immediate | 该优先级的级别最高。 |
| napi\_priority\_high | 该优先级的级别低于napi\_priority\_immediate。 |
| napi\_priority\_low | 该优先级的级别低于napi\_priority\_immediate和napi\_priority\_high。 |
| napi\_priority\_idle | 该优先级的级别最低。 |

## 支持的Node-API接口

Node-API接口在Node.js提供的原生模块基础上扩展，目前支持部分接口，具体可见下文。

### 异步安全线程相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_threadsafe\_function | 创建线程安全函数。 |
| napi\_get\_threadsafe\_function\_context | 获取线程安全函数中的context。 |
| napi\_call\_threadsafe\_function | 调用线程安全函数。 |
| napi\_acquire\_threadsafe\_function | 指示线程安全函数可以开始使用。 |
| napi\_release\_threadsafe\_function | 指示线程安全函数将停止使用。 |
| napi\_ref\_threadsafe\_function | 指示在主线程上运行的事件循环在线程安全函数被销毁之前不应退出。 |
| napi\_unref\_threadsafe\_function | 指示在主线程上运行的事件循环可能会在线程安全函数被销毁之前退出。 |

### buffer相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_buffer | 创建并获取一个指定大小的ArkTS Buffer。 |
| napi\_create\_buffer\_copy | 创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化。 |
| napi\_create\_external\_buffer | 创建并获取一个指定大小的ArkTS Buffer，使用给定的数据作为buffer对象的底层缓冲区，该接口可为Buffer附带额外数据。 |
| napi\_get\_buffer\_info | 获取JS Buffer底层data及其长度。 |
| napi\_is\_buffer | 判断给定JS value是否为Buffer对象。 |
| napi\_create\_external\_arraybuffer | 分配一个附加有外部数据的JS ArrayBuffer。 |

### string相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_string\_utf16 | 通过UTF16编码的C字符串数据创建ArkTS String。 |
| napi\_get\_value\_string\_utf16 | 获取给定ArkTS value对应的UTF16编码的字符串。 |
| napi\_create\_string\_latin1 | 通过ISO-8859-1编码的C字符串数据创建ArkTS String。 |
| napi\_create\_string\_utf8 | 通过UTF8编码的C字符串数据创建ArkTS String。 |
| napi\_get\_value\_string\_latin1 | 获取给定ArkTS value对应的ISO-8859-1编码的字符串。 |
| napi\_get\_value\_string\_utf8 | 获取给定ArkTS value对应的UTF8编码的字符串。 |
| napi\_create\_external\_string\_utf16 | 通过给定的UTF-16编码的字符串缓冲区来创建ArkTS字符串，该方法能避免字符串的内存拷贝。 |
| napi\_create\_external\_string\_ascii | 通过给定的ASCII编码的字符串缓冲区来创建ArkTS字符串，该方法能避免字符串的内存拷贝。 |

### date相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_date | 通过一个C的double数据创建ArkTS Date。 |
| napi\_get\_date\_value | 获取给定ArkTS Date对应的C double值。 |
| napi\_is\_date | 判断给定ArkTS value是否为ArkTS Date对象。 |

### arraybuffer相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_get\_arraybuffer\_info | 获取ArrayBuffer的底层缓冲区及其长度。 |
| napi\_is\_arraybuffer | 判断给定ArkTS value是否为ArrayBuffer。 |
| napi\_detach\_arraybuffer | 分离给定ArrayBuffer的底层数据。 |
| napi\_is\_detached\_arraybuffer | 判断给定的ArrayBuffer是否已被分离。 |
| napi\_create\_arraybuffer | 创建并获取一个指定大小的JS ArrayBuffer。 |

### module相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_module\_register | native模块注册接口。 |

### 生命周期相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_open\_handle\_scope | 创建一个napi\_handle\_scope。需要使用napi\_close\_handle\_scope进行关闭。 |
| napi\_close\_handle\_scope | 关闭传入的napi\_handle\_scope，关闭后，全部在其中产生的napi\_value都将被关闭。 |
| napi\_open\_escapable\_handle\_scope | 创建出一个可逃逸的handle scope，可将范围内声明的值返回到父作用域。需要使用napi\_close\_escapable\_handle\_scope进行关闭。 |
| napi\_close\_escapable\_handle\_scope | 关闭传入的可逃逸的handle scope。 |
| napi\_escape\_handle | 提升传入的JS Object的生命周期到其父作用域。 |
| napi\_create\_reference | 为Object创建一个napi\_ref。调用者需要自己管理napi\_ref生命周期。 |
| napi\_delete\_reference | 删除传入的napi\_ref。 |
| napi\_reference\_ref | 增加传入的napi\_ref的引用计数，并获取新的计数。 |
| napi\_reference\_unref | 减少传入的napi\_ref的引用计数，并获取新的计数。 |
| napi\_get\_reference\_value | 获取与napi\_ref相关联的JS Object。 |
| napi\_add\_finalizer | 当ArkTS Object中的对象被垃圾回收时调用注册的napi\_finalize回调。 |

### promise相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_promise | 创建一个Promise对象。 |
| napi\_resolve\_deferred | 对Promise关联的deferred对象进行兑现。 |
| napi\_reject\_deferred | 对Promise关联的deferred对象进行拒绝。 |
| napi\_is\_promise | 判断给定napi\_value是否为Promise对象。 |

### array相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_array | 创建一个ArkTS Array。 |
| napi\_create\_array\_with\_length | 创建并获取一个指定长度的ArkTS Array。 |
| napi\_get\_array\_length | 获取array的length。 |
| napi\_is\_array | 判断给定ArkTS value是否为array。 |
| napi\_set\_element | 在给定Object的指定索引处，设置属性值。 |
| napi\_get\_element | 获取给定Object指定索引处的元素。 |
| napi\_has\_element | 若给定Object的指定索引处拥有属性。 |
| napi\_delete\_element | 尝试删除给定Object的指定索引处的元素。 |
| napi\_create\_typedarray | 通过现有的ArrayBuffer创建一个ArkTS TypeArray。 |
| napi\_is\_typedarray | 判断给定ArkTS value是否为TypeArray。 |
| napi\_get\_typedarray\_info | 获取给定TypedArray的各种属性（例如：类型，长度，字节偏移量，ArrayBuffer等）。 |
| napi\_create\_dataview | 通过现有的ArrayBuffer创建一个ArkTS DataView。 |
| napi\_is\_dataview | 判断给定ArkTS value是否为DataView。 |
| napi\_get\_dataview\_info | 获取给定DataView的各种属性。 |

### primitive相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_get\_boolean | 根据给定的C boolean值，获取JS Boolean对象。 |
| napi\_get\_global | 获取global对象。 |
| napi\_get\_null | 获取null对象。 |
| napi\_get\_undefined | 获取undefined对象。 |
| napi\_coerce\_to\_bool | 将给定的JS value强转成JS Boolean。 |
| napi\_coerce\_to\_number | 将给定的JS value强转成JS Number。 |
| napi\_coerce\_to\_object | 将给定的JS value强转成JS Object。 |
| napi\_coerce\_to\_string | 将给定的JS value强转成JS String。 |

### class相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_new\_instance | 通过给定的构造函数，构建一个实例。 |
| napi\_get\_new\_target | 获取构造函数调用的new.target。 |
| napi\_define\_class | 定义与C++类相对应的JavaScript类。 |
| napi\_wrap | 在ArkTS对象上绑定一个Node-API模块对象实例。这个函数通常在将Node-API模块对象与ArkTS对象进行绑定时使用，以便在ArkTS中使用Native方法和属性。 |
| napi\_unwrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例。 |
| napi\_remove\_wrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例，并解除绑定。 |

### object相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_get\_prototype | 获取给定ArkTS Object的prototype。 |
| napi\_create\_object | 创建一个默认的ArkTS Object。 |
| napi\_object\_freeze | 冻结给定的对象。 |
| napi\_object\_seal | 密封给定的对象。 |
| napi\_typeof | 获取给定ArkTS value的ArkTS Type。 |
| napi\_instanceof | 判断给定object是否为给定constructor的实例。 |
| napi\_type\_tag\_object | 将tag指针的值与Object关联。 |
| napi\_check\_object\_type\_tag | 判断给定的tag指针是否被关联到了ArkTS Object上。 |
| napi\_create\_symbol | 创建一个ArkTS Symbol对象。 |
| napi\_create\_external | 用于创建一个ArkTS外部对象，该对象可以用于将C/C++中的自定义数据结构或对象传递到JS中，并且可以在ArkTS中访问其属性和方法。 |
| napi\_get\_value\_external | 用于获得napi\_create\_external创建的绑定了外部数据的ArkTS值，此函数可以在ArkTS和C/C++之间传递数据。 |

### 基本数据类型相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_int32 | 通过一个C的int32数据创建JS number。 |
| napi\_create\_uint32 | 通过一个C的uint32数据创建JS number。 |
| napi\_create\_int64 | 通过一个C的int64数据创建JS number。 |
| napi\_create\_double | 通过一个C的double数据创建JS number。 |
| napi\_get\_value\_int32 | 获取给定JS number对应的C int32值。 |
| napi\_get\_value\_uint32 | 获取给定JS number对应的C uint32值。 |
| napi\_get\_value\_int64 | 获取给定JS number对应的C int64值。 |
| napi\_get\_value\_double | 获取给定JS number对应的C double值。 |
| napi\_get\_value\_bool | 获取给定js Boolean对应的C bool值。 |

### bigint相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_bigint\_int64 | 通过一个C的int64数据创建JS BigInt。 |
| napi\_create\_bigint\_uint64 | 通过一个C的uint64数据创建JS BigInt。 |
| napi\_create\_bigint\_words | 通过一个C的uint64数组创建单个JS BigInt。 |
| napi\_get\_value\_bigint\_int64 | 获取给定JS BigInt对应的C int64值。 |
| napi\_get\_value\_bigint\_uint64 | 获取给定JS BigInt对应的C uint64值。 |
| napi\_get\_value\_bigint\_words | 获取给定JS BigInt对应的信息，包括符号位、64位小端序数组和数组中的元素个数。 |

### 异常和错误相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_throw | 抛出一个JS value。 |
| napi\_throw\_error | 用于抛出一个带文本信息的ArkTS Error。 |
| napi\_throw\_type\_error | 抛出一个带文本信息的ArkTS TypeError。 |
| napi\_throw\_range\_error | 抛出一个带文本信息的ArkTS RangeError。 |
| napi\_is\_error | 判断napi\_value是否表示为一个error对象。 |
| napi\_create\_error | 创建并获取一个带文本信息的ArkTS Error。 |
| napi\_create\_type\_error | 创建并获取一个带文本信息的ArkTS Error对象 |
| napi\_create\_range\_error | 创建并获取一个带文本信息的ArkTS Error对象。 |
| napi\_get\_and\_clear\_last\_exception | 获取并清除最近一次出现的异常。 |
| napi\_is\_exception\_pending | 判断是否出现了异常。 |
| napi\_fatal\_error | 引发致命错误以立即终止进程。 |
| napi\_get\_last\_error\_info | 获取napi\_extended\_error\_info结构体，其中包含最近一次出现的error信息。 |
| napi\_fatal\_exception | 抛出一个致命异常并终止进程, 同时产生相应的crash日志。 |

### 属性相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_get\_property\_names | 以字符串数组的形式获取对象的可枚举属性的名称。 |
| napi\_set\_property | 对给定Object设置属性。 |
| napi\_get\_property | 获取给定Object的给定属性。 |
| napi\_has\_property | 判断给定对象中是否存在给定属性。 |
| napi\_delete\_property | 尝试从给定Object中删除给定key属性。 |
| napi\_has\_own\_property | 判断给定Object中是否有名为key的own property。 |
| napi\_set\_named\_property | 对给定Object设置一个给定名称的属性。 |
| napi\_get\_named\_property | 获取给定Object中指定名称的属性。 |
| napi\_has\_named\_property | 判断给定Object中是否有给定名称的属性。 |
| napi\_define\_properties | 批量的向给定Object中定义属性。 |
| napi\_get\_all\_property\_names | 获取一个数组，其中包含此对象过滤后的属性名称。 |

### 异步任务相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_create\_async\_work | 创建一个异步工作对象。 |
| napi\_delete\_async\_work | 释放先前创建的异步工作对象。 |
| napi\_queue\_async\_work | 将异步工作对象加到队列，由底层去调度执行。 |
| napi\_cancel\_async\_work | 取消入队的异步任务。 |

### 自定义异步操作

| 接口 | 功能说明 |
| --- | --- |
| napi\_async\_init | 创建一个异步资源上下文环境（不支持与async\_hook相关能力）。 |
| napi\_make\_callback | 在异步资源上下文环境中回调JS函数（不支持与async\_hook相关能力）。 |
| napi\_async\_destroy | 销毁先前创建的异步资源上下文环境（不支持与async\_hook相关能力）。 |
| napi\_open\_callback\_scope | 创建一个回调作用域（不支持与async\_hook相关能力）。 |
| napi\_close\_callback\_scope | 关闭先前创建的回调作用域（不支持与async\_hook相关能力）。 |

### uv相关

| 接口 | 功能说明 |
| --- | --- |
| napi\_get\_uv\_event\_loop | 获取当前libuv loop实例。 |

### 函数调用

| 接口 | 功能说明 |
| --- | --- |
| napi\_call\_function | 在C/C++侧调用JS方法。 |
| napi\_get\_cb\_info | 从给定的callback info中获取有关调用的详细信息，如参数和this指针。 |

### 环境生命周期

| 接口 | 功能说明 |
| --- | --- |
| napi\_set\_instance\_data | 绑定与当前运行的环境相关联的数据项。 |
| napi\_get\_instance\_data | 检索与当前运行的环境相关联的数据项。 |

### 对象生命周期管理

| 接口 | 功能说明 |
| --- | --- |
| napi\_add\_env\_cleanup\_hook | 注册环境清理钩子函数。 |
| napi\_remove\_env\_cleanup\_hook | 取消环境清理钩子函数。 |
| napi\_add\_async\_cleanup\_hook | 注册清理异步钩子函数。 |
| napi\_remove\_async\_cleanup\_hook | 取消清理异步钩子函数。 |

### 扩展能力

[Node-API组件扩展的符号列表](../harmonyos-references/napi.md#node-api组件扩展的符号列表)

| 接口 | 功能说明 |
| --- | --- |
| napi\_queue\_async\_work\_with\_qos | 将异步工作对象加到队列，由底层根据传入的qos优先级去调度执行。 |
| napi\_run\_script\_path | 运行指定的abc文件。 |
| napi\_load\_module | 将abc文件作为模块加载，返回模块的命名空间。 |
| napi\_load\_module\_with\_info | 将abc文件作为模块加载，返回模块的命名空间，可在ArkTS基础运行时环境中使用。 |
| napi\_create\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建js Object。descriptor的键名必须为string，且不可转为number。 |
| napi\_create\_object\_with\_named\_properties | 使用给定的napi\_value和键名创建js Object。键名必须为string，且不可转为number。 |
| napi\_coerce\_to\_native\_binding\_object | 强制将js Object和Native对象绑定。 |
| napi\_create\_ark\_runtime | 创建基础运行时环境。 |
| napi\_destroy\_ark\_runtime | 销毁基础运行时环境。 |
| napi\_run\_event\_loop | 启动底层的事件循环。 |
| napi\_stop\_event\_loop | 停止底层的事件循环。 |
| napi\_serialize | 将ArkTS对象序列化为native数据。 |
| napi\_deserialize | 将native数据反序列化为ArkTS对象。 |
| napi\_delete\_serialization\_data | 删除序列化数据。 |
| napi\_call\_threadsafe\_function\_with\_priority | 按照指定的优先级和入队策略，将任务投递到ArkTS主线程中。 |
| napi\_is\_sendable | 判断给定的JS value是否是Sendable的。 |
| napi\_define\_sendable\_class | 创建一个Sendable类。 |
| napi\_create\_sendable\_object\_with\_properties | 使用给定的napi\_property\_descriptor创建一个Sendable对象。 |
| napi\_create\_sendable\_array | 创建一个Sendable数组。 |
| napi\_create\_sendable\_array\_with\_length | 创建一个指定长度的Sendable数组。 |
| napi\_create\_sendable\_arraybuffer | 创建一个Sendable ArrayBuffer。 |
| napi\_create\_sendable\_typedarray | 创建一个Sendable TypedArray。 |
| napi\_wrap\_sendable | 包裹一个native实例到ArkTS对象中。 |
| napi\_wrap\_sendable\_with\_size | 包裹一个native实例到ArkTS对象中并指定大小。 |
| napi\_unwrap\_sendable | 获取ArkTS对象包裹的native实例。 |
| napi\_remove\_wrap\_sendable | 移除并获取ArkTS对象包裹的native实例，移除后回调将不再触发，需手动delete释放内存。 |
| napi\_wrap\_enhance | 在ArkTS对象上绑定一个native对象实例并指定实例大小，运行时会统计传入的实例大小并将其累加，当累计大小达到GC触发阈值时，运行时会启动垃圾回收流程。开发者可以指定绑定的回调函数是否异步执行，如果是异步执行，回调函数必须保证是线程安全的。 |
| napi\_create\_ark\_context | 创建一个新的上下文环境。 |
| napi\_switch\_ark\_context | 切换到指定的运行时上下文环境。 |
| napi\_destroy\_ark\_context | 销毁通过napi\_create\_ark\_context创建的上下文环境。 |
| napi\_open\_critical\_scope | 打开临界区作用域。 |
| napi\_close\_critical\_scope | 关闭临界区作用域。 |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取ArkTS String的UTF-16编码内存缓冲区数据。 |
| napi\_create\_strong\_reference | 创建指向ArkTS对象的强引用。 |
| napi\_delete\_strong\_reference | 删除强引用。 |
| napi\_get\_strong\_reference\_value | 根据强引用对象获取其关联的ArkTS对象值。 |
| napi\_create\_strong\_sendable\_reference | 创建指向Sendable ArkTS对象的Sendable强引用。 |
| napi\_delete\_strong\_sendable\_reference | 删除Sendable强引用。 |
| napi\_get\_strong\_sendable\_reference\_value | 根据Sendable强引用获取其关联的ArkTS对象值。 |
| napi\_throw\_business\_error | 抛出一个带文本信息的ArkTS Error, 其错误对象的code属性类型为number。 |

**napi\_queue\_async\_work\_with\_qos**

```
1. napi_status napi_queue_async_work_with_qos(napi_env env,
2. napi_async_work work,
3. napi_qos_t qos);
```

用法同napi\_queue\_async\_work，但可以指定QoS等级。napi\_queue\_async\_work\_with\_qos使用方法可参考指定异步任务调度优先级。QoS详细介绍可参考[QoS 开发指导](qos-guidelines.md)。

**napi\_run\_script\_path**

```
1. napi_status napi_run_script_path(napi_env env,
2. const char* abcPath,
3. napi_value* result);
```

\*\*注：\*\*使用限制说明文档：[使用napi\_run\_script\_path接口执行包内abc文件的使用限制](../harmonyos-faqs/faqs-ndk-65.md)

**napi\_load\_module**

```
1. napi_status napi_load_module(napi_env env,
2. const char* path,
3. napi_value* result);
```

**napi\_create\_object\_with\_properties**

```
1. napi_status napi_create_object_with_properties(napi_env env,
2. napi_value* result,
3. size_t property_count,
4. const napi_property_descriptor* properties);
```

**napi\_create\_object\_with\_named\_properties**

```
1. napi_status napi_create_object_with_named_properties(napi_env env,
2. napi_value* result,
3. size_t property_count,
4. const char** keys,
5. const napi_value* values);
```

**napi\_coerce\_to\_native\_binding\_object**

```
1. napi_status napi_coerce_to_native_binding_object(napi_env env,
2. napi_value js_object,
3. napi_native_binding_detach_callback detach_cb,
4. napi_native_binding_attach_callback attach_cb,
5. void* native_object,
6. void* hint);
```

**napi\_create\_ark\_runtime**

```
1. napi_status napi_create_ark_runtime(napi_env *env);
```

[使用napi\_create\_ark\_runtime、napi\_destroy\_ark\_runtime接口创建ArkTS运行时环境](use-napi-ark-runtime.md)。

**napi\_destroy\_ark\_runtime**

```
1. napi_status napi_destroy_ark_runtime(napi_env *env);
```

**napi\_run\_event\_loop**

```
1. napi_status napi_run_event_loop(napi_env env, napi_event_mode mode);
```

开发者只能在自己通过napi\_create\_ark\_runtime创建的ArkTS运行环境中调用napi\_run\_event\_loop与napi\_stop\_event\_loop接口，使用方法可参考[使用扩展的Node-API接口在异步线程中运行和停止事件循环](use-napi-event-loop.md)。

**napi\_stop\_event\_loop**

```
1. napi_status napi_stop_event_loop(napi_env env);
```

**napi\_serialize**

```
1. napi_status napi_serialize(napi_env env,
2. napi_value object,
3. napi_value transfer_list,
4. napi_value clone_list,
5. void** result);
```

**napi\_deserialize**

```
1. napi_status napi_deserialize(napi_env env, void* buffer, napi_value* object);
```

**napi\_delete\_serialization\_data**

```
1. napi_status napi_delete_serialization_data(napi_env env, void* buffer);
```

**napi\_call\_threadsafe\_function\_with\_priority**

```
1. napi_status napi_call_threadsafe_function_with_priority(napi_threadsafe_function func,
2. void *data,
3. napi_task_priority priority,
4. bool isTail);
```

**napi\_is\_sendable**

```
1. napi_status napi_is_sendable(napi_env env, napi_value value, bool* result);
```

**napi\_define\_sendable\_class**

```
1. napi_status napi_define_sendable_class(napi_env env,
2. const char* utf8name,
3. size_t length,
4. napi_callback constructor,
5. void* data,
6. size_t property_count,
7. const napi_property_descriptor* properties,
8. napi_value parent,
9. napi_value* result);
```

**napi\_create\_sendable\_object\_with\_properties**

```
1. napi_status napi_create_sendable_object_with_properties(napi_env env,
2. size_t property_count,
3. const napi_property_descriptor* properties,
4. napi_value* result);
```

**napi\_create\_sendable\_array**

```
1. napi_status napi_create_sendable_array(napi_env env, napi_value* result);
```

**napi\_create\_sendable\_array\_with\_length**

```
1. napi_status napi_create_sendable_array_with_length(napi_env env, size_t length, napi_value* result);
```

**napi\_create\_sendable\_arraybuffer**

```
1. napi_status napi_create_sendable_arraybuffer(napi_env env, size_t byte_length, void** data, napi_value* result);
```

**napi\_create\_sendable\_typedarray**

```
1. napi_status napi_create_sendable_typedarray(napi_env env,
2. napi_typedarray_type type,
3. size_t length,
4. napi_value arraybuffer,
5. size_t byte_offset,
6. napi_value* result);
```

**napi\_wrap\_sendable**

```
1. napi_status napi_wrap_sendable(napi_env env,
2. napi_value js_object,
3. void* native_object,
4. napi_finalize finalize_cb,
5. void* finalize_hint);
```

**napi\_wrap\_sendable\_with\_size**

```
1. napi_status napi_wrap_sendable_with_size(napi_env env,
2. napi_value js_object,
3. void* native_object,
4. napi_finalize finalize_cb,
5. void* finalize_hint,
6. size_t native_binding_size);
```

**napi\_unwrap\_sendable**

```
1. napi_status napi_unwrap_sendable(napi_env env, napi_value js_object, void** result);
```

**napi\_remove\_wrap\_sendable**

```
1. napi_status napi_remove_wrap_sendable(napi_env env, napi_value js_object, void** result);
```

**napi\_wrap\_enhance**

```
1. napi_status napi_wrap_enhance(napi_env env,
2. napi_value js_object,
3. void* native_object,
4. napi_finalize finalize_cb,
5. bool async_finalizer,
6. void* finalize_hint,
7. size_t native_binding_size,
8. napi_ref* result);
```

**napi\_create\_ark\_context**

```
1. napi_status napi_create_ark_context(napi_env env,
2. napi_env* newEnv);
```

**napi\_switch\_ark\_context**

```
1. napi_status napi_switch_ark_context(napi_env env);
```

**napi\_destroy\_ark\_context**

```
1. napi_status napi_destroy_ark_context(napi_env env);
```

**napi\_open\_critical\_scope**

```
1. napi_status napi_open_critical_scope(napi_env env, napi_critical_scope* scope);
```

**napi\_close\_critical\_scope**

```
1. napi_status napi_close_critical_scope(napi_env env, napi_critical_scope scope);
```

**napi\_get\_buffer\_string\_utf16\_in\_critical\_scope**

```
1. napi_status napi_get_buffer_string_utf16_in_critical_scope(napi_env env,
2. napi_value value,
3. const char16_t** buffer,
4. size_t* length);
```

**napi\_create\_strong\_reference**

```
1. napi_status napi_create_strong_reference(napi_env env, napi_value value, napi_strong_ref* result);
```

**napi\_delete\_strong\_reference**

```
1. napi_status napi_delete_strong_reference(napi_env env, napi_strong_ref ref)
```

**napi\_get\_strong\_reference\_value**

```
1. napi_status napi_get_strong_reference_value(napi_env env, napi_strong_ref ref, napi_value* result)
```

**napi\_create\_external\_string\_utf16**

```
1. napi_status napi_create_external_string_utf16(napi_env env,
2. const char16_t* str,
3. size_t length,
4. napi_finalize_callback finalize_callback,
5. void* finalize_hint,
6. napi_value* result);
```

**napi\_create\_external\_string\_ascii**

```
1. napi_status napi_create_external_string_ascii(napi_env env,
2. const char* str,
3. size_t length,
4. napi_finalize_callback finalize_callback,
5. void* finalize_hint,
6. napi_value* result);
```

**napi\_create\_strong\_sendable\_reference**

```
1. napi_status napi_create_strong_sendable_reference(napi_env env,
2. napi_value value,
3. napi_sendable_ref* result);
```

**napi\_delete\_strong\_sendable\_reference**

```
1. napi_status napi_delete_strong_sendable_reference(napi_env env, napi_sendable_ref ref);
```

**napi\_get\_strong\_sendable\_reference\_value**

```
1. napi_status napi_get_strong_sendable_reference_value(napi_env env,
2. napi_sendable_ref ref,
3. napi_value* result);
```

**napi\_throw\_business\_error**

```
1. napi_status napi_throw_business_error(napi_env env,
2. int32_t errorCode,
3. const char* msg);
```

### 其他实用工具

| 接口 | 功能说明 |
| --- | --- |
| napi\_get\_version | 获取Node运行时支持的最高 NAPI 版本。 |
| node\_api\_get\_module\_file\_name | 用于获取加载项加载位置的绝对路径。 |
| napi\_strict\_equals | 当需要确保两个值不仅值相等且类型也相同时（例如处理特定类型的数据结构或算法时），可以使用napi\_strict\_equals来保证数据一致性。 |
