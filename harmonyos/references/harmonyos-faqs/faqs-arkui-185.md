---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-185
title: 使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:51a2acebaf1c56f86fa6edbc8a598602682ac0d8d6338555dfbb58658329352b
---

@Watch用于快速计算，在UI重新渲染之前执行。不建议在@Watch函数中调用async和await，因为异步行为会延迟组件的重新渲染，可能导致性能问题。

**参考链接**

[@Watch装饰器：状态变量更改通知](../harmonyos-guides/arkts-watch.md)
