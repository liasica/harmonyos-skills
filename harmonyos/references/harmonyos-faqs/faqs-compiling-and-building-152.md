---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-152
title: 编译报错“The version number of the module must be a string, but received a xxx.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The version number of the module must be a string, but received a xxx.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:34bdd03816727552ef9cf08e5698cb56dee104db6ea1f1915e5fe579d398dd57
---

**错误描述**

模块版本号必须为字符串类型。

**可能原因**

模块下的oh-package.json5文件中，version字段的配置值必须为字符串类型。

**解决措施**

在模块的oh-package.json5文件中，将version字段的值修改为字符串类型。
