---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-smart-fix
title: 修复编译报错
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > 修复编译报错
category: harmonyos-guides
scraped_at: 2026-11-28T10:35:01+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:26475d8a34c1bcdba7277453e83b69797956d7bb7ac310ce20b28b9fcc242ed7
---

应用工程构建过程中，如果出现ArkTS语法相关的编译报错，DevEco Code会提供AI自动修复能力。

**Windows/macOS****版**

点击报错信息后方**Quick Fix**，DevEco Code将自动引用构建报错信息，并自动修复代码源文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/fQNET2KfSRSMEf02C6DM5w/zh-cn_image_0000002783483060.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=79C38D3AF2742B320C98FCA8EBD20A829246BD97318CE643D39F2E39A67D03DE "点击放大")

如需关闭编译报错智能分析和自动修复，进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> CodeGenie****> General**页面，取消勾选**Enable AI auto-fix for build errors**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/tWOgD48tQG6TDyxfGL5K-A/zh-cn_image_0000002779566948.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=B48FAE2273D1F95B46125D200786CAB11A59198A30A2C6047DF21DE51DD47FB6)

**鸿蒙电脑版**

选中需要分析的报错日志，鼠标右键选择**Add to DevEco Code**后，直接点击发，或鼠标右键选择**Add to DevEco Code**，并在对话框中补充需求描述后，点击发送，DevEco Code将分析构建报错信息，修复代码源文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/8CuTSBKHR0SERkN95k1p9g/zh-cn_image_0000002821941265.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF55318BEAF7C1875836E54D474937612AC7DC99E8236E90A17F23F729701C03 "点击放大")
