---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-15
title: 如何将Native侧的函数封装到类中导出到ArkTS侧使用
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何将Native侧的函数封装到类中导出到ArkTS侧使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5b2007ff5a542e3632e62d4f6770fc66b2fc306b0b8b8101e729fa10e7165145
---

**问题详情**

现有一个C++库，提供的接口以类方法形式提供。Native侧可以封装成普通函数的形式供上层调用，也可以保持原有类方法的形式。

**解决措施**

Native侧提供以下类方法供上层调用。

具体代码如下：

1. Native侧封装类方法。

   ```cpp
   #include "napi/native_api.h" 
   #include <string> 
    
   static napi_value Sub(napi_env env, napi_callback_info info) { 
       size_t requireArgc = 2; 
       size_t argc = 2; 
       napi_value args[2] = {nullptr}; 
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
       napi_valuetype valuetype0; 
       napi_typeof(env, args[0], &valuetype0); 
       napi_valuetype valuetype1; 
       napi_typeof(env, args[1], &valuetype1); 
       double value0; 
       napi_get_value_double(env, args[0], &value0); 
       double value1; 
       napi_get_value_double(env, args[1], &value1); 
       napi_value sub; 
       napi_create_double(env, value0 - value1, &sub); 
       return sub; 
   } 
   static napi_value Sum(napi_env env, napi_callback_info info) { 
       size_t requireArgc = 2; 
       size_t argc = 2; 
       napi_value args[2] = {nullptr}; 
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
       napi_valuetype valuetype0; 
       napi_typeof(env, args[0], &valuetype0); 
       napi_valuetype valuetype1; 
       napi_typeof(env, args[1], &valuetype1); 
       double value0; 
       napi_get_value_double(env, args[0], &value0); 
       double value1; 
       napi_get_value_double(env, args[1], &value1); 
       napi_value sum; 
       napi_create_double(env, value0 + value1, &sum); 
       return sum; 
   } 
   napi_value Constructor(napi_env env, napi_callback_info info) { return nullptr; } 
   EXTERN_C_START 
   static napi_value Init(napi_env env, napi_value exports) { 
       std::string class_name = "TestEntryA"; 
       napi_property_descriptor desc[] = {{"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi_static, nullptr}, 
                                          {"sum", nullptr, Sum, nullptr, nullptr, nullptr, napi_static, nullptr}}; 
       napi_value defined_class = nullptr; 
       napi_define_class(env, class_name.c_str(), class_name.length(), Constructor, nullptr, 2, desc, &defined_class); 
       const napi_property_descriptor exports_desc[] = { 
           {class_name.c_str(), nullptr, nullptr, nullptr, nullptr, defined_class, napi_default, nullptr}, 
       }; 
       napi_define_properties(env, exports, 2, exports_desc); 
       return exports; 
   } 
   EXTERN_C_END
   ```
2. 在Index.d.ts文件中导出类及其方法。

   ```ts
   export declare class TestEntryA {
     static sub (a: number, b: number) : number;
     static sum (a: number, b: number) : number;
   }
   ```
3. 在ArkTS侧通过类调用方法。

   ```ts
   import { TestEntryA } from 'libfuncencapsulation.so';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Function Encapsulation';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               console.info(`Test NAPI 2 + 3 = ${TestEntryA.sum(2, 3)}`);
               console.info(`Test NAPI 2 - 3 = ${TestEntryA.sub(2, 3)}`);
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
