---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-ark-runtime
title: 使用Node-API接口创建ArkTS运行时环境
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口创建ArkTS运行时环境
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:25d69af7dcf5aaf5b3b8934de2185060501058609602be60e045936397c15b5b
---

## 场景介绍

开发者通过pthread\_create创建新线程后，可以通过napi\_create\_ark\_runtime来创建一个新的ArkTS基础运行时环境，并通过该运行时环境加载ArkTS模块。当使用结束后，开发者需要通过napi\_destroy\_ark\_runtime来销毁所创建的ArkTS基础运行时环境。

## 约束限制

一个进程最多只能创建64个运行时环境。

### 示例代码

* 接口声明

  ```typescript
  // index.d.ts
  export const createArkRuntime: () => object;
  ```
* 编译配置

  ```txt
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

  在当前模块的build-profile.json5文件中进行以下配置：

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
* 模块注册

  ```cpp
  // create_ark_runtime.cpp
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          { "createArkRuntime", nullptr, CreateArkRuntime, nullptr, nullptr, nullptr, napi_default, nullptr }
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

  extern "C" __attribute__((constructor)) void RegisterQueueWorkModule()
  {
      napi_module_register(&nativeModule);
  }
  ```
* 功能实现

  新建线程并创建ArkTS基础运行时环境，加载自定义模块请参考[napi\_load\_module\_with\_info](use-napi-load-module-with-info.md)。

  ```
  #include "napi/native_api.h"
  #include <pthread.h>
  // ...
  static void *CreateArkRuntimeFunc(void *arg)
  {
      // 1. 创建基础运行环境
      napi_env env = nullptr;
      napi_status ret = napi_create_ark_runtime(&env);
      if (ret != napi_ok) {
          return nullptr;
      }

      napi_handle_scope scope = nullptr;
      if (napi_open_handle_scope(env, &scope) != napi_ok) {
          napi_destroy_ark_runtime(&env);
          return nullptr;
      }

      // 2. 加载自定义模块
      napi_value objUtils = nullptr;
      ret = napi_load_module_with_info(env, "entry/src/main/ets/pages/ObjectUtils", "com.example.myapplication/entry",
                                       &objUtils);
      if (ret != napi_ok) {
          OH_LOG_INFO(LOG_APP, "Failed to load module");
          napi_close_handle_scope(env, scope);
          napi_destroy_ark_runtime(&env);
          return nullptr;
      }

      // 3. 使用ArkTS中的logger
      napi_value logger = nullptr;
      ret = napi_get_named_property(env, objUtils, "Logger", &logger);
      if (ret != napi_ok) {
          napi_close_handle_scope(env, scope);
          napi_destroy_ark_runtime(&env);
          return nullptr;
      }
      ret = napi_call_function(env, objUtils, logger, 0, nullptr, nullptr);
      if (ret != napi_ok) {
          napi_close_handle_scope(env, scope);
          napi_destroy_ark_runtime(&env);
          return nullptr;
      }

      napi_close_handle_scope(env, scope);

      // 4. 销毁ArkTS环境
      ret = napi_destroy_ark_runtime(&env);
      if (ret != napi_ok) {
          OH_LOG_INFO(LOG_APP, "Failed to destroy ark runtime");
      }

      return nullptr;
  }

  static napi_value CreateArkRuntime(napi_env env, napi_callback_info info)
  {
      pthread_t tid;
      pthread_create(&tid, nullptr, CreateArkRuntimeFunc, nullptr);
      pthread_join(tid, nullptr);
      return nullptr;
  }
  ```
* ArkTS导入头文件

  ```typescript
  import testNapi from 'libentry.so';
  ```
* ArkTS代码示例

  ```typescript
  export function Logger() {
    console.info('print log');
  }
  ```

  ```typescript
  // index.ets
  testNapi.createArkRuntime();
  ```
