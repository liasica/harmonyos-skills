---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/libuv
title: libuv
breadcrumb: API参考 > 标准库 > libuv
category: harmonyos-references
scraped_at: 2026-04-29T14:10:06+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:752319525de92c411ab92c0193972a24d25e814bebc9a457c64e8c9de9a46b87
---

## 简介

[libuv](http://libuv.org/)是一个跨平台库，基于事件驱动来实现异步I/O，适用于网络编程和文件系统操作。它是Node.js的核心库之一，也被其他语言的开发者广泛使用。

## 支持的能力

[libuv](http://libuv.org/)实现了跨平台的基于事件驱动的异步I/O。

支持标准库接口。

## 引入libuv能力

如果开发者需要使用libuv相关功能，首先请添加头文件：

```
1. #include <uv.h>
```

其次在CMakeLists.txt中添加以下动态链接库：

```
1. libuv.so
```

## 接口列表

详见[libuv支持的API文档](http://docs.libuv.org/en/v1.x/api.html)。

## HarmonyOS引入libuv的背景

在HarmonyOS的早期版本中，为了兼容Node.js的生态，将Node.js的Node-API引入到系统中，方便Node.js开发者快速接入HarmonyOS，扩展自己的JS接口。同时引入了Node.js的事件循环实现库——libuv。

### 演进方向

随着HarmonyOS的逐步完善，我们计划在未来的版本中，逐步将应用模型中的事件循环归一，并增强HarmonyOS自身的事件循环，以解决许多双loop机制下的调度问题，并为开发者提供更加完善的任务优先级、插队等与任务主循环交互的方法。

开发者应尽可能避免在napi\_get\_uv\_event\_loop接口获取的应用主loop上使用libuv的ndk进行操作，因为这可能会带来各种问题，并给未来的兼容性变更带来大量的工作量。

如果开发者希望跟主线程事件循环交互，比如插入任务等，应当使用[Node-API提供的接口](../harmonyos-guides/napi-data-types-interfaces.md)。

HarmonyOS还将长期通过Node-API来为开发者提供和主线程交互及扩展JS接口的能力，但会屏蔽实现层使用的事件循环。Node-API的主要功能接口将会长期维护，并保证与Node.js的原生行为一致，来保证熟悉Node.js的扩展机制的开发者方便地将自己的已有代码接入到HarmonyOS中来。

如果开发者对libuv非常熟悉，并自信能够处理好所有的内存管理和多线程问题，那么仍可以像使用原生libuv一样，自己启动线程，并在上面使用libuv完成自己的业务。在没有特殊版本要求的情况下，开发者不需要额外引入libuv库到自己的应用工程中。

## 当前问题和解决方案

根据现有机制，一个线程上只能存在一个事件循环，为了适配系统应用的主事件循环，在主线程上的JS环境中，uvloop中的事件处理是由主事件循环监听其fd，触发一次uv\_run来驱动的。因此部分依赖uvloop事件循环的功能无法生效。

基于上述，比较常用的场景和解决方案有：

### 场景一、在JS主线程抛异步任务到工作线程执行，在主线程中执行JS代码处理返回结果

**错误示例：**

在Native侧直接通过调用napi\_get\_uv\_event\_loop接口获取系统loop，调用libuv NDK接口实现相关功能。

ArkTS侧:

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("test")
11. .width('40%')
12. .fontSize('14fp')
13. .onClick(() => {
14. testNapi.test();
15. }).margin(20)
16. }.width('100%')
17. }.height('100%')
18. }
19. }
```

Native侧:

```
1. #include "napi/native_api.h"
2. #include "uv.h"
3. #define LOG_DOMAIN 0X0202
4. #define LOG_TAG "MyTag"
5. #include <hilog/log.h>

7. static void execute(uv_work_t* work)
8. {
9. OH_LOG_INFO(LOG_APP, "ohos in execute");
10. }

12. static void complete(uv_work_t* work, int status)
13. {
14. OH_LOG_INFO(LOG_APP, "ohos in complete");
15. delete work;
16. }
17. static napi_value Test(napi_env env, napi_callback_info info)
18. {
19. uv_loop_s* loop = nullptr;
20. /* 获取应用JS主线程的uv_loop */
21. napi_get_uv_event_loop(env, &loop);
22. uv_work_t* work = new uv_work_t;
23. int ret = uv_queue_work(loop, work, execute, complete);
24. if (ret != 0) {
25. OH_LOG_INFO(LOG_APP, "delete work");
26. delete work;
27. }
28. return 0;
29. }

31. EXTERN_C_START
32. static napi_value Init(napi_env env, napi_value exports)
33. {
34. napi_property_descriptor desc[] = {{"test", nullptr, Test, nullptr, nullptr, nullptr, napi_default, nullptr}};
35. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
36. return exports;
37. }
38. EXTERN_C_END

40. static napi_module demoModule = {
41. .nm_version = 1,
42. .nm_flags = 0,
43. .nm_filename = nullptr,
44. .nm_register_func = Init,
45. .nm_modname = "entry",
46. .nm_priv = ((void *)0),
47. .reserved = {0},
48. };

50. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
51. {
52. napi_module_register(&demoModule);
53. }
```

在index.d.ts文件中添加如下代码：

```
1. export const test:() => number;
```

在CMakeLists.txt中添加以下动态链接库：

```
1. libhilog_ndk.z.so
```

**正确示例：**

可通过napi\_create\_async\_work、napi\_queue\_async\_work搭配使用。

ArkTS侧:

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("test")
11. .width('40%')
12. .fontSize('14fp')
13. .onClick(() => {
14. testNapi.test();
15. }).margin(20)
16. }.width('100%')
17. }.height('100%')
18. }
19. }
```

Native侧:

```
1. #include "napi/native_api.h"
2. #include "uv.h"
3. #define LOG_DOMAIN 0X0202
4. #define LOG_TAG "MyTag"
5. #include <hilog/log.h>
6. uv_loop_t* loop = nullptr;
7. napi_value jsCb;
8. int fd = -1;

10. static napi_value Test(napi_env env, napi_callback_info info)
11. {
12. napi_value work_name;
13. napi_async_work work;
14. napi_create_string_utf8(env, "ohos", NAPI_AUTO_LENGTH, &work_name);
15. /* 第四个参数是异步线程的work任务，第五个参数为主线程的回调 */
16. napi_create_async_work(
17. env, nullptr, work_name, [](napi_env env, void* data){OH_LOG_INFO(LOG_APP, "ohos in execute"); },
18. [](napi_env env, napi_status status, void* data){
19. /* 不关心具体实现 */
20. OH_LOG_INFO(LOG_APP, "ohos in complete");
21. napi_delete_async_work(env, (napi_async_work)data);
22. },
23. nullptr, &work);
24. /* 通过napi_queue_async_work触发异步任务执行 */
25. napi_queue_async_work(env, work);
26. return 0;
27. }

29. EXTERN_C_START
30. static napi_value Init(napi_env env, napi_value exports)
31. {
32. napi_property_descriptor desc[] = {{"test", nullptr, Test, nullptr, nullptr, nullptr, napi_default, nullptr}};
33. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
34. return exports;
35. }
36. EXTERN_C_END

38. static napi_module demoModule = {
39. .nm_version = 1,
40. .nm_flags = 0,
41. .nm_filename = nullptr,
42. .nm_register_func = Init,
43. .nm_modname = "entry",
44. .nm_priv = ((void *)0),
45. .reserved = {0},
46. };

48. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
49. {
50. napi_module_register(&demoModule);
51. }
```

