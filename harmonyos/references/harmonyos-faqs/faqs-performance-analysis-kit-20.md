---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-20
title: 如何线上分析应用在CPU占用情况
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何线上分析应用在CPU占用情况
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:66ef7cbaef9dd75d711b1b5d39e153d7afb8ed1ede2fb82f3ba0bf3ac7457e6e
---

应用在发生卡顿、丢帧或评估运行状态时，可以通过hidebug接口获取资源数据，检测当前的运行状态。

利用[@ohos.hidebug](../harmonyos-references/js-apis-hidebug.md)可以获取应用内存的使用情况，包括应用进程的静态堆内存（native heap）信息、应用进程内存占用PSS（Proportional Set Size）信息等；可以完成虚拟机内存切片导出、虚拟机CPU Profiling采集等操作。
