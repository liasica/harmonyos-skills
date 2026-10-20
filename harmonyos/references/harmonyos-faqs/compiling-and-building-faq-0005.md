---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0005
title: Stage模型项目依赖FA模型编译报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > Stage模型项目依赖FA模型编译报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:f96e386028b660d9ae8a88afe62b73da36a3fa584848baa549c083458749314c
---

**Q：编译报错“This project is in the stage model and does not allow for dependencies of modules in the FA model.”时，可能的原因和解决措施是什么？**

**A**：错误描述：Stage模型项目不得依赖FA模型模块。可能原因：Stage模型的项目根目录下的build-profile.json5文件中，srcPath字段指定了 FA 模型的工程模块。解决措施：在项目根目录下的build-profile.json5文件中，移除对FA模型工程模块的引用。
