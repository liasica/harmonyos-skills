---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 概述
category: harmonyos-guides
scraped_at: 2026-10-17T06:42:46+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1ad61045ba8c0cc60faf07bc947c2e9688bcc0ebb07c29fb2e67331fcb2c14b4
---

出行凭证即在用户购买机票或车票后所产生的电子乘车凭据，用户可在华为钱包中方便查看。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/GepT52f0THeL-HEJHIf8DQ/zh-cn_image_0000002794491519.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/otV2IuSiTrarXw4AUNJFWg/zh-cn_image_0000002765132954.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/xsb1IgSlTu6fMQJRb7aj6Q/zh-cn_image_0000002794491533.png)

### 出行凭证展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/37UcmAJ9Q1ar3TV7Y0uWCg/zh-cn_image_0000002794411753.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/leIY046yQfK6mtBT6ydHZA/zh-cn_image_0000002764973034.png)

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
