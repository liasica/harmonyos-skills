---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-boot-memory
title: 启动时内存分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 启动时内存分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:30dc7f437df79ac531ac47b44421fe014d68969e04f856ab50db56961d22bc50
---

应用/元服务在启动过程中对内存资源的占用情况，是开发者较为关心的问题。DevEco Profiler的Allocation分析任务，提供了启动内存分析能力，协助开发者优化启动过程的内存占用。

针对调试应用的当前运行情况，DevEco Profiler对其做如下处理：

* 如选择的是已安装但未启动的应用，在启动该分析任务时，会自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。
* 如选择的是正在运行的应用，在启动该分析任务时，会先将应用停止，再自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。

具体操作方法为：在任务列表中单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/EnJeKhuTTyi-AGuAUWH4qA/zh-cn_image_0000002808766227.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=14F4177CF971C1E0BDEB32D94AA20CE25016A08099BB1307D503F344F1FE4F3F "点击放大")按钮。

在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同，请参考[内存分析介绍](ide-insight-session-allocations-memory.md)、[内存分析数据筛选](ide-insight-session-allocations-data-filtering.md)。
