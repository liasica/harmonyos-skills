---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-analyse
title: 代码分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能问答 > 代码分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:47+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:7f30e52aa77744abcc33356bb5e0793afeed3af4381fbe9455a12b63c5e7d9ed
---

CodeGenie支持在**对话框中**输入对代码段和代码文件分析要求，帮助开发者快速理解代码逻辑、代码功能、技术细节和潜在问题等，提升开发效率。

DevEco Studio 6.0.2 Beta1之前版本，分析代码文件时需要通过**Files**入口选中文件；分析代码片段时，选中代码段后需点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/-xcpS1bcR5aXniPG47gqDg/zh-cn_image_0000002779406464.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BC89B2AC5E329B4BE64ED4079088A41658EECA9AA93AB74B786D653BAD60699)图标开启光标上下文功能。

在DevEco Studio 6.0.2 Beta1版本，分析代码文件时，支持在对话框输入要分析的代码文件或直接分析当前文件；分析代码片段时，选中代码段后直接分析，无需开启![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_EuYOZakTrKVkqInYhTclA/zh-cn_image_0000002808766019.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B954D79B8B676FBA0ED7595B420742EE1F5EB91B4E1DC3C26E84AFC86BFA90D)图标。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Ask智能体分析代码文件。

1. 选择HarmonyOS Ask智能体，在对话框中输入“**/**”，点击**Project**。
2. 在对话框输入**@**符号选择**Files**，或点击**@****Add Context** > **Files**，或在对话框输入文件路径，指定需要分析的代码文件。未指定代码文件时，分析当前代码文件。
3. 在对话框输入描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/k2GFE1IlQQy6MlgJZCN6gg/zh-cn_image_0000002808886101.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=522308FE17A4B8E22351796BA8AE770E29E2E61842AFD2FDF1E7FCB1A25E0025)发送后等待回复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/rgC4ObFtTDqVEQdphAmxRg/zh-cn_image_0000002779566444.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CC3C57997E28343D160A1ABC47B7CF9EFE87DE9185114296AD67EB26E7D5EE7 "点击放大")
