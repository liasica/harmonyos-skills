---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-45
title: 如何在Native侧构建一个ArkTS对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧构建一个ArkTS对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:19050a6cd79b214eb58524de3fd0cb6f4c9d6ce9c8b0c69473c82550bfea1c20
---

1. 调用接口napi\_create\_object创建对象。

   ```cpp
   // Create object arg_order in the native layer
   napi_value arg_object;
   napi_create_object(env, &arg_object);
   ```
2. 调用接口napi\_set\_named\_property给对象属性赋值。

   ```cpp
   napi_value testNum, testString;
   // Set the property testNum and assign a value of 123 to the arg_order object created above
   napi_create_int32(env, 123, &testNum);
   napi_set_named_property(env, arg_object, "testNum", testNum);
   // Set the property testString and assign 'Pure' to the arg_order object created above
   napi_create_string_utf8(env, "Pure", NAPI_AUTO_LENGTH, &testString);
   napi_set_named_property(env, arg_object, "testString", testString);
   ```
