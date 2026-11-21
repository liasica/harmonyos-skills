---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:84649560d8356360e47c036ebd5865815127766d33428c099d17a760b2be1746
---

通用凭证为开发者提供了票券、会员卡、出行凭证等业务之外，没有明确且清晰业务划分的灵活选择，适用于预订凭证、行业资格证、服务预约单等多种场景。

该凭证支持标准的二维码展示与NFC能力，可将其保存至钱包，快速亮证核验通行。

通用凭证可帮助开发者以较低成本快速接入华为钱包，拓展更多垂直行业的电子化场景。用户将凭证保存至钱包后，不仅提升了使用粘性，也为开发者提供了持续触达用户的通道（如状态更新、服务提醒等），有助于提升服务完成率与用户复访意愿。

开发者可通过Wallet Kit快速接入通用凭证服务，商户可通过多种方式轻松将卡券集成到华为钱包中。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/R3nqWyPeQiykY7APy-Ck8w/zh-cn_image_0000002793038320.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=000773D263E9DDC8E8DF89845DC297BE6BB16548D97989441D49D03900C3AC5B)

| 角色 | 说明 |
| --- | --- |
| 开发者服务器 | 负责卡片管理的云侧实现。 |
| Wallet Kit服务器 | 提供服务器接口，用于开发者进行云云对接，推送卡片数据。 |
| 受理端POS | 提供扫码能力。 |
| 开发者客户端 | 负责卡片管理的端侧实现。 |
| 钱包App | 实现数字卡片业务能力。 |
| Wallet Kit框架 | 提供Wallet Kit对外接口。 |

## UI设计

### 通用凭证开通

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/4pmuThj3QqiuPkcRb0Sqnw/zh-cn_image_0000002792878372.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=17B695E16A296D4C7530CC8E839DDCB03E65D2F9DDB7DE046C54BD16992C714E)

### 通用凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/4Vz5_m4IS1i4we585Aab2g/zh-cn_image_0000002821838279.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=62AE6EBCA78E2F1C9E71259D3804F3AE6098A01450B0AA33D6663F6C737DFAC4)

## 接入流程

开发者可以参考以下接入流程，完成通用凭证业务相关准备及场景化能力开发。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 应用开发准备 | 请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置，再继续以下开发活动。 |
| 2 | 创建Wallet Kit服务 | 参考开发准备，[创建Wallet Kit服务](wallet-generalcard-prepare.md#创建wallet-kit服务)。 |
| 3 | 开通通用凭证 | 开通卡片，参考[开通通用凭证](wallet-generalcard-scene-open.md)章节。 |
| 4 | 查看通用凭证 | 查看卡片，参考[查看通用凭证](wallet-generalcard-scene-view.md)章节。 |
| 5 | 更新通用凭证 | 更新卡片，参考[更新通用凭证](wallet-generalcard-scene-update.md)章节。 |
| 6 | 删除通用凭证 | 删除卡片，参考[删除通用凭证](wallet-generalcard-scene-delete.md)章节。 |
