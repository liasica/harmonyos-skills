---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c9ad3bac88c00573108731220d2c189b3429552066b2a796e99a33684ba42a4
---

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/yvB057FmTvOh18QwXbzzsQ/zh-cn_image_0000002561753075.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=CD6C59961B86ABB44B80CA024D6E344AC4C4BC6E4DF50BD7CE329B437A36B8BF)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/sJqD1VPuT6yo6t3eYCMVNA/zh-cn_image_0000002544580918.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=2CB571C85CDE3FE55C4DDDB42ADC7437B804C51D4567BD9D2CD94093B4564999)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/y-o2udK9QxmhA5Aou80C-g/zh-cn_image_0000002530753148.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=3E03A4440A0E42BFE90D0E86F17395796FC3643A8F78B347AFD39AC0D8D1F707)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/NEM1LW1dTo6cOOS_FG94Qg/zh-cn_image_0000002544421564.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=94AB59AD451570B3EEA86AB299285EFDF8AB98D0E007BEBB61CA6EB6CE30D4BF)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/XD2nxF9_SCWDFga9nTa5Kg/zh-cn_image_0000002561833061.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=0A788F7B605D2FBBAA65E44E221A71D259BB57994E574DD34A792C4D498F1BD7)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/uxdSRv9kSBGEug1Ho6AmRQ/zh-cn_image_0000002575102649.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=725B079BE118ACFDF8A9B33EB40F9F0BE51C8382A031BFB547E516684D4CD6E9)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/LyjBebZjQ1GU2fbYf7nHjg/zh-cn_image_0000002544583224.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=F1A97632CB1B6E1799AF604B9ECDDD8C342E95D95AC5178DD54FEFCAD0866C4F)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/OFKh8OIUR_CKW4PMweD6Jw/zh-cn_image_0000002530753146.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=40A7D54E2F3A436721F23F9771CA906CA12A519502FE82D15D6047AE61795F3C)
