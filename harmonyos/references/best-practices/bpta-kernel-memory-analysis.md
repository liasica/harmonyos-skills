---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
title: 分析内核态内存
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 分析内核态内存
category: best-practices
scraped_at: 2026-11-14T08:54:13+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:99d855ecfa4b1db54efbab34248f2ef0aab7e9698a222115fccec1e1704bbd14
---

**DevEco 工具堆内存抓栈功能说明**

DevEco Studio Profiler插件Allocation模板可以帮助用户分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。

## 操作步骤

1. 打开IDE后，选择Profiler。
2. 点击Allocation选项。
3. 点击Create Session创建录制会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/0n6uGyNCSw6_LI6J5XjgKQ/zh-cn_image_0000002370565340.png?HW-CC-KV=V1&HW-CC-Date=20261114T005129Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F6ABFC5DBF7255E149BB4EDE1AA036EC4A04A3A6123603D3B8A1C5B6DA69F0E "点击放大")
4. 在筛选中勾选Memory。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/sT-Rlh3zSBCRQYpkB2l8Wg/zh-cn_image_0000002404125005.png?HW-CC-KV=V1&HW-CC-Date=20261114T005129Z&HW-CC-Expire=31536000000&HW-CC-Sign=906FCEC7D8664520990CE2F027CFCC43475351A3B4DEB3A25ED3833ADD95EECF)
5. 点击按钮开始抓栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/qrq0AzStSFqk-YV5SKKWmQ/zh-cn_image_0000002370405452.png?HW-CC-KV=V1&HW-CC-Date=20261114T005129Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACFB08266EBEFFA7D39BF117F72519900C05C5BE48131D2BA57E4E7EC8C46D84)
6. 录制完成后点击录制的结果，分析Memory中各内存的增长趋势。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/N_6ti6_GQteyT-tPY9IL-g/zh-cn_image_0000002404045177.png?HW-CC-KV=V1&HW-CC-Date=20261114T005129Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3AC8790F6196425DD40A544FDD4814BAEF34388D6DA42F5A16371025F9A3383 "点击放大")

## 内存类型说明

* FilePage Other：应用使用的ashmem（Anonymous Shared Memory，匿名共享内存）；
* GL：应用使用的GPU内存；
* Graph：应用使用的ION（内核内存管理器）内存。

如果这类内存发生增长，往往会导致卡死、花屏等较严重的问题，遇到这类问题，需要尽快修复，具体分析方法见[内存泄漏分析方法](bpta-stability-leak-way.md#section728319329442)中的ashmem、ION内存泄漏分析方法。
