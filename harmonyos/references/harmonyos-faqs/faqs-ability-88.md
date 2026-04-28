---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-88
title: app.json5文件与工程级build-profile.json5文件的区别
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > app.json5文件与工程级build-profile.json5文件的区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:75efab3f787c5d4eb71d7166e87143d96e1c364e8649f1b5f8a91423768531a1
---

使用场景和优先级存在差异。

* app.json5 文件用于定义应用的全局配置信息，包括 Bundle 名称、开发厂商和版本号等。如果在应用中使用 app.json5 文件进行全局配置，这些配置会被 build-profile.json5 文件中相同包名的配置覆盖。
* 工程级 build-profile.json5 文件主要用于定义构建和部署相关的配置，包括应用的包名、版本号等元数据。如果 app.json5 文件中定义了与 build-profile.json5 文件中相同的包名配置项，那么 build-profile.json5 文件中的配置项会覆盖 app.json5 文件中的配置项。

建议以工程级 build-profile.json5 文件中的配置为主。在构建和部署过程中，系统会优先使用工程级 build-profile.json5 文件中的配置信息。

**参考链接**

[app.json5配置文件标签](../harmonyos-guides/app-configuration-file.md#配置文件标签)
