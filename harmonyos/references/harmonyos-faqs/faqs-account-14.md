---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-14
title: 应用内关闭未成年人模式，却引导关闭系统未成年人模式
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 应用内关闭未成年人模式，却引导关闭系统未成年人模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:b862662c79f1e3ac8eeffe236d84c371669f419e44fec55be6cee5259de62509
---

## 问题现象

系统已开启未成年人模式，打开某小说应用，进入未成年人模式“青少年专区”，点击应用内“退出青少年专区”，跳转引导关闭了系统的未成年人模式，预期应该是仅关闭该应用的未成年人模式。

## 背景知识

* [关闭系统的未成年人模式](../harmonyos-guides/account-system-turn-off-minorsprotection.md)：系统的未成年人模式已开启。用户打开应用，在应用内关闭系统未成年人模式。应用可调用系统的未成年人模式关闭接口[leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnonminorsmode)，验证家长密码后关闭系统的未成年人模式。
* [关闭应用的未成年人模式（推荐）](../harmonyos-guides/account-appself-turn-off-minorsprotection.md)：系统的未成年人模式已开启，用户打开应用，希望单独关闭应用的未成年人模式，系统的未成年人模式仍保持开启。当用户需要关闭应用的未成年人模式时，应用可调用系统家长身份验证接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)，验证通过后可关闭应用的未成年人模式。

## 问题定位

点击应用内“退出青少年专区”时，在日志中检索关键字MINORS，通过如下日志推断出应用调用了系统的未成年人模式关闭接口leadToTurnOffMinorsMode。

```shell
C05320/com.example.app/huaweiId_framework_base  com.example.app  I     TurnOff:389# TurnMinorsMode begin TurnOff
C05320/com.example.app/huaweiId_framework_base  com.example.app  I     CheckSupportMinorsMode:324# CheckPrivate ret:0, type:0
C05320/com.example.app/huaweiId_framework_base  com.example.app  I     TurnOff:415# TurnMinorsMode end TurnOff
```

## 分析结论

应用内关闭“青少年专区”，错误调用了关闭系统的未成年人模式的接口，正常场景应该是调用关闭应用的未成年人模式的接口。

## 修改建议

1. 关闭应用的未成年人模式为推荐方案，相较于关闭系统的未成年人模式，单独关闭应用的未成年人模式更为灵活，且较符合用户体验预期。当前场景需要开发者在应用侧记录单独关闭状态（示例：userTurnOffFlag，记录用户是否主动关闭了应用的未成年人模式），便于后续与系统重新联动。如应用重新启动时：
   * 当应用查询到userTurnOffFlag为True，应用需保持应用的未成年人模式为关闭状态。
   * 当应用查询到userTurnOffFlag为False，应用需与系统进行联动。
2. 建议开发者在选择这种接入方式的时候，在界面上告知用户，当前仅关闭应用的未成年人模式，但系统的未成年人模式仍保持开启，避免用户误解。
3. 关闭应用的未成年人模式参考：[开发步骤](../harmonyos-guides/account-appself-turn-off-minorsprotection.md#开发步骤)。
