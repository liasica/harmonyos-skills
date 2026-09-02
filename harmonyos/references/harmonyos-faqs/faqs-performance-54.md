---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-54
title: 如何获取应用性能监控数据
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 如何获取应用性能监控数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:5c452f530317a8c700cf24889e329b7d9985c3b3fb440d7d0cfeff8254a33ad3
---

## 问题现象

场景一：应用的性能监控平台中，HarmonyOS如何收集应用的内存占用率和CPU使用率？

场景二：HarmonyOS如何获取磁盘平均每秒读字节数信息？

## 解决方案

场景一：

可以使用IDE的调优工具DevEco Profiler来监控应用的CPU、内存、帧率等数据，参考文档如下：[DevEco Profiler性能调优概述](../harmonyos-guides/ide-insight-description.md)，如果想通过API获取相关信息，可以参考如下接口文档：[Debug调试](../harmonyos-references/js-apis-hidebug.md)。

场景二：

可以使用[diskio plugin插件](../harmonyos-guides/hiprofiler.md#diskio-plugin插件)获取整机磁盘I/O使用率的相关信息。
