---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0001
title: console.log与hilog区别及使用选择常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > console.log与hilog区别及使用选择常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:34+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:2ff0079ffc8a6aaa9e3aa5a6d0e2d75ada8605fa64ab05e7312d77c29a84bc42
---

**Q：console.log和hilog的区别是什么，如何选择使用？**

A：console.log和hilog的区别及使用选择说明如下：

* console.log是对hilog日志系统的封装，采用默认参数。日志业务领域为A0c0d0，日志TAG为JSApp，日志级别为info。
* hilog日志打印时包含四部分：日志业务领域、日志TAG、日志级别和日志内容。开发者可以自定义设置日志业务领域、日志TAG和日志级别。
* console主要用于应用开发的调试阶段。
* 推荐使用hilog对日志系统进行分类和统一处理。使用console.log打印日志，不方便日志定位。

参考链接：[Hilog](../harmonyos-references/capi-hilog.md)。
