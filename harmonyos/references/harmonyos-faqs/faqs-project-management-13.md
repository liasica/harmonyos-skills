---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-13
title: 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:11+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c952fcb292ce28e0d0adae8032a45845eec13fd7f147ea0a4a384a1a8b041371
---

**问题描述**

Mac启动DevEco Studio时，“DevEco Studio”意外退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/xw5amg6hRWmOGQHtEntGPA/zh-cn_image_0000002229758581.png?HW-CC-KV=V1&HW-CC-Date=20260429T062009Z&HW-CC-Expire=86400&HW-CC-Sign=A08D1B68B137C531DE3E55F4C55F4303DC17D19FCD14AA3594F5754250EEA22F)

**解决方案**

问题根因：异常修改了JetBrains启动脚本中的环境变量，导致Java虚拟机无法启动，DevEco Studio无法打开，弹窗显示错误。

规避措施：删除启动脚本 /Users/{USER\_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist，然后重启 Mac。
