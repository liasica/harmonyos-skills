---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:7c95e9481b4e639b2b2f84285b7f430af5e9baf15e3440358ddd84df841171c8
---

**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/u8OgTuNHRFmk2FEELzYvtQ/zh-cn_image_0000002370565340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BC750125A7991F78747FEF5842BFBFE24D05530B14E51DD6E7064C7DC5D90FE "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/nhfD_2nMSPCnDm7osV4F8A/zh-cn_image_0000002404125005.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=A10C222BE97A79587040DAA4587406F8EAD3F6042FA577E605D583AF0AF9C228)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/2MF3CnhqTIKKdBFfH-tkLQ/zh-cn_image_0000002370405452.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=83B05F23E9C4DFA3366E3F1247A4F6EAAA9F25D7FD890BA90ED33623B172F65A)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/jC132MSETwOx6hR8RRnNCQ/zh-cn_image_0000002404045177.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF4A92C1A7B2474B3B2148DC65B078B5BE0F854E83F3075619D390A57A2CEC1C "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem（Anonymous Shared Memory，匿名共享内存）；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION（内核内存管理器）内存。

如果这类内存发生增长，往往会导致卡死、花屏等较严重的问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](bpta-stability-leak-way.md#section728319329442)中的ashmem、ION内存泄漏分析方法。
