---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:02+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b36fb3aedcdbb6ae6a14901f5d41da1f24a59094800baf152beacb49c31a8ff2
---

## 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/m_q4Iou5Qpy9CqcbtdrY4g/zh-cn_image_0000002701663234.png)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/OuKQpo1RRiGSU7ftSYlizg/zh-cn_image_0000002731382461.png)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/h6rpNjnAQym_gkuNaDvbBg/zh-cn_image_0000002701663242.png)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/mngTN1FlTsuqbA2r5lPVmw/zh-cn_image_0000002731542433.png)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/JDXlk1CERc-V8CTDi7eN4A/zh-cn_image_0000002731382457.png)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/lJjQdh2fR8i6qRqAO7CU7w/zh-cn_image_0000002731542425.png)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/zog87HtCRkSe92OqDH7wPw/zh-cn_image_0000002701823150.png)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/nd4Heu8ZTh28aaWCjZ_NAQ/zh-cn_image_0000002731382451.png)
