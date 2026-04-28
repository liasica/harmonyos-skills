---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-54
title: Native侧代码与ArkTS侧的代码线程关系以及线程使用限制
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > Native侧代码与ArkTS侧的代码线程关系以及线程使用限制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:57+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:37ca55bfce948cbdb7e3720cfe62b8d8df9aee0c16bd992a548a9ff22dfe5dab
---

**问题现象**

1. 主界面调用ArkTS接口到Native侧代码的加载是否都在一个线程里面？
2. Native侧支持的最大线程数分别是多少？

**解决措施**

应用侧调用的ArkTS接口代码与Native接口代码均运行在ArkTS主线程中。在Native侧用户可以提交任务到TaskPool线程池中，TaskPool内部会根据硬件条件、任务负载等情况动态调整线程数量，以确保高优先级任务的及时执行。
