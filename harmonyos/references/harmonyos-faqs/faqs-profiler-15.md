---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-15
title: 录制Snapshot模板时，看不到taskPool线程内存信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > 录制Snapshot模板时，看不到taskPool线程内存信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:15+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8500af628c47ece85ef41b810cf8abb398eedf6f8da0865f4f8e0a98a3128b09
---

**问题现象**

录制Snapshot模板时，无法看到taskPool线程的内存信息。

**可能原因**

Snapshot模板只支持dump主线程的虚拟机堆内存。

**解决措施**

可使用hidumper --mem-jsheap ${pid} -T ${tid}获取指定进程指定JS线程的虚拟机堆内存，文件生成后导入Profiler查看。详细信息参考[查询虚拟机堆内存](../harmonyos-guides/hidumper.md#查询虚拟机堆内存)。
