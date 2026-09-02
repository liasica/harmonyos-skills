---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-26
title: 如何在C++调用从ArkTS传递过来的function
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 如何在C++调用从ArkTS传递过来的function
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b662968d2a92705f364c0699b71dee1107a090508e289d2d5b1fdca0fef7d941
---

1. 在index.d.ts文件中，提供ArkTS侧的接口方法。

   ```ts
   export const nativeCallArkTS: (a: object) => number;
   ```
2. 实现Native侧的NativeCallArkTS接口，具体代码如下：

   ```cpp
   static napi_value NativeCallArkTS(napi_env env, napi_callback_info info) 
   {     
       size_t argc = 1; 
       // Declare parameter array 
       napi_value args[1] = {nullptr}; 
    
       // Retrieve the incoming parameters and sequentially place them into the parameter array 
       napi_get_cb_info(env, info, &argc, args , nullptr, nullptr); 
    
       // Create an int as a parameter for ArkTS
       napi_value argv = nullptr;     
       napi_create_int32(env, 2, &argv ); 
    
       // Call the incoming callback and return its result
       napi_value result = nullptr; 
       napi_call_function(env, nullptr, args[0], 1, &argv, &result); 
       return result; 
   }
   ```
3. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。

   ```ts
   // entry/src/main/ets/pages/Index.ets
   // Introduce native capabilities through import.
   import nativeModule from 'libentry.so'

   @Entry
   @Component
   struct Index {
     @State message: string = 'Test Node-API nativeCallArkTS result: ';
     build() {
       Row() {
         Column() {
           // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message += nativeModule.nativeCallArkTS((a: number)=> {
                 return a * 2;
               });
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

**参考链接**

[Native侧方法的实现](../harmonyos-guides/use-napi-process.md#native侧方法的实现)
