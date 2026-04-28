---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-16
title: 如何持有wakelock锁，防止系统休眠
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何持有wakelock锁，防止系统休眠
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:22+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:da36334fbe513d20a3153bce5f9724ab3e9413698341a3d48f8916f87e834a2b
---

调用runningLock.create接口创建RunningLock锁。使用[hold()](../harmonyos-references/js-apis-runninglock.md#hold9)接口设置锁定持续时间，期间系统不会休眠。锁超时后，若未设置其他RunningLock，锁自动释放，系统进入休眠状态。

**参考链接**

[RunningLock锁](../harmonyos-references/js-apis-runninglock.md)
