---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-6
title: 如何判断APP是用户通过点击通知栏推送而唤起的？
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 如何判断APP是用户通过点击通知栏推送而唤起的？
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9a7b5e393847ade73ca19649ad10792719f4fd03182fc42b110551afd61d0332
---

## 问题现象

以前通过判断ohos.aafwk.param.callerBundleName参数中的值是否为com.huawei.hms.pushservice来判断是否通过点击离线推送消息唤起，目前系统该字段参数变成com.ohos.sceneboard，导致判断失效。如何准确判断用户是通过点击离线推送消息唤起了APP？

## 解决方案

应用服务端调用Push Kit服务端的REST API推送通知消息时，可携带data字段，当用户点击消息时将传递数据至客户端应用。通过获取传递参数确认是否是通过点击通知栏推送唤起的应用。参考文档：[数据传递](../harmonyos-guides/push-send-alert.md#数据传递)。
