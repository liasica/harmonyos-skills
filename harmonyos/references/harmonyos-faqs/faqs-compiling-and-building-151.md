---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-151
title: 编译报错“The name of the 'xxx' module must be a string, but received a value of type 'xxx'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The name of the 'xxx' module must be a string, but received a value of type 'xxx'.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6da22ede061a57ecd7de578a5ff1249c1b65d5123b2224c554eb8c2fdb1836d4
---

**错误描述**

模块名称必须是字符串类型。

**可能原因**

模块下oh-package.json5中配置的模块名name字段，配置值不是字符串类型。

**解决措施**

在模块的oh-package.json5文件中，将name字段的值修改为字符串类型。
