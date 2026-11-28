---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:43+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:84c679cec08c12052673cd243adb79655e2e453ef8748488478d807dbe90d7af
---

从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/GkLejAEXT4-cDX5Ir5DK8Q/zh-cn_image_0000002779407076.png?HW-CC-KV=V1&HW-CC-Date=20261128T023443Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7CF9D90E0A8A5BF515D0B12F8A2991547F4F8CEEE48DEEF8C9C3A56B66F83B4)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/vbudLRqHTV-U9aYUaxPm-A/zh-cn_image_0000002779567054.png?HW-CC-KV=V1&HW-CC-Date=20261128T023443Z&HW-CC-Expire=31536000000&HW-CC-Sign=419ABC661AEB61F2B9F95D6252AE45761674C4299950783496E7DE1F87F2DC53)打开Run Anything窗口，搜索任务并双击执行。
