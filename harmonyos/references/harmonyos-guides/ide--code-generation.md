---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:38+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:46197d3be662ff0116ca86aa3760b0ccc55b7c5ac1c54c3e0ea01955c91bd074
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Gsk2mqOISNeh0H5QFa0qbg/zh-cn_image_0000002779566848.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B42769D2B629CCFD60AE91C32CAEFD4FF3E5A4088E7B46128CEF83DB63CFCD4)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/sUQaxb-ZQ9axM_RKEgVVxA/zh-cn_image_0000002779566846.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=12179329150034C548177CA9FD9A42C392D9CC8BF5DEC7EFB899E4EE2790AC35)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/6GPsmfsMR2q6snCdaCDSzg/zh-cn_image_0000002779406868.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ACDAB5CBC45CAE01400D76BE34300A38F49FE2F2FB3B3C35930BC4F6B128B05)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/MLtOL4pqS5O2DJksOKsrSA/zh-cn_image_0000002808766431.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3AD43D70D3CA1E4751BC4BD4C33F3BCFD9E9F53C36F7416B9EBE53A22353F09)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ORZFu-vpRg2dP6b6vYy55Q/zh-cn_image_0000002779406870.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=5625ED6428C1318AD2373BD8FD54E873D0F8A329239EA97B638E833300D15293)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/xj_c8k_XRh6FJfnYENckCQ/zh-cn_image_0000002808766427.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D12379440251426947115AE0E568A34D0FEFBA72E1A29727C5C1031429CCF0B "点击放大")
