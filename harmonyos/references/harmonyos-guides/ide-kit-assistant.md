---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-kit-assistant
title: 快速插入场景化代码片段
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 快速插入场景化代码片段
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:37+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:440e7ee225f756d6648f1814bcf4803633d850df433061757e96381ec9afe816
---

DevEco Studio提供Kit Assistant能力，支持通过拖拽方式将基础的场景化控件/代码片段插入ArkTS工程中，减少高频场景代码的编写时间。

1. 在菜单栏点击**View > Tool Windows > Kit Assistant**，或使用快捷键**Alt + K**（macOS为**O****ption + K**），进入Kit Assistant页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1YadxVm5RfmH9-r2_avgcg/zh-cn_image_0000002808886819.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=F43CB4D1D913675044060F93F618CB6626EDD02A796C82C0F401F5BAD73E4B14)
2. 在左侧目录中支持搜索、查看不同Kit提供的场景化控件或代码片段。Kit Assistant面板右侧展示该控件的使用约束、适用场景等详细信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/MWTjSuJUSHmuWMkgWX_VpA/zh-cn_image_0000002779567158.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=76C357756EFA6EEFF08597523F6718E0A14459E0CD2B5E01420A4C3A838107E4)
3. 在目录中点击选中需要的控件或功能代码，并拖拽至.ets文件中适当位置，即可在当前位置插入相应的代码片段。

   **说明** 

   若当前编辑器打开的文件或所在的模块，存在某些Kit能力不支持的设备类型/API版本/工程模型，或某些Kit能力或控件不支持在元服务工程中使用，则Kit Assistant目录中该Kit能力或控件将置灰并无法成功拖拽。
