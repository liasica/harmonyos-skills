---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-add-new-ability
title: 添加Ability
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 添加Ability
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:11+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:d379a1d3dab95df4f25941114ce5ce339911b1fec8328381791076d46469d3a8
---

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* Ability组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。
* ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。

## 在模块中添加Ability

1. 在工程目录选中对应的模块，单击鼠标右键，选择**新建 > Ability** 。
2. 设置**Ability名称**，单击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/CxbfZO4XR8GjPafUThITVA/zh-cn_image_0000002781471186.png?HW-CC-KV=V1&HW-CC-Date=20261114T004722Z&HW-CC-Expire=31536000000&HW-CC-Sign=A082F77D9E340DB29A6F4FCBD35D149F809561DF40E859913D19F35337999249 "点击放大")

## 在模块中添加Extension Ability

1. 在工程中选中对应的模块，单击鼠标右键，选择**新建> Extension Ability**，选择不同的场景类型 。
   * **Accessibility**：用于提供[辅助功能业务/无障碍](../doccenter-capabilities/accessibilitykit-overview.md)能力。
   * **InputMethod**：用于提供输入法功能业务的能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/P_D5CpjMSgayEp_DRiqmtg/zh-cn_image_0000002781311254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004722Z&HW-CC-Expire=31536000000&HW-CC-Sign=D91631E9624A1D75CBF8D70EF6AB6D544EB69928CED503EAC4069222446E5030 "点击放大")
2. 设置**Ability名称**，单击**确认**完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/GFJTpSaYQRyE4ni710Bg2w/zh-cn_image_0000002810630741.png?HW-CC-KV=V1&HW-CC-Date=20261114T004722Z&HW-CC-Expire=31536000000&HW-CC-Sign=52111516F5DD54411F2C43EA15AFE8809B10915E619E9FF3ED4437D71E4EC1DD "点击放大")
