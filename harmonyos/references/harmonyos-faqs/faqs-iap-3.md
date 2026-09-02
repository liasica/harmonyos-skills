---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-3
title: 服务器关键事件消息通知常见问题及解决方案
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 服务器关键事件消息通知常见问题及解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3556d114b8ad036d9b9ab267e343340cf5f933357f60373ab4d28e83f125d9b7
---

## 问题现象

**问题1**：在测试用户订阅场景时，发现配置的接收通知服务器没有收到任何通知？

**问题2**：DID\_NEW\_TRANSACTION的DOWNGRADE类型中，如何理解什么是下个续订生效？

**问题3**：应用内支付服务，服务端关键事件通知，收到哪些事件时给用户发放、取消相应的权益，才能保证不多发、不少发？

**问题4**：服务器关键事件通知如何识别周订阅前三天免费取消订阅视为无收入订单？

**问题5**：对于应用内支付而言，应用客户端上报给应用服务器的到底是PurchaseData还是InAppPurchaseData？如果上报的是PurchaseData，没有purchaseState这个字段，这种情况下购买状态到底要如何判断？

## 背景知识

* [服务端关键事件通知](../harmonyos-references/iap-key-event-notifications.md)：建议所有提供消耗型/非消耗型/自动续期订阅/非续期订阅商品的App均配置该通知接收地址，以便接收关键事件通知，为用户提供更好、更及时的服务。另外，通知接收地址必须基于HTTPS并且配置有商业域名机构颁发的证书。
* 如果在AppGallery Connect申请支付服务时提前配置通知接收地址，并且通知版本设置为v3，用户购买消耗型/非消耗型/自动续期订阅/非续期订阅商品后，iap服务器会在某些关键事件发生时调用此接口通知已配置的服务器。详细信息参考：[配置订单/订阅通知接收地址](../harmonyos-guides/iap-set-necessary-parameters.md#配置订单订阅通知接收地址)。

## 解决方案

* **问题1**：在iap服务器查看日志显示报错信息为nested exception is javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake\_failure，即SSL握手失败，可以按照如下步骤进行排查：
  + 开发前需要在AppGallery Connect平台中配置订单/订阅通知接收地址，地址必须支持HTTPS协议且具有合法商用证书。
  + 出于安全考虑，cipher需要支持ECDHE-RSA-AES128-GCM-SHA256、ECDHE-ECDSA-AES128-GCM-SHA256、ECDHE-RSA-AES256-GCM-SHA384或ECDHE-ECDSA-AES256-GCM-SHA384中至少一种，否则无法正常接收通知消息。
  + 按照[接口约束](../harmonyos-references/iap-key-event-notifications.md#接口约束)，可以在支持的协议上增加TLSv1.3，加密套件可以选择上述列出的4种加密套件之一。
* **问题2**：如果当前用户订阅没过期，就是在下个周期生效，通知会发DID\_CHANGE\_RENEWAL\_STATUS的DOWNGRADE通知类型；当前权益过期了，就是立即生效，会发DID\_NEW\_TRANSACTION的DOWNGRADE类型。
* **问题3**：收到主类型DID\_NEW\_TRANSACTION子类型是INITIAL\_BUY和DID\_RENEW和RESTORE通知去查询订单信息，然后发放权益，收到REVOKE事件通知在到期后取消权益。不同的[NotificationType](../harmonyos-references/iap-key-event-notifications.md#notificationtype)和[NotificationSubtype](../harmonyos-references/iap-key-event-notifications.md#notificationsubtype)对应的是不同的类型，建议开发者根据返回的通知类型的说明去设计相应的处理机制。
* **问题4**：当用户取消订阅时，系统会发送“DID\_CHANGE\_RENEWAL\_STATUS”通知，并且在通知中会包含用户取消订阅的时间。开发者可以记录这个时间，并且和三天的促销优惠时间进行比较，如果用户之前取消订阅的话，那么可视为无效订单，如果之后取消订阅可视为无效订单。
* **问题5**：应用客户端上报给应用服务器的是PurchaseData，InAppPurchaseData只是购买数据模型，只有PurchaseData才包含具体的一笔订单的购买订单信息或者订阅状态信息。

  **说明** 

  purchaseState并不是一笔订单的购买状态，而是订单的最终的交易状态；在一笔订单支付完成后，还需要走发货流程，在发货成功后还需要应用客户端向iap Kit发送finishPurchase请求，这样才算整个购买流程结束。

## 常见FAQ

Q：iap服务器周期性重发的规则是什么样的？比如重发的间隔，次数限制，降级等约束。

A：限制是48小时内，间隔不是固定的，前面是秒级的，后面是小时级的。只要返回非200就会重发。

Q：在沙盒环境进行测试，但是实际需要真实支付是为什么？

A：debug包切换为Release包之后，手机进程缓存没有失效导致。切换debug包和Release包后，需确保进程缓存失效，比如锁屏5分钟或者重启。

Q：是否有工具或手段不走支付流程就能测试服务端通知？

A：有，可以通过[测试服务端通知](../harmonyos-references/iap-server-notifications-test.md)接口调用，可不走支付流程调测。

Q：应用内支付非消耗型数字商品是否需要服务器支持？

A：服务器部分是对应用内支付的订单有效性和支付结果进行校验，非消耗型的数字商品的购买流程完全可以在客户端完成，适用于对安全性要求较低的场景。

Q：自动续期订阅商品是否需要开发者在服务端记录到期时间，在商品临近续费时并发送提醒给用户？

A：不需要，HarmonyOS应用中的自动续期订阅商品会在临近续费时由支付的服务器短信进行通知。

Q：服务端关键事件通知，主通知类型有几类，分别对应那些子通知类型？

A：NotificationType字段表示是主通知，NotificationSubtype字段表示是子通知类型，具体可以看服务端关键事件通知文档的NotificationType和NotificationSubtype说明。

Q：应用内支付服务端开发相关的demo可以参考？

A：可以参考生成服务端请求的token文档中的[代码示例](../harmonyos-references/iap-jwt-description.md#代码示例)，提供了多种语言服务端开发的示例代码。
