---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-9
title: 如何查询应用内支付交易后的订单信息
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 如何查询应用内支付交易后的订单信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f1f2abac3cbc8caa1387e20e8965d77d308204381c34ae6294b483f48e0a3d09
---

## 问题现象

应用中支付订单交易成功后，有哪些方式可以查询到订单信息？

## 背景知识

[收益分析和报告](../harmonyos-guides/iap-data-analysis.md)支持开发者通过[开发者联盟](https://developer.huawei.com/consumer/cn/)网站查询商品支付明细。

[查询用户的历史购买记录](../harmonyos-references/iap-order-info-query-by-order-history.md)、[应用购买记录相关支付订单查询](../harmonyos-references/iap-order-query.md)和[根据交易号查询订单状态信息](../harmonyos-references/iap-order-info-query-by-transaction-number.md)接口支持开发者在应用服务端通过接口请求方式获取订单信息。

## 解决方案

订单信息查询目前应用内支付服务提供两种方式查询：[开发者联盟](https://developer.huawei.com/consumer/cn/)网站查看报表和应用服务端接入相关API。

1. 登录[开发者联盟](https://developer.huawei.com/consumer/cn/)，进入“管理中心”，在“我的报表>支付报表”中可以查询到已售出的商品订单信息，通过该方式能直观的看到用户的支付金额、支付方式、订单状态和是否退款等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-jwQRD8DSfa3LJn4_u7TrQ/zh-cn_image_0000002628554464.png "点击放大")
2. 应用服务端查询订单信息，IAP KIT提供了三种API供开发者接入来查询对应的信息：
   * [查询用户的历史购买记录](../harmonyos-references/iap-order-info-query-by-order-history.md)：开发者可以通过此接口查询用户的历史购买记录，来判断是否给用户展示促销价格、是否已完成权益发放等场景。该方式支持开发者传入购买订单号purchaseOrderId后查询对应的购买记录，查询时间范围不超过365天。
   * [应用购买记录相关支付订单查询](../harmonyos-references/iap-order-query.md)：开发者可以通过查询指定时间范围内的付款和退款订单。该方式开发者仅需在应用购买记录相关支付订单查询接口的[Request Body](../harmonyos-references/iap-order-query.md#request-body)中传入startTime和endTime两个参数，接口请求成功后返回的orderInfoList中即可看到对应时间内的付款和退款订单。
   * [根据交易号查询订单状态信息](../harmonyos-references/iap-order-info-query-by-transaction-number.md)：此接口用于查询交易号对应的订单状态信息，适用于用户对订单信息有疑问向开发者求助的场景，开发者可以根据用户提供的交易号查询到对应订单信息。接口请求成功返回的jwsPurchaseOrder是已购订单相关状态信息的JWS格式数据，开发者需要[对返回结果验签](../harmonyos-references/iap-verifying-signature.md)处理，验签通过后解码获取相关订单状态信息。

     交易号可在用户设备的"设置"-"华为账号"-"付款与账单"-"购买记录"中对应订单详情中获取。

## 常见FAQ

Q：查询用户的历史购买记录接口在查询指定商品ID或者订阅组ID的历史购买记录时，最大支持查询多少个ID？

A：可以指定最多10个商品ID或者订阅组ID。

Q：应用购买记录相关支付订单查询接口获取当天订单信息不准确，是什么原因？

A：当天的订单信息可能还会发生变动，因此不建议使用此接口查询当天的实时订单数据，建议延迟一天查询。

Q：应用购买记录相关支付订单查询接口startTime和endTime使用注意点有哪些？

A：格式固定为13位的UTC时间戳，以毫秒为单位。

* 若startTime未指定，取值如下：指定endTime，startTime取值为：endTime-365天。未指定endTime，startTime取值为：当前时间-365天。
* 若endTime未指定，取值如下：指定startTime，endTime取值为：startTime+365天，但不会早于当前时刻。未指定startTime，endTime取值为：当前时间。

Q：应用服务端方式查询订单信息能查询多久的订单，任何订单都可以查询么？

A：应用购买记录相关支付订单查询方式支持查询到半年内的订单，根据交易号查询订单状态信息方式支持查询一年内的订单，查询用户的历史购买记录方式支持查询7年内的订单，三种查询方法均不支持查询沙盒测试订单。
