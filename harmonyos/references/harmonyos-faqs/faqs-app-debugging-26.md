---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-26
title: 如何使用DevEco Studio进行C/C++代码断点调试
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何使用DevEco Studio进行C/C++代码断点调试
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:93d1b54c83949de5b5db126e80a2d4dc08445ee6be0d547ca89d9756bed2b043
---

**问题现象**

在DevEco Studio上的C/C++代码处打断点，调试运行时断点不生效。

**可能原因**

DevEco Studio进行ArkTS/JS + Native混合调试时需要配置DevEco Studio的调试模式。

**解决措施**

选择配置项：Run/Debug Configurations > Debugger > Dual(ArkTS/JS + Native)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/bmpyspC2QIGmbhrao67yCA/zh-cn_image_0000002229604041.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=25B557308A4AF9CC4F9838A7C35E6FFAB1C87DCC36C3B599A174A853D8459AE1 "点击放大")
