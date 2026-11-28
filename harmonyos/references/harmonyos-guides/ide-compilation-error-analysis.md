---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-compilation-error-analysis
title: 编译报错智能分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 编译报错智能分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fbf2bb512c1e8623b81554139f44ef9285258937489e68af2d61b24a9c04c030
---

当DevEco Studio构建ArkTS工程出现失败时，CodeGenie仅能够对ArkTS语法相关的错误进行智能分析，提供错误原因及修复方案，帮助开发者快速解决编译构建问题。

在DevEco Studio 6.0.2 Beta1版本，编译报错修复的交互过程进一步优化，支持编辑区显示修改前后的差异点，以及开启自动编译验证。

从DevEco Studio 6.0.2 Release版本开始，编译报错智能修复能力使用的是HarmonyOS Act智能体。

从DevEco Studio 6.1.0 Beta2开始，不支持在编辑区点击Accept/Reject来接受/拒绝AI提供的修复方案；支持使用和切换模型。

## 操作步骤

1. 如需开启编译报错智能分析和自动修复，进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> CodeGenie****> General**页面，勾选**Enable AI** **auto-fix for build errors**和**Allow AI to modify local files for auto-fix**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/BSNOZ2qqTKqjAqvNhBdPMA/zh-cn_image_0000002808887089.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=65CBC687D11931224921CD75E12B618557C3DFAE9FAD2F85CD81733A689DFAE8)
2. 当ArkTS工程出现构建报错时，点击报错信息后方**Add To Chat**图标，CodeGenie将自动引用构建报错信息。

   开发者可在输入框中选择对当前报错修复任务进行补充指令，帮助开发者进行定制化修复，使修复更准确，如“当前工程为API 24工程，注意兼容性”等，点击或回车发送对话后，CodeGenie会分析该报错及开发者输入信息，并提供可能的错误原因，针对语法错误问题将参考开发者诉求，提供恰当的修复方案。

   若弹窗提醒"Please sign in to access DevEco CodeGenie"，请先登录CodeGenie后，再次点击**Add To Chat**图标查看解决方案。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/HBgG_SosTge9Y0ERUx4ziw/zh-cn_image_0000002808887085.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D00568A06681D881CE778E4BF94DB054AF6E23CA1B2487C989E9A1CBBEF6384 "点击放大")
3. CodeGenie提供的修复方案被自动应用到代码中。
   * DevEco Studio 6.1.0 Beta2之前版本：
     + 点击编辑区**Accept**（或使用快捷键**Ctrl+Shift+Y**），确认和接受AI提供的修复方案；点击**Reject**（或使用快捷键**Ctrl+Shift+N**）拒绝。
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/QX0qkGYlTmK0D4-Xm3zBfw/zh-cn_image_0000002808767005.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD8CD0BDC3DFB9E56D0AEC5F8D8F64C811BBBB243E319F130D82AF1FFC6558B0)可接受或拒绝该文件的修改。
   * DevEco Studio 6.1.0 Beta2及之后版本：
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/h7DCJwwCR6-x45isbb-f7A/zh-cn_image_0000002779407444.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=56F1182F39CA64CC1DDD168C7F23216336780A9A57D323F6A9CADD5DED75C8D2)可接受或拒绝该文件的修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/090kJ8ItSP6hC2HHna2_iA/zh-cn_image_0000002779567426.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=E27430D07E71E4134A8F4B678316342F9511073DAC31E3EF7651A1F4B38A927F "点击放大")
4. 点击**Run**编译验证，所需时间见提示，时间单位是秒。

   DevEco Studio 6.1.0 Beta2及之后版本，勾选对话问答结果中的**Auto Run**，或者Agent中**Auto Run**，开启自动编译验证开关。取消勾选Agent中**Auto Run**选项，关闭自动编译验证开关。

   DevEco Studio 6.1.0 Beta2之前版本，勾选对话问答结果中的**Automatically compile and verify without prompting**，或者**File** **>** **Settings****> CodeGenie >****General**中的**Allow AI to automatically run compilation verification during auto-fix**，开启自动编译验证开关。取消勾选**File** **>** **Settings****> CodeGenie >****Genera****l**中**Allow AI to automatically run compilation verification during auto-fix**选项，关闭自动编译验证开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/nH55R1sSTwOYugykgL-UBw/zh-cn_image_0000002808767001.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C246C06039B26AD2738E969CCAC17DC4E7D82AC8000205934C4632716BE1643)
