---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-269
title: TextInput的visibility属性设置为Hidden或者None之后是否可获焦
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > TextInput的visibility属性设置为Hidden或者None之后是否可获焦
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f34a17e1cfcfdf8067d71f7ae8a0a62e78caedbf4746ffaf348a8487970f6c1d
---

设置visibility属性为Hidden后，仍占据布局空间但组件会从页面中消失，因此无法获得焦点。可以通过将textInput的opacity属性设置为0来隐藏组件，不改变布局特性的同时不影响焦点的获取。
