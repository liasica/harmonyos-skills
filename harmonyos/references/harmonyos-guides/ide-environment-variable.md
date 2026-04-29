---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-variable
title: Terminal环境变量说明
breadcrumb: 指南 > 编写与调试应用 > 附录 > Terminal环境变量说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:06+08:00
doc_updated_at: 2026-03-31
content_hash: sha256:e1a16b6bf68d9a4e34031c01f7ade91cc1b49223cf683e702ae8c9ad3756c431
---

在DevEco Studio的Terminal中执行hvigor、ohpm等命令时，默认使用内置的环境变量，无需额外配置。

DevEco Studio内置环境变量的设置方式如下：

点击菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings** ） **> Tools > Terminal**，勾选以下选项表示开启内置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/pueguoYqRcil_9do1E3_Yw/zh-cn_image_0000002533959996.png?HW-CC-KV=V1&HW-CC-Date=20260429T054705Z&HW-CC-Expire=86400&HW-CC-Sign=9C0D29475F8A2DDB23AB29DF03C60079EAF9637372EF433013C87D729685A336)

除了内置的环境变量外，开发者也可以在本地系统中配置PATH环境变量。如果同时配置了内置环境变量和本地系统环境变量，两者存在优先级关系，实际生效的环境变量如下。

* DevEco Studio 6.0.2 Release（6.0.2.650）及以上版本：内置环境变量生效。
* DevEco Studio 6.0.2 Release（6.0.2.650）之前的版本：
  + Windows：内置环境变量生效。
  + macOS：本地系统环境变量生效。
