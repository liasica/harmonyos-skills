---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-21
title: 使用NAPI扩展TS接口时，常用属性和实现接口的基本用法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 使用NAPI扩展TS接口时，常用属性和实现接口的基本用法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1af226cb043f43cb41b2622d7fb7b7bb77cbaad09ee8a2cdd2bce7bbe37f1524
---

1. env是使用NAPI的模块化编程，注册模块后，通过回调函数调用。

   ```
   1. static napi_value CallNapi(napi_env env, napi_callback_info info) {
   2. size_t argc = 1;
   3. napi_value object = nullptr;
   4. napi_status status;
   5. status = napi_get_cb_info(env, info, &argc, &object, nullptr, nullptr);
   6. return object;
   7. }
   8. NAPI_MODULE_INIT() {
   9. napi_property_descriptor desc[] = {
   10. { "callNapi", nullptr, CallNapi, nullptr, nullptr, nullptr, napi_default, nullptr }
   11. };
   12. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   13. return exports;
   14. }
   ```

   [napi\_call.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/cpp/napi_call.cpp#L7-L20)
2. 实现回调：

   ```
   1. #include "napi/native_api.h"
   2. #include <assert.h>
   3. static napi_value NativeCall(napi_env env, napi_callback_info info) {
   4. size_t argc = 1;
   5. napi_value args[1] = { nullptr };
   6. napi_status status;
   7. status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   8. assert(status == napi_ok);
   9. napi_valuetype valuetype;
   10. napi_typeof(env, args[0], &valuetype);
   11. if (valuetype != napi_valuetype::napi_function) {
   12. napi_throw_type_error(env, nullptr, "napi_function is expected");
   13. }
   14. napi_value cb = args[0];
   15. napi_value undefined;
   16. status = napi_get_undefined(env, &undefined);
   17. assert(status == napi_ok);
   18. napi_value argv[2] = { nullptr };
   19. status = napi_create_int32(env, 1, &argv[0]);
   20. assert(status == napi_ok);
   21. status = napi_create_int32(env, 2, &argv[1]);
   22. assert(status == napi_ok);
   23. napi_value result;
   24. status = napi_call_function(env, undefined, cb, 2, argv, &result);
   25. assert(status == napi_ok);
   26. return nullptr;
   27. }
   28. EXTERN_C_START
   29. static napi_value Init(napi_env env, napi_value exports) {
   30. napi_property_descriptor desc[] = {
   31. { "nativeCall", nullptr, NativeCall, nullptr, nullptr, nullptr, napi_default, nullptr }
   32. };
   33. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   34. return exports;
   35. }
   36. EXTERN_C_END
   37. static napi_module module = {
   38. .nm_version = 1,
   39. .nm_flags = 0,
   40. .nm_filename = nullptr,
   41. .nm_register_func = Init,
   42. .nm_modname = "callback",
   43. .nm_priv = nullptr,
   44. .reserved = { 0 },
   45. };
   46. extern "C" __attribute__((constructor)) void RegisterCallbackModule(void) {
   47. napi_module_register(&module);
   48. }
   ```

   [napi\_callback.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/cpp/napi_callback.cpp#L8-L55)
3. Promise实现参考：

   ```
   1. #include "napi/native_api.h"
   2. // Empty value so that macros here are able to return NULL or void
   3. #define NAPI_RETVAL_NOTHING  // Intentionally blank
   4. #define GET_AND_THROW_LAST_ERROR(env)
   5. do {
   6. const napi_extended_error_info* errorInfo = nullptr;
   7. napi_get_last_error_info((env), &errorInfo);
   8. bool isPending = false;
   9. napi_is_exception_pending((env), &isPending);
   10. if (!isPending && errorInfo != nullptr) {
   11. const char* errorMessage =
   12. errorInfo->error_message != nullptr ? errorInfo->error_message : "empty error message";
   13. napi_throw_error((env), nullptr, errorMessage);
   14. }
   15. } while (0)
   16. #define NAPI_ASSERT_BASE(env, assertion, message, retVal)
   17. do {
   18. if (!(assertion)) {
   19. napi_throw_error((env), nullptr, "assertion ("#assertion") failed:" message);
   20. return retVal;
   21. }
   22. } while (0)
   23. #define NAPI_ASSERT(env, assertion, message) NAPI_ASSERT_BASE(env, assertion, message, nullptr)
   24. #define NAPI_ASSERT_RETURN_VOID(env, assertion, message)
   25. NAPI_ASSERT_BASE(env, assertion, message, NAPI_RETVAL_NOTHING)
   26. #define NAPI_CALL_BASE(env, theCall, retVal)
   27. do {
   28. if ((theCall) != napi_ok) {
   29. GET_AND_THROW_LAST_ERROR((env));
   30. return retVal;
   31. }
   32. } while (0)
   33. #define NAPI_CALL(env, theCall) NAPI_CALL_BASE(env, theCall, nullptr)
   34. #define NAPI_CALL_RETURN_VOID(env, theCall) NAPI_CALL_BASE(env, theCall, NAPI_RETVAL_NOTHING)
   35. struct AsyncData {
   36. napi_deferred deferred;
   37. napi_async_work work;
   38. int32_t arg;
   39. double retVal;
   40. };
   41. double DoSomething(int32_t val) {
   42. if (val != 0) {
   43. return 1.0 / val;
   44. }
   45. return 0;
   46. }
   47. void ExecuteCallback(napi_env env, void* data) {
   48. AsyncData* asyncData = reinterpret_cast<AsyncData*>(data);
   49. asyncData->retVal = DoSomething(asyncData->arg);
   50. }
   51. void CompleteCallback(napi_env env, napi_status status, void* data) {
   52. AsyncData* asyncData = reinterpret_cast<AsyncData*>(data);
   53. napi_value retVal;
   54. if (asyncData->retVal == 0) {
   55. NAPI_CALL_RETURN_VOID(env, napi_create_string_utf8(env, "arg can't be zero", NAPI_AUTO_LENGTH, &retVal));
   56. NAPI_CALL_RETURN_VOID(env, napi_reject_deferred(env, asyncData->deferred, retVal));
   57. } else {
   58. NAPI_CALL_RETURN_VOID(env, napi_create_double(env, asyncData->retVal, &retVal));
   59. NAPI_CALL_RETURN_VOID(env, napi_resolve_deferred(env, asyncData->deferred, retVal));
   60. }
   61. NAPI_CALL_RETURN_VOID(env, napi_delete_async_work(env, asyncData->work));
   62. asyncData->work = nullptr;
   63. asyncData->deferred = nullptr;
   64. delete asyncData;
   65. }
   66. static napi_value NativeCall(napi_env env, napi_callback_info info) {
   67. size_t argc = 1;
   68. napi_value args[1] = { nullptr };
   69. NAPI_CALL(env, napi_get_cb_info(env, info, &argc, args, nullptr, nullptr));
   70. int32_t arg;
   71. NAPI_CALL(env, napi_get_value_int32(env, args[0], &arg));
   72. // Create promise
   73. napi_deferred deferred;
   74. napi_value promise;
   75. NAPI_CALL(env, napi_create_promise(env, &deferred, &promise));
   76. AsyncData* data = new AsyncData;
   77. data->deferred = deferred;
   78. data->arg = arg;
   79. napi_async_work work;
   80. napi_value workName;
   81. napi_create_string_utf8(env, "promise", NAPI_AUTO_LENGTH, &workName);
   82. NAPI_CALL(env, napi_create_async_work(env, nullptr, workName,ExecuteCallback, CompleteCallback, data, &work));
   83. data->work = work;
   84. NAPI_CALL(env, napi_queue_async_work(env, work));
   85. return promise;
   86. }
   87. EXTERN_C_START
   88. static napi_value Init(napi_env env, napi_value exports) {
   89. napi_property_descriptor desc[] = {
   90. { "nativeCall", nullptr, NativeCall, nullptr, nullptr, nullptr, napi_default, nullptr }
   91. };
   92. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   93. return exports;
   94. }
   95. EXTERN_C_END
   96. static napi_module demoModule = {
   97. .nm_version = 1,
   98. .nm_flags = 0,
   99. .nm_filename = nullptr,
   100. .nm_register_func = Init,
   101. .nm_modname = "promise",
   102. .nm_priv = nullptr,
   103. .reserved = { 0 },
   104. };
   105. extern "C" __attribute__((constructor)) void RegisterPromiseModule(void) {
   106. napi_module_register(&demoModule);
   107. }
   ```

   [napi\_promise.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/cpp/napi_promise.cpp#L7-L113)
4. 使用libuv：直接导入[libuv](../harmonyos-references/libuv.md)库。
