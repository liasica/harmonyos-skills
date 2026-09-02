---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-21
title: 两个华为账号登录获取的OpenID相同
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 两个华为账号登录获取的OpenID相同
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4f33ccdc623b45c75dd19485a37df022176da34bbca99f354851ffd9788699e5
---

## 问题现象

用户使用华为账号登录后发现应用内的信息是其他用户的。

## 背景知识

华为账号登录包括[使用“华为账号登录”按钮登录](../harmonyos-guides/account-unionid-login-button.md)和[使用自定义按钮登录](../harmonyos-guides/account-unionid-login-api.md)两种方式。华为账号登录成功后会返回Authorization Code给应用客户端，应用客户端将Authorization Code传到应用服务端，服务端通过Authorization Code获取到Access Token，再使用Access Token调用[解析凭证](../harmonyos-references/account-api-get-token-info.md)接口获取UnionID/OpenID/手机号码和其他用户信息。应用会将解析出来的OpenID当成华为账号的唯一ID与应用自己的用户关联。

## 问题定位

1. 根据开发者反馈的华为账号登录代码片段排查登录流程是否有误。
2. 查看提供的日志打印，对比返回的OpenID。发现两次返回的OpenID有一个字母的大小写是不同的。
3. 考虑到OpenID是[大小写敏感](../harmonyos-guides/account-faq-9.md#大小写敏感)的，建议开发者排查下是否做了大小写区分。

## 分析结论

经过排查后发现，数据存入到数据库时是做了大小写区分的，但是查询时没有做大小写区分，导致两个不同的手机号查询到了两个OpenID，从而导致登录到了同一个账号。

## 修改建议

开发者在数据库中新增、修改、查询OpenID时保留大小写格式。
