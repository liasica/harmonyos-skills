---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-update
title: 更新活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 更新活动/景点门票
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4b35c8a2a2303944b82ad57ad3558b6db3d5e13de2558ebff523c09a534c76be
---

当门票信息发生变更时，如座位变更、入场提醒等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/G8m7MQ22Qg2CZZsOkH1pfQ/zh-cn_image_0000002788308372.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=589C8179A9E8EDA12619679FD5742B2994B46CADBD96467CE635B453615E0E93)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[活动/景点门票数据更新](../harmonyos-references/wallet-rest-api-ticket.md#门票数据更新)，钱包服务端给钱包推送更新通知。
