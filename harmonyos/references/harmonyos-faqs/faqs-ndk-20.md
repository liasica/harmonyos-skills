---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-20
title: 如何在Native侧直接使用其他模块的ArkTS方法
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧直接使用其他模块的ArkTS方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:667d42f10c42ad0afcfe255f58407ad3d5c64c0d6303c07ea146058a0d4c2a5a
---

**问题详情**

在ArkTS侧已经定义了接口，但未实现对应的NDK接口。当使用C++代码实现业务逻辑时，可以直接使用已有的ArkTS接口。

**解决措施**

可通过napi\_load\_module接口实现对ArkTS文件中的接口的调用。具体步骤如下：

1. 通过napi\_load\_module接口加载模块。
2. 通过napi\_get\_named\_property接口获取模块属性。
3. 通过napi\_call\_function接口调用方法。

   具体方法请参考以下示例代码，展示如何加载ArkTS文件中的模块。

声明ArkTS侧方法：

```ts
// src/main/ets/pages/Test.ets
let value = 123;
function test() {
  console.log('Hello HarmonyOS');
}
export {value, test};
```

在模块级build-profile.json5文件中进行以下配置：

注意是在模块级的build-profile.json5文件中配置，而非工程级。同时需要确保"sources"配置项为正确的Test.ets文件路径。

```json
"buildOption": {
  "externalNativeOptions": {
    "path": "./src/main/cpp/CMakeLists.txt",
    "arguments": "",
    "cppFlags": "",
  },
  "arkOptions": {
    "runtimeOnly": {
      "sources": [
        "./src/main/ets/pages/Test.ets"
      ]
    }
  },
},
```

使用napi\_load\_module加载Test文件，调用函数test，并获取变量value。

```cpp
#include "napi/native_api.h" 
#include <string> 
 
static napi_value LoadModule(napi_env env, napi_callback_info info) { 
    napi_value result; 
    // 1. Load modules from the Test file using napi_load_module 
    napi_status status = napi_load_module(env, "ets/pages/Test", &result); 
    napi_value testFn; 
    // 2. Use napi_get_named_property to obtain the test function 
    napi_get_named_property(env, result, "test", &testFn); 
    // 3. Call the function test using napi_call_function 
    napi_call_function(env, result, testFn, 0, nullptr, nullptr); 
    napi_value value; 
    napi_value key; 
    std::string keyStr = "value"; 
    napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key); 
    // 4. Get variable value using napi_get_property 
    napi_get_property(env, result, key, &value); 
    return value; 
}
```
