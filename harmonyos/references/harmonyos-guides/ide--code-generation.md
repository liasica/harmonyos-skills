---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:1da73f2b4d6a08e11b1d5d6af14176683a62d42b86885cc955119649f1dee84e
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/9ZWD4enXQuCuwQZLn0AbQg/zh-cn_image_0000002779566848.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=18D7C19B8EC08828C5B5B66462A3E26758EAAAB48FC40700CDD9C559D9A0D904)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/7CgxQxxnRFibYL4M4aFYYg/zh-cn_image_0000002779566846.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C19C9E6BCD2110C135FE15F0BE0ED764BF10B0A955DF7785FCDE8DB1FCA1807)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/_pWvASZESla6HMaW5uGgLw/zh-cn_image_0000002779406868.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=6269424AEDF2DD2BB3BAE14E651C9A4E5ED4CBE83FCF98EB860CCAEEADB6CF72)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/h949HyjWQ16QNO9N0-JtZQ/zh-cn_image_0000002808766431.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=A277519ABF530BF750D450F6AB3743300DD987C8360B312CD28E32CF5550E5D2)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/AL__0KGBRNuUpEilQNbsNQ/zh-cn_image_0000002779406870.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=602F2BC563BB63E841C466B8D976F19E182ED18A11B69336A6EBFEFE8EC22E14)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/jkmRSnUrQbCwvNmrDttobg/zh-cn_image_0000002808766427.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=93522FD34E2660AC8716C7B70CDE9F24124A1E1EB8077113DBB1EE5F6C2367B5 "点击放大")
