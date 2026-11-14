---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5020ebc51111dad7c94749026f622bc5505d6445ba3364fbb2ec2c75a2197c67
---

## 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/hcPQgn-ISyC4wnwBzPFCng/zh-cn_image_0000002779407062.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8FF6EBBC3F1A56719BA67A955056C681B5EDA1E407998FF1DEAF4D906AA79E5)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/2N6Srz4lQnCYXPggOlPEsA/zh-cn_image_0000002779567044.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD5E7A06E0C9A7B678AC003B5B86B87A770350040C5A233FAF72FE26E53BB7C8)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/rfFQaJYkRzS2ESJOKOYiEQ/zh-cn_image_0000002779407066.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2A33F518BEFBAF84D81A47DDF00B34046B1E9FA9D1395B3A7210B46D504DF4B)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/qQTcSizhTyGbk_D-egpSOQ/zh-cn_image_0000002779407064.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB9B385478857A072DE7690088815BB7AF3BFA451C1544162BFBA8FD781799F)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/mRdzVSZGSFey62wpiXb9Bg/zh-cn_image_0000002779567042.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AF8B987FA63BA2AF7E12F5C2C53FBE63F5852841973D9D6406BA845C8E53767)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/_aXt5GpiTz-k6dTUdijIjA/zh-cn_image_0000002808886701.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=B574E127CCC8A932791A7FA272030AEC779E51B5EB591E79C7951BDDDCFA3E74)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/TfxfVJpWTh-vkV67irTIpg/zh-cn_image_0000002779407060.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=52C7ABCDCA5A8401C347A761F138841B2B3D8A95A7C313F671B32F280959AAF1)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/D4kxA40NQyuVB2BcfxLSXw/zh-cn_image_0000002808766619.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=9538929269C1DA2925E5772622B79A05E5773406AE877CA71F09E1BA68FC546C)
