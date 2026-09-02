---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-18
title: 如何在Native侧调用ArkTS侧的系统能力
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧调用ArkTS侧的系统能力
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e9c3c1421c3500f0b7dbb890d68ce1a6586ca96eb5e5d77591714efcb49c521
---

**问题详情**

系统提供了 ArkTS 接口，但未提供对应的 NAPI 接口。使用 C++ 代码实现业务逻辑时，部分系统能力需要依赖 ArkTS 接口。

**解决措施**

1. 通过napi\_load\_module接口加载模块。
2. 通过napi\_get\_named\_property接口获取模块属性。
3. 通过napi\_call\_function接口调用方法。

具体方法请参考以下示例代码，用于获取设备的屏幕宽高。

```cpp
#include "CallSystemModule.h" 
#include "napi/native_api.h" 
#include <hilog/log.h> 
#define LOG_TAG "Pure" 
 
napi_value CallSystemModule::GetDisplaySize(napi_env env, napi_callback_info info) { 
    // Obtain the system library path on the arkts side
    char path[64] = "@ohos.display"; 
    size_t typeLen = 0; 
    napi_value string; 
    napi_create_string_utf8(env, path, typeLen, &string); 
    // Loading system libraries 
    napi_value sysModule; 
    napi_load_module(env, path, &sysModule); 
    // Retrieve the 'getDefault Display Sync' method from the system library 
    napi_value func = nullptr; 
    napi_get_named_property(env, sysModule, "getDefaultDisplaySync", &func); 
    napi_value funcResult; 
    napi_call_function(env, sysModule, func, 0, nullptr, &funcResult); 
    napi_value widthValue = nullptr; 
    napi_get_named_property(env, funcResult, "width", &widthValue); 
    double width; 
    napi_get_value_double(env, widthValue, &width); 
    OH_LOG_INFO(LOG_APP, "width: %{public}f", width); 
    napi_value heightValue = nullptr; 
    napi_get_named_property(env, funcResult, "height", &heightValue); 
    double height; 
    napi_get_value_double(env, heightValue, &height); 
    OH_LOG_INFO(LOG_APP, "height: %{public}f", height); 
    // By obtaining the width and height of the business, specific business logic can be further processed
    return nullptr; 
}
```
