---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-update
title: 更新活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 更新活动/景点门票
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:154f54e050d815bba53503cdb6c3fc0c05167fa4b0d502e3858b2a725fdbc3ab
---

当门票信息发生变更时，如座位变更、入场提醒等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/WxBRRxq2SOmygsifx2T7mA/zh-cn_image_0000002815560059.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=083DB4E74DC846E18322C8994078F0C6A010867924DBFE4A3D2BB6054801F20C)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[活动/景点门票数据更新](../harmonyos-references/wallet-rest-api-ticket.md#门票数据更新)，钱包服务端给钱包推送更新通知。
