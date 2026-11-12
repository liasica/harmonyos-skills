---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:59e596b88de876acc81bf8e93959ae098d30653d010e2ee5b14e954d7d02038e
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/lslDeGxsTva-iVivBfJGnA/zh-cn_image_0000002779566848.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=852F1B0CBA53886205213328D0E4A1A4B4FE761D05010AEFB4EE8D19D6E89B94)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/y_sUDP1MTIqRnLxEfhYYLQ/zh-cn_image_0000002779566846.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1135F4361C1A9040461AA8D30113E3EE47A0FB109743861A5B03F575FCDEF406)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/u1LR9So9T9OySazIDhUHqg/zh-cn_image_0000002779406868.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D6A24B4EAA1845219370CD42D323C76662DAE5D59B8595280BDD9C7BE210500)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/43r6QC00QD-v2wx6Jd1ZHw/zh-cn_image_0000002808766431.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8886E687387A9D1BB5A3EE90F850B33CF3E8FCBBB9091947BF70516D33101670)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/B591qwizTICTExdnFchFig/zh-cn_image_0000002779406870.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=372298ABBFCEB65440203FEC1F2D9F110E14286195FE5C783C8905024596A04D)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/XBe0oVaBTM6HVo1CPD1U2g/zh-cn_image_0000002808766427.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A2087F5F35E39B4C886725E91FE8165FA2D20E3D7B608D32B82B1F7AFC03086 "点击放大")
