---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-10
title: 如何在Native侧获取屏幕亮度
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧获取屏幕亮度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5b9821fce302cfda11963fec7915cf6eb1d1effc445a93cda2352c92cf4087c1
---

**问题详情**

如何在native层获取屏幕亮度，请提供代码示例。

**解决措施**

Native侧可通过napi\_load\_module接口访问到获取屏幕亮度的模块，然后调用它的get\_value函数获取屏幕亮度。

代码示例如下：

1. ArkTS侧传入模块名称。

   ```ts
   // Screenbrightness/src/main/ets/pages/Index.ets
   import testNapi from 'libscreenbrightness.so';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Get Screen Brightness';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               testNapi.napiLoadModule("@system.brightness");
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
2. 在Native侧获取屏幕亮度。

   ```cpp
   // Screenbrightness/src/main/cpp/napi_init.cpp
   #include "hilog/log.h"
   #include "napi/native_api.h"
   #include <string>

   #define LOG_TAG "Pure"

   static napi_value Success(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value args[1] = {nullptr};
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       napi_value obj = args[0];
       napi_value key;
       napi_value rv;
       std::string x = "value";
       napi_create_string_utf8(env, x.c_str(), 5, &key);
       napi_get_property(env, obj, key, &rv);
       uint32_t result;
       napi_get_value_uint32(env, rv, &result);
       OH_LOG_INFO(LOG_APP, "napi get brightness %{public}d", result);
       return nullptr;
   };
   static napi_value Fail(napi_env env, napi_callback_info info) { return nullptr; };
   static napi_value Complete(napi_env env, napi_callback_info info) { return nullptr; };
   static napi_value NapiLoadModule(napi_env env, napi_callback_info info) {
       napi_value result;
       size_t argc = 1;
       napi_value args[1] = {nullptr};
       napi_status get = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       char path[64] = {0};
       size_t typeLen = 0;
       napi_get_value_string_utf8(env, args[0], path, sizeof(path), &typeLen);
       napi_status status = napi_load_module(env, path, &result);
       if (status != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "napi_load_module failed");
           return nullptr;
       }
       napi_value outputObject;
       napi_get_named_property(env, result, "getValue", &outputObject);
       napi_value arg;
       napi_create_object(env, &arg);
       napi_property_descriptor desc[] = {
           {"success", nullptr, Success, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"fail", nullptr, Fail, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"complete", nullptr, Complete, nullptr, nullptr, nullptr, napi_default, nullptr}};
       napi_define_properties(env, arg, sizeof(desc) / sizeof(desc[0]), desc);
       napi_call_function(env, result, outputObject, 1, &arg, nullptr);
       return result;
   };
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports) {
       napi_property_descriptor desc[] = {
           {"napiLoadModule", nullptr, NapiLoadModule, nullptr, nullptr, nullptr, napi_default, nullptr},
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END

   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "screenbrightness",
       .nm_priv = ((void *)0),
       .reserved = {0},
   };
   extern "C" __attribute__((constructor)) void RegisterScreenBrightnessModule(void) { napi_module_register(&demoModule); }
   ```
3. 在Index.d.ts文件中声明映射到ArkTS侧的Native接口。

   ```ts
   // Screenbrightness/src/main/cpp/types/libscreenbrightness/Index.d.ts
   export const napiLoadModule: (a: string) => object;
   ```
4. 在CMakeLists文件中添加日志依赖库。

   ```text
   # Screenbrightness/src/main/cpp/CMakeLists.txt
   target_link_libraries(screenbrightness PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
