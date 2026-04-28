---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-27
title: http请求执行的线程是否可控
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求执行的线程是否可控
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5a1901eb5530b5f40069edf7f8e7046a7fcd2283ff63928002255c7599794855
---

**问题现象**

三方应用发起http请求时，其执行任务的线程是否可控？

**解决措施**

应用每次发送请求时，底层系统会从线程池中获取一个线程来执行。线程的执行过程由底层系统管理，第三方应用可以监听相关事件以获取各阶段的数据。第三方应用可以控制请求的创建和销毁，但具体的执行过程不受控制。

**参考链接**

[@ohos.net.http (数据请求)](../harmonyos-references/js-apis-http.md)
