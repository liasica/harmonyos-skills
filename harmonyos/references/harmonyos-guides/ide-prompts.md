---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2ba0444b170f1f157e6319990b3b1477aaef75a39762e56e454b469ca10cd587
---

## 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/3Rn5_b_XQ8yrZEUwgrJ2XA/zh-cn_image_0000002779407062.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D85B2CF6F8FA49503CEF53233593F15014269851611E568FCE0FE2E1BEC2A7FB)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/WvuhdVgXQ8CRXuNSWn_iSw/zh-cn_image_0000002779567044.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3F56D228170A688DC0C8AD2BB8FAB73A2840F098C703655456BEC10F51AB8B2)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/9lHiTyIwQda7JuVdAdBO9g/zh-cn_image_0000002779407066.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1F6F773B5512FEB575C3C7ADD31E77591D0270A63D5060390A52298A53911FC)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/ZDozWFZXTa63EoUhPPv0Lw/zh-cn_image_0000002779407064.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=473F477EFD91DAAAE1F99A961C3498AE48907E1F9C40D5EDDA2C571520261802)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/wO_gLkPARoezBIQ7AKm3Aw/zh-cn_image_0000002779567042.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=621BDD642D2A1C440C809A41A0F28CD61BBFFE15F1583F3CA3763593412AF6C5)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ww4gYq9dRcSMu-BABAUGfA/zh-cn_image_0000002808886701.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2996C231E4EDBE7CE91E52914FE45D9E02B6FBDE64698818EC309F420D357267)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/OBp2pZmcSZuxS4XPIYpTLA/zh-cn_image_0000002779407060.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1259B73D815C5792D687A545C6FFA6CA47D3AED3E2664490AD59769C3B33FD8)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/NVmxZCIKSEu7Hnwc3ajyVQ/zh-cn_image_0000002808766619.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C533DE11FEA97C7161E74D64B77ECBBC07983C38D2C97B0BD974D42B105B8797)
