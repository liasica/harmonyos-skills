---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:26+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4b04c8b4be66d23a877736c80d509e4ed2dac70cb373096c20aa1c6d3fb27406
---

从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lq3MdkkfQ0O3OEFQXB8vmA/zh-cn_image_0000002701823368.png)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/swIOwsLaTxW2zjyg0WT8og/zh-cn_image_0000002701663450.png)打开Run Anything窗口，搜索任务并双击执行。
