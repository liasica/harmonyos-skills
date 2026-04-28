---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent
title: 创建意图框架
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 创建意图框架
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:431b2feb51d725f95530edcad4703f711605abfff72c93422c045545e4e7abf5
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

     说明

     PlayMusic和PlayMusicList不支持同时关闭，请至少开启一个意图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/kOcZX-hAQOC9V54LlCz3Ow/zh-cn_image_0000002561833675.png?HW-CC-KV=V1&HW-CC-Date=20260427T235509Z&HW-CC-Expire=86400&HW-CC-Sign=05F698E8C37058FF9E292658DCA163C53956AA74E09BB483B9BF057DEB3695A2)
2. 点击**Finish**，完成意图框架创建。此时将在**entry > src > main > ets > insightintents**目录下生成入口代码文件；在**entry > src > main > resource > base > profile**中，生成**i****nsight\_intent.json**文件，可在该文件查看当前意图框架配置的相关信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/-Dh8ulq0Rg6n6NUhJt7bpQ/zh-cn_image_0000002530913748.png?HW-CC-KV=V1&HW-CC-Date=20260427T235509Z&HW-CC-Expire=86400&HW-CC-Sign=E58047C41B930A14A460F251F119D9988D3A9B8D3828817D34A6D83F3E9F50F5)
