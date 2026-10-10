---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:13+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:dc03dda0c50b2dea31e1b122f5692a03b1c045c50efa1d25dbd16bdb0184a331
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/oCpeoTSYSlm18EvRRuQUew/zh-cn_image_0000002731542347.png)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/G22EG7X0QISSn6-o4-12LQ/zh-cn_image_0000002701823068.png)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/PgODzBdPQCePdv2yFi4Qqg/zh-cn_image_0000002701663144.png)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/piXcNNBRRZuJTlutOc7MDw/zh-cn_image_0000002731382377.png)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/DIRveuF5RmmGYim5jCdVlA/zh-cn_image_0000002701663148.png)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/g9jbnMzqT4irEpWOHZG0MA/zh-cn_image_0000002701823064.gif "点击放大")
