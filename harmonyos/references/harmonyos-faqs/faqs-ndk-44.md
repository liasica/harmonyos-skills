---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-44
title: Native侧如何引入头文件deviceinfo.h
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何引入头文件deviceinfo.h
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8a4bee56114a4ab0f8e50374e27488f57045699f80ad110b0c93c55e767f9026
---

**问题现象：**

在C++文件中，参照官方指导文档，引入#include "deviceinfo.h"头文件后，编译时仍提示无法找到该头文件，日志提示未链接deviceinfo库。

**解决措施：**

当前public SDK中不包含deviceinfo.h头文件，该头文件仅在full SDK中才可以使用，并且需要在CMakeLists.txt导入libdeviceinfo\_ndk.z.so 库才能找到该头文件。方法如下：

```
1. # CMakeLists.txt
2. # ...
3. target_link_libraries(cpplib PUBLIC libace_napi.z.so libdeviceinfo_ndk.z.so)
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/cpplib/src/main/cpp/CMakeLists.txt#L4-L20)
