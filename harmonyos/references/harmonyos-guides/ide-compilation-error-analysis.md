---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-compilation-error-analysis
title: 编译报错智能分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 编译报错智能分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a3993ab3af232f2058f775ff431be45abb8d345411c8f76f060e5583b6c15771
---

当DevEco Studio构建ArkTS工程出现失败时，CodeGenie仅能够对ArkTS语法相关的错误进行智能分析，提供错误原因及修复方案，帮助开发者快速解决编译构建问题。

在DevEco Studio 6.0.2 Beta1版本，编译报错修复的交互过程进一步优化，支持编辑区显示修改前后的差异点，以及开启自动编译验证。

从DevEco Studio 6.0.2 Release版本开始，编译报错智能修复能力使用的是HarmonyOS Act智能体。

从DevEco Studio 6.1.0 Beta2开始，不支持在编辑区点击Accept/Reject来接受/拒绝AI提供的修复方案；支持使用和切换模型。

## 操作步骤

1. 如需开启编译报错智能分析和自动修复，进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> CodeGenie****> General**页面，勾选**Enable AI** **auto-fix for build errors**和**Allow AI to modify local files for auto-fix**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/zAPQELySQ7mNR-pQk9pl9g/zh-cn_image_0000002808887089.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF53F75073AF3020BD1688EEC001C301FB4132225F51DBC9456C996A2C434ADE)
2. 当ArkTS工程出现构建报错时，点击报错信息后方**Add To Chat**图标，CodeGenie将自动引用构建报错信息。

   开发者可在输入框中选择对当前报错修复任务进行补充指令，帮助开发者进行定制化修复，使修复更准确，如“当前工程为API 24工程，注意兼容性”等，点击或回车发送对话后，CodeGenie会分析该报错及开发者输入信息，并提供可能的错误原因，针对语法错误问题将参考开发者诉求，提供恰当的修复方案。

   若弹窗提醒"Please sign in to access DevEco CodeGenie"，请先登录CodeGenie后，再次点击**Add To Chat**图标查看解决方案。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/vfGYIszLQe2J7LJ11F60bA/zh-cn_image_0000002808887085.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F64E572169E8932C88808CF47C34607086535F3C1E0AC6E98547DF24801D6A9 "点击放大")
3. CodeGenie提供的修复方案被自动应用到代码中。
   * DevEco Studio 6.1.0 Beta2之前版本：
     + 点击编辑区**Accept**（或使用快捷键**Ctrl+Shift+Y**），确认和接受AI提供的修复方案；点击**Reject**（或使用快捷键**Ctrl+Shift+N**）拒绝。
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/jJ0nAzE0QGq69ObkdtvLOQ/zh-cn_image_0000002808767005.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDF9D6F399A76452DD3257329DB12DB699227BB0C9A3B6719465920258E3E09A)可接受或拒绝该文件的修改。
   * DevEco Studio 6.1.0 Beta2及之后版本：
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/wKktlNNkT5ik_K3c4kEufg/zh-cn_image_0000002779407444.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1B048D9CC387C1A6869311F89754B89B13A91C67B6B3DFACB9A0ED703E05D9F)可接受或拒绝该文件的修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Bthg1vdjQ5CUySWrqRxoEg/zh-cn_image_0000002779567426.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7F14F475D8A997DF252C94A58332D3F53EC4C7685D03FAE3D8D110CFCDFF074 "点击放大")
4. 点击**Run**编译验证，所需时间见提示，时间单位是秒。

   DevEco Studio 6.1.0 Beta2及之后版本，勾选对话问答结果中的**Auto Run**，或者Agent中**Auto Run**，开启自动编译验证开关。取消勾选Agent中**Auto Run**选项，关闭自动编译验证开关。

   DevEco Studio 6.1.0 Beta2之前版本，勾选对话问答结果中的**Automatically compile and verify without prompting**，或者**File** **>** **Settings****> CodeGenie >****General**中的**Allow AI to automatically run compilation verification during auto-fix**，开启自动编译验证开关。取消勾选**File** **>** **Settings****> CodeGenie >****Genera****l**中**Allow AI to automatically run compilation verification during auto-fix**选项，关闭自动编译验证开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/e5pDVmNTR-W0KU0dNO94gg/zh-cn_image_0000002808767001.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=19D097C6A7C1D2EABFCCBA2E4A3533FE50677A1198588F0E05A72C4674D7CAC1)
