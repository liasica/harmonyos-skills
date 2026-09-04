---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 概述
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:060e63da3f0426d85507990895576dc2a7d131de6b948b094aa932b94af522c5
---

各类实体会员卡添加至华为钱包后，不仅可随时查看积分、权益和品牌活动，还能第一时间接收商家推送的会员专属信息。这种便捷的触达方式，帮助商家持续与用户保持连接，有效提升会员活跃度与忠诚度。

开发者可通过Wallet Kit快速接入会员卡服务，商户可通过多种方式轻松将卡券集成到华为钱包中。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/SiWmJxgcTtC77K8t-9oNvA/zh-cn_image_0000002742124395.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/8SfRGwVvQguWoRs_UZ0Pig/zh-cn_image_0000002712245488.png)

### 会员卡展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/gXoUy5VXTJGXhpqXDynQaQ/zh-cn_image_0000002742004437.png)

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
