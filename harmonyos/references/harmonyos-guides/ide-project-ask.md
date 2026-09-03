---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-ask
title: 工程问答
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 智能问答 > 工程问答
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:27+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:3f9b15c024c9256414d535a549ef45fcf84c0fc8c5e0a8f40aa241ce1de8d65e
---

从DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie 新增工程问答能力。工程问答能够基于当前本地工程进行代码理解与分析，帮助开发者快速完成代码检索、定位和解读等工作。系统可自动分析工程结构，精准定位文件、类、函数、变量、常量、UI 元素等代码实体，并针对开发者提出的问题给出准确回答。

从26.0.0 Beta1版本开始，对于HarmonyOS应用开发相关问题，工具会自动检索HarmonyOS应用开发文档，提升问答的准确性，以及在同一会话中，支持多轮对话，实现深入问答。同时，支持在工程问答时调用MCP Market工具，问答时可自动调用相关MCP工具，实现更多功能；支持调用LSP（Language Server Protocol，语言服务器协议）工具，进行代码查找和引用查找；支持ArkTS和C++代码语义检索能力，用于跨文件、跨模块的代码搜索，有效提升查全率和准确率。调用MCP工具、LSP工具、开启语义检索的操作和示例如下。

## 调用MCP工具

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/4lM5KQtMSNiNinNrpWLwPQ/zh-cn_image_0000002731382927.png "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Jv85rfp1S4udWdnnFcXKRA/zh-cn_image_0000002731542897.png)按钮，选择**MCP > MCP Market**。
2. 添加和开启所需的MCP工具。
3. 返回到CodeGenie首页，在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/oUo5WBOhT6yIXlIvID8cpw/zh-cn_image_0000002701823628.png)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/EdbvRAWpQ-2ePx9RRxPhoQ/zh-cn_image_0000002731542899.gif "点击放大")

## 调用LSP工具

在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/XKV_ur_RSn-9FYFodcn0cA/zh-cn_image_0000002731382933.png)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/6KaYOF-eTYeaipoW3lkKjQ/zh-cn_image_0000002731542901.gif "点击放大")

## 语义检索

1. 在菜单栏点击**File > Settings...（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > General**，勾选Project Semantic Index下的**Enable**选项。
2. 点击**Apply**或点击**OK**，开启语义检索功能。
3. 在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/NYFb0BEXRWS5eggJRVCOmg/zh-cn_image_0000002731542907.png)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/Rgn7Fuj8RHuGT9up4TbZUg/zh-cn_image_0000002731382929.gif "点击放大")
