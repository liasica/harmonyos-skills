---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-10
title: 如何在Native侧获取屏幕亮度
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧获取屏幕亮度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a3780a13b3dc15da625dd1b62727aff4bca8b0535cb4429b7ef924fbc8eae426
---

**问题详情**

如何在native层获取屏幕亮度，请提供代码示例。

**解决措施**

Native侧可通过napi\_load\_module接口访问到获取屏幕亮度的模块，然后调用它的get\_value函数获取屏幕亮度。

代码示例如下：

1. ArkTS侧传入模块名称。

   ```
   1. // Screenbrightness/src/main/ets/pages/Index.ets
   2. import testNapi from 'libscreenbrightness.so';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'Get Screen Brightness';

   11. build() {
   12. Row() {
   13. Column() {
   14. Text(this.message)
   15. .fontSize(50)
   16. .fontWeight(FontWeight.Bold)
   17. .onClick(() => {
   18. testNapi.napiLoadModule("@system.brightness");
   19. })
   20. }
   21. .width('100%')
   22. }
   23. .height('100%')
   24. }
   25. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/Screenbrightness/src/main/ets/pages/Index.ets#L21-L45)
2. 在Native侧获取屏幕亮度。

   ```
   1. // Screenbrightness/src/main/cpp/napi_init.cpp
   2. #include "hilog/log.h"
   3. #include "napi/native_api.h"
   4. #include <string>

   7. #define LOG_TAG "Pure"

   10. static napi_value Success(napi_env env, napi_callback_info info) {
   11. size_t argc = 1;
   12. napi_value args[1] = {nullptr};
   13. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   14. napi_value obj = args[0];
   15. napi_value key;
   16. napi_value rv;
   17. std::string x = "value";
   18. napi_create_string_utf8(env, x.c_str(), 5, &key);
   19. napi_get_property(env, obj, key, &rv);
   20. uint32_t result;
   21. napi_get_value_uint32(env, rv, &result);
   22. OH_LOG_INFO(LOG_APP, "napi get brightness %{public}d", result);
   23. return nullptr;
   24. };
   25. static napi_value Fail(napi_env env, napi_callback_info info) { return nullptr; };
   26. static napi_value Complete(napi_env env, napi_callback_info info) { return nullptr; };
   27. static napi_value NapiLoadModule(napi_env env, napi_callback_info info) {
   28. napi_value result;
   29. size_t argc = 1;
   30. napi_value args[1] = {nullptr};
   31. napi_status get = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   32. char path[64] = {0};
   33. size_t typeLen = 0;
   34. napi_get_value_string_utf8(env, args[0], path, sizeof(path), &typeLen);
   35. napi_status status = napi_load_module(env, path, &result);
   36. if (status != napi_ok) {
   37. OH_LOG_ERROR(LOG_APP, "napi_load_module failed");
   38. return nullptr;
   39. }
   40. napi_value outputObject;
   41. napi_get_named_property(env, result, "getValue", &outputObject);
   42. napi_value arg;
   43. napi_create_object(env, &arg);
   44. napi_property_descriptor desc[] = {
   45. {"success", nullptr, Success, nullptr, nullptr, nullptr, napi_default, nullptr},
   46. {"fail", nullptr, Fail, nullptr, nullptr, nullptr, napi_default, nullptr},
   47. {"complete", nullptr, Complete, nullptr, nullptr, nullptr, napi_default, nullptr}};
   48. napi_define_properties(env, arg, sizeof(desc) / sizeof(desc[0]), desc);
   49. napi_call_function(env, result, outputObject, 1, &arg, nullptr);
   50. return result;
   51. };
   52. EXTERN_C_START
   53. static napi_value Init(napi_env env, napi_value exports) {
   54. napi_property_descriptor desc[] = {
   55. {"napiLoadModule", nullptr, NapiLoadModule, nullptr, nullptr, nullptr, napi_default, nullptr},
   56. };
   57. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   58. return exports;
   59. }
   60. EXTERN_C_END

   63. static napi_module demoModule = {
   64. .nm_version = 1,
   65. .nm_flags = 0,
   66. .nm_filename = nullptr,
   67. .nm_register_func = Init,
   68. .nm_modname = "screenbrightness",
   69. .nm_priv = ((void *)0),
   70. .reserved = {0},
   71. };
   72. extern "C" __attribute__((constructor)) void RegisterScreenBrightnessModule(void) { napi_module_register(&demoModule); }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/Screenbrightness/src/main/cpp/napi_init.cpp#L21-L92)
3. 在Index.d.ts文件中声明映射到ArkTS侧的Native接口。

   ```
   1. // Screenbrightness/src/main/cpp/types/libscreenbrightness/Index.d.ts
   2. export const napiLoadModule: (a: string) => object;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/Screenbrightness/src/main/cpp/types/libscreenbrightness/Index.d.ts#L21-L22)
4. 在CMakeLists文件中添加日志依赖库。

   ```
   1. # Screenbrightness/src/main/cpp/CMakeLists.txt
   2. target_link_libraries(screenbrightness PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/Screenbrightness/src/main/cpp/CMakeLists.txt#L18-L19)
