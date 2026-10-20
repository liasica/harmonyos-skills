---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0011
title: Stage模型与FA模型对象共享差异
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > Stage模型与FA模型对象共享差异
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:24+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:23a03fb2f05e3654063546f86a225d57c6dfd5ef873503a98b664d3ebd6a97e3
---

**Q：Stage模型与FA模型在进程内对象共享方面有哪些差异？**

**A**：差异如下：

* Stage模型中，多个应用组件共享同一个ArkTS引擎实例。应用组件之间可以方便地共享对象和状态，从而减少了复杂应用运行对内存的占用。
* FA模型中，每个应用组件独享一个ArkTS引擎实例。

Stage模型是主推的应用模型，开发者可以更方便地开发分布式场景下的复杂应用。

参考链接：[通过对比认识FA模型与Stage模型](../harmonyos-guides/stage-model-development-overview.md)。
