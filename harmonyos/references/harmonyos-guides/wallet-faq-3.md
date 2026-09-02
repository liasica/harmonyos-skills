---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-faq-3
title: Wallet Kit接口调用注意事项？
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > Wallet Kit常见问题 > Wallet Kit接口调用注意事项？
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0c340023c7a192a387e7c325ef262139a0909f481d36fc4bace2c1a7dd7bb56d
---

1. 请确保创建WalletPassClient时传入的context类型是否为UIAbilityContext，且为有效状态。Wallet Kit会使用调用方的context进行通信，如果context失效，则调用会失败。
2. 请确保调用Wallet Kit接口时应用处于前台，后台调用会被系统管控拦截，可能导致调用失败。
