---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation
title: 编辑区对话
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 编辑区代码生成 > 编辑区对话
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:08+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:79141940ac4884d420f50e1e45d4d44241cf3d32b40969c18a0f8b4b2eefc170
---

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

1. 当前有以下两种方式唤醒Inline Chat对话框：
   * 若未选中代码片段，在代码编辑区域右键选择**CodeGenie > Inline Chat**（或使用快捷键**Alt+I**，macOS中为**Command+I**）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/1v3uVlRRSZaO_zfHqdLGKw/zh-cn_image_0000002779567050.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=C34746CF98C9E17AF4618D6C6DB4722DAB6B1FC30EBF5304BF16170C417035A4)
   * 若选中一段代码，点击**Inline Chat（**或使用快捷键**Alt+I**，macOS中为**Command+I）**浮框，如未出现浮框，请参考如下操作启用。
     + 从26.0.0 Beta1版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie >****Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。
     + 从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Suggestion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Suggestion & Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。
     + 从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Completion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Completion & Inline Chat**）中勾选**Show Inline Chat tips**启用浮窗。
     + 在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在**File** > **Settings** > **CodeGenie** > **Code Generation**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Generation**）中取消勾选**Hide Inline Chat Overlay**选项。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/1k6YgxYITDKHe88HPh1onw/zh-cn_image_0000002779407074.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4801C0AE6DA305753AC87E07EE1B24D88B2F51DF5DF8F93485DB46FB211CCDC)
2. 选择在CodeGenie中已配置的三方模型，或者使用内置模型。三方模型配置具体请参考[模型（Model）配置](ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/T2OSlL4HT0KF9IWp4bnmsQ/zh-cn_image_0000002808766631.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB9DED2C0DDC8388390D9B5DBF31C23FBBBD18D007FE4DDE81146B337351AA07 "点击放大")
3. 在对话框中输入代码功能描述，点击发送或在键盘输入回车，等待代码生成；或在对话框中输入"/"，选择不同的快捷指令，进行代码文件分析或生成分析报告等。内置模型从26.0.0 Beta1版本开始，支持使用快捷指令。

   快捷指令的具体操作如下：
   * 未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/4F39InlUSjyDXiky6BGwEA/zh-cn_image_0000002779407070.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FA8DC5CB145146530A9F8EF33A466E3018718C564B224A080D96DBD7A09054A)
   * 选中一段代码，在对话框中输入"/"，选择**Parameter Validation**（参数校验）、**Code Explanation**（代码注释）、**Code Optimization**（代码优化），可输入或不输入功能描述，在键盘输入回车或点击发送后等待生成，分析报告和参数校验等结果跟模型有关。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/m_Zx--52R0Oi4yho0M3Cdw/zh-cn_image_0000002779567052.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8400829BFFAAF77523C34E010011B70F5B434ACC46B48D3B42BA817F4D918E9 "点击放大")
4. 生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。
   * 绿色区域：新生成的代码内容。
   * 蓝色区域：对现有代码进行修改的内容。
   * 红色区域：删除的代码内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/rJohOKIkQKWsl6lXXAno4g/zh-cn_image_0000002779407072.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=23B6D3543E7B7AEBD26444ACFA10E6DAAFF6444F5E5860FDB5FCA6D844ABE463)
   * 点击Inline Chat对话框中**Accept All**（或使用快捷键**Alt+Enter**），接受当前生成的全部内容；
   * 点击Inline Chat对话框中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/28T3Xzl5Sw60HB2gI0gS6A/zh-cn_image_0000002808886711.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=49E2F0C3D9286E38D5F507C29BC23C7DC53022AB900A8BE8722FC9A666C73989)刷新按钮**/****Regenerate**，将根据当前描述重新生成代码片段；
   * 点击编辑区中**Accept**（或使用快捷键**Shift+Ctrl+Y**，macOS上为**Shift+Command+Y**），分段逐一接受并保留生成内容；
   * 点击编辑区中**Reject**（或使用快捷键**Shift+Ctrl+N**，macOS上为**Shift+Command+N**），分段逐一拒绝并删除当前生成内容；
   * 点击**Further Edit**（或使用快捷键**Ctrl+K**，macOS上为**Command+K**），重新进行输入，开始新一轮问答。
