---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-13
title: 如何解决mac启动DevEco Studio报错提示“devecostudio”意外退出问题
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决mac启动DevEco Studio报错提示“devecostudio”意外退出问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:253925c1f50079b224991a3681bfb0d9fc9fc1f1886fd01f2ee5150948bd95ba
---

**问题描述**

Mac启动DevEco Studio时，“DevEco Studio”意外退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/h1RKsZdxSKuXeQhWnRtESA/zh-cn_image_0000002654797799.png)

**解决方案**

问题根因：异常修改了JetBrains启动脚本中的环境变量，导致Java虚拟机无法启动，DevEco Studio无法打开，弹窗显示错误。

规避措施：删除启动脚本 /Users/{USER\_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist，然后重启 Mac。
