---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-modify
title: 代码修改
breadcrumb: 指南 > 使用AI智能辅助编程 > 智能执行 > 代码修改
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c30308e30e087cba897ca1c01fc57463962b48b93bf7f56357b3b08533f01715
---

CodeGenie提供代码修改能力，在**对话框内**输入需求描述，生成符合要求的代码，提升代码质量与开发效率。

在DevEco Studio 6.0.1 Beta1和Release版本，生成的代码与原文件代码可快速对比和采纳。

从DevEco Studio 6.0.2 Beta1开始，生成的内容直接被应用到代码文件中。

从DevEco Studio 6.0.2 Release开始，代码修改使用的是HarmonyOS Act智能体。

以DevEco Studio 6.0.2 Release和DevEco Studio 6.0.1 Beta1版本为例说明，如下。

**DevEco Studio 6.0.2 Release**

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框中输入**@**符号选择**Files**，或点击**@****Add Context** > **Files**，选择需要修改的代码文件，或在对话框输入文件路径指定需要修改的代码文件，或修改当前代码文件。
2. 在对话框输入描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/0O154RPlRwOgnI20PAL9mQ/zh-cn_image_0000002561833125.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=A45CC479625489CDE842903978FA8A9DCCCE6828AB2A93151D08E5B14B7224B5)发送。
3. 在问答区域的**Changed Files**可以查看被修改的文件；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Ft68VjJ9TpeWy6Lu9Z676w/zh-cn_image_0000002530753204.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=7112DC892C3033353BA21868771DD20810FF85FF4BD6435F0D9AC5C4EA2CC99C)可接受或拒绝该文件的修改。
4. 点击问答区域中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/28Q7IBvDTvGkRH5WDYVFIg/zh-cn_image_0000002530753202.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=0E254C9A743CD21C69CAABE9279052DD4C945559E76F2790BD0F988FE70D6765 "点击放大")

**DevEco Studio 6.0.1 Beta1**

**操作步骤**

1. 点击**@Add Context >** **Files**选择需要修改的文件，在对话框输入代码修改描述。
2. 在对话问答区域，点击文件路径，打开代码对比页面。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ycojGJzMQjuFXywGixbTUQ/zh-cn_image_0000002530913198.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=F5E91D8FA0823B1A16CDC812889FFF92E4FD2C001FB916CF580294245E5735CB)，快速采纳修改后的代码。

**示例**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/sUiUyyQ3T5OT_5eghZSJ8g/zh-cn_image_0000002561753141.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=47A803742B4E6041D474880EBBBCFB8382FDEEC581F18D3276BF11301A5C28B9 "点击放大")
