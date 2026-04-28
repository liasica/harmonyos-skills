---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-5
title: 如何理解App、HAP、HAR、HSP的关系
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何理解App、HAP、HAR、HSP的关系
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:994896d2eb599780549189e3e34a1ac51e224c3a6b45d772c258177dd6e18f68
---

* App是发布到应用市场的基本单元，不能直接在设备上安装和运行。
* HAP（Harmony Ability Package）是应用安装和运行的基本单元，包含代码、资源、第三方库及配置文件等，主要分为entry和feature两种类型。
* HAR（Harmony Archive）是静态共享包，包含代码、C++库、资源和配置文件。HAR支持多个模块或工程共享ArkUI组件和相关代码。
* HSP（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，用于实现代码和资源的共享。HSP跟随宿主应用的App包一起发布，与宿主应用同进程，具有相同的包名和生命周期。
