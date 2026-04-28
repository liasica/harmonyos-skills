---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-33
title: 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4e91c7e6078595908c82ed3e8269d37970f03b4b20bfa9c335acfeb5b4e793d3
---

**问题现象**

Native工程使用find\_path时出现报错。因find\_path未在CMAKE\_SYSROOT限定路径中找到目标文件而触发该报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/aJ7_eMmHRNm8au8jcv5w4A/zh-cn_image_0000002229603961.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=E44E64C6543DF1AE78EB79B3197D616EF4E54A682F49F5807278A36EBEF11100 "点击放大")

**解决措施**

OpenHarmony SDK的ohos.toolchain.cmake文件限制搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将“D:/demo”添加至搜索路径：

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

添加后，即可使用find\_path查找“D:/demo”目录下的文件。
