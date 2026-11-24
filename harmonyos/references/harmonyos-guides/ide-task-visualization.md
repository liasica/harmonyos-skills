---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-task-visualization
title: 任务可视化与执行
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 任务可视化与执行
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:34+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fc200ed24c47350f150f22d1499ae9ab3ff2ffb0b65431d318202f9b73e2c525
---

从DevEco Studio 6.1.0 Beta1版本开始，Hvigor提供任务可视化窗口，用于展示工程和各个模块常用的构建任务，便于快速执行。

1. 点击编辑窗口右侧工具栏的**Hvigor**，或者菜单栏**View > Tool Windows >** **Hvigor**，打开任务可视化窗口，会显示当前product和构建模式下的任务，切换product和构建模式时会同步工程，同步成功后会刷新任务列表。
   * Tasks：工程级的任务。
   * Run Configurations：Run/Debug Configurations窗口中的任务。
   * 其他目录：模块级的任务，如entry。

   其中工程级和模块级的任务，build和help目录下是Hvigor的默认任务，other目录下是开发者[自定义的任务](ide-hvigor-task.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mhh64EKIR8iympZ8wAsX7A/zh-cn_image_0000002779407076.png?HW-CC-KV=V1&HW-CC-Date=20261124T044234Z&HW-CC-Expire=31536000000&HW-CC-Sign=24209F7A1C9B5F1B088399F1E567E2B15E6668B8A1869D56B05FCA98D1E13A8D)
2. 可以通过鼠标双击、鼠标右键或Enter键快速执行一个选中的任务，也可以点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/qnluBMemTVKUTqid5w613g/zh-cn_image_0000002779567054.png?HW-CC-KV=V1&HW-CC-Date=20261124T044234Z&HW-CC-Expire=31536000000&HW-CC-Sign=8480FF674AB238A05F66AC669CB06EA19F7E60ABDF7EE46502C11D24D8896A35)打开Run Anything窗口，搜索任务并双击执行。
