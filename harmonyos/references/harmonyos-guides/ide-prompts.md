---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ee63d1baa5f74494a7bfcf79091a6e4fee0954ddee7c2e04291f350a041e888
---

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/sRKXJJ7DTPqjzv_vEtR5JA/zh-cn_image_0000002561753075.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=42981122C8F693668FADDE90C9825F8D903CF6250740B03404DCAE4EE315F8F0)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/flIj7AOzS6GJP8f15c2mmQ/zh-cn_image_0000002544580918.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=16C9417A3E2AC41AC4E0C9730D8A265C3D4B8F30A725C4CDE3EF51688F58727B)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/adNJ2BScTV2zeGG30uXgzw/zh-cn_image_0000002530753148.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=0649A0FEDC0B9998B6410D48E1C3C196EF6FE01992E0DC509D342132BC4E47E0)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/V--DuDDpRwmAq_dlgm04xQ/zh-cn_image_0000002544421564.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=D1B8D1C379ADBBCC5339900853CC0AD0DC927668EAA2E0850F8143BBABA471B7)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/ze-jkDdZTb2DcSilDS42rw/zh-cn_image_0000002561833061.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B5FB37ED965897B53D1D3D74E1B69C19FD257AD36B5B2D8C4BBE35BE680D1EF1)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/I0b1y6tlRlSdOznzIECBrg/zh-cn_image_0000002575102649.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B54E486C707E935A886E9DE526D446172B2B1BA9BBBE03E8860DADCCA08F8072)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/lCBLw7z3RAmOxj_Wn4lnjA/zh-cn_image_0000002544583224.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=E340E44327C39A40D122353C5602A6957F7428775B34133B648FE999CB5AA0D1)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/SYPPUSVHT3ya4Av4ixz9Cw/zh-cn_image_0000002530753146.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=B9ED32D8A4A83B6A663ECC6A4FB439F2FA62C0C2BBB4DD258B4418C4B3F3DDDB)
