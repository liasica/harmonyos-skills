---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-38
title: HAR包是否支持依赖传递
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR包是否支持依赖传递
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eca315aa6b21fce9fe6c3a6aa16331d5d8d096aaa1967453cd8422a8f5942329
---

**问题现象**

例如，有三个HAR分别为A、B、C，A依赖B，B依赖C。A可以直接引用C的资源。

**解决措施**

A不能直接引用C的资源。A需直接依赖C，才能进行引用。
