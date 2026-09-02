---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-token-overview
title: 概述
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 开放接口调用凭证 > 概述
category: harmonyos-references
scraped_at: 2026-09-02T14:53:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3974123dde090c0de1a369aaad994ebdeaef506cf40026539fec650e68a78d0a
---

在华为账号开放接口中，凭证是调用各类接口的核心鉴权凭据，贯穿身份认证、权限校验、数据安全等关键环节。

## 场景介绍

* **获取用户级凭证**

  应用通过用户登录、授权获取的授权码（Authorization Code），获取用户级凭证Access Token，然后通过该凭证Access Token访问账号受权限管控的接口（如[获取华为账号用户信息-获取头像昵称](account-api-get-user-info-get-nickname-and-avatar.md)、[获取用户风险等级](account-api-getuserrisklevel.md)等）。
* **刷新用户级凭证**

  提供用户级凭证Access Token主动刷新机制，应用可通过定期刷新凭证信息避免接口调用中断。
* **解析凭证**

  提供对凭证的解析能力，应用可通过该场景获取凭证携带的关键信息（如应用Client ID、用户身份、有效期）。
* **取消用户级凭证授权**

  当用户主动解除授权或应用需要终止服务时，可通过该场景立即废弃凭证。
* **获取应用级凭证**

  通过应用的Client ID和Client Secret获取应用级凭证Access Token，用于调用应用级权限管控接口（如[通过OpenID获取UnionID](account-api-get-unionid.md)）。
* **扫码授权**

  + **获取二维码信息**

    [扫码授权登录](../harmonyos-guides/account-authorize-by-qrcode.md)场景下，应用调用该接口获取二维码信息，然后生成二维码供用户扫码授权登录。
  + **获取用户级凭证**

    [扫码授权登录](../harmonyos-guides/account-authorize-by-qrcode.md)场景下，应用服务端通过设备码轮询该接口，获取Access Token、Refresh Token、ID Token。
