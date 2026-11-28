---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-add-new-ability
title: 添加Ability
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 添加Ability
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:50+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:287251f7c65f9b773fd67923e80fbd42f238ba900efe947297256f018fbb288c
---

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* Ability组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。
* ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。

## 在模块中添加Ability

1. 在工程目录选中对应的模块，单击鼠标右键，选择**新建 > Ability** 。
2. 设置**Ability名称**，单击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/f7Nqln-kT2-glXL3rLxpgA/zh-cn_image_0000002791841142.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=24D629CADF469BCF60B7097B08D6BD2747A13B6EE958ED806C89549DC534B499 "点击放大")

## 在模块中添加Extension Ability

1. 在工程中选中对应的模块，单击鼠标右键，选择**新建> Extension Ability**，选择不同的场景类型 。
   * **Accessibility**：用于提供[辅助功能业务/无障碍](../doccenter-capabilities/accessibilitykit-overview.md)能力。
   * **InputMethod**：用于提供输入法功能业务的能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/fJXaFWclTmuBRN1cVJCrRA/zh-cn_image_0000002820721083.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=87F5A68242FFD690B11BE942104F6012AC68445B9CB5ED39ADA2B2258FA5CC38 "点击放大")
2. 设置**Ability名称**，单击**确认**完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/GJ5hlna9T7-J6hz_S79N1A/zh-cn_image_0000002792001116.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E32935DEA2120A518730F85B64F8D64EDB4EB1289BA7A386526A19E3180DB13 "点击放大")
