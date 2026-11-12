---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:963bd3d6b7a886e91f4863f20d8e9896363a922e36449b599f9263930a98bda2
---

出行凭证即在用户购买机票或车票后所产生的电子乘车凭据，用户可在华为钱包中方便查看。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/R0rBodhiSzueK985LGmWNQ/zh-cn_image_0000002815400137.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2B732147394C8B15460A68F60F3ED0F1134938941AF3ECCC4B86AC958FB02AE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/8CbhkAa6RuSXinhMH9wL9w/zh-cn_image_0000002815560067.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDBDDD9B18C1D6336769667B36746155425D2F8025D3BB126E65EDC4317117E7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/wAoBjVfITPWwrHf3lG4wfg/zh-cn_image_0000002815400151.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0342DDF5C2E2F63E24365807757BCC83B4EFF14AC849C43EAFC207975364316)

### 出行凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/XzPXqOrmRXOP6ATdTaeI3g/zh-cn_image_0000002786520576.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=686C516E96B48109153B5DC4732BC801AF4F52EBE2C8298414D2085C308F4B3E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/_MPaFrefR0SH8pIuBAZ9Qg/zh-cn_image_0000002786360648.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B5A8E45E9A48543BF346D671A604A70239E7B82350E45D33133E2834C82C42D)

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
