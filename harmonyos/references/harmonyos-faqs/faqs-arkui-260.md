---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-260
title: 是否navigation有最大页面数量限制？router栈的栈最大是32个，超过32个是无响应还是报错
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 是否navigation有最大页面数量限制？router栈的栈最大是32个，超过32个是无响应还是报错
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e791eceeeaee6d3e12b13a1628a40d1a7ea2c33209bb11c697fda650d5dd4f2b
---

Navigation 本身没有最大页面数量的限制，但实际运行受系统router栈的限制。当 router 栈中的页面数量超过 32 个时，系统将不再响应，也不会再有新页面入栈。
