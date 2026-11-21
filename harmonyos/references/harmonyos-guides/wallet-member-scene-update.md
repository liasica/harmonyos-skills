---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-update
title: 更新会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 更新会员卡
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:9c652a73162f99884b03cd769dc7b2901bed80973f7b8f2017973bb2ba743402
---

当会员卡信息发生变更时，如会员信息修改、权益发生变更等，更新钱包中的会员卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/muFWa7WXQiageyT6QTvUDA/zh-cn_image_0000002821758263.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E4B2254B10DC579DA05186F43082A144C6D1C73D2A7AAC07327CD92E292315E)

## 服务端开发

开发者服务器通知钱包服务端进行[会员卡数据更新](../harmonyos-references/wallet-rest-api-member.md#会员卡数据更新)，钱包服务端给钱包推送更新通知。
