---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-4
title: 从包管理的角度，保证代码安全的措施有哪些
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 从包管理的角度，保证代码安全的措施有哪些
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b92a4eaea62303f1fad1bb433bb4bbcf9d21ea6316bb6d823cbe86592c8ec93d
---

* 编译：编译时，HAR和HSP支持代码混淆。
* 打包：打包时为每个HSP/HAP单独签名，签名后的应用才允许安装。
* 安装：终端设备上的应用市场用于安装和卸载应用，不支持其他安装方式。
* 运行时：提供应用沙箱机制，这是一种以安全防护为目的的隔离机制，防止数据遭受恶意路径穿越访问。

**参考链接**

[混淆加固](../harmonyos-guides/ide-build-obfuscation.md)，[Stage模型应用程序包结构](../harmonyos-guides/application-package-structure-stage.md)，[应用安装卸载与更新开发指导](../harmonyos-guides/application-package-install-uninstall.md)，[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)
