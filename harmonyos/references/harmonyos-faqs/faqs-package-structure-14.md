---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-14
title: 如何判断应用可被卸载
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何判断应用可被卸载
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:39c94276bb3bc994e1f84890524535777ea3fe4d313e6bfff21408a0b3f9e166
---

1. 使用bundleManager.getApplicationInfo获取应用程序信息。
2. ApplicationInfo具有removable属性，可用于判断应用是否可卸载。

**参考链接**

[ApplicationInfo](../harmonyos-references/js-apis-bundlemanager-applicationinfo.md)
