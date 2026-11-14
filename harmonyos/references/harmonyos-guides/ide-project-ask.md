---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-ask
title: 工程问答
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能问答 > 工程问答
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:08+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:777bd21ba10b1ae13d89d681ad190f4d0a1666d58994ea4d0fb9fe8ed02d92c0
---

从DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie 新增工程问答能力。工程问答能够基于当前本地工程进行代码理解与分析，帮助开发者快速完成代码检索、定位和解读等工作。系统可自动分析工程结构，精准定位文件、类、函数、变量、常量、UI 元素等代码实体，并针对开发者提出的问题给出准确回答。

从26.0.0 Beta1版本开始，对于HarmonyOS应用开发相关问题，工具会自动检索HarmonyOS应用开发文档，提升问答的准确性，以及在同一会话中，支持多轮对话，实现深入问答。同时，支持在工程问答时调用MCP Market工具，问答时可自动调用相关MCP工具，实现更多功能；支持调用LSP（Language Server Protocol，语言服务器协议）工具，进行代码查找和引用查找；支持ArkTS和C++代码语义检索能力，用于跨文件、跨模块的代码搜索，有效提升查全率和准确率。调用MCP工具、LSP工具、开启语义检索的操作和示例如下。

## 调用MCP工具

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/JWfIRM_CQRC6BYkw_XlA2w/zh-cn_image_0000002779407190.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=14C1DD653BB69F5F1F53A811BC6B986F060C640CB77F159EB8BCD5CE0BCF0758 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/yvUjXC5OQNetvL-yL0PD1w/zh-cn_image_0000002779567164.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=695BE341CCAD19B8ACE85D289B4E5D001D2668F569B3959853ED68EB6D227CB5)按钮，选择**MCP > MCP Market**。
2. 添加和开启所需的MCP工具。
3. 返回到CodeGenie首页，在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/e64LhADQRge0spIwYmMtFA/zh-cn_image_0000002779567166.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=A98B11B7706A043415C24C7C38F9C8DE333C31140A918B703580DA88361F8BB4)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/q6OtAyuQTRmIrRkwQpk3TQ/zh-cn_image_0000002808886833.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=16BB3079D6B43209EFBE7B239EEE747303404C38058501C385867BB8C9746677 "点击放大")

## 调用LSP工具

在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/jQQhEEPcTEaF9Uc0UuBtHg/zh-cn_image_0000002808766751.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=03C297345E095A8BBF3C6FC9A9E3BB57F6C056DBBFEFC78C43EE963EDB2EA0F0)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/HdemlQpCS1Kw6046WqhqdA/zh-cn_image_0000002779407188.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=65596DFE708BEA4BF319F88775003962870C3D858E5F3BF681B146B1030CA469 "点击放大")

## 语义检索

1. 在菜单栏点击**File > Settings...（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > General**，勾选Project Semantic Index下的**Enable**选项。
2. 点击**Apply**或点击**OK**，开启语义检索功能。
3. 在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/vPGdG63ES7msvB1vW6jn5A/zh-cn_image_0000002779407186.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=789ADE1CEA4FD72772FA336F8228A5103EB4AF0B81685F64BAFD659CAF81716E)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/1h5U6RjhRxe49_R3jnfWYQ/zh-cn_image_0000002779567168.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7197840F6BC5CBBDA2A4A79D165C2B90E3EE22A311797223E2F4237472D55E2 "点击放大")
