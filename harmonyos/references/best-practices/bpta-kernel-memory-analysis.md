---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-09-10T06:30:12+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:2a4b32fffb25dcc9192f48af1e9d03d9fcc78dc1b16b754f135ad635e066f978
---

**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Wdd2QjZTRKmtVJSFGS8X6A/zh-cn_image_0000002370565340.png "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/hdZ2KL72R4Kzhi7wqVcX_Q/zh-cn_image_0000002404125005.png)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Eke0YVzgSYS-V3qZ-sT8yw/zh-cn_image_0000002370405452.png)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/H-OG2_euTtSvc4KC4k8Lig/zh-cn_image_0000002404045177.png "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem内存；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION内存。

如果这类内存发生膨胀，往往会导致卡死、花屏等较严重的整机问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](bpta-stability-leak-way.md#section2825227501)中的ashmem、ION内存泄漏分析方法。
