---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-thread-safety
title: 使用Node-API接口进行线程安全开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口进行线程安全开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74d2f12a14921136dc62e02310aa8b663965bb97c0e0b3a76554f07505f4543b
---

## 场景介绍

[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)是Node-API接口之一，用于创建一个线程安全的JavaScript函数。该函数主要用于在多个线程之间共享和调用，避免竞争条件和死锁。包含以下场景：

* 异步计算：若需执行耗时的计算或IO操作，可创建线程安全的函数，在另一线程中完成计算或IO操作，避免阻塞主线程，提升程序响应速度。
* 数据共享：若多个线程需访问同一份数据，可以创建一个线程安全的函数，避免数据进行读写操作时发生竞争条件或死锁等问题。
* 多线程编程：若需要进行多线程编程，可以创建一个线程安全的函数，确保多个线程之间的通信和同步操作正确。

## 使用示例

1. CMakeLists.txt配置

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(MyApplication3)

   5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(${PACKAGE_FIND_FILE})
   9. endif()
   10. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
   11. add_definitions( "-DLOG_TAG=\"testTag\"" )
   12. include_directories(${NATIVERENDER_ROOT_PATH}
   13. ${NATIVERENDER_ROOT_PATH}/include)

   15. add_library(entry SHARED napi_init.cpp)
   16. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)

   18. add_library(entry1 SHARED thread_safety.cpp)
   19. target_link_libraries(entry1 PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
2. 定义线程安全函数在Native入口。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include <future>

   5. static constexpr int INT_ARG_2 = 2; // 入参索引
   6. static constexpr int INT_BUF_32 = 32; // 入参索引

   8. struct CallbackData {
   9. napi_threadsafe_function tsfn;
   10. napi_async_work work;
   11. };

   13. // 在工作线程中调用ExecuteWork并执行线程安全函数
   14. static void ExecuteWork(napi_env env, void *data)
   15. {
   16. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
   17. std::promise<std::string> promise;
   18. auto future = promise.get_future();
   19. napi_acquire_threadsafe_function(callbackData->tsfn);
   20. napi_call_threadsafe_function(callbackData->tsfn, &promise, napi_tsfn_nonblocking);
   21. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
   22. try {
   23. auto result = future.get();
   24. OH_LOG_INFO(LOG_APP, "XXX, Result from JS %{public}s", result.c_str());
   25. } catch (const std::exception &e) {
   26. OH_LOG_INFO(LOG_APP, "XXX, Result from JS %{public}s", e.what());
   27. }
   28. }

   30. static napi_value ResolvedCallback(napi_env env, napi_callback_info info)
   31. {
   32. void *data = nullptr;
   33. size_t argc = 1;
   34. napi_value argv[1];
   35. if (napi_get_cb_info(env, info, &argc, argv, nullptr, &data) != napi_ok) {
   36. return nullptr;
   37. }
   38. size_t result = 0;
   39. char buf[32] = {0};
   40. napi_get_value_string_utf8(env, argv[0], buf, INT_BUF_32, &result);
   41. reinterpret_cast<std::promise<std::string> *>(data)->set_value(std::string(buf));
   42. return nullptr;
   43. }

   45. static napi_value RejectedCallback(napi_env env, napi_callback_info info)
   46. {
   47. void *data = nullptr;
   48. if (napi_get_cb_info(env, info, nullptr, nullptr, nullptr, &data) != napi_ok) {
   49. return nullptr;
   50. }
   51. reinterpret_cast<std::promise<std::string> *>(data)->set_exception(
   52. std::make_exception_ptr(std::runtime_error("Error in jsCallback")));
   53. return nullptr;
   54. }

   56. static void CallJs(napi_env env, napi_value jsCb, void *context, void *data)
   57. {
   58. if (env == nullptr) {
   59. return;
   60. }
   61. napi_value undefined = nullptr;
   62. napi_value promise = nullptr;
   63. napi_get_undefined(env, &undefined);
   64. napi_call_function(env, undefined, jsCb, 0, nullptr, &promise);
   65. napi_value thenFunc = nullptr;
   66. if (napi_get_named_property(env, promise, "then", &thenFunc) != napi_ok) {
   67. return;
   68. }
   69. napi_value resolvedCallback;
   70. napi_value rejectedCallback;
   71. napi_create_function(env, "resolvedCallback", NAPI_AUTO_LENGTH, ResolvedCallback, data, &resolvedCallback);
   72. napi_create_function(env, "rejectedCallback", NAPI_AUTO_LENGTH, RejectedCallback, data, &rejectedCallback);
   73. napi_value argv[2] = {resolvedCallback, rejectedCallback};
   74. napi_call_function(env, promise, thenFunc, INT_ARG_2, argv, nullptr);
   75. }

   77. // 任务执行完成后，进行资源清理回收
   78. static void WorkComplete(napi_env env, napi_status status, void *data)
   79. {
   80. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
   81. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
   82. napi_delete_async_work(env, callbackData->work);
   83. callbackData->tsfn = nullptr;
   84. callbackData->work = nullptr;
   85. delete callbackData;
   86. }

   88. static napi_value StartThread(napi_env env, napi_callback_info info)
   89. {
   90. CallbackData *callbackData = new CallbackData();
   91. size_t argc = 1;
   92. napi_value jsCb = nullptr;
   93. napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);

   95. // 创建一个线程安全函数
   96. napi_value resourceName = nullptr;
   97. napi_create_string_utf8(env, "Thread-safe Function Demo", NAPI_AUTO_LENGTH, &resourceName);
   98. napi_create_threadsafe_function(env, jsCb, nullptr, resourceName, 0, 1, callbackData, nullptr, callbackData, CallJs,
   99. &callbackData->tsfn);

   101. // 创建一个异步任务
   102. // ExecuteWork会执行在一个由libuv创建的非JS线程上
   103. // 此处使用napi_create_async_work是为了模拟在非JS线程场景使用napi_call_threadsafe_function接口向JS线程提交任务
   104. napi_create_async_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work);

   106. // 将异步任务加入到异步队列中
   107. napi_queue_async_work(env, callbackData->work);
   108. return nullptr;
   109. }
   ```
3. 模块注册。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. {"startThread", nullptr, StartThread, nullptr, nullptr, nullptr, napi_default, nullptr}
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   10. EXTERN_C_END

   12. static napi_module demoModule = {
   13. .nm_version = 1,
   14. .nm_flags = 0,
   15. .nm_filename = nullptr,
   16. .nm_register_func = Init,
   17. .nm_modname = "entry1",
   18. .nm_priv = ((void *)0),
   19. .reserved = {0},
   20. };

   22. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
4. ArkTS侧示例代码

   ```
   1. export const startThread: (a: () => Promise<string>) => void;
   ```

   导入头文件

   ```
   1. import nativeModule from 'libentry1.so';
   ```

   ```
   1. // index.ets
   2. let callback = (): Promise<string> => {
   3. return new Promise((resolve) => {
   4. setTimeout(() => {
   5. resolve('string from promise');
   6. }, 5000);
   7. });
   8. }
   9. nativeModule.startThread(callback);
   ```

## 子线程交互场景介绍

* napi\_threadsafe\_function在主线程和子线程使用并无差异，下面是子线程的使用示例。

### 基于[Worker](worker-introduction.md)实现的C++子线程与ArkTS子线程交互场景

1. CMakeLists.txt配置

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(MyApplication3)

   5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(${PACKAGE_FIND_FILE})
   9. endif()
   10. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
   11. add_definitions( "-DLOG_TAG=\"testTag\"" )
   12. include_directories(${NATIVERENDER_ROOT_PATH}
   13. ${NATIVERENDER_ROOT_PATH}/include)

   15. add_library(entry SHARED napi_init.cpp)
   16. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)

   18. add_library(entry1 SHARED thread_safety.cpp)
   19. target_link_libraries(entry1 PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
2. 在Native入口定义线程安全函数并创建子线程。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include <future>
   4. // ...

   6. struct TsfnContext {
   7. napi_ref callbackRef;
   8. };

   10. struct ThreadData {
   11. std::string inputStr;
   12. napi_threadsafe_function tsfn;
   13. };

   15. // C++子线程
   16. void NativeThread(void* arg)
   17. {
   18. auto* data = static_cast<ThreadData*>(arg);
   19. OH_LOG_INFO(LOG_APP, "[C++ SubThread] Received from Worker: %{public}s\n", data->inputStr.c_str());
   20. std::string str = "Hello from C++!";
   21. std::string msg = "Echo of " + str;
   22. char* cstr = strdup(msg.c_str());
   23. napi_call_threadsafe_function(data->tsfn, cstr, napi_tsfn_nonblocking);
   24. napi_release_threadsafe_function(data->tsfn, napi_tsfn_release);
   25. delete data;
   26. }

   28. // 在 JS 线程中实际执行的回调
   29. void CallJsCallback(napi_env env, napi_value jsCallback, void* context, void* data)
   30. {
   31. if (data == nullptr) {
   32. return;
   33. }
   34. char* message = static_cast<char*>(data);
   35. napi_value jsStr;
   36. napi_create_string_utf8(env, message, NAPI_AUTO_LENGTH, &jsStr);
   37. napi_value global;
   38. napi_get_global(env, &global);
   39. napi_value result;
   40. napi_call_function(env, global, jsCallback, 1, &jsStr, &result);
   41. free(message);
   42. }

   44. // tsfn销毁时的清理回调
   45. void TsfnFinalizeCallback(napi_env env, void* finalizeData, void* finalizeHint)
   46. {
   47. TsfnContext* ctx = static_cast<TsfnContext*>(finalizeData);
   48. if (ctx && ctx->callbackRef) {
   49. napi_delete_reference(env, ctx->callbackRef);
   50. delete ctx;
   51. }
   52. }

   54. // ArkTS 调用的入口函数
   55. napi_value StartWithCallback(napi_env env, napi_callback_info info)
   56. {
   57. size_t argc = 2;
   58. napi_value args[2];
   59. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   60. size_t length = 0;
   61. napi_status status = napi_get_value_string_utf8(env, args[0], nullptr, 0, &length);
   62. if (status != napi_ok) {
   63. OH_LOG_ERROR(LOG_APP, "napi_get_value_string_utf8 failed");
   64. return nullptr;
   65. }
   66. char* inputStr = new char[length + 1];
   67. std::fill(inputStr, inputStr + (length + 1), 0);
   68. status = napi_get_value_string_utf8(env, args[0], inputStr, length + 1, &length);
   69. if (status != napi_ok) {
   70. if (inputStr) {
   71. delete[] inputStr;
   72. }
   73. OH_LOG_ERROR(LOG_APP, "napi_get_value_string_utf8 failed");
   74. return nullptr;
   75. }
   76. std::string inputString(inputStr, length);
   77. delete[] inputStr;
   78. TsfnContext* ctx = new TsfnContext();
   79. napi_create_reference(env, args[1], 1, &ctx->callbackRef);
   80. napi_value resourceName;
   81. napi_create_string_utf8(env, "TSFN_WorkerToCpp", NAPI_AUTO_LENGTH, &resourceName);
   82. napi_threadsafe_function tsfn;
   83. napi_create_threadsafe_function(env, args[1], nullptr, resourceName,
   84. 0, 1, ctx, TsfnFinalizeCallback, nullptr, CallJsCallback, &tsfn);
   85. auto* threadData = new ThreadData{std::move(inputString), tsfn};
   86. std::thread nativethread(NativeThread, threadData);
   87. nativethread.detach();
   88. return nullptr;
   89. }
   ```
