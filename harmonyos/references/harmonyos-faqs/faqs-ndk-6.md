---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-6
title: ArkTS侧与Native侧如何进行map数据交互
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧与Native侧如何进行map数据交互
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a54e1bd0ab874b73403919611f232b5713b25826d6f601ab5ddbb54678a917df
---

当前没有专门的接口用于在ArkTS侧与Native侧之间转换map。要实现map（二维数组）的数据交互，可以读取map中的数据并传递到Native侧进行重组。

参考代码如下：

在ArkTS中声明hashmap，获取数据并传递到Native侧。

```ts
let hashmap: HashMap<string, number> = new HashMap()
hashmap.set("Abc", 123)
hashmap.set("Bcd", 234)
hashmap.set("Cde", 345)
for (let key of hashmap.keys()) {
  testNapi.mapDemo(key, hashmap.get(key))
  console.info(`key is ${key}, value is ${hashmap.get(key)}`)
}
```

获取数据并重组为map。

```cpp
#define LOG_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG_TAG "MY_TAG"  // Global tag macro, identifying module log tag 
#include "NativeMap.h"
#include "hilog/log.h"
#include <map>
#include <string>
std::map<std::string, int> testmap;
napi_value NativeMap::MapDemo(napi_env env, napi_callback_info info) {
    size_t requireArgc = 2;
    size_t argc = 2;
    napi_value args[2] = {nullptr};

    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    char str1[1024];
    size_t str1_len;
    napi_get_value_string_utf8(env, args[0], str1, 100, &str1_len);
    int num;
    napi_get_value_int32(env, args[1], &num);
    testmap.insert(std::make_pair(str1, num));
    for(auto e: testmap){
        OH_LOG_ERROR(LOG_APP, "key is: %{public}s, value is  %{public}d", (e.first).c_str(), e.second);
    }
    
    return nullptr;
}
```
