---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-2
title: 应用如何接入退款及常见问题
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 应用如何接入退款及常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e2b5ed285c2b8ab10a0c4b1f94e738f9d643317612883a1b6e67c9fdb08a70dd
---

## 问题现象

1. 用户购买虚拟数字商品后需要退款如何申请，开发者可以在哪儿处理退款申请，整个IAP退款的流程是怎样的？
2. 开发者如何在应用内接入退款入口以及用户申请退款后服务器是否会收到退款相关的事件通知？
3. 沙盒环境下，发起退款申请，服务端接收不到退款申请事件通知仅有退款成功事件通知？
4. 应用的用户发起退款申请后，如何核对退款金额，是否有可以查询退款金额的方式？
5. 用户退款申请通过并成功退款后，应用服务端未收到退款成功回调，如何解决？

## 背景知识

* 退款主要分为两部分：[开发者审核退款订单](../harmonyos-guides/iap-refund.md#开发者审核退款订单)和[用户申请退款](../harmonyos-guides/iap-refund.md#用户申请退款)。
* [应用内接入退款入口](../harmonyos-guides/iap-refund.md#应用内接入退款入口)：应用中通过接口的方式拉起退款界面，仅支持非游戏类应用接入和应用本身所产生的订单的退款。
* [接收退款申请事件通知](../harmonyos-references/iap-server-refund-receive-notify.md)：用户申请退款时，IAP服务器调用此接口向开发者服务器发送退款审核事件通知。

## 解决方案

1. 用户和开发者可以分别通过如下的途径去申请和处理退款：

   用户侧：

   * IAP订单退款设备侧操作入口：设置-华为账号-付款与账单-购买记录-详情-对订单有疑问-申请退款；
   * 或者通过设置-华为账号-付款与账单-帮助和反馈，通过客服申请退款。开发者侧：
   * 开发者登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“App与元服务”，在“运营”页签下，点击“产品运营>退款管理”，查看用户提交的退款申请，处理退款订单，退款申请后到退款完成非实时，一般从发起申请退款到完成需要7个工作日左右。

2. 用户发起退款后，应用客户端可以调用[iap.createRefundRequest](../harmonyos-references/iap-iap.md#iapcreaterefundrequest)接口传入退款的订单号从而拉起退款页面完成退款申请。同时开发者服务器会收到[NotificationType](../harmonyos-references/iap-key-event-notifications.md#notificationtype)对应字段是：REVOKE的退款事件通知，完成退款后则会收到[NotificationSubtype](../harmonyos-references/iap-key-event-notifications.md#notificationsubtype)对应字段是REFUND\_TRANSACTION的退款成功事件通知。
3. 沙盒环境下订单退款不支持退款申请事件通知，用户提交退款请求后，IAP会跳过退款审核流程，直接完成退款，同时给开发者服务器发送[NotificationSubtype](../harmonyos-references/iap-key-event-notifications.md#notificationsubtype)对应字段是REFUND\_TRANSACTION的退款成功事件通知。
4. IAP提供了两种方式让开发者来查询到用户退款相关信息：
   * 服务端API查询：用户申请退款后，IAP服务器会向开发者服务器发起请求，请求中会携带[RefundRequestData](../harmonyos-references/iap-server-refund-receive-notify.md#refundrequestdata)结构体，该结构体中的applyAmount字段就说明了用户申请的退款金额（单位：分），除此外还有refundReason（用户申请退款理由）和refundOrders（退款申请工单下的订单号）等参数。
   * AGC管理台查询退款信息：开发者登录AppGallery Connect，选择“App与元服务”，在“运营”页签下，点击“产品运营>退款管理”，查看用户提交的退款申请，处理退款订单。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/2TLUiP6RTNCsIf4F7yaq_Q/zh-cn_image_0000002654410216.png "点击放大")

5. 检查开发者在AppGallery Connect配置的通知版本是否设置为v3，配置的接收退款申请事件通知服务器地址是否有修改、变更等情形，有变动可以通过[测试服务通知](../harmonyos-references/iap-server-notifications-test.md)验证是否可以调用成功，除此外https证书失效或者不符合要求也会出现该问题。

## 常见FAQ

Q：消耗型商品是否可以退款？

A：可以的，虚拟数字商品退款不限制商品类型。

Q：订阅商品升级购买后，产生多笔订单，订单申请退款，退款逻辑是怎么样的？

A：按照每笔订单金额申请退款，审核通过后，将按开发者输入退款金额（小于等于订单金额）退至用户账户。

Q："返回退款审核结果"接口和"处理退款订单"功能是什么关系，用户申请了退款，AGC管理界面上操作退款审核了，还需要再通过接口通知华为的IAP服务器吗？

A：需要的，审核同意退款后，华为财务系统会发起原路退回款项流程，但是款项不会实时退回给用户，请勿在审核退款后直接回收用户权益，具体的权益回收时间建议以华为服务器发送的订单退款/撤销订阅事件通知为准。

Q：华为开发者账号登录AppGallery Connect管理台后看不到退款管理功能，如何解决？

A：开发者使用退款管理功能，需要拥有至少一个具备退款权限的角色：账号持有者、管理员、App管理员、财务。具体可查看[添加成员账号](../app/agc-help-manageaccount-0000001099996700.md#section151241455193313)。

Q：用户通过客服进线申请退款，开发者服务端是否会收到退款申请事件通知？

A：不会。用户通过客服进线（即人工退款）进行退款时，不会向开发者服务端发送退款申请事件通知，而是通过发送退款邮件与开发者确认是否同意退款。如开发者同意退款，再进行人工退款处理。正常退款申请通知通常在用户提交退款申请后很快推送，基本为分钟级。
