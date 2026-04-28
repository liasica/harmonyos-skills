---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c296a252e8fa6d1a958bc29d1dd5bd5936213ff9fe5fe8629044c4c739a557c4
---

从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/KrGQzHcGRlmbA6QCCThumg/zh-cn_image_0000002561753011.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=06E1D0A52E93E72263505FC213FD2B13DB70154B2022DED20AC09CA931075682)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/IROXl6_yTQuHl726G7xkag/zh-cn_image_0000002561832993.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=3AEA92190FC7F35A2C44CC39E523A55763AB465D51E227D71A3C5FFD9BFA3F22)打开Run Anything窗口，搜索任务并双击执行。
