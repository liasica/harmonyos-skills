---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 概述
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:eb348f9e219d8e3510935cfb4ce7f56a82290c125dd29cd813614c9f4d3ead76
---

活动/景点门票即为特定活动（如比赛，演唱会等）或景点所制作的电子入场凭证，用户通过活动/景点门票可以在手机上进行快速验票，以提升验票体验、活动运营效率及服务满意度。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/t29QFk5TR3id-Gku_F6GIA/zh-cn_image_0000002736434395.png)

| 角色 | 说明 |
| --- | --- |
| 开发者服务器 | 负责卡片管理的云侧实现。 |
| Wallet Kit服务器 | 提供服务器接口，用于开发者进行云云对接，推送卡片数据。 |
| 受理端POS | 提供扫码能力。 |
| 开发者客户端 | 负责卡片管理的端侧实现。 |
| 钱包App | 实现数字卡片业务能力。 |
| Wallet Kit框架 | 提供Wallet Kit对外接口。 |

## UI设计

### 活动/景点门票开通

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/SycswrprTKKU2ICuPNuKLw/zh-cn_image_0000002736434415.png)

### 活动/景点门票展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/AIL0V8wZQeGFqrckvFECcg/zh-cn_image_0000002706835266.png)

## 接入流程

开发者可以参考以下接入流程，完成活动/景点门票业务相关准备及场景化能力开发。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 应用开发准备 | 请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置，再继续以下开发活动。 |
| 2 | 创建Wallet Kit服务 | 参考开发准备，[创建Wallet Kit服务](wallet-ticket-prepare.md#创建wallet-kit服务)。 |
| 3 | 开通活动/景点门票 | 开通卡片，参考[开通活动/景点门票](wallet-ticket-scene-open.md)章节。 |
| 4 | 查看活动/景点门票 | 查看卡片，参考[查看活动/景点门票](wallet-ticket-scene-view.md)章节。 |
| 5 | 更新活动/景点门票 | 更新卡片，参考[更新活动/景点门票](wallet-ticket-scene-update.md)章节。 |
| 6 | 删除活动/景点门票 | 删除卡片，参考[删除活动/景点门票](wallet-ticket-scene-delete.md)章节。 |
