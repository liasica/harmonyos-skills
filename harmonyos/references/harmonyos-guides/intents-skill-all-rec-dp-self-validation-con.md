---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-con
title: 配置文件接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 配置文件接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5b528c27fc6a78d399a349fdae10ee3c81b87462e400448055d1c7bed4df8e5
---

Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为三个步骤：基础信息提供，环境准备，联调验证。

## 基础信息提供

达成开发意向后，开发者发送邮件到邮箱（hagservice@huawei.com）或者联系华为意图框架接口同事，向华为提供测试应用的信息。

| **序号** | **基础信息** | **描述** |
| --- | --- | --- |
| 1 | 应用名称 | 应用市场上架的应用名称。 |
| 2 | 应用包名 | 应用市场上架的应用包名。 |
| 3 | 华为账号（UID） | 参考[附录A获取UID](intents-appendix-a-get-uid.md)。 |
| 4 | 应用图标 | 应用的图标，具体要求如下：  图标背景：非透明。  比例&尺寸：1:1，72px\*72px。  大小：不超过1M。  格式：png、jpg、jpeg。 |
| 5 | 接入意图名称 | 开发者意向接入的意图名称（中英文）。 |

## 环境准备

准备一台装有HarmonyOS Next版本的手机设备，通过应用市场将小艺版本升级至最新，并按照以下顺序依次执行，不能更换执行顺序。

1. 保持设备联网，并且设备时间和实际北京时间保持一致。
2. 安装开发完成并携有意图声明文件的应用。
3. 打开开发者调试模式：进入设置 > 机型 > 关于手机，连续点击软件版本7次，弹出“开启“开发者模式””，点击“确认开启”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/y9F0Fj3eRhmkqTIMLuRbrA/zh-cn_image_0000002583479313.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=FA10E9887652A2C8C887A0FA61426458CE7DBD7AB9B0BFDDB0A194E04C513414)
4. 长按电源键唤醒小艺，将半屏态小艺向上拉升至全屏态，点击左上角返回上层，返回后点击右上角的头像，进入“设置”，找到并进入应用网络设置，打开“WLAN下自动更新”开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/1-fPZIMBTBKSJz7GvkT5JA/zh-cn_image_0000002552799664.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=D6CC031F0AA8FEBFE80C61894A0943A9DC4BE6FF02AE25E8B99C0DB27A023E85)
5. 进入设置 > 系统 > 开发者选项 > 意图框架调试，打开意图框架调试开关，如果下方显示“已切换至真机模式”，则代表真机模式切换成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/l1RMv-AUQbWEFzMvp4ejOA/zh-cn_image_0000002552959314.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=3AEA18F1F7A7355BC99CFA5DA935F92D67745BDEC07743DA20CAC23A9D1A2786)

   【提示】如果出现意图框架调试开关打开后，设备长时间无法出现“已切换至真机模式”时，可以尝试以下操作：

   登出华为账号，再登录之后重新开启意图框架调试开关。

   在小艺对话中点击右上角头像，设置 > 服务管理 > 注销服务 > 注销服务，然后返回桌面重新点击小艺建议的卡片，将展示“欢迎使用小艺建议”的卡片刷新成有服务推荐的卡片，最后重新开启意图框架调试开关。
6. 打开意图调试助手：进入“小艺 > 返回主页面 > 发现”，搜索“意图调试助手”，点击进入意图调试助手。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ASsjnfIiTCOVZcx39mEwxg/zh-cn_image_0000002583479331.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=B8ADEF8C4EAA0B25348AC00458C44009A26B8C58B641596E3CC12DB468688C81)

完成以上所有步骤，即可进行联调。
