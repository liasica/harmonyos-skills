---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95ffa7bfa4194850bc575af183b70752866743289996c69a01d5b30c1852a7af
---

从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/tOQ_XeLTRu-dDo5Y964JiQ/zh-cn_image_0000002561753011.png?HW-CC-KV=V1&HW-CC-Date=20260429T054401Z&HW-CC-Expire=86400&HW-CC-Sign=1CA9E6BD62174B88534D95F809D869850992BE4F690134F1559FFF76ECC125F5)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/z4G3_fuZRAu_yNc_DWgP4A/zh-cn_image_0000002561832993.png?HW-CC-KV=V1&HW-CC-Date=20260429T054401Z&HW-CC-Expire=86400&HW-CC-Sign=73483EA4EB4D99E1F0B3419D0F168DE02C1F2A8BE43480084D9067BDC305A706)打开Run Anything窗口，搜索任务并双击执行。
