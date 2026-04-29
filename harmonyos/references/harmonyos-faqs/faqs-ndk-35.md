---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-35
title: Native侧如何使用hilog打印出日志信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何使用hilog打印出日志信息
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3cc5d386b4f12c240e8297b3511e5133e2c6c3b743e30ab0e0f7531b3640687e
---

1.在CMakeLists.txt中新增libhilog\_ndk.z.so链接：

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/CMakeLists.txt#L27-L27)

2.在源文件中包含hilog头文件, 并定义domain、tag宏：

```
1. #include "hilog/log.h"
2. #undef LOG_DOMAIN
3. #undef LOG_TAG
4. #define LOG_DOMAIN 0x3200 // Global domain macro, identifying the business domain
5. #define LOG_TAG "MY_TAG"  // Global tag macro, identifying module log tags
```

[napi\_hilog.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/NativeCpp/napi_hilog.cpp#L9-L13)

3.打印日志，以打印ERROR级别的日志为例：

注意，需要加上{public}才会显示打印内容，不添加默认是{private}

```
1. int a = 5, b = 10;
2. OH_LOG_ERROR(LOG_APP, "Pure a:%{public}d b:%{private}d.", a, b);
```

[napi\_hilog.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/NativeCpp/napi_hilog.cpp#L18-L19)

结果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/btiSFL7DS-mQRoQRZShn9g/zh-cn_image_0000002194318320.png?HW-CC-KV=V1&HW-CC-Date=20260429T061551Z&HW-CC-Expire=86400&HW-CC-Sign=6732B999D31AE83D3A4C5D576D0F9CB7CFD9235BE69EFCFA5CB7783CAEA661C8 "点击放大")

**参考链接：**

[使用HiLog打印日志(C/C++)](../harmonyos-guides/hilog-guidelines-ndk.md)
