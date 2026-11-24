---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-11-24T12:47:51+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:84ae4fc56353573681541c4dff9d650728c4a948173cad4aa2d6ccd485b93399
---

**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/dkJ-ZNApQ76RGnVGyBAfZA/zh-cn_image_0000002370565340.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=16EF0C13E21FB0D4221D5B634A2769949081133DD790FC7D1B905C9D6FA282CE "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/paAMiYRbQ7WTLqjuAAUvEA/zh-cn_image_0000002404125005.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=21AF65173CA224C723B0365C331557D7B142826DC5F8B5F4046DB8BC2A37940C)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/5XFMT9f0SX6FT6wWWHcM4w/zh-cn_image_0000002370405452.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=98EF09FD705DEBAE9622AAC5793AFF5123AADDAF2FF1E8BC8FA094ACA251C80F)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/ztd6ouCWTtSQJdCabvmslg/zh-cn_image_0000002404045177.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D88262E94408F3FFEB1E2B3DAF1E84F01BBE4BF2394C60731BE15AD976CF913 "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem（Anonymous Shared Memory，匿名共享内存）；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION（内核内存管理器）内存。

如果这类内存发生增长，往往会导致卡死、花屏等较严重的问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](bpta-stability-leak-way.md#section728319329442)中的ashmem、ION内存泄漏分析方法。
