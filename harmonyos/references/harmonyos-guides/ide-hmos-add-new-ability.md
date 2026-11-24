---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-add-new-ability
title: 添加Ability
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 添加Ability
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:df4ba0a58279ad0baeb7680925a21513f6034851913280c62286266c039f5911
---

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* Ability组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。
* ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。

## 在模块中添加Ability

1. 在工程目录选中对应的模块，单击鼠标右键，选择**新建 > Ability** 。
2. 设置**Ability名称**，单击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/pbduClP8Q86mFuXOyKejbQ/zh-cn_image_0000002791841142.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=C07BE76FDA773AE84CE7814A9AF7F65FA2988D7EAAC5DE87F85EAF572BBC743B "点击放大")

## 在模块中添加Extension Ability

1. 在工程中选中对应的模块，单击鼠标右键，选择**新建> Extension Ability**，选择不同的场景类型 。
   * **Accessibility**：用于提供[辅助功能业务/无障碍](../doccenter-capabilities/accessibilitykit-overview.md)能力。
   * **InputMethod**：用于提供输入法功能业务的能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Oi87nEI3S9uxuXQAUBFE7g/zh-cn_image_0000002820721083.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=9190D8B1B8422AA52AF87F2F0344B96CCD1CBC7C3FA1E71CD6A137CBF61B5F1F "点击放大")
2. 设置**Ability名称**，单击**确认**完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/BrzapftnTFSg7vGnOoWA8g/zh-cn_image_0000002792001116.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=3445F6557F3943A706B8B6F1696F512E7CB92EA19ECD78B8ED782D9DF1A91E2A "点击放大")
