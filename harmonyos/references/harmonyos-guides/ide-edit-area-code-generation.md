---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation
title: 编辑区对话
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 编辑区代码生成 > 编辑区对话
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4a7e75bcde968b0752945083a6ebb035774372385594833f1f6b1c14e182ebcb
---

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

1. 当前有以下两种方式唤醒Inline Chat对话框：
   * 若未选中代码片段，在代码编辑区域右键选择**CodeGenie > Inline Chat**（或使用快捷键**Alt+I**，macOS中为**Command+I**）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/cJQ7EzbyTzeWtgkL2O5Lvg/zh-cn_image_0000002731382655.png)
   * 若选中一段代码，点击**Inline Chat（**或使用快捷键**Alt+I**，macOS中为**Command+I）**浮框，如未出现浮框，请参考如下操作启用。
     + 从26.0.0 Beta1版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie >****Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。
     + 从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Suggestion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Suggestion & Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。
     + 从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Completion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Completion & Inline Chat**）中勾选**Show Inline Chat tips**启用浮窗。
     + 在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在**File** > **Settings** > **CodeGenie** > **Code Generation**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Generation**）中取消勾选**Hide Inline Chat Overlay**选项。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/BzX9kQjlSFanzQlqyA0v8g/zh-cn_image_0000002701823362.png)
2. 选择在CodeGenie中已配置的三方模型，或者使用内置模型。三方模型配置具体请参考[模型（Model）配置](ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/lte5X_pzTGGLv6zfRuNZ2g/zh-cn_image_0000002731382657.png "点击放大")
3. 在对话框中输入代码功能描述，点击发送或在键盘输入回车，等待代码生成；或在对话框中输入"/"，选择不同的快捷指令，进行代码文件分析或生成分析报告等。内置模型从26.0.0 Beta1版本开始，支持使用快捷指令。

   快捷指令的具体操作如下：
   * 未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/i4rEAChyTsuVv60oZujMFw/zh-cn_image_0000002731382651.png)
   * 选中一段代码，在对话框中输入"/"，选择**Parameter Validation**（参数校验）、**Code Explanation**（代码注释）、**Code Optimization**（代码优化），可输入或不输入功能描述，在键盘输入回车或点击发送后等待生成，分析报告和参数校验等结果跟模型有关。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/jOHIZ1fxTmSrMlYJ0QZGRA/zh-cn_image_0000002731382663.png "点击放大")
4. 生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。
   * 绿色区域：新生成的代码内容。
   * 蓝色区域：对现有代码进行修改的内容。
   * 红色区域：删除的代码内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Beyqu9ljQ9OF-r2EvS81rw/zh-cn_image_0000002731382659.png)
   * 点击Inline Chat对话框中**Accept All**（或使用快捷键**Alt+Enter**），接受当前生成的全部内容；
   * 点击Inline Chat对话框中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/QpmklouYQKSC0VCwSmhI7g/zh-cn_image_0000002701823350.png)刷新按钮**/****Regenerate**，将根据当前描述重新生成代码片段；
   * 点击编辑区中**Accept**（或使用快捷键**Shift+Ctrl+Y**，macOS上为**Shift+Command+Y**），分段逐一接受并保留生成内容；
   * 点击编辑区中**Reject**（或使用快捷键**Shift+Ctrl+N**，macOS上为**Shift+Command+N**），分段逐一拒绝并删除当前生成内容；
   * 点击**Further Edit**（或使用快捷键**Ctrl+K**，macOS上为**Command+K**），重新进行输入，开始新一轮问答。
