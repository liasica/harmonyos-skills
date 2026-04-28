---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-3
title: 如何对多个C++源文件中接口进行导出声明
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何对多个C++源文件中接口进行导出声明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:91a71e7501707ddf00ad54a2de59c6db3a9611f63f5d48cac61679714a833455
---

**问题现象**

DevEco Studio创建的默认C++工程中是只有一个hello.cpp，想在C++侧加一个 a.cpp文件，并且希望可以从a.cpp文件中导出一个函数给ArkTS侧调用，具体如何实现？

**解决措施**

首先需要引入对应的a.cpp对应的头文件a.h，然后在初始化函数Init中进行接口映射，最后通过index.d.ts文件将接口导出。参考代码如下：

在NumberType.cpp文件中实现Add函数业务功能。

```
1. #include "NumberType.h" // Import header file
2. // NumberType is the class name, and Add is its function
3. napi_value NumberType::Add(napi_env env, napi_callback_info info) {
4. // ... Business Function Implementation Code
5. // ...
6. }
```

[NumberType.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/cpplib/src/main/cpp/NumberType.cpp#L26-L54)

在hello.cpp文件中引入头文件并初始化函数Init中进行接口映射。

```
1. #include "NumberType.h"
2. #include "napi/native_api.h"

4. EXTERN_C_START
5. static napi_value Init(napi_env env, napi_value exports)
6. {
7. /* Associate the externally provided interface with the written method, for example, associate add with the Add
8. * method.
9. */
10. napi_property_descriptor desc[] = {
11. { "add", nullptr, NumberType::Add, nullptr, nullptr, nullptr, napi_default, nullptr }
12. };
13. // napi_define_properties construct a return value that contains a list of methods that correspond.
14. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
15. return exports;
16. }
17. EXTERN_C_END
```

[hello.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/cpplib/src/main/cpp/hello.cpp#L5-L21)

在接口声明文件（index.d.ts）中对要传递给ArkTS侧的函数进行导出。

```
1. export const add: (a: number, b: number) => number;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/cpplib/src/main/cpp/types/libcpplib/Index.d.ts#L5-L5)

**参考链接**

[基于XComponent组件实现图像绘制功能](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-XComponent)
