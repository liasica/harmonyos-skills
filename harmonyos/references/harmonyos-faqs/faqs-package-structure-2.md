---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-2
title: HSP打包后，为什么会生成HAR包，它是否会导致App包大小膨胀
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HSP打包后，为什么会生成HAR包，它是否会导致App包大小膨胀
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6db90873ff87a30525b9007b23d6c4973a6be4cc5aa767bb27238537a00a5f8e
---

HSP编译生成的HAR包仅包含配置文件和接口定义，不包含代码逻辑。该HAR包仅用于开发阶段，不会影响App包的大小。
