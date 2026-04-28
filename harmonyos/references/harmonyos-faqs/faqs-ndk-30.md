---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-30
title: Native如何调ArkTS的方法
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native如何调ArkTS的方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:35+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:8a41868a1b1b16ddbb599dafa5f3188bd1a68620885cf5b24f806ae4d6ba4505
---

1. 在index.d.ts文件中提供 ArkTS 接口方法。

```
1. export const nativeCallArkTS: (a: object) => number;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/types/libentry/Index.d.ts#L11-L12)

2. 实现Native侧的NativeCallArkTS接口，代码如下：

```
1. static napi_value NativeCallArkTS(napi_env env, napi_callback_info info)
2. {
3. size_t argc = 1;
4. // Declaring parameter array ARG
5. napi_value args[1] = { nullptr };

7. // Retrieve the passed parameters and place them in the parameter array 'args'
8. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

10. // Create int as an input parameter for ArkTS
11. napi_value argv = nullptr;
12. napi_create_int32(env, 2, &argv );

14. // Call the incoming callback and return the result
15. napi_value result = nullptr;
16. napi_call_function(env, nullptr, args[0], 1, &argv, &result);
17. return result;
18. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/napi_init.cpp#L46-L63)

3. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。

entry/src/main/ets/pages/Index.ets

```
1. // Introduce native capabilities through import.
2. import nativeModule from 'libentry.so'

5. @Entry
6. @Component
7. struct InvokeArkTSMethod {
8. @State message: string = 'Test Node-API nativeCallArkTS result: ';

11. build() {
12. Row() {
13. Column() {
14. // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
15. Text(this.message)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .onClick(() => {
19. this.message += nativeModule.nativeCallArkTS((a: number) => {
20. return a * 2;
21. });
22. })
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/Index.ets#L5-L32)

**参考链接**

[Node-API典型使用场景](../harmonyos-guides/napi-scenarios.md)
