---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-update
title: 更新出行凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发场景 > 更新出行凭证
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:55f5927c5d679a0dd031dd28efe0e21bac6f3d3d15d91e3b5acb359406ceb9ce
---

当出行凭证信息发生变更时，如登机口变更、延误信息等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ngONvL1LRCqDcvAytUnUQg/zh-cn_image_0000002747292057.png)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[出行凭证数据更新](../harmonyos-references/wallet-rest-api-travel.md#出行凭证数据更新)，钱包服务端给钱包推送更新通知。
