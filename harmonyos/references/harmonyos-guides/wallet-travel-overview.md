---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:15+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b51e5c1f85e619861d9061a31ee8e5ef374b890ca64cbc9e49bfee70574af53e
---

出行凭证即在用户购买机票或车票后所产生的电子乘车凭据，用户可在华为钱包中方便查看。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/7Q-6ZwndRNyh3_1MG20-hA/zh-cn_image_0000002791726668.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0CE17E0AB4FD44E4E3C2014D792CCF0341335890979F05628BFB32691CEB0D5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/EfjqEAewQz2H1YOA9BvvAA/zh-cn_image_0000002820406661.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=83197AAE49C671E7BA36B37675F695D3971FA303AAAFF89AA1B1419FBA28DD43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/rvx_FYblTua3bhOwRLHiBw/zh-cn_image_0000002791726682.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=A06A0172FEAFD96AC389B47C34998669BE6C0ED969DC838BF633B4C50E390192)

### 出行凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/lsjTrOPbQmOhCpdGAhih9g/zh-cn_image_0000002791566710.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=25A2F055B9102B3BF72A93D99BD02524BC3FC6E8FF833E639DC930C8C1EB08C5)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/CUh7NlxtSjmEGIaqPXo54g/zh-cn_image_0000002820526663.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D33C1ACBFEA07EE5E0EDC62E48A78A7E00AC32090CD675EFEA02382E2276CA9)

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
