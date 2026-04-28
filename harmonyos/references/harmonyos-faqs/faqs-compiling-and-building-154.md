---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-154
title: 编译报错“This project is in the stage model and does not allow for dependencies of modules in the FA model.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“This project is in the stage model and does not allow for dependencies of modules in the FA model.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0de490bd5702b45e735ab2a2465e31a009232f8281c46f23a12ecf9ebbfbcd8c
---

**错误描述**

Stage模型项目不得依赖FA模型模块。

**可能原因**

Stage模型的项目根目录下的build-profile.json5文件中，srcPath字段指定了 FA 模型的工程模块。

**解决措施**

在项目根目录下的build-profile.json5文件中，移除对FA模型工程模块的引用。
