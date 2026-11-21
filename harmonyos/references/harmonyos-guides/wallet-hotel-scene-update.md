---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-update
title: 更新酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 更新酒店房卡
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:16a28870eab9dbb8cdac5c5775d87c35458cc4bf1f58e3c785c58b0754284a63
---

当用户更换房间时，更新钱包中的房卡数据，自动同步为新房间号，无需重新开卡。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/H4wPQieZQqi-ev2MkoW5Xw/zh-cn_image_0000002792878362.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ED4EB73A5C6A4BB478D875E41DB251A48596C721D937E257549D158F012E093)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[酒店房卡检测更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡检测更新)（每日最多一次）。
2. 开发者服务器检测到变化，通知钱包服务器进行[酒店房卡数据更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡数据更新)。
