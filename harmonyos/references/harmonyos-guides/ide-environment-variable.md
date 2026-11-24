---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-variable
title: Terminal环境变量说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > Terminal环境变量说明
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5721f372a5899e239631966d574d08567632048a2bed56c19bd543c87b27ee03
---

在DevEco Studio的Terminal中执行hvigor、ohpm等命令时，默认使用内置的环境变量，无需额外配置。

DevEco Studio内置环境变量的设置方式如下：

点击菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings** ） **> Tools > Terminal**，勾选以下选项表示开启内置环境变量，重启DevEco Studio后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/3573CqD2R2ahWZ2RBQ98uQ/zh-cn_image_0000002779567038.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=520DC4631152DB0122F005A9AC7EA0BF3FD8CB63517AD97853CDBFAC346C5E5B)

除了内置的环境变量外，开发者也可以在本地系统中配置PATH环境变量。如果同时配置了内置环境变量和本地系统环境变量，两者存在优先级关系，实际生效的环境变量如下。

* DevEco Studio 6.0.2 Release（6.0.2.650）及以上版本：内置环境变量生效。
* DevEco Studio 6.0.2 Release（6.0.2.650）之前的版本：
  + Windows：内置环境变量生效。
  + macOS：本地系统环境变量生效。
