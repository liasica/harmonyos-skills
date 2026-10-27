---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0011
title: Native工程CMake编译NOTFOUND报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > Native工程CMake编译NOTFOUND报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:708d1ae596b8c3c0e1e75a4687acb9a0c265ece96478eeeb27866df46b819957
---

**Q：Native工程使用find\_path时出现报错，因find\_path未在CMAKE\_SYSROOT限定路径中找到目标文件而触发该报错，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/LI5OYqENT-G3hyvVdB0RhA/zh-cn_image_0000002799410683.png "点击放大")

**A**：OpenHarmony SDK的ohos.toolchain.cmake文件限制搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将"D:/demo"添加至搜索路径：

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

添加后，即可使用find\_path查找"D:/demo"目录下的文件。
