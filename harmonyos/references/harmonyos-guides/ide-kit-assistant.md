---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-kit-assistant
title: 快速插入场景化代码片段
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 快速插入场景化代码片段
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:31+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:153261d15b7dd28e8ca6d7391ca6ebb33373d3a2d6b2093e7544f127fd6e3af9
---

DevEco Studio提供Kit Assistant能力，支持通过拖拽方式将基础的场景化的控件/代码片段插入ArkTS工程中，减少高频场景代码的编写时间。

1. 在菜单栏点击**View > Tool Windows > Kit Assistant**，或使用快捷键**Alt + K**（macOS为**O****ption + K**），进入Kit Assistant页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/5JrSU6z7TOS2mr7sj8J_EQ/zh-cn_image_0000002530913278.png)
2. 在左侧目录中支持搜索、查看不同Kit提供的场景化控件或代码片段。Kit Assistant面板右侧展示该控件的使用约束、适用场景等详细信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xJVq0HIaT6unVd34BsCPpw/zh-cn_image_0000002530913282.png)
3. 在目录中点击选中需要的控件或功能代码，并拖拽至.ets文件中适当位置，即可在当前位置插入相应的代码片段。

   说明

   若当前编辑器打开的文件或所在的模块，存在某些Kit能力不支持的设备类型/API版本/工程模型，或某些Kit能力或控件不支持在元服务工程中使用，则Kit Assistant目录中该Kit能力或控件将置灰并无法成功拖拽。
