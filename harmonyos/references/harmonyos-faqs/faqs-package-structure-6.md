---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-6
title: HSP/HAR包中如何引用外部编译的so库文件
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HSP/HAR包中如何引用外部编译的so库文件
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d059a07854d6b5a50dc46fda3862e9b30afaabc236f94f7f926c60efe0d93ed6
---

1. libxxx.so库文件放入HAR或HSP的libs/arm64-v8a目录。设备类型不同时，需添加对应子目录。新版的arm64为libs/arm64-v8a，老版的arm64为libs/armeabi-v7a，x86模拟器为libs/x86\_64。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/oySIA86nRDqRd8V9v2VLZg/zh-cn_image_0000002624475862.png "点击放大")
2. 在src/main/cpp/CMakeLists.txt文件中链接so库文件。例如：target\_link\_libraries(entry PUBLIC libxxx)
