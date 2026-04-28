---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-41
title: ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:464ab61b3f5aa8c10654626b3a8b00ab2c861c7a183972430457183b8a118fc2
---

1. 使用具体类型如 Record<string, number> 或 Map<string, number> 接收并修改数据。
2. 在ArkTS侧的函数中返回修改后的数据，在Native层通过napi\_call\_function可以获取到修改的数据。
3. 在Native侧，目前只能使用napi\_set\_property对对象的属性进行设置。

示例代码如下：

ArkTS侧

```
1. import testNapi from 'libentry.so';
2. // ...
3. build() {
4. // ...
5. .onClick(() => {
6. let data: Record<string, number> = testNapi.callbackToArkTS((value: object) => {
7. let obj: Record<string, number> = value as Record<string, number>;
8. console.info("pre type:" + obj["type"].toString())
9. console.info(JSON.stringify(value))
10. obj["type"] += 10;
11. return value;
12. });
13. console.info(JSON.stringify(data))
14. })
15. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/callbackToArkts/src/main/ets/pages/Index.ets#L3-L30)

Native侧

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"
3. #undef LOG_DOMAIN
4. #undef LOG_TAG
5. #define LOG_DOMAIN 0x3200
6. #define LOG_TAG "MY_TAG"

8. static bool Napi_AddPropertyInt32(napi_env env, napi_value obj, const char *key, int32_t value) {
9. napi_value key_napi = nullptr;
10. napi_status status = napi_create_string_utf8(env, key, NAPI_AUTO_LENGTH, &key_napi);
11. napi_value value_napi = nullptr;
12. status = napi_create_int32(env, value, &value_napi);
13. status = napi_set_property(env, obj, key_napi, value_napi);
14. return true;
15. }
16. static  napi_value CallbackToArkTS(napi_env env, napi_callback_info info) {
17. size_t argc = 1;
18. napi_value args[1] = {nullptr};
19. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
20. // Native callback to ArkTS layer object
21. napi_value argv = nullptr;
22. napi_create_object(env, &argv);
23. Napi_AddPropertyInt32(env, argv, "type", 1);
24. Napi_AddPropertyInt32(env, argv, "index", 2);
25. // Native callback to ArkTS layer
26. napi_value result = nullptr;
27. napi_call_function(env, NULL, args[0], 1, &argv, &result);
28. // Obtain the modified object of ArkTS
29. napi_value typeNumber = nullptr;
30. napi_get_named_property(env, result, "type", &typeNumber);
31. int32_t number;
32. napi_get_value_int32(env, typeNumber, &number);
33. OH_LOG_INFO(LOG_APP, "ArkTS modified type：%{public}d", number);
34. // Return the modified object
35. return result;
36. }
37. EXTERN_C_START
38. static napi_value Init(napi_env env, napi_value exports)
39. {
40. napi_property_descriptor desc[] = {
41. { "callbackToArkTS", nullptr, CallbackToArkTS, nullptr, nullptr, nullptr, napi_default, nullptr }
42. };
43. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
44. return exports;
45. }
46. EXTERN_C_END
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/callbackToArkts/src/main/cpp/napi_init.cpp#L3-L48)

index.d.ts

```
1. export const callbackToArkTS: (a: object) => Record<string, number>
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/callbackToArkts/src/main/cpp/types/libentry/Index.d.ts#L2-L2)
