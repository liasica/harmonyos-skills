---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-parallel-stacks
title: 堆栈可视化
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 堆栈可视化
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3dd74dff5abee0a4050f697659acffde0bcf7b51dd63a6010390fa52052fadd5
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/1BIZmJzITJmxclGJo4ls2w/zh-cn_image_0000002530753170.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=842328AAA728F038BD79CEDAD2E65AFD0E853F4644158D7978AFEF12F769A85A)，勾选**Parallel Stacks**，打开并行栈视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/oujXWbjOSS-Ey_0sJg9Fng/zh-cn_image_0000002561753109.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=0918ECA6E03A3D9E4A2C3CB79E2DD3E5F37E14D2EF92A0B9D27EA64FC389F27D)

在程序停下时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/FY5S93cBTkS8qW15QK5Jpw/zh-cn_image_0000002530753168.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=08CBC7B4F43307F95E7C788B45ED1D8EA4D1C7E84D93B4A9EC612903BB96742F)

## 调用栈跳转

您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。

## 线程信息查看

在多个线程合并的位置处悬停鼠标，可以显示这些线程的具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/HUQC1jSNSouU-56ZcTgRVg/zh-cn_image_0000002530753174.png?HW-CC-KV=V1&HW-CC-Date=20260427T235649Z&HW-CC-Expire=86400&HW-CC-Sign=90C25B513B21AA52BB1BA9DA63F09A6A0F3231C6E0FFF7AB46BCC353B03372FC)
