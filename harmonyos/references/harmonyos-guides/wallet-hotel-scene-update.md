---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-update
title: 更新酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 更新酒店房卡
category: harmonyos-guides
scraped_at: 2026-11-04T08:30:46+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ce1853cfb6e61e3b5bf4dcc9c2b4fa517cb4b96b172b822fac4d7e5d04c06111
---

当用户更换房间时，更新钱包中的房卡数据，自动同步为新房间号，无需重新开卡。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/7WK_KLouTc2rcG149E8L3w/zh-cn_image_0000002809011341.png)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[酒店房卡检测更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡检测更新)（每日最多一次）。
2. 开发者服务器检测到变化，通知钱包服务器进行[酒店房卡数据更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡数据更新)。
