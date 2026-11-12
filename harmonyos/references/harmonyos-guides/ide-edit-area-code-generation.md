---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation
title: 编辑区对话
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 编辑区代码生成 > 编辑区对话
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:c55fa0792d41ee7a4b9c3069b6d4f262d7b70429f5acb40a95e8ae8695c94f75
---

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

1. 当前有以下两种方式唤醒Inline Chat对话框：
   * 若未选中代码片段，在代码编辑区域右键选择**CodeGenie > Inline Chat**（或使用快捷键**Alt+I**，macOS中为**Command+I**）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Od26sCV6RJaBdmISDQ_dJA/zh-cn_image_0000002779567050.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAFEFEB0AB704BC5E6BACAE0E09B8E8B319B04EC704FA595C754EF707D67CF1A)
   * 若选中一段代码，点击**Inline Chat（**或使用快捷键**Alt+I**，macOS中为**Command+I）**浮框，如未出现浮框，请参考如下操作启用。
     + 从26.0.0 Beta1版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie >****Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。
     + 从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Suggestion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Suggestion & Inline Chat**）中勾选**Show inline chat floating hints**启用浮窗。
     + 从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Completion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Completion & Inline Chat**）中勾选**Show Inline Chat tips**启用浮窗。
     + 在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在**File** > **Settings** > **CodeGenie** > **Code Generation**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Generation**）中取消勾选**Hide Inline Chat Overlay**选项。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/R8onjKByQHaOgKuXcGDfgA/zh-cn_image_0000002779407074.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=66C7CF790BA7DAFC10A18C4ADD9C8E538259B6E3B3B19A54738195050219AE92)
2. 选择在CodeGenie中已配置的三方模型，或者使用内置模型。三方模型配置具体请参考[模型（Model）配置](ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/v-NitzvzQFGyJuUrLhHb2w/zh-cn_image_0000002808766631.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=38755C1A49238C707243171819BE9DD92C2AB27B8B1BA600DBBAFB3F7D4D1747 "点击放大")
3. 在对话框中输入代码功能描述，点击发送或在键盘输入回车，等待代码生成；或在对话框中输入"/"，选择不同的快捷指令，进行代码文件分析或生成分析报告等。内置模型从26.0.0 Beta1版本开始，支持使用快捷指令。

   快捷指令的具体操作如下：
   * 未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/F7b29QC1S-e7gieRBoE_Ww/zh-cn_image_0000002779407070.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=37015340B66ACC6B6D0B8D10CDFEB55603A0B2286E6C741FDF46EC5396F99175)
   * 选中一段代码，在对话框中输入"/"，选择**Parameter Validation**（参数校验）、**Code Explanation**（代码注释）、**Code Optimization**（代码优化），可输入或不输入功能描述，在键盘输入回车或点击发送后等待生成，分析报告和参数校验等结果跟模型有关。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/21u6uA9rQVua-N4jIrf4dA/zh-cn_image_0000002779567052.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B1F7BAA663F64320E629A772CD8525E2F21E50377678016F3A76DBB875DFFF8 "点击放大")
4. 生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。
   * 绿色区域：新生成的代码内容。
   * 蓝色区域：对现有代码进行修改的内容。
   * 红色区域：删除的代码内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/RU-KSywHTfGq6u4OFPkFiA/zh-cn_image_0000002779407072.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B08CC1B4BC85C5EBA504DC966A639B8914124914FF1E59D76DB1F5A5E96F53EA)
   * 点击Inline Chat对话框中**Accept All**（或使用快捷键**Alt+Enter**），接受当前生成的全部内容；
   * 点击Inline Chat对话框中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dT5KprsoS3SHG6Dv7eYAvg/zh-cn_image_0000002808886711.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=27176DC3FB5630622193429AEC9404D9FCADA4EDE5908E58B0449A2428AC8F02)刷新按钮**/****Regenerate**，将根据当前描述重新生成代码片段；
   * 点击编辑区中**Accept**（或使用快捷键**Shift+Ctrl+Y**，macOS上为**Shift+Command+Y**），分段逐一接受并保留生成内容；
   * 点击编辑区中**Reject**（或使用快捷键**Shift+Ctrl+N**，macOS上为**Shift+Command+N**），分段逐一拒绝并删除当前生成内容；
   * 点击**Further Edit**（或使用快捷键**Ctrl+K**，macOS上为**Command+K**），重新进行输入，开始新一轮问答。
