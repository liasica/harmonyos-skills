---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-glossary
title: Account Kit术语
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e098c47600d9c2b7e5dfd10814117e6f0e070b9898db85e3ca81e988ff04a14a
---

## A

### Access Token；访问凭证

访问被权限管控资源的凭证。可使用Access Token调用获取用户信息接口获取用户信息。

### Authorization Code；授权码

用户使用华为账号登录成功之后，可通过返回的凭据解析出授权码，通过授权码可获取Access Token、Refresh Token、ID Token等。

## G

### GroupUnionID；关联主体账号组维度用户标识符

华为账号用户在关联主体账号组内的唯一标识。不同开发者账号加入同一关联主体账号组后，其组内所有开发者的应用/元服务获取到用户的GroupUnionID相同。

## I

### ID Token；用户身份凭证

OIDC（[OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html)）相对于OAuth 2.0协议扩展的用户身份凭证，包含用户信息。用户使用华为账号登录成功后，可通过返回的凭据解析出ID Token等数据。

## O

### OpenID；应用维度用户标识符

华为账号用户在应用/元服务的唯一标识。不同应用/元服务（不管是否在同一个开发者账号下）获取到用户的OpenID不同，OpenID严格区分大小写。

## P

### permissions；数据或接口权限

用于判断应用是否有权限调用Account Kit接口或获取用户数据。

## R

### Refresh Token；刷新凭证

用于刷新用户级凭证Access Token的凭证。应用可通过定期刷新凭证信息避免接口调用中断。

## S

### scopes；应用需要访问的用户信息范围

scope列表，用于获取用户数据。开发者向华为账号服务申请不同类型用户数据的标识，比如头像昵称（profile）、匿名手机号（quickLoginAnonymousPhone）等。

## U

### UnionID；开发者维度用户标识符

华为账号用户同一开发者账号下的唯一标识。开发者有多个应用/元服务时，同一个开发者账号下的应用/元服务获取到用户的UnionID相同，UnionID严格区分大小写。

**说明** 

标识用户唯一性的应用/元服务必须是在同一个开发者账号下管理，一个应用/元服务转移到另外一个账号后，UnionID值也会变化。
