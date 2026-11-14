---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent
title: 创建意图框架
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 创建意图框架
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:48+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:723eb01c10d98b3e44eb7d2d73fa79dc9b3b283bfeaf9861319a71a696da2d97
---

DevEco Studio支持创建意图框架，帮助应用理解用户意图，并提供相应的服务和体验。

## 使用约束

* 支持API 11及以上工程创建意图框架；
* 仅支持在Stage工程的HAP模块中创建意图框架。

## 使用方式

1. 选中模块或模块下的文件，右键单击**New > Insight Intent**，进入意图框架配置界面。
   * **Intent domain**：意图垂域。
   * **Source entry name**：意图框架入口代码文件名。
   * **Intent Settings**：意图配置。以MusicDomain为例：
     + **PlayMusic：**开启/关闭PlayMusic意图能力，实现播放歌曲（指定一首）**。**默认需要关联UIAbility，可在**Ability name**中下拉框选择需要关联的Ability能力。
     + **PlayMusicList**：开启/关闭PlayMusicList意图能力，实现播放歌单（指定一整个歌单）**。**默认需要关联UIAbility，可在**Ability name**下拉框中选择需要关联的Ability能力。

     **说明** 

     PlayMusic和PlayMusicList不支持同时关闭，请至少开启一个意图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/MctrU-ZkSVSBZYmHaciKMA/zh-cn_image_0000002779567226.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=81D34F6D80B3B4534C63C984D5E94132800517267D5EB96DC255472666579768)
2. 点击**Finish**，完成意图框架创建。此时将在**entry > src > main > ets > insightintents**目录下生成入口代码文件；在**entry > src > main > resource > base > profile**中，生成**i****nsight\_intent.json**文件，可在该文件查看当前意图框架配置的相关信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/uKYMcy2CQVGTYF5mhV3XpA/zh-cn_image_0000002779407246.png?HW-CC-KV=V1&HW-CC-Date=20261114T004848Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E081002F904C563CD2527D383AB64F1FBE976591DCF5C0CFB46236DEA9C4044)
