---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-93
title: Webview如何设置HTTP代理
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > Webview如何设置HTTP代理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81c7f48ca2c55f4424c3ffe62df2d80d0f6630eb4bb989ed19600c74f3bf8960
---

## 问题现象

如何给Webview设置HTTP代理？

## 解决方案

可以使用[connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)方法，设置应用级HTTP代理配置信息，此配置会作用到Web组件里的请求。
