---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-event-loop
title: 使用扩展的Node-API接口在异步线程中运行和停止事件循环
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口在异步线程中运行和停止事件循环
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:96ac5785b6b0e690912e5a954a7cd4f2cafd312a05e8a15d765a3faf8b2220d5
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
  1. #include "napi/native_api.h"
  2. #include <pthread.h>
  3. #include <hilog/log.h>
  4. #include <napi/common.h>
  5. static constexpr int INT_ARG_2 = 2; // 入参索引
  6. // ...
  7. static napi_value ResolvedCallback(napi_env env, napi_callback_info info)
  8. {
  9. napi_stop_event_loop(env);
  10. return nullptr;
  11. }

  13. static napi_value RejectedCallback(napi_env env, napi_callback_info info)
  14. {
  15. napi_stop_event_loop(env);
  16. return nullptr;
  17. }

  19. static bool CallSetTimeoutWithCallbacks(napi_env env, napi_value objectUtils)
  20. {
  21. napi_value setTimeout = nullptr;
  22. napi_value promise = nullptr;

  24. if (napi_get_named_property(env, objectUtils, "SetTimeout", &setTimeout) != napi_ok) {
  25. return false;
  26. }
  27. if (napi_call_function(env, objectUtils, setTimeout, 0, nullptr, &promise) != napi_ok) {
  28. return false;
  29. }

  31. napi_value theFunc = nullptr;
  32. if (napi_get_named_property(env, promise, "then", &theFunc) != napi_ok) {
  33. return false;
  34. }

  36. napi_value resolvedCallback = nullptr;
  37. napi_value rejectedCallback = nullptr;
  38. if (napi_create_function(env, "resolvedCallback", NAPI_AUTO_LENGTH,
  39. ResolvedCallback, nullptr, &resolvedCallback) != napi_ok) {
  40. return false;
  41. }
  42. if (napi_create_function(env, "rejectedCallback", NAPI_AUTO_LENGTH,
  43. RejectedCallback, nullptr, &rejectedCallback) != napi_ok) {
  44. return false;
  45. }
  46. napi_value argv[2] = {resolvedCallback, rejectedCallback};
  47. if (napi_call_function(env, promise, theFunc, INT_ARG_2, argv, nullptr) != napi_ok) {
  48. return false;
  49. }
  50. return true;
  51. }

  53. static void *RunEventLoopFunc(void *arg)
  54. {
  55. // 1. 创建ArkTS实例
  56. napi_env env = nullptr;
  57. napi_status ret = napi_create_ark_runtime(&env);
  58. if (ret != napi_ok) {
  59. return nullptr;
  60. }

  62. napi_handle_scope scope = nullptr;
  63. napi_open_handle_scope(env, &scope);

  65. // 2. 加载自定义的模块
  66. napi_value objectUtils = nullptr;
  67. // 'com.example.myapplication' 为当前应用的bundleName
  68. ret = napi_load_module_with_info(env, "entry/src/main/ets/pages/ObjectUtils", "com.example.myapplication/entry",
  69. &objectUtils);
  70. if (ret != napi_ok) {
  71. OH_LOG_INFO(LOG_APP, "Failed to load module");
  72. napi_close_handle_scope(env, scope);
  73. napi_destroy_ark_runtime(&env);
  74. return nullptr;
  75. }

  77. // 3. 调用异步SetTimeout接口
  78. if (!CallSetTimeoutWithCallbacks(env, objectUtils)) {
  79. napi_close_handle_scope(env, scope);
  80. napi_destroy_ark_runtime(&env);
  81. return nullptr;
  82. }

  84. auto flag = reinterpret_cast<bool *>(arg);
  85. if (*flag == true) {
  86. if (napi_run_event_loop(env, napi_event_mode_default) != napi_ok) {
  87. napi_close_handle_scope(env, scope);
  88. napi_destroy_ark_runtime(&env);
  89. return nullptr;
  90. }
  91. } else {
  92. if (napi_run_event_loop(env, napi_event_mode_nowait) != napi_ok) {
  93. napi_close_handle_scope(env, scope);
  94. napi_destroy_ark_runtime(&env);
  95. return nullptr;
  96. }
  97. }

  99. if (scope != nullptr) {
  100. napi_close_handle_scope(env, scope);
  101. scope = nullptr;
  102. }
  103. if (env != nullptr) {
  104. napi_status destroy_ret = napi_destroy_ark_runtime(&env);
  105. if (destroy_ret != napi_ok) {
  106. OH_LOG_INFO(LOG_APP, "Failed to destroy ark runtime");
  107. }
  108. env = nullptr;
  109. }
  110. return nullptr;
  111. }

  113. static napi_value RunEventLoop(napi_env env, napi_callback_info info)
  114. {
  115. pthread_t tid;
  116. size_t argc = 1;
  117. napi_value argv[1] = { nullptr };
  118. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

  120. bool flag = false;
  121. napi_get_value_bool(env, argv[0], &flag);
  122. // 创建异步线程
  123. pthread_create(&tid, nullptr, RunEventLoopFunc, &flag);
  124. pthread_join(tid, nullptr);

  126. return nullptr;
  127. }
  ```
* 模块注册

  ```
  1. EXTERN_C_START
  2. static napi_value Init(napi_env env, napi_value exports)
  3. {
  4. napi_property_descriptor desc[] = {
  5. { "runEventLoop", nullptr, RunEventLoop, nullptr, nullptr, nullptr, napi_default, nullptr }
  6. };
  7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  8. return exports;
  9. }
  10. EXTERN_C_END

  12. static napi_module nativeModule = {
  13. .nm_version = 1,
  14. .nm_flags = 0,
  15. .nm_filename = nullptr,
  16. .nm_register_func = Init,
  17. .nm_modname = "entry",
  18. .nm_priv = nullptr,
  19. .reserved = { 0 },
  20. };

  22. extern "C" __attribute__((constructor)) void RegisterEntryModule()
  23. {
  24. napi_module_register(&nativeModule);
  25. }
  ```
* 接口声明

  ```
  1. // index.d.ts
  2. export const runEventLoop: (isDefault: boolean) => object;
  ```
* 编译配置

1. CMakeLists.txt文件需要按照如下配置

   ```
   1. // CMakeLists.txt
   2. # the minimum version of CMake.
   3. cmake_minimum_required(VERSION 3.5.0)
   4. project(MyApplication3)

   6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   8. if(DEFINED PACKAGE_FIND_FILE)
   9. include(${PACKAGE_FIND_FILE})
   10. endif()
   11. add_definitions( "-DLOG_TAG=\"LOG_TAG\"" )
   12. include_directories(${NATIVERENDER_ROOT_PATH}
   13. ${NATIVERENDER_ROOT_PATH}/include)

   15. add_library(entry SHARED napi_init.cpp)
   16. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
2. 需要在模块的build-profile.json5文件中进行以下配置

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

* ArkTS代码示例

  ```
  1. // 导入头文件
  2. import testNapi from 'libentry.so'
  ```

  ```
  1. // index.ets
  2. testNapi.runEventLoop(true);
  ```

  ```
  1. export function SetTimeout(): Promise<void> {
  2. return new Promise((resolve) => {
  3. setTimeout(() => {
  4. console.info('set timer delay 1s');
  5. // attempt to stop the event loop at napi terminal
  6. resolve();
  7. }, 1000)
  8. })
  9. }
  ```
