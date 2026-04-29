---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-04-29T14:13:25+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c869d01b1ec6cd3c81da17602eb8065f1397fd525324807ca94b705b1e2ff7dd
---

**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/1jsm3ch2RvevmTf1C8G8gg/zh-cn_image_0000002370565340.png?HW-CC-KV=V1&HW-CC-Date=20260429T061324Z&HW-CC-Expire=86400&HW-CC-Sign=300B4A5EE9CA828AFB860C8E8564255358EAA7286293ABBE6CBA32418094647E "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/vR4CE3IJRPOv8P-GeJaeHA/zh-cn_image_0000002404125005.png?HW-CC-KV=V1&HW-CC-Date=20260429T061324Z&HW-CC-Expire=86400&HW-CC-Sign=B396DADD08760478664DF71F670F9794E1958E06C8863E63F88D77D452915CDA)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/UVUfbf7HSnmJ74PTIauP2g/zh-cn_image_0000002370405452.png?HW-CC-KV=V1&HW-CC-Date=20260429T061324Z&HW-CC-Expire=86400&HW-CC-Sign=8133D3B761F941A5254E5445536E1C05C17045237F280DA9DA6D0D3CC2AC8B93)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/SpHCwku3TKSFWWi08_sPmQ/zh-cn_image_0000002404045177.png?HW-CC-KV=V1&HW-CC-Date=20260429T061324Z&HW-CC-Expire=86400&HW-CC-Sign=B91C73EB0986678250961884BC1C7606DA5E3EC85FBD67280CCEC7DA14AB509F "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem内存；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION内存。

如果这类内存发生膨胀，往往会导致卡死、花屏等较严重的整机问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](bpta-stability-leak-way.md#section2825227501)中的ashmem、ION内存泄漏分析方法。
