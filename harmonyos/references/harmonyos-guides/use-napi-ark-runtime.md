---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-ark-runtime
title: 使用Node-API接口创建ArkTS运行时环境
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口创建ArkTS运行时环境
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:15912eeb467eb0f2f9892890020addb7a7fdc9cf0eec2083becbcce1bccfa557
---

## 场景介绍

开发者通过pthread\_create创建新线程后，可以通过napi\_create\_ark\_runtime来创建一个新的ArkTS基础运行时环境，并通过该运行时环境加载ArkTS模块。当使用结束后，开发者需要通过napi\_destroy\_ark\_runtime来销毁所创建的ArkTS基础运行时环境。

## 约束限制

一个进程最多只能创建64个运行时环境。

### 示例代码

* 接口声明

  ```
  1. // index.d.ts
  2. export const createArkRuntime: () => object;
  ```
* 编译配置

  ```
  1. # the minimum version of CMake.
  2. cmake_minimum_required(VERSION 3.5.0)
  3. project(MyApplication3)

  5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
  6. if(DEFINED PACKAGE_FIND_FILE)
  7. include(${PACKAGE_FIND_FILE})
  8. endif()
  9. add_definitions( "-DLOG_TAG=\"LOG_TAG\"" )
  10. include_directories(${NATIVERENDER_ROOT_PATH}
  11. ${NATIVERENDER_ROOT_PATH}/include)

  13. add_library(entry SHARED napi_init.cpp)
  14. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
  ```

  在当前模块的build-profile.json5文件中进行以下配置：

  ```
  1. "buildOption": {
  2. "arkOptions" : {
  3. "runtimeOnly" : {
  4. "sources": [
  5. "./src/main/ets/pages/ObjectUtils.ets"
  6. ]
  7. }
  8. },
  ```
* 模块注册

  ```
  1. // create_ark_runtime.cpp
  2. EXTERN_C_START
  3. static napi_value Init(napi_env env, napi_value exports)
  4. {
  5. napi_property_descriptor desc[] = {
  6. { "createArkRuntime", nullptr, CreateArkRuntime, nullptr, nullptr, nullptr, napi_default, nullptr }
  7. };
  8. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  9. return exports;
  10. }
  11. EXTERN_C_END

  13. static napi_module nativeModule = {
  14. .nm_version = 1,
  15. .nm_flags = 0,
  16. .nm_filename = nullptr,
  17. .nm_register_func = Init,
  18. .nm_modname = "entry",
  19. .nm_priv = nullptr,
  20. .reserved = { 0 },
  21. };

  23. extern "C" __attribute__((constructor)) void RegisterQueueWorkModule()
  24. {
  25. napi_module_register(&nativeModule);
  26. }
  ```
* 功能实现

  新建线程并创建ArkTS基础运行时环境，加载自定义模块请参考[napi\_load\_module\_with\_info](use-napi-load-module-with-info.md)。

  ```
  1. #include "napi/native_api.h"
  2. #include <pthread.h>
  3. // ...
  4. static void *CreateArkRuntimeFunc(void *arg)
  5. {
  6. // 1. 创建基础运行环境
  7. napi_env env = nullptr;
  8. napi_status ret = napi_create_ark_runtime(&env);
  9. if (ret != napi_ok) {
  10. return nullptr;
  11. }

  13. napi_handle_scope scope = nullptr;
  14. if (napi_open_handle_scope(env, &scope) != napi_ok) {
  15. napi_destroy_ark_runtime(&env);
  16. return nullptr;
  17. }

  19. // 2. 加载自定义模块
  20. napi_value objUtils = nullptr;
  21. ret = napi_load_module_with_info(env, "entry/src/main/ets/pages/ObjectUtils", "com.example.myapplication/entry",
  22. &objUtils);
  23. if (ret != napi_ok) {
  24. OH_LOG_INFO(LOG_APP, "Failed to load module");
  25. napi_close_handle_scope(env, scope);
  26. napi_destroy_ark_runtime(&env);
  27. return nullptr;
  28. }

  30. // 3. 使用ArkTS中的logger
  31. napi_value logger = nullptr;
  32. ret = napi_get_named_property(env, objUtils, "Logger", &logger);
  33. if (ret != napi_ok) {
  34. napi_close_handle_scope(env, scope);
  35. napi_destroy_ark_runtime(&env);
  36. return nullptr;
  37. }
  38. ret = napi_call_function(env, objUtils, logger, 0, nullptr, nullptr);
  39. if (ret != napi_ok) {
  40. napi_close_handle_scope(env, scope);
  41. napi_destroy_ark_runtime(&env);
  42. return nullptr;
  43. }

  45. napi_close_handle_scope(env, scope);

  47. // 4. 销毁ArkTS环境
  48. ret = napi_destroy_ark_runtime(&env);
  49. if (ret != napi_ok) {
  50. OH_LOG_INFO(LOG_APP, "Failed to destroy ark runtime");
  51. }

  53. return nullptr;
  54. }

  56. static napi_value CreateArkRuntime(napi_env env, napi_callback_info info)
  57. {
  58. pthread_t tid;
  59. pthread_create(&tid, nullptr, CreateArkRuntimeFunc, nullptr);
  60. pthread_join(tid, nullptr);
  61. return nullptr;
  62. }
  ```
* ArkTS导入头文件

  ```
  1. import testNapi from 'libentry.so';
  ```
* ArkTS代码示例

  ```
  1. export function Logger() {
  2. console.info('print log');
  3. }
  ```

  ```
  1. // index.ets
  2. testNapi.createArkRuntime();
  ```
