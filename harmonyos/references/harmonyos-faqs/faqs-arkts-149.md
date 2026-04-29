---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149
title: 是否支持#include <memory_resource>和std::pmr::vector
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 是否支持#include <memory_resource>和std::pmr::vector
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:834b944920801990431d9d03d669eab8dfe7915f3564f81e2f85eb7428f9b644
---

暂时不支持。

C++从C++17标准开始正式支持 <memory\_resource> 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。

Windows：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/3HgfAvUJRQaEY5X-BfAQBg/zh-cn_image_0000002335841501.png?HW-CC-KV=V1&HW-CC-Date=20260429T061543Z&HW-CC-Expire=86400&HW-CC-Sign=1DC560F00DA44526E8E40553342CB553D9ACBBA1DA7EAF820DBEECB3180535E9)

Mac：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/GQ787NZgQfyLPgU-Vv2m3Q/zh-cn_image_0000002301915320.png?HW-CC-KV=V1&HW-CC-Date=20260429T061543Z&HW-CC-Expire=86400&HW-CC-Sign=2F177693857875CFC56276E9F347DFEF1ACDE1CD6625BD9ED00755830DAC8424 "点击放大")
