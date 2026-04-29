---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation
title: 编辑区对话
breadcrumb: 指南 > 使用AI智能辅助编程 > 编辑区代码生成 > 编辑区对话
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:11+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:75c00863cc737163e819e56dd5cdc3213292b6cb84c5a83eeb1bf6739443aea2
---

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型进行生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

1. 当前有以下两种方式唤醒Inline Chat对话框：
   * 若未选中代码片段，在代码编辑区域右键选择**CodeGenie > Inline Chat**（或使用快捷键**Alt+I**，macOS中为**Command+I**）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/mb8QhMBjTRSC4nQDn0q2HA/zh-cn_image_0000002530753294.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=77B798FB4502E187C4CEB8A770740D4FA5A7D3125AF2ADDE238B8CE1C37FA997)
   * 若选中一段代码，点击**Inline Chat（**或使用快捷键**Alt+I**，macOS中为**Command+I）**浮框。

     在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在**File** > **Settings** > **CodeGenie** > **Code Generation**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Generation**）中取消勾选**Hide Inline Chat Overlay**选项。

     从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Completion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Completion & Inline Chat**）中勾选**Show Inline Chat tips**启用浮窗。

     从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Suggestion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Suggestion & Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/RiVbw_5qRIuLpgmtIRMIAA/zh-cn_image_0000002530913284.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=4FE6F0D0E038760A8C36D69134E4BA0E6A60E1929F9456FE660EC842C33CEDC4)
2. 选择在CodeGenie中已配置的三方模型，或者使用默认模型。三方模型配置具体请参考[模型（Model）配置](ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/7RBXjnZWSuuitiE1xB7hPw/zh-cn_image_0000002530753296.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=96D283A771300C3080AE489A716171E9E3D28E1F35ED23FDD2049343C21F00A0 "点击放大")
3. 若选择默认模型，在对话框中输入所需要的代码功能描述，在键盘输入回车或点击发送，开始生成代码。点击**Stop Generation**，中断本轮代码生成过程。

   若选择三方模型，支持分析当前代码文件和生成分析报告，以及进行参数校验（**Parameter Validation**）、代码注释（**Code Explanation**）、代码优化（**Code Optimization**），分析报告和参数校验等结果跟模型有关，具体操作如下：
   * 未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/7TlYhnbpQUmgwOzce_3nkg/zh-cn_image_0000002561753231.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=F96FC321A0C0D0C25D63C6768F4FFE949A25601EF81884630899FA627E0F87C0)
   * 选中一段代码，在对话框中输入"/"，选择**Parameter Validation**/**Code Explanation**/**Code Optimization**，可输入或不输入所需的功能描述，在键盘输入回车或点击发送后开始生成。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/bxyLxj_KSiqfNVoAuIVq4Q/zh-cn_image_0000002561833211.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=D15A4DFC3AFE7ECD8AED643D5F94CEDC763BFB2A8F83904A13370406B2239414)
4. 生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。
   * 绿色区域：新生成的代码内容。
   * 蓝色区域：对现有代码进行修改的内容。
   * 红色区域：删除的代码内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ZXsMcqObSvWJ0W1HoSV8_g/zh-cn_image_0000002530913290.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=06D0BC5A7C5146FBE622C86DF1CDD7124820D237AD772DC575960B48FA84BB32)
   * 点击Inline Chat对话框中**Accept All**（或使用快捷键**Alt+Enter**），接受当前生成的全部内容；
   * 点击Inline Chat对话框中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/2eZ_8RH5S4-i7BTgoh_Z5g/zh-cn_image_0000002561833215.png?HW-CC-KV=V1&HW-CC-Date=20260429T054455Z&HW-CC-Expire=86400&HW-CC-Sign=63CA49045CEC2BEAE8212FA8671B84CBA446B22756F37F5B713A0C65C1ED6F71)刷新按钮**/****Regenerate**，将根据当前描述重新生成代码片段；
   * 点击编辑区中**Accept**（或使用快捷键**Shift+Ctrl+Y**，macOS上为**Shift+Command+Y**），分段逐一接受并保留生成内容；
   * 点击编辑区中**Reject**（或使用快捷键**Shift+Ctrl+N**，macOS上为**Shift+Command+N**），分段逐一拒绝并删除当前生成内容；
   * 点击**Further Edit**（或使用快捷键**Ctrl+K**，macOS上为**Command+K**），重新进行输入，开始新一轮问答。
