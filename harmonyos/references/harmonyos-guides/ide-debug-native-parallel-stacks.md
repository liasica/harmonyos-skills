---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-parallel-stacks
title: 堆栈可视化
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 堆栈可视化
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bd9420f67802e58b8c48f54fd126a14553e42f2cabfe5d1f275596fd5c6702ca
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/OCASlwjySc2ADIQBj2VJlA/zh-cn_image_0000002530753170.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=2D524BAB46CE56A294D97654357F13E73E4E4AE673CFC0C8C32EBC339066B40C)，勾选**Parallel Stacks**，打开并行栈视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/y740sh3bRwGtiK7ls5jYFA/zh-cn_image_0000002561753109.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=837FB40D1918405987E379E20159B16943259DD8B691FFAC95C8527410A93637)

在程序停下时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/BFXXzqRETdyIUN_WAVNwxQ/zh-cn_image_0000002530753168.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=B7ECEBD983E4CA5672624577153F0B53CD6CDB94C7B7DD66E76EEB40E5F3C0E8)

## 调用栈跳转

您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。

## 线程信息查看

在多个线程合并的位置处悬停鼠标，可以显示这些线程的具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/1GBxHFOATDyjqHDeGNkeqw/zh-cn_image_0000002530753174.png?HW-CC-KV=V1&HW-CC-Date=20260429T054645Z&HW-CC-Expire=86400&HW-CC-Sign=19E6CA721D3E2713D533FC93CC8E4E2AF81222897EE1B170423BDFCA6BDB3953)
