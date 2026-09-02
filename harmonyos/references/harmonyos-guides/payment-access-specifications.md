---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-access-specifications
title: 接入规范学习
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 接入规范学习
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:516522b5ad150e91f699b2c303be1706387620462d23d45325a2e3feb87b632f
---

为了确保用户获得良好的支付体验，Payment Kit制定了相关接入规范，请开发者遵照执行，具体要求（非强制性）如下：

## 支付方式呈现

1. 涉及支付公司名称，请统一使用：**花瓣支付（深圳）有限公司**。
2. 涉及支付方式说明（如涉及根据系统语言环境做国际化，也请对该支付方式说明一并做处理），请统一使用：**华为支付（中文）**、**Huawei Pay（英文）**。
3. 华为支付提供了支付图标设计规范，以此保证用户在使用华为支付时拥有一致的支付视觉体验，有关设计规范请参阅[华为支付设计规范](../design-guides/huaweipay-0000002054558905.md)。
4. 华为支付logo资源可[在此下载](https://developer.huawei.com/consumer/cn/design/resource/)。

## 支付体验要求

1. 建议在应用的订单页或支付页内直接拉起华为支付收银台，不建议跳转空白页拉起收银台。
2. 商户收银台展示数字人民币支付入口时，需与其他支付App在同一层级，建议不要隐藏数字人民币支付入口或满足一定条件后才在收银台页面展示。具体参考如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/8U46RmqsThieL1e7f37TAA/zh-cn_image_0000002736434247.png)
