---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-17
title: 华为账号一键登录是否有第三方隐私政策链接
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为账号一键登录是否有第三方隐私政策链接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:844a3074121d7d8cdf816367ee0a0ea5327450acb010307176ec0b6e2a650fb2
---

## 问题现象

华为账号一键登录是使用AccountKit完成的，这个属于SDK吗，有第三方隐私政策链接吗？

## 解决方案

华为账号一键登录属于SDK，隐私政策要求所有使用华为账号一键登录功能的应用必须满足华为账号一键登录的[约束与限制](../harmonyos-guides/account-phone-unionid-login.md#约束与限制)，其中有《华为账号用户认证协议》接入说明。需在登录页面提供该协议链接，用户点击后跳转至华为官方页面，此链接为华为统一提供的隐私政策页面，非第三方链接。应用若需额外接入其他协议（如用户协议、隐私协议），可自行补充展示，但不得替代该强制协议。
