---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-passwordless-auth-preparation
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-25T07:06:55+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:8edf11aab624239dc71bc5526d8ee8508082d9e99b1c07d41600a6b25dc4371c
---

## FIDO开发准备

开发者的业务需要接入符合FIDO UAF标准的协议，并部署符合FIDO UAF标准协议的FIDO服务端。FIDO网址：[FIDO官方网站](https://fidoalliance.org/) （见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## IFAA开发准备

开发者的业务需要接入IIFAA联盟，并接入IIFAA中心服务器。IIFAA网址：[IIFAA官方网站](https://www.iifaa.org.cn/technical#paper) （见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## SOTER开发准备

开发者的业务需要接入SOTER服务器。SOTER github：[SOTER开源项目](https://github.com/Tencent/soter)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## 通行密钥开发准备

* 仅当开发者使用FIDO2 C API开发时，需要申请如下通行密钥服务权限。在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。申请方式请参考：[申请受限权限](declare-permissions-in-acl.md)。

  | 应用能力 | 需要权限 |
  | --- | --- |
  | 通行密钥 | ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH |
* FIDO2协议基于应用的网址域名开通应用的通行密钥，开发者的应用需要关联网址域名，才可使用通行密钥服务。接入需完成四步：[开通App Linking服务](applinking-enable-applinking.md) > [建立域名与应用关联关系](app-linking-startupapp.md#建立域名与应用关联关系) > [在AGC为应用创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名) > [在module.json5中配置关联的网址域名](app-linking-startupapp.md#在modulejson5中配置关联的网址域名)。

## DID数字身份开发准备

* 开发者需要部署符合W3C DID协议的服务器。
* 开发者基于数字身份服务开发时，需要申请如下数字身份权限。在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。申请方式请参考：[申请受限权限](declare-permissions-in-acl.md)。

  | 应用能力 | 需要权限 |
  | --- | --- |
  | 数字身份 | ohos.permission.ACCESS\_DIGITAL\_IDENTITY |
