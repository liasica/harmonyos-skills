---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-2
title: 导入历史数据失败
breadcrumb: FAQ > DevEco Studio > 性能分析 > 导入历史数据失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e02992e6be3c59860c7950d4c173eed44e4255a782d078762018e76570d0d854
---

**问题现象**

使用其他版本的DevEco Studio导出的Profiler深度分析任务文件（.insight 文件）时，可能会遇到异常。

* 导入失败
* 导入后不显示泳道
* 导入后无数据

**解决措施**

请使用与导出文件时相同版本的DevEco Studio重新操作。

如果无法从导出方确认DevEco Studio的版本号，可以通过查看.insight文件中的manifest.json目录下的devEcoStudioBuildVersion字段来确认版本号信息。

说明

.insight文件可以使用常用解压软件打开并查看。
