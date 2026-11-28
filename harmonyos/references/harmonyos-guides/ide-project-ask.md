---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-ask
title: 工程问答
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能问答 > 工程问答
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fc828be3bef02d7ccb6b38026a01fd1d1ad910c29edb9a03d596360fd475a4b9
---

从DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie 新增工程问答能力。工程问答能够基于当前本地工程进行代码理解与分析，帮助开发者快速完成代码检索、定位和解读等工作。系统可自动分析工程结构，精准定位文件、类、函数、变量、常量、UI 元素等代码实体，并针对开发者提出的问题给出准确回答。

从26.0.0 Beta1版本开始，对于HarmonyOS应用开发相关问题，工具会自动检索HarmonyOS应用开发文档，提升问答的准确性，以及在同一会话中，支持多轮对话，实现深入问答。同时，支持在工程问答时调用MCP Market工具，问答时可自动调用相关MCP工具，实现更多功能；支持调用LSP（Language Server Protocol，语言服务器协议）工具，进行代码查找和引用查找；支持ArkTS和C++代码语义检索能力，用于跨文件、跨模块的代码搜索，有效提升查全率和准确率。调用MCP工具、LSP工具、开启语义检索的操作和示例如下。

## 调用MCP工具

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/I6_e318FSQaz2A10dbNGaA/zh-cn_image_0000002779407190.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A55CDD36812624BF174937986EBBDE0F53860F9C0E72A79C972409B6F628C6F "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/nNeHY94gTs6TQLoDCheqLQ/zh-cn_image_0000002779567164.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3AD739C1C5F5F102F44794DE8C43A951836DEB15ADDAC56AA79A59AEAB5BA0A)按钮，选择**MCP > MCP Market**。
2. 添加和开启所需的MCP工具。
3. 返回到CodeGenie首页，在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/CCIKc7iJSnmAy2eJ-R3NEQ/zh-cn_image_0000002779567166.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=75544D598521FF59954693BA0C07E48E9FD082F74CFDD2439E4F3065B4132819)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/FCZpU15CTaGisEIx9BXQXA/zh-cn_image_0000002808886833.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E5B6A2CF03454CA80FFF461C04AB6BA549DD2580D617774E1CCE67D8A3A7617 "点击放大")

## 调用LSP工具

在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/TS6GKiEBSiu1FdHoJ9GGQw/zh-cn_image_0000002808766751.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3F4C65DC0C44857C6B66126FCA0E87E8D30C10C8101F377ACFF296625F07320)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ejtBsNlXSpOQoE5YM1nyqg/zh-cn_image_0000002779407188.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD891F664F6EAE2E426341811D317B1294ED01FD33A6B0CB19DF174C7E1A20C2 "点击放大")

## 语义检索

1. 在菜单栏点击**File > Settings...（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > General**，勾选Project Semantic Index下的**Enable**选项。
2. 点击**Apply**或点击**OK**，开启语义检索功能。
3. 在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/TixToyAATNOQGWHoUCDL1w/zh-cn_image_0000002779407186.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F52AB73E801A13C30029F56DD32484923583579B62CCFB09121B87F075D181D)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/g-IT83gMSVqC7qCqzEUgAQ/zh-cn_image_0000002779567168.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=17523A3B65C5147265F11AC4B4F827A69D5CEF0C837CCE09D8EE0D717F80BEF4 "点击放大")
