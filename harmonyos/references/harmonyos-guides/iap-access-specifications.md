---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-access-specifications
title: IAP Kit接入规范
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit接入规范
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:15fd174280f9b027356f9f9bb360f6c3537b41265015ac5cf5deab11667f9423
---

为了确保用户获得良好的支付体验，IAP Kit制定了应用接入IAP Kit的设计规范，请开发者遵照执行，否则可能影响应用上架。具体要求如下：

## 界面设计规范

1. 请不要在应用商品购买页展示支付方式栏目信息，包括支付方式logo、支付方式名称（如“华为支付”、“鸿蒙支付”、“应用内支付”等）等信息。建议采用购买、订阅等按钮确认用户购买或订阅意愿。用户点击按钮确认购买或订阅意愿后，应用直接拉起IAP Kit收银台完成购买流程。
2. 建议应用在商品购买页拉起IAP Kit收银台时，展示加载动效，保证应用购买的流畅性，提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/FGxdwCQ_QZWd33GID9_kPg/zh-cn_image_0000002552799272.png?HW-CC-KV=V1&HW-CC-Date=20260427T234922Z&HW-CC-Expire=86400&HW-CC-Sign=6A64BCF5FFC96C548A651AD9877876FD2EA5DC20FA989DF702A0F479B45E1ABD)

## 接入限制

数字商品（虚拟商品）要求通过IAP Kit接入购买能力，不能独立对接支付宝、微信支付等三方支付，否则可能影响应用上架。
