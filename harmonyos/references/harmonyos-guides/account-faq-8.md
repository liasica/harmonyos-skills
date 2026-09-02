---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-8
title: 无法获取到头像昵称如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 无法获取到头像昵称如何解决
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e90749e2840122144cda0400774c0c0b3245c304e760956a15fa07c81a758efe
---

1. 确认获取authorizationCode时，调用[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)接口是否传入正确的scope：'profile'。

   ```typescript
   import { authentication } from '@kit.AccountKit';

   // 创建授权请求，并设置参数
   const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   // 获取头像昵称需要传如下scope
   authRequest.scopes = ['profile'];
   // 若开发者需要进行服务端开发，则需传如下permission获取authorizationCode
   authRequest.permissions = ['serviceauthcode'];
   ```
2. 确认通过[AuthenticationController.executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)接口执行授权请求后，响应返回的Authorization Code在5分钟有效期内。
3. 确认调用的是华为账号服务器[获取头像昵称](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md)接口。
