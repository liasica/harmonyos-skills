---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-smart-fix
title: 修复编译报错
breadcrumb: 指南 > DevEco Code > DevEco Studio Plugin > 操作指南 > 修复编译报错
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:43+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:b28efb3f3b80725494731f2e0042d35086dcbcee985d3dffe71ba23f4fa0049d
---

应用工程构建过程中，如果出现ArkTS语法相关的编译报错，DevEco Code会提供AI自动修复（Smart Fix）能力。

点击报错信息后方**Add To Chat**，DevEco Code将自动引用构建报错信息。

开发者可在对话框中选择对当前报错修复任务补充指令，帮助开发者进行定制化修复，使修复更准确，如“当前工程为API 24工程，注意兼容性”等，按**Enter**或者点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/hdPVqk1VRSOoDD3_Y-fq_g/zh-cn_image_0000002776971160.png)发送，DevEco Code会分析该报错及开发者输入信息，并自动修复代码源文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/uSht3FYDT6qwHtDIihHnnA/zh-cn_image_0000002806073191.png)

如需关闭编译报错智能分析和自动修复功能，进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，取消勾选**Enable AI auto-fix for build errors**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/xSE4Gps_STmnENVWpL1eLQ/zh-cn_image_0000002776953470.png)
