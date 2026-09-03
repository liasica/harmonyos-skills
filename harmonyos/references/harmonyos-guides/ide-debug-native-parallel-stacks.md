---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-parallel-stacks
title: 堆栈可视化
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 堆栈可视化
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ae3ed50f379e39716047e95f59434713027be106337b8be1f50fc33e0f215210
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/z2Co8dXgR9upYd9OE12UvA/zh-cn_image_0000002731542421.png)，勾选**Parallel Stacks**，打开并行栈视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/73lbyh2pRYGC0a_kTpEvUg/zh-cn_image_0000002701663228.png)

在程序停下时，并行栈视图可以同时展示多个线程的调用栈信息，合并重复调用栈，帮助您更好地理解程序的并发执行情况，以及发现潜在的多线程问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/5sgfVDaCSA2-BT9HjGvz_Q/zh-cn_image_0000002731382447.png)

## 调用栈跳转

您可以在视图上对某一个调用栈双击来跳转到对应堆栈，Frames页签中会随之跳转，此时可以查看该堆栈的变量等信息。

## 线程信息查看

在多个线程合并的位置处悬停鼠标，可以显示这些线程的具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/yKiZtHROQsujBCMTAFeyng/zh-cn_image_0000002701823146.png)
