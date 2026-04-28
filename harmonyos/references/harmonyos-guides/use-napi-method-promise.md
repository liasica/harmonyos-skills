---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-method-promise
title: 使用Node-API调用返回值为promise的ArkTS方法
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API调用返回值为promise的ArkTS方法
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:11+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:171fa5f689bf4365af3cbc833398820dc8729f361ab8e7da339765dc55e70647
---

## 场景介绍

当ArkTS的返回值为Promise时，可以按以下方式在创建的ArkTS运行环境中调用异步接口。

## 调用异步的ArkTS接口示例

使用C++通过NAPI调用返回Promise的ArkTS方法。

处理[Promise](use-napi-about-promise.md)对象：将Promise与C++回调绑定，处理异步结果。

转换数据类型：在回调中将JavaScript结果转换为c++可用的数据。

### 示例代码

* 模块注册

  ```
  1. #include "hilog/log.h"
  2. #include "napi/native_api.h"

  4. // 解析Promise结果的回调
  5. static napi_value ResolvedCallback(napi_env env, napi_callback_info info)
  6. {
  7. size_t argc = 1;
  8. napi_value args[1] = { nullptr };
  9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  11. int result = 0;
  12. napi_get_value_int32(env, args[0], &result);
  13. OH_LOG_INFO(LOG_APP, "Promise resolved with result:%{public}d", result);
  14. return nullptr;
  15. }

  17. // 拒绝Promise的回调
  18. static napi_value RejectedCallback(napi_env env, napi_callback_info info)
  19. {
  20. size_t argc = 1;
  21. napi_value args[1] = { nullptr };
  22. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  24. napi_value error = nullptr;
  25. napi_coerce_to_string(env, args[0], &error);
  26. char errorMsg[1024] = {0};
  27. size_t len = 0;
  28. napi_get_value_string_utf8(env, error, errorMsg, sizeof(errorMsg) - 1, &len);
  29. errorMsg[len] = '\0';
  30. OH_LOG_ERROR(LOG_APP, "Promise rejected with error:%{public}s", errorMsg);
  31. return nullptr;
  32. }

  34. static napi_value CallArkTSAsync(napi_env env, napi_callback_info info)
  35. {
  36. size_t argc = 1;
  37. napi_value argv[1] = { nullptr };
  38. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
  39. // 初始化Promise对象
  40. napi_value promise = nullptr;
  41. napi_call_function(env, nullptr, argv[0], 0, nullptr, &promise);

  43. // 初始化thenFunc对象
  44. napi_value thenFunc = nullptr;
  45. if (napi_get_named_property(env, promise, "then", &thenFunc) != napi_ok) {
  46. return nullptr;
  47. }
  48. // 初始化onResolve对象
  49. napi_value onResolve = nullptr;
  50. // 初始化onReject对象
  51. napi_value onReject = nullptr;
  52. napi_create_function(env, "onResolve", NAPI_AUTO_LENGTH, ResolvedCallback, nullptr, &onResolve);
  53. napi_create_function(env, "onReject", NAPI_AUTO_LENGTH, RejectedCallback, nullptr, &onReject);
  54. // 创建参数数组
  55. napi_value thenArgv[2] = {onResolve, onReject};
  56. napi_call_function(env, promise, thenFunc, 2, thenArgv, nullptr);

  58. return nullptr;
  59. }

  61. // 注册模块接口
  62. EXTERN_C_START
  63. static napi_value Init(napi_env env, napi_value exports)
  64. {
  65. // 初始化属性描述数组
  66. napi_property_descriptor desc[] = {
  67. {"callArkTSAsync", nullptr, CallArkTSAsync, nullptr, nullptr, nullptr, napi_default, nullptr}
  68. };
  69. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  70. return exports;
  71. }
  72. EXTERN_C_END

  74. // 初始化模块
  75. static napi_module nativeModule = {
  76. .nm_version = 1,
  77. .nm_flags = 0,
  78. .nm_filename = nullptr,
  79. .nm_register_func = Init,
  80. .nm_modname = "entry",
  81. .nm_priv = nullptr,
  82. .reserved = { 0 },
  83. };

  85. extern "C" __attribute__((constructor)) void RegisterEntryModule()
  86. {
  87. napi_module_register(&nativeModule);
  88. }
  ```
* 接口声明

  ```
  1. // index.d.ts
  2. export const callArkTSAsync: (func: Function) => void;
  ```
* CMakeLists.txt文件需要按照以下配置：

  ```
  1. // CMakeLists.txt
  2. # the minimum version of CMake.
  3. cmake_minimum_required(VERSION 3.4.1)
  4. project(myapplication)

  6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  8. if(DEFINED PACKAGE_FIND_FILE)
  9. include(${PACKAGE_FIND_FILE})
  10. endif()

  12. include_directories(${NATIVERENDER_ROOT_PATH}
  13. ${NATIVERENDER_ROOT_PATH}/include)

  15. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
  16. add_definitions( "-DLOG_TAG=\"testTag\"" )

  18. add_library(entry SHARED napi_init.cpp)
  19. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
  ```
* ArkTS代码示例

  ```
  1. // index.ets
  2. import testNapi from 'libentry.so';

  4. export function SetTimeout() : Promise<number> {
  5. return new Promise((resolve) => {
  6. setTimeout(() => {
  7. resolve(42);
  8. }, 1000);
  9. })
  10. }
  11. testNapi.callArkTSAsync(SetTimeout);
  ```
