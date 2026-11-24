---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-kit-assistant
title: 快速插入场景化代码片段
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 快速插入场景化代码片段
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:66d6d84884111b2ae2dd28f6081bd8562aff4e2c2efcece4b6d6b219c50d8633
---

DevEco Studio提供Kit Assistant能力，支持通过拖拽方式将基础的场景化控件/代码片段插入ArkTS工程中，减少高频场景代码的编写时间。

1. 在菜单栏点击**View > Tool Windows > Kit Assistant**，或使用快捷键**Alt + K**（macOS为**O****ption + K**），进入Kit Assistant页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/l1Ik9MjvQuGgquLOOsFp2g/zh-cn_image_0000002808886819.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=71EA05EB272C7F6B35E71A45AB539F8A76A13AA3FE6BC1A6FBFAB46533950C89)
2. 在左侧目录中支持搜索、查看不同Kit提供的场景化控件或代码片段。Kit Assistant面板右侧展示该控件的使用约束、适用场景等详细信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/KwtaNbMMRTOr4dPs_ghRZw/zh-cn_image_0000002779567158.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA114A8AED7B7628A61CEA55BD573B59D5E6704AD267006B0958EEE5CD230F93)
3. 在目录中点击选中需要的控件或功能代码，并拖拽至.ets文件中适当位置，即可在当前位置插入相应的代码片段。

   **说明** 

   若当前编辑器打开的文件或所在的模块，存在某些Kit能力不支持的设备类型/API版本/工程模型，或某些Kit能力或控件不支持在元服务工程中使用，则Kit Assistant目录中该Kit能力或控件将置灰并无法成功拖拽。
