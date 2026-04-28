---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-cleanuphook
title: 使用Node-API接口注册和使用环境清理钩子
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口注册和使用环境清理钩子
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a74181e286087f9cd310bfe90aaeb732348339ced773a76ca9c86eac27a304ba
---

## 简介

使用Node-API接口在进程退出时处理未释放资源，在Node-API模块注册清理钩子，一旦当前环境退出，这些钩子就会运行，使所有资源都被正确释放。

## 基本概念

Node-API提供了注册和取消注册清理钩子函数的功能，以下是相关概念：

* **资源管理**：在ArkTS中，通常需要管理一些系统资源，比如内存、文件句柄、网络连接等。这些资源必须在Node-API模块的生命周期中正确地创建、使用和释放，以避免资源泄漏和程序崩溃。资源管理通常包括初始化资源、在合适的时候清理资源，以及在清理资源时执行必要的操作，比如关闭文件或断开网络连接。
* **钩子函数（Hook）**：钩子函数是一种在特定事件或时间点自动执行的回调函数。在Node-API模块的上下文中，清理钩子函数通常用于在环境或进程退出时执行资源清理任务。这是因为环境或进程退出时，操作系统可能不会立即回收所有资源，因此需要通过清理钩子函数来确保所有资源都被正确释放。

以上这些基本概念是理解和使用Node-API接口注册环境清理钩子的基础，下面将介绍具体的接口和使用示例。

## 场景和功能介绍

以下Node-API接口用于注册和取消不同类型的清理钩子。他们的使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_add\_env\_cleanup\_hook | 注册一个环境清理钩子函数，该函数将在Node-API环境退出时被调用。 |
| napi\_remove\_env\_cleanup\_hook | 取消之前注册的环境清理钩子函数，避免其在环境清理时执行。 |
| napi\_add\_async\_cleanup\_hook | 注册一个异步清理钩子函数，该函数将在Node-API进程退出时异步执行。 |
| napi\_remove\_async\_cleanup\_hook | 取消之前注册的异步清理钩子函数，确保在不需要时不会执行相关的清理工作。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_add\_env\_cleanup\_hook

用于注册一个环境清理钩子函数，该函数将在环境退出时执行。这是确保资源在环境销毁前得到清理的重要机制。

需要注意的是，napi\_add\_env\_cleanup\_hook接口并不支持对同一arg绑定多个回调。若出现env已销毁，但cleanup回调未被执行的情况，可以在启用ArkTS运行时[多线程检测](ide-multi-thread-check.md)功能的前提下，查看hilog流水日志AddCleanupHook Failed, data cannot register multiple times.来查找发生注册失败的调用。

### napi\_remove\_env\_cleanup\_hook

用于取消之前注册的环境清理钩子函数。在某些情况下，需要在插件卸载或资源被重新分配时取消钩子函数。

cpp部分代码

