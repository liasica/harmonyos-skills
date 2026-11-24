---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-so
title: so信息可视化
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > so信息可视化
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:94c0faa58aaac9733a47e87791d96ab5b95b0e150c72dca35330c2a675794ceb
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/V7XMxjWyQMaVlJzQOHe7mw/zh-cn_image_0000002808766791.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B694E825B8CE0334C7174178450E0DFBCD82DD38460169BAECE9E8E2F5514DEA)，勾选**Modules**，打开模块视图。

在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持字符串匹配搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/NtGiyYA4TfGFkdM5MEqUzg/zh-cn_image_0000002808886871.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F089E8632E9E75B4B111437B3488CD7657E739A53EF9B690F926F087B304EE7D)

* 加载符号表文件

  如果符号未加载，可右键点击模块，选择**Load Module**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。

  如需将符号恢复为初始状态，可右键点击模块，选择**Reset** **Modules**。
* 添加源码地址映射

  加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。

  如需恢复为默认路径，可右键点击模块，选择**Reset** **Source Mapping****s**。
