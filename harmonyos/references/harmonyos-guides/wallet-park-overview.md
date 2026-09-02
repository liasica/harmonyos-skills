---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 概述
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c975757917e524973f4657ed88ff750e380a5373391068a5fa028c59dd7b6d03
---

园区卡是华为钱包推出的面向企事业单位职员或学校学生的门禁解决方案，用户可将自己单位所属的入场凭证（如校园卡）等添加到华为钱包，并使用手机来通过单位门禁。

园区卡依托华为钱包行业标准卡集成方案，基于华为手机“芯-端-云”一体化的安全能力将一卡通模拟至华为钱包内。用户可通过网页、短信、Email、App等多种方式进行添加卡片操作。

## 系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/SqBF2I2WQSSckguVuTVB3A/zh-cn_image_0000002706675300.png)

| 角色 | 说明 |
| --- | --- |
| 园区卡后台服务 | 负责园区员工身份认证的云侧实现。 |
| Wallet Kit服务器 | 提供服务器接口，用于开发者进行云云对接，推送园区卡数据。 |
| 园区卡管理平台 | 负责园区卡的管理和发卡。 |
| 园区卡应用/元服务 | 负责园区员工身份认证的端侧实现。 |
| 钱包App | 实现园区卡业务能力，提供刷卡功能。 |
| Wallet Kit框架 | 提供Wallet Kit对外接口。 |
| Wallet Kit Applet | 安全存储园区卡数据，支持nfc刷卡。 |
| 园区卡闸机 | 作为园区门禁和消费受理端，和移动终端进行身份核验与支付扣款。 |

## UI设计

### 园区卡开通

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/8S41KfI5SWmADgaQXpSmlQ/zh-cn_image_0000002736434387.png)

### 园区卡展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/qqDrbJ9HQqqXXSleobvXww/zh-cn_image_0000002706835238.png)

## 接入流程

开发者可以参考以下接入流程，完成园区卡业务相关准备及场景化能力开发。

| 序号 | 步骤 | 说明 |
| --- | --- | --- |
| 1 | 应用开发准备 | 请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置，再继续以下开发活动。 |
| 2 | 创建Wallet Kit服务 | 参考开发准备，[创建Wallet Kit服务](wallet-park-prepare.md#创建wallet-kit服务)。 |
| 3 | 开通园区卡 | 开通卡片，参考[开通园区卡](wallet-park-scene-open.md)章节。 |
| 4 | 查看园区卡 | 查看卡片，参考[查看园区卡](wallet-park-scene-view.md)章节。 |
| 5 | 更新园区卡 | 更新卡片，参考[更新园区卡](wallet-park-scene-update.md)章节。 |
| 6 | 删除园区卡 | 删除卡片，参考[删除园区卡](wallet-park-scene-delete.md)章节。 |
| 7 | 生成展示二维码（可选） | 参考[生成展示二维码](wallet-park-scene-qr.md)章节。 |
