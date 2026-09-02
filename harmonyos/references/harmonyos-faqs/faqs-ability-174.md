---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-174
title: 三方应用无页面常驻后台进程的实现方式
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 三方应用无页面常驻后台进程的实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:6c8ca6696ca8364019b00b5418ef1737eadd994292639e3eaa66bd118a760ce2
---

## 问题现象

在HarmonyOS中，三方应用是否只能创建带前台页面的应用，无法创建不带页面的常驻后台进程？

## 解决方案

三方应用当前无法创建完全无前台页面的纯后台应用。如果业务场景需要后台服务能力，建议在拥有前台UI的基础上合理使用后台任务机制来实现需求。从API version 20开始，支持开发者使用[AppServiceExtensionAbility](../harmonyos-guides/app-service-extension-ability.md)组件，为应用提供后台服务能力，其他三方应用可通过启动或连接该组件获取相应的服务。
