---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-2
title: 关于云侧接口推送成功但设备收不到推送消息的问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 关于云侧接口推送成功但设备收不到推送消息的问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:52b8a73d847cc0cbcfe59c6717e60bf60323546599c51384de37304f2c88a003
---

云侧消息下发成功后，可能会因为消息频控、通知开关未打开等原因，导致端侧消息未展示。

## 收不到推送消息的可能原因

* 消息被频控，请检查是否[开通消息自分类权益](push-send-alert.md#开通权益)。调测阶段建议发送测试消息，详情请参见[关于通知消息被频控的问题](push-faq-5.md)。
* 终端设备的网络连接异常。如终端设备切到测试环境，且未连接外部网络。
* 终端的通知开关关闭。
* 使用的Push Token已经失效，如应用已卸载，未安装等（Push Token失效原因请参见[场景介绍](push-get-token.md#场景介绍)），请重新生成Push Token发送消息。
* 应用在前台，推送的是语音播报消息（[push-type](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)为2）。请将应用切至后台重新推送语音播报消息，或重新推送普通通知消息（push-type字段设置为0）。
* skills标签配置问题，正确的配置方法请参见[点击消息动作](push-send-alert.md#点击消息动作)。
* 检查消息是否是静默通知。发送了资讯营销类的消息，或是未申请自分类权益，都会静默通知。当收到消息时，由于静默通知仅在通知中心展示，并不会锁屏和横幅通知、响铃和振动，需要去通知中心查看。

## 如何定位此类问题

1. Push Kit建议您[开发消息回执](push-msg-receipt.md)，Push服务端会将消息送达状态以回执消息形式发送给您的应用回执服务端，您可通过[回执状态码](push-msg-receipt.md#回执状态码)定位问题。
2. 您还可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)进行消息追踪和token信息查询，查询路径：“开发与服务 > 增长 > 推送服务 > 自助分析（Beta）”。
