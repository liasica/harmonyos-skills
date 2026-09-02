---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-33
title: "编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:5e4b9c14b6b7a9eee86ae00f858b56438609f4d9518f7d06b1dff65763a0e56d
---

**问题现象**

Native工程使用find\_path时出现报错。因find\_path未在CMAKE\_SYSROOT限定路径中找到目标文件而触发该报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/c5V6QHnpQP2Nn6CIfAR3VQ/zh-cn_image_0000002624478504.png "点击放大")

**解决措施**

OpenHarmony SDK的ohos.toolchain.cmake文件限制搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将“D:/demo”添加至搜索路径：

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

添加后，即可使用find\_path查找“D:/demo”目录下的文件。