在index.d.ts文件中添加如下代码：

```
1. export const test:() => number;
```

在CMakeLists.txt中添加以下动态链接库：

```
1. libhilog_ndk.z.so
```

### 场景二、在Native侧向应用主循环抛fd事件，接口无法生效

由于应用主循环仅仅接收fd事件，在监听了uvloop中的backend\_fd后，只有该fd事件被触发才会执行一次uv\_run。这就意味着，在应用主循环中调用uv接口，如果不触发一次fd事件，uv\_run将永远不会被执行，最后导致libuv的接口正常调用时不生效（仅当应用中没有触发uvloop中的fd事件时）。

**错误示例：**

我们以uv\_poll\_start接口举例，来说明在HarmonyOS中，我们像使用原生libuv一样调用uv\_poll\_start接口时无法生效的问题。

ArkTS侧:

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("testClose")
11. .width('40%')
12. .fontSize('14fp')
13. .onClick(() => {
14. testNapi.testClose();
15. }).margin(20)
16. }.width('100%')
17. }.height('100%')
18. }
19. }
```

Native侧:

```
1. #include "napi/native_api.h"
2. #include "uv.h"
3. #define LOG_DOMAIN 0X0202
4. #define LOG_TAG "MyTag"
5. #include <hilog/log.h>
6. #include <thread>
7. #include <sys/eventfd.h>

9. uv_loop_t* loop = nullptr;
10. napi_value jsCb;
11. int fd = -1;

13. void poll_handler(uv_poll_t* handle,int status, int events)
14. {
15. OH_LOG_INFO(LOG_APP, "ohos poll print");
16. }

18. static napi_value TestClose(napi_env env, napi_callback_info info)
19. {
20. std::thread::id this_id = std::this_thread::get_id();
21. OH_LOG_INFO(LOG_APP, "ohos thread id : %{public}ld", this_id);
22. size_t argc = 1;
23. napi_value workBname;

25. napi_create_string_utf8(env, "test", NAPI_AUTO_LENGTH, &workBname);

27. napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);
28. // 获取事件循环
29. napi_get_uv_event_loop(env, &loop);
30. // 创建一个eventfd
31. fd = eventfd(0, 0);
32. OH_LOG_INFO(LOG_APP, "fd is %{public}d",fd);
33. uv_poll_t* poll_handle = new uv_poll_t;
34. // 初始化一个poll句柄，并将其与eventfd关联
35. uv_poll_init(loop, poll_handle, fd);
36. // 开始监听poll事件
37. uv_poll_start(poll_handle, UV_READABLE, poll_handler);
38. // 创建一个新线程，向eventfd写入数据
39. std::thread mythread([](){
40. for (int i = 0; i < 8; i++){
41. int value = 10;
42. int ret = eventfd_write(fd, value);
43. if (ret == -1){
44. OH_LOG_INFO(LOG_APP, "write failed!");
45. continue;
46. }
47. }
48. });
49. mythread.detach();
50. return 0;
51. }

53. EXTERN_C_START
54. static napi_value Init(napi_env env, napi_value exports)
55. {
56. napi_property_descriptor desc[] = {{"testClose", nullptr, TestClose, nullptr, nullptr, nullptr, napi_default, nullptr}};
57. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
58. return exports;
59. }
60. EXTERN_C_END

62. static napi_module demoModule = {
63. .nm_version = 1,
64. .nm_flags = 0,
65. .nm_filename = nullptr,
66. .nm_register_func = Init,
67. .nm_modname = "entry",
68. .nm_priv = ((void *)0),
69. .reserved = {0},
70. };

72. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
73. {
74. napi_module_register(&demoModule);
75. }
```

在index.d.ts添加如下代码：

```
1. export const testClose:() => number;
```

在CMakeLists.txt中添加以下动态链接库：

```
1. libhilog_ndk.z.so
```

在上述代码中，流程如下：

1. 首先通过napi\_get\_uv\_event\_loop接口获取到应用主线程的uvloop。
2. 然后创建一个eventfd。
3. 初始化uv\_poll\_t，并启动该句柄使其生效，在eventfd可读时触发回调函数poll\_handler。
4. 新开一个线程，向eventfd里写入字符。

执行上述代码，poll\_handler并不能正常打印。这是由于应用主线程是靠fd驱动来执行uv\_run的，而非以UV\_RUN\_DEFAULT模式来进行循环。尽管uvloop中的backend\_fd已经被event\_handler监听，但是当执行uv\_poll\_start的时候，fd并未通过epoll\_ctl加入到backend\_fd中被其监听，**而是在下一次uv\_run中的uv\_\_io\_poll这个函数才会执行epoll\_ctl函数。因此，如果应用进程中没有其他触发backend\_fd事件的时候，libuv接口的正常使用可能不会达到开发者的预期。**

**临时方案：**

在当下的系统版本中，我们并不推荐开发者直接通过napi\_get\_uv\_event\_loop获取应用主线程的uvloop进行业务逻辑的开发。如果当前Node-API的接口无法满足开发者的开发需求，确有必要使用libuv来实现业务功能，为了使libuv接口在主线程上生效，开发者可以在调用类似uv\_xxx\_start后，执行一次uv\_async\_send的方式来主动触发应用主线程执行一次uv\_run。这样可以保证该接口生效并正常执行。

针对上述无法生效的代码示例，可以修改如下使其生效。

ArkTS侧:

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("testClose")
11. .width('40%')
12. .fontSize('14fp')
13. .onClick(() => {
14. testNapi.testClose();
15. }).margin(20)
16. }.width('100%')
17. }.height('100%')
18. }
19. }
```

Native侧:

