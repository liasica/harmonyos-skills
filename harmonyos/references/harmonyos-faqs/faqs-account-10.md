---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-10
title: 华为账号一键登录后是否可以与应用自身账号体系解绑
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为账号一键登录后是否可以与应用自身账号体系解绑
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad07a0865013e78f9139547b72a18d60cefcdd684ab0c7fced4404a8fd8bdbb7
---

## 问题现象

应用集成[华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)，会通过获取到的手机号码等与应用自身账号体系进行绑定。一键登录账号绑定之后，是否可以再解绑呢？

## 解决方案

用户通过华为账号一键登录应用之后，开发者可以获取用户手机号，获取手机号后是否与应用自身账号体系进行绑定，是应用服务端自身实现逻辑，与华为账号一键登录没有关系，开发者可以自己控制账号绑定或解绑。
