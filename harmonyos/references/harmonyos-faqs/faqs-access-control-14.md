---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-14
title: module.json5配置文件中extensionAbilities和requestPermissions的权限声明有何区别
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > module.json5配置文件中extensionAbilities和requestPermissions的权限声明有何区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ebf4284aac6c9a2b8c652fc83c0e7e7141154a976919b2233167f12d0e34805e
---

* requestPermissions：标识当前应用运行时需向系统申请的权限集合。未在此配置的权限不会生效。
* extensionAbilities.permissions：标识当前ExtensionAbility组件自定义的权限信息。其他应用访问该 ExtensionAbility 时，需申请相应权限，仅用于权限校验。

**参考链接**

[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)
