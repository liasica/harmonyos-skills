---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-update
title: 更新出行凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发场景 > 更新出行凭证
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:45cb0199bb8185d90f0bdaa2c65b8fa97cd126e1ee85f31f9a30b688aa03cef0
---

当出行凭证信息发生变更时，如登机口变更、延误信息等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/x7lMjoApTByALdFg5etJ6A/zh-cn_image_0000002788308372.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=27D259A6F7B0490644D8C327CD96A6FC30DF234A17154B8587B921DC71F06C04)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[出行凭证数据更新](../harmonyos-references/wallet-rest-api-travel.md#出行凭证数据更新)，钱包服务端给钱包推送更新通知。
