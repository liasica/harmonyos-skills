---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-useriam-get-auth-result
title: 如何感知指纹登录中间认证失败结果
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > User Authentication Kit常见问题 > 如何感知指纹登录中间认证失败结果
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:05+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:e222336a73fde449a7da295c476ff8b88581016bb1c761a48fee744127a5b998
---

## 问题现象

指纹验证错误5次后回调错误码12500003并锁定认证，导致无法精准判断是否达到5次错误以自动关闭指纹登录功能。

## 背景知识

* 提供用户认证能力，应用于设备解锁、支付、应用登录等场景。
* [start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口用于开始认证流程。此接口需要配置ohos.permission.ACCESS\_BIOMETRIC权限。
* [on('authTip')](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)接口可用于订阅[认证中间状态](../harmonyos-references/js-apis-useriam-userauth.md#userauthtipcode20)，例如认证失败、临时冻结（连续比对失败5次）。

## 解决方案

1. 在手机设置中录入个人指纹，完成指纹验证功能设置。
2. [申请权限](prerequisites.md#申请权限)：ohos.permission.ACCESS\_BIOMETRIC。
3. [查询认证能力是否支持](obtain-supported-authentication-capabilities.md#开发步骤)，需要根据[错误码](../harmonyos-references/errorcode-useriam.md)的不同，给予用户不同的提示。
4. 订阅认证[中间状态](../harmonyos-references/js-apis-useriam-userauth.md#onauthtip20)和[认证结果](../harmonyos-references/js-apis-useriam-userauth.md#onresult10-1)，并开始认证，根据返回的中间状态和结果进行对应处理。
