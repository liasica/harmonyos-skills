---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-15
title: 如何获取应用级别的temp路径和files路径
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取应用级别的temp路径和files路径
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:09d6303bcb56978b6a837e97f31e8efa2afbadcc2db2d79b6b490e41d5304ba0
---

通过上下文 context 获取。例如：

* temp路径：通过 this.context.getApplicationContext().tempDir 获取。
* 文件路径：可通过 this.context.getApplicationContext().filesDir 获取。

**参考链接**

[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)
