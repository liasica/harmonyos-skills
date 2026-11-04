---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-smart-fix
title: 修复编译报错
breadcrumb: 指南 > DevEco Code > DevEco Studio Plugin > 操作指南 > 修复编译报错
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:55+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:cdd36b1cc18ba897ea3ee083da00c88282f2f22218711b05ecab588b61777c06
---

应用工程构建过程中，如果出现ArkTS语法相关的编译报错，DevEco Code会提供AI自动修复（Smart Fix）能力。

点击报错信息后方**Add To Chat**，DevEco Code将自动引用构建报错信息。

开发者可在对话框中选择对当前报错修复任务补充指令，帮助开发者进行定制化修复，使修复更准确，如“当前工程为API 24工程，注意兼容性”等，按**Enter**或者点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/ijvK49ZIQ4-yM5P0Ng1qpw/zh-cn_image_0000002776971160.png)发送，DevEco Code会分析该报错及开发者输入信息，并自动修复代码源文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/LHQNV07KRWWEuvJCThQ8nw/zh-cn_image_0000002806073191.png)

如需关闭编译报错智能分析和自动修复功能，进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，取消勾选**Enable AI auto-fix for build errors**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/fWw7wIY2RBe_R7WBM6E_JA/zh-cn_image_0000002776953470.png)
