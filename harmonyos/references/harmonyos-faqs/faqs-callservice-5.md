---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-callservice-5
title: 通话服务中callId是否可以自定义，需要保持一致吗
breadcrumb: FAQ > 应用服务开发 > VoIP通话服务（Call Service Kit） > 通话服务中callId是否可以自定义，需要保持一致吗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:a8182cfd99a7aa06c4af102a6384f0cdb6e8f177f28822d08b70ed5f5c00487b
---

## 问题现象

Call Service Kit拉起通知栏需要callId，callId是否可以自定义？服务端下发的callId数据由华为服务端返回，使用自定义callId进行通知栏拉起操作。来电消息传递失败要上报error，是以服务端下发的callId进行上报还是以我们拉起通知的callId去上报呢？请问callId是否支持用户自定义？

## 解决方案

* callId是应用内通话的唯一标识，支持应用自定义。
* 若服务端通过华为通道返回callId，必须使用服务端下发的callId进行后续操作。自定义callId会导致与华为服务端状态不一致，引发通话管理异常。
* 无论是服务端下发的callId还是应用自定义的callId，错误上报时必须使用最初调用reportIncomingCall时传入的callId。
