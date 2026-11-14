---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-update
title: 更新酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 更新酒店房卡
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5194bc017aaa43437e04933be2c4a8aa5ab827a7f25a3da4855aee217a82664c
---

当用户更换房间时，更新钱包中的房卡数据，自动同步为新房间号，无需重新开卡。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/8d5rHhD5SAGU4Dmxj8t-MQ/zh-cn_image_0000002788468322.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC0712461E7D80BD5736DF73C33E5C03D9A081F52FDC85C9DB5F118BFD3B121D)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[酒店房卡检测更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡检测更新)（每日最多一次）。
2. 开发者服务器检测到变化，通知钱包服务器进行[酒店房卡数据更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡数据更新)。
