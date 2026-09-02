---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-7
title: Push Kit消息缓存时间
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > Push Kit消息缓存时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:8fc764132fa7ba0d318a9f71193ea4f13d76f9c1c38a24123518c1d1a2516fb8
---

## 问题现象

Push Kit在接收方因各种原因无法收到应用消息时，应用消息可以缓存多长时间？

## 解决方案

Push Kit接收方无法收到消息分两种情况：

1. 如果接收端的设备离线，导致消息重新发送到接收端设备，则应用消息最多可以在Push Kit服务器侧缓存15天，该缓存时间可以在[pushOptions](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)中由ttl参数定义。
2. 如果接收端设备在线，但是应用不在前台，导致[推送后台消息](../harmonyos-guides/push-background.md)时无法推送至应用，则该消息会缓存至端侧，最多可缓存7天。
