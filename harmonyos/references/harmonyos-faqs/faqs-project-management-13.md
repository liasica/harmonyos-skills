---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-13
title: 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:11+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:043b4b7ef18f3bf65bce0c74805ceab1029bc2ea2421b0b90457596425fe36e0
---

**问题描述**

Mac启动DevEco Studio时，“DevEco Studio”意外退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/xw5amg6hRWmOGQHtEntGPA/zh-cn_image_0000002229758581.png)

**解决方案**

问题根因：异常修改了JetBrains启动脚本中的环境变量，导致Java虚拟机无法启动，DevEco Studio无法打开，弹窗显示错误。

规避措施：删除启动脚本 /Users/{USER\_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist，然后重启 Mac。
