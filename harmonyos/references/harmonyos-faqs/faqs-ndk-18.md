---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-18
title: 如何在Native侧调用ArkTS侧的系统能力
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧调用ArkTS侧的系统能力
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:31+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:455ed2f6e01fb426a9d8adade127bdc43b161ad5310651d907879a6613947e77
---

**问题详情**

系统提供了 ArkTS 接口，但未提供对应的 NAPI 接口。使用 C++ 代码实现业务逻辑时，部分系统能力需要依赖 ArkTS 接口。

**解决措施**

1. 通过napi\_load\_module接口加载模块。
2. 通过napi\_get\_named\_property接口获取模块属性。
3. 通过napi\_call\_function接口调用方法。

具体方法请参考以下示例代码，用于获取设备的屏幕宽高。

```
1. #include "CallSystemModule.h"
2. #include "napi/native_api.h"
3. #include <hilog/log.h>
4. #define LOG_TAG "Pure"

6. napi_value CallSystemModule::GetDisplaySize(napi_env env, napi_callback_info info) {
7. // Obtain the system library path on the arkts side
8. char path[64] = "@ohos.display";
9. size_t typeLen = 0;
10. napi_value string;
11. napi_create_string_utf8(env, path, typeLen, &string);
12. // Loading system libraries
13. napi_value sysModule;
14. napi_load_module(env, path, &sysModule);
15. // Retrieve the 'getDefault Display Sync' method from the system library
16. napi_value func = nullptr;
17. napi_get_named_property(env, sysModule, "getDefaultDisplaySync", &func);
18. napi_value funcResult;
19. napi_call_function(env, sysModule, func, 0, nullptr, &funcResult);
20. napi_value widthValue = nullptr;
21. napi_get_named_property(env, funcResult, "width", &widthValue);
22. double width;
23. napi_get_value_double(env, widthValue, &width);
24. OH_LOG_INFO(LOG_APP, "width: %{public}f", width);
25. napi_value heightValue = nullptr;
26. napi_get_named_property(env, funcResult, "height", &heightValue);
27. double height;
28. napi_get_value_double(env, heightValue, &height);
29. OH_LOG_INFO(LOG_APP, "height: %{public}f", height);
30. // By obtaining the width and height of the business, specific business logic can be further processed
31. return nullptr;
32. }
```

[CallSystemModule.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/CallSystemModule/CallSystemModule.cpp#L19-L50)