3. 模块注册。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. {"startWithCallback", nullptr, StartWithCallback, nullptr, nullptr, nullptr, napi_default, nullptr}
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   10. EXTERN_C_END

   12. static napi_module demoModule = {
   13. .nm_version = 1,
   14. .nm_flags = 0,
   15. .nm_filename = nullptr,
   16. .nm_register_func = Init,
   17. .nm_modname = "entry1",
   18. .nm_priv = ((void *)0),
   19. .reserved = {0},
   20. };

   22. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
4. DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建 "Worker" 为例。

   ```
   1. "buildOption": {
   2. "sourceOption": {
   3. "workers": [
   4. "./src/main/ets/workers/Worker.ets"
   5. ]
   6. },
   7. }
   ```
5. Worker线程示例代码。

   ```
   1. // entry/src/main/ets/workers/Worker.ets

   3. import nativeModule from 'libentry1.so';
   4. import { worker, MessageEvents } from '@kit.ArkTS';

   6. const port = worker.workerPort;

   8. port.onmessage = (e: MessageEvents) => {
   9. console.info('Worker thread received:' + e.data);
   10. nativeModule.startWithCallback('Hello', (result: string) => {
   11. console.info('[Worker] Got from native:', result);
   12. port.postMessage(result);
   13. });
   14. }
   ```
