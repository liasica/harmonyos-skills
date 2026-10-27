---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0009
title: 应用Debug与Release包判断常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 应用Debug与Release包判断常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7fc37afec561d7d3e8b121c5d7db5fa67cb4dc95b6cf29d0f2de647fa816511b
---

**Q：如何判断当前应用程序是Debug包还是Release包？**

**A**：在编译构建时，Hvigor会生成BuildProfile类，可以通过该类在运行时获取编译构建参数，BuildProfile.BUILD\_MODE\_NAME即为编译模式。编译模式为“debug”表示Debug包，“release”则表示Release包。

参考链接：[获取自定义编译参数-能力说明](../harmonyos-guides/ide-hvigor-get-build-profile-para-guide.md)。
