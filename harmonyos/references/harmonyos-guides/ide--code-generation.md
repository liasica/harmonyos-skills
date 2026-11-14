---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:08+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:da7ca8e55dcea8e8d62d28fdb39d8fc10d0abda4852723bb85fc926c5ef146ba
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/qqqL9mmFRKKTgoz-vMQirw/zh-cn_image_0000002779566848.png?HW-CC-KV=V1&HW-CC-Date=20261114T004720Z&HW-CC-Expire=31536000000&HW-CC-Sign=D626CD9577B690B7E46EE459107D0F72C0A5F140BB29187EF031D31EC089FC9A)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/TA-3V7rETEuAGiFJATDbIw/zh-cn_image_0000002779566846.png?HW-CC-KV=V1&HW-CC-Date=20261114T004720Z&HW-CC-Expire=31536000000&HW-CC-Sign=2429C9BCD10C7F02AA4E873A3E3928ED526BFD67D827464AB87410A7CD601AB4)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ZD9f-c_8Sh6XgSM8lqL65w/zh-cn_image_0000002779406868.png?HW-CC-KV=V1&HW-CC-Date=20261114T004720Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB259131CBB09D054F029FF0670ECFD4ECBAC09B9AC5BA98E9AEBB69AA26BAB1)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/gqOP2wUARe-zKKgVufaVcQ/zh-cn_image_0000002808766431.png?HW-CC-KV=V1&HW-CC-Date=20261114T004720Z&HW-CC-Expire=31536000000&HW-CC-Sign=31E7A2A3687F8C655F1CC401B71397AC93D946E12CB0DC22CF171A36DA514A9A)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ZuO9LgO2T2C46xlUhoef1Q/zh-cn_image_0000002779406870.png?HW-CC-KV=V1&HW-CC-Date=20261114T004720Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BDADEEE44380F4578AA6419595DD31C59F1205B6222F2E4E46306E74733C9E4)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/fiAYTv_DQ0SwmZn-iaNMAg/zh-cn_image_0000002808766427.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004720Z&HW-CC-Expire=31536000000&HW-CC-Sign=F79E29B84E28A9FC03E5D3BA75835BD82352A16685961C3BBE40B063A3D3B1EF "点击放大")
