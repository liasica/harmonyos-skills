---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-event-loop
title: 使用扩展的Node-API接口在异步线程中运行和停止事件循环
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口在异步线程中运行和停止事件循环
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:478ef7bd3bf80088272246ae8d4a4760389092e6fea2548b162eba4d718af736
---

## 场景介绍

开发者在自己创建的ArkTS运行环境中调用异步的ArkTS接口时，可以通过使用Node-API中的扩展接口napi\_run\_event\_loop和napi\_stop\_event\_loop来运行和停止ArkTS实例中的事件循环。

## 调用异步的ArkTS接口示例

调用的ArkTS接口为异步接口时，需要通过扩展接口napi\_run\_event\_loop将异步线程中的事件循环运行起来，底层事件队列中的异步任务将被处理执行。当前Node-API扩展了两种事件循环模式来运行异步线程的事件循环，分别为napi\_event\_mode\_nowait模式和napi\_event\_mode\_default模式。

如果使用napi\_event\_mode\_nowait模式运行底层事件循环，系统会尝试从底层的事件队列中取出一个任务并处理，完成之后事件循环停止，如果底层的事件队列中没有任务，事件循环会立刻停止，当前的异步线程不会被阻塞；

如果使用napi\_event\_mode\_default模式来运行底层事件循环，系统会阻塞当前的线程，同时会一直尝试从事件队列中获取任务并执行处理这些任务。如果不想当前线程继续被阻塞，可以使用扩展接口napi\_stop\_event\_loop将正在运行的事件循环停止。

### 示例代码

* 功能实现

  ```
  #include "napi/native_api.h"
  #include <pthread.h>
  #include <hilog/log.h>
  #include <napi/common.h>
  static constexpr int INT_ARG_2 = 2; // 入参索引
  // ...
  static napi_value ResolvedCallback(napi_env env, napi_callback_info info)
  {
      napi_stop_event_loop(env);
      return nullptr;
  }

  static napi_value RejectedCallback(napi_env env, napi_callback_info info)
  {
      napi_stop_event_loop(env);
      return nullptr;
  }

  static bool CallSetTimeoutWithCallbacks(napi_env env, napi_value objectUtils)
  {
      napi_value setTimeout = nullptr;
      napi_value promise = nullptr;

      if (napi_get_named_property(env, objectUtils, "SetTimeout", &setTimeout) != napi_ok) {
          return false;
      }
      if (napi_call_function(env, objectUtils, setTimeout, 0, nullptr, &promise) != napi_ok) {
          return false;
      }

      napi_value theFunc = nullptr;
      if (napi_get_named_property(env, promise, "then", &theFunc) != napi_ok) {
          return false;
      }

      napi_value resolvedCallback = nullptr;
      napi_value rejectedCallback = nullptr;
      if (napi_create_function(env, "resolvedCallback", NAPI_AUTO_LENGTH,
                               ResolvedCallback, nullptr, &resolvedCallback) != napi_ok) {
          return false;
      }
      if (napi_create_function(env, "rejectedCallback", NAPI_AUTO_LENGTH,
                               RejectedCallback, nullptr, &rejectedCallback) != napi_ok) {
          return false;
      }
      napi_value argv[2] = {resolvedCallback, rejectedCallback};
      if (napi_call_function(env, promise, theFunc, INT_ARG_2, argv, nullptr) != napi_ok) {
          return false;
      }
      return true;
  }

  static void *RunEventLoopFunc(void *arg)
  {
      // 1. 创建ArkTS实例
      napi_env env = nullptr;
      napi_status ret = napi_create_ark_runtime(&env);
      if (ret != napi_ok) {
          return nullptr;
      }

      napi_handle_scope scope = nullptr;
      napi_open_handle_scope(env, &scope);

      // 2. 加载自定义的模块
      napi_value objectUtils = nullptr;
      // 'com.example.myapplication' 为当前应用的bundleName
      ret = napi_load_module_with_info(env, "entry/src/main/ets/pages/ObjectUtils", "com.example.myapplication/entry",
                                       &objectUtils);
      if (ret != napi_ok) {
          OH_LOG_INFO(LOG_APP, "Failed to load module");
          napi_close_handle_scope(env, scope);
          napi_destroy_ark_runtime(&env);
          return nullptr;
      }

      // 3. 调用异步SetTimeout接口
      if (!CallSetTimeoutWithCallbacks(env, objectUtils)) {
          napi_close_handle_scope(env, scope);
          napi_destroy_ark_runtime(&env);
          return nullptr;
      }

      auto flag = reinterpret_cast<bool *>(arg);
      if (*flag == true) {
          if (napi_run_event_loop(env, napi_event_mode_default) != napi_ok) {
              napi_close_handle_scope(env, scope);
              napi_destroy_ark_runtime(&env);
              return nullptr;
          }
      } else {
          if (napi_run_event_loop(env, napi_event_mode_nowait) != napi_ok) {
              napi_close_handle_scope(env, scope);
              napi_destroy_ark_runtime(&env);
              return nullptr;
          }
      }

      if (scope != nullptr) {
          napi_close_handle_scope(env, scope);
          scope = nullptr;
      }
      if (env != nullptr) {
          napi_status destroy_ret = napi_destroy_ark_runtime(&env);
          if (destroy_ret != napi_ok) {
              OH_LOG_INFO(LOG_APP, "Failed to destroy ark runtime");
          }
          env = nullptr;
      }
      return nullptr;
  }

  static napi_value RunEventLoop(napi_env env, napi_callback_info info)
  {
      pthread_t tid;
      size_t argc = 1;
      napi_value argv[1] = { nullptr };
      napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

      bool flag = false;
      napi_get_value_bool(env, argv[0], &flag);
      // 创建异步线程
      pthread_create(&tid, nullptr, RunEventLoopFunc, &flag);
      pthread_join(tid, nullptr);

      return nullptr;
  }
  ```
* 模块注册

  ```
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          { "runEventLoop", nullptr, RunEventLoop, nullptr, nullptr, nullptr, napi_default, nullptr }
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
  export const runEventLoop: (isDefault: boolean) => object;
  ```
* 编译配置

1. CMakeLists.txt文件需要按照如下配置

   ```text
   // CMakeLists.txt
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
2. 需要在模块的build-profile.json5文件中进行以下配置

   ```json5
     "buildOption": {
       "arkOptions" : {
         "runtimeOnly" : {
           "sources": [
             "./src/main/ets/pages/ObjectUtils.ets"
           ]
         }
       },
   // ...
     },
   ```

* ArkTS代码示例

  ```typescript
  // 导入头文件
  import testNapi from 'libentry.so'
  ```

  ```typescript
  // index.ets
  testNapi.runEventLoop(true);
  ```

  ```typescript
  export function SetTimeout(): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.info('set timer delay 1s');
        // attempt to stop the event loop at napi terminal
        resolve();
      }, 1000)
    })
  }
  ```