```
1. #include "napi/native_api.h"
2. #include "uv.h"
3. #define LOG_DOMAIN 0x0202
4. #define LOG_TAG "MyTag"
5. #include <hilog/log.h>
6. #include <thread>
7. #include <sys/eventfd.h>

9. uv_loop_t* loop = nullptr;
10. napi_value jsCb;
11. int fd = -1;

13. void poll_handler(uv_poll_t* handle,int status, int events)
14. {
15. OH_LOG_INFO(LOG_APP, "ohos poll print");
16. }

18. static napi_value TestClose(napi_env env, napi_callback_info info)
19. {
20. std::thread::id this_id = std::this_thread::get_id();
21. OH_LOG_INFO(LOG_APP, "ohos thread id : %{public}ld", this_id);
22. size_t argc = 1;
23. napi_value workBName;

25. napi_create_string_utf8(env, "test", NAPI_AUTO_LENGTH, &workBName);

27. napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);

29. napi_get_uv_event_loop(env, &loop);

31. fd = eventfd(0, 0);
32. OH_LOG_INFO(LOG_APP, "fd is %{public}d",fd);
33. uv_poll_t* poll_handle = new uv_poll_t;
34. uv_poll_init(loop, poll_handle, fd);
35. uv_poll_start(poll_handle, UV_READABLE, poll_handler);

37. // 主动触发一次fd事件，让主线程执行一次uv_run
38. uv_async_send(&loop->wq_async);

40. std::thread mythread([](){
41. for (int i = 0; i < 8; i++){
42. int value = 10;
43. int ret = eventfd_write(fd, value);
44. if (ret == -1){
45. OH_LOG_INFO(LOG_APP, "write failed!");
46. continue;
47. }
48. }
49. });
50. mythread.detach();
51. return 0;
52. }

54. EXTERN_C_START
55. static napi_value Init(napi_env env, napi_value exports)
56. {
57. napi_property_descriptor desc[] = {{"testClose", nullptr, TestClose, nullptr, nullptr, nullptr, napi_default, nullptr}};
58. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
59. return exports;
60. }
61. EXTERN_C_END

63. static napi_module demoModule = {
64. .nm_version = 1,
65. .nm_flags = 0,
66. .nm_filename = nullptr,
67. .nm_register_func = Init,
68. .nm_modname = "entry",
69. .nm_priv = ((void *)0),
70. .reserved = {0},
71. };

73. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
74. {
75. napi_module_register(&demoModule);
76. }
```

在index.d.ts添加如下代码：

```
1. export const testClose:() => number;
```

在CMakeLists.txt中添加以下动态链接库：

```
1. libhilog_ndk.z.so
```

## libuv使用指导

**重要：libuv NDK中所有依赖uv\_run的接口在当前系统的应用主循环中无法及时生效，并且可能会导致卡顿掉帧的现象。因此不建议直接在JS主线程上使用libuv NDK接口，对于异步任务执行及与使用线程安全函数与主线程通信，开发者可以直接调用Node-API接口来实现相关功能。**

### libuv接口与Node-API接口对应关系

当前HarmonyOS提供了一些Node-API接口，可以替换libuv接口的使用。主要包括异步任务相关接口，线程安全的函数调用接口。

**1. 异步任务接口**

当开发者需要执行一个比较耗时的操作但又不希望阻塞主线程执行时，libuv提供了底层接口uv\_queue\_work帮助开发者在异步线程中执行耗时操作，然后将结果回调到主线程上进行处理。

在Node-API中，通常可以通过[napi\_async\_work](../harmonyos-guides/use-napi-asynchronous-task.md)相关函数来实现异步开发的功能。

相关函数为：

```
1. /**
2. * @brief 创建一个新的异步工作
3. *
4. * @param env 指向当前环境的指针
5. * @param async_resource 可选的资源对象，用于跟踪异步操作
6. * @param async_resource_name 可选的字符串，用于描述异步资源
7. * @param execute 一个回调函数，它将在一个新的线程中执行异步操作
8. * @param complete 一个回调函数，它将在异步操作完成后被调用
9. * @param data 用户定义的数据，它将被传递给execute和complete回调函数
10. * @param result 指向新创建的异步工作的指针
11. */
12. napi_status napi_create_async_work(napi_env env,
13. napi_value async_resource,
14. napi_value async_resource_name,
15. napi_async_execute_callback execute,
16. napi_async_complete_callback complete,
17. void* data,
18. napi_async_work* result);

20. /**
21. * @brief 将异步工作添加到队列中
22. *
23. * @param env 指向当前环境的指针
24. * @param work 指向异步工作的指针
25. */
26. napi_status napi_queue_async_work(napi_env env, napi_async_work work);

28. /**
29. * @brief 删除异步工作
30. *
31. * @param env 指向当前环境的指针
32. * @param work 指向异步工作的指针
33. */
34. napi_status napi_delete_async_work(napi_env env, napi_async_work work);
```

**2. 跨线程共享和调用的线程安全函数**

当开发者想在任意子线程传递某个回调函数到应用主线程上执行时，libuv的实现方式一般使用uv\_async\_t句柄用于线程间通信。

相关函数包含：

* uv\_async\_init()
* uv\_async\_send()

Node-API与之对应的接口为[napi\_threadsafe\_function](../harmonyos-guides/use-napi-thread-safety.md)相关函数。

相关函数：

```
1. /**
2. * @brief 用于创建一个线程安全的函数，该函数可以在多个线程中调用，而不需要担心数据竞争或其他线程安全问题
3. *
4. * @param env 指向NAPI环境的指针，用于创建和操作Javascript值
5. * @param func 指向JavaScript函数的指针
6. * @param async_resource 异步资源，通常是一个表示异步操作的对象
7. * @param async_resource_name 指向资源名称的指针，这个名称将用于日志和调试
8. * @param max_queue_size 一个整数，表示队列的最大大小，当队列满时，新的调用将被丢弃
9. * @param initial_thread_count 无符号整数，表示在创建线程安全函数时，初始的线程数量
10. * @param thread_finalize_data 一个指向在所有线程之前需要清理的数据
11. * @param napi_finalize thread_finalize_cb 回调函数，当所有线程完成时被调用，用于清理资源
12. * @param context 指向上下文的指针，这个上下文将被传递给call_js_func函数
13. * @param call_js_cb 指向回调函数的指针，这个函数将在Javascript函数被调用时被调用
14. * @param result 指向napi_threadsafe_function结构的指针，这个结构将被填充为新创建的线程安全函数
15. */
16. napi_status napi_create_threadsafe_function(napi_env env,
17. napi_value func,
18. napi_value async_resource,
19. napi_value async_resource_name,
20. size_t max_queue_size,
21. size_t initial_thread_count,
22. void* thread_finalize_data,
23. napi_finalize thread_finalize_cb,
24. void* context,
25. napi_threadsafe_function_call_js call_js_cb,
26. napi_threadsafe_function* result);

28. /**
29. * @brief 获取一个线程安全的函数
30. *
31. * @param function 指向线程安全函数的指针
32. */
33. napi_status napi_acquire_threadsafe_function(napi_threadsafe_function function);

35. /**
36. * @brief 调用一个线程安全的函数
37. * @param function 指向线程安全函数的指针
38. * @param data 用户数据
39. * @param is_blocking 枚举值，它决定调用JavaScript函数是阻塞的还是非阻塞的
40. */
41. napi_status napi_call_threadsafe_function(napi_threadsafe_function function,
42. void* data,
43. napi_threadsafe_function_call_mode is_blocking);
44. /**
45. * @brief 释放一个线程安全的函数
46. *
47. * @param function 指向线程安全函数的指针
48. * @param is_blocking 枚举值，它决定调用JavaScript函数是阻塞的还是非阻塞的
49. */
50. napi_status napi_release_threadsafe_function(napi_threadsafe_function function,
51. napi_threadsafe_function_call_mode is_blocking);
```

除此之外，如果开发者需要libuv其他原生接口来实现业务功能，为了让开发者正确使用libuv提供的接口能力，避免因为错误使用而陷入到问题当中。在后续章节，我们将逐步介绍libuv的一些基本概念和HarmonyOS系统中常用函数的正确使用方法，它仅仅可以保证开发者使用libuv接口的时候不会出现应用进程崩溃等现象。另外，我们还统计了在当前应用主线程上可以正常使用的接口，以及无法在应用主线程上使用的接口。

