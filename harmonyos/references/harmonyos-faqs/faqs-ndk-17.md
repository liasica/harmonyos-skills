---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-17
title: Native侧如何获取ArkTS侧的应用包名
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧的应用包名
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8bea5067c2d18899964b29e0483fc1e23d19e258550552bcb839da73f7c5f0ad
---

**问题详情**

ArkTS侧调用Native开放的接口时，如何在Native侧获取TS侧应用包名？

**解决措施**

Native代码可以使用Native Bundle接口获取应用的包名和appId等信息。使用时，需在CMakeLists文件中添加libbundle\_ndk.z.so依赖。

具体代码如下：

```
1. #include "CGetAppPackageName.h"
2. #include "napi/native_api.h"
3. #include <bundle/native_interface_bundle.h>
4. #include <cstdlib>
5. #include "hilog/log.h"
6. #define LOG_TAG "Pure"

8. napi_value CGetAppPackageName::GetCurrentApplicationPackageName(napi_env env, napi_callback_info info)
9. {
10. // Call the Native interface to obtain application information
11. OH_NativeBundle_ApplicationInfo nativeApplicationInfo = OH_NativeBundle_GetCurrentApplicationInfo();
12. // Convert the application package name obtained by the Native interface to the bundleName property in the JS object
13. napi_value bundleName;
14. napi_create_string_utf8(env, nativeApplicationInfo.bundleName, NAPI_AUTO_LENGTH, &bundleName);
15. OH_LOG_INFO(LOG_APP, "napi get application package name： %{public}s", nativeApplicationInfo.bundleName);
16. // Finally, to prevent memory leaks, manually release
17. free(nativeApplicationInfo.bundleName);
18. return nullptr;
19. }
```

[CGetAppPackageName.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/CGetAppPackageName/CGetAppPackageName.cpp#L19-L37)

更多相关信息可参考链接：

[NativeBundle开发指导](../harmonyos-guides/native-bundle-guidelines.md)
