---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-62
title: Hilog模块提供的OH_LOG_SetCallback接口返回的日志与系统落盘的Hilog日志是否一致
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > Hilog模块提供的OH_LOG_SetCallback接口返回的日志与系统落盘的Hilog日志是否一致
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:edc25aa0405d4f61ae9ae6997b044f530ffe92bd85b2a66fcecabe0c5d3bb3ce
---

Hilog模块提供的OH\_LOG\_SetCallback接口返回的是该应用运行进程内打印的符合日志输出级别的全部日志，返回的日志不受系统超限机制管控。

系统落盘的Hilog日志是当前系统全部进程的符合日志输出级别的日志，包括应用通过OH\_LOG\_SetCallback接口监听的该应用运行进程内的日志。落盘的日志受系统超限机制管控，超限后的日志无法输出保存。

基于上述原因，针对该应用运行进程内的日志，OH\_LOG\_SetCallback返回的日志数量应该大于等于落盘中的应用日志数量。
