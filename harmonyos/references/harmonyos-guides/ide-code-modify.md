---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-modify
title: 代码修改
breadcrumb: 指南 > 使用AI智能辅助编程 > 智能执行 > 代码修改
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6a8714f788232bbb3f02421869676f5a435974403de894ca2a4dbcb674a0843
---

CodeGenie提供代码修改能力，在**对话框内**输入需求描述，生成符合要求的代码，提升代码质量与开发效率。

在DevEco Studio 6.0.1 Beta1和Release版本，生成的代码与原文件代码可快速对比和采纳。

从DevEco Studio 6.0.2 Beta1开始，生成的内容直接被应用到代码文件中。

从DevEco Studio 6.0.2 Release开始，代码修改使用的是HarmonyOS Act智能体。

以DevEco Studio 6.0.2 Release和DevEco Studio 6.0.1 Beta1版本为例说明，如下。

**DevEco Studio 6.0.2 Release**

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框中输入**@**符号选择**Files**，或点击**@****Add Context** > **Files**，选择需要修改的代码文件，或在对话框输入文件路径指定需要修改的代码文件，或修改当前代码文件。
2. 在对话框输入描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/5cIoTeR-ReawG26lelL4KQ/zh-cn_image_0000002561833125.png?HW-CC-KV=V1&HW-CC-Date=20260429T054509Z&HW-CC-Expire=86400&HW-CC-Sign=71B9DF04D04684CE043D2F3CD789E68C5AD82E4DDF971DA63D06A3843FCDBC9C)发送。
3. 在问答区域的**Changed Files**可以查看被修改的文件；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/sUWXmt5SRDOcawO5W1gUig/zh-cn_image_0000002530753204.png?HW-CC-KV=V1&HW-CC-Date=20260429T054509Z&HW-CC-Expire=86400&HW-CC-Sign=E8B5110A1AF7FCD7F162EB2CD97C4D32DD6F5267EE3662CEBCF0B46621BFBC43)可接受或拒绝该文件的修改。
4. 点击问答区域中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/pSv5SWIBR0214JBKYEMfBw/zh-cn_image_0000002530753202.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054509Z&HW-CC-Expire=86400&HW-CC-Sign=0BDB9C05BBD100DE19E4F42B98466CEE6F30163871449C0A8C39736571A8449F "点击放大")

**DevEco Studio 6.0.1 Beta1**

**操作步骤**

1. 点击**@Add Context >** **Files**选择需要修改的文件，在对话框输入代码修改描述。
2. 在对话问答区域，点击文件路径，打开代码对比页面。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Fo4TWUNCSzGUUOUEXUE7ZQ/zh-cn_image_0000002530913198.png?HW-CC-KV=V1&HW-CC-Date=20260429T054509Z&HW-CC-Expire=86400&HW-CC-Sign=8C3D17BA698A4E51678D977ABF1222F1AA15D4CA580A2880337C718694515F4A)，快速采纳修改后的代码。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/wd5HEF8iRrCm_cMRV2W2hQ/zh-cn_image_0000002561753141.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054509Z&HW-CC-Expire=86400&HW-CC-Sign=49CA3AC8ADD69AD1AC3AB34EDA60AE4D62D0D0F7A3FDEC5CD5063F5828647380 "点击放大")
