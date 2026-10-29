---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-10-29T08:03:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:588629556f9b3ba6eb0d10970371782d04e66a62568d47f8ad2ab6f7835aa716
---

**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/4grfr5TVRu6RAYjnFJGyrg/zh-cn_image_0000002370565340.png "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/7sYnGM3JSPKropVdP5jF4Q/zh-cn_image_0000002404125005.png)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/oPY8H70JQWGQ_Kz-AvSScQ/zh-cn_image_0000002370405452.png)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/AhErEnA4TaK09L1k70LyGg/zh-cn_image_0000002404045177.png "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem（Anonymous Shared Memory，匿名共享内存）；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION（内核内存管理器）内存。

如果这类内存发生增长，往往会导致卡死、花屏等较严重的问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](bpta-stability-leak-way.md#section728319329442)中的ashmem、ION内存泄漏分析方法。
