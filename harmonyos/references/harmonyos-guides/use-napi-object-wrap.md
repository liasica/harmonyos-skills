---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-object-wrap
title: Native与ArkTS对象绑定
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > Native与ArkTS对象绑定
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:08+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:0a9354f7f79981c16ec4e1dde8ce00fd2ccea2070961d72d350e5bfc5798b31c
---

## 场景介绍

通过napi\_wrap将ArkTS对象与Native的C++对象绑定，后续操作时再通过napi\_unwrap将ArkTS对象绑定的C++对象取出，并对其进行操作。

## 使用示例

1. 接口声明、编译配置以及模块注册

   **接口声明**

   ```
   1. // index.d.ts
   2. export class MyObject {
   3. constructor(arg: number);
   4. plusOne: () => number;

   6. public get value();
   7. public set value(newVal: number);
   8. }
   ```

   **编译配置**

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(napi_wrap_demo)

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

   5. class MyObject {
   6. public:
   7. static napi_value Init(napi_env env, napi_value exports);
   8. static void Destructor(napi_env env, void* nativeObject, void* finalize_hint);

   10. private:
   11. explicit MyObject(double value_ = 0);
   12. ~MyObject();

   14. static napi_value New(napi_env env, napi_callback_info info);
   15. static napi_value GetValue(napi_env env, napi_callback_info info);
   16. static napi_value SetValue(napi_env env, napi_callback_info info);
   17. static napi_value PlusOne(napi_env env, napi_callback_info info);

   19. double value_;
   20. napi_env env_;
   21. napi_ref wrapper_;
   22. };

   24. MyObject::MyObject(double value) : value_(value), env_(nullptr), wrapper_(nullptr) {}

   26. MyObject::~MyObject()
   27. {
   28. napi_status status = napi_delete_reference(env_, wrapper_);
   29. if (status != napi_ok) {
   30. OH_LOG_INFO(LOG_APP, "Failed to delete reference, return code: %{public}d", status);
   31. }
   32. }

   34. void MyObject::Destructor(napi_env env, void* nativeObject, [[maybe_unused]] void* finalize_hint)
   35. {
   36. OH_LOG_INFO(LOG_APP, "MyObject::Destructor called");
   37. delete reinterpret_cast<MyObject*>(nativeObject);
   38. }

   40. napi_value MyObject::Init(napi_env env, napi_value exports)
   41. {
   42. napi_property_descriptor properties[] = {
   43. { "value", nullptr, nullptr, GetValue, SetValue, nullptr, napi_default, nullptr },
   44. { "plusOne", nullptr, PlusOne, nullptr, nullptr, nullptr, napi_default, nullptr }
   45. };

   47. napi_value cons = nullptr;
   48. napi_status status = napi_define_class(env, "MyObject", NAPI_AUTO_LENGTH, New, nullptr, 2, properties, &cons);
   49. if (status != napi_ok) {
   50. napi_throw_error(env, nullptr, "Node-API napi_define_class fail");
   51. return nullptr;
   52. }

   54. status = napi_set_named_property(env, exports, "MyObject", cons);
   55. if (status != napi_ok) {
   56. napi_throw_error(env, nullptr, "Node-API napi_set_named_property fail");
   57. return nullptr;
   58. }
   59. return exports;
   60. }

   62. EXTERN_C_START
   63. static napi_value Init(napi_env env, napi_value exports)
   64. {
   65. MyObject::Init(env, exports);
   66. return exports;
   67. }
   68. EXTERN_C_END

   70. static napi_module nativeModule = {
   71. .nm_version = 1,
   72. .nm_flags = 0,
   73. .nm_filename = nullptr,
   74. .nm_register_func = Init,
   75. .nm_modname = "entry",
   76. .nm_priv = nullptr,
   77. .reserved = { 0 },
   78. };

   80. extern "C" __attribute__((constructor)) void RegisterObjectWrapModule()
   81. {
   82. napi_module_register(&nativeModule);
   83. }
   ```
2. 在构造函数中绑定ArkTS与C++对象

   ```
   1. napi_value MyObject::New(napi_env env, napi_callback_info info)
   2. {
   3. OH_LOG_INFO(LOG_APP, "MyObject::New called");

   5. napi_value newTarget = nullptr;
   6. napi_status status = napi_get_new_target(env, info, &newTarget);
   7. if (status != napi_ok) {
   8. napi_throw_error(env, nullptr, "Node-API napi_get_new_target fail");
   9. return nullptr;
   10. }
   11. if (newTarget != nullptr) {
   12. // 使用`new MyObject(...)`调用方式
   13. size_t argc = 1;
   14. napi_value args[1] = { nullptr };
   15. napi_value jsThis = nullptr;
   16. status = napi_get_cb_info(env, info, &argc, args, &jsThis, nullptr);
   17. if (status != napi_ok) {
   18. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   19. return nullptr;
   20. }

   22. double value = 0.0;
   23. napi_valuetype valuetype = napi_undefined;
   24. status = napi_typeof(env, args[0], &valuetype);
   25. if (status != napi_ok) {
   26. napi_throw_error(env, nullptr, "Node-API napi_typeof fail");
   27. return nullptr;
   28. }
   29. if (valuetype != napi_undefined) {
   30. status = napi_get_value_double(env, args[0], &value);
   31. if (status != napi_ok) {
   32. napi_throw_error(env, nullptr, "Node-API napi_get_value_double fail");
   33. return nullptr;
   34. }
   35. }

   37. MyObject* obj = new MyObject(value);

   39. obj->env_ = env;
   40. // 通过napi_wrap将ArkTS对象jsThis)与C++对象obj绑定
   41. status = napi_wrap(env,
   42. jsThis,
   43. reinterpret_cast<void*>(obj),
   44. MyObject::Destructor,
   45. nullptr,  // finalize_hint
   46. &obj->wrapper_);
   47. // napi_wrap失败时，必须手动释放已分配的内存，以防止内存泄漏
   48. if (status != napi_ok) {
   49. delete obj;
   50. napi_throw_error(env, nullptr, "Node-API napi_wrap fail");
   51. return jsThis;
   52. }
   53. // 从napi_wrap接口的result获取napi_ref的行为，将会为jsThis创建强引用，
   54. // 若开发者不需要主动管理jsThis的生命周期，可直接在napi_wrap最后一个参数中传入nullptr，
   55. // 或者使用napi_reference_unref方法将napi_ref转为弱引用。
   56. uint32_t refCount = 0;
   57. napi_reference_unref(env, obj->wrapper_, &refCount);

   59. return jsThis;
   60. } else {
   61. // 使用`MyObject(...)`调用方式
   62. size_t argc = 1;
   63. napi_value args[1] = { nullptr };
   64. napi_value jsThis = nullptr;
   65. status = napi_get_cb_info(env, info, &argc, args, &jsThis, nullptr);
   66. if (status != napi_ok) {
   67. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   68. return nullptr;
   69. }

   71. napi_value cons = nullptr;
   72. const char* constructorName = "MyObject";
   73. status = napi_get_named_property(env, jsThis, constructorName, &cons);
   74. if (status != napi_ok) {
   75. napi_throw_error(env, nullptr, "Node-API napi_get_named_property fail");
   76. return nullptr;
   77. }
   78. napi_value instance = nullptr;
   79. status = napi_new_instance(env, cons, argc, args, &instance);
   80. if (status != napi_ok) {
   81. napi_throw_error(env, nullptr, "Node-API napi_new_instance fail");
   82. return nullptr;
   83. }

   85. return instance;
   86. }
   87. }
   ```
3. 将ArkTS对象之前绑定的C++对象取出，并对其进行操作

   ```
   1. napi_value MyObject::GetValue(napi_env env, napi_callback_info info)
   2. {
   3. OH_LOG_INFO(LOG_APP, "MyObject::GetValue called");

   5. napi_value jsThis = nullptr;
   6. napi_status status = napi_get_cb_info(env, info, nullptr, nullptr, &jsThis, nullptr);
   7. if (status != napi_ok) {
   8. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   9. return nullptr;
   10. }

   12. MyObject* obj = nullptr;
   13. // 通过napi_unwrap将jsThis之前绑定的C++对象取出，并对其进行操作
   14. status = napi_unwrap(env, jsThis, reinterpret_cast<void**>(&obj));
   15. if (status != napi_ok) {
   16. napi_throw_error(env, nullptr, "Node-API napi_unwrap fail");
   17. return nullptr;
   18. }
   19. napi_value num = nullptr;
   20. status = napi_create_double(env, obj->value_, &num);
   21. if (status != napi_ok) {
   22. napi_throw_error(env, nullptr, "Node-API napi_create_double fail");
   23. return nullptr;
   24. }

   26. return num;
   27. }

   29. napi_value MyObject::SetValue(napi_env env, napi_callback_info info)
   30. {
   31. OH_LOG_INFO(LOG_APP, "MyObject::SetValue called");

   33. size_t argc = 1;
   34. napi_value value = nullptr;
   35. napi_value jsThis = nullptr;

   37. napi_status status = napi_get_cb_info(env, info, &argc, &value, &jsThis, nullptr);
   38. if (status != napi_ok) {
   39. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   40. return nullptr;
   41. }

   43. MyObject* obj = nullptr;
   44. // 通过napi_unwrap将jsThis之前绑定的C++对象取出，并对其进行操作
   45. status = napi_unwrap(env, jsThis, reinterpret_cast<void**>(&obj));
   46. if (status != napi_ok) {
   47. napi_throw_error(env, nullptr, "Node-API napi_unwrap fail");
   48. return nullptr;
   49. }
   50. status = napi_get_value_double(env, value, &obj->value_);
   51. if (status != napi_ok) {
   52. napi_throw_error(env, nullptr, "Node-API napi_get_value_double fail");
   53. return nullptr;
   54. }

   56. return nullptr;
   57. }

   59. napi_value MyObject::PlusOne(napi_env env, napi_callback_info info)
   60. {
   61. OH_LOG_INFO(LOG_APP, "MyObject::PlusOne called");

   63. napi_value jsThis = nullptr;
   64. napi_status status = napi_get_cb_info(env, info, nullptr, nullptr, &jsThis, nullptr);
   65. if (status != napi_ok) {
   66. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
   67. return nullptr;
   68. }

   70. MyObject* obj = nullptr;
   71. // 通过napi_unwrap将jsThis之前绑定的C++对象取出，并对其进行操作
   72. status = napi_unwrap(env, jsThis, reinterpret_cast<void**>(&obj));
   73. if (status != napi_ok) {
   74. napi_throw_error(env, nullptr, "Node-API napi_unwrap fail");
   75. return nullptr;
   76. }
   77. obj->value_ += 1;
   78. napi_value num = nullptr;
   79. status = napi_create_double(env, obj->value_, &num);
   80. if (status != napi_ok) {
   81. napi_throw_error(env, nullptr, "Node-API napi_create_double fail");
   82. return nullptr;
   83. }

   85. return num;
   86. }
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
