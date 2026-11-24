---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent
title: 创建意图框架
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 创建意图框架
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:af5cdaa45634c39b095252a4ab327c18108c3cde7f528f2a984efeae1369588e
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/drum3QJrT1aqz_3KKEmxIQ/zh-cn_image_0000002779567226.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6D85B4A46DA1A0D6B75CB0B9F753D6B7176B0C573F34967BDA9035E8522A0E8)
2. 点击**Finish**，完成意图框架创建。此时将在**entry > src > main > ets > insightintents**目录下生成入口代码文件；在**entry > src > main > resource > base > profile**中，生成**i****nsight\_intent.json**文件，可在该文件查看当前意图框架配置的相关信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/XSxlvekrTyqMUAxkyZF0Og/zh-cn_image_0000002779407246.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCF937FA71249CFD2D294883F6FDAF3912DDDFA990EE05D3A3ADCD899FDE6D18)
