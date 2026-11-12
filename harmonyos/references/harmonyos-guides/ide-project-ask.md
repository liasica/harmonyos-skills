---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-ask
title: 工程问答
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能问答 > 工程问答
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f8c41a0ee62b41e001b08b5afe8cddc88e7742dbd40fb311fe0f2152b6eed967
---

从DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie 新增工程问答能力。工程问答能够基于当前本地工程进行代码理解与分析，帮助开发者快速完成代码检索、定位和解读等工作。系统可自动分析工程结构，精准定位文件、类、函数、变量、常量、UI 元素等代码实体，并针对开发者提出的问题给出准确回答。

从26.0.0 Beta1版本开始，对于HarmonyOS应用开发相关问题，工具会自动检索HarmonyOS应用开发文档，提升问答的准确性，以及在同一会话中，支持多轮对话，实现深入问答。同时，支持在工程问答时调用MCP Market工具，问答时可自动调用相关MCP工具，实现更多功能；支持调用LSP（Language Server Protocol，语言服务器协议）工具，进行代码查找和引用查找；支持ArkTS和C++代码语义检索能力，用于跨文件、跨模块的代码搜索，有效提升查全率和准确率。调用MCP工具、LSP工具、开启语义检索的操作和示例如下。

## 调用MCP工具

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/3bbaWxLKRjSzO-3XGPIstA/zh-cn_image_0000002779407190.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBDC009D5608CD7D2D9E168E0DBD4E61526EFC922535E8C86402C044DE327CF6 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/5bkdvzRJSUy8FFfgX-M0hA/zh-cn_image_0000002779567164.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E33DDE4C28B3380E183663E797046AC7902C1DA7E3C29198CC41DD8F0593A563)按钮，选择**MCP > MCP Market**。
2. 添加和开启所需的MCP工具。
3. 返回到CodeGenie首页，在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/3EVJDlZDR0aDcayvgRxnig/zh-cn_image_0000002779567166.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E301AAD9984E6478673B8F640EF5543B29B768C9216514E68A3800A229D83EE)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/8m0yatowQQO8LbleofEBVQ/zh-cn_image_0000002808886833.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF0DBE9A6845C75CAAC152BE2CC1230FB3ACE534BFB940C30C8E256F870E8F2E "点击放大")

## 调用LSP工具

在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/774LJEEGT_SDfg-FjNnhnA/zh-cn_image_0000002808766751.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1416DDC861375B1E574D639CDFDE1AEFEF48D80507E6956987A51517391F40FB)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/U3GKPPUlRN6wtnXjGC_iZA/zh-cn_image_0000002779407188.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB6926409435E0008F4A76A1654C0999E1A019CA111C4C568A27024F76EFBE5 "点击放大")

## 语义检索

1. 在菜单栏点击**File > Settings...（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > General**，勾选Project Semantic Index下的**Enable**选项。
2. 点击**Apply**或点击**OK**，开启语义检索功能。
3. 在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/-5OpuciHSCCcsaA3AzVWhg/zh-cn_image_0000002779407186.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=725F684FF0C91F39ED611B272E6668FCDDAE9609CDBC301AE97A61D1327DEF0D)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/u2aKKOsSQRSPdsKLUvqBqw/zh-cn_image_0000002779567168.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=360946709F24BDFE7127BAA0FFFB06D600B1AC0278BBA989D0BE0237EEF4A7CA "点击放大")
