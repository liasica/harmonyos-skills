---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3c1d08aff2eb168562712ef797a2202179f223385d25d945e95a42c783bb2d7c
---

出行凭证即在用户购买机票或车票后所产生的电子乘车凭据，用户可在华为钱包中方便查看。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ql8ZtEQrQ7eV2eD--_z5TA/zh-cn_image_0000002817427729.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=46A9EF9B43E23F6BD2D58A65C9B610151732805D951C04D18DE64FD764A287D1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/_k1oYtA3S3apXsmdkmkWNw/zh-cn_image_0000002788308380.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=D460F7014D3142C6449917A33C817891F0A87AB77749A7D910DB5FD1C29995F4)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/zFpHDiesRL-KXzLO0T-l-A/zh-cn_image_0000002817427743.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DA2E8628265A5A9286FF4B694C40A5764081487612DD384F41FE9D36AB861B2)

### 出行凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/NKBvjrC4Qj6US_SVg_5NLQ/zh-cn_image_0000002788468324.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=B71B0016B62BD8BFA9E1C6573C59C6A627B7C1A68FECE0EA42492919E35D2471)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/LGFi_eWdRseTl1OvRpSwFw/zh-cn_image_0000002817507813.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5F509076893A96D3A91D81C8081017BA410E6EB462E75C85C1298C871915AFB)

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
