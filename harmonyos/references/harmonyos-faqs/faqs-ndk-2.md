---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-2
title: 在Native侧如何处理ArkTS侧传入的字符串被截断的异常场景
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在Native侧如何处理ArkTS侧传入的字符串被截断的异常场景
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:28+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:70d5ee668d4afdf540627de2f102c4fb43e02769fafba78f5f3f6990a3635f49
---

**问题现象**

获取ArkTS侧传入的字符串到char数组时，字符串未完整获取。

**原因**

原因一：char数组长度小于字符串长度。

原因二：使用接口napi\_get\_value\_string\_utf8()获取字符串时，第四个参数数值小于传入的字符串长度。

**解决措施**

假设info中存储的ArkTS参数为“abcdefghigk”。

原因一：字符数组长度不足。

```
1. static napi_value TestFunc(napi_env env, napi_callback_info info)
2. {
3. size_t argc = 1;
4. napi_value args[1] = {nullptr};
5. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

7. size_t len = 0;
8. char buf[5];                                                            // Allocate a char array of length 5
9. napi_get_value_string_utf8(env, args[0], buf, 1024, &len);  // Get string, buf result is' abcde '
10. // ...
11. }
```

[Test1.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/Test/Test1.cpp#L11-L21)

设置char数组长度为5，字符串被截断：buf为"abcde"。

原因二：使用接口napi\_get\_value\_string\_utf8()获取字符串时，第四个参数数值太小，没超过传入的字符串长度。

```
1. static napi_value TestFunc(napi_env env, napi_callback_info info)
2. {
3. size_t argc = 1;
4. napi_value args[1] = {nullptr};
5. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

7. size_t len = 0;
8. char buf[1024];
9. napi_get_value_string_utf8(env, args[0], buf, 5, &len);                    // Get string, buf result is' abcde '
10. // ...
11. }
```

[Test2.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/Test/Test2.cpp#L11-L21)

设置第四个参数值为5，字符串被截断：buf为"abcd"，终止符'\0'占用一个字符空间。

确保char数组的长度大于或等于字符串本身的长度，并且在调用napi\_get\_value\_string\_utf8()获取字符串时，第四个参数的值足够大。首先，调用napi\_get\_value\_string\_utf8函数来获取字符串的长度，然后根据该长度动态分配char数组的内存空间。在分配内存时，建议将长度加 1，以便为字符串的终止符\0留出空间。

参考代码如下：

```
1. napi_value Test::TestFunc(napi_env env, napi_callback_info info) {
2. size_t argc = 1;
3. napi_value args[1] = {nullptr};
4. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

6. size_t len = 0;
7. napi_get_value_string_utf8(env, args[0], nullptr, 0, &len);   // Get string length to len
8. char *buf = new char[len + 1];                                // Allocate a char array of appropriate size
9. napi_get_value_string_utf8(env, args[0], buf, len + 1, &len); // get string
10. OH_LOG_ERROR(LOG_APP, "result is:  b:%{public}s.", buf);
11. return nullptr;
12. }
```

[Test.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/Test/Test.cpp#L16-L27)
