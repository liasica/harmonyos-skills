---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-6
title: 设置域名过滤规则后未生效如何解决
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 设置域名过滤规则后未生效如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:17+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:b9a24451ed756460eba2607643af4348e2d69b9f043801e8e6f7db26d766a2a5
---

## 问题现象

使用接口[networkManager.addDomainFilterRule](../harmonyos-references/js-apis-enterprise-networkmanager.md#networkmanageradddomainfilterrule)添加过滤规则，设置白名单，调用networkManager.getDomainFilterRules发现设置白名单成功，但是实际去访问不在白名单的域名，仍然可以访问。

## 解决方案

1. 查看设备IP地址：为设备添加域名过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。
2. 清空缓存，确保不受缓存影响，特殊情况下可通过恢复出厂设置彻底清缓存。
3. 添加过滤规则时可以指定规则链，且支持使用IP段来做拦截，具体请参考[domainfilterrule](../harmonyos-references/js-apis-enterprise-networkmanager.md#domainfilterrule)。

**说明** 

升级到HarmonyOS 7.0.0 Beta1及以上版本后，调用接口设置域名防火墙时，系统会自动发起DNS清缓存，保证规则即时生效。
