---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-add-new-ability
title: 添加Ability
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 添加Ability
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:15+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a16b5ff2f920f251665cc2317d46509f74231de0d9903325f9541b372b40ef45
---

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* Ability组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。
* ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。

## 在模块中添加Ability

1. 在工程目录选中对应的模块，单击鼠标右键，选择**新建 > Ability** 。
2. 设置**Ability名称**，单击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/O0WOwH7mSLestUb4prDkZg/zh-cn_image_0000002779608727.png "点击放大")

## 在模块中添加Extension Ability

1. 在工程中选中对应的模块，单击鼠标右键，选择**新建> Extension Ability**，选择不同的场景类型 。
   * **Accessibility**：用于提供[辅助功能业务/无障碍](../doccenter-capabilities/accessibilitykit-overview.md)能力。
   * **InputMethod**：用于提供输入法功能业务的能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/0VkjeKAVQz-NtTc6N15Axw/zh-cn_image_0000002779728879.png "点击放大")
2. 设置**Ability名称**，单击**确认**完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/GiGH6JWpR1KzN10SSP3mXg/zh-cn_image_0000002750009818.png "点击放大")
