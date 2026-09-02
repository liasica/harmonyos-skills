---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-12
title: 如何在Native侧添加debug版本声明
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧添加debug版本声明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:812f38393645dc1d5b7f2e919bb3a9d2c4d19ac999180bf5a6c949dfed13bfb3
---

**问题详情**

尝试过在需要编译的库的build-profile.json5文件中，buildOptionSet字段中添加 { "name": "debug", "externalNativeOptions": { "arguments": "-DDEBUG=1" } } 或在buildOption.externalNativeOptions.arguments字段中设置"-DDEBUG=1"， 在使用debug模式运行时均不会执行#ifdef DEBUG中的语句。

**解决措施**

1.CMakeLists.txt文件中增加如下语句：

```text
if(CMAKE_BUILD_TYPE STREQUAL Debug)
    add_definitions(-D_DEBUG)
endif()
```

2.C++文件中增加如下代码：

```cpp
#include "napi/native_api.h" 
#include "hilog/log.h" 
#define LOG_TAG "Pure" 
 
static napi_value DefDebug(napi_env env, napi_callback_info info) { 
#ifdef _DEBUG 
    OH_LOG_INFO(LOG_APP, "debug enter Project"); 
#else 
    OH_LOG_INFO(LOG_APP, "release enter Project"); 
#endif 
    return nullptr; 
}
```
