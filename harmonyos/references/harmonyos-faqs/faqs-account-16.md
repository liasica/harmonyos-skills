---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-16
title: 仅支持三方用户账号登录的应用如何对接华为一键登录
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 仅支持三方用户账号登录的应用如何对接华为一键登录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:58e301bb10dcc28ba375705b2a4f4912e80aed3059e54f917166948c72013d59
---

## 问题现象

应用不提供用户注册功能，使用三方账户授权方式登录，当前接入华为账号如何与已有用户体系关联。

## 解决方案

* 华为账号一键登录功能本身不需要用户在应用中进行账号注册。如果用户已经在手机上（设置）中登录了华为账号，那么在应用中直接一键登录即可获取用户的登录信息。如果用户未在手机上登录华为账号（或未注册），可以引导用户注册或登录华为账号。
* 华为一键登录与已有用户体系关联参照以下步骤：
  1. 申请[华为账号一键登录权限](../harmonyos-guides/account-config-permissions.md)。
  2. 接入[华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)。
  3. 前端登录成功后获取匿名手机号和Authorization Code，同时将Authorization Code传到服务端，在服务端通过[/oauth2/v6/quickLogin/getPhoneNumber接口](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md)获取完整手机号码和[unionId](../harmonyos-guides/account-phone-unionid-login.md)。
  4. 通过手机号码和[unionId](../harmonyos-guides/account-phone-unionid-login.md)与已有用户匹配，匹配分为以下三种场景：
     + 场景一：手机号码匹配成功（并且[unionId](../harmonyos-guides/account-phone-unionid-login.md)为空），则用户是存量用户，客户端提示用户确认绑定，并且在服务端将完成用户和[unionId](../harmonyos-guides/account-phone-unionid-login.md)的绑定。
     + 场景二：通过手机号码没有匹配到存量用户，创建新用户并且将用户账号绑定[unionId](../harmonyos-guides/account-phone-unionid-login.md)。
     + 场景三：手机号匹配失败，[unionId](../harmonyos-guides/account-phone-unionid-login.md)匹配成功，则需要提示用户手机号码已变更，通过客户端提示用户是否变更手机号。
  5. 如果通过华为账号获取用户手机号码为空则需增加用户手机号录入功能，获取手机号码后走步骤4。
