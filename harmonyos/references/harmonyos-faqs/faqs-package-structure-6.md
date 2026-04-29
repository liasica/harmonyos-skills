---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-6
title: HSP/HAR包中如何引用外部编译的so库文件
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HSP/HAR包中如何引用外部编译的so库文件
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:adec3e1c12c6190f5ab6060d2c69adfca1db2fae8c1b2420b85ba06d2b7c7d7b
---

1. libxxx.so库文件放入HAR或HSP的libs/arm64-v8a目录。设备类型不同时，需添加对应子目录。新版的arm64为libs/arm64-v8a，老版的arm64为libs/armeabi-v7a，x86模拟器为libs/x86\_64。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/2I-bkpe6TRq30kHBDoK_yA/zh-cn_image_0000002194158696.png?HW-CC-KV=V1&HW-CC-Date=20260429T061441Z&HW-CC-Expire=86400&HW-CC-Sign=5A58F33C3AD7718EBFCC8C6A8DA36D93A8D59B255B74D1925EAB1570896B4699 "点击放大")
2. 在src/main/cpp/CMakeLists.txt文件中链接so库文件。例如：target\_link\_libraries(entry PUBLIC libxxx)
