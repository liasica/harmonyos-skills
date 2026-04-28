---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-105
title: 滑动的页面软键盘挡住内容不能向上滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 滑动的页面软键盘挡住内容不能向上滑动
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:169b5ae1d9373a0e3d3a46075c6cf1d7f5ffa6d7d42dc667658ee249551d3921
---

计算软键盘的高度，然后将整体的margin-bottom设置为软键盘的高度。软键盘消失时，将margin-bottom设置为 0。软键盘高度可通过监听软键盘的显示事件获取。

**参考链接**

[输入法框架](../harmonyos-references/js-apis-inputmethod.md)
