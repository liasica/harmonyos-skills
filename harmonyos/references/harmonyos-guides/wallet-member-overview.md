---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:aa855759a7015e629e6465988a99c735c898b42eb42d400cdfcb69d6378e4a23
---

各类实体会员卡添加至华为钱包后，不仅可随时查看积分、权益和品牌活动，还能第一时间接收商家推送的会员专属信息。这种便捷的触达方式，帮助商家持续与用户保持连接，有效提升会员活跃度与忠诚度。

开发者可通过Wallet Kit快速接入会员卡服务，商户可通过多种方式轻松将卡券集成到华为钱包中。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/pG9SM5Y9TwWl1lGieSc2QA/zh-cn_image_0000002793038320.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABA4D4AD66C1C0C0895AA79FFBEB3A4757724569EB4D7C2A10C64ADA1F4DEE56)

| 角色 | 说明 |
| --- | --- |
| 开发者服务器 | 负责卡片管理的云侧实现。 |
| Wallet Kit服务器 | 提供服务器接口，用于开发者进行云云对接，推送卡片数据。 |
| 受理端POS | 提供扫码能力。 |
| 开发者客户端 | 负责卡片管理的端侧实现。 |
| 钱包App | 实现数字卡片业务能力。 |
| Wallet Kit框架 | 提供Wallet Kit对外接口。 |

## UI设计

### 会员卡开通

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/BdJD7FSzQEqma-qGYG7f3g/zh-cn_image_0000002792878350.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC4447D237924840FABE2FAAC77FBBBD6873CB408F6C475FCC14E30BB979893A)

### 会员卡展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/T1vSQYvmR-KE8njvbi4B5A/zh-cn_image_0000002821838257.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B2E6E451049FC352234DA33A26F37F8DF48965647965B6FE575B54CB340A084)

## 接入流程

开发者可以参考以下接入流程，完成会员卡业务相关准备及场景化能力开发。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 应用开发准备 | 请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置，再继续以下开发活动。 |
| 2 | 创建Wallet Kit服务 | 参考开发准备，[创建Wallet Kit服务](wallet-member-prepare.md#创建wallet-kit服务)。 |
| 3 | 开通会员卡 | 开通卡片，参考[开通会员卡](wallet-member-scene-open.md)章节。 |
| 4 | 查看会员卡 | 查看卡片，参考[查看会员卡](wallet-member-scene-view.md)章节。 |
| 5 | 更新会员卡 | 更新卡片，参考[更新会员卡](wallet-member-scene-update.md)章节。 |
| 6 | 删除会员卡 | 删除卡片，参考[删除会员卡](wallet-member-scene-delete.md)章节。 |
