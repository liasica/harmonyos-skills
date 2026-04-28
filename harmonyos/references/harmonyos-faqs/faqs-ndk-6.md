---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-6
title: ArkTS侧与Native侧如何进行map数据交互
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧与Native侧如何进行map数据交互
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:248a2392a62349fea6b2e93e6f6731f1bce448601cdbfc01ef0db2cef155f82f
---

当前没有专门的接口用于在ArkTS侧与Native侧之间转换map。要实现map（二维数组）的数据交互，可以读取map中的数据并传递到Native侧进行重组。

参考代码如下：

在ArkTS中声明hashmap，获取数据并传递到Native侧。

```
1. let hashmap: HashMap<string, number> = new HashMap()
2. hashmap.set("Abc", 123)
3. hashmap.set("Bcd", 234)
4. hashmap.set("Cde", 345)
5. for (let key of hashmap.keys()) {
6. testNapi.mapDemo(key, hashmap.get(key))
7. console.info(`key is ${key}, value is ${hashmap.get(key)}`)
8. }
```

[NativeMap.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/NativeMap.ets#L9-L16)

获取数据并重组为map。

```
1. #define LOG_DOMAIN 0x3200 // Global domain macro, identifying the business domain
2. #define LOG_TAG "MY_TAG"  // Global tag macro, identifying module log tag
3. #include "NativeMap.h"
4. #include "hilog/log.h"
5. #include <map>
6. #include <string>
7. std::map<std::string, int> testmap;
8. napi_value NativeMap::MapDemo(napi_env env, napi_callback_info info) {
9. size_t requireArgc = 2;
10. size_t argc = 2;
11. napi_value args[2] = {nullptr};

13. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
14. char str1[1024];
15. size_t str1_len;
16. napi_get_value_string_utf8(env, args[0], str1, 100, &str1_len);
17. int num;
18. napi_get_value_int32(env, args[1], &num);
19. testmap.insert(std::make_pair(str1, num));
20. for(auto e: testmap){
21. OH_LOG_ERROR(LOG_APP, "key is: %{public}s, value is  %{public}d", (e.first).c_str(), e.second);
22. }

24. return nullptr;
25. }
```

[NativeMap.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/NativeMap/NativeMap.cpp#L25-L49)
