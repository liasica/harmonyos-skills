---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-thread-safety
title: 使用Node-API接口进行线程安全开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口进行线程安全开发
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4bb10d7b9d51bb3b7d00a7381c6bc12c1e8062a4b8d6411acb2bf37b97f8792e
---

## 场景介绍

[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)是Node-API接口之一，用于创建一个线程安全的JavaScript函数。该函数主要用于在多个线程之间共享和调用，避免竞争条件和死锁。包含以下场景：

* 异步计算：若需执行耗时的计算或IO操作，可创建线程安全的函数，在另一线程中完成计算或IO操作，避免阻塞主线程，提升程序响应速度。
* 数据共享：若多个线程需访问同一份数据，可以创建一个线程安全的函数，避免数据进行读写操作时发生竞争条件或死锁等问题。
* 多线程编程：若需要进行多线程编程，可以创建一个线程安全的函数，确保多个线程之间的通信和同步操作正确。

## 使用示例

1. CMakeLists.txt配置

   ```txt
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(MyApplication3)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()
   add_definitions( "-DLOG_DOMAIN=0xd0d0" )
   add_definitions( "-DLOG_TAG=\"testTag\"" )
   include_directories(${NATIVERENDER_ROOT_PATH}
                       ${NATIVERENDER_ROOT_PATH}/include)

   add_library(entry SHARED napi_init.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)

   add_library(entry1 SHARED thread_safety.cpp)
   target_link_libraries(entry1 PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
2. 定义线程安全函数在Native入口。

   ```
   #include "napi/native_api.h"
   #include "hilog/log.h"
   #include <future>

   static constexpr int INT_ARG_2 = 2; // 入参索引
   static constexpr int INT_BUF_32 = 32; // 入参索引

   struct CallbackData {
       napi_threadsafe_function tsfn;
       napi_async_work work;
   };

   // 在工作线程中调用ExecuteWork并执行线程安全函数
   static void ExecuteWork(napi_env env, void *data)
   {
       CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
       std::promise<std::string> promise;
       auto future = promise.get_future();
       napi_acquire_threadsafe_function(callbackData->tsfn);
       napi_call_threadsafe_function(callbackData->tsfn, &promise, napi_tsfn_nonblocking);
       napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
       try {
           auto result = future.get();
           OH_LOG_INFO(LOG_APP, "XXX, Result from JS %{public}s", result.c_str());
       } catch (const std::exception &e) {
           OH_LOG_INFO(LOG_APP, "XXX, Result from JS %{public}s", e.what());
       }
   }

   static napi_value ResolvedCallback(napi_env env, napi_callback_info info)
   {
       void *data = nullptr;
       size_t argc = 1;
       napi_value argv[1];
       if (napi_get_cb_info(env, info, &argc, argv, nullptr, &data) != napi_ok) {
           return nullptr;
       }
       size_t result = 0;
       char buf[32] = {0};
       napi_get_value_string_utf8(env, argv[0], buf, INT_BUF_32, &result);
       reinterpret_cast<std::promise<std::string> *>(data)->set_value(std::string(buf));
       return nullptr;
   }

   static napi_value RejectedCallback(napi_env env, napi_callback_info info)
   {
       void *data = nullptr;
       if (napi_get_cb_info(env, info, nullptr, nullptr, nullptr, &data) != napi_ok) {
           return nullptr;
       }
       reinterpret_cast<std::promise<std::string> *>(data)->set_exception(
           std::make_exception_ptr(std::runtime_error("Error in jsCallback")));
       return nullptr;
   }

   static void CallJs(napi_env env, napi_value jsCb, void *context, void *data)
   {
       if (env == nullptr) {
           return;
       }
       napi_value undefined = nullptr;
       napi_value promise = nullptr;
       napi_get_undefined(env, &undefined);
       napi_call_function(env, undefined, jsCb, 0, nullptr, &promise);
       napi_value thenFunc = nullptr;
       if (napi_get_named_property(env, promise, "then", &thenFunc) != napi_ok) {
           return;
       }
       napi_value resolvedCallback;
       napi_value rejectedCallback;
       napi_create_function(env, "resolvedCallback", NAPI_AUTO_LENGTH, ResolvedCallback, data, &resolvedCallback);
       napi_create_function(env, "rejectedCallback", NAPI_AUTO_LENGTH, RejectedCallback, data, &rejectedCallback);
       napi_value argv[2] = {resolvedCallback, rejectedCallback};
       napi_call_function(env, promise, thenFunc, INT_ARG_2, argv, nullptr);
   }

   // 任务执行完成后，进行资源清理回收
   static void WorkComplete(napi_env env, napi_status status, void *data)
   {
       CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
       napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
       napi_delete_async_work(env, callbackData->work);
       callbackData->tsfn = nullptr;
       callbackData->work = nullptr;
       delete callbackData;
   }

   static napi_value StartThread(napi_env env, napi_callback_info info)
   {
       CallbackData *callbackData = new CallbackData();
       size_t argc = 1;
       napi_value jsCb = nullptr;
       napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);

       // 创建一个线程安全函数
       napi_value resourceName = nullptr;
       napi_create_string_utf8(env, "Thread-safe Function Demo", NAPI_AUTO_LENGTH, &resourceName);
       napi_create_threadsafe_function(env, jsCb, nullptr, resourceName, 0, 1, callbackData, nullptr, callbackData, CallJs,
                                       &callbackData->tsfn);

       // 创建一个异步任务
       // ExecuteWork会执行在一个由libuv创建的非JS线程上
       // 此处使用napi_create_async_work是为了模拟在非JS线程场景使用napi_call_threadsafe_function接口向JS线程提交任务
       napi_create_async_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work);

       // 将异步任务加入到异步队列中
       napi_queue_async_work(env, callbackData->work);
       return nullptr;
   }
   ```
3. 模块注册。

   ```
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           {"startThread", nullptr, StartThread, nullptr, nullptr, nullptr, napi_default, nullptr}
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END

   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "entry1",
       .nm_priv = ((void *)0),
       .reserved = {0},
   };

   extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
