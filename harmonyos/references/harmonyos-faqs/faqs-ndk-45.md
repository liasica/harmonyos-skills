---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-45
title: 如何在Native侧构建一个ArkTS对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧构建一个ArkTS对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c8c04bc3834714f59edd614d7edebfbe70089c520fe5a79669e00345755d7c81
---

1. 调用接口napi\_create\_object创建对象。

   ```
   1. // Create object arg_order in the native layer
   2. napi_value arg_object;
   3. napi_create_object(env, &arg_object);
   ```

   [napi\_create\_arkts.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/NativeCpp/napi_create_arkts.cpp#L11-L13)
2. 调用接口napi\_set\_named\_property给对象属性赋值。

   ```
   1. napi_value testNum, testString;
   2. // Set the property testNum and assign a value of 123 to the arg_order object created above
   3. napi_create_int32(env, 123, &testNum);
   4. napi_set_named_property(env, arg_object, "testNum", testNum);
   5. // Set the property testString and assign 'Pure' to the arg_order object created above
   6. napi_create_string_utf8(env, "Pure", NAPI_AUTO_LENGTH, &testString);
   7. napi_set_named_property(env, arg_object, "testString", testString);
   ```

   [napi\_create\_arkts.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/NativeCpp/napi_create_arkts.cpp#L17-L23)