```
1. #include <hilog/log.h>
2. #include <string>
3. #include "napi/native_api.h"
4. #include "uv.h"

6. // 定义内存结构，包含指向数据的指针和数据的大小
7. typedef struct {
8. char *data;
9. size_t size;
10. } Memory;

12. // 外部缓冲区清理回调函数，用于释放分配的内存
13. void ExternalFinalize(napi_env env, void *finalizeData, void *finalizeHint)
14. {
15. Memory *wrapper = (Memory *)finalizeHint;
16. // ...
17. free(wrapper->data);
18. free(wrapper);
19. OH_LOG_INFO(LOG_APP, "Node-API napi_add_env_cleanup_hook ExternalFinalize");
20. }

22. // 在环境关闭时执行一些清理操作，如清理全局变量或其他需要在环境关闭时处理的资源
23. static void Cleanup(void *arg)
24. {
25. // 执行清理操作
26. OH_LOG_INFO(LOG_APP, "Node-API napi_add_env_cleanup_hook cleanuped: %{public}d", *(int *)(arg));
27. }

29. // 创建外部缓冲区并注册环境清理钩子函数
30. static napi_value NapiEnvCleanUpHook(napi_env env, napi_callback_info info)
31. {
32. // 分配内存并复制字符串数据到内存中
33. std::string str("Hello from Node-API!");
34. Memory *wrapper = (Memory *)malloc(sizeof(Memory));
35. if (wrapper == nullptr) {
36. OH_LOG_ERROR(LOG_APP, "malloc for wrapper failed");
37. return nullptr;
38. }
39. wrapper->data = static_cast<char *>(malloc(str.size() + 1));
40. if (wrapper->data == nullptr) {
41. free(wrapper);
42. OH_LOG_ERROR(LOG_APP, "malloc for wrapper->data failed");
43. return nullptr;
44. }
45. std::copy_n(str.c_str(), str.size() + 1, wrapper->data);
46. wrapper->size = str.size();
47. // 创建外部缓冲区对象，并指定清理回调函数
48. // 注意：wrapper->data 的内存释放依赖于 ExternalFinalize 回调，只有 buffer 被正确持有并最终被 GC 回收时，ExternalFinalize 才会被调用，否则会导致内存泄漏。
49. napi_value buffer = nullptr;
50. napi_status status = napi_create_external_buffer(env, wrapper->size, (void *)wrapper->data,
51. ExternalFinalize, wrapper, &buffer);
52. if (status != napi_ok) {
53. // 创建失败时需主动释放内存，避免泄漏
54. free(wrapper->data);
55. free(wrapper);
56. OH_LOG_ERROR(LOG_APP, "napi_create_external_buffer failed.");
57. return nullptr;
58. }
59. // 静态变量作为钩子函数参数
60. static int hookArg = 42;
61. static int hookParameter = 1;
62. // 注册环境清理钩子函数
63. status = napi_add_env_cleanup_hook(env, Cleanup, &hookArg);
64. if (status != napi_ok) {
65. OH_LOG_ERROR(LOG_APP, "Test Node-API napi_add_env_cleanup_hook failed.");
66. return nullptr;
67. }
68. // 注册环境清理钩子函数，此处不移除环境清理钩子，为了在ArkTS环境被销毁时，这个钩子函数被调用，用来模拟执行一些清理操作，例如释放资源、关闭文件等。
69. status = napi_add_env_cleanup_hook(env, Cleanup, &hookParameter);
70. if (status != napi_ok) {
71. OH_LOG_ERROR(LOG_APP, "Test Node-API napi_add_env_cleanup_hook failed.");
72. return nullptr;
73. }
74. // 立即移除环境清理钩子函数，确保不会在后续环境清理时被调用
75. // 不需要此钩子函数时可以将其移除。如果希望钩子在环境退出时执行，不需要移除。
76. napi_remove_env_cleanup_hook(env, Cleanup, &hookArg);
77. napi_remove_env_cleanup_hook(env, Cleanup, &hookParameter);
78. // 返回创建的外部缓冲区对象
79. return buffer;
80. }
```

接口声明

```
1. export const napiEnvCleanUpHook: () => Object | undefined;
```

ArkTS侧示例代码

```
1. let wk = new worker.ThreadWorker('entry/ets/workers/worker.ts');
2. // 发送消息到worker线程
3. wk.postMessage('test NapiEnvCleanUpHook');
4. // 处理来自worker线程的消息
5. wk.onmessage = (message) => {
6. hilog.info(0x0000, 'testTag', 'Test Node-API message from worker: %{public}s',
7. JSON.stringify(message));
8. wk.terminate();
9. };
```

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { worker } from '@kit.ArkTS';
3. import testNapi from 'libentry.so';

5. let parent = worker.workerPort;
6. // 处理来自主线程的消息
7. parent.onmessage = (message) => {
8. hilog.info(0x0000, 'testTag', 'Test Node-API message from main thread: %{public}s', JSON.stringify(message));
9. // 发送消息到主线程
10. parent.postMessage('Test Node-API worker:' + testNapi.napiEnvCleanUpHook());
11. };
```

worker相关开发配置和流程参考以下链接：

[使用Worker进行线程间通信](worker-introduction.md)

### napi\_add\_async\_cleanup\_hook

这个接口用于注册一个异步清理钩子函数，该函数将在环境退出时异步执行。与同步钩子不同，异步钩子允许在进程退出时进行更长时间的操作，而不会阻塞进程退出。

### napi\_remove\_async\_cleanup\_hook

这个接口用于取消之前注册的异步清理钩子函数。与取消同步钩子类似，这通常是在不再需要钩子函数时进行的操作。

cpp部分代码

```
1. typedef struct {
2. napi_env env;
3. void *testData;
4. uv_async_s asyncUv;
5. napi_async_cleanup_hook_handle cleanupHandle;
6. } AsyncContent;

