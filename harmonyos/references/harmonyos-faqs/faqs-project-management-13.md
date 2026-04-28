---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-13
title: 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ff04290f593dd29372fe11335f416158d5fe245b03e66b9421abd3478315af83
---

**问题描述**

Mac启动DevEco Studio时，“DevEco Studio”意外退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/xw5amg6hRWmOGQHtEntGPA/zh-cn_image_0000002229758581.png?HW-CC-KV=V1&HW-CC-Date=20260428T002857Z&HW-CC-Expire=86400&HW-CC-Sign=15E3971B43DC7D98B145CF86F2576C1E26F64205D4845AA8DC7BF57F78566B4E)

**解决方案**

问题根因：异常修改了JetBrains启动脚本中的环境变量，导致Java虚拟机无法启动，DevEco Studio无法打开，弹窗显示错误。

规避措施：删除启动脚本 /Users/{USER\_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist，然后重启 Mac。
