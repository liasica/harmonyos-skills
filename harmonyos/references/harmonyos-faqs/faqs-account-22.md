---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-22
title: 客户端获取的OpenID、UnionID和服务端获取的OpenID、UnionID有什么区别
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 客户端获取的OpenID、UnionID和服务端获取的OpenID、UnionID有什么区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:74c0b3c55e9286b8cd25e0404348a1d69465f61109eceea0dbf8730b970c8145
---

## 问题现象

应用使用自定义按钮实现华为账号登录，根据官网[业务流程](../harmonyos-guides/account-unionid-login-api.md#业务流程)介绍：UnionID、OpenID是通过在服务端解析Access Token获取后再传递给客户端。但是客户端调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest)方法执行登录请求后获取Authorization Code时也可以获取UnionID、OpenID。这两处获取的UnionID、OpenID有什么区别？

## 背景知识

UnionID是华为账号用户同一开发者账号下的唯一标识，开发者拥有多个应用获取同一个华为账号的UnionID是同一个；OpenID是华为账号用户在应用/元服务的唯一标识，同一个华为账号在不同应用获取的OpenID不同。[OpenID和UnionID的格式](../harmonyos-guides/account-faq-9.md)根据创建时间有所不同。

## 解决方案

1. 客户端通过executeRequest方法获取的UnionID、OpenID和服务端使用Access Token调用[解析凭证](../harmonyos-references/account-api-get-token-info.md)接口获取的UnionID、OpenID是分别相同的。
2. 使用场景不同：
   * 客户端获取UnionID、OpenID推荐应用没有服务端时使用。由客户端侧完成UnionID、OpenID的持久化和失效。失效后需要重新调用AuthenticationController对象的executeRequest重新获取。
   * 服务端获取UnionID、OpenID推荐应用有服务端时使用。UnionID、OpenID由服务端统一维护。可以复用Access Token的有效性，维护登录状态更简单。
