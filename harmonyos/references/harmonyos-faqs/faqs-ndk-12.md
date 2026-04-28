---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-12
title: 如何在Native侧添加debug版本声明
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧添加debug版本声明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9821113a2d6853f1f0600eef6a8e363d33a7cad071dd3de5181923db9093b4ed
---

**问题详情**

尝试过在需要编译的库的build-profile.json5文件中，buildOptionSet字段中添加 { "name": "debug", "externalNativeOptions": { "arguments": "-DDEBUG=1" } } 或在buildOption.externalNativeOptions.arguments字段中设置"-DDEBUG=1"， 在使用debug模式运行时均不会执行#ifdef DEBUG中的语句。

**解决措施**

1.CMakeLists.txt文件中增加如下语句：

```
1. if(CMAKE_BUILD_TYPE STREQUAL Debug)
2. add_definitions(-D_DEBUG)
3. endif()
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/CMakeLists.txt#L10-L12)

2.C++文件中增加如下代码：

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"
3. #define LOG_TAG "Pure"

5. static napi_value DefDebug(napi_env env, napi_callback_info info) {
6. #ifdef _DEBUG
7. OH_LOG_INFO(LOG_APP, "debug enter Project");
8. #else
9. OH_LOG_INFO(LOG_APP, "release enter Project");
10. #endif
11. return nullptr;
12. }
```

[DefDebug.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/NativeCpp/DefDebug.cpp#L8-L19)
