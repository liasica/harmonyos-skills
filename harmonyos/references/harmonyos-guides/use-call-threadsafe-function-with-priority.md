---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-call-threadsafe-function-with-priority
title: 使用Node-API接口从异步线程向ArkTS线程投递指定优先级和入队方式的任务
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口从异步线程向ArkTS线程投递指定优先级和入队方式的任务
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:35848827e8cf6fee29615ac1cb7c1bc63e090d6baccf7d6e3ea3474be5a67e3e
---

Node-API中的napi\_call\_threadsafe\_function\_with\_priority接口的功能是从异步线程向ArkTS线程投递指定优先级和入队方式的任务，底层队列会根据任务的优先级和入队方式来处理任务。

## 函数说明

```cpp
napi_status napi_call_threadsafe_function_with_priority(napi_threadsafe_function func, void *data,
                                                        napi_task_priority priority, bool isTail);
```

| 参数 | 说明 |
| --- | --- |
| func | 线程安全方法 |
| data | 异步线程期望传递给主线程的数据 |
| priority | 指定任务的优先级[napi\_task\_priority](napi-data-types-interfaces.md#线程安全任务优先级) |
| isTail | 指定任务的入队方式，true代表任务从队列的尾部入队，false代表任务从队列的头部入队 |

## 场景介绍

异步线程向ArkTS主线程中投递的任务需要根据任务指定的优先级和入队方式进行处理。

## 调用异步的ArkTS接口示例

### 示例代码

* 功能实现

  ```
  #include "napi/native_api.h"
  // ...
  #include <hilog/log.h>
  // ...
  static constexpr int INT_ARG_2 = 2; // 入参索引
  static constexpr int INT_ARG_12 = 12; // 入参索引
  static constexpr int INT_ARG_15 = 15; // 入参索引
  // ...
  struct CallbackData {
      napi_threadsafe_function tsfn;
      napi_async_work work;
  };
  static void CallJs(napi_env env, napi_value jsCb, void *context, void *data)
  {
      if (env == nullptr) {
          return;
      }

      napi_handle_scope scope = nullptr;
      napi_status status = napi_open_handle_scope(env, &scope);
      if (status != napi_ok) {
          return;
      }

      napi_value resultNumber = nullptr;
      napi_value undefined = nullptr;
      napi_get_undefined(env, &undefined);
      napi_value number1 = nullptr;
      napi_create_int32(env, INT_ARG_12, &number1);
      napi_value number2 = nullptr;
      napi_create_int32(env, INT_ARG_15, &number2);
      napi_value argv[2] = {number1, number2};
      napi_call_function(env, undefined, jsCb, INT_ARG_2, argv, &resultNumber);
      int32_t res = 0;
      // 获取resultNumber对应的int32值
      napi_get_value_int32(env, resultNumber, &res);

      napi_close_handle_scope(env, scope);
  }

  // 异步线程中调用该接口向ArkTS线程投递指定优先级和入队方式的任务
  static void ExecuteWork(napi_env env, void *data)
  {
      CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
      // 投递指定优先级为napi_priority_idle，入队方式为队列尾部入队的任务
      napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_idle, true);
      // 投递指定优先级为napi_priority_low，入队方式为队列尾部入队的任务
      napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_low, true);
      // 投递指定优先级为napi_priority_high，入队方式为队列尾部入队的任务
      napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_high, true);
      // 投递指定优先级为napi_priority_immediate，入队方式为队列尾部入队的任务
      napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_immediate, true);
      // 投递指定优先级为napi_priority_high，入队方式为队列头部入队的任务
      napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_high, false);
  }

  static void WorkComplete(napi_env env, napi_status status, void *data)
  {
      CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
      if (callbackData->tsfn != nullptr) {
          napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
          callbackData->tsfn = nullptr;
      }
      if (callbackData->work != nullptr) {
          napi_delete_async_work(env, callbackData->work);
          callbackData->work = nullptr;
      }
      delete callbackData;
  }

  static napi_value CallThreadSafeWithPriority(napi_env env, napi_callback_info info)
  {
      size_t argc = 1;
      napi_value jsCb = nullptr;
      CallbackData *callbackData = new CallbackData();
      napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);
      napi_value resourceName = nullptr;
      napi_create_string_utf8(env, "Thread-safe Function Demo", NAPI_AUTO_LENGTH, &resourceName);
      if (napi_create_threadsafe_function(env, jsCb, nullptr, resourceName, 0, 1, nullptr, nullptr, nullptr, CallJs,
                                          &callbackData->tsfn) != napi_ok) {
          delete callbackData;
          return nullptr;
      }
      // 创建一个异步任务对象
      if (napi_create_async_work(env, nullptr, resourceName,
                                 ExecuteWork, WorkComplete, callbackData, &callbackData->work) != napi_ok) {
          if (callbackData->tsfn != nullptr) {
              napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
          }
          delete callbackData;
          return nullptr;
      }
      if (napi_queue_async_work(env, callbackData->work) != napi_ok) {
          if (callbackData->tsfn != nullptr) {
              napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
          }
          napi_delete_async_work(env, callbackData->work);
          delete callbackData;
          return nullptr;
      }
      return nullptr;
  }
  ```
* 模块注册

  ```
  // 注册模块接口
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          { "callThreadSafeWithPriority", nullptr, CallThreadSafeWithPriority, nullptr, nullptr, nullptr, napi_default, nullptr }
      };
      napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
      return exports;
  }
  EXTERN_C_END

  static napi_module nativeModule = {
      .nm_version = 1,
      .nm_flags = 0,
      .nm_filename = nullptr,
      .nm_register_func = Init,
      .nm_modname = "entry",
      .nm_priv = nullptr,
      .reserved = { 0 },
  };

  extern "C" __attribute__((constructor)) void RegisterEntryModule()
  {
      napi_module_register(&nativeModule);
  }
  ```
* 接口声明

  ```typescript
  // index.d.ts
  export const callThreadSafeWithPriority: (cb: (a: number, b: number) => number) => void;
  ```
* 编译配置

  CMakeLists.txt文件需要按照如下配置

  ```text
  # the minimum version of CMake.
  cmake_minimum_required(VERSION 3.5.0)
  project(MyApplication3)

  set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  if(DEFINED PACKAGE_FIND_FILE)
      include(${PACKAGE_FIND_FILE})
  endif()
  add_definitions( "-DLOG_TAG=\"LOG_TAG\"" )
  include_directories(${NATIVERENDER_ROOT_PATH}
                      ${NATIVERENDER_ROOT_PATH}/include)

  add_library(entry SHARED napi_init.cpp)
  target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
  ```
* ArkTS导入头文件

  ```typescript
  import testNapi from 'libentry.so';
  ```
* ArkTS代码示例

  ```typescript
  // index.ets
  let callback = (a: number, b: number): number => {
    console.info('result is ' + (a + b))
    return a + b;
  }
  testNapi.callThreadSafeWithPriority(callback);
  ```
