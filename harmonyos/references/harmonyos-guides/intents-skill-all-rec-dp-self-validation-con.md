---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-con
title: 配置文件接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 配置文件接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:83f8ca8c80b0884c3c7dc9080002430802be0c0f7e5cc5fcd3e054f57a335d38
---

Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为三个步骤：基础信息提供，环境准备，联调验证。

## 基础信息提供

开发者在AppGallery Connect平台上提交的技能调用方案能力申请审核成功后，可根据审核成功的反馈提示，提供测试应用的信息。能力申请的步骤参考[Intents Kit接入流程](intents-access-flow.md)。

| **序号** | **基础信息** | **描述** |
| --- | --- | --- |
| 1 | 应用名称 | 应用市场上架的应用名称。 |
| 2 | 应用包名 | 应用市场上架的应用包名。 |
| 3 | 华为账号（UID） | 参考[附录A获取UID](intents-appendix-a-get-uid.md)。 |
| 4 | 应用图标 | 应用的图标，具体要求如下：  图标背景：非透明。  比例&尺寸：1:1，72px\*72px。  大小：不超过1M。  格式：png、jpg、jpeg。 |
| 5 | 接入意图名称 | 开发者意向接入的意图名称（中英文）。 |

## 环境准备

准备一台装有HarmonyOS 5及以上版本的手机设备，通过应用市场将小艺版本升级至最新，并按照以下顺序依次执行，不能更换执行顺序。

1. 保持设备联网，并且设备时间和实际北京时间保持一致。
2. 安装开发完成并携有意图声明文件的应用。
3. 打开开发者调试模式：进入“设置 > 机型 > 关于手机”，连续点击软件版本7次，弹出“开启开发者选项”弹窗，点击“确认开启”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/kBZXuYV0SCq4Z6REUDpq5g/zh-cn_image_0000002791566792.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=50E4A5DDDA134CD60BD7ED63CC202B6294065CEB0CF2B5CFB1574DC21316162A)
4. 长按电源键唤醒小艺，将半屏态小艺向上拉升至全屏态，点击左上角返回上层，返回后点击右上角的头像，进入“设置”，找到并进入应用网络设置，打开“WLAN下自动更新”开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Cat_yV67TOOEjF51MPKyLw/zh-cn_image_0000002820526745.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=84237E1843E2E7EE80182E5BE53810419BFE1C1EE10FA11B431585D0676F50DB)
5. 进入“设置 > 系统 > 开发者选项 > 意图框架调试”，打开意图框架调试开关，如果下方显示“已切换至真机模式”，则代表真机模式切换成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/koiBlIgnTBO88ZLZVuvgJA/zh-cn_image_0000002791726766.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=C937C0E717F343622B1B32E8976FBCA3EADE3B8F2BBF7FCEE31967B577D9AA2F)

   【提示】如果出现意图框架调试开关打开后，设备长时间无法出现“已切换至真机模式”时，可以尝试以下操作：

   * 登出华为账号，再登录之后重新开启意图框架调试开关。
   * 在小艺对话中点击右上角头像，点击“设置 > 服务管理 > 注销服务 > 注销服务”，然后返回桌面重新点击小艺建议的卡片，将展示“欢迎使用小艺建议”的卡片刷新成有服务推荐的卡片，最后重新开启意图框架调试开关。
6. 打开意图调试助手：进入小艺App，返回主页面，切换“发现”页签，在搜索框内搜索“意图调试助手”，点击进入意图调试助手。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/DuAm1WU_Q0CzRrbYLG6x9g/zh-cn_image_0000002791566810.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=1159FBDD836DA5EA3DCB929AB36A238B3594ACA602C7EB7526916FF59E22D074)

完成以上所有步骤，即可进行联调。
