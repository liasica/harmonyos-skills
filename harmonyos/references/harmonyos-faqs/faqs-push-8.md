---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-8
title: 应用内通话消息是继承UIAbility还是VoIPExtensionAbility
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 应用内通话消息是继承UIAbility还是VoIPExtensionAbility
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3d2e7c061a0c23f28fa2206d9a610095314c79f3a7a49cd2bcac49d7c2711789
---

## 问题现象

推送VoIP消息，客户端未收到消息，自助分析平台反馈分析：是否有且仅有一个Ability配置了“action.ohos.push.listener”。

## 解决方案

[应用内通话消息](../harmonyos-guides/push-voip.md)的能力需要创建[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)负责处理应用内通话消息的主流程，而非[VoIPExtensionAbility](../harmonyos-references/push-voip-ability.md)。监听消息需要在此Ability中配置“action.ohos.push.listener”，应用有且只有一个Ability配置此Action。
