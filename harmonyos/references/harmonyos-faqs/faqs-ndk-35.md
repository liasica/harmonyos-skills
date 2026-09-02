---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-35
title: Native侧如何使用hilog打印出日志信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何使用hilog打印出日志信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d37bf624b6893994aa097d60656ab32267931df62a8c895a5eee630e78f0eaf
---

1.在CMakeLists.txt中新增libhilog\_ndk.z.so链接：

```text
target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
```

2.在源文件中包含hilog头文件, 并定义domain、tag宏：

```cpp
#include "hilog/log.h"
#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG_TAG "MY_TAG"  // Global tag macro, identifying module log tags
```

3.打印日志，以打印ERROR级别的日志为例：

注意，需要加上{public}才会显示打印内容，不添加默认是{private}

```cpp
int a = 5, b = 10;
OH_LOG_ERROR(LOG_APP, "Pure a:%{public}d b:%{private}d.", a, b);
```

结果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/9zE51xzJS_esMYwYm3av4A/zh-cn_image_0000002624475902.png "点击放大")

**参考链接：**

[使用HiLog打印日志(C/C++)](../harmonyos-guides/hilog-guidelines-ndk.md)
