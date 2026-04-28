---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-stability-basic-quality-test-2
title: 内存泄漏的定位日志为什么是乱码
breadcrumb: FAQ > DevEco Testing > 专项测试 > 稳定性基础质量测试 > 内存泄漏的定位日志为什么是乱码
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:400a39bb6a395d1ae2e7f142571757ce63dc76827030dd36b296fe6a482061dc
---

系统自动抓取的调用栈文件（memleak native --[process\_name]--[pid]--[timestamp].txt）无法直接在DevEco Studio中打开。需要将文件后缀名修改为.nas，然后使用DevEco Studio-Profiler-打开并分析。
