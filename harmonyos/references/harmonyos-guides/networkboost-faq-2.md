---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-faq-2
title: 如果使用多网并发能力超过剩余配额限制，会发生什么
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > Network Boost Kit常见问题 > 如果使用多网并发能力超过剩余配额限制，会发生什么
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:02+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a6f75407a11654f7176ddbf7712612791ddd6877c24050ec2829648c5d9df1ea
---

配额（次数或时长）耗尽会限制使用，多网会自动释放，应用可以在[netHandover.on('multiPathStateChange')](../harmonyos-references/networkboost-nethandover.md#nethandoveronmultipathstatechange)中监听到多网退出回调。如果此时再请求多网会抛出错误码，应用可以在[netHandover.requestMultiPath()](../harmonyos-references/networkboost-nethandover.md#nethandoverrequestmultipath)的错误码中判断错误类型。应用配额以24小时的周期进行刷新。
