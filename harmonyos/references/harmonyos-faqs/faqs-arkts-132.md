---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-132
title: 当前ArkTS是否采用类Node.js的异步I/O机制
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 当前ArkTS是否采用类Node.js的异步I/O机制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:aae638977e6f86b5aac82d458019b5cd904b8ae690b11ed60c35d20a37602b27
---

Node.js使用事件循环机制处理异步操作，支持回调函数和Promise。ArkTS使用基于协程的异步I/O机制，I/O事件分发到I/O线程，不阻塞JS线程，支持回调函数、Promise和async/await。
