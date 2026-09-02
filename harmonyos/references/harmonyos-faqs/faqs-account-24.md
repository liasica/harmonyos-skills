---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-24
title: 使用华为账号登录，出口IP会有变化
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 使用华为账号登录，出口IP会有变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5539798f41b29e144ac7cb1e4e81feeb0c06ecfd4e54437b33669b8c197b30e7
---

## 问题现象

* **场景1：**华为账号服务器地址是多少？目前我们公司内网访问受限，无法访问外网地址，华为账号登录服务端调用API获取用户信息需要开通点对点策略。
* **场景2：**华为账号登录中，获取用户凭证和获取华为账号绑定号码的域名是不一样的吗？

## 背景知识

**Authorization Code**：授权码，用户使用华为账号登录成功之后，在客户端获取Authorization Code并传递给服务端。

[服务端开发](../harmonyos-guides/account-unionid-login-button.md#服务端开发)：应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证](../harmonyos-references/account-api-obtain-user-token.md#接口原型)接口向华为账号服务器请求获取Access Token、Refresh Token。

## 问题定位

开发者第一次通过IP地址访问华为账号服务器时正常，再次请求时提示“Name or Service not known”，猜测是因为华为账号服务器IP地址变化导致开发者网络之前配置的IP白名单失效。

## 分析结论

华为账号服务器域名关联的IP不是固定的，会存在后续变化的可能，无法提供固定的IP或者IP范围。

## 修改建议

网络白名单按照域名开通，华为账号域名如下：

* [oauth-login-drcn.platform.dbankcloud.com](http://oauth-login-drcn.platform.dbankcloud.com/)
* [hwid.platform.hicloud.com](http://hwid.platform.hicloud.com/)
* [hwid-drcn.platform.hicloud.com](http://hwid-drcn.platform.hicloud.com/)
* [oauth-login.platform.dbankcloud.com](http://oauth-login.platform.dbankcloud.com/)
* [api.cloud.huawei.com](http://api.cloud.huawei.com/)
