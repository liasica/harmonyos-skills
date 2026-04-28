---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-42
title: 如果在ArkTS中大部分后台任务（计算、埋点、数据存储）都使用异步并发的方式，是否会使主线程响应变慢，引起卡顿掉帧问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如果在ArkTS中大部分后台任务（计算、埋点、数据存储）都使用异步并发的方式，是否会使主线程响应变慢，引起卡顿掉帧问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:24+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:38125866cd1b97156c92b091fdec1ccdcecf3c294db5e972ac110bf978a0d9fb
---

在ArkTS层接口中，如果异步操作不涉及I/O操作，异步任务将在主线程的微任务执行时机触发，仍然会占用主线程。建议使用TaskPool，将任务分发到后台任务池中执行。
