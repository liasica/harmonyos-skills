---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0017
title: oh-package.json5模块配置编译报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > oh-package.json5模块配置编译报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:8967a601ff2c0ec42593985d5b4f906da3944c869200fd29c92098ee1334c22b
---

**Q：编译报错“The name of the 'xxx' module must be a string, but received a value of type 'xxx'.”。**

**A**：错误描述：模块名称必须是字符串类型。

可能原因：模块下oh-package.json5中配置的模块名name字段，配置值不是字符串类型。

解决措施：在模块的oh-package.json5文件中，将name字段的值修改为字符串类型。
