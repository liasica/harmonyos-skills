---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-22
title: 应用申请权限是否可以在子模块中申请
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 应用申请权限是否可以在子模块中申请
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4291a73da2c0b1193d323e35b99b7db0bc26bb66439888a486bfd933036a6295
---

## 问题现象

应用开发，采用分包架构，除了entry模块外，还有多个子模块，开发过程中，会按照业务模块、功能等将代码写到不同子模块中，当代码涉及权限申请时，权限在子模块的module.json5中申请，还是在entry模块的module.json5中申请？

## 解决方案

* 在子模块或者entry模块的module.json5中申请均可。
* 建议涉及权限的代码写在哪个子模块就在哪个子模块中申请，子模块中申请后，权限将在整个应用生效。这样方便子模块提供给其他工程使用，权限配置不会遗漏。
