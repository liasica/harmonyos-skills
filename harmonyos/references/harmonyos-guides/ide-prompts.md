---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9438103fe7ee4d2f9372027e0d3cae187c3397b43570a7b52d4e2150ee5a8825
---

## 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/xFmfHkIfQg-TNNsn_G_9Pw/zh-cn_image_0000002779407062.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=9802152E3593157EACEB39E17661DA59B13EFEC19CC792F2D0FE96FDAA4F28EA)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/5Ue49Qg_RSaIfAjhrlIfkw/zh-cn_image_0000002779567044.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=D000E9F8C2D0D398C933D8B59017CEC80C6B0F1C77D88E1A1CCC0D18EB0FB825)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/gYR-bxFFQc2u_OQG5EM7MQ/zh-cn_image_0000002779407066.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=75AAB0964C49F0F25468E12E4C35C3AF7BB94741891E51D8692EB1EFAB6A9A79)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/SZ_Jk8yCTDqpq6zHhIXTBw/zh-cn_image_0000002779407064.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=737066DE816DCB386082B3018AB2AF3CD8F58EBF14B5B1FFD6186D8F1AE55F67)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/1cyStRDvSkKz0kHaBIJnqg/zh-cn_image_0000002779567042.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=424725812FEF71FE3C7E7C66AF9E5D2AE93D27026B3F0A675BEFACF797C65AE9)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/9qalU8OcSSKmnKpgxxY9mw/zh-cn_image_0000002808886701.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=B97D9767B06ECBCC40B9CB9C62168171AD94A7A2DF1F4C3104215124C8FDD4C7)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/iPpkl0tkTvWI1ZDrTYTYUg/zh-cn_image_0000002779407060.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAF03A1CCD4D6B487DAC307CCC32A9C03F782AE46D7A67EA7F3BE11569EE74F0)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/VWjDI8i8Ssy5PMhv5qz8QQ/zh-cn_image_0000002808766619.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=842A4BE7E5C46EE99CA1A0753A9122C48D2038F406E9D8CF99F01B752C285C1F)
