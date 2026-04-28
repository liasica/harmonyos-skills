---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-380
title: 应用冷启动时，trace中dlopen：libace_compatible.z.so耗时长的可能原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 应用冷启动时，trace中dlopen：libace_compatible.z.so耗时长的可能原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7da6176099fbeb007bace6db95cd4f3bb580015b78c68f2f0d8c7d2b28eec97
---

libace\_compatible.z.so为ArkUI引擎的核心动态库，加载该so耗时长为异常情况。

在常规场景下为低概率事件，但在系统资源紧张时可能高频发生，主要原因包括：CPU资源被抢占（如系统其他高优先级进程占用CPU）、锁冲突（如加载时与其他模块存在资源竞争）、系统低内存（导致动态链接库加载时需频繁换页）等。
