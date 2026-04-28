---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-21
title: 60180007 服务端通过Authorization Code无法获取到华为账号一键登录手机号如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 60180007 服务端通过Authorization Code无法获取到华为账号一键登录手机号如何解决
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e243c1520d2c96abe46f6ea04748e1526adf7c2e171aadc9bec37431214be78a
---

**问题现象**

调用服务器接口/oauth2/v6/quickLogin/getPhoneNumber时出现错误60180007，无法获取华为账号的一键登录手机号。

**可能原因**

调用服务器接口/oauth2/v6/quickLogin/getPhoneNumber的入参code，不是通过调用华为账号的一键登录组件获取到的。

**解决措施**

请参考[客户端开发](account-phone-unionid-login.md#客户端开发)的展示一键登录页面并获取Authorization Code，获取调用服务器接口/oauth2/v6/quickLogin/getPhoneNumber需要的入参code。
