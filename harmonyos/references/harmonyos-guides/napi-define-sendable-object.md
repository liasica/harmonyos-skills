---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-define-sendable-object
title: 自定义Native Sendable对象的多线程操作场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 自定义Native Sendable对象的多线程操作场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ff081c67375fb67ab80dde06db59d1fc394af9fa2152d0e54f7db8595e6b9ead
---

ArkTS支持开发者自定义Native Sendable对象，Sendable对象提供了并发实例间高效的通信能力，即引用传递，适用于开发者自定义大对象需要线程间通信的场景，例如子线程读取数据库数据并返回给宿主线程。

本示例将详细说明如何使用自定义Native Sendable对象实现并发实例间数据共享。

1. 接口声明中自定义Sendable类。

   ```
   1. // Index.d.ets
   2. @Sendable
   3. export class MyObject {
   4. constructor(arg: number);
   5. plusOne(): number;

   7. public get value(): number;
   8. public set value(newVal: number);
   9. }
   ```
2. 编译配置。

   ```
   1. # CMakeLists.txt
   2. # the minimum version of CMake.
   3. cmake_minimum_required(VERSION 3.5.0)
   4. project(napi_wrap_sendable_demo)

   6. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   8. if(DEFINED PACKAGE_FIND_FILE)
   9. include(${PACKAGE_FIND_FILE})
   10. endif()

   12. include_directories(${NATIVERENDER_ROOT_PATH}
   13. ${NATIVERENDER_ROOT_PATH}/include)

   15. add_definitions("-DLOG_DOMAIN=0x0000")
   16. add_definitions("-DLOG_TAG=\"testTag\"")

   18. add_library(entry SHARED napi_init.cpp)
   19. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
3. Native实现各项接口功能，例如取值、设置值或者给Native对象的值加1等功能。

   ```
   1. // napi_init.cpp
   2. #include "napi/native_api.h"
   3. #include "hilog/log.h"

   5. // 一个native类，它的实例在下面会包装在ArkTS的Sendable对象中
   6. class MyObject {
   7. public:
   8. static napi_value Init(napi_env env, napi_value exports);
   9. static void Destructor(napi_env env, void *nativeObject, void *finalizeHint);

   11. private:
   12. explicit MyObject(double value = 0);
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

   30. void MyObject::Destructor(napi_env env, void *nativeObject, [[maybe_unused]] void *finalizeHint)
   31. {
   32. OH_LOG_INFO(LOG_APP, "MyObject::Destructor called");
   33. reinterpret_cast<MyObject *>(nativeObject)->~MyObject();
   34. }

   36. // 在构造函数中绑定ArkTS Sendable对象与C++对象
   37. napi_value MyObject::New(napi_env env, napi_callback_info info)
   38. {
   39. OH_LOG_INFO(LOG_APP, "MyObject::New called");

   41. napi_value newTarget;
   42. napi_get_new_target(env, info, &newTarget);
   43. if (newTarget != nullptr) {
   44. // 使用`new MyObject(...)`调用方式
   45. size_t argc = 1;
   46. napi_value args[1];
   47. napi_value jsThis;
   48. napi_get_cb_info(env, info, &argc, args, &jsThis, nullptr);

   50. double value = 0.0;
   51. napi_valuetype valuetype;
   52. napi_typeof(env, args[0], &valuetype);
   53. if (valuetype != napi_undefined) {
   54. napi_get_value_double(env, args[0], &value);
   55. }

   57. MyObject *obj = new MyObject(value);

   59. obj->env_ = env;
   60. // 通过napi_wrap_sendable将ArkTS Sendable对象jsThis与C++对象obj绑定
   61. napi_wrap_sendable(env, jsThis, reinterpret_cast<void *>(obj), MyObject::Destructor, nullptr);

   63. return jsThis;
   64. } else {
   65. // 使用`MyObject(...)`调用方式
   66. size_t argc = 1;
   67. napi_value args[1];
   68. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   70. napi_value cons;
   71. napi_get_reference_value(env, g_ref, &cons);
   72. napi_value instance;
   73. napi_new_instance(env, cons, argc, args, &instance);

   75. return instance;
   76. }
   77. }

   79. // 取出Native对象的值
   80. napi_value MyObject::GetValue(napi_env env, napi_callback_info info)
   81. {
   82. OH_LOG_INFO(LOG_APP, "MyObject::GetValue called");

   84. napi_value jsThis;
   85. napi_get_cb_info(env, info, nullptr, nullptr, &jsThis, nullptr);

   87. MyObject *obj;
   88. // 通过napi_unwrap_sendable将jsThis之前绑定的C++对象取出，并对其进行操作
   89. napi_unwrap_sendable(env, jsThis, reinterpret_cast<void **>(&obj));
   90. napi_value num;
   91. napi_create_double(env, obj->value_, &num);

   93. return num;
   94. }

   96. // 设置Native对象的值
   97. napi_value MyObject::SetValue(napi_env env, napi_callback_info info)
   98. {
   99. OH_LOG_INFO(LOG_APP, "MyObject::SetValue called");

   101. size_t argc = 1;
   102. napi_value value;
   103. napi_value jsThis;

   105. napi_get_cb_info(env, info, &argc, &value, &jsThis, nullptr);

   107. MyObject *obj;
   108. // 通过napi_unwrap_sendable将jsThis之前绑定的C++对象取出，并对其进行操作
   109. napi_unwrap_sendable(env, jsThis, reinterpret_cast<void **>(&obj));
   110. napi_get_value_double(env, value, &obj->value_);

   112. return nullptr;
   113. }

   115. // 给Native对象的值加1
   116. napi_value MyObject::PlusOne(napi_env env, napi_callback_info info)
   117. {
   118. OH_LOG_INFO(LOG_APP, "MyObject::PlusOne called");

   120. napi_value jsThis;
   121. napi_get_cb_info(env, info, nullptr, nullptr, &jsThis, nullptr);

   123. MyObject *obj;
   124. // 通过napi_unwrap_sendable将jsThis之前绑定的C++对象取出，并对其进行操作
   125. napi_unwrap_sendable(env, jsThis, reinterpret_cast<void **>(&obj));
   126. obj->value_ += 1;
   127. napi_value num;
   128. napi_create_double(env, obj->value_, &num);

   130. return num;
   131. }

   133. napi_value MyObject::Init(napi_env env, napi_value exports)
   134. {
   135. napi_value num;
   136. napi_create_double(env, 0, &num);
   137. napi_property_descriptor properties[] = {
   138. {"value", nullptr, nullptr, GetValue, SetValue, nullptr, napi_default, nullptr},
   139. {"plusOne", nullptr, PlusOne, nullptr, nullptr, nullptr, napi_default, nullptr},
   140. };

   142. napi_value cons;
   143. // 定义一个Sendable class MyObject
   144. napi_define_sendable_class(env, "MyObject", NAPI_AUTO_LENGTH, New, nullptr,
   145. sizeof(properties) / sizeof(properties[0]), properties, nullptr, &cons);

   147. napi_create_reference(env, cons, 1, &g_ref);
   148. // 在exports对象上挂载MyObject类
   149. napi_set_named_property(env, exports, "MyObject", cons);
   150. return exports;
   151. }

   153. EXTERN_C_START
   154. // 模块初始化
   155. static napi_value Init(napi_env env, napi_value exports)
   156. {
   157. MyObject::Init(env, exports);
   158. return exports;
   159. }
   160. EXTERN_C_END

   162. // 准备模块加载相关信息，将上述Init函数与本模块名等信息记录下来
   163. static napi_module nativeModule = {
   164. .nm_version = 1,
   165. .nm_flags = 0,
   166. .nm_filename = nullptr,
   167. .nm_register_func = Init,
   168. .nm_modname = "entry",
   169. .nm_priv = nullptr,
   170. .reserved = {0},
   171. };

   173. // 加载so时，自动调用该函数，将上述nativeModule模块注册到系统中
   174. extern "C" __attribute__((constructor)) void RegisterObjectWrapModule() { napi_module_register(&nativeModule); }
   ```
4. ArkTS侧在UI主线程中定义Sendable实例对象并传递给TaskPool子线程，子线程处理完数据后返回UI主线程，UI主线程可以继续访问该Sendable实例对象。

   ```
   1. // Index.ets
   2. import { MyObject } from 'libentry.so';
   3. import { taskpool } from '@kit.ArkTS';

   5. @Concurrent
   6. async function sum(object: MyObject) {
   7. object.value = 2000;
   8. let num = object.plusOne();
   9. console.info('taskpool thread num is ' + num); // 日志输出：taskpool thread num is 2001
   10. return num;
   11. }

   13. @Entry
   14. @Component
   15. struct Index {
   16. @State message: string = '使用Sendable对象进行线程间通信';

   18. build() {
   19. Row() {
   20. Column() {
   21. Button(this.message)
   22. .fontSize($r('app.float.page_text_font_size'))
   23. .fontWeight(FontWeight.Bold)
   24. .onClick( async () => {
   25. let object : MyObject = new MyObject(0);
   26. object.value = 1023;
   27. let num = object.plusOne();
   28. console.info('host thread num1 is ' + num); // 日志输出：host thread num1 is 1024
   29. let task = new taskpool.Task(sum, object);
   30. let result = await taskpool.execute(task);
   31. console.info('host thread result is ' + result); // 日志输出：host thread result is 2001
   32. console.info('host thread num2 is ' + object.value); // 日志输出：host thread num2 is 2001
   33. this.message = 'host thread num2 is ' + object.value;
   34. })
   35. }
   36. .width('100%')
   37. }
   38. .height('100%')
   39. }
   40. }
   ```
5. 修改与Index.d.ets同目录下的配置文件oh-package.json5，配置如下：

   ```
   1. {
   2. "name": "libentry.so",
   3. "types": "./Index.d.ets",
   4. "version": "1.0.0",
   5. "description": "Please describe the basic information."
   6. }
   ```
