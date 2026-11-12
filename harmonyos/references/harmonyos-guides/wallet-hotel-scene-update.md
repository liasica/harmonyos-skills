---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-update
title: 更新酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 更新酒店房卡
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:71cc33f8aa2b4e1687b1723ec13b5223398cd84098623a99f0bbae0f64a5c7d7
---

当用户更换房间时，更新钱包中的房卡数据，自动同步为新房间号，无需重新开卡。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Df2YC1MlR2G0MfIY5zddew/zh-cn_image_0000002786520574.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F39F9433673BBC3C5A7EC2C639003FA2E4D5588563D118A60590C92C4941D046)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[酒店房卡检测更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡检测更新)（每日最多一次）。
2. 开发者服务器检测到变化，通知钱包服务器进行[酒店房卡数据更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡数据更新)。
