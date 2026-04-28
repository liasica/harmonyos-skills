---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation
title: 编辑区对话
breadcrumb: 指南 > 使用AI智能辅助编程 > 编辑区代码生成 > 编辑区对话
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95863e974964a30236aee4efc32bb3969bafd056835c5876464aeb0292117a53
---

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型进行生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

从DevEco Studio 6.1.0 Beta2版本开始，需要在设置中勾选Show Inline Chat tips开启编辑区Inline Chat浮窗。

1. 当前有以下两种方式唤醒Inline Chat对话框：
   * 若未选中代码片段，在代码编辑区域右键选择**CodeGenie > Inline Chat**（或使用快捷键**Alt+I**，macOS中为**Command+I**）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/C0ItHkd0R7GacQ7k2VlFRQ/zh-cn_image_0000002530753294.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=91A463FD5B2EA5C47F97BDC21B51067612D5D5EA67DA01248412407238D80D08)
   * 若选中一段代码，点击**Inline Chat（**或使用快捷键**Alt+I**，macOS中为**Command+I）**浮框。

     在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在**File** > **Settings** > **CodeGenie** > **Code Generation**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Generation**）中取消勾选**Hide Inline Chat Overlay**选项。

     从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在**File** > **Settings** > **CodeGenie > Code Completion** **& Inline Chat**（macOS中为**DevEco Studio** > **Prefe****rences/Settings** > **CodeGenie** > **Code Completion & Inline Chat**）中勾选**Show Inline Chat tips**启用浮窗。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/mTTMqxLFQ7uup8Ej1DclRA/zh-cn_image_0000002530913284.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=58A4A53754DA95A2B8B31B2CA0BE7AC221775B4BE2A578881D535623485763FE)
2. 选择在CodeGenie中已配置的三方模型，或者使用默认模型。三方模型配置具体请参考[模型（Model）配置](ide-agent-model.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/yRTBn4yoTUO5Mu6FHCf0iQ/zh-cn_image_0000002530753296.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=56FA6E89DF8F5E9B02DD08FBF47BB79ED2C31540F46F91359417E2F590E70E2F "点击放大")
3. 若选择默认模型，在对话框中输入所需要的代码功能描述，在键盘输入回车或点击发送，开始生成代码。点击**Stop Generation**，中断本轮代码生成过程。

   若选择三方模型，支持分析当前代码文件和生成分析报告，以及进行参数校验（**Parameter Validation**）、代码注释（**Code Explanation**）、代码优化（**Code Optimization**），分析报告和参数校验等结果跟模型有关，具体操作如下：
   * 未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/XHM17hdZRLmd1oXPbpMTiw/zh-cn_image_0000002561753231.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=CF05F1A9C4D77E2C60084E10726BAEFE93D6CEDF88BE7E9E2B4DF22B59198FAC)
   * 选中一段代码，在对话框中输入"/"，选择**Parameter Validation**/**Code Explanation**/**Code Optimization**，可输入或不输入所需的功能描述，在键盘输入回车或点击发送后开始生成。点击**Stop Generation**，中断本轮代码生成过程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/oEMHGlojRai8Rv34KqvOgw/zh-cn_image_0000002561833211.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=F1FEE93D76A936198A6457867589B37183255151109C66B8DFCA918B36377288)
4. 生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。
   * 绿色区域：新生成的代码内容。
   * 蓝色区域：对现有代码进行修改的内容。
   * 红色区域：删除的代码内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/oRZNpFlBQh6DCn1XNDuH-A/zh-cn_image_0000002530913290.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=623C368C72B0B8FC64CA43A6D803E041E9988714CABAB5405F797BCB8561682F)
   * 点击Inline Chat对话框中**Accept All**（或使用快捷键**Alt+Enter**），接受当前生成的全部内容；
   * 点击Inline Chat对话框中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/uL1CQhH2SwORTgHatuZJKg/zh-cn_image_0000002561833215.png?HW-CC-KV=V1&HW-CC-Date=20260427T235513Z&HW-CC-Expire=86400&HW-CC-Sign=D667205613EB3E2AE778566B576B2983A66009FC3CC3D6E116A51FD3C17A015F)刷新按钮**/****Regenerate**，将根据当前描述重新生成代码片段；
   * 点击编辑区中**Accept**（或使用快捷键**Shift+Ctrl+Y**，macOS上为**Shift+Command+Y**），分段逐一接受并保留生成内容；
   * 点击编辑区中**Reject**（或使用快捷键**Shift+Ctrl+N**，macOS上为**Shift+Command+N**），分段逐一拒绝并删除当前生成内容；
   * 点击**Further Edit**（或使用快捷键**Ctrl+K**，macOS上为**Command+K**），重新进行输入，开始新一轮问答。
