---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-4
title: 如何设置升级策略
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 如何设置升级策略
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48f3063c1aa72c24681f2aefde8968c2d910446575b1fa1f85f6c0cd9f535f2a
---

## 问题现象

MDM应用中如何禁止用户主动去更新系统，其他的升级策略还有哪些。

## 背景知识

[systemManager.setOtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)：设置升级策略。此接口仅可在Stage模型下使用，并需要[ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM](../harmonyos-guides/permissions-for-mdm-apps.md#ohospermissionenterprise_manage_system)权限。

## 解决方案

MDM Kit提供了企业设备管理[systemManager.setOtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)接口可以设置升级策略，接口第二个参数policy为[OtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#otaupdatepolicy)类型，将OtaUpdatePolicy中的升级策略类型[PolicyType](../harmonyos-references/js-apis-enterprise-systemmanager.md#policytype)设置为PROHIBIT可实现禁止升级策略。

除了可设置禁止升级策略，还提供其他四种升级策略：

* 默认升级策略。周期提示用户，用户确认后升级。
* 强制升级策略。需指定最晚升级时间（latestUpdateTime）参数。
* 指定时间窗口升级策略。需指定时间窗口参数（installStartTime、installEndTime）。
* 延迟升级策略。延迟指定时间（delayUpdateTime）后进入DEFAULT模式，周期提示用户升级。

使用升级策略接口中，常见注意事项如下：

* 内网升级场景下，需要先调用[systemManager.notifyUpdatePackages](../harmonyos-references/js-apis-enterprise-systemmanager.md#systemmanagernotifyupdatepackages)接口通知系统更新包，再调用该接口设置升级策略。
* [OtaUpdatePolicy](../harmonyos-references/js-apis-enterprise-systemmanager.md#otaupdatepolicy)中的version参数是指待升级软件的版本号，并不是OS系统版本号。
