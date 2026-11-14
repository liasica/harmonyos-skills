---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:04+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:92a3ec95334667da3a25d2f093b72f1f6248245752afd67764bd08b19b7bb98c
---

从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/Fhx2jGQJSDy3kAxeXzqjNw/zh-cn_image_0000002779407076.png?HW-CC-KV=V1&HW-CC-Date=20261114T004716Z&HW-CC-Expire=31536000000&HW-CC-Sign=C164C1964E6F352CA0E55937EEBFF785C8BA2DCE2AF97FCD8422C30FE7044A24)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/fJXMt1ChShSG58t_B4cEPg/zh-cn_image_0000002779567054.png?HW-CC-KV=V1&HW-CC-Date=20261114T004716Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E19B25426784745EDCA216932E1DF5ABF5E650639508A8FDFF3A273C3C836F5)打开Run Anything窗口，搜索任务并双击执行。
