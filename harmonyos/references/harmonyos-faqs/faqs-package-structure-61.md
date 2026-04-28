---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-61
title: 如何判断当前应用程序是Debug包还是Release包
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何判断当前应用程序是Debug包还是Release包
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3530eea5e91c381151816347dcc2906758c2214e8e4a2ed0162997e02ef4e678
---

在编译构建时，Hvigor会生成BuildProfile类，可以通过该类在运行时获取编译构建参数，BuildProfile.BUILD\_MODE\_NAME即为编译模式。编译模式为“debug”表示Debug包，“release”则表示Release包。

**参考链接**

[获取自定义编译参数-能力说明](../harmonyos-guides/ide-hvigor-get-build-profile-para-guide.md)
