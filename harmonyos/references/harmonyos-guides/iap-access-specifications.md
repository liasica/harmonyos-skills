---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-access-specifications
title: IAP Kit接入规范
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit接入规范
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0a6b3801e231140cd2080c7d7e70043185cc848e4397f027bee59db89977838
---

为了确保用户获得良好的支付体验，IAP Kit制定了应用接入IAP Kit的设计规范，请开发者遵照执行，否则可能影响应用上架。具体要求如下：

## 界面设计规范

1. 请不要在应用商品购买页展示支付方式栏目信息，包括支付方式logo、支付方式名称（如“华为支付”、“鸿蒙支付”、“应用内支付”等）等信息。建议采用购买、订阅等按钮确认用户购买或订阅意愿。用户点击按钮确认购买或订阅意愿后，应用直接拉起IAP Kit收银台完成购买流程。
2. 建议应用在商品购买页拉起IAP Kit收银台时，展示加载动效，保证应用购买的流畅性，提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/_nuQUc2uSGiW9FkRpaJtFw/zh-cn_image_0000002589325291.png?HW-CC-KV=V1&HW-CC-Date=20260429T053832Z&HW-CC-Expire=86400&HW-CC-Sign=7552234FE970C1F203B0BB4C98055C099C8EC739102B8EB33C267C0F35046FB9)

## 接入限制

数字商品（虚拟商品）要求通过IAP Kit接入购买能力，不能独立对接支付宝、微信支付等三方支付，否则可能影响应用上架。
