---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-set-necessary-parameters
title: （可选）配置应用内购买服务参数
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 基本准备工作 > （可选）配置应用内购买服务参数
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:95041822d8d89ef2cf6d8ea8999412d1156f7a7a371a98a663fb35486472850e
---

## 配置订单/订阅通知接收地址

IAP服务器支持[服务端关键事件通知](../harmonyos-references/iap-key-event-notifications.md)的能力。用户购买商品后，IAP服务器会在订单（消耗型/非消耗型商品）和订阅场景的某些关键事件发生时发送通知至开发者配置的订单/订阅通知接收地址，具体的通知接收地址配置请参见[激活服务和配置事件通知](../app/parameters-0000001931995692.md)。

## 配置密钥

IAP服务器要求对每个服务端API请求进行JSON Web Token（JWT）授权。开发者可以使用从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)下载的API密钥对Token签名生成JWT，授权发起的服务端API请求。

开发者可参见[创建密钥](../app/key-0000001959074877.md)、[下载密钥](../app/download-0000001958955101.md)、[撤销密钥](../app/cancel-0000001931995696.md)管理服务端密钥。
