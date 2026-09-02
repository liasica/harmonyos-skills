---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-14
title: module.json5配置文件中extensionAbilities和requestPermissions的权限声明有何区别
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > module.json5配置文件中extensionAbilities和requestPermissions的权限声明有何区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:37f4148b66290f8dd96e9bfa2fc40972c44b79b761810fb8b04a3922c826ddc3
---

* requestPermissions：标识当前应用运行时需向系统申请的权限集合。未在此配置的权限不会生效。
* extensionAbilities.permissions：标识当前ExtensionAbility组件自定义的权限信息。其他应用访问该 ExtensionAbility 时，需申请相应权限，仅用于权限校验。

## 参考链接

[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)
