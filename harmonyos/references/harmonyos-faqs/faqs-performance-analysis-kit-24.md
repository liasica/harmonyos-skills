---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-24
title: console.log和hilog的区别，如何选择使用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > console.log和hilog的区别，如何选择使用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6d991cd898804c0a524fa1ce0fd99e79c2cad5ef0d2b6ebcea5d6d9bb1c2ecd7
---

* console.log是对hilog日志系统的封装，采用默认参数。日志业务领域为A0c0d0，日志TAG为JSApp，日志级别为info。
* hilog日志打印时包含四部分：日志业务领域、日志TAG、日志级别和日志内容。开发者可以自定义设置日志业务领域、日志TAG和日志级别。
* console主要用于应用开发的调试阶段。
* 推荐使用hilog对日志系统进行分类和统一处理。使用console.log打印日志，不方便日志定位。

**参考链接**

[Hilog](../harmonyos-references/capi-hilog.md)
