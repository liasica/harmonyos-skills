---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-20
title: 如何在Native侧直接使用其他模块的ArkTS方法
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧直接使用其他模块的ArkTS方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c4610a4a4f8399ca11ee40308f42959ed38d9e0b88ca02d22ba32bc251baf87b
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

```
1. // src/main/ets/pages/Test.ets
2. let value = 123;
3. function test() {
4. console.log('Hello HarmonyOS');
5. }
6. export {value, test};
```

[Test.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CallCustomMethod/src/main/ets/pages/Test.ets#L19-L24)

在模块级build-profile.json5文件中进行以下配置：

注意是在模块级的build-profile.json5文件中配置，而非工程级。同时需要确保"sources"配置项为正确的Test.ets文件路径。

```
1. "buildOption": {
2. "externalNativeOptions": {
3. "path": "./src/main/cpp/CMakeLists.txt",
4. "arguments": "",
5. "cppFlags": "",
6. },
7. "arkOptions": {
8. "runtimeOnly": {
9. "sources": [
10. "./src/main/ets/pages/Test.ets"
11. ]
12. }
13. },
14. },
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CallCustomMethod/build-profile.json5#L7-L20)

使用napi\_load\_module加载Test文件，调用函数test，并获取变量value。

```
1. #include "napi/native_api.h"
2. #include <string>

4. static napi_value LoadModule(napi_env env, napi_callback_info info) {
5. napi_value result;
6. // 1. Load modules from the Test file using napi_load_module
7. napi_status status = napi_load_module(env, "ets/pages/Test", &result);
8. napi_value testFn;
9. // 2. Use napi_get_named_property to obtain the test function
10. napi_get_named_property(env, result, "test", &testFn);
11. // 3. Call the function test using napi_call_function
12. napi_call_function(env, result, testFn, 0, nullptr, nullptr);
13. napi_value value;
14. napi_value key;
15. std::string keyStr = "value";
16. napi_create_string_utf8(env, keyStr.c_str(), keyStr.size(), &key);
17. // 4. Get variable value using napi_get_property
18. napi_get_property(env, result, key, &value);
19. return value;
20. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CallCustomMethod/src/main/cpp/napi_init.cpp#L19-L38)
