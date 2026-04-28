---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-66
title: 如何通过C接口使用网络相关功能
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何通过C接口使用网络相关功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5800a25ae23c6e3691b9ad72ebc3d1a4e27ee308ff315659e1daa6bdc4e4297f
---

以下模块提供了C接口：自定义DNS解析、证书校验、WebSocket。

对于未直接提供C接口的模块，可以通过AKI机制调用ArkTS接口。

参考链接

[OHOS\_NetConn\_RegisterDnsResolver()](../harmonyos-references/capi-net-connection-h.md#ohos_netconn_registerdnsresolver)

[Netstack](../harmonyos-references/capi-netstack.md)

[使用WebSocket访问网络(C/C++)](../harmonyos-guides/native-websocket-guidelines.md)
