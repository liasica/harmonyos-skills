---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-boot-memory
title: 启动时内存分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 启动时内存分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:73d973cd719812855bbd154094c8585bafcd739fe1a0ad803d102da288068af9
---

应用/元服务在启动过程中对内存资源的占用情况，是开发者较为关心的问题。DevEco Profiler的Allocation分析任务，提供了启动内存分析能力，协助开发者优化启动过程的内存占用。

针对调测应用的当前运行情况，DevEco Profiler对其做如下处理：

* 如选择的是已安装但未启动的应用，在启动该分析任务时，会自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。
* 如选择的是正在运行的应用，在启动该分析任务时，会先将应用停止，再自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。

具体操作方法为：在任务列表中单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/hhTDDYqKRJa58Wj3x-hykA/zh-cn_image_0000002561752741.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=B9433DCF41D32FC4CE42DD179398A6579001919DC8BFFA7A86524D9B1321D979)按钮。

在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同，请参考[内存分析介绍](ide-insight-session-allocations-memory.md)、[内存分析数据筛选](ide-insight-session-allocations-data-filtering.md)。
