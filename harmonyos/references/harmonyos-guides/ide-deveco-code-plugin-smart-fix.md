---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-smart-fix
title: 修复编译报错
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > 修复编译报错
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:51+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:ad7a169a9de9be7082f759cd9f413b825a1a7be4f2905c8f8f476dd24f02e4ae
---

应用工程构建过程中，如果出现ArkTS语法相关的编译报错，DevEco Code会提供AI自动修复能力。

**Windows/macOS****版**

点击报错信息后方**Quick Fix**，DevEco Code将自动引用构建报错信息，并自动修复代码源文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/3TVcz52YTPagQU-pgZ0u6A/zh-cn_image_0000002783483060.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=68E77056ADE193D0B7B7893967ADA8780C74DE6B09E797F13FEB54B8AD7E9666 "点击放大")

如需关闭编译报错智能分析和自动修复，进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，取消勾选**Enable AI auto-fix for build errors**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/C2-1rRXoQbaDBiHRZbNiZA/zh-cn_image_0000002779566948.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=D986880C0EA0071D6EFBBFAB0DE267F4D69FF820358764E2B7392EBE5B330BF9)

**鸿蒙电脑版**

选中需要分析的报错日志，鼠标右键选择**Add to DevEco Code**后，直接点击发，或鼠标右键选择**Add to DevEco Code**，并在对话框中补充需求描述后，点击发送，DevEco Code将分析构建报错信息，修复代码源文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/0Y2Et6IpRDetI8doLIMhkw/zh-cn_image_0000002821941265.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=54FAD9BEF48CFEB7C501E3F44084120B0890B520E8B9971E7D5FD425BA427893 "点击放大")
