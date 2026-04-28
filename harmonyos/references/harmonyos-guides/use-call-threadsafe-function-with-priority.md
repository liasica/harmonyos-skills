---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-call-threadsafe-function-with-priority
title: 使用Node-API接口从异步线程向ArkTS线程投递指定优先级和入队方式的任务
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口从异步线程向ArkTS线程投递指定优先级和入队方式的任务
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60822ed532bac53f6e8e1d84f5088681e18806846d6faaaa14833fa48570d2ef
---

Node-API中的napi\_call\_threadsafe\_function\_with\_priority接口的功能是从异步线程向ArkTS线程投递指定优先级和入队方式的任务，底层队列会根据任务的优先级和入队方式来处理任务。

## 函数说明

```
1. napi_status napi_call_threadsafe_function_with_priority(napi_threadsafe_function func, void *data,
2. napi_task_priority priority, bool isTail);
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
  1. #include "napi/native_api.h"
  2. // ...
  3. #include <hilog/log.h>
  4. // ...
  5. static constexpr int INT_ARG_2 = 2; // 入参索引
  6. static constexpr int INT_ARG_12 = 12; // 入参索引
  7. static constexpr int INT_ARG_15 = 15; // 入参索引
  8. // ...
  9. struct CallbackData {
  10. napi_threadsafe_function tsfn;
  11. napi_async_work work;
  12. };
  13. static void CallJs(napi_env env, napi_value jsCb, void *context, void *data)
  14. {
  15. if (env == nullptr) {
  16. return;
  17. }

  19. napi_handle_scope scope = nullptr;
  20. napi_status status = napi_open_handle_scope(env, &scope);
  21. if (status != napi_ok) {
  22. return;
  23. }

  25. napi_value resultNumber = nullptr;
  26. napi_value undefined = nullptr;
  27. napi_get_undefined(env, &undefined);
  28. napi_value number1 = nullptr;
  29. napi_create_int32(env, INT_ARG_12, &number1);
  30. napi_value number2 = nullptr;
  31. napi_create_int32(env, INT_ARG_15, &number2);
  32. napi_value argv[2] = {number1, number2};
  33. napi_call_function(env, undefined, jsCb, INT_ARG_2, argv, &resultNumber);
  34. int32_t res = 0;
  35. // 获取resultNumber对应的int32值
  36. napi_get_value_int32(env, resultNumber, &res);

  38. napi_close_handle_scope(env, scope);
  39. }

  41. // 异步线程中调用该接口向ArkTS线程投递指定优先级和入队方式的任务
  42. static void ExecuteWork(napi_env env, void *data)
  43. {
  44. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
  45. // 投递指定优先级为napi_priority_idle，入队方式为队列尾部入队的任务
  46. napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_idle, true);
  47. // 投递指定优先级为napi_priority_low，入队方式为队列尾部入队的任务
  48. napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_low, true);
  49. // 投递指定优先级为napi_priority_high，入队方式为队列尾部入队的任务
  50. napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_high, true);
  51. // 投递指定优先级为napi_priority_immediate，入队方式为队列尾部入队的任务
  52. napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_immediate, true);
  53. // 投递指定优先级为napi_priority_high，入队方式为队列头部入队的任务
  54. napi_call_threadsafe_function_with_priority(callbackData->tsfn, nullptr, napi_priority_high, false);
  55. }

  57. static void WorkComplete(napi_env env, napi_status status, void *data)
  58. {
  59. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
  60. if (callbackData->tsfn != nullptr) {
  61. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
  62. callbackData->tsfn = nullptr;
  63. }
  64. if (callbackData->work != nullptr) {
  65. napi_delete_async_work(env, callbackData->work);
  66. callbackData->work = nullptr;
  67. }
  68. delete callbackData;
  69. }

  71. static napi_value CallThreadSafeWithPriority(napi_env env, napi_callback_info info)
  72. {
  73. size_t argc = 1;
  74. napi_value jsCb = nullptr;
  75. CallbackData *callbackData = new CallbackData();
  76. napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);
  77. napi_value resourceName = nullptr;
  78. napi_create_string_utf8(env, "Thread-safe Function Demo", NAPI_AUTO_LENGTH, &resourceName);
  79. if (napi_create_threadsafe_function(env, jsCb, nullptr, resourceName, 0, 1, nullptr, nullptr, nullptr, CallJs,
  80. &callbackData->tsfn) != napi_ok) {
  81. delete callbackData;
  82. return nullptr;
  83. }
  84. // 创建一个异步任务对象
  85. if (napi_create_async_work(env, nullptr, resourceName,
  86. ExecuteWork, WorkComplete, callbackData, &callbackData->work) != napi_ok) {
  87. if (callbackData->tsfn != nullptr) {
  88. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
  89. }
  90. delete callbackData;
  91. return nullptr;
  92. }
  93. if (napi_queue_async_work(env, callbackData->work) != napi_ok) {
  94. if (callbackData->tsfn != nullptr) {
  95. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
  96. }
  97. napi_delete_async_work(env, callbackData->work);
  98. delete callbackData;
  99. return nullptr;
  100. }
  101. return nullptr;
  102. }
  ```
* 模块注册

  ```
  1. // 注册模块接口
  2. EXTERN_C_START
  3. static napi_value Init(napi_env env, napi_value exports)
  4. {
  5. napi_property_descriptor desc[] = {
  6. { "callThreadSafeWithPriority", nullptr, CallThreadSafeWithPriority, nullptr, nullptr, nullptr, napi_default, nullptr }
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

  23. extern "C" __attribute__((constructor)) void RegisterEntryModule()
  24. {
  25. napi_module_register(&nativeModule);
  26. }
  ```
* 接口声明

  ```
  1. // index.d.ts
  2. export const callThreadSafeWithPriority: (cb: (a: number, b: number) => number) => void;
  ```
* 编译配置

  CMakeLists.txt文件需要按照如下配置

  ```
  1. # the minimum version of CMake.
  2. cmake_minimum_required(VERSION 3.5.0)
  3. project(MyApplication3)

  5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  7. if(DEFINED PACKAGE_FIND_FILE)
  8. include(${PACKAGE_FIND_FILE})
  9. endif()
  10. add_definitions( "-DLOG_TAG=\"LOG_TAG\"" )
  11. include_directories(${NATIVERENDER_ROOT_PATH}
  12. ${NATIVERENDER_ROOT_PATH}/include)

  14. add_library(entry SHARED napi_init.cpp)
  15. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
  ```
* ArkTS导入头文件

  ```
  1. import testNapi from 'libentry.so';
  ```
* ArkTS代码示例

  ```
  1. // index.ets
  2. let callback = (a: number, b: number): number => {
  3. console.info('result is ' + (a + b))
  4. return a + b;
  5. }
  6. testNapi.callThreadSafeWithPriority(callback);
  ```
