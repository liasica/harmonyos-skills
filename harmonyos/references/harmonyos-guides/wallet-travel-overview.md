---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:32+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1f1734bd82bd3916d1f11ce3149981033d4b9c837ae7c045e67c3b50eb88ec0d
---

出行凭证即在用户购买机票或车票后所产生的电子乘车凭据，用户可在华为钱包中方便查看。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/fry52OGAQ1ikL_QzYFZJMw/zh-cn_image_0000002747211967.png)

| 角色 | 说明 |
| --- | --- |
| 开发者服务器 | 负责卡片管理的云侧实现。 |
| Wallet Kit服务器 | 提供服务器接口，用于开发者进行云云对接，推送卡片数据。 |
| 受理端POS | 提供扫码能力。 |
| 开发者客户端 | 负责卡片管理的端侧实现。 |
| 钱包App | 实现数字卡片业务能力。 |
| Wallet Kit框架 | 提供Wallet Kit对外接口。 |

## UI设计

### 出行凭证开通

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/1Ckn9acnToGOHuFH4aubtQ/zh-cn_image_0000002747292065.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ZV-AGK5HS5e7cCNfgaxpqA/zh-cn_image_0000002747211981.png)

### 出行凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/9r6OPgHPQqueFOzWIpOz2w/zh-cn_image_0000002717772046.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/AhqMiA0GSDaLiUUqveoc5Q/zh-cn_image_0000002717612114.png)

## 接入流程

开发者可以参考以下接入流程，完成出行凭证业务相关准备及场景化能力开发。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 应用开发准备 | 请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置，再继续以下开发活动。 |
| 2 | 创建Wallet Kit服务 | 参考开发准备，[创建Wallet Kit服务](wallet-travel-prepare.md#创建wallet-kit服务)。 |
| 3 | 开通出行凭证 | 开通卡片，参考[开通出行凭证](wallet-travel-scene-open.md)章节。 |
| 4 | 查看出行凭证 | 查看卡片，参考[查看出行凭证](wallet-travel-scene-view.md)章节。 |
| 5 | 更新出行凭证 | 更新卡片，参考[更新出行凭证](wallet-travel-scene-update.md)章节。 |
| 6 | 删除出行凭证 | 删除卡片，参考[删除出行凭证](wallet-travel-scene-delete.md)章节。 |
