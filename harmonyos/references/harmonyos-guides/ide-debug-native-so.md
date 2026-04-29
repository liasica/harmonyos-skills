---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-so
title: so信息可视化
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > so信息可视化
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:47+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:3d9fc55e3e9ba7ac797b26edff16d4c06369cb20565ea14e4eea1942250a0615
---

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/f12f098PSg-cp4HCSNPz3w/zh-cn_image_0000002530753332.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=121F7715F0039BD5AFC5370B7DE75E72495F8DEBF083E4BA917A2491E92C14A6)，勾选**Modules**，打开模块视图。

在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持字符串匹配搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/TqC5CPfxTgmej9zWYvv3iw/zh-cn_image_0000002561753269.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=A23758455B33A48EAB5711485A68124527B6348E89E85028702F6314311C3481)

* 加载符号表文件

  如果符号未加载，可右键点击模块，选择**Load Modules**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。

  如需将符号恢复为初始状态，可右键点击模块，选择**Reset** **Modules**。
* 添加源码地址映射

  加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。

  如需恢复为默认路径，可右键点击模块，选择**Reset** **Source Mapping****s**。