6. 接口对应的.d.ts描述。

   ```
   1. export const startWithCallback: (input: string, callback: (msg: string) => void) => void;
   ```
7. ArkTS侧调用接口。

   ```
   1. import nativeModule from 'libentry1.so';
   2. import { worker } from '@kit.ArkTS';
   ```

   ```
   1. // index.ets
   2. const wk = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
   3. wk.postMessage('Start');
   4. wk.onmessage = (msg) => {
   5. console.info('[Main] Received:', msg.data);
   6. wk.terminate();
   7. }
   ```

   ```
   1. 运行结果：
   2. Worker thread received:Start
   3. [C++ SubThread] Received from Worker: Hello
   4. [Worker] Got from native: Echo of Hello from C++!
   5. [Main] Received: Echo of Hello from C++
   ```

### 基于[Taskpool](taskpool-introduction.md)实现的C++子线程与ArkTS子线程交互场景

1. native侧实现代码以及模块注册与“基于Worker实现的C++子线程与ArkTS子线程交互场景”一致，可直接复用。
2. ArkTS侧示例代码。

   ```
   1. import nativeModule from 'libentry1.so';
   2. import { taskpool } from '@kit.ArkTS';

   4. @Concurrent
   5. function nativeCall(input : string): void {
   6. console.info('Taskpool thread received:%s', input);
   7. nativeModule.startWithCallback('Hello', (result: string) => {
   8. console.info('[Taskpool] Got from native:', result);
   9. });
   10. }

   12. async function testTaskpool() : Promise<void> {
   13. try {
   14. const task = new taskpool.Task(nativeCall, 'Start');
   15. await taskpool.execute(task);
   16. } catch (e) {
   17. console.error(`Taskpool execute error: ${e}`);
   18. }
   19. }
   ```

   ```
   1. // index.ets
   2. testTaskpool();
   ```

   ```
   1. 运行结果：
   2. Taskpool thread received:Start
   3. [C++ SubThread] Received from Worker: Hello
   4. [Taskpool] Got from native: Echo of Hello from C++!
   ```
