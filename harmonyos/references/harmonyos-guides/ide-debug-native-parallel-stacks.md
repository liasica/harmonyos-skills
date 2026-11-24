---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-parallel-stacks
title: 堆栈可视化
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 堆栈可视化
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1f0d49b59f55fe981e60e085dcbce90c87f5f70378fb4ae0273116bd3dbf000e
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/awT1eHG2TVCouyPin2NK6g/zh-cn_image_0000002779407004.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=D899F03F04C4B7228A4C5D95337E75A60BCA3AB09AB6F1354FD7135791221ABD)，勾选**Parallel Stacks**，打开并行栈视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/IV0fex1rRwapaP2aHpHg7g/zh-cn_image_0000002779407006.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AEAA87359849259527409E996E3DB68996F9C195D60FF0F173602A5CF85C7E7)

在程序停下时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/v7W6Bu1ITiei_V7jDsgtJw/zh-cn_image_0000002779566982.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBAE7BB59B3A3AE120B5FCC7BE41B7742B251A6764C07EB0A994D1E3F1946807)

## 调用栈跳转

您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。

## 线程信息查看

在多个线程合并的位置处悬停鼠标，可以显示这些线程的具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/7M8iKhtzQXe7DJA1uHdIxg/zh-cn_image_0000002779566984.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=C946A68124AF2239C325FB95ED2D387EDCC8227F2C69CE02E2598B6C9F990ADC)