4. ArkTS侧示例代码

   ```typescript
   export const startThread: (a: () => Promise<string>) => void;
   ```

   导入头文件

   ```ts
   import nativeModule from 'libentry1.so';
   ```

   ```typescript
   // index.ets
   let callback = (): Promise<string> => {
     return new Promise((resolve) => {
       setTimeout(() => {
         resolve('string from promise');
       }, 5000);
     });
   }
   nativeModule.startThread(callback);
   ```

## 子线程交互场景介绍

* napi\_threadsafe\_function在主线程和子线程使用并无差异，下面是子线程的使用示例。

### 基于[Worker](worker-introduction.md)实现的C++子线程与ArkTS子线程交互场景

1. CMakeLists.txt配置

   ```txt
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(MyApplication3)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()
   add_definitions( "-DLOG_DOMAIN=0xd0d0" )
   add_definitions( "-DLOG_TAG=\"testTag\"" )
   include_directories(${NATIVERENDER_ROOT_PATH}
                       ${NATIVERENDER_ROOT_PATH}/include)

   add_library(entry SHARED napi_init.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)

   add_library(entry1 SHARED thread_safety.cpp)
   target_link_libraries(entry1 PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
2. 在Native入口定义线程安全函数并创建子线程。

   ```
   #include "napi/native_api.h"
   #include "hilog/log.h"
   #include <future>
   // ...

   struct TsfnContext {
       napi_ref callbackRef;
   };

   struct ThreadData {
       std::string inputStr;
       napi_threadsafe_function tsfn;
   };

   // C++子线程
   void NativeThread(void* arg)
   {
       auto* data = static_cast<ThreadData*>(arg);
       OH_LOG_INFO(LOG_APP, "[C++ SubThread] Received from %{public}s\n", data->inputStr.c_str());
       std::string str = "Hello from C++!";
       std::string msg = "Echo of " + str;
       char* cstr = strdup(msg.c_str());
       napi_call_threadsafe_function(data->tsfn, cstr, napi_tsfn_nonblocking);
       napi_release_threadsafe_function(data->tsfn, napi_tsfn_release);
       delete data;
   }

   // 在 JS 线程中实际执行的回调
   void CallJsCallback(napi_env env, napi_value jsCallback, void* context, void* data)
   {
       if (data == nullptr) {
           return;
       }
       char* message = static_cast<char*>(data);
       napi_value jsStr;
       napi_create_string_utf8(env, message, NAPI_AUTO_LENGTH, &jsStr);
       napi_value global;
       napi_get_global(env, &global);
       napi_value result;
       napi_call_function(env, global, jsCallback, 1, &jsStr, &result);
       free(message);
   }

   // tsfn销毁时的清理回调
   void TsfnFinalizeCallback(napi_env env, void* finalizeData, void* finalizeHint)
   {
       TsfnContext* ctx = static_cast<TsfnContext*>(finalizeData);
       if (ctx && ctx->callbackRef) {
           napi_delete_reference(env, ctx->callbackRef);
           delete ctx;
       }
   }

   // ArkTS 调用的入口函数
   napi_value StartWithCallback(napi_env env, napi_callback_info info)
   {
       size_t argc = 2;
       napi_value args[2];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       size_t length = 0;
       napi_status status = napi_get_value_string_utf8(env, args[0], nullptr, 0, &length);
       if (status != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "napi_get_value_string_utf8 failed");
           return nullptr;
       }
       char* inputStr = new char[length + 1];
       std::fill(inputStr, inputStr + (length + 1), 0);
       status = napi_get_value_string_utf8(env, args[0], inputStr, length + 1, &length);
       if (status != napi_ok) {
           if (inputStr) {
               delete[] inputStr;
           }
           OH_LOG_ERROR(LOG_APP, "napi_get_value_string_utf8 failed");
           return nullptr;
       }
       std::string inputString(inputStr, length);
       delete[] inputStr;
       TsfnContext* ctx = new TsfnContext();
       napi_create_reference(env, args[1], 1, &ctx->callbackRef);
       napi_value resourceName;
       napi_create_string_utf8(env, "TSFN_WorkerToCpp", NAPI_AUTO_LENGTH, &resourceName);
       napi_threadsafe_function tsfn;
       napi_create_threadsafe_function(env, args[1], nullptr, resourceName,
                                       0, 1, ctx, TsfnFinalizeCallback, nullptr, CallJsCallback, &tsfn);
       auto* threadData = new ThreadData{std::move(inputString), tsfn};
       std::thread nativethread(NativeThread, threadData);
       nativethread.detach();
       return nullptr;
   }
   ```
3. 模块注册。

   ```
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           {"startWithCallback", nullptr, StartWithCallback, nullptr, nullptr, nullptr, napi_default, nullptr}
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END

   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "entry1",
       .nm_priv = ((void *)0),
       .reserved = {0},
   };

   extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
4. DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建 "Worker" 为例。

   ```json5
   "buildOption": {
     "sourceOption": {
       "workers": [
         "./src/main/ets/workers/Worker.ets"
        ]
     },
   }
   ```
5. Worker线程示例代码。

   ```typescript
   // entry/src/main/ets/workers/Worker.ets

   import nativeModule from 'libentry1.so';
   import { worker, MessageEvents } from '@kit.ArkTS';

   const port = worker.workerPort;

   port.onmessage = (e: MessageEvents) => {
     console.info('Worker thread received:' + e.data);
     nativeModule.startWithCallback('Worker', (result: string) => {
       console.info('[Worker] Got from native:', result);
       port.postMessage(result);
     });
   }
   ```
6. 接口对应的.d.ts描述。

   ```typescript
   export const startWithCallback: (input: string, callback: (msg: string) => void) => void;
   ```
7. ArkTS侧调用接口。

   ```ts
   import nativeModule from 'libentry1.so';
   import { worker } from '@kit.ArkTS';
   ```

   ```typescript
   // index.ets
   const wk = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
   wk.postMessage('Start');
   wk.onmessage = (msg) => {
     console.info('[Main] Received:', msg.data);
     wk.terminate();
   }
   ```

   ```txt
   运行结果：
   Worker thread received:Start
   [C++ SubThread] Received from Worker
   [Worker] Got from native: Echo of Hello from C++!
   [Main] Received: Echo of Hello from C++!
   ```

### 基于[Taskpool](taskpool-introduction.md)实现的C++子线程与ArkTS子线程交互场景

1. native侧实现代码以及模块注册与“基于Worker实现的C++子线程与ArkTS子线程交互场景”一致，可直接复用。
2. ArkTS侧示例代码。

   ```ts
   import nativeModule from 'libentry1.so';
   import { taskpool } from '@kit.ArkTS';

   @Concurrent
   function nativeCall(input : string): void {
     console.info('Taskpool thread received:%s', input);
     nativeModule.startWithCallback('Taskpool', (result: string) => {
       console.info('[Taskpool] Got from native:', result);
     });
   }

   async function testTaskpool() : Promise<void> {
     try {
       const task = new taskpool.Task(nativeCall, 'Start');
       await taskpool.execute(task);
     } catch (e) {
       console.error(`Taskpool execute error: ${e}`);
     }
   }
   ```

   ```typescript
   // index.ets
   testTaskpool();
   ```

   ```txt
   运行结果：
   Taskpool thread received:Start
   [C++ SubThread] Received from Taskpool
   [Taskpool] Got from native: Echo of Hello from C++!
   ```
