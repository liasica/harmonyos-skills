---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:15+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7adca61270c33e5ad27503add0e8b759a66a89a39f76ed77049c4b5d0d917da5
---

华为钱包将酒店房卡与会员卡合二为一。用户在线上领取会员卡，办理入住后自动激活房卡，手机轻碰门锁即可通行电梯、房门、洗衣房及健身房等场景。

对酒店而言，这一模式的价值在于：

* 入住前即可获客，即使宾客离店后仍可借会员卡持续触达用户，提升忠诚度。
* 入住后降本增效，减少实体制卡成本与前台人力，宾客体验也由此更加流畅、智能。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/RRbXEMPcQmibimkup4yBuA/zh-cn_image_0000002791566702.png?HW-CC-KV=V1&HW-CC-Date=20261119T014820Z&HW-CC-Expire=31536000000&HW-CC-Sign=020EB0C3458C04993CC83EAC48D8DFBCCBDC000794A2E7A1AF6E1D36834F4111)

| 角色 | 说明 |
| --- | --- |
| 酒店应用后台服务 | 负责酒店会员身份管理的云侧实现。 |
| Wallet Kit服务器 | 提供服务器接口，用于开发者进行云云对接，推送酒店房卡数据。 |
| 酒店PMS系统 | 负责酒店门锁钥匙的管理和发卡。 |
| 门锁管理系统 | 酒店门锁的边缘服务，负责门锁侧的钥匙管理。 |
| 酒店应用 | 负责酒店会员身份管理的端侧实现。 |
| 钱包App | 实现酒店房卡业务能力，提供刷卡开门、梯控等功能 |
| Wallet Kit框架 | 提供Wallet Kit对外接口。 |
| Wallet Kit Applet | 安全存储酒店房卡数据，支持nfc刷卡。 |
| 酒店卡闸机 | 作为酒店门禁，和移动终端进行身份核验。 |

## UI设计

### 酒店房卡开通

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ex3H0ivFSxKdGAkPIj0KGg/zh-cn_image_0000002820526655.png?HW-CC-KV=V1&HW-CC-Date=20261119T014820Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF5A1F50ECFE3E99B41712292DCBB468C2613951D6AA687D8E33561E762F8B1F)

### 酒店房卡展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/pn7W_KFuRHmLdRqTeb2xQQ/zh-cn_image_0000002820406655.png?HW-CC-KV=V1&HW-CC-Date=20261119T014820Z&HW-CC-Expire=31536000000&HW-CC-Sign=836A6E284767E5828797947E6028B1C1001530E6B6DED1E614F7A7B520DA707D)

### 酒店房卡更新

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/kytJq9-URHu948LV4DwYsg/zh-cn_image_0000002791726676.png?HW-CC-KV=V1&HW-CC-Date=20261119T014820Z&HW-CC-Expire=31536000000&HW-CC-Sign=8916ABAD963A88FE5EEC353D5325F175B4E354C937B9E1C262B8BD4A76B44A45)

## 接入流程

开发者可以参考以下接入流程，完成酒店房卡业务相关准备及场景化能力开发。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 应用开发准备 | 请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置，再继续以下开发活动。 |
| 2 | 创建Wallet Kit服务 | 参考开发准备，[创建Wallet Kit服务](wallet-hotel-prepare.md#创建wallet-kit服务)。 |
| 3 | 开通酒店房卡 | 开通卡片，参考[开通酒店房卡](wallet-hotel-scene-open.md)章节。 |
| 4 | 查看酒店房卡 | 查看卡片，参考[查看酒店房卡](wallet-hotel-scene-view.md)章节。 |
| 5 | 更新酒店房卡 | 更新卡片，参考[更新酒店房卡](wallet-hotel-scene-update.md)章节。 |
| 6 | 删除酒店房卡 | 删除卡片，参考[删除酒店房卡](wallet-hotel-scene-delete.md)章节。 |
