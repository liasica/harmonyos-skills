---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149
title: 是否支持#include <memory_resource>和std::pmr::vector
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 是否支持#include <memory_resource>和std::pmr::vector
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:99a4f4c7a80fc9cd3eb576fd9014507bc8b39041ebbf031a85e031bbf60897bc
---

暂时不支持。

C++从C++17标准开始正式支持 <memory\_resource> 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。

Windows：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/U46FkGNJRW-VFj17jFnA0A/zh-cn_image_0000002654795261.png "点击放大")

Mac：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/xYT0BX3lT2a4lWvDV2ontw/zh-cn_image_0000002624635792.png "点击放大")
