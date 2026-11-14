---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-so
title: so信息可视化
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > so信息可视化
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e4ff9c4905b7dc89b604d80065872b31632b4025810bb5312a95488ab39d3202
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/uGaEEV8eSAueH0JGTwBk2A/zh-cn_image_0000002808766791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4FED678CE1F72B64C662585CBCF9E873D434D20E3436431AB7EB976B7FEC683)，勾选**Modules**，打开模块视图。

在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持字符串匹配搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/LqSNu7C5RxermgI5pxHPhQ/zh-cn_image_0000002808886871.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=06FFF86EA6BC9DBEB4F64EDEE31CE18CED39836C82037048B8E79BB295F85FC9)

* 加载符号表文件

  如果符号未加载，可右键点击模块，选择**Load Module**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。

  如需将符号恢复为初始状态，可右键点击模块，选择**Reset** **Modules**。
* 添加源码地址映射

  加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。

  如需恢复为默认路径，可右键点击模块，选择**Reset** **Source Mapping****s**。
