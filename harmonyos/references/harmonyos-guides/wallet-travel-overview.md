---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f600aa83a60a5e5e24ac07893255aa41359cef65a95343d041c48113909273c8
---

出行凭证即在用户购买机票或车票后所产生的电子乘车凭据，用户可在华为钱包中方便查看。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/AKxEukbtSCikh_C6g3K0Aw/zh-cn_image_0000002793038320.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=50BE388BEE6E85A859694E7553243A99104B8D9FBDB343DE1F536781FB8C5D53)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/W0BNoqkGTz2-Xbn7NUW-gg/zh-cn_image_0000002821758271.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=457FF2F29C239C5DA49345BE8D23EBC026AFB17B35A07CB317C08D509C875768)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/CEaSJSbuQaeys9Uj0nZrKA/zh-cn_image_0000002793038334.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=685B23DF78203F4248F58B8C2D57BB5C28377E416A24243E176B38D3339CF91D)

### 出行凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/EiRy0Xt7QdaS1rxsno6sWg/zh-cn_image_0000002792878364.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F7D0FEF41C529BBE1AAC5C40AC92BF34F78725A1ACAFD03B22E5C67A0C49752)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/v5FPE-S2R1OWwqihl0xULA/zh-cn_image_0000002821838271.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8834A63D21EEBAF7AB940E998D0D8A9C0EF0C88CB5478B2EDB4E691E5560AA5)

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
