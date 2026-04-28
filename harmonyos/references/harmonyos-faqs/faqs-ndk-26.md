---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-26
title: 如何在C++调用从ArkTS传递过来的function
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 如何在C++调用从ArkTS传递过来的function
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f2afec28708c0e7c4c6f2845b08277abc417729aed82cc67a94e8878d998aca8
---

1. 在index.d.ts文件中，提供ArkTS侧的接口方法。

   ```
   1. export const nativeCallArkTS: (a: object) => number;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/Index.d.ts#L21-L21)
2. 实现Native侧的NativeCallArkTS接口，具体代码如下：

   ```
   1. static napi_value NativeCallArkTS(napi_env env, napi_callback_info info)
   2. {
   3. size_t argc = 1;
   4. // Declare parameter array
   5. napi_value args[1] = {nullptr};

   7. // Retrieve the incoming parameters and sequentially place them into the parameter array
   8. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

   10. // Create an int as a parameter for ArkTS
   11. napi_value argv = nullptr;
   12. napi_create_int32(env, 2, &argv );

   14. // Call the incoming callback and return its result
   15. napi_value result = nullptr;
   16. napi_call_function(env, nullptr, args[0], 1, &argv, &result);
   17. return result;
   18. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CPlusCallArkTSFunc/src/main/cpp/napi_init.cpp#L22-L39)
3. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。

   ```
   1. // entry/src/main/ets/pages/Index.ets
   2. // Introduce native capabilities through import.
   3. import nativeModule from 'libentry.so'

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'Test Node-API nativeCallArkTS result: ';
   9. build() {
   10. Row() {
   11. Column() {
   12. // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
   13. Text(this.message)
   14. .fontSize(50)
   15. .fontWeight(FontWeight.Bold)
   16. .onClick(() => {
   17. this.message += nativeModule.nativeCallArkTS((a: number)=> {
   18. return a * 2;
   19. });
   20. })
   21. }
   22. .width('100%')
   23. }
   24. .height('100%')
   25. }
   26. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CPlusCallArkTSFunc/src/main/ets/pages/Index.ets#L20-L45)

**参考链接**

[Native侧方法的实现](../harmonyos-guides/use-napi-process.md#native侧方法的实现)
