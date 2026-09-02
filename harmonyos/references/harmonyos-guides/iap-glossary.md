---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-glossary
title: IAP Kit术语
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:28+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:ff34e9b07043fa02ab18af2f40773943263b89083d3b4ad448c53eeb41964b17
---

## C

**Checkout Screen; 收银台**

IAP Kit提供的支付确认页面，展示商品名称、价格等信息，用户在此完成支付。收银台由IAP Kit系统级页面提供，开发者无法自定义样式。

## E

**Embedded Cashier Component; 嵌入式收银台**

IAP Kit提供的一种可以内嵌在开发者页面的收银台组件。

## J

**JSON Web Signature(JWS); JSON Web签名**

用于传输购买结果的加密数据格式，包含订单信息的签名数据。开发者需对JWS数据进行解码验签以验证购买结果的真实性。

## O

**Order Loss; 掉单**

由于网络错误或进程被中止等原因，应用无法确认用户是否实际支付成功，从而导致权益未能及时发放。

## T

**Time Machine; 时光机**

沙盒环境下订阅续订时间加速概念，订阅换算时间为10秒/天，用于快速测试订阅续期场景。例如1周订阅在70秒后会发生续期。
