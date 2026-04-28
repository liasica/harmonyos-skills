---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149
title: 是否支持#include <memory_resource>和std::pmr::vector
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 是否支持#include <memory_resource>和std::pmr::vector
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fef760508fb1adf09551c974ad251dccab3aa1ab3fd43114d52c83b8ea03aa4c
---

暂时不支持。

C++从C++17标准开始正式支持 <memory\_resource> 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。

Windows：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/3HgfAvUJRQaEY5X-BfAQBg/zh-cn_image_0000002335841501.png?HW-CC-KV=V1&HW-CC-Date=20260428T002426Z&HW-CC-Expire=86400&HW-CC-Sign=3E6C6099248E9AAAADE7D8A2B63B856A5EFFCC0D40B76517A54CAB6E85897C3A)

Mac：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/GQ787NZgQfyLPgU-Vv2m3Q/zh-cn_image_0000002301915320.png?HW-CC-KV=V1&HW-CC-Date=20260428T002426Z&HW-CC-Expire=86400&HW-CC-Sign=90E7C83279E669220ED61D28A92D08FF30105922DDD9278D1C0A44C1DB6E9DD8 "点击放大")
