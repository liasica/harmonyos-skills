---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-compilation-error-analysis
title: 编译报错智能分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 编译报错智能分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5962bba61bdb2c73e8fd3232b75b61ebdf8f4433316d3b341432116040d144da
---

当DevEco Studio构建ArkTS工程出现失败时，CodeGenie仅能够对ArkTS语法相关的错误进行智能分析，提供错误原因及修复方案，帮助开发者快速解决编译构建问题。

在DevEco Studio 6.0.2 Beta1版本，编译报错修复的交互过程进一步优化，支持编辑区显示修改前后的差异点，以及开启自动编译验证。

从DevEco Studio 6.0.2 Release版本开始，编译报错智能修复能力使用的是HarmonyOS Act智能体。

从DevEco Studio 6.1.0 Beta2开始，不支持在编辑区点击Accept/Reject来接受/拒绝AI提供的修复方案；支持使用和切换模型。

## 操作步骤

1. 如需开启编译报错智能分析和自动修复，进入**File > Settings**（macOS为****DevEco Studio > Preferences/Settings****） **> CodeGenie****> General**页面，勾选**Enable AI** **auto-fix for build errors**和**Allow AI to modify local files for auto-fix**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/i3KZzaipT62NkJ-1AsJb1Q/zh-cn_image_0000002808887089.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=93CC48C708182626FA149C416DC25C5EEEEAC3D32E33DF5568C5987B76216B5C)
2. 当ArkTS工程出现构建报错时，点击报错信息后方**Add To Chat**图标，CodeGenie将自动引用构建报错信息。

   开发者可在输入框中选择对当前报错修复任务进行补充指令，帮助开发者进行定制化修复，使修复更准确，如“当前工程为API 24工程，注意兼容性”等，点击或回车发送对话后，CodeGenie会分析该报错及开发者输入信息，并提供可能的错误原因，针对语法错误问题将参考开发者诉求，提供恰当的修复方案。

   若弹窗提醒"Please sign in to access DevEco CodeGenie"，请先登录CodeGenie后，再次点击**Add To Chat**图标查看解决方案。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9HzrC0OkRSe733BazR8H0g/zh-cn_image_0000002808887085.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A9A9D6E26D754CE7CB6ECF5C8926CC4E6CDE2798CB2F75BFB409ABC6B32A56A "点击放大")
3. CodeGenie提供的修复方案被自动应用到代码中。
   * DevEco Studio 6.1.0 Beta2之前版本：
     + 点击编辑区**Accept**（或使用快捷键**Ctrl+Shift+Y**），确认和接受AI提供的修复方案；点击**Reject**（或使用快捷键**Ctrl+Shift+N**）拒绝。
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/1OsWsMFQS0C7mDaw0sxjmA/zh-cn_image_0000002808767005.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E625C904CA1E41BD579B80C00675AFFFA293FAFBF11805A202497BCCEDB644D)可接受或拒绝该文件的修改。
   * DevEco Studio 6.1.0 Beta2及之后版本：
     + 点击右侧对话框中的**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/ExsgOJ5RTea_uezaaewv0g/zh-cn_image_0000002779407444.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=067CB20372A9ADFAF13AFE76560E3E399CB5843F756784C13B99A9CF462441DC)可接受或拒绝该文件的修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/U-M52E7SRRGSA-KN_WNVmw/zh-cn_image_0000002779567426.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0AC9187E33FDD61BD1A647DF0D22BB353D34F66C7230211C0638D012D1C5CB3 "点击放大")
4. 点击**Run**编译验证，所需时间见提示，时间单位是秒。

   DevEco Studio 6.1.0 Beta2及之后版本，勾选对话问答结果中的**Auto Run**，或者Agent中**Auto Run**，开启自动编译验证开关。取消勾选Agent中**Auto Run**选项，关闭自动编译验证开关。

   DevEco Studio 6.1.0 Beta2之前版本，勾选对话问答结果中的**Automatically compile and verify without prompting**，或者**File** **>** **Settings****> CodeGenie >****General**中的**Allow AI to automatically run compilation verification during auto-fix**，开启自动编译验证开关。取消勾选**File** **>** **Settings****> CodeGenie >****Genera****l**中**Allow AI to automatically run compilation verification during auto-fix**选项，关闭自动编译验证开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/b7crJ7z8QPiiUmtDLm4e8Q/zh-cn_image_0000002808767001.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=619E4C6AD2BF3B3FDB81FC40316D3298FA2ECA861F85F232A5C639FB453F30A0)
