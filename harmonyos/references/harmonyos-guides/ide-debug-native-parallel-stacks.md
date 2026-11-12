---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-parallel-stacks
title: 堆栈可视化
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 堆栈可视化
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:047cdd32be61c99b4e4701acb959bfe2a5c6e836d2dc4e774f75897d13bffd33
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/O9811wzrQMCN-CDF2Xy8PQ/zh-cn_image_0000002779407004.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D100F3C75894A960D5586C2B5C2A845740149B62001CA78455E5C2A00DC4B362)，勾选**Parallel Stacks**，打开并行栈视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ipfk4giYTFaxHJrhyFCUxw/zh-cn_image_0000002779407006.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4B5F305F5594D0435E5FF8274C3F56D29013386E2BCF30A69389F38B63A54D2)

在程序停下时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/zVoDa6Z3SRCzgatW9IBQyw/zh-cn_image_0000002779566982.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=55A36FCBD8C2A749711D903542D06F40E04CCCE877FA9ACEA2D84BE0492CF258)

## 调用栈跳转

您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。

## 线程信息查看

在多个线程合并的位置处悬停鼠标，可以显示这些线程的具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/3qAyJStRQ5Oakw5xZaMZ0Q/zh-cn_image_0000002779566984.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0B2174ECC6411AD55DC983DE370E716F32E271FCCEB7882086A31526E736CA1)