### 接口汇总说明

| 接口类型 | 接口汇总 |
| --- | --- |
| [loop概念及相关接口](libuv.md#libuv中的事件循环) | uv\_loop\_init |
| [loop概念及相关接口](libuv.md#libuv中的事件循环) | uv\_loop\_close |
| [loop概念及相关接口](libuv.md#libuv中的事件循环) | uv\_default\_loop |
| [loop概念及相关接口](libuv.md#libuv中的事件循环) | uv\_run |
| [loop概念及相关接口](libuv.md#libuv中的事件循环) | uv\_loop\_alive |
| [loop概念及相关接口](libuv.md#libuv中的事件循环) | uv\_stop |
| [Handle概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_poll\_\* |
| [Handle概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_timer\_\* |
| [Handle概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_async\_\* |
| [Handle概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_signal\_\* |
| [Handle概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_fs\_\* |
| [Request概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_random |
| [Request概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_getaddrinfo |
| [Request概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_getnameinfo |
| [Request概念及相关接口](libuv.md#libuv中的handles和requests) | uv\_queue\_work |
| [线程间通信原理及相关接口](libuv.md#线程间通信) | uv\_async\_init |
| [线程间通信原理及相关接口](libuv.md#线程间通信) | uv\_async\_send |
| [线程池概念及相关接口](libuv.md#线程池) | uv\_queue\_work |

### libuv单线程约束

在HarmonyOS中使用libuv时，**务必注意：使用uv\_loop\_init接口初始化loop的线程和调用uv\_run的线程应保持一致，称为loop线程，并且对uvloop的所有非线程安全操作，均需保证与loop同线程，否则将会有发生crash的风险**。HarmonyOS对libuv的使用有更严格的约束，对于非线程安全的函数，libuv将实现多线程检测机制，检测到多线程问题后输出警告日志。为了确保检测机制的准确性，协助开发者规避uv接口的不规范使用，我们建议在创建事件循环与执行uv\_run始终保持在同一线程。根据loop来源的不同，可分为两种情况，即开发者创建loop和从env获取loop。

**1. 开发者创建loop**

开发者可以通过调用uv\_loop\_new创建loop或者uv\_loop\_init接口初始化loop，loop的生命周期由开发者自行维护。在这种情况下，如前文所述，需要保证uv\_run执行在与创建/初始化loop操作相同的线程上，即loop线程上。此外，其余非线程安全操作，如timer相关操作等，均需要在loop线程上进行。

如果因为业务需要，必须在其他线程往loop线程抛任务，请使用uv\_async\_send函数：即在async句柄初始化时，注册一个回调函数，并在该回调中实现相应的操作，当调用uv\_async\_send时，在主线程上执行该回调函数。

ArkTS侧：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("TestTimerAsync")
11. .width('40%')
12. .fontSize('14fp')
13. .onClick(() => {
14. testNapi.testTimerAsync();  // 初始化async句柄
15. }).margin(20)

17. Button("TestTimerAsyncSend")
18. .width('40%')
19. .fontSize('14fp')
20. .onClick(() => {
21. testNapi.testTimerAsyncSend();  // 子线程调用uv_async_send提交定时器任务
22. }).margin(20)
23. }.width('100%')
24. }.height('100%')
25. }
26. }
```

Native侧：

```
1. #include <napi/native_api.h>
2. #include <uv.h>
3. #define LOG_DOMAIN 0x0202
4. #define LOG_TAG "MyTag"
5. #include "hilog/log.h"
6. #include <thread>

8. uv_async_t* async = new uv_async_t;
9. bool cond1 = false;
10. bool cond2 = false;

12. // 使用技巧：在使用loop时, 需要特别注意uv_stop函数的使用, 开发者需要确保uv_stop前
13. // 通知与loop相关的所有线程的handle都关闭, 参考stop_loop函数的实现
14. int stop_loop(uv_loop_t* loop)
15. {
16. uv_stop(loop);
17. auto const ensure_close = [](uv_handle_t* handle, void*) {
18. if (uv_is_closing(handle)) {
19. return;
20. } else {
21. uv_close(handle, nullptr);
22. }
23. };
24. // 遍历所有句柄, 如果handle处于活跃状态, 调用ensure_close
25. uv_walk(loop, ensure_close, nullptr);
26. // 继续运行uv_run, 直到loop中不存在活跃的句柄和请求为止
27. while(true) {
28. if (uv_run(loop, UV_RUN_DEFAULT) == 0) {
29. break;
30. }
31. }

33. // 最后检查loop状态
34. if (uv_loop_alive(loop) != 0) {
35. return -1;
36. }
37. return 0;
38. }

40. // 执行创建定时器操作
41. void async_cb(uv_async_t* handle) {
42. auto loop = handle->loop;
43. uv_timer_t* timer = new uv_timer_t;
44. uv_timer_init(loop, timer);

46. // 在适当的时机关闭async句柄
47. if (cond2) {
48. uv_close((uv_handle_t*)handle, [](uv_handle_t* handle){
49. delete (uv_async_t*)handle;
50. });
51. return;
52. }

54. uv_timer_start(timer,
55. [](uv_timer_t* timer){
56. // do something
57. // 在适当的时机停掉timer
58. if (cond1) {
59. uv_timer_stop(timer);
60. uv_close((uv_handle_t*)timer, [](uv_handle_t* handle){
61. delete(uv_timer_t*)handle;
62. });
63. }
64. },
65. 100, 100);
66. }

68. // 初始化async句柄, 绑定对应的回调函数
69. static napi_value TestTimerAsync(napi_env env, napi_callback_info info) {
70. std::thread t([](){  // A线程，loop线程
71. uv_loop_t* loop = new uv_loop_t;
72. // 开发者自己创建loop, 请注意维护loop的生命周期
73. uv_loop_init(loop);
74. // 初始化一个async句柄, 注册回调函数
75. uv_async_init(loop, async, async_cb);
76. // 让loop开始运行
77. uv_run(loop, UV_RUN_DEFAULT);
78. // 清理所有的handle
79. stop_loop(loop);
80. // 释放loop
81. uv_loop_close(loop);
82. delete loop;
83. });
84. t.detach();
85. return 0;
86. }

88. // 在另一个线程上调用uv_async_send函数
89. static napi_value TestTimerAsyncSend(napi_env env, napi_callback_info info)
90. {
91. std::thread t1([](){ // B线程
92. uv_async_send(async);  // 调用uv_async_send, 通知loop线程调用与async句柄绑定的timer_cb
93. uv_sleep(500);
94. // 修改cond1, 关闭timer handle
95. cond1 = true;
96. });

98. std::thread t2([](){ // B线程
99. uv_sleep(1000);
100. // 修改cond2, 关闭async handle
101. cond2 = true;
102. uv_async_send(async);
103. });

105. t1.detach();
106. t2.detach();
107. return 0;
108. }

110. EXTERN_C_START
111. static napi_value Init(napi_env env, napi_value exports)
112. {
113. napi_property_descriptor desc[] = {
114. {"testTimerAsync", nullptr, TestTimerAsync, nullptr, nullptr, nullptr, napi_default, nullptr},
115. {"testTimerAsyncSend", nullptr, TestTimerAsyncSend, nullptr, nullptr, nullptr, napi_default, nullptr},
116. };
117. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
118. return exports;
119. }
120. EXTERN_C_END

122. static napi_module demoModule = {
123. .nm_version = 1,
124. .nm_flags = 0,
125. .nm_filename = nullptr,
126. .nm_register_func = Init,
127. .nm_modname = "entry",
128. .nm_priv = ((void *)0),
129. .reserved = {0},
130. };

132. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
133. {
134. napi_module_register(&demoModule);
135. }
```

在index.d.ts添加如下代码：

```
1. export const testTimerAsync:() => number;
2. export const testTimerAsyncSend:() => number;
```

**2. 从env获取loop**

开发者使用napi\_get\_uv\_event\_loop接口从env获取到的loop一般是系统创建的JS主线程的事件循环，因此应当避免在子线程中调用非线程安全函数。

如因业务需要，必须在非loop线程上调用非线程安全函数，请使用线程安全函数uv\_async\_send将任务提交到loop线程。即定义一个uv\_async\_t\*类型的句柄，初始化该句柄的时候，将需要在子线程调用的非线程安全函数在对应的async\_cb中调用，然后在非loop线程上调用uv\_async\_send函数，并回到loop线程上执行async\_cb。请参考[libuv中的handles和requests](libuv.md#libuv中的handles和requests)章节关于**正确使用timer示例**的场景二内容。

### 线程安全函数

在libuv中，由于涉及到大量的异步任务，稍有不慎就会陷入到多线程问题中。在这里，我们对libuv中常用的线程安全函数和非线程安全函数做了汇总。若开发者在多线程编程中调用了非线程安全的函数，势必要对其进行加锁保护或者保证代码的正确运行时序，否则将陷入到crash问题中。

线程安全函数：

* uv\_async\_send()：向异步句柄发送信号，可以在任何线程中调用。
* uv\_thread\_create()：创建一个新线程并执行指定的函数，可以在任何线程中调用。
* 锁相关的操作，如uv\_mutex\_lock()、uv\_mutex\_unlock()等等。

**提示：所有形如uv\_xxx\_init的函数，即使它是以线程安全的方式实现的，但使用时要注意，避免多个线程同时调用uv\_xxx\_init，否则它依旧会引起多线程资源竞争的问题。最好的方式是在事件循环线程中调用该函数。**

**注：uv\_async\_send函数被调用后，回调函数是被异步触发的。如果调用了多次uv\_async\_send，libuv只保证至少有一次回调会被执行。这就可能导致一旦对同一句柄触发了多次uv\_async\_send，libuv对回调的处理可能会违背开发者的预期。多次对同一个async句柄进行send操作，还会导致任意两次相同句柄send操作之间提交的的其他async\_cb任务丢失。** 而在Native侧，可以保证回调的执行次数和开发者调用napi\_call\_threadsafe\_function的次数保持一致。

非线程安全函数：

* uv\_os\_unsetenv()：删除环境变量
* uv\_os\_setenv()：设置环境变量
* uv\_os\_getenv()：获取环境变量
* uv\_os\_environ()：检索所有的环境变量
* uv\_os\_tmpdir()：获取临时目录
* uv\_os\_homedir()：获取家目录

### libuv中的事件循环

事件循环是libuv中最核心的一个概念，loop负责管理整个事件循环的所有资源，它贯穿于整个事件循环的生命周期。通常将uv\_run所在的线程称为该事件循环的主线程。

**1. 事件循环运行的三种方式**

UV\_RUN\_DEFAULT：默认轮询方式，该模式将会一直运行下去，直到loop中没有活跃的句柄和请求。

UV\_RUN\_ONCE：一次轮询模式，如果pending\_queue中有回调函数，则执行，然后跳过uv\_\_io\_poll函数。此模式默认认为loop中一定有事件发生。

UV\_RUN\_NOWAIT：非阻塞模式，该模式下不会执行pending\_queue，而是直接执行一次I/O轮询（uv\_\_io\_poll）。

**2. 常用接口**

```
1. int uv_loop_init(uv_loop_t* loop);
```

对loop进行初始化。

```
1. int uv_loop_close(uv_loop_t* loop);
```

关闭loop，该函数只有在loop中所有的句柄和请求都关闭后才能成功返回，否则将返回UV\_EBUSY。

```
1. int uv_loop_delete(uv_loop_t* loop);
```

释放loop，该接口会先调用uv\_loop\_close，然后再将loop释放掉。在HarmonyOS平台上，由于assert函数不生效，因此不论uv\_loop\_close函数是否成功清理loop上的资源，都会将loop释放掉。开发者使用该接口时，请务必确保在loop线程退出时，loop上的资源可以被正确释放，即挂在loop上的handle和request均被关闭，否则会导致资源泄漏。**开发者使用该接口时务必格外谨慎，建议非必要不使用。**

```
1. uv_loop_t* uv_default_loop(void);
```

该函数创建一个进程级的loop。在HarmonyOS中，由于目前的应用主循环及其他JS工作线程还存在着libuv的loop。因此我们不建议开发者使用该函数来创建loop并实现业务功能。

```
1. int uv_run(uv_loop_t* loop, uv_run_mode mode);
```

启动事件循环。运行模式可查看事件循环运行的三种方式。

```
1. int uv_loop_alive(uv_loop_t loop);
```

判断loop是否处于活跃状态。

```
1. void uv_stop(uv_loop_t* loop);
```

该函数用来停止一个事件循环，在loop的下一次迭代中才会停止。如果该函数发生在I/O操作之前，将不会阻塞而是直接跳过uv\_\_io\_poll。

### libuv中的handles和requests

handle表示一个持久性的对象，通常挂载到loop中对应的handle\_queue队列上。如果handle处于活跃状态，每次uv\_run都会处理handle中的回调函数。

request表示一个短暂性的请求，一个request只触发一次回调操作。

下面是HarmonyOS系统中最常用的几个Handles和Requests：

```
1. /* Handle Type */
2. typedef struct uv_handle_s uv_handle_t;
3. typedef struct uv_timer_s uv_timer_t;
4. typedef struct uv_async_s uv_async_t;
5. typedef struct uv_signal_s uv_signal_t;

7. /* Request Type */
8. typedef struct uv_req_s uv_req_t;
9. typedef struct uv_work_s uv_work_t;
10. typedef struct uv_fs_s uv_fs_t;
```

**注：在handles中，uv\_xxx\_t继承了uv\_handle\_t；在requests中，uv\_work\_t继承了uv\_req\_t。**

对于libuv中的handles，对其有正确的认识并管理好它的生命周期至关重要。handle作为一个长期存在于loop中的句柄，在使用中，开发者应遵循下面的原则：

1. 句柄的初始化工作应在事件循环的线程中进行。
2. 若由于业务问题，句柄需要在其他工作线程初始化，在使用之前用原子变量判断是否初始化完成。
3. 句柄在确定后续不再使用后，调用uv\_close将句柄从loop中摘除。

在这里，需要特别说明一下uv\_close的使用方法。uv\_close被用来关闭一个handle，但是关闭handle的动作是异步的。函数原型为：

```
1. void uv_close(uv_handle_t* handle, uv_close_cb close_cb)
```

handle：要关闭的句柄。

close\_cb：处理该句柄的函数，用来进行内存管理等操作。

调用uv\_close后，首先将要关闭的handle挂载到loop的closing\_handles队列上，然后等待loop所在线程运行uv\_\_run\_closing\_handles函数。最后回调函数close\_cb将会在loop的下一次迭代中执行。因此，释放内存等操作应该在close\_cb中进行。并且这种异步的关闭操作会带来多线程问题，开发者需要谨慎处理uv\_close的时序问题，并且保证在close\_cb执行之前handles的生命周期。

**Tips**：在[libuv官方文档](http://libuv.org/)中，有个经验法则需要在此提示一下。原文翻译：如果 uv\_foo\_t 类型的句柄具有 uv\_foo\_start() 函数，则从调用该函数的那一刻起，它就处于活动状态。 同样，uv\_foo\_stop()再次停用句柄。

注意

1. 所有的handle关闭前必须要调用uv\_close，所有的内存操作都要在uv\_close的close\_cb中执行。
2. 所有的handle操作都不能通过获取其他线程loop的方式，在非loop线程上调用。

对于libuv中的requests，开发者需要确保在进行异步任务提交时，**通过动态申请的request，要在loop所在线程执行的complete回调函数中释放**。用uv\_work\_t举例，代码可参考如下：

```
1. uv_work_t* work = new uv_work_t;
2. uv_queue_work(loop, work, [](uv_work_t* req) {
3. // 异步操作
4. }, [](uv_work_t* req, int status) {
5. // 回调操作
6. delete req;
7. });
```

### libuv timer使用规范

使用libuv timer需要遵守如下约定：

1. 请不要在多个线程中使用libuv的接口（uv\_timer\_start、uv\_timer\_stop和uv\_timer\_again）同时操作同一个loop的timer heap，否则将导致崩溃，如果想要使用libuv的接口操作定时器，请**保持在与当前env绑定的loop所在线程上操作**；
2. 如因业务需求往指定线程抛定时器，请使用uv\_async\_send线程安全函数实现。

**1. 错误使用timer示例**

以下错误示例中，由于在多个线程操作同一个loop的timer heap，崩溃率极高。

ArkTS侧：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. function waitforRunner(): number {
5. "use concurrent"
6. hilog.info(0xff, "testTag", "executed");
7. return 0;
8. }

10. @Entry
11. @Component
12. struct Index {
13. build() {
14. Row() {
15. Column() {
16. Button("TimerTest")
17. .width('40%')
18. .fontSize('14fp')
19. .onClick(() => {
20. let i: number = 20;
21. while (i--) {
22. setTimeout(waitforRunner, 200);
23. testNapi.testTimer();
24. }
25. }).margin(20)
26. }.width('100%')
27. }.height('100%')
28. }
29. }
```

Native C++侧：

```
1. #include <napi/native_api.h>
2. #include <uv.h>
3. #define LOG_DOMAIN 0x0202
4. #define LOG_TAG "MyTag"
5. #include "hilog/log.h"
6. #include <thread>
7. #include <unistd.h>

9. static napi_value TestTimer(napi_env env, napi_callback_info info)
10. {
11. uv_loop_t* loop = nullptr;
12. uv_timer_t* timer = new uv_timer_t;

14. napi_get_uv_event_loop(env, &loop);
15. uv_timer_init(loop, timer);
16. std::thread t1([&loop, &timer](){
17. uv_timer_start(timer, [](uv_timer_t* timer){
18. uv_timer_stop(timer);
19. }, 1000, 0);
20. });

22. t1.detach();
23. return 0;
24. }

26. EXTERN_C_START
27. static napi_value Init(napi_env env, napi_value exports)
28. {
29. napi_property_descriptor desc[] = {
30. {"testTimer", nullptr, TestTimer, nullptr, nullptr, nullptr, napi_default, nullptr},
31. };
32. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
33. return exports;
34. }
35. EXTERN_C_END

37. static napi_module demoModule = {
38. .nm_version = 1,
39. .nm_flags = 0,
40. .nm_filename = nullptr,
41. .nm_register_func = Init,
42. .nm_modname = "entry",
43. .nm_priv = ((void *)0),
44. .reserved = {0},
45. };

47. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
48. {
49. napi_module_register(&demoModule);
50. }
```

在index.d.ts添加如下代码：

```
1. export const testTimer:() => number;
```

**2. 正确使用timer示例**

**场景一：** 在上述场景中，需保证在JS主线程上进行timer的相关操作。将上述TestTimer函数的代码做如下修改，便可以避免崩溃发生。

```
1. static napi_value TestTimer(napi_env env, napi_callback_info info)
2. {
3. uv_loop_t* loop = nullptr;
4. uv_timer_t* timer = new uv_timer_t;

6. napi_get_uv_event_loop(env, &loop);
7. uv_timer_init(loop, timer);
8. uv_timer_start(timer, [](uv_timer_t* timer){
9. uv_timer_stop(timer);
10. }, 1000, 0);

12. return 0;
13. }
```

**场景二：** 如果需要在指定的子线程抛定时器，请使用线程安全函数uv\_async\_send实现。

ArkTS侧：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so'

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Button("TestTimerAsync")
11. .width('40%')
12. .fontSize('14fp')
13. .onClick(() => {
14. testNapi.testTimerAsync();  // 初始化async句柄
15. }).margin(20)

17. Button("TestTimerAsyncSend")
18. .width('40%')
19. .fontSize('14fp')
20. .onClick(() => {
21. testNapi.testTimerAsyncSend();  // 子线程调用uv_async_send提交定时器任务
22. }).margin(20)
23. }.width('100%')
24. }.height('100%')
25. }
26. }
```

Native侧：

```
1. #include <napi/native_api.h>
2. #include <uv.h>
3. #define LOG_DOMAIN 0x0202
4. #define LOG_TAG "MyTag"
5. #include "hilog/log.h"
6. #include <thread>
7. #include <unistd.h>
8. uv_async_t* async = new uv_async_t;

10. // 执行创建定时器操作
11. void async_cb(uv_async_t* handle)
12. {
13. auto loop = handle->loop;
14. uv_timer_t* timer = new uv_timer_t;
15. uv_timer_init(loop, timer);

17. uv_timer_start(timer, [](uv_timer_t* timer){
18. uv_timer_stop(timer);
19. }, 1000, 0);
20. }

22. // 初始化async句柄，绑定对应的回调函数
23. static napi_value TestTimerAsync(napi_env env, napi_callback_info info)
24. {
25. uv_loop_t* loop = nullptr;
26. napi_get_uv_event_loop(env, &loop);
27. uv_async_init(loop, async, async_cb);
28. return 0;
29. }

31. static napi_value TestTimerAsyncSend(napi_env env, napi_callback_info info)
32. {
33. std::thread t([](){
34. uv_async_send(async);  // 在任意子线程中调用uv_async_send，通知主线程调用与async绑定的timer_cb
35. });
36. t.detach();
37. return 0;
38. }

40. EXTERN_C_START
41. static napi_value Init(napi_env env, napi_value exports)
42. {
43. napi_property_descriptor desc[] = {
44. {"testTimerAsync", nullptr, TestTimerAsync, nullptr, nullptr, nullptr, napi_default, nullptr},
45. {"testTimerAsyncSend", nullptr, TestTimerAsyncSend, nullptr, nullptr, nullptr, napi_default, nullptr},
46. };
47. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
48. return exports;
49. }
50. EXTERN_C_END

52. static napi_module demoModule = {
53. .nm_version = 1,
54. .nm_flags = 0,
55. .nm_filename = nullptr,
56. .nm_register_func = Init,
57. .nm_modname = "entry",
58. .nm_priv = ((void *)0),
59. .reserved = {0},
60. };

62. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
63. {
64. napi_module_register(&demoModule);
65. }
```

在index.d.ts添加如下代码：

```
1. export const testTimerAsync:() => number;
2. export const testTimerAsyncSend:() => number;
```

### 线程间通信

上面简单介绍了一些libuv中的基本概念，在这里我们将着重介绍libuv中的线程间通信。

libuv的线程间通信是通过uv\_async\_t句柄来进行的，相关函数如下：

```
1. int uv_async_init(uv_loop_t* loop, uv_async_t* handle, uv_async_cb async_cb)
```

loop：事件循环loop。

handle：线程间通信句柄。

async\_cb：回调函数。

返回：成功，返回0。失败，返回错误码。

```
1. int uv_async_send(uv_async_t* handle)
```

handle：线程间通信句柄。

返回：成功，返回0。失败，返回错误码。

说明

1. uv\_async\_t从调用uv\_async\_init开始后就一直处于活跃状态，除非用uv\_close将其关闭。
2. uv\_async\_t的执行顺序严格按照uv\_async\_init的顺序，而非通过uv\_async\_send的顺序来执行的。因此按照初始化的顺序来管理好时序问题是必要的。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ThTgsOu6Teeby6B-7CQQrw/zh-cn_image_0000002589247247.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061005Z&HW-CC-Expire=86400&HW-CC-Sign=5B6B322A4657489734FB4B0C27B22C90DD9B0C3E47008B6B9A56758ADD2FE94F)

示例代码：

```
1. #include <iostream>
2. #include <thread>
3. #include "uv.h"

5. uv_loop_t* loop = nullptr;
6. uv_async_t* async = nullptr;
7. int g_counter = 10;

9. void async_handler(uv_async_t* handle)
10. {
11. std::cout << "ohos async print" << std::endl;
12. if (--g_counter == 0) {
13. // 调用uv_close关闭async，在主循环中释放内存。
14. uv_close((uv_handle_t*)async, [](uv_handle_t* handle) {
15. std::cout << "delete async" << std::endl;
16. delete (uv_async_t*)handle;
17. });
18. }
19. }

21. int main()
22. {
23. loop = uv_default_loop();
24. async = new uv_async_t;
25. uv_async_init(loop, async, async_handler);
26. std::thread subThread([]() {
27. for (int i = 0; i < 10; i++) {
28. usleep(100); // 避免多次调用uv_async_send只执行一次
29. std::cout << i << "th: subThread triggered" << std::endl;
30. uv_async_send(async);
31. }
32. });
33. subThread.detach();
34. return uv_run(loop, UV_RUN_DEFAULT);
35. }
```

该示例代码仅仅描述了一个简单的场景，步骤如下：

1. 在主线程中初始化async句柄；
2. 新建一个子线程，在里面每隔100毫秒触发一次uv\_async\_send。10次以后调用uv\_close关闭async句柄；
3. 在主线程运行事件循环。

可以看到，每触发一次，主线程都会执行一次回调函数。

```
1. 0th:subThread triggered
2. ohos async print
3. 1th:subThread triggered
4. ohos async print
5. 2th:subThread triggered
6. ohos async print
7. 3th:subThread triggered
8. ohos async print
9. 4th:subThread triggered
10. ohos async print
11. 5th:subThread triggered
12. ohos async print
13. 6th:subThread triggered
14. ohos async print
15. 7th:subThread triggered
16. ohos async print
17. 8th:subThread triggered
18. ohos async print
19. 9th:subThread triggered
20. ohos async print
21. delete async
```

### 线程池

线程池是libuv的一个核心功能，libuv中的线程池通过uv\_loop\_t中的成员变量wq\_async来控制工作线程与主线程的通信。核心函数如下：

```
1. int uv_queue_work(uv_loop_t* loop,
2. uv_work_t* req,
3. uv_work_cb work_cb,
4. uv_after_work_cb after_work_cb)
```

work\_cb：提交给工作线程的任务。

after\_work\_cb：loop所在线程要执行的回调函数。

注意

work\_cb与after\_work\_cb的执行有一个时序问题，只有work\_cb执行完，通过uv\_async\_send(loop->wq\_async)触发fd事件，loop所在线程在下一次迭代中才会执行after\_work\_cb。只有执行到after\_work\_cb时，与之相关的uv\_work\_t生命周期才算结束。

**1. 异步任务提交**

下图为原生libuv的线程池工作流程，图中流程已简化，默认句柄的pending标志为1，worker线程个数不代表线程池中线程的真实数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/EdmJZi6dTMi-W7TvSr4zzg/zh-cn_image_0000002558767440.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061005Z&HW-CC-Expire=86400&HW-CC-Sign=C36BEAD6106BF6B37D66061B38080AC849BB715B3B40BA1E17DAAE694260EBD3)

**2. 异步任务提交注意事项**

在HarmonyOS中，uv\_queue\_work函数在UI线程的工作流程为：将work\_cb抛到FFRT对应优先级的线程池中，然后待FFRT调度执行该任务，并将after\_work\_cb抛到eventhandler对应优先级的event queue中，等待eventhandler调度并回到loop线程执行。需要注意的是，uv\_queue\_work调用完后，并不代表其中的任何一个任务执行完，仅代表将work\_cb插入到FFRT对应优先级的线程池中。taskpool和jsworker线程的工作流程和原生libuv逻辑保持一致。

**3. uv\_queue\_work使用约束**

特别强调，开发者需要明确，uv\_queue\_work函数仅用于抛异步任务，**异步任务的execute回调被提交到线程池后会经过调度执行，因此并不保证多次提交的任务及其回调按照时序关系执行**。

另外，uv\_queue\_work仅限于在loop线程中调用，这样不会有多线程安全问题。**请不要把uv\_queue\_work作为线程间通信的手段，即A线程获取到B线程的loop，并通过uv\_queue\_work抛异步任务的方式，把execute置为空任务，而把complete回调放在B线程中执行。** 这种方式不仅低效，而且还增加了发生故障时定位问题的难度。为了避免低效的任务提交，请使用[napi\_threadsafe\_function相关函数](../harmonyos-guides/use-napi-thread-safety.md)。

### libuv的使用现状

当前HarmonyOS系统中涉及到libuv的线程主要有主线程、JS Worker线程、Taskpool中的TaskWorker线程以及IPC线程。除了主线程采用了eventhandler作为主循环，其他线程都是使用libuv中的UV\_RUN\_DEFAULT运行模式作为当前线程的事件主循环来执行任务。在主线程中，eventhandler通过fd驱动的方式来触发任务的执行，eventhandler监听了uv\_loop中的backend\_fd。当loop中有fd事件触发的时候，eventhandler会执行一次uv\_run来执行一遍libuv中的任务。

综上所述，开发者会发现这样一种现象：**同样的libuv接口在主线程上不生效，但在JS Worker线程中就没问题。这主要还是因为主线程上所有不通过触发fd来驱动的uv接口都不会得到及时的响应。**

另外，在应用主线程中，所有的异步任务尽管最终都是通过libuv得到执行的。但是在当前系统中，libuv的线程池已经对接到了FFRT中，任何抛向libuv的异步任务都会在FFRT的线程中得到调度。应用主线程的回调函数也通过PostTask接口插入到eventhandler的队列上。这就意味着FFRT线程上的异步任务完成后不再通过uv\_async\_send的方式触发主线程的回调。过程如下图:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/dcouKpY1SgWeVFzkzoPghQ/zh-cn_image_0000002558607782.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061005Z&HW-CC-Expire=86400&HW-CC-Sign=23A35801DE5E2323624C42B79C4245C4231D561AA6827ED756279FE31554A533)

我们总结了五种类型的请求任务是直接可以按照正常用法在应用主循环中生效的：

* uv\_random\_t

  函数原型：

```
1. /**
2. * @brief 将一个工作请求添加到事件循环的队列中。
3. *
4. * @param loop 事件循环
5. * @param req 随机数请求
6. * @param buf 存储随机数的缓冲区
7. * @param buflen 缓冲区的长度
8. * @param flags 一个无符号整数，表示生成随机数的选项
9. * @param cb  随机数生成完成后的回调函数
10. *
11. * @return 成功返回0，失败返回错误码
12. */
13. int uv_random(uv_loop_t* loop,
14. uv_random_t* req,
15. void* buf,
16. size_t buflen,
17. unsigned flags,
18. uv_random_cb cb);
```

* uv\_work\_t

  函数原型：

```
1. /**
2. * @brief 将一个工作请求添加到事件循环的队列中。当事件循环在下一次迭代时，work_cb函数将会在一个新的线程中被调用。当work_cb函数完成时，after_work_cb函数将会在事件循环的线程中被调用。
3. *
4. * @param loop 事件循环
5. * @param req 工作请求
6. * @param work_cb 在新线程中被调用的函数
7. * @param after_work_cb 在事件循环线程中被调用的函数
8. *
9. * @return 成功返回0，失败返回-1
10. */
11. int uv_queue_work(uv_loop_t* loop,
12. uv_work_t* req,
13. uv_work_cb work_cb,
14. uv_after_work_cb after_work_cb);
```

* uv\_fs\_t

  文件类提供的所有异步接口，在应用主线程中都是可以生效的。主要有如下：

```
1. /**
2. * @brief 异步读取文件
3. *
4. * @param loop 事件循环
5. * @param req 文件操作请求
6. * @param file 文件描述符
7. * @param bufs 读取数据的缓冲区
8. * @param nbufs 缓冲区的数量
9. * @param off 文件的偏移量
10. * @param cb 完成后的回调函数
11. * @return 成功返回0，失败返回-1
12. */
13. int uv_fs_read(uv_loop_t* loop, uv_fs_t* req,
14. uv_file file,
15. const uv_buf_t bufs[],
16. unsigned int nbufs,
17. int64_t off,
18. uv_fs_cb cb);

20. /**
21. * @brief 异步打开文件
22. *
23. * @param loop 事件循环
24. * @param req 文件操作请求
25. * @param path 文件路径
26. * @param flags 打开文件的方式
27. * @param mode 文件权限
28. * @param cb 完成后的回调函数
29. *
30. * @return 成功返回0，失败返回-1
31. */
32. int uv_fs_open(uv_loop_t* loop,
33. uv_fs_t* req,
34. const char* path,
35. int flags,
36. int mode,
37. uv_fs_cb cb);

39. /**
40. * @brief 异步发送文件
41. *
42. * @param loop 事件循环
43. * @param req 文件操作请求
44. * @param out_fd 输出文件描述符
45. * @param in_fd 输入文件描述符
46. * @param off 文件的偏移量
47. * @param len 发送的长度
48. * @param cb 完成后的回调函数
49. *
50. * @return 成功返回0，失败返回-1
51. */
52. int uv_fs_sendfile(uv_loop_t* loop,
53. uv_fs_t* req,
54. uv_file out_fd,
55. uv_file in_fd,
56. int64_t off,
57. size_t len,
58. uv_fs_cb cb);

60. /**
61. * @brief 异步写入文件
62. *
63. * @param loop 事件循环
64. * @param req 文件操作请求
65. * @param file 文件描述符
66. * @param bufs 要写入的数据
67. * @param nbufs 数据的数量
68. * @param off 文件的偏移量
69. * @param cb 完成后的回调函数
70. *
71. * @return 成功返回0，失败返回-1
72. */
73. int uv_fs_write(uv_loop_t* loop,
74. uv_fs_t* req,
75. uv_file file,
76. const uv_buf_t bufs[],
77. unsigned int nbufs,
78. int64_t off,
79. uv_fs_cb cb);

81. /**
82. * @brief 异步复制文件
83. *
84. * @param loop 事件循环
85. * @param req 文件操作请求
86. * @param path 源文件路径
87. * @param new_path 目标文件路径
88. * @param flags 复制选项
89. * @param cb 完成后的回调函数
90. *
91. * @return 成功返回0，失败返回-1
92. */
93. int uv_fs_copyfile(uv_loop_t* loop,
94. uv_fs_t* req,
95. const char* path,
96. const char* new_path
97. int flags,
98. uv_fs_cb cb);
```

* uv\_getaddrinfo\_t

  函数原型：

```
1. /**
2. * @brief 异步获取地址信息
3. *
4. * @param loop 事件循环
5. * @param req 地址信息请求
6. * @param cb 完成后的回调函数
7. * @param hostname 主机名
8. * @param service 服务名
9. * @param hints 地址信息提示
10. *
11. * @return 成功返回0，失败返回-1
12. */
13. int uv_getaddrinfo(uv_loop_t* loop,
14. uv_getaddrinfo_t* req,
15. uv_getaddrinfo_cb cb,
16. const char* hostname,
17. const char* service,
18. const struct addrinfo* hints);
```

* uv\_getnameinfo\_t

  函数原型：

```
1. /**
2. * @brief 异步获取名称信息
3. *
4. * @param loop 事件循环
5. * @param req 名称信息请求
6. * @param getnameinfo_cb 完成后的回调函数
7. * @param addr 地址
8. * @param flags 标志
9. *
10. * @return 成功返回0，失败返回-1
11. */
12. int uv_getnameinfo(uv_loop_t* loop,
13. uv_getnameinfo_t* req,
14. uv_getnameinfo_cb getnameinfo_cb,
15. const struct sockaddr* addr,
16. int flags);
```

在应用主线程上不生效的接口主要包括：

* idle句柄
* prepare句柄
* check句柄
* signal相关函数
* tcp及udp相关函数
