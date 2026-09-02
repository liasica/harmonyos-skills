---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149
title: 是否支持#include <memory_resource>和std::pmr::vector
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 是否支持#include <memory_resource>和std::pmr::vector
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b082987e0d09368d02db5c840ede9d069c39a69752000543a127e637513f9948
---

暂时不支持。

C++从C++17标准开始正式支持 <memory\_resource> 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。

Windows：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/3HgfAvUJRQaEY5X-BfAQBg/zh-cn_image_0000002335841501.png)

Mac：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/GQ787NZgQfyLPgU-Vv2m3Q/zh-cn_image_0000002301915320.png "点击放大")
