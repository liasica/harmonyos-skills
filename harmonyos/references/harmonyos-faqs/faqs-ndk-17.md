---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-17
title: Native侧如何获取ArkTS侧的应用包名
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧的应用包名
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b50bfe43f7c6acc8cfbf02ca77327c6200b5738674f7c98aa63ed5ae49a571b6
---

**问题详情**

ArkTS侧调用Native开放的接口时，如何在Native侧获取TS侧应用包名？

**解决措施**

Native代码可以使用Native Bundle接口获取应用的包名和appId等信息。使用时，需在CMakeLists文件中添加libbundle\_ndk.z.so依赖。

具体代码如下：

```cpp
#include "CGetAppPackageName.h" 
#include "napi/native_api.h" 
#include <bundle/native_interface_bundle.h> 
#include <cstdlib> 
#include "hilog/log.h" 
#define LOG_TAG "Pure" 
 
napi_value CGetAppPackageName::GetCurrentApplicationPackageName(napi_env env, napi_callback_info info) 
{ 
    // Call the Native interface to obtain application information 
    OH_NativeBundle_ApplicationInfo nativeApplicationInfo = OH_NativeBundle_GetCurrentApplicationInfo(); 
    // Convert the application package name obtained by the Native interface to the bundleName property in the JS object 
    napi_value bundleName; 
    napi_create_string_utf8(env, nativeApplicationInfo.bundleName, NAPI_AUTO_LENGTH, &bundleName); 
    OH_LOG_INFO(LOG_APP, "napi get application package name： %{public}s", nativeApplicationInfo.bundleName); 
    // Finally, to prevent memory leaks, manually release
    free(nativeApplicationInfo.bundleName); 
    return nullptr; 
}
```

更多相关信息可参考链接：

[NativeBundle开发指导](../harmonyos-guides/native-bundle-guidelines.md)
