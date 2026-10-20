---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0002
title: 调试时出现安装错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 调试时出现安装错误
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:17+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:faedc1e6f9f0605da45200bd820e65eab2679648726c2dd382d6d8f9e1a58553
---

**Q：使用发布证书进行调试时出现安装错误：Install Failed: error: failed to install bundle.如何解决？**

A：应用市场发布的证书无法通过非应用市场渠道安装。 若要测试发布证书应用，可以参考以下2种方式：

* API ≤ 9 的应用请使用[开放式测试](../AppGallery-connect-Guides/agc-betatest-introduction-0000001071477284.md)。
* API ≥ 10的应用请使用[邀请测试和公开测试](../app/agc-help-harmonyos-testapp-0000001873653977.md)。
