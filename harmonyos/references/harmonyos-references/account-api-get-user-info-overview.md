---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-overview
title: 概述
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 获取用户信息 > 概述
category: harmonyos-references
scraped_at: 2026-04-28T08:16:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:262b911fcde29b7b3536bcb47fdeadf7af53c3b726b3811acf38b767909f77f2
---

华为账号为开发者提供了便捷的用户身份验证和用户信息获取能力，开发者可以通过Account Kit提供的相关能力，引导用户填写、管理相关信息完成授权，再获取凭证并调用华为账号服务器获取相关信息。

## 场景介绍

* **一键登录获取华为账号绑定号码和UnionID/OpenID**

  通过华为账号快速获取用户UnionID/OpenID和手机号；实现极简登录体验，**同时关联应用原有账号体系**，参见[一键登录获取华为账号绑定号码和UnionID/OpenID](account-api-get-user-info-quicklogin-by-code.md)。
* **获取华为账号用户信息-获取头像昵称**

  用户选择授权给应用特定的头像昵称后，应用服务器调用华为账号服务器快速完善个人信息，参见[获取华为账号用户信息-获取头像昵称](account-api-get-user-info-get-nickname-and-avatar.md)。
* **获取华为账号用户信息-获取手机号**

  用户选择授权给应用特定的手机号码后，应用服务器调用华为账号服务器快速完善个人信息，参见[获取华为账号用户信息-获取手机号](account-api-get-user-info-get-phone.md)。
* **获取用户风险等级**

  当应用登录后需要获取用户风险等级时，应用服务器调用华为账号服务器获取用户风险等级，参见[获取用户风险等级](account-api-getuserrisklevel.md)。
