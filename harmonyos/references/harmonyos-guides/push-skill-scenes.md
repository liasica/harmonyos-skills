---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-skill-scenes
title: 场景化消息开发Skill
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > （可选）接入Skill > 场景化消息开发Skill
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:00+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:303aae167b5fe9f44b65629bab71002e72c88f6adc617c0f010a971b489000ae
---

## 概述

场景化消息开发Skill，旨在帮助开发者快速集成Push Kit推送场景化消息。Skill包含客户端与服务端两部分，可自动生成客户端页面代码与服务端接口工程，支持端到端验证，有效简化接入流程、降低开发成本。

## 能力覆盖范围

场景化消息开发Skill能帮助开发者快速接入Push Kit，并实现推送场景化消息。其中：

* 客户端Skill负责生成推送通知消息、后台消息、应用内通话消息的ArkTS代码以及配置工程依赖。
* 服务端Skill负责生成服务端工程代码，实现Push场景化消息发送能力。

## 注意事项

* 客户端Skill生成的代码需在ArkTS工程中运行，当前仅支持ArkTS开发框架。
* 服务端Skill目前仅支持生成java代码。
* 请务必在集成发布前，在测试环境中充分验证所生成代码的正确性与安全性。

## 使用方式

### 下载并配置Skill

点击下方链接下载对应Skill，并放到AI编码工具（如DevEco CodeGenie、Claude Code等）的Skill配置目录下（不同工具规范不一致，按工具要求处理）。

* [客户端Skill](https://matrix.openharmony.cn/#/skillSquare/details?id=6a2a34e6efaf3913a71c544e)：生成推送通知消息、后台消息、应用内通话消息的ArkTS代码以及配置工程依赖。
* [服务端Skill](https://gitcode.com/HarmonyOS_Samples/push-kit_-sample-code_-server-demo_-java/tree/master/hmos-push-kit-server-integration)：生成服务端工程代码，实现Push场景化消息发送能力。

### DevEco CodeGenie接入示例

1. 打开[DevEco Studio](https://developer.huawei.com/consumer/cn/download/)之后，在右侧工具栏点击CodeGenie，详情见[DevEco CodeGenie工具概述](ide-codegenie.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/zDqnY-vnRHqIFI_ZV7Cb8g/zh-cn_image_0000002736434315.png)
2. 参考[操作步骤](ide-skills.md#section20151122814121)导入Skill。如图所示，选择在[下载并配置Skill](push-skill-scenes.md#下载并配置skill)中下载的Skill，需要导入名为hmos-push-kit的文件夹，以及4个子文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/sPgaP85JSRCE3wSRcDx_lA/zh-cn_image_0000002706835164.png)
3. 全部导入成功后，如图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/HO4B9qpfQfGoNVhoVg0FlQ/zh-cn_image_0000002736314271.png)
4. 回到对话页面，选择**HarmonyOS Act**以及合适的模型，并按需求输入提示词。如图所示，CodeGenie调用对应技能接入Push Kit。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/yIkbXeq2SMOeSxWILe6Tpg/zh-cn_image_0000002706675228.png)
5. 接入完成后，CodeGenie会提示需要开通推送服务等注意事项。

### 触发Skill

| 触发方式 | 示例 |
| --- | --- |
| 关键词触发 | “帮我接入推送服务” |
| Skill名称触发 | “使用hmos-push-kit，帮我接入推送服务” |

| 客户端技能 | Skill名称 | 关键词 | 说明 |
| --- | --- | --- | --- |
| 推送服务集成助手Skill | hmos-push-kit | 帮我接入推送服务 | 若使用该关键词正确触发主skill，AI编码工具会向开发者询问具体接入哪种场景。目前支持接入以下三种场景。 |
| 通知消息Skill | hmos-push-kit-notification | 帮我接入通知消息 | 通知消息场景子skill。还可以触发的关键词，如：接入notification、接入push推送通知消息等相似语义。 |
| 后台消息Skill | hmos-push-kit-background | 帮我接入后台消息 | 后台消息场景子skill。还可以触发的关键词，如：接入background、添加后台消息功能等相似语义。 |
| 应用内通话消息Skill | hmos-push-kit-voip | 帮我接入应用内通话 | 应用内通话场景子skill。还可以触发的关键词，如：接入voip、添加应用内通话等相似语义。 |

| 服务端技能 | Skill名称 | 关键词 | 说明 |
| --- | --- | --- | --- |
| Push Kit服务端Skill | hmos-push-kit-server-integration | 帮我生成Push消息发送服务端java代码 | 服务端Skill目前支持通知消息的发送与撤回，以及应用内通话消息的发送。 |
