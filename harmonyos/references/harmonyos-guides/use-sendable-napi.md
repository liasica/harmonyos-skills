---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-sendable-napi
title: Native与Sendable ArkTS对象绑定
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > Native与Sendable ArkTS对象绑定
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:09+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:ff898bcc7e0338996533d8f6e4076bbd27688ca62836e57e97f9e3ff17ebca18
---

## 场景介绍

通过napi\_wrap\_sendable将[Sendable](arkts-sendable.md) ArkTS对象与Native的C++对象绑定，后续操作时再通过napi\_unwrap\_sendable将ArkTS对象绑定的C++对象取出，并对其进行操作。

## 使用示例

1. 接口声明、编译配置以及模块注册

   **接口声明**

   ```
   1. // index.d.ets
   2. @Sendable
   3. export class MyObject {
   4. constructor(arg: number);
   5. plusOne(): number;

   7. public get value();
   8. public set value(newVal: number);
   9. }
   ```

   **编译配置**

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(napi_wrap_sendable_demo)

   5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(${PACKAGE_FIND_FILE})
   9. endif()

   11. include_directories(${NATIVERENDER_ROOT_PATH}
   12. ${NATIVERENDER_ROOT_PATH}/include)

   14. add_definitions("-DLOG_DOMAIN=0x0000")
   15. add_definitions("-DLOG_TAG=\"testTag\"")

   17. add_library(entry SHARED napi_init.cpp)
   18. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```

   **模块注册**

   ```
   1. // napi_init.cpp
   2. #include "napi/native_api.h"
   3. #include "hilog/log.h"

   5. // 一个native类，它的实例在下面会包装在Sendable ArkTS对象中
   6. class MyObject {
   7. public:
   8. static napi_value Init(napi_env env, napi_value exports);
   9. static void Destructor(napi_env env, void *nativeObject, void *finalize_hint);

   11. private:
   12. explicit MyObject(double value_ = 0);
   13. ~MyObject();

   15. static napi_value New(napi_env env, napi_callback_info info);
   16. static napi_value GetValue(napi_env env, napi_callback_info info);
   17. static napi_value SetValue(napi_env env, napi_callback_info info);
   18. static napi_value PlusOne(napi_env env, napi_callback_info info);

   20. double value_;
   21. napi_env env_;
   22. };

   24. static thread_local napi_ref g_ref = nullptr;

   26. MyObject::MyObject(double value) : value_(value), env_(nullptr) {}

   28. MyObject::~MyObject() {}

   30. void MyObject::Destructor(napi_env env, void *nativeObject, [[maybe_unused]] void *finalize_hint) {
   31. OH_LOG_INFO(LOG_APP, "MyObject::Destructor called");
   32. reinterpret_cast<MyObject *>(nativeObject)->~MyObject();
   33. }

   35. napi_value MyObject::Init(napi_env env, napi_value exports) {
   36. napi_value num = nullptr;
   37. napi_status status = napi_create_double(env, 0, &num);
   38. if (status != napi_ok) {
   39. napi_throw_error(env, nullptr, "Node-API napi_create_double fail");
   40. return nullptr;
   41. }
   42. napi_property_descriptor properties[] = {
   43. {"value", nullptr, nullptr, GetValue, SetValue, nullptr, napi_default, nullptr},
   44. {"plusOne", nullptr, PlusOne, nullptr, nullptr, nullptr, napi_default, nullptr},
   45. };

   47. napi_value cons = nullptr;
   48. // 定义一个Sendable class MyObject
   49. status = napi_define_sendable_class(env, "MyObject", NAPI_AUTO_LENGTH, New, nullptr,
   50. sizeof(properties) / sizeof(properties[0]), properties, nullptr, &cons);
   51. if (status != napi_ok) {
   52. napi_throw_error(env, nullptr, "Node-API napi_define_sendable_class fail");
   53. return nullptr;
   54. }

   56. status = napi_create_reference(env, cons, 1, &g_ref);
   57. if (status != napi_ok) {
   58. napi_throw_error(env, nullptr, "Node-API napi_create_reference fail");
   59. return nullptr;
   60. }
   61. // 在exports对象上挂载MyObject类
   62. status = napi_set_named_property(env, exports, "MyObject", cons);
   63. if (status != napi_ok) {
   64. napi_throw_error(env, nullptr, "Node-API napi_set_named_property fail");
   65. return nullptr;
   66. }
   67. return exports;
   68. }

   70. EXTERN_C_START
   71. // 模块初始化
   72. static napi_value Init(napi_env env, napi_value exports) {
   73. MyObject::Init(env, exports);
   74. return exports;
   75. }
   76. EXTERN_C_END

   78. // 准备模块加载相关信息，将上述Init函数与本模块名等信息记录下来。
   79. static napi_module nativeModule = {
   80. .nm_version = 1,
   81. .nm_flags = 0,
   82. .nm_filename = nullptr,
   83. .nm_register_func = Init,
   84. .nm_modname = "entry",
   85. .nm_priv = nullptr,
   86. .reserved = {0},
   87. };

   89. // 加载so时，该函数会自动被调用，将上述nativeModule模块注册到系统中。
   90. extern "C" __attribute__((constructor)) void RegisterObjectWrapModule() { napi_module_register(&nativeModule); }
   ```
2. 在构造函数中绑定Sendable ArkTS与C++对象

   ```
   1. napi_value MyObject::New(napi_env env, napi_callback_info info) {
   2. OH_LOG_INFO(LOG_APP, "MyObject::New called");

   4. napi_value newTarget = nullptr;
   5. napi_status status = napi_get_new_target(env, info, &newTarget);
   6. if (status != napi_ok) {
   7. napi_throw_error(env, nullptr, "Node-API napi_get_new_target fail");
   8. return nullptr;
   9. }
   10. if (newTarget != nullptr) {
   11. // 使用`new MyObject(...)`调用方式
   12. size_t argc = 1;
   13. napi_value args[1] = { nullptr };
   14. napi_value jsThis = nullptr;
   15. status = napi_get_cb_info(env, info, &argc, args, &jsThis, nullptr);
   16. if (status != napi_ok) {
   17. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   18. return nullptr;
   19. }

   21. double value = 0.0;
   22. napi_valuetype valuetype = napi_undefined;
   23. status = napi_typeof(env, args[0], &valuetype);
   24. if (status != napi_ok) {
   25. napi_throw_error(env, nullptr, "Node-API napi_typeof fail");
   26. return nullptr;
   27. }
   28. if (valuetype != napi_undefined) {
   29. status = napi_get_value_double(env, args[0], &value);
   30. if (status != napi_ok) {
   31. napi_throw_error(env, nullptr, "Node-API napi_get_value_double fail");
   32. return nullptr;
   33. }
   34. }

   36. MyObject *obj = new MyObject(value);

   38. obj->env_ = env;
   39. // 通过napi_wrap_sendable将Sendable ArkTS对象jsThis与C++对象obj绑定
   40. status = napi_wrap_sendable(env, jsThis, reinterpret_cast<void *>(obj), MyObject::Destructor, nullptr);
   41. if (status != napi_ok) {
   42. napi_throw_error(env, nullptr, "Node-API napi_wrap_sendable fail");
   43. delete obj;
   44. return nullptr;
   45. }

   47. return jsThis;
   48. } else {
   49. // 使用`MyObject(...)`调用方式
   50. size_t argc = 1;
   51. napi_value args[1] = { nullptr };
   52. status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   53. if (status != napi_ok) {
   54. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   55. return nullptr;
   56. }

   58. napi_value cons = nullptr;
   59. status = napi_get_reference_value(env, g_ref, &cons);
   60. if (status != napi_ok) {
   61. napi_throw_error(env, nullptr, "Node-API napi_get_reference_value fail");
   62. return nullptr;
   63. }
   64. napi_value instance = nullptr;
   65. status = napi_new_instance(env, cons, argc, args, &instance);
   66. if (status != napi_ok) {
   67. napi_throw_error(env, nullptr, "Node-API napi_new_instance fail");
   68. return nullptr;
   69. }

   71. return instance;
   72. }
   73. }
   ```
3. 将Sendable ArkTS对象之前绑定的C++对象取出，并对其进行操作

   ```
   1. napi_value MyObject::GetValue(napi_env env, napi_callback_info info) {
   2. OH_LOG_INFO(LOG_APP, "MyObject::GetValue called");

   4. napi_value jsThis = nullptr;
   5. napi_status status = napi_get_cb_info(env, info, nullptr, nullptr, &jsThis, nullptr);
   6. if (status != napi_ok) {
   7. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   8. return nullptr;
   9. }

   11. MyObject *obj = nullptr;
   12. // 通过napi_unwrap_sendable将jsThis之前绑定的C++对象取出，并对其进行操作
   13. status = napi_unwrap_sendable(env, jsThis, reinterpret_cast<void **>(&obj));
   14. if (status != napi_ok) {
   15. napi_throw_error(env, nullptr, "Node-API napi_unwrap_sendable fail");
   16. return nullptr;
   17. }
   18. napi_value num = nullptr;
   19. status = napi_create_double(env, obj->value_, &num);
   20. if (status != napi_ok) {
   21. napi_throw_error(env, nullptr, "Node-API napi_create_double fail");
   22. return nullptr;
   23. }

   25. return num;
   26. }

   28. napi_value MyObject::SetValue(napi_env env, napi_callback_info info) {
   29. OH_LOG_INFO(LOG_APP, "MyObject::SetValue called");

   31. size_t argc = 1;
   32. napi_value value = nullptr;
   33. napi_value jsThis = nullptr;

   35. napi_status status = napi_get_cb_info(env, info, &argc, &value, &jsThis, nullptr);
   36. if (status != napi_ok) {
   37. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   38. return nullptr;
   39. }

   41. MyObject *obj = nullptr;
   42. // 通过napi_unwrap_sendable将jsThis之前绑定的C++对象取出，并对其进行操作
   43. status = napi_unwrap_sendable(env, jsThis, reinterpret_cast<void **>(&obj));
   44. if (status != napi_ok) {
   45. napi_throw_error(env, nullptr, "Node-API napi_unwrap_sendable fail");
   46. return nullptr;
   47. }
   48. status = napi_get_value_double(env, value, &obj->value_);
   49. if (status != napi_ok) {
   50. napi_throw_error(env, nullptr, "Node-API napi_get_value_double fail");
   51. return nullptr;
   52. }

   54. return nullptr;
   55. }

   57. napi_value MyObject::PlusOne(napi_env env, napi_callback_info info) {
   58. OH_LOG_INFO(LOG_APP, "MyObject::PlusOne called");

   60. napi_value jsThis = nullptr;
   61. napi_status status = napi_get_cb_info(env, info, nullptr, nullptr, &jsThis, nullptr);
   62. if (status != napi_ok) {
   63. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   64. return nullptr;
   65. }

   67. MyObject *obj = nullptr;
   68. // 通过napi_unwrap_sendable将jsThis之前绑定的C++对象取出，并对其进行操作
   69. status = napi_unwrap_sendable(env, jsThis, reinterpret_cast<void **>(&obj));
   70. if (status != napi_ok) {
   71. napi_throw_error(env, nullptr, "Node-API napi_unwrap_sendable fail");
   72. return nullptr;
   73. }
   74. obj->value_ += 1;
   75. napi_value num = nullptr;
   76. status = napi_create_double(env, obj->value_, &num);
   77. if (status != napi_ok) {
   78. napi_throw_error(env, nullptr, "Node-API napi_create_double fail");
   79. return nullptr;
   80. }

   82. return num;
   83. }
   ```
4. ArkTS侧示例代码

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { MyObject } from 'libentry.so';

   4. try {
   5. let object : MyObject = new MyObject(0);
   6. object.value = 1023.1;
   7. hilog.info(0x0000, 'testTag', 'MyObject value after set: %{public}s', object.value.toString());
   8. hilog.info(0x0000, 'testTag', 'MyObject plusOne: %{public}s', object.plusOne().toString());
   9. } catch (error) {
   10. hilog.error(0x0000, 'testTag', 'Test Node-API error: %{public}s', error.message);
   11. }
   ```
