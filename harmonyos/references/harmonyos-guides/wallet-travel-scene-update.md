---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-update
title: 更新出行凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发场景 > 更新出行凭证
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c91d83b7b996cdea9ae5a691d7d8b9c3706756f0832a7a01bacdc0242b8118c1
---

当出行凭证信息发生变更时，如登机口变更、延误信息等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/poJqSsYqTT2e9CrtMyYVaw/zh-cn_image_0000002706675314.png)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[出行凭证数据更新](../harmonyos-references/wallet-rest-api-travel.md#出行凭证数据更新)，钱包服务端给钱包推送更新通知。
