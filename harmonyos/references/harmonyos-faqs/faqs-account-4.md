---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-4
title: oauth-login.cloud.huawei.com域名ip不固定的原因
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > oauth-login.cloud.huawei.com域名ip不固定的原因
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b8790737d94ee3d8447e9a5348179d6b6339ce332bd454e4bfd9167ce404e924
---

## 问题现象

华为的oauth-login.cloud.huawei.com域名IP不固定的原因是什么？这个域名是CDN域名吗？

## 背景知识

该域名oauth-login.cloud.huawei.com是华为账号服务提供对外API接口的域名。具体参见：[基于OAuth 2.0开放鉴权](../HMSCore-Guides/open-platform-oauth-0000001053629189.md)。

## 解决方案

oauth-login.cloud.huawei.com域名的IP地址不固定，主要是因为该域名是通过CDN（Content Delivery Network，内容分发网络）服务来提供访问的。

由于CDN的分布式特性，当用户访问oauth-login.cloud.huawei.com时，用户请求将被路由至最近的CDN节点，因此IP地址是动态的而非固定不变。

## 常见FAQ

Q：如何使用该域名对应的IP配置白名单？

A：建议使用域名配置白名单，而非IP。
