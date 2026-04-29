---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-compilation-error-analysis
title: 编译报错智能分析
breadcrumb: 指南 > 使用AI智能辅助编程 > 编译报错智能分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9378819f6a21b0d4d476f65ecfa517e95a9c6111cb7eedae8ed84e68f7d4e68e
---

当DevEco Studio构建ArkTS工程出现失败时，CodeGenie仅能够对ArkTS语法相关的错误进行智能分析，提供错误原因及修复方案，帮助开发者快速解决编译构建问题。

在DevEco Studio 6.0.2 Beta1版本，编译报错修复的交互过程进一步优化，支持编辑区显示修改前后的差异点，以及开启自动编译验证。

从DevEco Studio 6.0.2 Release版本开始，编译报错智能修复能力使用的是HarmonyOS Act智能体。

从DevEco Studio 6.1.0 Beta2开始，不支持在编辑区点击Accept/Reject来接受/拒绝AI提供的修复方案；支持使用和切换模型。

## 操作步骤

1. 如需开启编译报错智能分析和自动修复，进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> CodeGenie****> General**页面，勾选**Enable AI** **auto-fix for build errors**和**Allow AI to modify local files for auto-fix**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/oumFigS9SOCTeRkjCHVR-Q/zh-cn_image_0000002530913422.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=BA482A2893FF3A996ED482532C2220DF4ED0FC5AF5168D29D90C6497A1C6A0E3)
2. 当ArkTS工程出现构建报错时，点击报错信息后方**Add To Chat**图标，CodeGenie将自动引用构建报错信息。

   开发者可在输入框中选择对当前报错修复任务进行补充指令，帮助开发者进行定制化修复，使修复更准确，如“当前工程为API 24工程，注意兼容性”等，点击或回车发送对话后，CodeGenie会分析该报错及开发者输入信息，并提供可能的错误原因，针对语法错误问题将参考开发者诉求，提供恰当的修复方案。

   若弹窗提醒"Please sign in to access DevEco CodeGenie"，请先登录CodeGenie后，再次点击**Add To Chat**图标查看解决方案。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/PLf8rCNhTuu0CbeZlFq0wg/zh-cn_image_0000002561753363.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=6C2764F7CB1A0FDF2660276066812BCE9D5F039436952B2F42B4AD4002831E77)
3. CodeGenie提供的修复方案被自动应用到代码中。
   * DevEco Studio 6.1.0 Beta2之前版本：
     + 点击编辑区**Accept**（或使用快捷键**Ctrl+Shift+Y**），确认和接受AI提供的修复方案；点击**Reject**（或使用快捷键**Ctrl+Shift+N**）拒绝。
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/QM1sXKxsT_2BDhdYcDU1Zg/zh-cn_image_0000002530753428.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=C287C37CD4D03BB9FA7F30C9CCED89B6F82977870DC247A096A3AC2BAAE2A9D3)可接受或拒绝该文件的修改。
   * DevEco Studio 6.1.0 Beta2及之后版本：
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/2TnzZzbBQaeO8v6tRgJjZQ/zh-cn_image_0000002530913420.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=672BDA1DD78006AE44FD4F7CFE8216776B713D646002F16BAA861D2F0933D5F1)可接受或拒绝该文件的修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/aaxzWl-GS5uTCFvaNLfomg/zh-cn_image_0000002530753426.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=B7D4BF1015E2434389695DBAE42EE7FD740799CEBDCEBDFEF94F8E3E160E7FBB)
4. 点击**Run**编译验证，所需时间见提示，时间单位是秒。

   DevEco Studio 6.1.0 Beta2及之后版本，勾选对话问答结果中的**Auto Run**，或者Agent中**Auto Run**，开启自动编译验证开关。取消勾选Agent中**Auto Run**选项，关闭自动编译验证开关。

   DevEco Studio 6.1.0 Beta2之前版本，勾选对话问答结果中的**Automatically compile and verify without prompting**，或者**File** **>** **Settings****> CodeGenie >****General**中的**Allow AI to automatically run compilation verification during auto-fix**，开启自动编译验证开关。取消勾选**File** **>** **Settings****> CodeGenie >****Genera****l**中**Allow AI to automatically run compilation verification during auto-fix**选项，关闭自动编译验证开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/C-lbXgAkRTivRlvRYcX36g/zh-cn_image_0000002561833345.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=9C478887A47F8628ED8CB09DDF72486DC7768210F506579E0C99C09291B2EAC7)
