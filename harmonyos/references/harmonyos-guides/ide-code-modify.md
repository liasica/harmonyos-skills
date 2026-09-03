---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-modify
title: 代码修改
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码修改
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:204c1c9376eab9af324610f16c299d2413a8722e036971c32a8c1b6ecff8f4aa
---

CodeGenie提供代码修改能力，在**对话框内**输入需求描述，生成符合要求的代码，提升代码质量与开发效率。

在DevEco Studio 6.0.1 Beta1和Release版本，生成的代码与原文件代码可快速对比和采纳。

从DevEco Studio 6.0.2 Beta1开始，生成的内容直接被应用到代码文件中。

从DevEco Studio 6.0.2 Release开始，代码修改使用的是HarmonyOS Act智能体。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入**@**符号选择**Files**，或点击**@****Add Context** > **Files**，或在对话框输入文件路径，指定需要分析的代码文件。未指定代码文件时，分析当前代码文件。
2. 在对话框输入描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/2JFkCevRTf6Jg07RPh6Xlg/zh-cn_image_0000002731382505.png)发送。
3. 在问答区域的**Changed Files**可以查看被修改的文件；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/ftLuZoqERJCeKTRV83Ypog/zh-cn_image_0000002731542475.png)可接受或拒绝该文件的修改。
4. 点击问答区域中**Run**，可以编译验证；开启**Auto Run**开关，可以进行自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6CBAdkpnRpeeUjppo0nvsA/zh-cn_image_0000002701823198.gif "点击放大")
