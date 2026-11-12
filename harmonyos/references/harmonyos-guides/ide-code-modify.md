---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-modify
title: 代码修改
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码修改
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:8be1352dd50299092a2e68decfa06c2c540f5f93fb8c2e1c3cac70dc19df91ce
---

CodeGenie提供代码修改能力，在**对话框内**输入需求描述，生成符合要求的代码，提升代码质量与开发效率。

在DevEco Studio 6.0.1 Beta1和Release版本，生成的代码与原文件代码可快速对比和采纳。

从DevEco Studio 6.0.2 Beta1开始，生成的内容直接被应用到代码文件中。

从DevEco Studio 6.0.2 Release开始，代码修改使用的是HarmonyOS Act智能体。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入**@**符号选择**Files**，或点击**@****Add Context** > **Files**，或在对话框输入文件路径，指定需要分析的代码文件。未指定代码文件时，分析当前代码文件。
2. 在对话框输入描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/1Ak3fDWBT-6jNd3IYsY41Q/zh-cn_image_0000002779407108.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E9DB8E601798B3210B57653F17730F9304B238777AEFF0581B05F1CB748D3C5)发送。
3. 在问答区域的**Changed Files**可以查看被修改的文件；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/eu6Ek2mMQcCLavlFSMvLlQ/zh-cn_image_0000002779567086.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B57DE97C4765DCC20FE40D76CEF9CB5AF93E11EBDF27B8DC6588FF3B1A1048BD)可接受或拒绝该文件的修改。
4. 点击问答区域中**Run**，可以编译验证；开启**Auto Run**开关，可以进行自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/9a9-G6QCQ6iPzoRTBveWdQ/zh-cn_image_0000002779407106.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4785622438CA658AD8DED3FF1F598E99EA29C2C8EB83D1EF481FF77AFAD5ECC6 "点击放大")