8. // 删除异步工作对象并注销钩子函数
9. static void FinalizeWork(uv_handle_s *handle)
10. {
11. AsyncContent *asyncData = reinterpret_cast<AsyncContent *>(handle->data);
12. // 不再需要异步清理钩子函数的情况下，尝试将其从环境中移除
13. napi_status result = napi_remove_async_cleanup_hook(asyncData->cleanupHandle);
14. if (result != napi_ok) {
15. napi_throw_error(asyncData->env, nullptr, "Test Node-API napi_remove_async_cleanup_hook failed");
16. }
17. // 释放AsyncContent
18. free(asyncData);
19. }

21. // 异步执行环境清理工作
22. static void AsyncWork(uv_async_s *async)
23. {
24. // 执行一些清理工作,比如释放动态分配的内存
25. AsyncContent *asyncData = reinterpret_cast<AsyncContent *>(async->data);
26. if (asyncData != nullptr && asyncData->testData != nullptr) {
27. free(asyncData->testData);
28. asyncData->testData = nullptr;
29. }
30. // 关闭libuv句柄，并触发FinalizeWork回调清理
31. uv_close((uv_handle_s *)async, FinalizeWork);
32. }

34. // 异步清理钩子函数，创建异步工作对象并执行
35. static void AsyncCleanup(napi_async_cleanup_hook_handle handle, void *info)
36. {
37. AsyncContent *data = reinterpret_cast<AsyncContent *>(info);
38. // 获取libUv循环实例并初始化一个异步句柄，以便后续执行异步工作
39. uv_loop_s *uvLoop;
40. napi_get_uv_event_loop(data->env, &uvLoop);
41. uv_async_init(uvLoop, &data->asyncUv, AsyncWork);

43. data->asyncUv.data = data;
44. data->cleanupHandle = handle;
45. // 发送异步信号触发AsyncWork函数执行清理工作
46. uv_async_send(&data->asyncUv);
47. }

49. static napi_value NapiAsyncCleanUpHook(napi_env env, napi_callback_info info)
50. {
51. // 分配AsyncContent内存
52. AsyncContent *data = reinterpret_cast<AsyncContent *>(malloc(sizeof(AsyncContent)));
53. // ...
54. data->env = env;
55. data->cleanupHandle = nullptr;
56. // 分配内存并复制字符串数据
57. const char *testDataStr = "TestNapiAsyncCleanUpHook";
58. data->testData = strdup(testDataStr);
59. if (data->testData == nullptr) {
60. free(data);
61. napi_throw_error(env, nullptr, "Test Node-API data->testData is nullptr");
62. return nullptr;
63. }
64. // 添加异步清理钩子函数
65. napi_status status = napi_add_async_cleanup_hook(env, AsyncCleanup, data, &data->cleanupHandle);
66. if (status != napi_ok) {
67. free(data->testData);
68. free(data);
69. napi_throw_error(env, nullptr, "Test Node-API napi_add_async_cleanup_hook failed");
70. return nullptr;
71. }
72. napi_value result = nullptr;
73. napi_get_boolean(env, true, &result);
74. return result;
75. }
```

由于需要包含“uv.h”库，所以需要在CMakeLists文件中添加配置：

```
1. // CMakeLists.txt
2. target_link_libraries(entry PUBLIC libace_napi.z.so libuv.so)
```

接口声明

```
1. export const napiAsyncCleanUpHook: () => boolean | undefined;
```

ArkTS侧示例代码

```
1. try {
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_add_async_cleanup_hook: %{public}s',
3. testNapi.napiAsyncCleanUpHook());
4. // ...
5. } catch (error) {
6. hilog.error(0x0000, 'testTag',
7. 'Test Node-API napi_add_async_cleanup_hook error.message: %{public}s',
8. error.message);
9. // ...
10. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
